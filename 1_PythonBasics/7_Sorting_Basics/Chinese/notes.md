# 排序基础 — 语法笔记

这份笔记假设你已经熟悉变量 (variables)、数据类型 (data types)、
字符串 (strings)、控制流 (control flow)、列表 (lists)、字典 (dicts)
以及 lambda 的基础知识。这里的重点仅仅是 Python 内置排序工具的**语法**
—— 而不是排序算法（不涉及冒泡排序，也不需要从零开始编写自己的排序算法）。

---

## `sorted()` 与 `.sort()`

Python 提供了两种排序方式：**`sorted()` 函数**和**`.sort()` 列表方法**。
它们并不能互换使用。

- `sorted(iterable)` —— 一个内置**函数**。它适用于任何可迭代对象
  (iterable)（列表、元组、字符串等），并返回一个**全新的列表**，原始数据
  保持不变。
- `my_list.sort()` —— 一个**只存在于列表上的方法**。它会**原地**排序列表
  （修改原始列表），并返回 `None`。

```python
numbers = [4, 2, 9, 1]

# sorted() —— 返回一个新列表，原列表不受影响
new_list = sorted(numbers)
print(new_list)   # [1, 2, 4, 9]
print(numbers)     # [4, 2, 9, 1]  <- 未改变

# .sort() —— 原地排序，返回 None
result = numbers.sort()
print(numbers)     # [1, 2, 4, 9]  <- 已改变！
print(result)       # None
```

- 当你想保留原始顺序，或者要排序的对象不是列表（例如元组或字符串中的字符）
  时，使用 `sorted()`。
- 当你确实想重新排列已有的列表、并且不再需要原始顺序时，使用 `.sort()`。

---

## `reverse=True` 参数

`sorted()` 和 `.sort()` 都接受一个 `reverse` 关键字参数。默认情况下排序是
升序的（`reverse=False`）；传入 `reverse=True` 则改为降序排序。

```python
numbers = [4, 2, 9, 1]

print(sorted(numbers))               # [1, 2, 4, 9]
print(sorted(numbers, reverse=True))  # [9, 4, 2, 1]

names = ["Charlie", "Alice", "Bob"]
names.sort(reverse=True)
print(names)   # ['Charlie', 'Bob', 'Alice']
```

- `reverse=True` 只是简单地翻转最终顺序 —— 它**不会**改变 Python 在比较时
  认为什么是"更小"或"更大"。

---

## 带有 lambda 的 `key=` 参数

`key=` 参数让你可以控制排序时**用哪个值来进行比较**，而不改变列表中实际
存储的内容。你需要给它传入一个函数（通常是 `lambda`），该函数接收一个元素
并返回用于排序的值。

```python
words = ["banana", "kiwi", "fig", "apple"]

# 按字符串长度而不是按字母顺序排序
by_length = sorted(words, key=lambda word: len(word))
print(by_length)   # ['fig', 'kiwi', 'apple', 'banana']
```

```python
pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]

# 按每个元组的第二个元素排序
by_second = sorted(pairs, key=lambda pair: pair[1])
print(by_second)   # [('banana', 1), ('cherry', 2), ('apple', 3)]
```

- `key=` 和 `reverse=True` 可以组合使用 —— Python 会先为每个元素计算
  key，然后根据这些 key 排序（并可选地反转顺序）。

```python
pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]
by_second_desc = sorted(pairs, key=lambda pair: pair[1], reverse=True)
print(by_second_desc)   # [('apple', 3), ('cherry', 2), ('banana', 1)]
```

---

## 按字典的某个键的值对字典列表排序

一个非常常见的模式：你有一个字典列表（例如包含多个字段的记录），并希望按
其中某一个特定字段排序。使用 `key=lambda d: d["field_name"]` —— 这个
lambda 接收每个字典，并返回用于比较的值。

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

by_age = sorted(people, key=lambda person: person["age"])
for p in by_age:
    print(p["name"], p["age"])
# Bob 25
# Alice 30
# Charlie 35
```

- 这种方式在 `.sort()` 上同样适用 —— 如果你想原地排序原始列表，只需调用
  `people.sort(key=lambda person: person["age"])` 即可。
- lambda 的作用只是*挑选出*用于比较的值 —— 它本身并不执行比较；
  Python 的排序会自动处理比较过程。

---

## 常见陷阱

- **误以为 `.sort()` 会返回排序后的列表。** 它返回的是 `None`。
  `my_list = my_list.sort()` 是一个经典的 bug —— 它会悄悄地丢弃你的列表，
  并把它替换成 `None`。如果你想要一个保存排序结果的新变量，请改用
  `sorted()`。
- **混淆 `sorted()` 和 `.sort()`。** `sorted()` 适用于任何可迭代对象，
  并且总是返回一个新列表；`.sort()` 只存在于列表上，并且是原地修改。
  除非你确实需要原地修改，否则默认使用 `sorted()`。
- **试图通过翻转 key（而不是使用 `reverse=True`）来实现"倒序"。**
  对于数字，你不需要像 `key=lambda x: -x` 这样的技巧 —— 只需传入
  `reverse=True` 即可。（对某些类型取负甚至可能是错误的，比如字符串，
  你根本无法对它们取负。）
- **给 `key=` 传入一个值而不是一个函数。** `key=` 必须被赋予一个
  Python 可以对每个元素调用的*可调用对象*（函数或 lambda）—— 例如
  `key=lambda d: d["age"]`，而不是 `key=d["age"]`。写成
  `key=person["age"]` 会尝试提前一次性求出这个表达式的值，这并不是你想要
  的结果（而且通常会报错）。
- **忘记 `key=` 不会改变元素本身。** 用 `key=lambda w: len(w)` 对
  `words` 排序后，得到的仍然是原始字符串，只是顺序变了 —— 并不会把它们
  替换成它们的长度。
