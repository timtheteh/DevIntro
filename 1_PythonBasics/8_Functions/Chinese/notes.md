# 函数（Functions）— 语法笔记

本笔记假设你已经掌握了变量、数据类型、字符串、字典（dict）、匿名函数（lambda）和排序。
这里的重点纯粹是 Python 中的**函数语法**——如何正确地编写和调用函数，而不是函数内部应该
放什么算法。

---

## `def` 语法基础

函数使用 `def`、一个名称、一个带括号的参数列表、一个冒号，以及一个缩进的函数体来定义。
`return` 会把一个值返回给调用者（没有 `return` 语句，或者只写一个空的 `return`，都会
返回 `None`）。

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Ada")
print(result)  # Hello, Ada!
```

---

## 位置参数（Positional Arguments）

位置参数完全根据它们在调用时的顺序，与函数的参数一一对应。

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

print(describe("cow", "moo"))       # 按位置匹配
print(describe("dog", "woof"))
```

---

## 关键字参数（Keyword Arguments）

在调用函数时，你可以通过显式地写出参数名来传递参数。这样就可以不按顺序传参，
也能让函数调用更易读。

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

print(describe(sound="moo", animal="cow"))  # 这里顺序无关紧要
print(describe("cow", sound="moo"))         # 位置参数与关键字参数混用
```

规则：一旦在调用中使用了关键字参数，它之后的所有参数也都必须是关键字参数。

---

## 默认参数值（Default Argument Values）

可以在 `def` 那一行给参数设置一个默认值。如果调用者没有提供该参数，就会使用默认值。
带默认值的参数必须写在不带默认值的参数之后。

```python
def describe(animal, sound="???"):
    return f"The {animal} says {sound}"

