# HW5 findings

## 1. Drawing: one search for "Monet"
(photo here)

## 2. Two questions about the code
1. What do request.values.get("artist") do and why use "strip" after that
2. Why does the /result route allow both method equal to a list

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | The home page sows an artist search form | Pass |
| 2 | Shows error message when search with empty input | Pass |
| 3 | Searching for artist name like "monet" displays artwork titles, dtaes adn images | Pass |
| 4 | searching for a nonexist artist should display "No results found." | Fail |

## 4. AI review
What it found that I missed: 

AI found some problems that I did not notice before. In app.py, line 20 catches all exceptions instead of specific errors. Line 21 also shows detailed error messages to users, which might not be safe. Another issue is debug=True on line 26, which should not be used when the website is public. AI also suggested improving error handling and accessibility.

What it got wrong:

AI initially suggested that using the q parameter in api.py was a bug because it does not always return artworks by the exact artist. However, I checked prompt.md and found that the original instructions specifically asked for the q parameter. So the code follows the prompt, even though the search results are sometimes inaccurate.

Answers to my two questions, in my own words:

request.values.get("artist") gets the artist name from the user's input. The .strip() removes extra spaces before and after the name. This helps the app get a cleaner search term.

The list tells Flask that the route can accept both GET and POST requests. GET is usually used to get information, while POST is used to submit form data. Using both allows the route to handle different types of requests.

## 5. My fix
What was wrong: 
The app showed detailed error messages when the API failed. This might expose private information about the code.

What I changed: 
I changed app.py to show a simple error message instead. I also added logging to help find errors.

How I checked it works: 
I added a new test in test_app.py to simulate an API error. I ran python3 -m pytest -v, and all three tests passed.

Commit before: 393519b  Commit after: 53e38fd

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
