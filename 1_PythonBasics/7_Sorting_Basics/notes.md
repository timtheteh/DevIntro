# Sorting Basics — Syntax Notes

These notes assume you're already comfortable with variables, data types,
strings, control flow, lists, dicts, and lambda basics. The focus here is
purely the **syntax** of Python's built-in sorting tools — not sorting
algorithms (no bubble sort, no writing your own sort from scratch).

---

## `sorted()` vs `.sort()`

Python gives you two ways to sort: the **`sorted()` function** and the
**`.sort()` list method**. They are not interchangeable.

- `sorted(iterable)` — a built-in **function**. It works on any iterable
  (list, tuple, string, etc.) and returns a **brand-new list**, leaving the
  original untouched.
- `my_list.sort()` — a **method** that only exists on lists. It sorts the
  list **in place** (modifies the original list) and returns `None`.

```python
numbers = [4, 2, 9, 1]

# sorted() — returns a new list, original is untouched
new_list = sorted(numbers)
print(new_list)   # [1, 2, 4, 9]
print(numbers)     # [4, 2, 9, 1]  <- unchanged

# .sort() — sorts in place, returns None
result = numbers.sort()
print(numbers)     # [1, 2, 4, 9]  <- changed!
print(result)       # None
```

- Use `sorted()` when you want to keep the original order around, or when
  you're sorting something that isn't a list (e.g. a tuple or the characters
  of a string).
- Use `.sort()` when you genuinely want to reorder the list you already have
  and don't need the original order anymore.

---

## The `reverse=True` argument

Both `sorted()` and `.sort()` accept a `reverse` keyword argument. By
default sorting is ascending (`reverse=False`); pass `reverse=True` to sort
descending instead.

```python
numbers = [4, 2, 9, 1]

print(sorted(numbers))               # [1, 2, 4, 9]
print(sorted(numbers, reverse=True))  # [9, 4, 2, 1]

names = ["Charlie", "Alice", "Bob"]
names.sort(reverse=True)
print(names)   # ['Charlie', 'Bob', 'Alice']
```

- `reverse=True` simply flips the final order — it does **not** change what
  Python considers "smaller" or "larger" during comparison.

---

## The `key=` argument with a lambda

The `key=` argument lets you control **what value is used for comparison**
during sorting, without changing what's actually stored in the list. You
pass it a function (often a `lambda`) that takes one item and returns the
value to sort by.

```python
words = ["banana", "kiwi", "fig", "apple"]

# sort by string length instead of alphabetically
by_length = sorted(words, key=lambda word: len(word))
print(by_length)   # ['fig', 'kiwi', 'apple', 'banana']
```

```python
pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]

# sort by the second element of each tuple
by_second = sorted(pairs, key=lambda pair: pair[1])
print(by_second)   # [('banana', 1), ('cherry', 2), ('apple', 3)]
```

- `key=` and `reverse=True` can be combined — Python computes the key for
  every item, then orders (and optionally reverses) based on those keys.

```python
pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]
by_second_desc = sorted(pairs, key=lambda pair: pair[1], reverse=True)
print(by_second_desc)   # [('apple', 3), ('cherry', 2), ('banana', 1)]
```

---

## Sorting a list of dicts by a key's value

A very common pattern: you have a list of dicts (e.g. records with several
fields) and want to sort them by one particular field. Use `key=lambda d:
d["field_name"]` — the lambda receives each dict and returns the value to
compare.

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

by_age = sorted(people, key=lambda person: person["age"])
for p in by_age:
    print(p["name"], p["age"])
# Bob 25
# Alice 30
# Charlie 35
```

- This works the same way with `.sort()` — just call `people.sort(key=lambda
  person: person["age"])` if you want to sort the original list in place.
- The lambda's job is only to *pick out* the value to compare — it doesn't
  do the comparing itself; Python's sort handles that automatically.

---

## Common Pitfalls

- **Assuming `.sort()` returns the sorted list.** It returns `None`.
  `my_list = my_list.sort()` is a classic bug — it silently throws away your
  list and replaces it with `None`. If you want a new variable holding the
  sorted result, use `sorted()` instead.
- **Confusing `sorted()` and `.sort()`.** `sorted()` works on any iterable
  and always returns a new list; `.sort()` only exists on lists and mutates
  in place. Reach for `sorted()` by default unless you specifically need an
  in-place mutation.
- **Trying to sort in "reverse order" by flipping the key instead of using
  `reverse=True`.** You don't need tricks like `key=lambda x: -x` for
  numbers — just pass `reverse=True`. (Negating the key can even be wrong
  for things like strings, where you can't just negate them.)
- **Passing a value instead of a function to `key=`.** `key=` must be given
  a *callable* (a function or lambda) that Python can call on each item —
  e.g. `key=lambda d: d["age"]`, not `key=d["age"]`. Writing `key=person["age"]`
  tries to evaluate that expression once up front and will not do what you
  want (and often errors).
- **Forgetting that `key=` doesn't change the items themselves.** Sorting
  `words` with `key=lambda w: len(w)` still gives you back the original
  strings, just reordered — it does not replace them with their lengths.
