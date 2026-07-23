# Exception Handling in Python

Exception handling lets you deal with errors that occur while your program is running, instead of letting them crash the program. This lesson focuses purely on the **syntax** of exception handling — not on strategy or design.

---

## 1. The `try` / `except` block

The most basic form: put code that *might* raise an error inside `try`, and code that handles the error inside `except`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

If no error occurs, the `except` block is simply skipped. If an error occurs that doesn't match the `except` type, it propagates up (i.e. the program still crashes).

---

## 2. Catching specific exception types

You can name the exact exception class you expect. This is best practice — it avoids accidentally hiding bugs you didn't anticipate.

```python
try:
    number = int("not a number")
except ValueError:
    print("That wasn't a valid integer.")
```

You can also capture the exception object itself using `as`, so you can inspect it (e.g. print its message):

```python
try:
    number = int("not a number")
except ValueError as e:
    print(f"Conversion failed: {e}")
```

---

## 3. Catching multiple exception types

### Multiple `except` blocks (different handling per type)

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
```

### A single `except` for multiple types (same handling)

Use a tuple of exception types when you want to treat several exceptions the same way:

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Something went wrong: {e}")
```

---

## 4. Catching the base `Exception`

`Exception` is the base class for almost all built-in exceptions (excluding things like `SystemExit` and `KeyboardInterrupt`, which come from `BaseException`). Catching it will catch almost anything.

```python
try:
    risky_operation()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

This is useful as a **last resort / catch-all**, but it should usually come *after* more specific `except` clauses, never before them (see Common Pitfalls).

---

## 5. `else` and `finally`

- `else` runs only if the `try` block completed **without** raising an exception.
- `finally` runs **no matter what** — whether an exception occurred, was handled, or wasn't handled at all.

```python
try:
    number = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion succeeded: {number}")
finally:
    print("This always runs, no matter what.")
```

Typical use for `finally`: cleanup code (closing files, releasing resources) that must run regardless of success or failure.

```python
try:
    file = open("data.txt")
    contents = file.read()
finally:
    file.close()
```

---

## 6. The full block order

The full syntax, in the only order Python allows:

```python
try:
    pass
except SomeError:
    pass
except AnotherError:
    pass
else:
    pass
finally:
    pass
```

`try` is required; everything else is optional, but if present they must appear in this order: `except` clause(s) → `else` → `finally`.

---

## 7. The `raise` statement

### Raising a built-in exception

You can trigger an exception yourself with `raise`, optionally with a message.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

set_age(-5)
```

### Re-raising the current exception

Inside an `except` block, a bare `raise` (no argument) re-raises the exception that was just caught — useful when you want to log or react to an error but still let it propagate.

```python
try:
    1 / 0
except ZeroDivisionError:
    print("Logging the error before passing it on...")
    raise
```

### Raising a new exception while preserving the original (`raise ... from ...`)

```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise RuntimeError("Calculation failed") from e
```

---

## 8. Defining and raising custom exception classes

You can define your own exception types by subclassing `Exception` (directly or indirectly). By convention, custom exception names end in `Error`.

```python
class InvalidAgeError(Exception):
    """Raised when an age value is invalid."""
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    print(f"Age set to {age}")

try:
    set_age(-1)
except InvalidAgeError as e:
    print(f"Custom error caught: {e}")
```

Custom exceptions can also store extra data by overriding `__init__`:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Cannot withdraw {amount}, only {balance} available"
        super().__init__(message)

try:
    raise InsufficientFundsError(balance=50, amount=100)
except InsufficientFundsError as e:
    print(e)
    print(e.balance, e.amount)
```

---

## Common Pitfalls

- **Using a bare `except:`** — writing `except:` with no exception type catches *everything*, including `KeyboardInterrupt` and `SystemExit`, which can make your program impossible to stop with Ctrl+C and can hide real bugs. Always name a type, at minimum `except Exception:`.
- **Ordering `except` clauses incorrectly with inheritance** — if you catch a general parent class (like `Exception`) *before* a more specific child class (like `ValueError`), the specific clause becomes unreachable ("dead code"), because the parent clause matches first. More specific exceptions must come before more general ones.
- **Confusing `else` and `finally`** — `else` only runs when the `try` succeeds (no exception), and it will **not** run if an exception is raised and caught. `finally` always runs, success or failure, even if the exception was never caught (it runs right before the exception propagates further).
- **Swallowing exceptions silently** — writing `except Exception: pass` hides errors completely, making bugs very hard to find later. At minimum, log or print something so the failure is visible.
- **Forgetting that `raise` without an argument only works inside an active `except` block** — using bare `raise` outside of exception handling (with no exception currently being handled) causes a `RuntimeError`.
