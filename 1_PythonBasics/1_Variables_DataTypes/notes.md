# Variables & Data Types

Welcome to your first Python lesson! Before we write any "real" programs, we need to learn how to store and label information, and what kinds of information Python can work with. That is what this lesson is about.

---

## What is a Variable?

A **variable** is a name that points to a piece of data stored in your computer's memory. Think of it like a labelled box: you put a value inside the box, and you write a name on the outside so you can find it again later.

In Python, you create a variable by **assigning** a value to a name using the `=` sign. This is called **assignment**, and `=` is the **assignment operator**.

```python
x = 5
print(x)      # 5

name = "Alice"
print(name)   # Alice
```

Here, `x` is a variable that now refers to the value `5`. `name` is a variable that refers to the text `"Alice"`.

A few important ideas about assignment:

- The variable name always goes on the **left** of `=`, and the value goes on the **right**.
- `x = 5` does **not** mean "x equals 5" the way it would in maths. It means "take the value 5, and make the name x refer to it."
- You can change what a variable refers to at any time, simply by assigning it a new value:

```python
x = 5
print(x)   # 5
x = 10
print(x)   # 10
```

- You can also assign the result of an expression, not just a plain value:

```python
x = 5
y = x + 1
print(y)   # 6
```

### Variable Naming Rules and Conventions

Python has strict **rules** (things that will cause an error if broken) and looser **conventions** (style habits that good Python programmers follow).

**Rules (must follow):**
- A variable name can only contain letters, numbers, and underscores (`_`).
- A variable name **cannot start with a number** (e.g. `2cats` is invalid, but `cats2` is fine).
- A variable name **cannot contain spaces** (use `_` instead, e.g. `my_variable`).
- A variable name **cannot be a Python keyword** (reserved words like `if`, `for`, `while`, `True`, `None`, etc.).
- Variable names are **case-sensitive**: `age`, `Age`, and `AGE` are three different variables.

**Conventions (good style):**
- Use lowercase words separated by underscores for variable names, e.g. `first_name`, `total_score`. This style is called `snake_case` and is the standard in Python.
- Use descriptive names. `age` is better than `a`; `total_price` is better than `tp`.

```python
# Valid variable names
age = 25
first_name = "Sam"
_temp = 99
score2 = 100

# Invalid variable names (would cause errors) - do not run these!
# 2score = 100        # cannot start with a number
# my name = "Sam"     # cannot contain a space
# class = "Python"    # 'class' is a reserved keyword
```

---

## Core Data Types

Every value in Python has a **type**, which tells Python (and you) what kind of data it is, and what you can do with it. Python has a built-in function called `type()` that tells you the type of any value or variable.

### int (Integer)

An `int` is a whole number — positive, negative, or zero — with no decimal point.

```python
age = 25
temperature = -10
count = 0

print(type(age))   # <class 'int'>
```

### float (Floating-Point Number)

A `float` is a number that has a decimal point. Even `3.0` is a float, not an int, because of the decimal point.

```python
price = 19.99
pi = 3.14159
temperature = -2.5

print(type(price))   # <class 'float'>
```

### str (String)

A `str` (short for "string") is text. You create a string by wrapping characters in either single quotes `'...'` or double quotes `"..."` — both work the same way, just be consistent.

```python
name = "Alice"
greeting = 'Hello there'
letter = "A"

print(type(name))   # <class 'str'>
```

### bool (Boolean)

