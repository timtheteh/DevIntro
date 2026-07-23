# Classes Syntax — Tutoring Notes

These notes cover the **syntax** of Python classes only: how to write them correctly. We are not covering design patterns, algorithms, or bigger applied projects here — just the mechanics.

---

## The `class` keyword, `__init__`, and `self`

A class is defined with the `class` keyword followed by a name (by convention, `CapWords`) and a colon. Inside the class body, `__init__` is a special method that Python automatically calls when you create a new object (an "instance") of the class. It's used to set up the object's initial state.

`self` is the first parameter of every instance method, including `__init__`. It refers to the specific object being created or acted on. Python passes it automatically — you never supply it yourself when calling the method.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # store the argument on the instance
        self.age = age

# Creating (instantiating) an object:
d = Dog("Rex", 3)
print(d.name)  # Rex
print(d.age)   # 3
```

Note: `Dog("Rex", 3)` does NOT pass `self` explicitly — Python supplies `self` as the newly created object automatically. You only write `name` and `age` as arguments.

---

## Instance attributes vs class attributes

- **Instance attributes** belong to one specific object. They are usually set inside `__init__` using `self.attribute_name = value`. Each instance has its own copy.
- **Class attributes** belong to the class itself and are shared by all instances (unless an instance overrides them). They are defined directly inside the class body, not inside `__init__`.

```python
class Dog:
    species = "Canis familiaris"   # class attribute — shared by all Dogs

    def __init__(self, name):
        self.name = name            # instance attribute — unique per Dog

a = Dog("Rex")
b = Dog("Fido")

print(a.species, b.species)   # Canis familiaris Canis familiaris
print(a.name, b.name)         # Rex Fido

Dog.species = "Wolf-ish"       # change via the class...
print(a.species, b.species)    # Wolf-ish Wolf-ish  (both see the change)

a.name = "Rexy"                # change via one instance...
print(a.name, b.name)          # Rexy Fido  (only 'a' changes)
```

You access both kinds of attributes the same way (`instance.attribute`), but they are stored and shared differently.

---

## Dunder methods: `__str__`, `__repr__`, `__eq__`

"Dunder" = **d**ouble **under**score. These are special methods with fixed names (`__something__`) that Python calls automatically in specific situations, rather than you calling them directly.

- `__str__(self)` — called by `print(obj)` and `str(obj)`. Should return a readable, user-friendly string.
- `__repr__(self)` — called by `repr(obj)`, and used when you inspect an object in a REPL/console, or when an object appears inside a container like a list. Should return an unambiguous string, ideally one that looks like valid Python code to recreate the object.
- `__eq__(self, other)` — called when you use `==` between two objects. By default, `==` compares identity (are they the same object in memory); defining `__eq__` lets you compare by value instead.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1)          # (1, 2)          <- uses __str__
print(str(p1))      # (1, 2)          <- uses __str__
print(repr(p1))     # Point(x=1, y=2) <- uses __repr__
print([p1])         # [Point(x=1, y=2)] <- lists use __repr__ on elements

print(p1 == p2)      # True  <- uses __eq__
print(p1 is p2)       # False <- 'is' checks identity, not __eq__
```

If `__str__` is not defined, `print()` falls back to `__repr__`. If neither is defined, Python uses a default like `<__main__.Point object at 0x...>`.

---

## Inheritance syntax, `super()`

A class can inherit from another class by putting the parent class name in parentheses after the class name. The new class (subclass/child) gets all the attributes and methods of the parent class (superclass), and can add new ones or override existing ones.

`super()` gives you access to the parent class from inside the child class — most commonly used inside `__init__` to call the parent's `__init__` and avoid repeating its setup code.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):                 # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)      # calls Animal's __init__ to set self.name
        self.breed = breed          # Dog adds its own attribute

    def speak(self):                # overrides Animal's speak method
        return f"{self.name} barks."


a = Animal("Generic Animal")
d = Dog("Rex", "Labrador")

print(a.speak())   # Generic Animal makes a sound.
print(d.speak())   # Rex barks.
print(d.name, d.breed)   # Rex Labrador

print(isinstance(d, Animal))   # True — a Dog is also an Animal
```

---

## Common Pitfalls

- **Forgetting `self` as the first parameter** of instance methods. `def __init__(name, age):` (missing `self`) will raise a `TypeError` when you try to call it, because Python automatically passes the instance as the first argument.
- **Using a mutable default value as a class attribute** meant to be per-instance, e.g. `class Dog: tricks = []` — since this list is a *class* attribute, every instance shares the *same* list, so `some_dog.tricks.append(...)` affects all dogs. Mutable per-instance data should be created fresh inside `__init__` instead: `self.tricks = []`.
- **Forgetting to call `super().__init__(...)`** in a subclass that defines its own `__init__`. If you skip it, the attributes the parent class normally sets up (e.g. `self.name`) will never be created, leading to `AttributeError` later.
- **Confusing `__str__` and `__repr__`** — `__str__` is for a human-readable display (used by `print()`), while `__repr__` is for an unambiguous, developer-facing representation (used in lists, dicts, and the console). Don't assume defining one automatically gives you sensible behaviour for the other in every context — lists/containers always use `__repr__` for their elements, not `__str__`.
- **Defining `__eq__` without realizing it affects hashing** — by default, defining `__eq__` makes instances unhashable (you cannot put them in a `set` or use them as `dict` keys) unless you also define `__hash__`. This is more of an intermediate gotcha, but worth knowing it exists once you start using `__eq__`.
