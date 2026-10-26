# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*

My plan was to create a function called save_results(artworks, filename). The function would open a text file, loop through the artworks, get the title, artist, and date, and write one artwork on each line. I also wanted to make sure that missing artist information would not appear as None.

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

I used AI to help me understand how to create the save_results function, where to place it in fetch.py, and where to call it after the API search. I also used AI to help me understand why my real API request returned a 403 Forbidden error even though check.py passed.


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

Before running the function, I expected the text file to contain one artwork on each line with the title, artist, and date.

After I ran the program, results.txt was created successfully. It contained the search results, with each artwork written on a separate line using the title, artist, and date.



## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

I was surprised that my code passed all the tests in check.py, but the real API still returned 403 Forbidden at first. I learned that code can be logically correct but a real API may still reject a request because of how the request is sent. After adding a request header, the live API call worked correctly.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed the format of each saved line so the date appears first, followed by the title and artist. I made this change because it makes the results easier to scan in chronological order.