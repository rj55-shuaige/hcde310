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