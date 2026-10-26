# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display,image_id"

# Functions go here (above the code that runs)
def count_by_artist(artworks):
    counts = {}
    for artwork in artworks:
        artist = artwork.get("artist_title", "Unknown")
        if artist is None:
            artist = "Unknown"
        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1
    return counts

def save_results(artworks, filename):
    with open(filename, "w") as file:
        for artwork in artworks:
            title = artwork.get("title", "No title available")
            artist = artwork.get("artist_title")
            if artist is None:
                artist = "Unknown artist"
            date = artwork.get("date_display", "No date available")
            file.write(f"{date} - {title} - {artist} \n")


term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"  
params = {"q": term, "fields": FIELDS} 
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    if not data["data"]:
        print("No results found.")
    else:
        for artwork in data["data"]:
            title = artwork.get("title", "No title available")
            artist = artwork.get("artist_title")
            if artist is None:
                artist = "Unknown artist"
            date = artwork.get("date_display", "No date available")
            medium = artwork.get("medium_display", "No medium available")
            image_id = artwork.get("image_id", "No image available")
            print(f"Title: {title}, Artist: {artist}, Date: {date}, Medium: {medium}, Image ID: {image_id}")
        counts = count_by_artist(data["data"])
        save_results(data["data"], "results.txt")
        print(counts)
else:
    print(f"Error: {response.status_code}, {response.reason}")

