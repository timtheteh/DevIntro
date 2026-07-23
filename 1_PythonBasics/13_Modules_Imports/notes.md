# Modules & Imports — Syntax Notes

A **module** is just a Python file (or built-in component) full of code — functions, classes,
variables — that you can reuse in another file. Python ships with a large standard library of
built-in modules (`math`, `os`, `random`, `datetime`, ...), so we'll use those to demonstrate the
syntax without needing to write our own files.

---

## 1. `import module` syntax

The most basic form: `import module_name` loads the whole module and binds the **module itself**
to a name. To use anything inside it, you must prefix it with the module name and a dot:
`module_name.thing`.

```python
import math

print(math.sqrt(16))     # 4.0
print(math.pi)            # 3.141592653589793
print(math.floor(7.9))    # 7
```

Key points:
- `math` becomes a variable in your code that refers to the module object.
- You **cannot** call `sqrt(16)` directly — it must be `math.sqrt(16)`, because `sqrt` lives
  inside the `math` namespace, not your own.
- You can import several modules on one line, separated by commas, though one-per-line is more
  common and more readable:

```python
import math, random

print(math.pi)
print(random.randint(1, 6))
```

---

## 2. `from module import name` syntax

Instead of importing the whole module, you can import specific names (functions, classes,
variables) directly into your own namespace. Then you use the name **without** the module prefix.

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0  -- no "math." prefix needed
print(pi)          # 3.141592653589793
```

You can import multiple names by separating them with commas. Each imported name behaves exactly
as if you had defined it yourself in the current file — so it can also **shadow** an existing
variable or built-in with the same name, which is something to watch for.

```python
from os import getcwd

print(getcwd())   # prints the current working directory
```

---

## 3. `as` aliasing

Both import forms let you rename what you import using `as`. This is useful for shortening long
module names, avoiding name clashes, or following common community conventions (e.g. `numpy as np`
in data science code, though we don't need numpy here).

### 3a. `import module as alias`

The module is bound to the alias instead of its original name. The original name (`math`) is not
available at all after this — only the alias is.

```python
import datetime as dt

now = dt.datetime.now()
print(now.year)
```

### 3b. `from module import name as alias`

Only the imported name is renamed; the module itself is still not directly accessible.

```python
from random import choice as pick_one

fruits = ["apple", "banana", "cherry"]
print(pick_one(fruits))
```

You can even alias multiple names from the same `from ... import ...` statement:

```python
from math import sqrt as square_root, floor as round_down

print(square_root(9))   # 3.0
print(round_down(4.8))  # 4
```

---

## 4. `if __name__ == "__main__":` pattern

Every Python file has a built-in variable called `__name__`.

- If the file is run **directly** (e.g. `python myscript.py`), Python sets `__name__` to the
  string `"__main__"`.
- If the file is **imported** as a module from somewhere else (e.g. `import myscript`), Python
  sets `__name__` to the module's own name instead (e.g. `"myscript"`), not `"__main__"`.

This lets a file behave differently depending on whether it's being run as the main program or
being reused as a library of functions elsewhere. Code inside the `if __name__ == "__main__":`
block only runs when the file is executed directly — it is skipped when the file is imported.

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # this only runs when this file is executed directly,
    # NOT when some other file does "import this_file"
    print(greet("World"))
```

Why this matters: if you write a script with useful functions and someone else `import`s it to
reuse those functions, you don't want your test/demo code (like the `print(greet("World"))` above)
to automatically run just because they imported the file. The `__name__` guard prevents that.

---

## Common Pitfalls

- **`from module import *`** imports *everything* public from a module into your current
  namespace with no prefix at all. This can silently overwrite your own variables or functions
  and makes it unclear where a name came from when reading the code later. Prefer explicit
  imports (`from module import specific_name`) or `import module` instead.
- **Circular imports** — if `file_a.py` does `import file_b` and `file_b.py` does
  `import file_a`, Python can get stuck or raise an `ImportError`, because each file is trying to
  finish importing the other before it's fully loaded itself.
- **Forgetting the `__name__` guard** in a script that's meant to be reused — without it, every
  top-level statement (including test prints or function calls) runs automatically the moment the
  file is imported elsewhere, which is usually not what you want.
- **Confusing the module name with the file name** — `import my_script` looks for a file called
  `my_script.py` in a location Python can find (same folder, or somewhere on `sys.path`). You
  import the name *without* the `.py` extension, and the name must exactly match the filename
  (case-sensitive).
- **Re-using a module name as a variable name** — e.g. writing `math = 5` after
  `import math` replaces your reference to the module with the integer `5`, so `math.sqrt(...)`
  will then fail with an `AttributeError`.
