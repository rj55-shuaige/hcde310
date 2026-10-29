def label(year):
   if year < 1900:
         return "old"
   return "modern"
print(label(1889), label(1942))

myList = ["cats", "dogs", "goats"]
for i in range(len(myList)):
    print(f"{i + 1}. {myList[i]}")

