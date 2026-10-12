# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

for i in range(len(titles)):
    print(f"{i + 1}. {titles[i]}")

print(f"Titles: {len(titles)}")

count = 0
for title in titles:
    if "a" in title.lower():
        count += 1
print(f'Titles with an "a": {count}')

longest = ""
for title in titles:
    if len(title) > len(longest):
        longest = title
print(f"Longest: {longest}")