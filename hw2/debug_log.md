# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
TypeError: type 'itertools.count' is not subscriptable


### 2. What I thought it meant
I thought something wrong with the dictionary.

### 3. What it actually meant
Inside if statement I accidentally wrote count[artist] instead of counts[artist]. Python could not find a variable named count.

### 4. The fix
Change count[artist] to counts[artist]

## Entry 2

### 1. Error message
SyntaxError: invalid character '）' (U+FF09)


### 2. What I thought it meant
I thought might be a spelling mistake

### 3. What it actually meant
I used a Chinese closing parenthesis ）instead of an English closing parenthesis ). Python does not recognize it.

### 4. The fix
Replace to the English parenthesis.