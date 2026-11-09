# api.py: calls Open Library for books by an author.
import requests

URL = "https://openlibrary.org/search.json"


def get_books(url, author):
    # Returns two things: (books, error).
    # It worked:   (first 10 books, None)
    # It didn't:   (None, a short reason), so app.py can show a message
    try:
        # timeout=10: stop waiting after 10 seconds instead of hanging forever
        r = requests.get(url, params={"author": author}, timeout=10,
                         headers={"User-Agent": "HCDE310 books app"})
    except requests.RequestException:
        # No answer at all: no wifi, wrong domain, too slow
        return None, "no answer"

    if r.status_code != 200:
        # The server answered, and the answer is "no" (404, 500...)
        return None, f"{r.status_code} {r.reason}"

    return r.json()["docs"][:10], None      # [:10] = the first 10 books
