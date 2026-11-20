#!/usr/bin/env python3
"""Update the road-conditions data for the Death Valley + Joshua Tree trip site.

Sources (all official NPS, no API key needed):
  - Per-park alerts JSON that the NPS website itself loads for its Alerts
    section: https://www.nps.gov/<code>/park-alerts-<code>.json
  - Mojave's "Primary Roads" table on its conditions page
    (Death Valley's road status lives in an interactive map, and Joshua Tree
    has no road-status table, so those two parks get alerts only).

Filters:
  - Road-relevant only (road / closure / construction / detour / flood /
    washout / debris / highway / entrance / access, or a road-closure event).
  - Drops alerts that already ended before the trip starts (2026-12-17);
    alerts with no end date are treated as ongoing and kept.

Output: _data/road_conditions.json (read by the "Road conditions" section in
index.md via Jekyll/Liquid). Run daily by the GitHub Actions workflow
.github/workflows/update-road-conditions.yml; also runnable by hand:
    python3 scripts/update_road_conditions.py
"""
import json
import re
import sys
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "_data" / "road_conditions.json"
TRIP_START = datetime(2026, 12, 17, tzinfo=ZoneInfo("America/Chicago"))
UA = {"User-Agent": "Mozilla/5.0 (compatible; TripPlanner/1.0; road-conditions updater)"}

PARKS = [
    {"code": "deva", "name": "Death Valley National Park",
     "url": "https://www.nps.gov/deva/planyourvisit/conditions.htm"},
    {"code": "moja", "name": "Mojave National Preserve",
     "url": "https://www.nps.gov/moja/planyourvisit/conditions.htm"},
    {"code": "jotr", "name": "Joshua Tree National Park",
     "url": "https://www.nps.gov/jotr/planyourvisit/conditions.htm"},
]

ROAD_WORDS = re.compile(
    r"road|highway|entrance|detour|route|bridge|\bpass\b|"
    r"kelbaker|badwater|artists drive|titus|geology tour|covington flats",
    re.IGNORECASE,
)


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def parse_nps_date(s):
    """NPS dates look like 'June, 28 2026 12:00:00' (or '')."""
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%B, %d %Y %H:%M:%S", "%B %d, %Y %H:%M:%S", "%B, %d %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=ZoneInfo("America/Chicago"))
        except ValueError:
            continue
    return None


def road_relevant(a):
    if (a.get("road_closure_event_type") or "no").lower() != "no":
        return True
    title = a.get("title", "")
    # A trail/site closure with no road in it is not a road condition.
    if re.search(r"trail", title, re.I) and not re.search(r"road", title, re.I):
        return False
    text = " ".join([
        title, a.get("description", ""),
        a.get("road_closure_name", ""), a.get("road_closure_description", ""),
    ])
    return bool(ROAD_WORDS.search(text))


def filter_alerts(alerts):
    kept = []
    for a in alerts:
        if not road_relevant(a):
            continue
        end = parse_nps_date(a.get("end_date") or a.get("road_closure_end_date"))
        if end is not None and end < TRIP_START:
            continue  # already over before the trip starts
        kept.append({
            "title": (a.get("title") or "").strip(),
            "category": (a.get("category") or "").strip(),
            "description": re.sub(r"\s+", " ", (a.get("description") or "").strip()),
        })
    return kept


def clean_html(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def split_cell(html):
    """Split a table cell on <br> into cleaned, non-empty parts."""
    return [clean_html(p) for p in re.split(r"<br\s*/?>", html or "")
            if clean_html(p)]


def moja_roads(html):
    """Parse Mojave's 'Primary Roads' table: Road | Status | Notes.

    One row (Kelbaker) packs two segments in a single row — North (OPEN)
    and South (CLOSED) — separated by <br>; split those into two entries.
    """
    m = re.search(r"Primary Roads.*?<table.*?</table>", html, re.S | re.I)
    if not m:
        return []
    rows = []
    for rm in re.finditer(r"<tr>(.*?)</tr>", m.group(0), re.S | re.I):
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", rm.group(1), re.S | re.I)
        if len(cells) < 3 or clean_html(cells[0]).strip() == "Road":
            continue  # header row (exact match — road names contain "Road" too)
        segments = split_cell(cells[0])
        # Status words (OPEN / CLOSED) in order, ignoring "Caution".
        statuses = re.findall(r"\b(OPEN|Closed|CLOSED)\b", cells[1])
        caution = bool(re.search(r"caution", cells[1], re.I))
        notes_parts = split_cell(cells[2])
        full_notes = clean_html(cells[2])
        if len(segments) > 1 and len(statuses) == len(segments):
            for i, seg in enumerate(segments):
                rows.append({
                    "road": seg,
                    "status": statuses[i].upper(),
                    "caution": caution,
                    "notes": notes_parts[i] if i < len(notes_parts) else full_notes,
                })
        else:
            status = "CLOSED" if any(s.lower() == "closed" for s in statuses) else (
                "OPEN" if statuses else "UNKNOWN")
            rows.append({
                "road": " ".join(segments) if segments else clean_html(cells[0]),
                "status": status,
                "caution": caution,
                "notes": full_notes,
            })
    return rows


def main():
    now = datetime.now(ZoneInfo("America/Chicago"))
    parks = []
    for p in PARKS:
        alerts = json.loads(fetch(
            f"https://www.nps.gov/{p['code']}/park-alerts-{p['code']}.json"))
        entry = {"code": p["code"], "name": p["name"], "url": p["url"],
                 "alerts": filter_alerts(alerts), "roads": None}
        if p["code"] == "moja":
            entry["roads"] = moja_roads(fetch(p["url"]))
        parks.append(entry)
        print(f"{p['code']}: {len(entry['alerts'])} road alerts"
              + (f", {len(entry['roads'])} roads" if entry["roads"] is not None else ""))

    data = {
        "updated": now.isoformat(timespec="minutes"),
        "updated_display": now.strftime("%a %b %d, %Y, %-I:%M %p CT"),
        "parks": parks,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
