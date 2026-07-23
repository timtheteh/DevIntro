# 控制流 — 语法笔记

本笔记假设你已经熟悉变量 (variable)、数据类型 (data type)、字符串 (string)、
字典 (dict)、匿名函数 (lambda) 以及排序 (sorting)。这里的重点纯粹是 Python
控制流结构的**语法**——而不是算法或应用问题的解决。

---

## `if` / `elif` / `else`

Python 没有 switch/case 语句（3.10 版本之前）——`if` / `elif` / `else` 是
标准的分支结构。注意每个子句后面都必须有冒号 `:`，并且代码块是通过缩进
（而不是花括号）来划定的。

```python
temperature = 21

if temperature > 30:
    print("hot")
elif temperature > 15:
    print("mild")
else:
    print("cold")
```

- `elif` 是 Python 中 "else if" 的写法——并没有 `else if` 这样的关键字组合。
- 你可以按需连接任意多个 `elif` 代码块；`else` 是可选的。
- 比较运算符可以直接连写：`if 0 < x < 10:` 是合法的 Python 代码，等价于
  `if 0 < x and x < 10:`。

---

## 三元表达式 (`x if cond else y`)

这是 if/else 的单行表达式形式，用在你想*产生一个值*而不是执行一段语句分支
的时候。阅读顺序是：**条件为真时的值，然后是条件，然后是条件为假时的值**。

```python
age = 17
status = "adult" if age >= 18 else "minor"
print(status)  # minor
```

- 这是一个**表达式**，而不是语句——它可以用在任何需要一个值的地方（赋值、
  函数参数、f-string 内部等）。
- 三元表达式没有对应的 elif 写法，但可以进行链式/嵌套：

```python
n = 0
sign = "positive" if n > 0 else "negative" if n < 0 else "zero"
print(sign)  # zero
```

---

## `for` 循环 与 `while` 循环

`for` 循环用于遍历一个**可迭代对象 (iterable)**（一个已知的项目序列，或惰性
生成的序列）——你不需要自己维护一个计数器。`while` 循环则会**只要条件为真
就持续重复**——当驱动循环的是一个终止条件，而不是一串项目时，就用它。

```python
# for: 遍历一个已知的集合
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# while: 重复执行直到条件发生变化
count = 3
while count > 0:
    print(count)
    count -= 1
```

- Python 没有 C 语言风格的 `for (i = 0; i < n; i++)` 循环——当你需要一个计数器
  时，`range()`（见下文）是符合 Python 习惯的替代方案。
- `while True:` 搭配 `break` 是一种常见模式，用于"在循环体内满足某个条件之前
  持续循环"。

---

## `range()`（包括步长 step 参数）

`range()` 会产生一个惰性的整数序列，最常与 `for` 搭配使用。它可以接受 1、2
或 3 个参数：

```python
range(stop)               # 0, 1, ..., stop-1
range(start, stop)        # start, start+1, ..., stop-1
range(start, stop, step)  # start, start+step, start+2*step, ...
```

```python
for i in range(5):
    print(i)          # 0 1 2 3 4（stop 是不包含在内的！）

for i in range(2, 10, 2):
    print(i)           # 2 4 6 8

for i in range(10, 0, -1):
    print(i)           # 倒数：10 9 8 ... 1

for i in range(10, 0, -2):
    print(i)           # 10 8 6 4 2
```

- `stop` 参数总是**不包含在内的**——`range(5)` 永远不会产生 `5`。
- 负数的 `step` 会向下计数；如果 `start`/`stop`/`step` 在该方向上不会产生任何
  值，`range()` 会产生一个空序列（而不是报错），例如 `range(0, 5, -1)` 就是空的。
- `range()` 对象不会在内存中构建一个列表——如果你想直接查看/具体化这些值，
  可以用 `list(range(...))` 包裹它。

---

## `break` / `continue`

这两者只有在循环体内使用才有意义。

- `break` 会立即退出**整个循环**（不再执行任何后续迭代）。
- `continue` 会跳过**当前这次迭代剩余的部分**，直接进入下一次迭代——循环
  本身会继续运行。

```python
for i in range(10):
    if i == 5:
        break        # 一旦 i 等于 5，就彻底停止循环
    print(i)         # 打印 0 1 2 3 4

for i in range(10):
    if i % 2 == 0:
        continue     # 跳过偶数，继续循环
    print(i)         # 打印 1 3 5 7 9
```

- 在嵌套循环中，`break`/`continue` 只会影响它们**直接所在的最内层**循环——
  Python 没有内置的"跳出外层循环"关键字。

---

## 鲜为人知的 `for` / `while` 循环的 `else` 子句

`for` 和 `while` 循环都可以带一个 `else` 子句。它会在**循环正常结束之后**运行
一次——也就是说循环没有被 `break` 提前终止。这是 Python 特有的语法，在大多
数其他语言中都没有对应的写法。

```python
for n in range(2, 10):
    if n % 7 == 0:
        print(f"found a multiple of 7: {n}")
        break
else:
    # 只有在循环没有触发 break、正常结束的情况下才会运行
    print("no multiple of 7 found")
```

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    # 因为 while 条件自然变为 False 而运行
    print("loop finished normally")
```

- 记忆方式：`for/while ... else` 可以理解为"执行这个循环，**否则**（如果我们
  从未 break 出去）就执行这个。"
- 如果循环体内完全没有 `break`，那么 `else` 子句会*总是*在循环结束后运行——
  这通常说明这个 `else` 其实没有必要，你可以直接把代码写在循环之后。
- 这种写法常用于"查找"模式：循环查找某个目标，找到时 `break`，`else` 则
  处理"未找到"的情况。

---

## 常见错误

- **忘记写冒号** —— 每一个 `if`、`elif`、`else`、`for`、`while` 的开头行都必须以
  `:` 结尾。`if x > 0`（没有冒号）会导致 `SyntaxError`。
- **弄反三元表达式的顺序** —— 正确语法是 `value_if_true if condition
  else value_if_false`，而不是 `condition if value_if_true else
  value_if_false`。如果你习惯了其他语言的 `cond ? a : b` 写法，很容易把顺序
  写反。
- **`range()` 的差一错误 (off-by-one)** —— 要记住 `stop` 是不包含在内的。
  `range(1, 5)` 得到的是 `1, 2, 3, 4`，*而不是* `1, 2, 3, 4, 5`。
- **误解 `for...else`，以为是"循环体为空/为假时执行 else"** —— 这其实和循环
  是否有零次迭代毫无关系；它的意思是"循环运行到结束都没有触发 `break`"。
  遍历一个空序列的循环*同样也会*触发 `else`（因为它也"完成"了，只是是
  平凡地完成的）。
- **混淆 `break` 和 `continue`** —— `break` 会彻底离开循环；`continue` 只会跳到
  下一次迭代。把两者用混是非常常见的逻辑错误，而不是语法错误，所以 Python
  不会对此发出警告。
