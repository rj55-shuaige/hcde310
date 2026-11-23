import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

class WeatherError(Exception):
    pass


def get_forecast(resort):
    params = {
        "latitude": resort["latitude"],
        "longitude": resort["longitude"],
        "daily": "snowfall_sum,temperature_2m_max,wind_speed_10m_max",
        "timezone": "America/Los_Angeles",
        "forecast_days": 3,
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        daily = data["daily"]
        return {
            "date": daily["time"][0],
            "snowfall_cm": daily["snowfall_sum"][0],
            "temperature_c": daily["temperature_2m_max"][0],
            "wind_kmh": daily["wind_speed_10m_max"][0],
        }
    except (requests.RequestException, ValueError, KeyError, TypeError, IndexError) as e:
        raise WeatherError("Forecast unavailable or incomplete") from e
