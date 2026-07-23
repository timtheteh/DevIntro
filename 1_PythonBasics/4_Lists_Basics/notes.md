# Lists Basics — Syntax Notes

These notes assume you're already comfortable with variables, data types,
basic strings, and control flow (if/elif/else, for/while loops, `range()`,
`break`/`continue`). The focus here is purely the **syntax** of lists — not
algorithms or applied projects, and not the more advanced slicing,
unpacking, or comprehension syntax (that's covered in a later Data
Structures lesson).

---

## Creating a list

A list is created with square brackets `[]`, with items separated by
commas. Lists can hold **mixed types** in the same list — numbers,
strings, booleans, even other lists, all together.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

empty_list = []
print(empty_list)

mixed = ["hello", 42, 3.14, True]
print(mixed)
```

- Lists are **ordered** — the items stay in the position you put them in.
- Lists are **mutable** — you can change their contents after creating
  them (more on this below and in the pitfalls section).

---

## Indexing (positive and negative)

Each item in a list has a position, called its **index**. Indexes start
at `0`, not `1`. Negative indexes count from the end of the list, with
`-1` being the last item.

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # apple  (first item)
print(fruits[2])    # cherry (third item)
print(fruits[-1])   # date   (last item)
print(fruits[-2])   # cherry (second-to-last item)
```

- `fruits[0]` is the first item, `fruits[1]` is the second, and so on.
- `fruits[-1]` is always the last item, regardless of how long the list
  is — very handy when you don't know/care about the exact length.

---

## Simple slicing (`a[start:end]`)

A slice lets you grab a sub-section of a list using `a[start:end]`.
`start` is inclusive, `end` is **exclusive** (same rule as `range()`).

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30]        items at index 1 and 2
print(numbers[:2])    # [10, 20]        start defaults to 0
print(numbers[2:])    # [30, 40, 50]    end defaults to len(numbers)
print(numbers[:])     # [10, 20, 30, 40, 50]   a copy of the whole list
```

- Leaving out `start` means "from the beginning"; leaving out `end` means
  "through the end".
- A slice always returns a **new list**, even if it's just one item or
  empty — it never causes an `IndexError`, even if `end` is bigger than
  the list.

---

## Common list methods: `append()`, `insert()`, `remove()`, `pop()`, `len()`, `in`

```python
fruits = ["apple", "banana"]

fruits.append("cherry")        # adds to the end
print(fruits)                  # ["apple", "banana", "cherry"]

fruits.insert(1, "kiwi")       # inserts "kiwi" at index 1
print(fruits)                  # ["apple", "kiwi", "banana", "cherry"]

fruits.remove("banana")        # removes the first matching VALUE
print(fruits)                  # ["apple", "kiwi", "cherry"]

last_item = fruits.pop()       # removes and returns the last item
print(last_item)               # cherry
print(fruits)                  # ["apple", "kiwi"]

second_item = fruits.pop(1)    # removes and returns the item at INDEX 1
print(second_item)             # kiwi
print(fruits)                  # ["apple"]

print(len(fruits))             # 1

print("apple" in fruits)       # True  — checks membership
print("banana" in fruits)      # False
```

- `append(x)` adds `x` as one new item at the end.
- `insert(index, x)` adds `x` at a specific position, shifting later
  items along.
- `remove(x)` deletes the **first** item that equals `x` (searches by
  value, not position).
- `pop()` with no argument removes and returns the **last** item;
  `pop(index)` removes and returns the item at that **index**.
- `len(a)` returns the number of items in the list.
- `x in a` returns `True`/`False` depending on whether `x` is present —
  works the same way you've already seen with strings.

---

## `extend()` vs `append()`

`append()` always adds exactly **one** new item, even if that item is
itself a list. `extend()` adds **each item** from another iterable
individually.

```python
a = [1, 2, 3]
b = [1, 2, 3]

a.append([4, 5])
print(a)   # [1, 2, 3, [4, 5]]   <- one new item, which is a list

b.extend([4, 5])
print(b)   # [1, 2, 3, 4, 5]     <- two new items, unpacked in
```

- If you want to merge two lists together into one flat list, use
  `extend()`, not `append()`.

---

## Iterating over a list with `for`

You already know `for item in <iterable>:` from control flow — a list is
just another iterable, so the same syntax applies directly.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry
```

- No indexes or `range()` needed if you just want each value in turn —
  `for item in some_list:` gives you each item directly.

---

## Nested lists (a brief mention)

A list can contain other lists as items. This is called a **nested
list**. You access an item inside the inner list by chaining two
indexes.

```python
grid = [[1, 2, 3], [4, 5, 6]]

print(grid[0])       # [1, 2, 3]   <- the first inner list
print(grid[0][1])    # 2           <- second item of the first inner list
print(grid[1][2])    # 6           <- third item of the second inner list
```

- Nested lists are just lists whose items happen to also be lists — the
  same indexing rules apply, just applied twice.

---

## Common Pitfalls

- **`IndexError` from out-of-range indexes** — `fruits[5]` on a
  3-item list raises `IndexError: list index out of range`. Unlike
  slicing, indexing a single item does *not* forgive an out-of-bounds
  index.
- **Confusing `remove()` with `pop()`** — `remove(value)` searches for
  and deletes an item **by value**; `pop(index)` deletes an item **by
  position** (and hands it back to you). Calling `remove()` with a value
  that isn't in the list raises a `ValueError`; calling `pop()` with an
  index that's out of range raises an `IndexError`.
- **`append()` vs `extend()` mix-ups** — `my_list.append(other_list)`
  adds `other_list` as a single nested item, not its individual
  elements. If you meant to combine two lists item-by-item, you wanted
  `extend()`.
- **Forgetting lists are mutable / shared references** — assigning
  `b = a` does **not** copy the list; `a` and `b` point to the *same*
  list, so changing one through `.append()`, `.pop()`, etc. changes the
  other too. Use `b = a[:]` (a full slice) if you want an independent
  copy.
- **Off-by-one slicing mistakes** — remembering `end` is exclusive, just
  like `range()`: `numbers[1:3]` gives you index `1` and `2`, not `3`.
