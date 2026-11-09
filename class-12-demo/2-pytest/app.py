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
