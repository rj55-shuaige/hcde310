import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display,image_id"


def search_art(term):
    # Search the Art Institute API using the user's search term
    url = "https://api.artic.edu/api/v1/artworks/search"

    params = {"q": term, "fields": FIELDS}

    headers = {"AIC-User-Agent": "HCDE310 student project"}

    response = requests.get(url, params=params, headers=headers)

    # If the API request works, return the artwork list
    if response.status_code == 200:
        data = response.json()
        return data["data"]

    # If the API request fails, return None
    return None