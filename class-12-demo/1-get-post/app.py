# app.py: the routes for the books app.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books, URL

app = Flask(__name__)


def are_fields_empty(books):
    # True if no book has a title (so there's nothing useful to show), False otherwise
    for book in books:
        if book.get("title"):
            return False
    return True


@app.route("/")
def home():
    return render_template("home.html")


# GET vs. POST demo: this route uses GET (the search shows in the URL).
# To flip it to POST, change 3 things together:
#   1. templates/home.html:  <form action="/results" method="post">
#   2. here:                 @app.route("/results", methods=["POST"])
#   3. here:                 request.form.get(...) instead of request.args.get(...)
# Change only 1 and you get "405 Method Not Allowed". For a search, which one would you pick?
@app.route("/results")
def results():
    author = request.args.get("author_search", "").strip()   # "" if missing

    # Empty input: check BEFORE calling the API
    if author == "":
        return render_template("home.html", message="No search term entered.")

    books, error = get_books(URL, author)

    # API error: no answer, or the answer was "no"
    if error:
        print("API error:", error)          # for you, in the terminal
        return render_template("home.html",
                               message="The library isn't answering. Try again in a minute.")

    # No results, or results with no titles at all
    if len(books) == 0 or are_fields_empty(books):
        return render_template("home.html", message=f'No results found for "{author}".')

    # Happy path (books with a missing title are skipped in the template)
    return render_template("results.html", books=books, author=author)


if __name__ == "__main__":
    app.run(debug=True)