print(describe("cat"))            # 使用默认值：The cat says ???
print(describe("cat", "meow"))    # 覆盖默认值
```

---

## `*args` —— 可变数量的位置参数

`*args` 会把任意数量的额外位置参数收集到函数内部的一个**元组（tuple）**中。名字 `args`
只是一种约定俗成的写法——真正起作用的是 `*`。

```python
def total(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(4, 5, 6, 7))    # 22
print(total())               # 0
```

---

## `**kwargs` —— 可变数量的关键字参数

`**kwargs` 会把任意数量的额外关键字参数收集到函数内部的一个**字典（dict）**中。

```python
def build_profile(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    return kwargs

profile = build_profile(name="Ada", age=30, city="London")
print(profile)  # {'name': 'Ada', 'age': 30, 'city': 'London'}
```

`*args` 和 `**kwargs` 可以与普通参数结合使用。在 `def` 中所要求的顺序是：

```python
def func(pos1, pos2, *args, kw_only=None, **kwargs):
    ...
```

也就是说：位置参数 → `*args` → 仅限关键字参数（keyword-only，可带或不带默认值）
→ `**kwargs`。

```python
def summarize(title, *items, separator=", ", **metadata):
    body = separator.join(items)
    return f"{title}: {body} | meta={metadata}"

print(summarize("Shopping", "milk", "eggs", "bread", author="Sam"))
```

---

## 调用处的解包（Unpacking at Call Sites，`*` 和 `**`）

在**调用处**，`*` 会把一个可迭代对象（iterable）解包成位置参数，而 `**` 会把一个字典
解包成关键字参数。

```python
def describe(animal, sound):
    return f"The {animal} says {sound}"

pair = ["cow", "moo"]
print(describe(*pair))          # 解包列表 -> describe("cow", "moo")

info = {"animal": "dog", "sound": "woof"}
print(describe(**info))         # 解包字典 -> describe(animal="dog", sound="woof")
```

你也可以把解包和 `*args`/`**kwargs` 的定义结合起来使用：

```python
def total(*args):
    return sum(args)

numbers = [1, 2, 3, 4]
print(total(*numbers))   # 10，等同于 total(1, 2, 3, 4)
```

解包也可以用来在*构建*集合时进行合并（这不是函数调用，但用的是同样的 `*`/`**` 语法）：

```python
a = [1, 2]
b = [3, 4]
combined = [*a, *b]          # [1, 2, 3, 4]

d1 = {"x": 1}
d2 = {"y": 2}
merged = {**d1, **d2}        # {'x': 1, 'y': 2}
```

---

## Lambda 语法 —— 进阶用法

快速复习：`lambda 参数: 表达式` 会创建一个小型匿名函数，用来求值并返回单一表达式的
结果。lambda 真正的价值在于：可以在需要一个函数的地方直接传入它，而不用写 `def`。

```python
square = lambda x: x * x
print(square(5))  # 25
```

**作为排序（sort）的 key：**

```python
people = [("Ada", 30), ("Sam", 25), ("Kai", 40)]

by_age = sorted(people, key=lambda person: person[1])
print(by_age)  # [('Sam', 25), ('Ada', 30), ('Kai', 40)]

by_name_length = sorted(people, key=lambda person: len(person[0]))
print(by_name_length)
```

**配合 `map` 使用：**

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6, 8]
```

**配合 `filter` 使用：**

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

lambda 可以像 `def` 函数一样接受多个参数、默认值，甚至 `*args`/`**kwargs`——但函数体
必须始终是单一表达式：

```python
add = lambda a, b=10: a + b
print(add(5))       # 15
print(add(5, 20))   # 25
```

---

## 类型提示（Type Hints）

类型提示用来标注一个函数期望的参数类型和返回值类型。它们在运行时**不会被强制检查**——
存在的目的是提高可读性、支持编辑器的自动补全，以及配合 `mypy` 这类静态检查工具使用。

```python
def add(a: int, b: int) -> str:
    return f"Result: {a + b}"

print(add(2, 3))  # Result: 5
```

带默认值的参数同样也可以加上类型提示：

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

对于容器类型，使用内置的泛型写法（Python 3.9 及以上版本）：

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

def lookup(data: dict[str, int]) -> int:
    return sum(data.values())
```

`Optional[X]`（来自 `typing` 模块）表示"X 或者 None"——是 `Union[X, None]` 的简写：

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Ada", 2: "Sam"}
    return users.get(user_id)  # 找不到时返回 None

print(find_user(1))  # Ada
print(find_user(99))  # None
```

其他值得了解的常见 `typing` 类型提示：

```python
from typing import Union, Callable

def parse(value: Union[int, str]) -> str:
    return str(value)

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

print(apply(lambda x: x + 1, 10))  # 11
```

类型提示同样适用于 `*args` 和 `**kwargs`：

```python
def total(*args: int) -> int:
    return sum(args)

def build_profile(**kwargs: str) -> dict[str, str]:
    return kwargs
```

---

## 常见陷阱（Common Pitfalls）

- **可变默认参数（Mutable default arguments）。** `def f(items=[]):` 这种写法只会
  在函数*定义*的那一刻创建一次这个列表，之后每次调用都会复用（并且可能被修改！）同一个
  列表对象。应该改用 `def f(items=None): items = items if items is not None else []`。
- **`def` 中的参数顺序。** 不带默认值的位置参数必须放在带默认值的参数之前，带默认值的
  参数必须放在 `*args` 之前，`*args` 必须放在仅限关键字参数之前，仅限关键字参数必须
  放在 `**kwargs` 之前。顺序写错会导致 `SyntaxError`。
- **调用中位置参数出现在关键字参数之后。** 一旦在一次调用中传了一个关键字参数，它之后
  的所有参数也都必须是关键字参数——不能再回到位置参数。`f(1, x=2, 3)` 会导致
  `SyntaxError`。
- **解包了错误的类型。** `*` 可以把任意可迭代对象解包成位置参数；而 `**` 只能把一个
  映射（mapping，即类似字典的对象）解包成关键字参数。对一个列表尝试 `f(**my_list)`
  会引发 `TypeError`。
- **lambda 函数体只能是一个表达式。** 你不能在 lambda 内部写语句（赋值语句、
  `if`/`else` 语句、循环等）——只能写单一表达式（不过像
  `lambda x: "yes" if x else "no"` 这样的条件*表达式*是可以的）。
