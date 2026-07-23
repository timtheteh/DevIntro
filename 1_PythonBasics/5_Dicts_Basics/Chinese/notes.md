# 字典（dict）— 语法笔记

本笔记假设你已经熟悉变量、数据类型、字符串、控制流和列表。这里的重点纯粹是 Python 字典（`dict`）类型的**语法**——而不是算法或应用型问题求解。（字典推导式将在后续更进阶的数据结构课程中介绍。）

字典存储的是一组 **键: 值（key: value）** 对的集合。与列表按位置查找元素不同，字典是按键（key）来查找值的。

---

## 创建字典（`{key: value}`）

字典字面量用花括号 `{}` 编写，每个条目写成 `key: value` 的形式，用逗号分隔。

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(ages)          # {'Alice': 30, 'Bob': 25, 'Charlie': 35}
print(type(ages))    # <class 'dict'>

empty = {}            # 空字典
print(type(empty))    # <class 'dict'>
```

- 键通常是字符串或数字，但任何**不可变**（可哈希，hashable）的类型都可以作为键——参见下方的常见陷阱部分。
- 值可以是**任何东西**——数字、字符串、列表，甚至是其他字典。
- 单独的 `{}` 创建的是一个**空字典**，而不是空集合（set）。

---

## 通过键访问值（`d[key]`）与 `.get()`

使用方括号加上键（而不是索引）来获取值。

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(ages["Bob"])   # 25
```

如果键不存在，`d[key]` 会引发 `KeyError` 并使程序崩溃。`.get()` 方法是更安全的替代方案——当键不存在时，它会返回 `None`（而不是崩溃）：

```python
print(ages.get("Bob"))       # 25
print(ages.get("Diana"))     # None（不会报错！）
```

`.get()` 还可以接受第二个参数：当键不存在时，返回这个**默认值**，而不是 `None`。

```python
print(ages.get("Diana", 0))            # 0
print(ages.get("Diana", "not found"))  # not found
```

---

## 添加/更新键，删除键

要添加新键或更新已有键，只需对 `d[key]` 进行赋值——Python 会自动判断这是一个新键还是已有的键。

```python
ages = {"Alice": 30, "Bob": 25}

ages["Charlie"] = 35   # 添加一个新键
print(ages)             # {'Alice': 30, 'Bob': 25, 'Charlie': 35}

ages["Bob"] = 26        # 更新一个已有的键
print(ages)             # {'Alice': 30, 'Bob': 26, 'Charlie': 35}
```

删除键有两种常见方式：`del` 语句，以及 `.pop()` 方法（它还会*返回*被删除的值）。

```python
del ages["Charlie"]
print(ages)              # {'Alice': 30, 'Bob': 26}

removed_value = ages.pop("Bob")
print(removed_value)     # 26
print(ages)               # {'Alice': 30}
```

- `.pop()` 同样可以接受第二个参数作为默认值，这样即使键不存在也不会崩溃：`ages.pop("Zoe", None)`。

---

## 用 `in` 检查键是否存在

在尝试访问某个键**之前**，使用 `in` 运算符检查它是否存在于字典中——这样可以避免 `KeyError` 导致的崩溃。

```python
ages = {"Alice": 30, "Bob": 25}

print("Alice" in ages)   # True
print("Zoe" in ages)     # False

if "Bob" in ages:
    print(ages["Bob"])   # 25
```

- `in` 只针对**键**进行检查，而不是值。
- `not in` 的用法相同：`if "Zoe" not in ages:`。

---

## 遍历字典：键、`.values()`、`.items()`

直接用 `for` 遍历字典时，默认得到的是**键**。

```python
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}

for name in ages:            # 默认遍历的是键
    print(name)
    # Alice
    # Bob
    # Charlie
```

这与显式地遍历 `.keys()` 完全等价：

```python
for name in ages.keys():
    print(name)
```

若只想遍历**值**，可以使用 `.values()`：

```python
for age in ages.values():
    print(age)
    # 30
    # 25
    # 35
```

若想**同时**遍历键和值，可以使用 `.items()`——每次迭代都会给你一个 `(key, value)` 元组，你可以直接将它解包到两个循环变量中：

```python
for name, age in ages.items():
    print(name, "is", age, "years old")
    # Alice is 30 years old
    # Bob is 25 years old
    # Charlie is 35 years old
```

---

## 常见陷阱

- **用 `[]` 访问不存在的键导致 `KeyError`** —— 如果键不存在，`d["missing_key"]` 会使程序崩溃。当键可能不存在时，使用 `.get()`（可选择带上默认值）；只有在你确定键一定存在的情况下，才使用 `d[key]`。
- **键必须是不可变的（可哈希，hashable）** —— 字符串、数字和元组都可以作为字典的键，但**列表不可以**（`{[1, 2]: "value"}` 会引发 `TypeError`），因为列表在创建后是可以改变的。
- **需要同时用到键和值时忘记使用 `.items()`** —— 用 `for name in ages:` 循环只能得到键。如果你接着在循环内写 `ages[name]` 来同时获取值，虽然可行，但用 `for name, age in ages.items():` 一次性同时获取两者会更简单、更直接。
- **字典的键是唯一的——重复的键会被静默覆盖** —— 写 `{"a": 1, "a": 2}` 不会报错；后面的 `"a": 2` 会直接覆盖前面的，最终结果是 `{"a": 2}`。如果你用同一个键对 `d["a"] = ...` 赋值两次，也会发生同样的情况。
- **误以为 `in` 是针对值而非键进行检查** —— `"Alice" in ages` 检查的是键。如果你想检查某个*值*是否存在，需要改用 `30 in ages.values()`——直接对字典使用 `in` 永远不会去查看值。
