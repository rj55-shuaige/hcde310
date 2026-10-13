# Class 4: Five broken snippets

Your name: 
Collaborator: 

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? 
- What error will Python show? (the kind and the message)
- What's the fix?

- Line 8 breaks.
- Would show a key error since the letter "r" in "room" should be lower case not upper case. 
- Change "R" to "r"
## Snippet 2
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

- Line 12 breaks
- Would show a type error since a string cannot follow by an integer
- Change "exhibit["room"]" to "str(exhibit["room"])"
## Snippet 3
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

- Line 16 breaks
- Would show a index error since it's out of range
- change "range(len(exhibits) + 1)" into "range(len(exhibits))"

## Snippet 4
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

- line 29 breaks 
- Name error since the vaiable in the function is "visits" not "visit"
- change "visit" to "visits"

## Snippet 5
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

- line 41 will break
- key error? since there is no return value for the function
- change line 38 "print(longest)" to "return longest"

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
- What error did Python show?
- What's the fix?

- same
## Snippet 2
- Which line broke?
- What error did Python show?
- What's the fix?

- same

## Snippet 3
- Which line broke?
- What error did Python show?
- What's the fix?

- line 17 broke

## Snippet 4
- Which line broke?
- What error did Python show?
- What's the fix?

- Same
## Snippet 5
- Which line broke?
- What error did Python show?
- What's the fix?

- attribute error
When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5
- Our guess before asking: We guessed that the problem was related to print(longest). We thought the function should return the longest title instead of only printing it.
- Chat: The tutor explained that longest_title() prints the longest title but does not return it. Because there is no return, the variable title becomes None. Then title.upper() causes an AttributeError. The fix is to change print(longest) to return longest.
- Did it give you too much? What did you do?
t gave more explanation than we needed. We focused on the error type and the one line that needed to be changed.