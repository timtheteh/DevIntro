# Data Structures — Syntax Notes

Focus: the *syntax* of Python's built-in container types, unpacking, and
comprehensions. This assumes you're already comfortable with variables,
data types, strings, dicts, lambdas, and sorting — so no re-teaching of
those basics here.

---

## List, Tuple, Set, Dict Literal Syntax

```python
my_list = [1, 2, 3]          # mutable, ordered
my_tuple = (1, 2, 3)         # immutable, ordered
my_set = {1, 2, 3}           # mutable, unordered, unique elements
my_dict = {"a": 1, "b": 2}   # mutable, ordered (insertion order), key-value

# empty containers
empty_list = []
empty_tuple = ()
empty_set = set()      # NOT {} — that's an empty dict!
empty_dict = {}

# single-element tuple needs a trailing comma
single_tuple = (1,)    # a tuple containing 1
not_a_tuple = (1)      # just the int 1, parentheses are grouping only

print(type(single_tuple), type(not_a_tuple))
```

---

## Indexing

Works on lists, tuples, and strings (anything ordered/sequence-like).
Sets and dicts are NOT indexable by position (dicts are indexed by key).

```python
a = [10, 20, 30, 40, 50]

print(a[0])     # 10  -> first element
print(a[-1])    # 50  -> last element
print(a[-2])    # 40  -> second-to-last

d = {"x": 1, "y": 2}
print(d["x"])   # 1   -> lookup by key, not position
```

---

## Slicing (including extended slicing)

Slice syntax is `sequence[start:stop:step]`. `start` is inclusive,
`stop` is exclusive. Any of the three parts can be omitted.

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:3])     # [1, 2]        -> index 1 up to (not including) 3
print(a[:4])      # [0, 1, 2, 3]  -> start defaults to 0
print(a[6:])      # [6, 7, 8, 9]  -> stop defaults to len(a)
print(a[:])       # full shallow copy of the list

print(a[::-1])    # [9, 8, ..., 0] -> step -1 reverses the sequence
print(a[::2])     # [0, 2, 4, 6, 8] -> every 2nd element
print(a[1:8:2])   # [1, 3, 5, 7]    -> start, stop, and step combined

print(a[-3:])     # [7, 8, 9]     -> negative indices count from the end
print(a[:-3])     # [0, 1, ..., 6] -> everything except the last 3

# slicing works the same way on tuples and strings
t = (0, 1, 2, 3, 4)
print(t[1:3])     # (1, 2)
s = "hello world"
print(s[::-1])    # "dlrow olleh"
```

Sets and dicts do not support slicing (no fixed order to slice by index).

---

## Unpacking

Assign multiple variables at once from an iterable. The number of names
must match the number of elements, unless you use a starred `*name` to
soak up the rest.

```python
a, b, c = [1, 2, 3]
print(a, b, c)          # 1 2 3

# starred unpacking — grabs "the rest" into a list
first, *rest = [1, 2, 3, 4, 5]
print(first, rest)      # 1 [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

*rest, last = [1, 2, 3, 4, 5]
print(rest, last)       # [1, 2, 3, 4] 5

# nested unpacking
(a, b), c = [(1, 2), 3]
print(a, b, c)          # 1 2 3

# swapping values uses tuple unpacking under the hood
x, y = 1, 2
x, y = y, x
print(x, y)             # 2 1

# unpacking works with any iterable, including strings
p, q, r = "xyz"
print(p, q, r)           # x y z
```

---

## List Comprehensions

Syntax: `[expression for item in iterable if condition]`

```python
squares = [n ** 2 for n in range(6)]
print(squares)                       # [0, 1, 4, 9, 16, 25]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)                         # [0, 2, 4, 6, 8]

# nested loops inside a comprehension, read left-to-right like nested for-loops
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)                         # [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]

# conditional expression inside the mapped value (ternary, not a filter)
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
print(labels)                        # ['even','odd','even','odd','even']
```

---

## Dict Comprehensions

Syntax: `{key_expr: value_expr for item in iterable if condition}`

```python
squares_by_n = {n: n ** 2 for n in range(5)}
print(squares_by_n)                  # {0:0, 1:1, 2:4, 3:9, 4:16}

# building a dict from two parallel lists via zip
names = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(names, values)}
print(combined)                      # {'a':1, 'b':2, 'c':3}

# inverting a dict (keys <-> values)
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
print(inverted)                      # {1: 'a', 2: 'b'}
```

---

## Set Comprehensions

Syntax: `{expression for item in iterable if condition}` — note the
braces are the same as a dict comprehension, but there's no `:`.

```python
unique_lengths = {len(word) for word in ["hi", "bye", "yo", "hey"]}
print(unique_lengths)                # {2, 3} -- duplicates collapse automatically

remainders = {n % 3 for n in range(10)}
print(remainders)                    # {0, 1, 2}
```

---

## Generator Expressions

Syntax looks like a list comprehension but with `(...)` instead of
`[...]`. The key syntactic/behavioral difference: a generator expression
is **lazy** — it produces values one at a time on demand and does not
build the whole collection in memory, and it can only be iterated once.

```python
squares_list = [n ** 2 for n in range(5)]   # built immediately, a list
squares_gen = (n ** 2 for n in range(5))    # lazy, a generator object

print(type(squares_list))    # <class 'list'>
print(type(squares_gen))     # <class 'generator'>

print(list(squares_gen))     # [0, 1, 4, 9, 16] -- forces evaluation
print(list(squares_gen))     # [] -- already exhausted, can't reuse it

# generator expressions can be passed directly as a single function argument
# without extra parentheses
total = sum(n ** 2 for n in range(5))
print(total)                 # 30
```

---

## Common Pitfalls

- **Off-by-one slicing errors** — remember `stop` is *exclusive*.
  `a[1:3]` gives you indices 1 and 2, not 1 through 3.
- **`(1,)` vs `(1)`** — a trailing comma is what makes a tuple; `(1)` is
  just the integer `1` in parentheses. `()` alone is an empty tuple, but
  `{}` alone is an empty **dict**, not an empty set (use `set()`).
- **Mutability confusion** — lists and sets are mutable (can be changed
  in place with `.append()`, `.add()`, item assignment, etc.); tuples are
  immutable. This also means tuples (and not lists) can be used as dict
  keys or set elements, since those need hashable elements.
- **Comprehension variable scoping** — the loop variable inside a
  comprehension (e.g. the `n` in `[n for n in range(5)]`) does **not**
  leak into the enclosing scope in Python 3 (unlike a regular `for`
  loop). Don't rely on it existing after the comprehension runs.
- **Reusing a generator expression** — a generator is exhausted after
  one full iteration. If you need to iterate the same data twice, use a
  list/tuple comprehension instead, or recreate the generator.
