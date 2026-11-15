---
layout: default
title: Death Valley + Joshua Tree — Trail Links, Dec 19–23, 2026
---

# Death Valley + Joshua Tree — Trail Links {#top}

**Five park days · Sat Dec 19 – Wed Dec 23, 2026 · Death Valley → Mojave National Preserve → Joshua Tree**
Every hike, viewpoint, and scramble on the trip, with its AllTrails page and a Google Maps pin. Distances are AllTrails' figures unless noted. All 25 stops have an AllTrails trail page.

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
- [Sat Dec 19 — Death Valley east / central](#day-1)
- [Sun Dec 20 — Death Valley canyons](#day-2)
- [Mon Dec 21 — Mojave National Preserve + transfer](#day-3)
- [Tue Dec 22 — Joshua Tree west / central](#day-4)
- [Wed Dec 23 — Joshua Tree east + the big hike](#day-5)
- [Not in the plan](#not-in-the-plan)
- [Know before you go](#know-before-you-go)

## Trip at a glance {#trip-at-a-glance}

- **Dates:** Dec 17–23, 2026 — fly into Las Vegas, five park days Sat Dec 19 – Wed Dec 23, fly home on the Wed night redeye.
- **Route:** Death Valley first, then Mojave National Preserve on the Mon Dec 21 transfer day, then Joshua Tree.
- **Lodging areas:** Death Valley Fri–Sun Dec 18–20 (Furnace Creek ×2, Stovepipe Wells ×1); Joshua Tree town Mon–Tue Dec 21–22 (2 nights).
- **Park entry:** $30 per vehicle per park, or the $80 America the Beautiful pass covering both.
- **Passport stamps:** bring the Collector's Edition book. Death Valley and Joshua Tree stamps at their visitor centers; Mojave stamp at the Barstow headquarters desk on Wed Dec 23 (or Hole-in-the-Wall on Mon Dec 21 if it's open — verify by phone, 760-252-6104).

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

Every stop on one map: 🔵 **Day 1** (Sat, Death Valley east/central) · 🟠 **Day 2** (Sun, Death Valley canyons) · 🟢 **Day 3** (Mon, Mojave + transfer) · 🟣 **Day 4** (Tue, Joshua Tree west/central) · 🔴 **Day 5** (Wed, Joshua Tree east + the big hike). Pins are numbered in visit order — tap a pin for the stop and a Google Maps link. **Filter by day:** use the layer checkboxes on the map (top right — on a phone, tap the layers icon). [Open the map full-screen](map.html) for easier browsing on a phone.

<iframe src="map.html" width="100%" style="border:1px solid #ccc; border-radius:8px; height:82vh; min-height:620px;" loading="lazy" title="Death Valley and Joshua Tree trip map — stops color-coded by day"></iframe>

## Sat Dec 19 — Death Valley east / central {#day-1}

The easy first day: the classic east-side viewpoints in one loop — Zabriskie Point's badlands at the start, Dante's View looking down 5,000 feet to Badwater, the salt flats, Artist's Palette, and Natural Bridge on the way back to Furnace Creek.

| Stop | Distance | Links |
| --- | --- | --- |
| Zabriskie Point / Badlands Loop | 2.6 mi | [AllTrails](https://www.alltrails.com/trail/us/california/badlands-loop-via-zabriskie-point-trail-and-gower-gulch-path) · [Map](https://www.google.com/maps/search/?api=1&query=Zabriskie+Point+Death+Valley+National+Park+CA) |
| Dante's View | 0.9 mi | [AllTrails](https://www.alltrails.com/trail/us/california/dantes-view-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Dante%27s+View+Death+Valley+National+Park+CA) |
| Badwater Salt Flat Trail | 1.9 mi | [AllTrails](https://www.alltrails.com/trail/us/california/badwater-basin-salt-flats-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Badwater+Basin+Death+Valley+National+Park+CA) |
| Artist's Palette / Artists Drive | 0.3 mi | [AllTrails](https://www.alltrails.com/trail/us/california/artists-palette-overlook) · [Map](https://www.google.com/maps/search/?api=1&query=Artist%27s+Palette+Death+Valley+National+Park+CA) |
| Natural Bridge Canyon Trail | 1.5 mi | [AllTrails](https://www.alltrails.com/trail/us/california/death-valley-natural-bridge-road) · [Map](https://www.google.com/maps/search/?api=1&query=Natural+Bridge+Canyon+Death+Valley+National+Park+CA) |
| Harmony Borax Works Interpretive Trail | 0.4 mi | [AllTrails](https://www.alltrails.com/trail/us/california/harmony-borax-works) · [Map](https://www.google.com/maps/search/?api=1&query=Harmony+Borax+Works+Death+Valley+National+Park+CA) |

**The stops, in order:**

- **Zabriskie Point / Badlands Loop** — the golden badlands ridges at the park's east edge, with Manly Beacon in the middle distance. The loop climbs into the badlands for the classic view; best in morning light.
- **Dante's View** — a paved viewpoint more than 5,000 feet above Badwater Basin. Look straight down at the salt flats and across the valley to Telescope Peak.
- **Badwater Salt Flat** — walk out onto the salt polygons at the lowest point in North America, 282 feet below sea level. Flat and easy, but carry water even in December.
- **Artist's Palette / Artists Drive** — a one-way scenic drive through hills stained pink, green, and purple by minerals, with a short walk to the palette viewpoint itself.
- **Natural Bridge Canyon** — a short gravel-road drive, then a walk up a dry wash to a natural rock bridge. An easy 1.5-mile round trip.
- **Harmony Borax Works** — the ruins of the 1880s borax operation, with interpretive signs telling the twenty-mule-team story. A short, flat walk.

Sleep: Furnace Creek.

## Sun Dec 20 — Death Valley canyons {#day-2}

The canyon day, and the longest hiking day in Death Valley. Golden Canyon and Gower Gulch combine into one 4.3-mile loop — hike in through Golden Canyon, out through Gower Gulch — then Desolation and Mosaic Canyons, and the day ends at Mesquite Flat Sand Dunes for sunset.

| Stop | Distance | Links |
| --- | --- | --- |
| Golden Canyon Trail (to Red Cathedral) | — | [AllTrails](https://www.alltrails.com/trail/us/california/golden-canyon-trail-to-red-cathedral) · [Map](https://www.google.com/maps/search/?api=1&query=Golden+Canyon+Trail+Death+Valley+National+Park+CA) |
| Gower Gulch Loop (Golden Canyon → Gower Gulch) | 4.3 mi | [AllTrails](https://www.alltrails.com/trail/us/california/gower-gulch-loop-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Gower+Gulch+Death+Valley+National+Park+CA) |
| Desolation Canyon Trail | 3.8 mi | [AllTrails](https://www.alltrails.com/trail/us/california/desolation-canyon-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Desolation+Canyon+Death+Valley+National+Park+CA) |
| Mosaic Canyon Trail | 3.6 mi | [AllTrails](https://www.alltrails.com/trail/us/california/mosaic-canyon-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Mosaic+Canyon+Death+Valley+National+Park+CA) |
| Mesquite Flat Sand Dunes Trail | 2 mi | [AllTrails](https://www.alltrails.com/trail/us/california/mesquite-flat-sand-dunes-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Mesquite+Flat+Sand+Dunes+Death+Valley+National+Park+CA) |

**The stops, in order:**

- **Golden Canyon Trail** — red and gold canyon walls leading to Red Cathedral, a towering rock formation at the canyon's end. This is the way in.
- **Gower Gulch Loop** — the way back out: a 4.3-mile loop returning through a narrow badlands gorge. The wash floor can be rough after rain.
- **Desolation Canyon Trail** — a quieter badlands canyon with colorful walls and slot-like narrows, and far fewer people than Golden Canyon.
- **Mosaic Canyon Trail** — polished marble narrows: smooth white and tan walls that tighten after about a mile. Can be slippery when wet.
- **Mesquite Flat Sand Dunes** — the sunset stop. The tallest dune is about 100 feet; the sand is soft, so allow extra time for the walk in from the Stovepipe Wells side.

Sleep: Stovepipe Wells — the west side, which sets up Monday's transfer.

## Mon Dec 21 — Mojave National Preserve + transfer {#day-3}

The transfer day doubles as the Mojave day. South from Stovepipe Wells through Shoshone to Baker, then into the preserve: Kelso Dunes, the Kelso Depot exterior (visitor center closed), Amboy Crater and Roy's on Route 66, then CA-62 to Joshua Tree town, arriving ~6–7 PM. Wildrose Peak and Darwin Falls were dropped to make room for Mojave.

| Stop | Distance | Links |
| --- | --- | --- |
| Kelso Dunes Trail | 3.0 mi | [AllTrails](https://www.alltrails.com/trail/us/california/kelso-dunes-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Kelso+Dunes+Mojave+National+Preserve+CA) |
| Amboy Crater Trail | 4.1 mi | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/amboy-crater) · [Map](https://www.google.com/maps/search/?api=1&query=Amboy+Crater+Mojave+National+Preserve+CA) |

**The stops, in order:**

- **Kelso Dunes Trail** — a 3-mile out-and-back to the top of the dunes, the tallest in the Mojave. The dunes can "sing" — a low hum — when dry sand slides down the steep face, and the soft-sand climb is harder than it looks.
- **Amboy Crater Trail** — an ancient volcanic cinder cone on Route 66. A short walk across old lava flows leads to the crater rim. Roy's Motel &amp; Cafe, the Route 66 landmark, is just up the road.

Sleep: Joshua Tree town / Yucca Valley.

## Tue Dec 22 — Joshua Tree west / central {#day-4}

The full Joshua Tree day: Ryan Mountain first for the morning light, then the short loops — Hidden Valley, Barker Dam, Skull Rock, Split Rock, Hall of Horrors — and up to Keys View for the afternoon, with the steep, partly unmarked Inspiration Peak climb from the Keys View lot before sunset at Keys View itself.

| Stop | Distance | Links |
| --- | --- | --- |
| Ryan Mountain Trail | 2.9 mi | [AllTrails](https://www.alltrails.com/trail/us/california/ryan-mountain-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Ryan+Mountain+Joshua+Tree+National+Park+CA) |
| Hidden Valley Nature Trail | 1.0 mi | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/hidden-valley--3) · [Map](https://www.google.com/maps/search/?api=1&query=Hidden+Valley+Joshua+Tree+National+Park+CA) |
| Barker Dam Trail | 1.3 mi | [AllTrails](https://www.alltrails.com/trail/us/california/barker-dam--2) · [Map](https://www.google.com/maps/search/?api=1&query=Barker+Dam+Joshua+Tree+National+Park+CA) |
| Skull Rock Trail | 1.7 mi | [AllTrails](https://www.alltrails.com/trail/us/california/skull-rock-nature-trail) · [Map](https://www.google.com/maps/search/?api=1&query=Skull+Rock+Joshua+Tree+National+Park+CA) |
| Split Rock Loop Trail | 2.5 mi | [AllTrails](https://www.alltrails.com/trail/us/california/split-rock-loop--4) · [Map](https://www.google.com/maps/search/?api=1&query=Split+Rock+Joshua+Tree+National+Park+CA) |
| Hall of Horrors | — | [AllTrails](https://www.alltrails.com/trail/us/california/hall-of-horrors) · [Map](https://www.google.com/maps/search/?api=1&query=Hall+of+Horrors+Joshua+Tree+National+Park+CA) |
| Inspiration Peak (from Keys View) | 1.9 mi | [AllTrails](https://www.alltrails.com/trail/us/california/inspiration-peak-trail--2) · [Map](https://www.google.com/maps/search/?api=1&query=Mount+Inspiration+Joshua+Tree+National+Park+CA) |
| Keys View | 0.1 mi | [AllTrails](https://www.alltrails.com/trail/us/california/keys-view) · [Map](https://www.google.com/maps/search/?api=1&query=Keys+View+Joshua+Tree+National+Park+CA) |

**The stops, in order:**

- **Ryan Mountain Trail** — the day's real climb: 2.9 miles and about 1,050 feet to the best panoramic summit in the park. Do it first, before the afternoon catches up.
- **Hidden Valley Nature Trail** — a 1-mile loop through a boulder-enclosed valley once used as a cattle-rustling hideout. Rock climbers are often on the walls above the trail.
- **Barker Dam Trail** — a 1.3-mile loop to a 1900s dam built by cattlemen, with desert views and petroglyphs nearby. Look for water in the dam's pool after rain.
- **Skull Rock Trail** — a 1.7-mile walk along Park Boulevard to the skull-shaped boulder, with rock piles and desert gardens along the way. Short and easy.
- **Split Rock Loop Trail** — a 2.5-mile loop past the split boulder and through desert wash scenery, with big rock formations the whole way.
- **Hall of Horrors** — a short scramble among house-sized boulders by Ryan Campground. It's rock scrambling rather than a formal trail, so take it slow.
- **Inspiration Peak** — a steep, partly unmarked climb from the Keys View parking lot, ranked as the park's #5 sunrise spot. Download the offline map before you start.
- **Keys View** — a 0.1-mile paved overlook and the sunset stop: views over Coachella Valley to San Jacinto and San Gorgonio peaks on a clear day.

Sleep: Joshua Tree town.

## Wed Dec 23 — Joshua Tree east + the big hike {#day-5}

The last day: Cholla Cactus Garden at sunrise, Arch Rock, then one big hike started early — Boy Scout Trail to Willow Hole or Lost Palms Oasis. Leave Joshua Tree town by ~1:30 PM for the Mojave stamp at the Barstow headquarters desk (~20–30 min, weekdays until ~4:30 PM), then drive to Las Vegas for the Wednesday night flight home.

| Stop | Distance | Links |
| --- | --- | --- |
| Cholla Cactus Garden Nature Trail | 0.2 mi | [AllTrails](https://www.alltrails.com/trail/us/california/cholla-cactus-garden) · [Map](https://www.google.com/maps/search/?api=1&query=Cholla+Cactus+Garden+Joshua+Tree+National+Park+CA) |
| Arch Rock Nature Trail | 1.2 mi | [AllTrails](https://www.alltrails.com/trail/us/california/arch-rock-trail--2) · [Map](https://www.google.com/maps/search/?api=1&query=Arch+Rock+Trail+Joshua+Tree+National+Park+CA) |
| Boy Scout Trail to Willow Hole | 6.9 mi | [AllTrails](https://www.alltrails.com/en-gb/trail/us/california/willow-hole) · [Map](https://www.google.com/maps/search/?api=1&query=Willow+Hole+Joshua+Tree+National+Park+CA) |
| Lost Palms Oasis Trail | 7.4 mi | [AllTrails](https://www.alltrails.com/trail/us/california/lost-palms-oasis--4) · [Map](https://www.google.com/maps/search/?api=1&query=Lost+Palms+Oasis+Joshua+Tree+National+Park+CA) |

**The stops, in order:**

- **Cholla Cactus Garden Nature Trail** — a 0.2-mile flat loop through a dense stand of teddybear cholla, best at sunrise when the spines glow. Look, don't touch — the segments detach easily.
- **Arch Rock Nature Trail** — a 1.2-mile loop to the park's best-known granite arch, a 30-foot span on the White Tank Campground trail. Good morning light.
- **Boy Scout Trail to Willow Hole** — a 6.9-mile sandy-wash hike to Willow Hole, a grove of willows and palms in the desert. Pick **one** big hike: this, or Lost Palms Oasis.
- **Lost Palms Oasis Trail** — a 7.4-mile hike in the park's south end to a palm oasis in a rocky canyon. Pick **one** big hike: this, or Boy Scout to Willow Hole. Carry plenty of water either way.

## Not in the plan {#not-in-the-plan}

- **Telescope Peak** (12.2 mi) — a full day on its own, can be snowed in in December.
- **Ubehebe Crater** — far north end of Death Valley, a half-day detour from Stovepipe Wells.
- Both stay cut unless the trip extends or a day is swapped.

## Know before you go {#know-before-you-go}

- **Download offline maps before the parks** — get AllTrails+ while on Wi-Fi in Las Vegas on Fri Dec 18. Cell service is spotty to nonexistent inside both parks.
- **Water and gas are scarce in Death Valley** — stock up in Las Vegas or Pahrump on Friday night.
- **Friday's drive arrives ~midnight** — the Furnace Creek hotel must allow very late check-in.
- **No toll roads on this loop** — decline the toll pass at the rental counter.

[Back to top](#top)

<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (h && h.charAt(0) !== '#') { a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noopener'); }
  });
});
</script>
