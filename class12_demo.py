# HCDE 310 Class 12: GET vs. POST, testing a Flask page, spec first, your nouns
# All the code from today's class, for review.
# Run it with: python3 class12_demo.py   (needs flask and requests, with .venv on)
# Tip: before you run each section, predict what it will print.


import requests
from flask import Flask, request


# ---- 1. GET vs. POST ----
# GET is a postcard: what you typed is in the URL (request.args). Bookmark it, share it, refresh it.
# POST is a sealed envelope: the data rides inside the request (request.form). Use it to save or change something.
app = Flask(__name__)
saved = []  # a list in memory: it's empty again every time the app restarts


@app.route("/results")
def results():
    artist = request.args.get("artist", "")       # from the URL: /results?artist=Monet
    if artist == "":
        return "No search term entered."
    return f"Results for {artist}"


@app.route("/save", methods=["POST"])
def save():
    title = request.form.get("title", "")         # from inside the request, not the URL
    saved.append(title)
    return f"Saved {title}. You have {len(saved)} saved."


# test_client() is a pretend browser: no server needed
client = app.test_client()
print("GET: ", client.get("/results?artist=Monet").data)
print("POST:", client.post("/save", data={"title": "Water Lilies"}).data)
# Predict: what does client.get("/save") give? (Only POST is allowed there.)
print("GET /save status:", client.get("/save").status_code)


# ---- 2. Testing a Flask page ----
# A test is a function whose name starts with test_. It asserts what the page should say.
# page.data is bytes, so the text you look for starts with b.
# Run tests with: python3 -m pytest   (here we just call the function ourselves)
def test_empty_search_message():
    page = client.get("/results?artist=")
    assert page.status_code == 200
    assert b"No search term" in page.data


test_empty_search_message()
print("test_empty_search_message passed")


# ---- 3. Spec first, then prompt ----
# Write the spec and the checks BEFORE you open Copilot. Then compare what it gives you with your checks.
#   What:   today's high temperature for a city
#   Input:  a city name
#   Output: "Seattle: 12°C"
#   Checks: Seattle shows a number / "zzzz" shows "No city found" / no internet shows a message, not a crash
HEADERS = {"User-Agent": "HCDE310 class demo"}


def todays_high(city):
    try:
        # Step 1: city name -> latitude and longitude
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                           params={"name": city, "count": 1}, headers=HEADERS, timeout=10).json()
        if "results" not in geo:          # no match: the key is missing, not an empty list
            return "No city found"
        place = geo["results"][0]
        # Step 2: latitude and longitude -> today's high
        weather = requests.get("https://api.open-meteo.com/v1/forecast",
                               params={"latitude": place["latitude"], "longitude": place["longitude"],
                                       "daily": "temperature_2m_max", "timezone": "auto", "forecast_days": 1},
                               headers=HEADERS, timeout=10).json()
    except requests.RequestException:
        return "The weather service isn't answering. Try again in a minute."
    high = weather["daily"]["temperature_2m_max"][0]
    return f"{place['name']}: {round(high)}°C"


print(todays_high("Seattle"))
print(todays_high("zzzz"))
# The checks from the spec, as asserts (the no-internet one: turn off wifi and run again)
assert "°C" in todays_high("Seattle")
assert todays_high("zzzz") == "No city found"


# ---- 4. Commit after every change that works ----
# The loop: make one change -> run your checks -> pass? look at git diff, commit -> fail? git restore app.py
#   git diff
#   git add .
#   git commit -m "Show a message for an empty search"
#   git push
# In pairs: pull before you start, push when you stop.


# ---- 5. What are your nouns? ----
# Every app is about some things. One noun = one dict (Class 3). A list of them = a list of dicts.
artwork = {"title": "Water Lilies", "year": 1906, "artist": "Claude Monet"}
favorites = [artwork, {"title": "The Bedroom", "year": 1889, "artist": "Vincent van Gogh"}]
for a in favorites:
    print(a["title"], a["year"])


# Your nouns are what programmers call classes.
# A class = a template for a noun. An object = one specific thing made from it.
# Read it, don't write it: when AI writes classes for your project, can you tell what each one holds and does?
class Artwork:
    def __init__(self, title, year):
        # data it holds
        self.title = title
        self.year = year

    # something it can do
    def label(self):
        return f"{self.title} ({self.year})"


# Predict first: what does this print?
print(Artwork("Water Lilies", 1906).label())
