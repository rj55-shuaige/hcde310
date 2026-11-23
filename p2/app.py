from pathlib import Path
import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from resorts import load_resorts, find_resort
from weather import get_forecast, WeatherError
from summary import build_summary

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY") or "dev-only-local-secret"  # local-only fallback
FAVORITES_FILE = Path(__file__).parent / "data" / "favorites.json"


def get_favorites():
    try:
        with FAVORITES_FILE.open(encoding="utf-8") as f:
            data = json.load(f)
        return data.get("resort_ids", [])
    except (FileNotFoundError, ValueError, OSError):
        return []


def valid_pair(a, b, resorts):
    return a != b and bool(find_resort(resorts, a)) and bool(find_resort(resorts, b))


@app.get("/")
def home():
    resorts = load_resorts()
    return render_template("index.html", resorts=resorts, favorites=get_favorites())


@app.post("/compare")
def compare():
    resorts = load_resorts()
    a_id = request.form.get("resort_a", "")
    b_id = request.form.get("resort_b", "")
    if not valid_pair(a_id, b_id, resorts):
        flash("Please select two different valid resorts.", "error")
        return redirect(url_for("home"))
    a, b = find_resort(resorts, a_id), find_resort(resorts, b_id)
    try:
        forecast_a = get_forecast(a)
        forecast_b = get_forecast(b)
    except WeatherError:
        flash("Weather data is unavailable right now. Please try again later.", "error")
        return redirect(url_for("home"))
    return render_template("compare.html", a=a, b=b, fa=forecast_a, fb=forecast_b,
                           summary=build_summary(a, forecast_a, b, forecast_b))


@app.post("/favorites")
def favorites():
    resorts = load_resorts()
    a_id = request.form.get("resort_a", "")
    b_id = request.form.get("resort_b", "")
    if not valid_pair(a_id, b_id, resorts):
        flash("Could not save: choose two different valid resorts.", "error")
        return redirect(url_for("home"))
    try:
        FAVORITES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with FAVORITES_FILE.open("w", encoding="utf-8") as f:
            json.dump({"resort_ids": [a_id, b_id]}, f, indent=2)
    except OSError:
        flash("Could not save favorites. Please try again.", "error")
    else:
        flash("Favorite resorts saved!", "success")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
