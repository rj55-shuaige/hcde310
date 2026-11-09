# Spec: today's high for a city

**What:** a Flask page that shows today's high temperature for a city.

**Input:** a city name from a form.

**Output:** "Seattle: 12°C"

**Data:** Open-Meteo. First the geocoding API (city name to latitude and longitude), then the forecast API (today's high).

**Checks:**
1. Seattle shows a number
2. "zzzz" shows "No city found"
3. No internet shows a message, not a crash

**Out of scope:** a database, saving anything, styling, documentation, tests that fake the API.
