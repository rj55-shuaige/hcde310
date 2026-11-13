# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page

def test_empty_search():
    client = app.test_client()
    page = client.post("/results", data={"artist": ""})

    assert page.status_code == 200
    assert b"No search term entered." in page.data

def test_api_error(monkeypatch):
    def fake_get_artworks(artist):
        raise Exception("Secret internal error")

    monkeypatch.setattr("app.get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b"Sorry, something went wrong." in page.data
    assert b"Secret internal error" not in page.data