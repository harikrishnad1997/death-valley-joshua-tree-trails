---
layout: default
title: Death Valley + Joshua Tree Trip, Dec 19–23, 2026
---

# Death Valley + Joshua Tree Trip {#top}

**Five park days · Sat Dec 19 – Wed Dec 23, 2026 · Death Valley → Mojave National Preserve → Joshua Tree**
Every hike, viewpoint, and scramble on the trip, with its AllTrails page and a Google Maps pin. Distances are AllTrails' figures unless noted. All 28 stops in the plan have an AllTrails trail page, plus Ubehebe Crater as an optional Sunday detour and Travelers Monument as an optional Monday stop.

<style>
.trip-fig { margin: 14px 0; }
.trip-fig img { width: 100%; height: auto; border-radius: 10px; display: block; }
.trip-fig figcaption { font-size: 0.85em; color: #606c71; text-align: center; margin-top: 5px; }
.hero-fig img { max-height: 420px; object-fit: cover; }
</style>

<figure class="trip-fig hero-fig"><img src="https://commons.wikimedia.org/wiki/Special:FilePath/Death%20Valley%20-%20Zabriskie%20Point.jpg?width=1280" alt="Zabriskie Point, Death Valley — the golden badlands ridges at the first stop on Saturday." loading="lazy"><figcaption>Zabriskie Point, Death Valley — the first stop on Saturday's east/central day.</figcaption></figure>

## Contents {#contents}

- [Trip at a glance](#trip-at-a-glance)
- [Weather in the desert — live forecast](#weather)
- [Trip map — color-coded by day](#trip-map)
- [Fri Dec 18 — Las Vegas: Lake Mead + Tule Springs](#day-0)
- [Sat Dec 19 — Death Valley east / central](#day-1)
- [Sun Dec 20 — Death Valley canyons](#day-2)
- [Mon Dec 21 — Mojave National Preserve + transfer](#day-3)
- [Tue Dec 22 — Joshua Tree west / central](#day-4)
- [Wed Dec 23 — Joshua Tree east + the big hike](#day-5)
- [Visitor centers](#visitor-centers)
- [Places to eat](#places-to-eat)
- [Food to pack on the way](#food-to-pack)
- [Not in the plan](#not-in-the-plan)
- [Know before you go](#know-before-you-go)
- [Packing checklist](#packing-checklist)

## Trip at a glance {#trip-at-a-glance}

- **Dates:** Dec 17–23, 2026 — fly into Las Vegas, five park days Sat Dec 19 – Wed Dec 23, fly home on the Wed night redeye.
- **Fri Dec 18:** work in Las Vegas till 2 PM PT, then Lake Mead Visitor Center + Tule Springs in the afternoon; back ~5:45 PM, dinner downtown; 9 PM rental pickup at LAS, night drive to Furnace Creek via US-95 (Alien Center if the pickup is on time).
- **Flights:** United. Out — **Thu Dec 17, UA 777**, ORD 8:20 PM → LAS 10:38 PM ([Track UA 777](https://www.flightaware.com/live/flight/UAL777)). Home — **Wed Dec 23, UA 2102**, LAS 11:50 PM → ORD 5:31 AM Thu Dec 24 ([Track UA 2102](https://www.flightaware.com/live/flight/UAL2102)).
- **Route:** Death Valley first, then Mojave National Preserve on the Mon Dec 21 transfer day, then Joshua Tree.
- **Lodging areas:** Death Valley Fri–Sun Dec 18–20 (Furnace Creek ×2, Pahrump ×1); Joshua Tree town Mon–Tue Dec 21–22 (2 nights).
- **Park entry:** $30 per vehicle per park, or the $80 America the Beautiful pass covering both.
- **Passport stamps:** bring the Collector's Edition book. Death Valley and Joshua Tree stamps at their visitor centers; the Mojave stamp is got at Hole-in-the-Wall on Mon Dec 21 (open Fri–Mon 10 AM–4 PM) — the same center also holds the Castle Mountains stamp. Barstow HQ is the backup if Hole-in-the-Wall is closed — verify by phone, 760-252-6104.

## Weather in the desert — live forecast {#weather}

Live forecasts for Furnace Creek (Death Valley) and Twentynine Palms (Joshua Tree), powered by [Open-Meteo](https://open-meteo.com). The green cards are the trip days, Sat Dec 19 – Wed Dec 23.
Backups: the [National Weather Service forecast for Furnace Creek](https://forecast.weather.gov/MapClick.php?lat=36.4623&lon=-116.8668) and for [Twentynine Palms](https://forecast.weather.gov/MapClick.php?lat=34.1357&lon=-116.0617).

### Death Valley — Furnace Creek

<div id="wx-dv" class="wx-row"><p>Loading the latest forecast…</p></div>

### Joshua Tree — Twentynine Palms

<div id="wx-jt" class="wx-row"><p>Loading the latest forecast…</p></div>

<p id="wx-note" class="wx-note"></p>

<style>
.wx-row { display: flex; gap: 10px; flex-wrap: wrap; margin: 10px 0 4px; }
.wx-card { flex: 1 1 100px; max-width: 128px; border: 1px solid #d6dee3; border-radius: 10px; padding: 10px 6px; text-align: center; background: #f7faf9; }
.wx-card.trip { border: 2px solid #2e5a3c; background: #eef6f0; }
.wx-d { font-weight: 700; font-size: 13px; }
.wx-i { font-size: 26px; line-height: 1.25; }
.wx-t { font-size: 14px; font-weight: 600; }
.wx-c { font-size: 12px; color: #606c71; }
.wx-p { font-size: 12px; color: #1d6fb8; }
.wx-note { font-size: 12px; color: #606c71; margin-top: 0; }
</style>

<script>
(function () {
  var TRIP = { "2026-12-19": 1, "2026-12-20": 1, "2026-12-21": 1, "2026-12-22": 1, "2026-12-23": 1 };
  var note = document.getElementById("wx-note");
  var seen = 0;
  function wmo(c) {
    if (c === 0) return ["☀️", "Clear"];
    if (c === 1 || c === 2) return ["🌤️", "Partly cloudy"];
    if (c === 3) return ["☁️", "Overcast"];
    if (c === 45 || c === 48) return ["🌫️", "Fog"];
    if (c === 51 || c === 53 || c === 55) return ["🌦️", "Drizzle"];
    if (c === 56 || c === 57) return ["🌦️", "Freezing drizzle"];
    if (c === 61 || c === 63 || c === 65) return ["🌧️", "Rain"];
    if (c === 66 || c === 67) return ["🌧️", "Freezing rain"];
    if (c === 71 || c === 73 || c === 75 || c === 77) return ["🌨️", "Snow"];
    if (c === 80 || c === 81 || c === 82) return ["🌦️", "Showers"];
    if (c === 85 || c === 86) return ["🌨️", "Snow showers"];
    if (c === 95) return ["⛈️", "Thunderstorm"];
    if (c === 96 || c === 99) return ["⛈️", "Thunderstorm, hail"];
    return ["🌡️", ""];
  }
  function dayName(iso) {
    var p = iso.split("-");
    var d = new Date(p[0], p[1] - 1, p[2]);
    var days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    var mons = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return days[d.getDay()] + " " + mons[d.getMonth()] + " " + d.getDate();
  }
  function load(id, lat, lon, fallback) {
    var el = document.getElementById(id);
    fetch("https://api.open-meteo.com/v1/forecast?latitude=" + lat + "&longitude=" + lon + "&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&forecast_days=16")
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var t = d.daily.time, html = "";
        for (var i = 0; i < t.length; i++) {
          var w = wmo(d.daily.weather_code[i]);
          var isTrip = TRIP[t[i]] ? " trip" : "";
          if (TRIP[t[i]]) seen++;
          var pp = d.daily.precipitation_probability_max[i];
          html += '<div class="wx-card' + isTrip + '"><div class="wx-d">' + dayName(t[i]) + (TRIP[t[i]] ? " · TRIP" : "") + '</div><div class="wx-i">' + w[0] + '</div><div class="wx-t">' + Math.round(d.daily.temperature_2m_max[i]) + "° / " + Math.round(d.daily.temperature_2m_min[i]) + '°F</div><div class="wx-c">' + w[1] + '</div><div class="wx-p">' + (pp === null || pp === undefined ? "" : "💧 " + pp + "%") + "</div></div>";
        }
        el.innerHTML = html;
        note.textContent = seen === 0
          ? "Showing the current forecast window. Your trip (Dec 19–23) is not in it yet — check back during trip week and those days will be highlighted here."
          : "Your trip days are in this forecast — the green cards are the ones that matter. Desert days swing wide between day and night, so dress for the low as well as the high.";
      })
      .catch(function () {
        el.innerHTML = '<p>Could not load the live forecast right now — use the <a href="' + fallback + '">National Weather Service forecast</a> instead.</p>';
      });
  }
  load("wx-dv", 36.4623, -116.8668, "https://forecast.weather.gov/MapClick.php?lat=36.4623&lon=-116.8668");
  load("wx-jt", 34.1357, -116.0617, "https://forecast.weather.gov/MapClick.php?lat=34.1357&lon=-116.0617");
})();
</script>

## Trip map — color-coded by day {#trip-map}

Every stop on one map: 🟤 **Fri Dec 18** (Las Vegas: Lake Mead + Tule Springs) · 🔵 **Day 1** (Sat, Death Valley east/central) · 🟠 **Day 2** (Sun, Death Valley canyons) · 🟢 **Day 3** (Mon, Mojave + transfer) · 🟣 **Day 4** (Tue, Joshua Tree west/central) · 🔴 **Day 5** (Wed, Joshua Tree east + the big hike). Pins are numbered in visit order — tap a pin for the stop and a Google Maps link. **Filter by day:** use the layer checkboxes on the map (top right — on a phone, tap the layers icon). [Open the map full-screen](map.html) for easier browsing on a phone.

<iframe src="map.html" width="100%" style="border:1px solid #ccc; border-radius:8px; height:82vh; min-height:620px;" loading="lazy" title="Death Valley and Joshua Tree trip map — stops color-coded by day"></iframe>

## Fri Dec 18 — Las Vegas: Lake Mead + Tule Springs, then the night drive {#day-0}

Work in Las Vegas till 2 PM PT, then the afternoon is free: the Lake Mead Visitor Center in Boulder City for two passport stamps, and the Tule Springs Fossil Beds trailhead in North Las Vegas. Back in Las Vegas ~5:45 PM for dinner downtown, then the 9 PM rental pickup at LAS before the night drive to Furnace Creek via US-95 — with the Area 51 Alien Center as a conditional stop, only if the pickup runs on time (it closes 11 PM; if the pickup runs late, skip it and take the Pahrump route instead).

<iframe src="map.html?day=day0" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Friday Dec 18 — Las Vegas: Lake Mead + Tule Springs"></iframe>

[Open the map for Friday full-screen](map.html?day=day0)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Lake Mead Visitor Center (stamps)](https://www.google.com/maps/search/?api=1&query=36.009907,-114.796774) | — | ~45 min | ~2:45 PM | [visitor center lot](https://www.google.com/maps/search/?api=1&query=36.009907,-114.796774) | [Map](https://www.google.com/maps/search/?api=1&query=36.009907,-114.796774) |
| [Tule Springs Fossil Beds — Aliante trailhead](https://www.google.com/maps/search/?api=1&query=36.309226,-115.18898) | — | ~45 min | ~4:20 PM | [Aliante kiosk lot](https://www.google.com/maps/search/?api=1&query=36.309226,-115.18898) | [Map](https://www.google.com/maps/search/?api=1&query=36.309226,-115.18898) |
| [Area 51 Alien Center](https://www.google.com/maps/search/?api=1&query=36.643747,-116.395994) — **CONDITIONAL** | — | ~30 min | ~10:30 PM | [lot on US-95](https://www.google.com/maps/search/?api=1&query=36.643747,-116.395994) | [Map](https://www.google.com/maps/search/?api=1&query=36.643747,-116.395994) |

**The stops, in order:**

- [**Lake Mead Visitor Center**](https://www.google.com/maps/search/?api=1&query=36.009907,-114.796774) — the Alan Bible Visitor Center in Boulder City, open daily 9 AM–4:30 PM. Get the Lake Mead stamp here — and the Tule Springs Fossil Beds stamp too, from the same desk. Exhibits, a park film, and a desert garden. Free to enter from the Boulder City side.
- [**Tule Springs Fossil Beds — Aliante trailhead**](https://www.google.com/maps/search/?api=1&query=36.309226,-115.18898) — the monument protects Ice Age fossil beds (mammoth, dire wolf, ground sloth). No visitor center, restrooms, or water on site — the Aliante kiosk parking area (open 7 AM–7 PM) is the way in for a short walk on the beds. Bring water; there's no shade.
- [**Area 51 Alien Center — CONDITIONAL**](https://www.google.com/maps/search/?api=1&query=36.643747,-116.395994) — alien-themed roadside stop on US-95 in Amargosa Valley: diner, gift shop, gas. Open daily 5 AM–11 PM. Only if the 9 PM rental pickup runs on time — you'd reach it ~10:30 PM, and it pushes Furnace Creek to ~12:30 AM. If the pickup runs late, skip it and take the Pahrump route instead.

Sleep: Furnace Creek (arrive ~midnight, ~12:30 AM with the Alien Center stop).

## Sat Dec 19 — Death Valley east / central {#day-1}

The easy first day: the classic east-side viewpoints in one loop — Zabriskie Point's badlands at the start, Dante's View looking down 5,000 feet to Badwater, the salt flats, Artist's Palette, and Natural Bridge on the way back to Furnace Creek.

<iframe src="map.html?day=day1" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Saturday Dec 19 — Death Valley east/central"></iframe>

[Open the map for Saturday full-screen](map.html?day=day1)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Zabriskie Point / Badlands Loop 🌅 6:54 AM](https://www.google.com/maps/search/?api=1&query=36.42085,-116.8099) | 2.6 mi | 1–1.5 hr | ~6:40 AM | [Zabriskie lot](https://www.google.com/maps/search/?api=1&query=36.42085,-116.8099) | [AllTrails](https://www.alltrails.com/trail/us/california/badlands-loop-via-zabriskie-point-trail-and-gower-gulch-path) · [Map](https://www.google.com/maps/search/?api=1&query=36.42085,-116.8099) |
| [Dante's View](https://www.google.com/maps/search/?api=1&query=36.220659,-116.726753) | 0.9 mi | 0.5–1 hr | ~8:15 AM | [Dante's lot](https://www.google.com/maps/search/?api=1&query=36.220659,-116.726753) | [AllTrails](https://www.alltrails.com/trail/us/california/dantes-view-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.220659,-116.726753) |
| [Badwater Salt Flat Trail](https://www.google.com/maps/search/?api=1&query=36.25033,-116.825858) | 1.9 mi | 0.5–1 hr | ~9:15 AM | [Badwater lot](https://www.google.com/maps/search/?api=1&query=36.25033,-116.825858) | [AllTrails](https://www.alltrails.com/trail/us/california/badwater-basin-salt-flats-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.25033,-116.825858) |
| [Artist's Palette / Artists Drive](https://www.google.com/maps/search/?api=1&query=36.363515,-116.802741) | 0.3 mi | 0.5–1 hr | ~10:15 AM | [Palette pullouts](https://www.google.com/maps/search/?api=1&query=36.363515,-116.802741) | [AllTrails](https://www.alltrails.com/trail/us/california/artists-palette-overlook) · [Map](https://www.google.com/maps/search/?api=1&query=36.363515,-116.802741) |
| [Natural Bridge Canyon Trail](https://www.google.com/maps/search/?api=1&query=36.28115,-116.7699) | 1.5 mi | 52 min (mirror) | ~11:00 AM | [Natural Bridge lot](https://www.google.com/maps/search/?api=1&query=36.28115,-116.7699) | [AllTrails](https://www.alltrails.com/trail/us/california/death-valley-natural-bridge-road) · [Map](https://www.google.com/maps/search/?api=1&query=36.28115,-116.7699) |
| [Furnace Creek Visitor Center (stamp)](https://www.google.com/maps/search/?api=1&query=Furnace+Creek+Visitor+Center+Death+Valley+CA) | — | ~30 min | ~12:30 PM | [VC lot](https://www.google.com/maps/search/?api=1&query=Furnace+Creek+Visitor+Center+Death+Valley+CA) | [Map](https://www.google.com/maps/search/?api=1&query=Furnace+Creek+Visitor+Center+Death+Valley+CA) |
| [Harmony Borax Works Interpretive Trail](https://www.google.com/maps/search/?api=1&query=36.47982,-116.87107) | 0.4 mi | 9 min | ~1:00 PM | [Harmony lot](https://www.google.com/maps/search/?api=1&query=36.47982,-116.87107) | [AllTrails](https://www.alltrails.com/trail/us/california/harmony-borax-works) · [Map](https://www.google.com/maps/search/?api=1&query=36.47982,-116.87107) |


**The stops, in order:**

- [**Zabriskie Point / Badlands Loop**](https://www.google.com/maps/search/?api=1&query=36.42085,-116.8099) — the golden badlands ridges at the park's east edge, with Manly Beacon in the middle distance. The loop climbs into the badlands for the classic view; best at sunrise. Sunrise is 6:54 AM — be here by ~6:40 AM for it.
- [**Dante's View**](https://www.google.com/maps/search/?api=1&query=36.220659,-116.726753) — a paved viewpoint more than 5,000 feet above Badwater Basin. Look straight down at the salt flats and across the valley to Telescope Peak.
- [**Badwater Salt Flat**](https://www.google.com/maps/search/?api=1&query=36.25033,-116.825858) — walk out onto the salt polygons at the lowest point in North America, 282 feet below sea level. Flat and easy, but carry water even in December.
- [**Artist's Palette / Artists Drive**](https://www.google.com/maps/search/?api=1&query=36.363515,-116.802741) — a one-way scenic drive through hills stained pink, green, and purple by minerals, with a short walk to the palette viewpoint itself.
- [**Natural Bridge Canyon**](https://www.google.com/maps/search/?api=1&query=36.28115,-116.7699) — a short gravel-road drive, then a walk up a dry wash to a natural rock bridge. An easy 1.5-mile round trip.
- [**Harmony Borax Works**](https://www.google.com/maps/search/?api=1&query=36.47982,-116.87107) — the ruins of the 1880s borax operation, with interpretive signs telling the twenty-mule-team story. A short, flat walk.

Sleep: Furnace Creek.

## Sun Dec 20 — Death Valley canyons {#day-2}

The canyon day, and the longest hiking day in Death Valley. Golden Canyon and Gower Gulch combine into one 4.3-mile loop — hike in through Golden Canyon, out through Gower Gulch — then Desolation and Mosaic Canyons, and the day ends at Mesquite Flat Sand Dunes for sunset (4:35 PM).

<iframe src="map.html?day=day2" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Sunday Dec 20 — Death Valley canyons"></iframe>

[Open the map for Sunday full-screen](map.html?day=day2)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Golden Canyon Trail (to Red Cathedral)](https://www.google.com/maps/search/?api=1&query=36.420745,-116.846614) | 3.0 mi | 1 h 26 min (mirror) | ~7:00 AM | [Golden Canyon lot](https://www.google.com/maps/search/?api=1&query=36.420745,-116.846614) | [AllTrails](https://www.alltrails.com/trail/us/california/golden-canyon-trail-to-red-cathedral) · [Map](https://www.google.com/maps/search/?api=1&query=36.420745,-116.846614) |
| [Gower Gulch Loop (Golden Canyon → Gower Gulch)](https://www.google.com/maps/search/?api=1&query=36.41647,-116.835842) | 4.3 mi | 2.5 hr (NPS) | ~7:00 AM (same loop) | [Golden Canyon lot](https://www.google.com/maps/search/?api=1&query=36.420745,-116.846614) | [AllTrails](https://www.alltrails.com/trail/us/california/gower-gulch-loop-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.41647,-116.835842) |
| [Desolation Canyon Trail](https://www.google.com/maps/search/?api=1&query=36.395833,-116.83877) | 3.8 mi | 2.5 hr (NPS) | ~10:15 AM | [Desolation pullout](https://www.google.com/maps/search/?api=1&query=36.395833,-116.83877) | [AllTrails](https://www.alltrails.com/trail/us/california/desolation-canyon-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.395833,-116.83877) |
| [Mosaic Canyon Trail](https://www.google.com/maps/search/?api=1&query=36.56653,-117.13459) | 3.6 mi | 2 h 2 min (mirror) | ~1:20 PM | [Mosaic lot](https://www.google.com/maps/search/?api=1&query=36.56653,-117.13459) | [AllTrails](https://www.alltrails.com/trail/us/california/mosaic-canyon-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.56653,-117.13459) |
| [Stovepipe Wells Ranger Station (backup stamp)](https://www.google.com/maps/search/?api=1&query=Stovepipe+Wells+Ranger+Station+Death+Valley+CA) | — | ~15 min | anytime (backup) | [station lot](https://www.google.com/maps/search/?api=1&query=Stovepipe+Wells+Ranger+Station+Death+Valley+CA) | [Map](https://www.google.com/maps/search/?api=1&query=Stovepipe+Wells+Ranger+Station+Death+Valley+CA) |
| [Mesquite Flat Sand Dunes Trail 🌇 4:35 PM](https://www.google.com/maps/search/?api=1&query=36.6618711,-117.0962487) | 2 mi | 0.5–1 hr | ~3:45 PM | [Mesquite Dunes lot](https://www.google.com/maps/search/?api=1&query=36.6618711,-117.0962487) | [AllTrails](https://www.alltrails.com/trail/us/california/mesquite-flat-sand-dunes-trail) · [Map](https://www.google.com/maps/search/?api=1&query=36.6618711,-117.0962487) |
| [Ubehebe Crater](https://www.google.com/maps/search/?api=1&query=37.0098,-117.45082) — **OPTIONAL** | 1.8 mi | 0.5–1 hr | — (only if Desolation is dropped) | [crater lot](https://www.google.com/maps/search/?api=1&query=37.0098,-117.45082) | [AllTrails](https://www.alltrails.com/trail/us/california/ubehebe-and-little-hebe-crater-trail) · [Map](https://www.google.com/maps/search/?api=1&query=37.0098,-117.45082) |


**The stops, in order:**

- [**Golden Canyon Trail**](https://www.google.com/maps/search/?api=1&query=36.420745,-116.846614) — red and gold canyon walls leading to Red Cathedral, a towering rock formation at the canyon's end. This is the way in.
- [**Gower Gulch Loop**](https://www.google.com/maps/search/?api=1&query=36.41647,-116.835842) — the way back out: a 4.3-mile loop returning through a narrow badlands gorge. The wash floor can be rough after rain.
- [**Desolation Canyon Trail**](https://www.google.com/maps/search/?api=1&query=36.395833,-116.83877) — a quieter badlands canyon with colorful walls and slot-like narrows, and far fewer people than Golden Canyon.
- [**Mosaic Canyon Trail**](https://www.google.com/maps/search/?api=1&query=36.56653,-117.13459) — polished marble narrows: smooth white and tan walls that tighten after about a mile. Can be slippery when wet.
- [**Mesquite Flat Sand Dunes**](https://www.google.com/maps/search/?api=1&query=36.6618711,-117.0962487) — the sunset stop: sunset 4:35 PM. Be on the dunes by ~4:00 PM for the golden-hour light — start the walk in by ~3:45 PM, since the sand is soft and the walk takes extra time. The tallest dune is about 100 feet.
- [**Ubehebe Crater — OPTIONAL**](https://www.google.com/maps/search/?api=1&query=37.0098,-117.45082) — a half-mile-wide volcanic crater, 500–777 feet deep, with a 1.8-mile rim loop that takes about an hour. It's ~32 miles (about 45 minutes each way) north of Stovepipe Wells, so it only fits if you drop Desolation Canyon — go after Mosaic Canyon and still make the dunes for sunset.

Sleep: Stovepipe Wells — the west side, which sets up Monday's transfer.

## Mon Dec 21 — Mojave National Preserve + transfer {#day-3}

The transfer day is now a full Mojave day — and a long one. Leave Pahrump by ~6 AM: south through Shoshone to Baker, then north on I-15 to Cima Road for Teutonia Peak, south through Kelso for the dunes and the depot exterior, east to Hole-in-the-Wall for the Rings Loop and the stamps, back west for the Lava Tube, then Amboy Crater as a viewpoint stop and Roy's on Route 66 before CA-62 to Joshua Tree town, arriving ~9–10 PM (estimate). The full 4.1-mile Amboy Crater loop no longer fits the day, so Amboy is a short stop, not a hike. One swap to know: the Lava Tube's light beams are a midday thing (11 AM–1 PM), and in this order you'll reach the tube in the late afternoon — if the beams matter to you, do the tube right after the dunes and Hole-in-the-Wall after it, at the cost of ~30 minutes of backtracking. Wildrose Peak and Darwin Falls were dropped to make room for Mojave. Optional first stop: from Baker, back south on I-15 to Zzyzx for the Travelers Monument walk across Soda Lake — dry lakebed only, ~1 hr, and it pushes Teutonia to ~10 AM. A second optional: Castle Mountains National Monument instead of Teutonia Peak — north on I-15 to the Nipton exit, then Nipton Road and the graded dirt Walking Box Ranch Road to the monument boundary, ~3.5–4 hours round trip; the rest of the day runs ~1.5 hours later (Joshua Tree town ~11 PM).

<iframe src="map.html?day=day3" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Monday Dec 21 — Mojave + transfer"></iframe>

[Open the map for Monday full-screen](map.html?day=day3)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Travelers Monument](https://www.google.com/maps/search/?api=1&query=35.13084,-116.09527) — **OPTIONAL** | ~2 mi round trip | ~1 hr | ~8:30 AM | [Zzyzx lot](https://www.google.com/maps/search/?api=1&query=35.14279,-116.10474) | [Map](https://www.google.com/maps/search/?api=1&query=35.13084,-116.09527) |
| [Castle Mountains National Monument](https://www.google.com/maps/search/?api=1&query=35.291563,-115.093561) — **OPTIONAL (instead of Teutonia Peak)** | — | ~3.5–4 hr | ~9:00 AM | [Walking Box Ranch Rd](https://www.google.com/maps/search/?api=1&query=35.291563,-115.093561) | [Map](https://www.google.com/maps/search/?api=1&query=35.291563,-115.093561) |
| [Teutonia Peak Trail](https://www.google.com/maps/search/?api=1&query=35.31625,-115.5525) | 3.2 mi | 1.5–2 hr | ~9:00 AM | [pullout on Cima Rd](https://www.google.com/maps/search/?api=1&query=35.31625,-115.5525) | [AllTrails](https://www.alltrails.com/trail/us/california/teutonia-peak-trail) · [Map](https://www.google.com/maps/search/?api=1&query=35.31625,-115.5525) |
| [Kelso Dunes Trail](https://www.google.com/maps/search/?api=1&query=34.89235,-115.69906) | 3.0 mi | 1 h 20 min (mirror) | ~12:00 PM | [Kelso Dunes lot](https://www.google.com/maps/search/?api=1&query=34.89235,-115.69906) | [AllTrails](https://www.alltrails.com/trail/us/california/kelso-dunes-trail) · [Map](https://www.google.com/maps/search/?api=1&query=34.89235,-115.69906) |
| [Hole-in-the-Wall Information Center (stamps)](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) | — | ~15 min | ~2:00 PM | [visitor center lot](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) | [Map](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) |
| [Hole-in-the-Wall Rings Trail](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) | 1.4 mi | 1–2 hr (NPS) | ~2:20 PM | [visitor center lot](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) | [AllTrails](https://www.alltrails.com/trail/us/california/hole-in-the-wall-rings-trail) · [Map](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) |
| [Lava Tube Trail](https://www.google.com/maps/search/?api=1&query=35.21378,-115.7532) | 0.5 mi | 0.5–1 hr | ~4:45 PM | [pullout on Aiken Mine Rd](https://www.google.com/maps/search/?api=1&query=35.21378,-115.7532) | [AllTrails](https://www.alltrails.com/trail/us/california/lava-tube-trail--2) · [Map](https://www.google.com/maps/search/?api=1&query=35.21378,-115.7532) |
| [Amboy Crater — viewpoint stop](https://www.google.com/maps/search/?api=1&query=34.5572,-115.7814) | — | ~15 min | ~6:15 PM | [viewpoint on Route 66](https://www.google.com/maps/search/?api=1&query=34.5572,-115.7814) | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/amboy-crater) · [Map](https://www.google.com/maps/search/?api=1&query=34.5572,-115.7814) |


**The stops, in order:**

- [**Travelers Monument — OPTIONAL**](https://www.google.com/maps/search/?api=1&query=35.13084,-116.09527) — a pile of rocks on the dry Soda Lake at mile ~100 of the Old Mojave Road, just south of Baker. Park at Zzyzx (Desert Studies Center, off I-15) and walk ~1 mile across the lakebed — the tradition is to carry a rock across and add it to the pile, and there's a plaque with a secret message hidden in the rocks. About an hour all in, only if the lakebed is dry; skip it if it's wet. Doing it pushes Teutonia Peak to ~10 AM.
- [**Castle Mountains National Monument — OPTIONAL (instead of Teutonia Peak)**](https://www.google.com/maps/search/?api=1&query=35.291563,-115.093561) — the monument's approach is the graded dirt Walking Box Ranch Road off Nipton Road (I-15 exit 286): ~10 miles of Nipton Road, then ~10 miles of dirt to the "Entering Castle Mountains National Monument" sign at the state line, with the Castle Peaks beyond. ~3.5–4 hours round trip from the Monday route, so it only works if Teutonia Peak is dropped — and it pushes the rest of the day ~1.5 hours later (Joshua Tree town ~11 PM). No visitor services, no trails, no stamp to collect (already got Monday at Hole-in-the-Wall); the payoff is the entrance sign, the Joshua tree woodland, and the Castle Peaks.
- [**Teutonia Peak Trail**](https://www.google.com/maps/search/?api=1&query=35.31625,-115.5525) — a 3.2-mile out-and-back through the Cima Dome Joshua tree forest to a rocky summit with panoramic views over the preserve. The forest burned in the 2020 Dome Fire, so it's recovering rather than the dense forest it was — the hike is still one of the few signed, maintained trails in the preserve.
- [**Kelso Dunes Trail**](https://www.google.com/maps/search/?api=1&query=34.89235,-115.69906) — a 3-mile out-and-back to the top of the dunes, the tallest in the Mojave. The dunes can "sing" — a low hum — when dry sand slides down the steep face, and the soft-sand climb is harder than it looks.
- [**Hole-in-the-Wall Rings Trail**](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) — a 1.4-mile loop through Banshee Canyon, climbing out of the slot with two sets of metal rings bolted to the rock, past petroglyphs. Get the stamps at the information center first (open Fri–Mon 10 AM–4 PM) — it holds the cancellations for both Mojave National Preserve and Castle Mountains, which is why Wednesday's Barstow detour is gone.
- [**Lava Tube Trail**](https://www.google.com/maps/search/?api=1&query=35.21378,-115.7532) — a 0.5-mile walk down a metal staircase into a lava tube, lit by skylights in the ceiling. The road in (Aiken Mine Road) is rough, washboarded dirt — high clearance recommended, though the Rogue AWD should manage it slowly. Bring a flashlight.
- [**Amboy Crater — viewpoint stop**](https://www.google.com/maps/search/?api=1&query=34.5572,-115.7814) — an ancient volcanic cinder cone on Route 66. The full 4.1-mile loop doesn't fit this day anymore, so this is a short look from the trailhead area, not the hike. Roy's Motel &amp; Cafe, the Route 66 landmark, is just up the road.

Sleep: Joshua Tree town / Yucca Valley.

## Tue Dec 22 — Joshua Tree west / central {#day-4}

The full Joshua Tree day: Ryan Mountain first for the morning light, then the short loops — Hidden Valley, Barker Dam, Skull Rock, Split Rock, Hall of Horrors — and up to Keys View for the afternoon, with the steep, partly unmarked Inspiration Peak climb from the Keys View lot before sunset at Keys View itself (4:40 PM; start the climb by ~2:15 PM).

<iframe src="map.html?day=day4" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Tuesday Dec 22 — Joshua Tree west/central"></iframe>

[Open the map for Tuesday full-screen](map.html?day=day4)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Ryan Mountain Trail](https://www.google.com/maps/search/?api=1&query=34.00257,-116.13594) | 2.9 mi | 2–2.5 hr | ~7:00 AM | [Ryan lot](https://www.google.com/maps/search/?api=1&query=34.00257,-116.13594) | [AllTrails](https://www.alltrails.com/trail/us/california/ryan-mountain-trail) · [Map](https://www.google.com/maps/search/?api=1&query=34.00257,-116.13594) |
| [Joshua Tree Visitor Center (stamp + café)](https://www.google.com/maps/search/?api=1&query=Joshua+Tree+Visitor+Center+6554+Park+Blvd+Joshua+Tree+CA) | — | ~30 min | ~9:45 AM | [VC lot](https://www.google.com/maps/search/?api=1&query=Joshua+Tree+Visitor+Center+6554+Park+Blvd+Joshua+Tree+CA) | [Map](https://www.google.com/maps/search/?api=1&query=Joshua+Tree+Visitor+Center+6554+Park+Blvd+Joshua+Tree+CA) |
| [Hidden Valley Nature Trail](https://www.google.com/maps/search/?api=1&query=34.012466,-116.168057) | 1.0 mi | 0.5–1 hr | ~10:30 AM | [Hidden Valley lot](https://www.google.com/maps/search/?api=1&query=34.012466,-116.168057) | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/hidden-valley--3) · [Map](https://www.google.com/maps/search/?api=1&query=34.012466,-116.168057) |
| [Barker Dam Trail](https://www.google.com/maps/search/?api=1&query=34.0251,-116.142) | 1.3 mi | 0.5–1 hr | ~11:15 AM | [Barker Dam lot](https://www.google.com/maps/search/?api=1&query=34.0251,-116.142) | [AllTrails](https://www.alltrails.com/trail/us/california/barker-dam--2) · [Map](https://www.google.com/maps/search/?api=1&query=34.0251,-116.142) |
| [Skull Rock Trail](https://www.google.com/maps/search/?api=1&query=33.997722,-116.059458) | 1.7 mi | 38 min | ~11:50 AM | [pullout on Park Blvd](https://www.google.com/maps/search/?api=1&query=33.997722,-116.059458) | [AllTrails](https://www.alltrails.com/trail/us/california/skull-rock-nature-trail) · [Map](https://www.google.com/maps/search/?api=1&query=33.997722,-116.059458) |
| [Split Rock Loop Trail](https://www.google.com/maps/search/?api=1&query=34.00955,-116.05577) | 2.5 mi | 1–1.5 hr | ~12:35 PM | [Split Rock lot](https://www.google.com/maps/search/?api=1&query=34.00955,-116.05577) | [AllTrails](https://www.alltrails.com/trail/us/california/split-rock-loop--4) · [Map](https://www.google.com/maps/search/?api=1&query=34.00955,-116.05577) |
| [Hall of Horrors](https://www.google.com/maps/search/?api=1&query=34.00052,-116.147084) | 0.6 mi | 0.5–1 hr | ~1:45 PM | [pullout](https://www.google.com/maps/search/?api=1&query=34.00052,-116.147084) | [AllTrails](https://www.alltrails.com/trail/us/california/hall-of-horrors) · [Map](https://www.google.com/maps/search/?api=1&query=34.00052,-116.147084) |
| [Inspiration Peak (from Keys View)](https://www.google.com/maps/search/?api=1&query=33.93576,-116.19551) | 1.9 mi | avg ~1 h 12 min | ~3:30 PM | [Keys View lot](https://www.google.com/maps/search/?api=1&query=33.92658,-116.187214) | [AllTrails](https://www.alltrails.com/trail/us/california/inspiration-peak-trail--2) · [Map](https://www.google.com/maps/search/?api=1&query=33.93576,-116.19551) |
| [Keys View 🌇 4:40 PM](https://www.google.com/maps/search/?api=1&query=33.92658,-116.187214) | 0.1 mi | 2 min | ~3:30 PM | [Keys View lot](https://www.google.com/maps/search/?api=1&query=33.92658,-116.187214) | [AllTrails](https://www.alltrails.com/trail/us/california/keys-view) · [Map](https://www.google.com/maps/search/?api=1&query=33.92658,-116.187214) |


**The stops, in order:**

- [**Ryan Mountain Trail**](https://www.google.com/maps/search/?api=1&query=34.00257,-116.13594) — the day's real climb: 2.9 miles and about 1,050 feet to the best panoramic summit in the park. Do it first, before the afternoon catches up.
- [**Hidden Valley Nature Trail**](https://www.google.com/maps/search/?api=1&query=34.012466,-116.168057) — a 1-mile loop through a boulder-enclosed valley once used as a cattle-rustling hideout. Rock climbers are often on the walls above the trail.
- [**Barker Dam Trail**](https://www.google.com/maps/search/?api=1&query=34.0251,-116.142) — a 1.3-mile loop to a 1900s dam built by cattlemen, with desert views and petroglyphs nearby. Look for water in the dam's pool after rain.
- [**Skull Rock Trail**](https://www.google.com/maps/search/?api=1&query=33.997722,-116.059458) — a 1.7-mile walk along Park Boulevard to the skull-shaped boulder, with rock piles and desert gardens along the way. Short and easy.
- [**Split Rock Loop Trail**](https://www.google.com/maps/search/?api=1&query=34.00955,-116.05577) — a 2.5-mile loop past the split boulder and through desert wash scenery, with big rock formations the whole way.
- [**Hall of Horrors**](https://www.google.com/maps/search/?api=1&query=34.00052,-116.147084) — a short scramble among house-sized boulders by Ryan Campground. It's rock scrambling rather than a formal trail, so take it slow.
- [**Inspiration Peak**](https://www.google.com/maps/search/?api=1&query=33.93576,-116.19551) — a steep, partly unmarked climb from the Keys View parking lot, ranked as the park's #5 sunrise spot (sunrise 6:46 AM) — but the plan climbs it in the afternoon, before the Keys View sunset: start by ~2:15 PM to be back at the overlook by ~3:30 PM. Download the offline map before you start.
- [**Keys View**](https://www.google.com/maps/search/?api=1&query=33.92658,-116.187214) — a 0.1-mile paved overlook and the sunset stop: sunset 4:40 PM, so be back here by ~4:15 PM. Views over Coachella Valley to San Jacinto and San Gorgonio peaks on a clear day.

Sleep: Joshua Tree town.

## Wed Dec 23 — Joshua Tree east + the big hike {#day-5}

The last day: Cholla Cactus Garden at sunrise (6:46 AM — leave Joshua Tree town ~5:45 AM), Arch Rock, then one big hike started early — Boy Scout Trail to Willow Hole or Lost Palms Oasis. No Barstow detour anymore — the Mojave stamp was got at Hole-in-the-Wall on Monday — so after the hike it's Pioneertown for a late lunch on Mane Street, then the drive to Las Vegas for the Wednesday night flight home.

<iframe src="map.html?day=day5" width="100%" style="border:1px solid #ccc; border-radius:8px; height:60vh; min-height:420px;" loading="lazy" title="Map for Wednesday Dec 23 — Joshua Tree east + the big hike"></iframe>

[Open the map for Wednesday full-screen](map.html?day=day5)

| Stop | Distance | Time | Start | Parking | Links |
| --- | --- | --- | --- | --- | --- |
| [Cholla Cactus Garden Nature Trail 🌅 6:46 AM](https://www.google.com/maps/search/?api=1&query=33.9248428,-115.9293477) | 0.2 mi | 0.5–1 hr | ~6:30 AM | [Cholla lot](https://www.google.com/maps/search/?api=1&query=33.9248428,-115.9293477) | [AllTrails](https://www.alltrails.com/trail/us/california/cholla-cactus-garden) · [Map](https://www.google.com/maps/search/?api=1&query=33.9248428,-115.9293477) |
| [Arch Rock Nature Trail](https://www.google.com/maps/search/?api=1&query=33.9899,-116.02275) | 1.2 mi | 0.5–1 hr | ~8:00 AM | [Arch Rock lot](https://www.google.com/maps/search/?api=1&query=33.9899,-116.02275) | [AllTrails](https://www.alltrails.com/trail/us/california/arch-rock-trail--2) · [Map](https://www.google.com/maps/search/?api=1&query=33.9899,-116.02275) |
| [Boy Scout Trail to Willow Hole](https://www.google.com/maps/search/?api=1&query=34.05708,-116.17954) | 6.9 mi | 2–2.5 hr | ~9:30 AM | [Boy Scout Trailhead](https://www.google.com/maps/search/?api=1&query=34.04042,-116.18627) | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/willow-hole) · [Map](https://www.google.com/maps/search/?api=1&query=34.05708,-116.17954) |
| [Lost Palms Oasis Trail](https://www.google.com/maps/search/?api=1&query=33.737,-115.8107) | 7.4 mi | 3–4 hr (guides) | ~10:00 AM | [Cottonwood Spring lot](https://www.google.com/maps/search/?api=1&query=33.67555,-115.80163) | [AllTrails](https://www.alltrails.com/trail/us/california/lost-palms-oasis--4) · [Map](https://www.google.com/maps/search/?api=1&query=33.737,-115.8107) |
| [Pioneertown (Mane Street + Pappy & Harriet's)](https://www.google.com/maps/search/?api=1&query=Pioneertown+CA) | — | ~1.5 hr | ~1:00 PM | [Pioneertown lot](https://www.google.com/maps/search/?api=1&query=Pioneertown+CA) | [Map](https://www.google.com/maps/search/?api=1&query=Pioneertown+CA) |


**The stops, in order:**

- [**Cholla Cactus Garden Nature Trail**](https://www.google.com/maps/search/?api=1&query=33.9248428,-115.9293477) — a 0.2-mile flat loop through a dense stand of teddybear cholla, best at sunrise when the spines glow: sunrise 6:46 AM, so be there by ~6:30 AM — leave Joshua Tree town around 5:45 AM, about a 40-minute drive (estimate). Look, don't touch — the segments detach easily.
- [**Arch Rock Nature Trail**](https://www.google.com/maps/search/?api=1&query=33.9899,-116.02275) — a 1.2-mile loop to the park's best-known granite arch, a 30-foot span on the White Tank Campground trail. Good morning light.
- [**Boy Scout Trail to Willow Hole**](https://www.google.com/maps/search/?api=1&query=34.05708,-116.17954) — a 6.9-mile sandy-wash hike to Willow Hole, a grove of willows and palms in the desert. Pick **one** big hike: this, or Lost Palms Oasis.
- [**Lost Palms Oasis Trail**](https://www.google.com/maps/search/?api=1&query=33.737,-115.8107) — a 7.4-mile hike in the park's south end to a palm oasis in a rocky canyon. Pick **one** big hike: this, or Boy Scout to Willow Hole. Carry plenty of water either way.
- [**Pioneertown**](https://www.google.com/maps/search/?api=1&query=Pioneertown+CA) — a 1940s Western movie-set town on Pioneertown Road, about 20 minutes from Joshua Tree town. Walk Mane Street's false-front storefronts (no cars, foot only), then a late lunch at Pappy & Harriet's Pioneertown Palace (53688 Pioneertown Rd) — veggie burgers and vegetarian nachos. About an hour and a half, after the big hike (around 12:30 PM if you do Willow Hole, closer to 2 PM for Lost Palms); then it's the drive to Las Vegas.

## Visitor centers {#visitor-centers}

Every center the trip actually needs — for the passport stamps, passes, water, and ranger info. Each one below holds a stamp; Kelso Depot is closed, so it's listed only so you don't count on it.

| Visitor center | Day | What for | Food inside? | Hours |
| --- | --- | --- | --- | --- |
| [Lake Mead Visitor Center](https://www.google.com/maps/search/?api=1&query=36.009907,-114.796774) | Fri Dec 18 afternoon | Lake Mead stamp — and the Tule Springs Fossil Beds stamp too, from the same desk. Exhibits, park film, desert garden | No food inside — eat in Boulder City or back in Las Vegas | Daily 9 AM–4:30 PM |
| [Furnace Creek Visitor Center](https://www.google.com/maps/search/?api=1&query=Furnace+Creek+Visitor+Center+Death+Valley+CA) | Sat Dec 19 (or any time Fri–Sun — you're based there) | Death Valley stamp, park film, passes, water, restrooms — the park's only full visitor center | No restaurant inside — the Inn Dining Room and Last Kind Words Saloon are right there at Furnace Creek (see Places to eat) | Daily 8 AM–5 PM |
| [Stovepipe Wells Ranger Station](https://www.google.com/maps/search/?api=1&query=Stovepipe+Wells+Ranger+Station+Death+Valley+CA) | Sun Dec 20 — backup only | A second Death Valley stamp (Stovepipe Wells oval) if you miss Furnace Creek; also sells passes. Contact station, not a full center — hours vary and it isn't open every day, so call 760-786-3200 first | No restaurant inside — Toll Road Restaurant and Badwater Saloon are at Stovepipe Wells Village | Varies — call ahead |
| [Hole-in-the-Wall Information Center](https://www.google.com/maps/search/?api=1&query=35.044,-115.398) | Mon Dec 21 | Mojave + Castle Mountains stamps — get them first, then the Rings Loop | No food here — stock up in Baker before the preserve drive | Fri–Mon 10 AM–4 PM |
| [Joshua Tree Visitor Center](https://www.google.com/maps/search/?api=1&query=Joshua+Tree+Visitor+Center+6554+Park+Blvd+Joshua+Tree+CA) | Tue Dec 22, on the way in via the West Entrance | Joshua Tree stamp (dated stamp plus two picture stamps — a Joshua tree and a desert tortoise), maps, passes, cafe | Yes — the Roadrunner Grab+Go Café inside: coffee, sandwiches, wraps and snacks (grab-and-go, good for the drive in) | Daily 7:30 AM–5 PM |
| [Joshua Tree National Park Visitor Center](https://www.google.com/maps/search/?api=1&query=Joshua+Tree+National+Park+Visitor+Center+Twentynine+Palms+CA) | Alternate for the Joshua Tree stamp | Same stamp, at the park headquarters by the Oasis of Mara near the North Entrance — use it if you miss the downtown center | No restaurant inside — eat in Twentynine Palms town | Daily 8 AM–5 PM |

Not needed: the **Kelso Depot Visitor Center** is closed for repairs (exterior only, no stamp); the **Barstow headquarters** (weekdays ~8 AM–4:30 PM) is the backup Mojave stamp only if Hole-in-the-Wall is closed; **Cottonwood Visitor Center** (south entrance) and **Black Rock Nature Center** (Yucca Valley) aren't on the route.

## Places to eat {#places-to-eat}

Vegetarian options at each stop of the trip. Inside Death Valley there are only the resort restaurants — no fast food and no real grocery beyond the general stores — so stock up in Las Vegas or Pahrump on Friday night.

**Las Vegas — Thu Dec 17, Fri Dec 18, Wed Dec 23**

- [**Crossroads Kitchen**](https://www.google.com/maps/search/?api=1&query=Crossroads+Kitchen+3000+S+Las+Vegas+Blvd+Las+Vegas+NV) (Resorts World, 3000 S Las Vegas Blvd, the Strip) — fully plant-based fine dining: Mediterranean-inspired small plates. [Map](https://www.google.com/maps/search/?api=1&query=Crossroads+Kitchen+3000+S+Las+Vegas+Blvd+Las+Vegas+NV)
- [**Tacotarian**](https://www.google.com/maps/search/?api=1&query=Tacotarian+Planet+Hollywood+Las+Vegas+NV) (Planet Hollywood, 3663 Las Vegas Blvd S, the Strip) — plant-based Mexican tacos, in the Miracle Mile mall. [Map](https://www.google.com/maps/search/?api=1&query=Tacotarian+Planet+Hollywood+Las+Vegas+NV)
- [**True Food Kitchen**](https://www.google.com/maps/search/?api=1&query=True+Food+Kitchen+Forum+Shops+Caesars+Las+Vegas+NV) (The Forum Shops at Caesars, the Strip) — a full vegetarian and vegan menu alongside the regular dishes. [Map](https://www.google.com/maps/search/?api=1&query=True+Food+Kitchen+Forum+Shops+Caesars+Las+Vegas+NV)
- [**Siegel's Bagelmania**](https://www.google.com/maps/search/?api=1&query=Siegels+Bagelmania+252+Convention+Center+Dr+Las+Vegas+NV) (252 Convention Center Dr, near the Strip) — New York-style bagels since 1989: lox bagel, everything bagel, egg breakfast bagels, cream cheese; open 6 AM–3:30 PM daily. [Map](https://www.google.com/maps/search/?api=1&query=Siegels+Bagelmania+252+Convention+Center+Dr+Las+Vegas+NV)
- [**Subway**](https://www.google.com/maps/search/?api=1&query=Subway+Las+Vegas+NV) (all over Las Vegas, including the Strip) — cheap and quick: Veggie Delite, egg breakfast sandwiches in the morning. [Map](https://www.google.com/maps/search/?api=1&query=Subway+Las+Vegas+NV)

**Death Valley — Sat Dec 19, Sun Dec 20**

- [**The Inn at Death Valley Dining Room**](https://www.google.com/maps/search/?api=1&query=The+Inn+at+Death+Valley+Dining+Room+Furnace+Creek+CA) (Furnace Creek) — the upscale in-park restaurant; creative vegan options like chipotle basil pesto pasta. Reservations recommended. [Map](https://www.google.com/maps/search/?api=1&query=The+Inn+at+Death+Valley+Dining+Room+Furnace+Creek+CA)
- [**The Last Kind Words Saloon**](https://www.google.com/maps/search/?api=1&query=The+Last+Kind+Words+Saloon+Death+Valley+CA) (The Ranch at Death Valley, Furnace Creek) — casual saloon with a black bean burger, vegetarian pizza, and pistachio sun-dried pasta. [Map](https://www.google.com/maps/search/?api=1&query=The+Last+Kind+Words+Saloon+Death+Valley+CA)
- [**Toll Road Restaurant**](https://www.google.com/maps/search/?api=1&query=Toll+Road+Restaurant+Stovepipe+Wells+CA) (Stovepipe Wells Village) — casual breakfast, lunch, and dinner with vegan and vegetarian options, right at the Stovepipe Wells junction on Sunday's route before the drive to Pahrump. [Map](https://www.google.com/maps/search/?api=1&query=Toll+Road+Restaurant+Stovepipe+Wells+CA)

**Baker — Mon Dec 21**

- [**The Mad Greek Cafe**](https://www.google.com/maps/search/?api=1&query=The+Mad+Greek+Cafe+Baker+CA) (72112 Baker Blvd) — Greek spot on the main strip through Baker, listed vegetarian friendly; hummus, salads, and veggie plates. [Map](https://www.google.com/maps/search/?api=1&query=The+Mad+Greek+Cafe+Baker+CA)
- [**Denny's**](https://www.google.com/maps/search/?api=1&query=Dennys+Baker+CA) (72415 Baker Blvd) — the reliable fallback, listed vegetarian friendly, open long hours. [Map](https://www.google.com/maps/search/?api=1&query=Dennys+Baker+CA)

**Joshua Tree, Twentynine Palms &amp; Pioneertown — Mon Dec 21, Tue Dec 22, Wed Dec 23**

- [**Crossroads Cafe**](https://www.google.com/maps/search/?api=1&query=Crossroads+Cafe+61715+29+Palms+Hwy+Joshua+Tree+CA) (downtown Joshua Tree) — the town's breakfast and lunch institution, with plenty of vegetarian and vegan choices; go early, it fills up 8–10 AM. [Map](https://www.google.com/maps/search/?api=1&query=Crossroads+Cafe+61715+29+Palms+Hwy+Joshua+Tree+CA)
- [**Natural Sisters Cafe**](https://www.google.com/maps/search/?api=1&query=Natural+Sisters+Cafe+61695+Twentynine+Palms+Hwy+Joshua+Tree+CA) (61695 Twentynine Palms Hwy, Joshua Tree) — vegetarian and vegan-friendly cafe: smoothies, bowls, and wraps, near the West Entrance. [Map](https://www.google.com/maps/search/?api=1&query=Natural+Sisters+Cafe+61695+Twentynine+Palms+Hwy+Joshua+Tree+CA)
- [**Pie for the People**](https://www.google.com/maps/search/?api=1&query=Pie+for+the+People+61740+29+Palms+Hwy+Joshua+Tree+CA) (downtown Joshua Tree) — pizza by the slice with vegan and vegetarian options; the late-afternoon hiker staple for dinner. [Map](https://www.google.com/maps/search/?api=1&query=Pie+for+the+People+61740+29+Palms+Hwy+Joshua+Tree+CA)
- [**Pappy & Harriet's Pioneertown Palace**](https://www.google.com/maps/search/?api=1&query=Pappy+Harriet%27s+Pioneertown+CA) (53688 Pioneertown Rd, Pioneertown) — the Wednesday lunch stop after the big hike: a legendary desert roadhouse with live music, vegetarian-friendly — veggie burgers and vegetarian nachos. Open Wed 11 AM–11 PM. [Map](https://www.google.com/maps/search/?api=1&query=Pappy+Harriet%27s+Pioneertown+CA)

One more worth knowing: **La Copine** in Flamingo Heights is the area's best table — a small farm-to-table spot with a seasonal menu — but it needs a reservation weeks ahead, so it isn't a walk-in option.

## Food to pack on the way {#food-to-pack}

No real grocery inside either park, so the packable food comes from the towns on the way — sandwiches for the trails, and the supplies for the food checklist below.

**Las Vegas — Thu Dec 17, Fri Dec 18**

- [**Panera Bread**](https://www.google.com/maps/search/?api=1&query=Panera+Bread+2400+S+Rancho+Dr+Las+Vegas+NV) (2400 S Rancho Dr, 6:30 AM–10 PM; also 5130 S Fort Apache Rd, drive-thru) — sandwiches, soups, and salads with vegetarian options like the Mediterranean Veggie sandwich; Rapid Pick-Up to grab and go. They also sell whole loaves of bread for the trail sandwiches. [Map](https://www.google.com/maps/search/?api=1&query=Panera+Bread+2400+S+Rancho+Dr+Las+Vegas+NV)

**Pahrump — Fri Dec 18 night, Mon Dec 21 morning**

- There is no Panera in Pahrump — the nearest is back in Las Vegas. The stock-up stop here is the grocery instead:
- [**Albertsons**](https://www.google.com/maps/search/?api=1&query=Albertsons+200+S+Hwy+160+Pahrump+NV) (200 S Hwy 160, 6 AM–10 PM) — full grocery with deli and bakery: bread, peanut butter, trail snacks, water. [Map](https://www.google.com/maps/search/?api=1&query=Albertsons+200+S+Hwy+160+Pahrump+NV)
- [**Walmart Supercenter**](https://www.google.com/maps/search/?api=1&query=Walmart+300+S+Hwy+160+Pahrump+NV) (300 S Hwy 160, 6 AM–11 PM) — same, plus a Subway inside for a packable sandwich. [Map](https://www.google.com/maps/search/?api=1&query=Walmart+300+S+Hwy+160+Pahrump+NV)
- Both open from 6 AM, so Monday's restock before the preserve drive works too.

**Joshua Tree / Yucca Valley — Mon Dec 21, Tue Dec 22**

- No Panera in the Joshua Tree area either — the nearest is in Barstow, off the route.
- [**Stater Bros. Markets**](https://www.google.com/maps/search/?api=1&query=Stater+Bros+57075+29+Palms+Hwy+Yucca+Valley+CA) (57075 and 58060 29 Palms Hwy, Yucca Valley, 6 AM–11 PM) — deli and bakery; restock bread, peanut butter, fruit, and snacks Monday evening or Tuesday morning. [Map](https://www.google.com/maps/search/?api=1&query=Stater+Bros+57075+29+Palms+Hwy+Yucca+Valley+CA)

## Not in the plan {#not-in-the-plan}

- **Telescope Peak** (12.2 mi) — a full day on its own, can be snowed in in December.
- It stays cut unless the trip extends or a day is swapped. (Ubehebe Crater moved up to an optional Sunday detour — see Sun Dec 20.)

## Know before you go {#know-before-you-go}

- **Download offline maps before the parks** — get AllTrails+ while on Wi-Fi in Las Vegas on Fri Dec 18. Cell service is spotty to nonexistent inside both parks.
- **Water and gas are scarce in Death Valley** — stock up in Las Vegas or Pahrump on Friday night.
- **Friday's drive arrives ~midnight** — the Furnace Creek hotel must allow very late check-in.
- **No toll roads on this loop** — decline the toll pass at the rental counter.
- **Parking lots fill up** — Golden Canyon, Ryan Mountain, Hidden Valley, Barker Dam, Split Rock and Keys View can all fill or close when full (NPS), so start early and if a lot is full, move on to the next stop and swing back.
- **Table start times are estimates (~)** — built from the hike times and the day's anchors (sunrise/sunset, visitor center hours). Hike times are AllTrails' figures; where AllTrails lists none, the cell notes its source: (mirror) = AllTrails data on another site, (NPS) = the park service, (guides) = hiking guides.

## Packing checklist {#packing-checklist}

December desert: mild days, cold mornings and nights, no cell service in the parks, and water that has to be carried or refilled at the visitor centers.

**Hiking gear**

- [ ] Broken-in hiking boots
- [ ] Camp shoes or sandals for the evenings
- [ ] Daypack
- [ ] Trekking poles
- [ ] Headlamp or flashlight — the Lava Tube is dark inside, and Monday runs late

**Clothing**

- [ ] Layers: base layer, fleece or insulated mid-layer, warm jacket
- [ ] Wind / rain shell for the desert wind
- [ ] Warm hat and gloves — for the Cholla sunrise and the Mesquite Dunes and Keys View sunsets
- [ ] Sun hat and sunglasses
- [ ] Extra socks

**Water, food, sun**

- [ ] Water bottles — carry more than you think; refill at Furnace Creek, Stovepipe Wells, and the visitor centers
- [ ] Trail snacks and food for the long Monday drive through the preserve
- [ ] Sunscreen and lip balm — the desert sun is strong even in December

**Food to pack / make ourselves** — buy it all Friday night in Las Vegas or Pahrump; there is no real grocery inside the parks

- [ ] Bread — a loaf (Panera sells whole loaves, or from Albertsons / Stater Bros)
- [ ] Peanut butter + jam
- [ ] Trail mix, granola bars, dried fruit
- [ ] Fruit that travels well — bananas, apples
- [ ] Coffee — a big bag, for the mornings
- [ ] Coke Zero — a case (or two) for the drives
- [ ] Crackers
- [ ] A butter knife, napkins, and zip bags for the sandwiches

**Tech and navigation**

- [ ] Phone, charger, and power bank
- [ ] Offline maps downloaded in AllTrails+ before leaving Las Vegas
- [ ] Laptop and charger — Friday is a remote-work day in Las Vegas
- [ ] Car charger

**Passport and documents**

- [ ] Collector's Edition passport book
- [ ] Regional sticker sets: 1990 (Death Valley), 1999 (Joshua Tree), 2007 (Mojave)
- [ ] ID and payment card — Death Valley is cashless

**Car and safety**

- [ ] First-aid kit and blister care
- [ ] Any personal medication
- [ ] A paper map as a backup — no service in the parks

[Back to top](#top)

<script>
document.querySelectorAll('a[href^="http"]').forEach(function (a) { a.target = "_blank"; a.rel = "noopener"; });
</script>

<a href="#top" title="Back to top" style="position:fixed; right:16px; bottom:16px; z-index:99; background:#1d6fb8; color:#fff; padding:10px 16px; border-radius:24px; text-decoration:none; font-size:14px; font-weight:600; box-shadow:0 2px 6px rgba(0,0,0,.3);">↑ Top</a>

<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (h && h.charAt(0) !== '#') { a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noopener'); }
  });
});
</script>
