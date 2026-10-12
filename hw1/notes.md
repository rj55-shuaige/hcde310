# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
"len(titles)" is asking for the len of the list "titles", which is the number of items in the list, so output is 10. "len(titles[0])" counts the number of characters in the first item of the list, which is "The Bedroom", so output is 11.

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

For the Day one app, I could now recognize some python language in it. At the very beginning, the app use lists to store different artworks and their related information. Also for the searching box of the app, I think it used loops and "if else" statement to loop over all artworks to get the best match of what users are typing in. After this week of study, I feel like getting more familiar of what is going on in a period of code.