"""Run locally to collect REAL Open-Meteo evidence for Section 4 of P2.
Paste only the fields actually returned by the API. Internet required.
"""
import json
import requests
from resorts import load_resorts

resort = load_resorts()[0]
params = {"latitude": resort["latitude"], "longitude": resort["longitude"],
          "daily": "snowfall_sum,temperature_2m_max,wind_speed_10m_max",
          "timezone": "America/Los_Angeles", "forecast_days": 3}
response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
response.raise_for_status()
data = response.json()
print("REQUEST URL:", response.url)
print("REAL TRIMMED RESPONSE:")
print(json.dumps({"daily_units": data.get("daily_units"), "daily": data.get("daily")}, indent=2))
