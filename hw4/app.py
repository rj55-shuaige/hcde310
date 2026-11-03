from flask import Flask, render_template, request
from api import search_art

app = Flask(__name__)


# Home route
# Show the search form
@app.route("/")
def home():
    return render_template("home.html")


# Results route
# 1. Get the search term from the form
# 2. Check if the search term is empty
# 3. Call the API search function
# 4. Check if the API had an error
# 5. Check if there are no results
# 6. Send the results to results.html

@app.route("/results")
def results():
    search_term = request.args.get("search", "")
    
    # Check if the user submitted an empty search
    if search_term.strip() == "":
        return render_template(
            "results.html",
            search_term=search_term,
            artworks=[],
            message="Please enter a search term."
        )

    # Call the API search function with the user's search term
    artworks = search_art(search_term)
    
    # Check if the API request failed
    if artworks is None:
        return render_template(
            "results.html",
            search_term=search_term,
            artworks=[],
            message="Sorry, there was a problem getting artwork data."
        )
    
    # Check if there are no results
    if artworks == []:
        return render_template(
            "results.html",
            search_term=search_term,
            artworks=[],
            message="No results found."
        )

    return render_template("results.html", search_term=search_term, artworks=artworks)


if __name__ == "__main__":
    app.run(debug=True)