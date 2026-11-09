# test_books.py: a test does what you'd check by hand, in code.
# Run from this folder:  python3 -m pytest
# (First time: python3 -m pip install pytest, with .venv on)
from app import app


def test_empty_search_message():
    # By hand: open a browser
    client = app.test_client()        # a pretend browser: no server, no window

    # By hand: type /results?author_search= in the address bar (an empty search)
    page = client.get("/results?author_search=")

    # By hand: see that the page loaded
    assert page.status_code == 200    # 200 = loaded fine, same as with APIs

    # By hand: read the page and see "No search term"
    assert b"No search term" in page.data   # page.data is bytes, so the text starts with b


# Try it: change b"No search term" to b"Banana" and run again.
# The test fails, and pytest shows which assert. A failing test is a good find.
