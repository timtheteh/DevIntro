# Functions — Syntax Notes

These notes assume you're already comfortable with variables, data types, strings,
dicts, lambdas, and sorting. The focus here is purely on **function syntax** in
Python — how to write and call functions correctly, not what algorithms to put
inside them.

---

## `def` Syntax Basics

A function is defined with `def`, a name, a parenthesized parameter list, a colon,
and an indented body. `return` sends a value back to the caller (no `return`
statement, or a bare `return`, gives back `None`).

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Ada")
print(result)  # Hello, Ada!
```

---

## Positional Arguments

Positional arguments are matched to parameters purely by their order in the call.

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

print(describe("cow", "moo"))       # matched by position
print(describe("dog", "woof"))
```

---

## Keyword Arguments

You can pass arguments by explicitly naming the parameter at the call site. This
lets you supply them out of order, and can make calls more readable.

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

print(describe(sound="moo", animal="cow"))  # order doesn't matter here
print(describe("cow", sound="moo"))         # positional + keyword mixed
```

Rule: once you use a keyword argument in a call, every argument after it must
also be a keyword argument.

---

## Default Argument Values

A parameter can be given a default value in the `def` line. If the caller doesn't
supply that argument, the default is used. Parameters with defaults must come
after parameters without defaults.

```python
def describe(animal, sound="???"):
    return f"The {animal} says {sound}"

print(describe("cat"))            # uses default: The cat says ???
print(describe("cat", "meow"))    # overrides default
```

---

## `*args` — Variable Positional Arguments

`*args` collects any number of extra positional arguments into a **tuple** inside
the function. The name `args` is just convention — the `*` is what matters.

```python
def total(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(4, 5, 6, 7))    # 22
print(total())               # 0
```

---

## `**kwargs` — Variable Keyword Arguments

`**kwargs` collects any number of extra keyword arguments into a **dict** inside
the function.

```python
def build_profile(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    return kwargs

profile = build_profile(name="Ada", age=30, city="London")
print(profile)  # {'name': 'Ada', 'age': 30, 'city': 'London'}
```

`*args` and `**kwargs` can be combined with normal parameters. The required
ordering in a `def` is:

```python
def func(pos1, pos2, *args, kw_only=None, **kwargs):
    ...
```

i.e. positional params → `*args` → keyword-only params (with or without
defaults) → `**kwargs`.

```python
def summarize(title, *items, separator=", ", **metadata):
    body = separator.join(items)
    return f"{title}: {body} | meta={metadata}"

print(summarize("Shopping", "milk", "eggs", "bread", author="Sam"))
```

---

## Unpacking at Call Sites (`*` and `**`)

At a **call site**, `*` unpacks an iterable into positional arguments, and `**`
unpacks a dict into keyword arguments.

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

pair = ["cow", "moo"]
print(describe(*pair))          # unpacks list -> describe("cow", "moo")

info = {"animal": "dog", "sound": "woof"}
print(describe(**info))         # unpacks dict -> describe(animal="dog", sound="woof")
```

You can combine unpacking with `*args`/`**kwargs` definitions too:

```python
def total(*args):
    return sum(args)

numbers = [1, 2, 3, 4]
print(total(*numbers))   # 10, same as total(1, 2, 3, 4)
```

Unpacking also works to combine collections when *building* them (not a function
call, but the same `*`/`**` syntax):

```python
a = [1, 2]
b = [3, 4]
combined = [*a, *b]          # [1, 2, 3, 4]

d1 = {"x": 1}
d2 = {"y": 2}
merged = {**d1, **d2}        # {'x': 1, 'y': 2}
```

---

## Lambda Syntax — Advanced Usage

Quick refresher: `lambda arguments: expression` creates a small anonymous
function that evaluates and returns a single expression. The real value of
lambdas is passing them where a function is expected without a `def`.

```python
square = lambda x: x * x
print(square(5))  # 25
```

**As a sort key:**

```python
people = [("Ada", 30), ("Sam", 25), ("Kai", 40)]

by_age = sorted(people, key=lambda person: person[1])
print(by_age)  # [('Sam', 25), ('Ada', 30), ('Kai', 40)]

by_name_length = sorted(people, key=lambda person: len(person[0]))
print(by_name_length)
```

**With `map`:**

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6, 8]
```

**With `filter`:**

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

Lambdas can take multiple arguments, default values, and even `*args`/`**kwargs`,
just like a `def` function — but the body must remain a single expression:

```python
add = lambda a, b=10: a + b
print(add(5))       # 15
print(add(5, 20))   # 25
```

---

## Type Hints

Type hints annotate what types a function expects and returns. They are **not
enforced at runtime** — they exist for readability, editor autocomplete, and
static checkers like `mypy`.

```python
def add(a: int, b: int) -> str:
    return f"Result: {a + b}"

print(add(2, 3))  # Result: 5
```

Parameters can have type hints with default values too:

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

For containers, use the built-in generics (Python 3.9+):

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

def lookup(data: dict[str, int]) -> int:
    return sum(data.values())
```

`Optional[X]` (from the `typing` module) means "X or None" — shorthand for
`Union[X, None]`:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Ada", 2: "Sam"}
    return users.get(user_id)  # returns None if not found

print(find_user(1))  # Ada
print(find_user(99))  # None
```

Other common `typing` hints worth knowing:

```python
from typing import Union, Callable

def parse(value: Union[int, str]) -> str:
    return str(value)

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

print(apply(lambda x: x + 1, 10))  # 11
```

Type hints also work with `*args` and `**kwargs`:

```python
def total(*args: int) -> int:
    return sum(args)

def build_profile(**kwargs: str) -> dict[str, str]:
    return kwargs
```

---

## Common Pitfalls

- **Mutable default arguments.** `def f(items=[]):` creates the list *once*,
  when the function is defined, and it's reused (and mutated!) across calls.
  Use `def f(items=None): items = items if items is not None else []` instead.
- **Parameter ordering in `def`.** Non-default positional params must come
  before default params, which must come before `*args`, which must come
  before keyword-only params, which must come before `**kwargs`. Getting this
  order wrong is a `SyntaxError`.
- **Keyword arguments after positional in a call.** Once you pass one keyword
  argument in a call, every argument after it must also be keyword — you
  can't go back to positional. `f(1, x=2, 3)` is a `SyntaxError`.
- **Unpacking the wrong type.** `*` unpacks any iterable into positional
  arguments; `**` unpacks only a mapping (dict-like object) into keyword
  arguments. Trying `f(**my_list)` on a list raises a `TypeError`.
- **Lambda body limited to one expression.** You cannot put statements
  (assignments, `if`/`else` statements, loops) inside a lambda — only a
  single expression (though a conditional *expression* like
  `lambda x: "yes" if x else "no"` is fine).
