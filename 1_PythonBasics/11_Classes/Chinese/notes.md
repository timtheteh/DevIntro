# 类（Classes）语法 — 辅导笔记

这份笔记只涵盖 Python 类的**语法**：也就是如何正确地写出类。我们这里不讨论设计模式、算法或更大型的实际项目，只关注其运行机制。

---

## `class` 关键字、`__init__` 与 `self`

定义一个类要使用 `class` 关键字，后面跟一个名称（按照惯例使用 `CapWords`，即每个单词首字母大写的驼峰式命名）和一个冒号。在类的主体内部，`__init__` 是一个特殊方法，当你创建该类的一个新对象（称为一个"实例"，instance）时，Python 会自动调用它。它用于设置对象的初始状态。

`self` 是每一个实例方法（包括 `__init__`）的第一个参数。它指代正在被创建或被操作的那个具体对象。Python 会自动传入它——你在调用方法时永远不需要自己提供它。

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # 将参数存储到实例上
        self.age = age

# 创建（实例化）一个对象：
d = Dog("Rex", 3)
print(d.name)  # Rex
print(d.age)   # 3
```

注意：`Dog("Rex", 3)` 并没有显式传入 `self`——Python 会自动把新创建的对象作为 `self` 传入。你只需要把 `name` 和 `age` 作为参数写出来。

---

## 实例属性（instance attributes）与类属性（class attributes）

- **实例属性**属于某一个具体的对象。它们通常在 `__init__` 内部通过 `self.attribute_name = value` 的方式设置。每个实例都拥有自己独立的一份。
- **类属性**属于类本身，由所有实例共享（除非某个实例覆盖了它）。它们直接定义在类主体内部，而不是在 `__init__` 内部。

```python
class Dog:
    species = "Canis familiaris"   # 类属性 —— 所有 Dog 共享

    def __init__(self, name):
        self.name = name            # 实例属性 —— 每只 Dog 各不相同

a = Dog("Rex")
b = Dog("Fido")

print(a.species, b.species)   # Canis familiaris Canis familiaris
print(a.name, b.name)         # Rex Fido

Dog.species = "Wolf-ish"       # 通过类来修改……
print(a.species, b.species)    # Wolf-ish Wolf-ish  （两者都能看到这个变化）

a.name = "Rexy"                # 通过某一个实例来修改……
print(a.name, b.name)          # Rexy Fido  （只有 'a' 发生了变化）
```

两种属性的访问方式相同（`instance.attribute`），但它们的存储方式和共享方式不同。

---

## 双下划线方法（Dunder methods）：`__str__`、`__repr__`、`__eq__`

"Dunder" = **d**ouble **under**score（双下划线）。这些是拥有固定名称（`__something__`）的特殊方法，Python 会在特定情况下自动调用它们，而不是由你直接调用。

- `__str__(self)` —— 由 `print(obj)` 和 `str(obj)` 调用。应当返回一个易读、对用户友好的字符串。
- `__repr__(self)` —— 由 `repr(obj)` 调用，也用于在 REPL/控制台中查看对象时，或者当对象出现在像列表这样的容器内部时。应当返回一个明确无歧义的字符串，理想情况下应看起来像能够重新创建该对象的合法 Python 代码。
- `__eq__(self, other)` —— 当你在两个对象之间使用 `==` 时被调用。默认情况下，`==` 比较的是身份（identity，即它们是否是内存中的同一个对象）；定义 `__eq__` 可以让你改为按值（value）进行比较。

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

print(p1)          # (1, 2)          <- 使用 __str__
print(str(p1))      # (1, 2)          <- 使用 __str__
print(repr(p1))     # Point(x=1, y=2) <- 使用 __repr__
print([p1])         # [Point(x=1, y=2)] <- 列表对其元素使用 __repr__

print(p1 == p2)      # True  <- 使用 __eq__
print(p1 is p2)       # False <- 'is' 检查的是身份，而不是 __eq__
```

如果没有定义 `__str__`，`print()` 会回退（fall back）使用 `__repr__`。如果两者都没有定义，Python 会使用类似 `<__main__.Point object at 0x...>` 这样的默认表示。

---

## 继承（Inheritance）语法与 `super()`

一个类可以通过在类名后面的括号中写上父类的名称，来继承另一个类。新的类（子类，subclass/child）会获得父类（超类，superclass）的所有属性和方法，并且可以添加新的属性/方法，或者覆盖（override）已有的属性/方法。

`super()` 让你可以从子类内部访问父类——最常见的用法是在 `__init__` 内部调用父类的 `__init__`，以避免重复编写父类的初始化代码。

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):                 # Dog 继承自 Animal
    def __init__(self, name, breed):
        super().__init__(name)      # 调用 Animal 的 __init__ 来设置 self.name
        self.breed = breed          # Dog 添加了自己的属性

    def speak(self):                # 覆盖了 Animal 的 speak 方法
        return f"{self.name} barks."


a = Animal("Generic Animal")
d = Dog("Rex", "Labrador")

print(a.speak())   # Generic Animal makes a sound.
print(d.speak())   # Rex barks.
print(d.name, d.breed)   # Rex Labrador

print(isinstance(d, Animal))   # True —— Dog 同时也是一个 Animal
```

---

## 常见陷阱（Common Pitfalls）

- **忘记把 `self` 作为实例方法的第一个参数。** `def __init__(name, age):`（缺少 `self`）在你尝试调用它时会引发 `TypeError`，因为 Python 会自动把实例作为第一个参数传入。
- **把可变（mutable）的默认值当作类属性使用，而本意是想让它按实例区分**，例如 `class Dog: tricks = []`——由于这个列表是一个*类*属性，所有实例都共享*同一个*列表，因此 `some_dog.tricks.append(...)` 会影响到所有的 dog。按实例区分的可变数据应当在 `__init__` 内部重新创建：`self.tricks = []`。
- **在定义了自己 `__init__` 的子类中忘记调用 `super().__init__(...)`。** 如果你跳过了这一步，父类原本会设置的属性（例如 `self.name`）就永远不会被创建，之后会导致 `AttributeError`。
- **混淆 `__str__` 和 `__repr__`**——`__str__` 用于人类可读的显示（由 `print()` 使用），而 `__repr__` 用于明确无歧义、面向开发者的表示形式（用于列表、字典以及控制台中）。不要以为定义了其中一个，就能在所有场景下自动获得另一个的合理表现——列表/容器对其元素**始终**使用 `__repr__`，而不是 `__str__`。
- **定义 `__eq__` 却没有意识到它会影响哈希（hashing）**——默认情况下，定义了 `__eq__` 会使实例变为不可哈希（unhashable，即你不能把它放进 `set` 中，也不能用作 `dict` 的键），除非你同时也定义了 `__hash__`。这算是一个更偏中级的坑，但一旦你开始使用 `__eq__`，就值得了解它的存在。
