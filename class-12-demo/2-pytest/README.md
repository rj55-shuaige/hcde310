# Class 12 pytest demo: testing a Flask page

Run the test: python3 -m pytest
Run the app (to compare by hand): python3 app.py, then open http://127.0.0.1:5000

Needs flask, requests and pytest (with .venv on):
python3 -m pip install flask requests pytest

The empty-search test never calls the API, so it works without internet.
