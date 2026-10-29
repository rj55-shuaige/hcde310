# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?

data["data][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths

1. The date of the first artwork: 
data["data"][0]["date_display"]
2. The medium of the second artwork:
data["data"][1]["medium_display"]
3. The image of the third artwork:
data["data"][2]["image_id"]


## 3. Which fields are `null` for some works?

artwork_title is null for the third works

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*

Comes an error cause the url is empty, the python could not send the request.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*

Python gives this error: "requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied. Perhaps you meant https://?" 
Because the url is empty.
The error came from line 16:"response = requests.get(url, params=params)"