A `bool` represents one of exactly two values: `True` or `False`. Note the capital letters — this matters in Python! Booleans are often the result of comparisons (which we'll see later in this lesson).

```python
is_raining = True
is_sunny = False

print(type(is_raining))   # <class 'bool'>
```

### None (NoneType)

`None` is a special, unique value in Python that represents "nothing" or "no value at all." It is not the same as `0`, `False`, or an empty string `""` — it means the absence of a value. Its type is called `NoneType`.

```python
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>
```

You'll often see `None` used as a placeholder for a variable that doesn't have a real value yet.

---

## Type Conversion (Casting)

Sometimes you have a value of one type but need it as another type. Python lets you **convert** (or "cast") between types using functions named after the target type: `int()`, `float()`, `str()`, and `bool()`.

```python
# String to int / float
x = int("5")        # 5 (as an int)
y = float("3.14")    # 3.14 (as a float)

# Number to string
z = str(42)          # "42" (as a str)

# Number to bool
a = bool(0)           # False  (0 is treated as "false-y")
b = bool(1)           # True   (any non-zero number is "truth-y")
c = bool("")          # False  (empty string is "false-y")
d = bool("hello")     # True   (non-empty string is "truth-y")

print(x, type(x))
print(y, type(y))
print(z, type(z))
```

A very common use of casting is converting text input into a number so you can do maths with it — we'll see this with `input()` shortly.

**Important:** not every conversion is possible. `int("hello")` will cause an error, because `"hello"` cannot be understood as a number.

---

## Operators

An **operator** is a symbol that performs an operation on one or more values.

### Arithmetic Operators

These perform maths on numbers (`int` or `float`).

```python
a = 7
b = 2

print(a + b)    # 9   addition
print(a - b)    # 5   subtraction
print(a * b)    # 14  multiplication
print(a / b)    # 3.5 division (always returns a float)
print(a // b)   # 3   floor division (divides, then rounds DOWN to whole number)
print(a % b)    # 1   modulo (the REMAINDER after division)
print(a ** b)   # 49  exponent (a to the power of b)
```

The two that trip beginners up most are `//` and `%`:
- `//` (floor division) gives you the whole number result of a division, discarding anything after the decimal point.
- `%` (modulo) gives you the *remainder* left over from that division.

For example, `7 // 2` is `3` (2 goes into 7 three whole times), and `7 % 2` is `1` (with 1 left over).

### Comparison Operators

These compare two values and always produce a `bool` (`True` or `False`).

```python
a = 7
b = 2

print(a == b)   # False   equal to
print(a != b)   # True    not equal to
print(a > b)    # True    greater than
print(a < b)    # False   less than
print(a >= b)   # True    greater than or equal to
print(a <= b)   # False   less than or equal to
```

**Note the difference between `=` and `==`:** `=` assigns a value to a variable, while `==` checks whether two values are equal. This is one of the most common beginner mistakes — see "Common Pitfalls" below.

### Logical Operators

These combine or invert `bool` values.

```python
is_sunny = True
is_warm = False

print(is_sunny and is_warm)   # False  (both must be True)
print(is_sunny or is_warm)    # True   (at least one must be True)
print(not is_sunny)           # False  (flips True to False, or vice versa)
```

- `and` → `True` only if **both** sides are `True`.
- `or` → `True` if **at least one** side is `True`.
- `not` → flips a `bool` to its opposite.

### Augmented Assignment Operators

These are a shorthand for "update a variable based on its current value." Instead of writing `x = x + 1`, you can write `x += 1`.

```python
total = 10

total += 5    # same as: total = total + 5   -> total is now 15
total -= 3    # same as: total = total - 3   -> total is now 12
total *= 2    # same as: total = total * 2   -> total is now 24
total /= 4    # same as: total = total / 4   -> total is now 6.0

print(total)  # 6.0
```

These are extremely common when keeping a running total or counter.

---

## `print()` and `input()`

### `print()`

`print()` displays output to the screen. You can pass it a value directly, a variable, or several values separated by commas (which `print` will display separated by spaces).

```python
print("Hello, world!")

name = "Sam"
age = 30
print(name, "is", age, "years old")   # Sam is 30 years old
```

### `input()`

`input()` pauses your program, displays an optional prompt message, and waits for the user to type something and press Enter. Whatever the user types is returned by `input()`.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

**Crucial fact:** `input()` **always** returns a `str` (string) — even if the user types numbers! If you want to do maths with what the user typed, you must convert it first using `int()` or `float()`.

```python
age_text = input("How old are you? ")   # e.g. user types 25
print(type(age_text))                     # <class 'str'>  <-- still a string!

age = int(age_text)                       # now it's an int
print(age + 1)                            # 26
```

---

## Common Pitfalls

- **Confusing `=` and `==`.** A single `=` assigns a value (`x = 5`). A double `==` compares two values and gives `True`/`False` (`x == 5`). Using `=` when you meant to compare is a very common bug.
- **Confusing `/` and `//`.** `/` always gives a float (e.g. `7 / 2` is `3.5`), while `//` gives the whole-number, rounded-down result (`7 // 2` is `3`). Reach for `//` only when you specifically want to discard the remainder.
- **Forgetting that `input()` always returns a string.** Even if the user types `"25"`, `input()` gives you back the text `"25"`, not the number `25`. If you try to do `input("Age: ") + 1` without converting, Python will raise an error because you can't add a string and an int directly.
- **Breaking variable naming rules.** Variable names cannot start with a digit (`1st_place` is invalid), cannot contain spaces, and cannot be one of Python's reserved keywords (like `True`, `for`, or `if`).
- **Mixing up `True`/`False` capitalisation.** Python's booleans are capitalised: `True` and `False`. Writing `true` or `false` (lowercase) will cause an error, since Python treats those as undefined variable names, not booleans.
