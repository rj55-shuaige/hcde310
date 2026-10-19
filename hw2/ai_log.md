# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
I predicted that if there are no artworks by the artist, the function will return an empty list of titles. I was right.


## 2. What clicked
I was confused about how works_by(artist, artworks) works. Now I understand that artist is the artist name we are looking for, and artworks is the list of artwork dictionaries. We go through each artwork in the list, check whether its artist matches the artist we are looking for, and add the title to a new list. At the end, the function returns that list. If there are no matches, it returns an empty list.

## 3. Too much?
No, the tutor only asked me single small question each time. So It helps me to figue out the question myself.


## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
- I was a little bit confused about how to make a definition of takes an artist name and a list of artworks to return a list of titles by that artist.
- That confusion makes sense — this part is introducing functions, so the structure is new.

For now, don’t write the whole function. Think about the inputs and output first.

The function is called works_by(artist, artworks). That means it takes two inputs:

artist: one artist name
artworks: the list of artwork dictionaries
And it should return:

a list of titles made by that artist
Guiding question: if artist were "Claude Monet", what titles from your earlier output do you think should end up in the returned list?
- Stacks of wheat.
- Yes — “Stacks of Wheat (End of Summer)” should be one of them. You also had “Water Lilies” by Claude Monet.
So the function should return a list containing both matching titles.
Next guiding question: when you loop through each artwork dictionary, which key do you think you need to check to decide whether that artwork belongs to Claude Monet?
- Artist.
- Correct — you would check the "artist" key.
Next question: once you find an artwork where the artist matches, which key should you read to add the artwork’s name to your result list?
- Uh, the title.
- Exactly — the title.
So the logic is:
1. Start with an empty list.
2. Look at each artwork.
3. Check whether its "artist" matches the artist passed into the function.
4. If it matches, add that artwork’s "title" to the list.
5. Return the list at the end.
Next question: what do you think the very first thing inside the function should be — an empty list, a print statement, or a return statement?