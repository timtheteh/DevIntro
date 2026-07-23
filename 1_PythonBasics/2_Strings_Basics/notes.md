# Strings Basics

Strings are how Python stores text. You've already used them a little with `print()` and `input()` — now let's look at how they actually work.

## String Literals: Single Quotes vs Double Quotes

You can create a string using either single quotes `'...'` or double quotes `"..."`. Python treats them exactly the same way — the choice is mostly about convenience, especially when your text contains a quote character itself.

```python
name = 'Alice'
greeting = "Hello there"

# Handy when the text contains an apostrophe:
sentence = "It's a sunny day"

# Or when the text contains double quotes:
quote = 'She said "hello" to me'

print(name)
print(greeting)
print(sentence)
print(quote)
```

## Concatenation with `+` and Repetition with `*`

You can join strings together using `+`, and repeat a string multiple times using `*`.

```python
first = "Py"
second = "thon"
combined = first + second   # "Python"
print(combined)

# Adding a space between words
full_name = "Ada" + " " + "Lovelace"
print(full_name)

# Repetition
line = "-" * 10   # "----------"
print(line)

laugh = "ha" * 3  # "hahaha"
print(laugh)
```

## Indexing (Positive and Negative)

Every character in a string has a position, called an index. Indexing starts at **0**, not 1. You can also count backwards from the end using negative indices, where `-1` is the last character.

```python
word = "Python"

print(word[0])    # 'P'  (first character)
print(word[1])    # 'y'  (second character)
print(word[5])    # 'n'  (last character)

print(word[-1])   # 'n'  (last character)
print(word[-2])   # 'o'  (second-to-last character)
```

## Slicing: `s[start:end]`

Slicing lets you pull out a chunk of a string. `s[start:end]` gives you the characters from index `start` up to (but **not including**) index `end`.

```python
word = "Python"

print(word[0:2])   # 'Py'   (indices 0 and 1)
print(word[2:6])   # 'thon' (indices 2, 3, 4, 5)

# Leaving out start means "from the beginning"
print(word[:4])    # 'Pyth'

# Leaving out end means "to the end"
print(word[2:])    # 'thon'
```

## `len()` on Strings

`len()` tells you how many characters are in a string (including spaces).

```python
message = "Hello, world"
print(len(message))   # 12

empty = ""
print(len(empty))     # 0
```

## Common String Methods

Methods are functions that belong to a string, called using dot notation: `my_string.method_name()`.

```python
text = "  Hello World  "

print(text.upper())     # '  HELLO WORLD  '
print(text.lower())     # '  hello world  '
print(text.strip())     # 'Hello World'  (removes leading/trailing whitespace)

sentence = "I like cats"
print(sentence.replace("cats", "dogs"))   # 'I like dogs'

words = "I like cats".split()
print(words)             # ['I', 'like', 'cats']  (splits on whitespace by default)

csv_line = "apple,banana,cherry"
print(csv_line.split(","))   # ['apple', 'banana', 'cherry']  (splits on a given character)

# join() does the opposite of split() — it combines a list of strings using a separator
parts = ["apple", "banana", "cherry"]
print(",".join(parts))       # 'apple,banana,cherry'
print(" ".join(["I", "like", "cats"]))  # 'I like cats'
```

### Checking for a Substring with `in`

The `in` operator checks whether one string appears inside another, and gives back `True` or `False`.

```python
sentence = "The quick brown fox"

print("quick" in sentence)   # True
print("slow" in sentence)    # False
print("Quick" in sentence)   # False (case-sensitive!)
```

## Converting Non-String Values to Strings with `str()`

You can only use `+` to join strings together with other strings. If you want to concatenate a number (or other type) onto a string, you need to convert it first using `str()`.

```python
age = 12
# print("I am " + age + " years old")   # This would cause a TypeError!

message = "I am " + str(age) + " years old"
print(message)   # 'I am 12 years old'

price = 4.5
print("The price is $" + str(price))
```

> Note: Later on you'll learn about f-strings and `.format()`, which are much more powerful and convenient ways to build strings with values mixed in. For now, focus on getting comfortable with `+` and `str()`.

## Common Pitfalls

- **Strings are immutable** — you cannot change a character in place (e.g. `word[0] = "J"` will raise an error). Instead, you create a *new* string, for example with slicing, concatenation, or `.replace()`.
- **Off-by-one errors in indexing/slicing** — remember indexing starts at `0`, and `s[start:end]` does **not** include the character at `end`. `word[0:3]` gives you 3 characters (indices 0, 1, 2), not 4.
- **Forgetting `str()` when concatenating a number** — `"Score: " + 10` raises a `TypeError`. You must write `"Score: " + str(10)`.
- **Mixing quote styles with apostrophes** — `'It's a test'` is a syntax error, because Python thinks the string ends right after `It`. Use double quotes instead (`"It's a test"`), or escape the apostrophe.
- **Methods don't change the original string** — `text.upper()` returns a *new* string; it doesn't modify `text` itself. If you want to keep the result, you need to assign it: `text = text.upper()`.
