# String Syntax — Tutoring Notes

These notes assume you're already comfortable with strings as a data type
and basic operations (indexing, slicing, concatenation). The focus here is
purely on **syntax**: the different ways Python lets you write, format, and
manipulate string literals.

---

## 1. f-strings (Formatted String Literals)

An f-string is a string literal prefixed with `f` (or `F`). Any expression
inside `{}` is evaluated and inserted into the string.

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")   # Ada is 36 years old
```

### Nested expressions
You can put arbitrary expressions — including function calls, arithmetic,
and even other strings — inside the braces.

```python
items = ["pen", "book", "cup"]
print(f"First item (upper): {items[0].upper()}")
print(f"Total items: {len(items) * 2}")
```

### Format specs — `f"{x:.2f}"`
After a `:`, you can add a **format spec** to control width, precision,
alignment, thousands separators, percentages, etc.

```python
pi = 3.14159265
price = 1234.5

print(f"{pi:.2f}")        # 3.14   -> 2 decimal places
print(f"{price:,.2f}")    # 1,234.50 -> thousands separator + 2 dp
print(f"{price:>10.2f}")  # right-align in a 10-char field
print(f"{0.4567:.1%}")    # 45.7%  -> percentage with 1 dp
print(f"{42:08d}")        # 00000042 -> zero-padded integer, width 8
print(f"{42:b}")          # 101010 -> binary
```

### Conversion flags — `f"{x!r}"`
`!r`, `!s`, and `!a` call `repr()`, `str()`, or `ascii()` on the value
*before* formatting.

```python
text = "line\n"
print(f"{text}")     # prints with an actual newline
print(f"{text!r}")   # 'line\n'  -> shows the repr, escapes visible
```

### The `=` debug specifier — `f"{x=}"`
Added in Python 3.8. It prints both the expression text and its value —
great for quick debugging without writing `print("x:", x)`.

```python
width = 10
height = 4
print(f"{width=}")               # width=10
print(f"{width * height=}")      # width * height=40
print(f"{width=:.2f}")           # width=10.00  (combine with a format spec)
```

---

## 2. `.format()` Method Syntax

The older, more explicit way to format strings. Placeholders `{}` in the
string are filled in by arguments to `.format()`.

```python
# Positional (implicit order)
print("{} is {} years old".format("Ada", 36))

# Positional (explicit index) — allows reuse/reordering
print("{0} scored {1}, {0} wins!".format("Ada", 95))

# Keyword arguments
print("{name} is {age} years old".format(name="Ada", age=36))

# Format specs work the same way as f-strings, after a colon
print("{:.2f}".format(3.14159))     # 3.14
print("{:,.2f}".format(1234.5))     # 1,234.50
print("{:>10}".format("hi"))        # right-aligned in width 10
```

---

## 3. String Methods (Syntax Patterns)

A quick syntax refresher on frequently used string methods. All are called
on a string instance and (with the exception of `join`) most return a
**new** string or list — strings are immutable.

```python
s = "  Hello, World, Foo  "

s.strip()            # "Hello, World, Foo"   -> removes leading/trailing whitespace
s.strip(" H")         # strips specific chars from both ends
s.lstrip(); s.rstrip()  # strip only left / only right

s.split(",")          # ["  Hello", " World", " Foo  "]
s.split(",", maxsplit=1)  # limit number of splits

",".join(["a", "b", "c"])   # "a,b,c"  -> note: called ON the separator

s.replace("Hello", "Hi")    # replace all occurrences
s.replace("o", "0", 1)      # replace only first N occurrences

s.lower(); s.upper(); s.title(); s.capitalize()

s.startswith("  He")  # True
s.endswith("Foo  ")   # True

s.find("World")       # index, or -1 if not found
s.index("World")      # index, or raises ValueError if not found

s.count("o")           # number of occurrences
```

---

## 4. Multi-line Strings (Triple-Quoted Strings)

Enclose a string in `"""` or `'''` to let it span multiple lines. Newlines
in the source are preserved literally in the string value.

```python
message = """Dear Ada,

Thank you for your submission.
Regards,
The Committee"""

print(message)
```

Triple-quoted strings are also commonly used for docstrings:

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"
```

You can combine the triple-quote syntax with the `f` or `r` prefixes:

```python
name = "Ada"
note = f"""Hi {name},
this is line two."""
```

---

## 5. Raw Strings (`r"..."`)

Prefixing a string literal with `r` (or `R`) tells Python to treat
backslashes as **literal characters**, not the start of an escape
sequence. The string still ends where a matching quote appears.

```python
path = r"C:\Users\Ada\Documents"
print(path)             # C:\Users\Ada\Documents  (backslashes kept as-is)

pattern = r"\d+\.\d+"   # common for regex patterns
print(pattern)          # \d+\.\d+
```

Note: a raw string **cannot end with an odd number of backslashes**,
because the backslash still escapes the quote character itself:

```python
# bad = r"C:\path\"   # SyntaxError
good = r"C:\path" + "\\"   # workaround if you need a trailing backslash
```

---

## 6. Escape Sequences

Inside a normal (non-raw) string, a backslash starts an escape sequence —
a way to represent characters that are hard or impossible to type
directly.

```python
print("Line one\nLine two")     # \n -> newline
print("Col1\tCol2\tCol3")       # \t -> tab
print("She said \"hi\"")        # \" -> literal double quote
print('It\'s fine')             # \' -> literal single quote
print("Back\\slash")            # \\ -> a single literal backslash
print("Bell sound: \a")         # \a -> ASCII bell (rarely used)
print("Unicode: \u00e9")        # \uXXXX -> unicode code point (é)
```

You can also escape a quote of the *other* type without a backslash by
choosing the enclosing quote style:

```python
a = "It's fine"       # no need to escape ' inside "..."
b = 'She said "hi"'   # no need to escape " inside '...'
```

---

## Common Pitfalls

- **Forgetting `r"..."` for paths and regex.** Writing `"C:\new\test"`
  silently mangles the string because `\n` and `\t` are interpreted as
  newline/tab. Use `r"C:\new\test"` (or forward slashes) instead.
- **Mixing up `.format()` positional indices** — reusing `{0}` without
  realizing later `{}` (auto-numbered) placeholders can't be mixed with
  explicit `{0}`/`{1}` in the *same* `.format()` call; Python will raise
  a `ValueError`.
- **Malformed f-string format specs**, e.g. `f"{x:.2}"` (precision without
  a type, giving unexpected general formatting) vs `f"{x:.2f}"` (fixed-point
  float) — the trailing type character (`f`, `d`, `%`, `b`, etc.) matters.
- **Forgetting that f-strings evaluate at runtime**, not `.format()`-style
  — you cannot build an f-string template once and reuse it later with
  different variable values the way you can with `.format()`.
- **A raw string can't end in a single backslash** (`r"path\"` is a
  `SyntaxError`) because the backslash still escapes the following quote
  character.
