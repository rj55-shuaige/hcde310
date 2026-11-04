# Open-Meteo Weather API: A Quick Start Guide

## What is it, and why should designers care?

[Open-Meteo](https://open-meteo.com/en/docs) is a weather API that provides forecasts and current weather information, including temperature, precipitation, and wind speed. It returns data as JSON, which makes it easy to use in a Python project or website. Designers can use weather data to create tools that help people make everyday decisions, such as choosing clothing, deciding whether to bike, or planning outdoor activities.

## Setup

1. Install Python 3 and open a terminal in your project folder.
2. Install the `requests` library:

   ```bash
   python3 -m pip install requests
   ```

3. **Authentication:** No API key or account is needed for the free, non-commercial API.
4. Save the example below as `weather.py`, then run:

   ```bash
   python3 weather.py
   ```

I tested this example in VS Code and received the output shown below.

## One working example: Current weather in Seattle

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 47.6062,
    "longitude": -122.3321,
    "current": "temperature_2m,precipitation,wind_speed_10m",
    "timezone": "America/Los_Angeles"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()
current = data["current"]

print("Seattle Weather")
print("Temperature:", current["temperature_2m"], "°C")
print("Precipitation:", current["precipitation"], "mm")
print("Wind Speed:", current["wind_speed_10m"], "km/h")
```

**Output from my test in VS Code:**

```text
Seattle Weather
Temperature: 5.5 °C
Precipitation: 0.0 mm
Wind Speed: 5.0 km/h
```

Weather values will change as conditions change.

## Gotchas

- **Rate limits:** The free, non-commercial service has usage limits. Check the [pricing and usage information](https://open-meteo.com/en/pricing) before building an app that makes many requests.
- **Missing data:** Some fields may be unavailable for certain locations or models. Check whether a value is present before showing it.
- **Units and time zones:** Confirm the units in `current_units`, and specify a time zone so timestamps are easier to interpret.
- **Errors:** `raise_for_status()` catches HTTP error responses. A finished app should also handle connection errors and explain failures to users.

## Design angle

**Project idea:** Create a UW outdoor activity planner that shows temperature, precipitation, and wind before students decide whether to walk, bike, or plan a weekend trip. The interface could summarize conditions in simple language instead of displaying only raw numbers.

**Ethical / UX consideration:** Weather predictions are not guarantees. A weather app should clearly show when data was updated and avoid presenting forecasts as certain. If it uses a person's location, it should ask permission and offer a manual location option. The app should also credit Open-Meteo as the data source.

## AI use and testing disclosure

I used ChatGPT to help organize and write this Markdown guide and draft the Python example. I ran the complete Python example myself in VS Code and confirmed that it worked. The output above is from my test.

**Documentation:** https://open-meteo.com/en/docs
