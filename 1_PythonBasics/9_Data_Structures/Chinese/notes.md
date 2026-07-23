# 数据结构（Data Structures）—— 语法笔记

重点：Python 内置容器类型（container types）、解包（unpacking）和推导式
（comprehensions）的**语法**。这里假设你已经掌握了变量、数据类型、字符串、
字典（dict）、lambda 表达式和排序等基础知识——因此不会重新讲解这些基础内容。

---

## 列表、元组、集合、字典的字面量语法（Literal Syntax）

```python
my_list = [1, 2, 3]          # 可变（mutable），有序
my_tuple = (1, 2, 3)         # 不可变（immutable），有序
my_set = {1, 2, 3}           # 可变，无序，元素唯一
my_dict = {"a": 1, "b": 2}   # 可变，有序（按插入顺序），键值对（key-value）

# 空容器
empty_list = []
empty_tuple = ()
empty_set = set()      # 不是 {} —— 那是空字典！
empty_dict = {}

# 只有一个元素的元组需要在末尾加逗号
single_tuple = (1,)    # 一个包含 1 的元组
not_a_tuple = (1)      # 只是整数 1，括号只是用于分组

print(type(single_tuple), type(not_a_tuple))
```

---

## 索引（Indexing）

适用于列表、元组和字符串（任何有序/类似序列的类型）。
集合和字典**不能**按位置索引（字典是按键（key）索引的）。

```python
a = [10, 20, 30, 40, 50]

print(a[0])     # 10  -> 第一个元素
print(a[-1])    # 50  -> 最后一个元素
print(a[-2])    # 40  -> 倒数第二个元素

d = {"x": 1, "y": 2}
print(d["x"])   # 1   -> 按键查找，而不是按位置
```

---

## 切片（Slicing，包括扩展切片）

切片语法为 `sequence[start:stop:step]`。`start` 是包含的（inclusive），
`stop` 是不包含的（exclusive）。三个部分都可以省略。

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:3])     # [1, 2]        -> 从索引 1 到（不包括）3
print(a[:4])      # [0, 1, 2, 3]  -> start 默认为 0
print(a[6:])      # [6, 7, 8, 9]  -> stop 默认为 len(a)
print(a[:])       # 整个列表的浅拷贝（shallow copy）

print(a[::-1])    # [9, 8, ..., 0] -> step 为 -1 表示反转序列
print(a[::2])     # [0, 2, 4, 6, 8] -> 每隔一个元素取一个
print(a[1:8:2])   # [1, 3, 5, 7]    -> start、stop、step 一起使用

print(a[-3:])     # [7, 8, 9]     -> 负索引从末尾开始计数
print(a[:-3])     # [0, 1, ..., 6] -> 除了最后 3 个元素之外的全部

# 切片对元组和字符串的用法是一样的
t = (0, 1, 2, 3, 4)
print(t[1:3])     # (1, 2)
s = "hello world"
print(s[::-1])    # "dlrow olleh"
```

集合和字典不支持切片（没有固定的顺序可供按索引切片）。

---

## 解包（Unpacking）

从一个可迭代对象（iterable）中一次性给多个变量赋值。变量名的数量必须与
元素的数量一致，除非使用带星号的 `*name` 来收集剩余的元素。

```python
a, b, c = [1, 2, 3]
print(a, b, c)          # 1 2 3

# 带星号的解包 —— 把“剩下的部分”收集到一个列表中
first, *rest = [1, 2, 3, 4, 5]
print(first, rest)      # 1 [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

*rest, last = [1, 2, 3, 4, 5]
print(rest, last)       # [1, 2, 3, 4] 5

# 嵌套解包
(a, b), c = [(1, 2), 3]
print(a, b, c)          # 1 2 3

# 交换变量的值，底层用的就是元组解包
x, y = 1, 2
x, y = y, x
print(x, y)             # 2 1

# 解包适用于任何可迭代对象，包括字符串
p, q, r = "xyz"
print(p, q, r)           # x y z
```

---

## 列表推导式（List Comprehensions）

语法：`[expression for item in iterable if condition]`

```python
squares = [n ** 2 for n in range(6)]
print(squares)                       # [0, 1, 4, 9, 16, 25]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)                         # [0, 2, 4, 6, 8]

# 推导式内部可以嵌套循环，从左到右读，就像嵌套的 for 循环一样
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)                         # [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]

# 在映射的值里使用条件表达式（三元表达式，不是过滤条件）
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
print(labels)                        # ['even','odd','even','odd','even']
```

---

## 字典推导式（Dict Comprehensions）

语法：`{key_expr: value_expr for item in iterable if condition}`

```python
squares_by_n = {n: n ** 2 for n in range(5)}
print(squares_by_n)                  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 通过 zip 把两个并行的列表组合成一个字典
names = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(names, values)}
print(combined)                      # {'a':1, 'b':2, 'c':3}

# 反转字典（键与值互换）
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
print(inverted)                      # {1: 'a', 2: 'b'}
```

---

## 集合推导式（Set Comprehensions）

语法：`{expression for item in iterable if condition}` —— 注意花括号
和字典推导式相同，但是没有 `:`。

```python
unique_lengths = {len(word) for word in ["hi", "bye", "yo", "hey"]}
print(unique_lengths)                # {2, 3} -- 重复的值会自动去重

remainders = {n % 3 for n in range(10)}
print(remainders)                    # {0, 1, 2}
```

---

## 生成器表达式（Generator Expressions）

写法看起来和列表推导式很像，但是用 `(...)` 代替 `[...]`。语法/行为上
的关键区别是：生成器表达式是**惰性的（lazy）**——它按需一次生成一个值，
不会把整个集合都构建在内存中，而且**只能被迭代一次**。

```python
squares_list = [n ** 2 for n in range(5)]   # 立即构建完成，是一个列表
squares_gen = (n ** 2 for n in range(5))    # 惰性的，是一个生成器对象

print(type(squares_list))    # <class 'list'>
print(type(squares_gen))     # <class 'generator'>

print(list(squares_gen))     # [0, 1, 4, 9, 16] -- 强制求值
print(list(squares_gen))     # [] -- 已经被耗尽了，不能重复使用

# 生成器表达式可以直接作为函数的唯一参数传入，
# 不需要额外加括号
total = sum(n ** 2 for n in range(5))
print(total)                 # 30
```

---

## 常见陷阱（Common Pitfalls）

- **切片的差一错误（off-by-one）** —— 记住 `stop` 是**不包含**的。
  `a[1:3]` 得到的是索引 1 和 2，而不是 1 到 3。
- **`(1,)` 与 `(1)` 的区别** —— 末尾的逗号才是构成元组的关键；`(1)` 只
  是加了括号的整数 `1`。单独的 `()` 是空元组，但单独的 `{}` 是空**字典**，
  而不是空集合（要用 `set()`）。
- **可变性（mutability）造成的困惑** —— 列表和集合是可变的（可以用
  `.append()`、`.add()`、按元素赋值等方式原地修改）；元组是不可变的。
  这也意味着元组（而不是列表）可以用作字典的键或集合中的元素，因为这些
  地方需要可哈希（hashable）的元素。
- **推导式中变量的作用域（scoping）** —— 推导式内部的循环变量（比如
  `[n for n in range(5)]` 中的 `n`）在 Python 3 中**不会**泄漏到外层作用
  域（这一点和普通的 `for` 循环不同）。不要指望推导式运行完之后这个变量
  还存在。
- **重复使用生成器表达式** —— 生成器在完整迭代一次之后就会被耗尽。如果
  需要对同一份数据迭代两次，请改用列表/元组推导式，或者重新创建一个生成
  器。
