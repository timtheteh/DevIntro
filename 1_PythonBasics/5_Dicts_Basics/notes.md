# Dicts — Syntax Notes

These notes assume you're already comfortable with variables, data types,
strings, control flow, and lists. The focus here is purely the **syntax** of
Python's dictionary (`dict`) type — not algorithms or applied problem
solving. (Dict comprehensions are covered later, in the more advanced Data
Structures lesson.)

A dict stores a collection of **key: value** pairs. Instead of looking up an
item by its position (like a list), you look it up by its key.

---

## Creating a dict (`{key: value}`)

A dict literal is written with curly braces `{}`, with each entry as
`key: value`, separated by commas.

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(ages)          # {'Alice': 30, 'Bob': 25, 'Charlie': 35}
print(type(ages))    # <class 'dict'>

empty = {}            # an empty dict
print(type(empty))    # <class 'dict'>
```

- Keys are usually strings or numbers, but any **immutable** (hashable) type
  can be a key — see Common Pitfalls below.
- Values can be *anything* — numbers, strings, lists, even other dicts.
- `{}` on its own creates an **empty dict**, not an empty set.

---

## Accessing values by key (`d[key]`) and `.get()`

Use square brackets with a key (instead of an index) to retrieve a value.

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(ages["Bob"])   # 25
```

If the key doesn't exist, `d[key]` raises a `KeyError` and crashes the
program. The `.get()` method is a safer alternative — it returns `None`
(instead of crashing) if the key is missing:

```python
print(ages.get("Bob"))       # 25
print(ages.get("Diana"))     # None  (no error!)
```

`.get()` also accepts a second argument: a **default value** to return
instead of `None` when the key is missing.

```python
print(ages.get("Diana", 0))            # 0
print(ages.get("Diana", "not found"))  # not found
```

---

## Adding/updating a key, removing a key

To add a new key or update an existing one, assign to `d[key]` — Python
figures out automatically whether it's a new key or an existing one.

```python
ages = {"Alice": 30, "Bob": 25}

ages["Charlie"] = 35   # adds a new key
print(ages)             # {'Alice': 30, 'Bob': 25, 'Charlie': 35}

ages["Bob"] = 26        # updates an existing key
print(ages)             # {'Alice': 30, 'Bob': 26, 'Charlie': 35}
```

There are two common ways to remove a key: the `del` statement, and the
`.pop()` method (which also *returns* the removed value).

```python
del ages["Charlie"]
print(ages)              # {'Alice': 30, 'Bob': 26}

removed_value = ages.pop("Bob")
print(removed_value)     # 26
print(ages)               # {'Alice': 30}
```

- `.pop()` also accepts a default value as a second argument, so it won't
  crash if the key is missing: `ages.pop("Zoe", None)`.

---

## Checking key existence with `in`

Use the `in` operator to check whether a key exists in a dict **before**
trying to access it — this avoids `KeyError` crashes.

```python
ages = {"Alice": 30, "Bob": 25}

print("Alice" in ages)   # True
print("Zoe" in ages)     # False

if "Bob" in ages:
    print(ages["Bob"])   # 25
```

- `in` checks against the **keys** only, not the values.
- `not in` works the same way: `if "Zoe" not in ages:`.

---

## Iterating over a dict: keys, `.values()`, `.items()`

Looping over a dict directly with `for` gives you the **keys** by default.

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

for name in ages:            # loops over keys by default
    print(name)
    # Alice
    # Bob
    # Charlie
```

This is exactly the same as looping over `.keys()` explicitly:

```python
for name in ages.keys():
    print(name)
```

To loop over just the **values**, use `.values()`:

```python
for age in ages.values():
    print(age)
    # 30
    # 25
    # 35
```

To loop over **both** the key and the value together, use `.items()` — each
iteration gives you a `(key, value)` pair, which you can unpack directly into
two loop variables:

```python
for name, age in ages.items():
    print(name, "is", age, "years old")
    # Alice is 30 years old
    # Bob is 25 years old
    # Charlie is 35 years old
```

---

## Common Pitfalls

- **`KeyError` from accessing a missing key with `[]`** — `d["missing_key"]`
  crashes the program if the key isn't there. Use `.get()` (optionally with
  a default value) when the key might not exist, and reserve `d[key]` for
  cases where you're sure the key is present.
- **Keys must be immutable (hashable)** — strings, numbers, and tuples can
  be dict keys, but **lists cannot** (`{[1, 2]: "value"}` raises a
  `TypeError`), because lists can change after they're created.
- **Forgetting `.items()` when you need both key and value** — looping with
  `for name in ages:` only gives you the key. If you then write
  `ages[name]` inside the loop to get the value too, it works, but it's
  simpler and more direct to loop with `for name, age in ages.items():`
  and get both at once.
- **Dict keys are unique — duplicate keys silently overwrite** — writing
  `{"a": 1, "a": 2}` does not raise an error; the second `"a": 2` simply
  overwrites the first, leaving `{"a": 2}`. The same happens if you assign
  `d["a"] = ...` twice with the same key.
- **Checking `in` against values instead of keys** — `"Alice" in ages`
  checks the keys. If you want to check whether a *value* exists, you need
  `30 in ages.values()` instead — `in` on the dict itself never looks at
  the values.
