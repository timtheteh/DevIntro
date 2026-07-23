# Miscellaneous Advanced Syntax — Notes

These notes assume you're already comfortable with variables, data types,
strings, dicts, lambdas, and sorting. The focus here is purely on **syntax**:
decorators, context managers, and the walrus operator — how to write them
correctly, not how to design programs around them.

---

## Decorators — Defining One

A decorator is just a function that takes a function as input and returns a
(usually new) function as output. Because functions are ordinary objects in
Python, you can wrap one function inside another.

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def greet():
    return "hello"

greet = shout(greet)   # manually "decorating" greet
print(greet())         # HELLO
```

The `wrapper` function is what actually gets called later — it calls the
original `func` and can do things before and/or after that call.

---

## Decorators — Applying with `@` Syntax

`@decorator_name` placed directly above a `def` is shorthand for
`func = decorator_name(func)`. It's applied at the moment the function is
defined, not when it's called.

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())   # HELLO — same effect as greet = shout(greet)
```

If the wrapped function takes arguments, the inner `wrapper` must accept and
forward them (usually with `*args, **kwargs` so the decorator works on any
function):

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))
# Before call
# After call
# 5
```

---

## Context Managers — `with ... as ...:`

A context manager guarantees that some "setup" happens before a block of code
runs and some "teardown" happens after it finishes — even if an exception is
raised inside the block. The most common built-in example is `open()`, used
for files.

```python
with open("example.txt", "w") as f:
    f.write("Hello, file!")
# f is automatically closed here, even if an error occurred above
```

`as f` binds the value the context manager provides (here, the open file
object) to the name `f`, which is only usable inside the indented block.

You can also open multiple context managers in a single `with` statement:

```python
with open("a.txt", "w") as fa, open("b.txt", "w") as fb:
    fa.write("data for a")
    fb.write("data for b")
```

---

## Context Managers — Supporting `with` in Your Own Class

Any class can work with `with` if it defines two special methods:
`__enter__` (runs at the start of the block, and its return value is what
`as` binds to) and `__exit__` (runs at the end of the block, even on error).

```python
class Timer:
    def __enter__(self):
        print("Starting")
        return self   # this is what gets bound to `as timer`

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stopping")
        # returning False (or None) lets any exception propagate normally

with Timer() as timer:
    print("Doing work...")

# Starting
# Doing work...
# Stopping
```

---

## Walrus Operator (`:=`) — Assignment Expressions

Normal `=` is a *statement* — it can't appear inside another expression.
`:=` is an *expression* — it assigns a value to a name **and** evaluates to
that value, so it can be used inline, e.g. inside an `if` or `while`
condition.

```python
# Without walrus: compute, then check, in two steps
value = 10
if value > 5:
    print(value)

# With walrus: assign and check in one expression
if (value := 10) > 5:
    print(value)   # 10
```

---

## Walrus Operator — Where It's Legal

`:=` is commonly used inside `while` loop conditions (to assign a value and
test it in the same line) and inside comprehensions or `if` conditions to
avoid computing something twice.

```python
# while loop: read input until the user types "quit"
inputs = ["a", "b", "quit"]
i = iter(inputs)

while (word := next(i)) != "quit":
    print("Got:", word)

# list comprehension: reuse a computed value without calling the function twice
values = [1, 2, 3, 4, 5]
results = [y for x in values if (y := x * x) > 4]
print(results)   # [9, 16, 25]
```

`:=` must always be wrapped in parentheses unless the surrounding syntax
already unambiguously allows it (e.g. directly inside an `if`/`while`
condition or as a whole statement on its own). It **cannot** be used as a
plain top-level assignment in place of `=`, and it cannot be used to assign
to attributes, subscripts, or in certain other positions like default
argument values:

```python
x := 5          # SyntaxError — bare walrus statement not allowed
# obj.attr := 5   # SyntaxError — can't walrus-assign to an attribute
```

---

## Common Pitfalls

- **Forgetting a decorator must return a callable.** If your outer function
  doesn't `return wrapper` (or otherwise return a function), the decorated
  name becomes `None` and calling it raises a `TypeError`.
- **Forgetting `*args, **kwargs` in the wrapper.** If `wrapper()` takes no
  parameters but the decorated function needs arguments, calling it raises a
  `TypeError`. Use `def wrapper(*args, **kwargs):` to forward arguments generically.
- **Not using `with` and forgetting to close resources.** `f = open(...)`
  without `with` (or a manual `f.close()`) can leave files open, leak
  handles, or lose buffered writes if an exception happens before `close()`.
- **Overusing the walrus operator for "readability".** `:=` is meant to
  avoid recomputation or awkward two-step patterns in loops/comprehensions —
  cramming it into every `if` statement just to save a line often makes code
  *harder* to read, not easier.
- **Using `:=` where only `=` is syntactically allowed.** A bare
  `name := value` on its own line, or as a function's default argument
  value, is a `SyntaxError` — the walrus operator is only legal inside an
  expression context (parenthesized, or within `if`/`while`/comprehensions).
