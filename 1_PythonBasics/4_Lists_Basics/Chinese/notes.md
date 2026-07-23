# 列表基础 — 语法笔记

本笔记假定你已经熟悉变量 (variable)、数据类型 (data type)、
基础字符串 (string)，以及控制流（if/elif/else、for/while 循环、
`range()`、`break`/`continue`）。这里的重点纯粹是列表 (list) 的**语法**——
不涉及算法或应用项目，也不涉及更进阶的切片、
解包 (unpacking) 或推导式 (comprehension) 语法（那些会在之后的数据
结构课程中讲到）。

---

## 创建列表

列表使用方括号 `[]` 创建，元素之间用逗号分隔。列表可以在同一个
列表中容纳**混合类型**——数字、字符串、布尔值，甚至其他列表，
都可以放在一起。

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

empty_list = []
print(empty_list)

mixed = ["hello", 42, 3.14, True]
print(mixed)
```

- 列表是**有序的 (ordered)**——元素会保持在你放入时的位置上。
- 列表是**可变的 (mutable)**——创建之后你可以修改它们的内容
  （下面以及"常见陷阱"部分会详细介绍）。

---

## 索引（正索引与负索引）

列表中的每个元素都有一个位置，称为它的**索引 (index)**。索引从
`0` 开始，而不是 `1`。负索引从列表末尾开始计数，`-1` 表示最后
一个元素。

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # apple  （第一个元素）
print(fruits[2])    # cherry （第三个元素）
print(fruits[-1])   # date   （最后一个元素）
print(fruits[-2])   # cherry （倒数第二个元素）
```

- `fruits[0]` 是第一个元素，`fruits[1]` 是第二个，依此类推。
- `fruits[-1]` 永远是最后一个元素，无论列表有多长——当你不知道
  或不关心确切长度时非常方便。

---

## 简单切片（`a[start:end]`）

切片 (slice) 让你可以用 `a[start:end]` 取出列表的一个子片段。
`start` 是包含 (inclusive) 的，`end` 是**不包含 (exclusive)** 的
（和 `range()` 的规则一样）。

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30]        索引 1 和 2 的元素
print(numbers[:2])    # [10, 20]        start 默认为 0
print(numbers[2:])    # [30, 40, 50]    end 默认为 len(numbers)
print(numbers[:])     # [10, 20, 30, 40, 50]   整个列表的一份拷贝
```

- 省略 `start` 表示"从头开始"；省略 `end` 表示"直到末尾"。
- 切片总是返回一个**新列表 (new list)**，即使结果只有一个元素或
  为空——它不会引发 `IndexError`，即使 `end` 比列表还大。

---

## 常见列表方法：`append()`、`insert()`、`remove()`、`pop()`、`len()`、`in`

```python
fruits = ["apple", "banana"]

fruits.append("cherry")        # 添加到末尾
print(fruits)                  # ["apple", "banana", "cherry"]

fruits.insert(1, "kiwi")       # 在索引 1 处插入 "kiwi"
print(fruits)                  # ["apple", "kiwi", "banana", "cherry"]

fruits.remove("banana")        # 删除第一个匹配的“值”
print(fruits)                  # ["apple", "kiwi", "cherry"]

last_item = fruits.pop()       # 删除并返回最后一个元素
print(last_item)               # cherry
print(fruits)                  # ["apple", "kiwi"]

second_item = fruits.pop(1)    # 删除并返回“索引”1 处的元素
print(second_item)             # kiwi
print(fruits)                  # ["apple"]

print(len(fruits))             # 1

print("apple" in fruits)       # True  — 检查成员资格
print("banana" in fruits)      # False
```

- `append(x)` 在末尾添加 `x` 作为一个新元素。
- `insert(index, x)` 在指定位置添加 `x`，后面的元素依次后移。
- `remove(x)` 删除**第一个**等于 `x` 的元素（按值查找，而不是
  按位置）。
- 不带参数的 `pop()` 删除并返回**最后一个**元素；`pop(index)`
  删除并返回该**索引**处的元素。
- `len(a)` 返回列表中元素的数量。
- `x in a` 根据 `x` 是否存在返回 `True`/`False`——用法和你在
  字符串中见过的方式相同。

---

## `extend()` 与 `append()` 的区别

`append()` 总是恰好添加**一个**新元素，即使这个元素本身就是一个
列表。`extend()` 会把另一个可迭代对象 (iterable) 中的**每一个元素**
逐个添加进来。

```python
a = [1, 2, 3]
b = [1, 2, 3]

a.append([4, 5])
print(a)   # [1, 2, 3, [4, 5]]   <- 一个新元素，它是一个列表

b.extend([4, 5])
print(b)   # [1, 2, 3, 4, 5]     <- 两个新元素，被拆开加入
```

- 如果你想把两个列表合并成一个扁平的列表，应该使用
  `extend()`，而不是 `append()`。

---

## 使用 `for` 遍历列表

你已经从控制流中学过 `for item in <iterable>:` 的用法——列表
只是另一种可迭代对象，所以同样的语法可以直接使用。

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry
```

- 如果你只是想依次获取每个值，不需要索引或 `range()`——
  `for item in some_list:` 会直接给你每一个元素。

---

## 嵌套列表（简单提及）

一个列表可以把其他列表作为元素包含在内。这称为**嵌套列表
(nested list)**。你可以通过连续使用两个索引来访问内部列表中的
元素。

```python
grid = [[1, 2, 3], [4, 5, 6]]

print(grid[0])       # [1, 2, 3]   <- 第一个内部列表
print(grid[0][1])    # 2           <- 第一个内部列表的第二个元素
print(grid[1][2])    # 6           <- 第二个内部列表的第三个元素
```

- 嵌套列表其实就是元素恰好也是列表的普通列表——同样的索引
  规则依然适用，只是应用了两次。

---

## 常见陷阱

- **索引越界导致的 `IndexError`** —— 在一个 3 个元素的列表上
  执行 `fruits[5]` 会引发 `IndexError: list index out of range`。
  和切片不同，对单个元素进行索引*不会*宽容越界的索引。
- **混淆 `remove()` 和 `pop()`** —— `remove(value)` 是**按值**
  查找并删除元素；`pop(index)` 是**按位置**删除元素（并把它
  返回给你）。用列表中不存在的值调用 `remove()` 会引发
  `ValueError`；用超出范围的索引调用 `pop()` 会引发
  `IndexError`。
- **`append()` 与 `extend()` 混用出错** —— `my_list.append(other_list)`
  会把 `other_list` 作为一个单独的嵌套元素添加进去，而不是把
  它的各个元素分别加入。如果你想把两个列表逐个元素地合并
  在一起，应该使用 `extend()`。
- **忘记列表是可变的/共享引用** —— `b = a` **不会**拷贝列表；
  `a` 和 `b` 指向*同一个*列表，所以通过 `.append()`、`.pop()`
  等方法修改其中一个，另一个也会跟着改变。如果你想要一份
  独立的拷贝，请使用 `b = a[:]`（完整切片）。
- **差一错误的切片错误** —— 记住 `end` 是不包含的，就像
  `range()` 一样：`numbers[1:3]` 给你的是索引 `1` 和 `2`，
  而不是 `3`。
