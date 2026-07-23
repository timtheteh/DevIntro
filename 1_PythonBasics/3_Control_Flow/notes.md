# Control Flow — Syntax Notes

These notes assume you're already comfortable with variables, data types, strings,
dicts, lambdas, and sorting. The focus here is purely the **syntax** of Python's
control flow constructs — not algorithms or applied problem solving.

---

## `if` / `elif` / `else`

Python has no switch/case (pre-3.10) — `if` / `elif` / `else` is the standard
branching construct. Note the required colon `:` after each clause, and that
blocks are defined by indentation (no braces).

```python
temperature = 21

if temperature > 30:/Users/timothyteh/Documents/Tutoring/Coding Tuition/CodingTuition/PythonBasics
    print("hot")
elif temperature > 15:
    print("mild")
else:
    print("cold")
```

- `elif` is Python's spelling of "else if" — there is no `else if` keyword pair.
- You can chain as many `elif` blocks as you like; `else` is optional.
- Comparisons can be chained directly: `if 0 < x < 10:` is valid Python and
  means `if 0 < x and x < 10:`.

---

## Ternary expressions (`x if cond else y`)

A single-expression form of if/else, used when you want to *produce a value*
rather than execute a branch of statements. The order reads: **value_if_true,
then condition, then value_if_false**.

```python
age = 17
status = "adult" if age >= 18 else "minor"
print(status)  # minor
```

- This is an **expression**, not a statement — it can be used anywhere a value
  is expected (assignment, function argument, inside an f-string, etc.).
- There is no elif equivalent, but ternaries can be chained/nested:

```python
n = 0
sign = "positive" if n > 0 else "negative" if n < 0 else "zero"
print(sign)  # zero
```

---

## `for` loops vs `while` loops

A `for` loop iterates over an **iterable** (a sequence of items already known,
or produced lazily) — you don't manage a counter yourself. A `while` loop
repeats **as long as a condition is true** — use it when the stopping
condition, not a sequence of items, drives the loop.

```python
# for: iterating over a known collection
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# while: repeating until a condition changes
count = 3
while count > 0:
    print(count)
    count -= 1
```

- Python has no C-style `for (i = 0; i < n; i++)` loop — `range()` (below) is
  the idiomatic replacement when you need a counter.
- `while True:` combined with a `break` is a common pattern for "loop until
  some condition met inside the loop body".

---

## `range()` (including the step argument)

`range()` produces a lazy sequence of integers and is most commonly used with
`for`. It takes 1, 2, or 3 arguments:

```python
range(stop)               # 0, 1, ..., stop-1
range(start, stop)        # start, start+1, ..., stop-1
range(start, stop, step)  # start, start+step, start+2*step, ...
```

```python
for i in range(5):
    print(i)          # 0 1 2 3 4  (stop is exclusive!)

for i in range(2, 10, 2):
    print(i)           # 2 4 6 8

for i in range(10, 0, -1):
    print(i)           # counts down: 10 9 8 ... 1

for i in range(10, 0, -2):
    print(i)           # 10 8 6 4 2
```

- `stop` is always **exclusive** — `range(5)` never produces `5`.
- A negative `step` counts downward; `range()` produces nothing (an empty
  sequence, not an error) if `start`/`stop`/`step` don't produce any values
  in that direction, e.g. `range(0, 5, -1)` is empty.
- `range()` objects don't build a list in memory — wrap in `list(range(...))`
  if you want to see/materialize the values directly.

---

## `break` / `continue`

Both only make sense inside a loop body.

- `break` exits the **entire loop** immediately (no more iterations at all).
- `continue` skips the **rest of the current iteration** and moves on to the
  next one — the loop keeps running.

```python
for i in range(10):
    if i == 5:
        break        # stop the loop entirely once i is 5
    print(i)         # prints 0 1 2 3 4

for i in range(10):
    if i % 2 == 0:
        continue     # skip even numbers, keep looping
    print(i)         # prints 1 3 5 7 9
```

- In nested loops, `break`/`continue` only affect the **innermost** loop they
  are directly written in — there's no built-in "break outer loop" keyword.

---

## The lesser-known `else` clause on `for` / `while` loops

Both `for` and `while` loops can have an `else` clause. It runs **once, after
the loop finishes normally** — i.e. the loop was not stopped early via
`break`. This is Python-specific syntax with no equivalent in most other
languages.

```python
for n in range(2, 10):
    if n % 7 == 0:
        print(f"found a multiple of 7: {n}")
        break
else:
    # only runs if the loop completed WITHOUT hitting break
    print("no multiple of 7 found")
```

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    # runs because the while condition became False naturally
    print("loop finished normally")
```

- Mental model: `for/while ... else` reads as "do this loop, **else** (if we
  never broke out) do this."
- If there's no `break` anywhere in the loop body, the `else` clause will
  *always* run after the loop — that's often a sign the `else` is unnecessary
  and you can just write the code after the loop normally.
- This is commonly used for "search" patterns: loop looking for something,
  `break` when found, `else` handles the "not found" case.

---

## Common Pitfalls

- **Forgetting the colon** — every `if`, `elif`, `else`, `for`, and `while`
  header line must end in `:`. `if x > 0` (no colon) is a `SyntaxError`.
- **Mixing up ternary order** — the syntax is `value_if_true if condition
  else value_if_false`, not `condition if value_if_true else
  value_if_false`. It's easy to write it backwards when you're used to
  other languages' `cond ? a : b` order.
- **Off-by-one errors with `range()`** — remembering that `stop` is
  exclusive. `range(1, 5)` gives `1, 2, 3, 4`, *not* `1, 2, 3, 4, 5`.
- **Misreading `for...else` as "else if the loop body is empty/false"** — it
  has nothing to do with the loop having zero iterations; it means "the loop
  ran to completion without hitting a `break`." A loop over an empty
  sequence *also* triggers the `else` (since it "completes" trivially).
- **Confusing `break` and `continue`** — `break` leaves the loop entirely;
  `continue` only skips to the next iteration. Using one where you meant the
  other is a very common logic bug, not a syntax error, so Python won't warn
  you.
