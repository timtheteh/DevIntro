# 变量与数据类型

欢迎来到你的第一堂 Python 课程！在我们编写任何"真正的"程序之前，我们需要先学习如何存储和标记信息，以及 Python 可以处理哪些类型的信息。这就是本课的主题。

---

## 什么是变量？

**变量 (variable)** 是一个指向存储在计算机内存中的一段数据的名字。可以把它想象成一个贴了标签的盒子：你把一个值放进盒子里，然后在盒子外面写上名字，方便以后再次找到它。

在 Python 中，你可以使用 `=` 号将一个值**赋给 (assign)**一个名字，从而创建一个变量。这个过程叫做**赋值 (assignment)**，`=` 被称为**赋值运算符 (assignment operator)**。

```python
x = 5
print(x)      # 5

name = "Alice"
print(name)   # Alice
```

在这里，`x` 是一个现在指向值 `5` 的变量。`name` 是一个指向文本 `"Alice"` 的变量。

关于赋值，有几个重要的概念：

- 变量名总是写在 `=` 的**左边**，值写在**右边**。
- `x = 5` **并不**表示数学意义上的"x 等于 5"。它的意思是"取值 5，让名字 x 指向它"。
- 你可以随时通过给变量赋一个新的值，来改变它所指向的内容：

```python
x = 5
print(x)   # 5
x = 10
print(x)   # 10
```

- 你也可以把一个表达式的运算结果赋值给变量，而不仅仅是一个普通的值：

```python
x = 5
y = x + 1
print(y)   # 6
```

### 变量命名规则与惯例

Python 有严格的**规则 (rules)**（违反会导致报错）和相对宽松的**惯例 (conventions)**（优秀的 Python 程序员会遵循的编码风格习惯）。

**规则（必须遵守）：**
- 变量名只能包含字母、数字和下划线 (`_`)。
- 变量名**不能以数字开头**（例如 `2cats` 是无效的，但 `cats2` 是可以的）。
- 变量名**不能包含空格**（请使用 `_` 代替，例如 `my_variable`）。
- 变量名**不能是 Python 的关键字 (keyword)**（例如 `if`、`for`、`while`、`True`、`None` 等保留字）。
- 变量名是**区分大小写的 (case-sensitive)**：`age`、`Age` 和 `AGE` 是三个不同的变量。

**惯例（良好的编码风格）：**
- 变量名使用小写单词并以下划线分隔，例如 `first_name`、`total_score`。这种风格叫做 `snake_case`（蛇形命名法），是 Python 中的标准写法。
- 使用具有描述性的名字。`age` 比 `a` 更好；`total_price` 比 `tp` 更好。

```python
# 有效的变量名
age = 25
first_name = "Sam"
_temp = 99
score2 = 100

# 无效的变量名（会导致报错）——请勿运行这些代码！
# 2score = 100        # 不能以数字开头
# my name = "Sam"     # 不能包含空格
# class = "Python"    # 'class' 是保留关键字
```

---

## 核心数据类型

Python 中的每一个值都有一个**类型 (type)**，它告诉 Python（以及你）这是什么样的数据，以及你能对它做什么操作。Python 内置了一个叫 `type()` 的函数，可以告诉你任意值或变量的类型。

### int（整数）

`int` 是一个整数——可以是正数、负数或零——没有小数点。

```python
age = 25
temperature = -10
count = 0

print(type(age))   # <class 'int'>
```

### float（浮点数）

`float` 是带有小数点的数字。即使是 `3.0`，由于有小数点，它也是 float 而不是 int。

```python
price = 19.99
pi = 3.14159
temperature = -2.5

print(type(price))   # <class 'float'>
```

### str（字符串）

`str`（string 的缩写）表示文本。你可以用单引号 `'...'` 或双引号 `"..."` 将字符包裹起来创建字符串——两种方式效果相同，只要保持一致即可。

```python
name = "Alice"
greeting = 'Hello there'
letter = "A"

print(type(name))   # <class 'str'>
```

### bool（布尔值）

`bool` 表示两个值中的一个：`True`（真）或 `False`（假）。注意首字母要大写——这在 Python 中很重要！布尔值通常是比较运算的结果（我们会在本课稍后看到）。

```python
is_raining = True
is_sunny = False

print(type(is_raining))   # <class 'bool'>
```

### None（空值类型）

`None` 是 Python 中一个特殊且唯一的值，表示"什么都没有"或"完全没有值"。它与 `0`、`False` 或空字符串 `""` 都不相同——它表示值的缺失。它的类型叫做 `NoneType`。

```python
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>
```

你会经常看到 `None` 被用作一个还没有真正值的变量的占位符。

---

## 类型转换（Casting）

有时候你手上有一个类型的值，但需要把它转换成另一种类型。Python 允许你使用以目标类型命名的函数在类型之间进行**转换 (convert)**（也叫 "casting"）：`int()`、`float()`、`str()` 和 `bool()`。

```python
# 字符串转 int / float
x = int("5")        # 5（转换为 int）
y = float("3.14")    # 3.14（转换为 float）

# 数字转字符串
z = str(42)          # "42"（转换为 str）

# 数字转布尔值
a = bool(0)           # False  （0 被视为"假值"）
b = bool(1)           # True   （任何非零数字都被视为"真值"）
c = bool("")          # False  （空字符串被视为"假值"）
d = bool("hello")     # True   （非空字符串被视为"真值"）

print(x, type(x))
print(y, type(y))
print(z, type(z))
```

类型转换的一个常见用途是把用户输入的文本转换成数字，这样你就可以对它进行数学运算——我们很快会在 `input()` 中看到这一点。

**重要提示：** 并非所有的转换都是可行的。`int("hello")` 会导致报错，因为 `"hello"` 无法被理解为一个数字。

---

## 运算符（Operators）

**运算符 (operator)** 是对一个或多个值执行操作的符号。

### 算术运算符（Arithmetic Operators）

这些运算符对数字（`int` 或 `float`）进行数学运算。

```python
a = 7
b = 2

print(a + b)    # 9   加法
print(a - b)    # 5   减法
print(a * b)    # 14  乘法
print(a / b)    # 3.5 除法（结果总是返回 float）
print(a // b)   # 3   整除（先做除法，然后向下取整为整数）
print(a % b)    # 1   取模（除法之后剩下的余数）
print(a ** b)   # 49  指数（a 的 b 次方）
```

最容易让初学者困惑的是 `//` 和 `%`：
- `//`（整除）给出除法运算的整数部分结果，舍去小数点后的部分。
- `%`（取模）给出该除法运算剩下的*余数*。

例如，`7 // 2` 的结果是 `3`（2 可以整除 7 三次），而 `7 % 2` 的结果是 `1`（剩下 1）。

### 比较运算符（Comparison Operators）

这些运算符比较两个值，结果总是一个 `bool`（`True` 或 `False`）。

```python
a = 7
b = 2

print(a == b)   # False   等于
print(a != b)   # True    不等于
print(a > b)    # True    大于
print(a < b)    # False   小于
print(a >= b)   # True    大于或等于
print(a <= b)   # False   小于或等于
```

**注意 `=` 和 `==` 的区别：** `=` 是把一个值赋给变量，而 `==` 是检查两个值是否相等。这是最常见的初学者错误之一——请参见下方的"常见陷阱"部分。

### 逻辑运算符（Logical Operators）

这些运算符用来组合或反转 `bool` 值。

```python
is_sunny = True
is_warm = False

print(is_sunny and is_warm)   # False  （两边都必须为 True）
print(is_sunny or is_warm)    # True   （至少一边为 True 即可）
print(not is_sunny)           # False  （把 True 变成 False，或反之）
```

- `and` → 只有**两边都**为 `True` 时才为 `True`。
- `or` → 只要**至少一边**为 `True` 就为 `True`。
- `not` → 把一个 `bool` 反转为它的相反值。

### 复合赋值运算符（Augmented Assignment Operators）

这些是"根据变量当前的值来更新它"的简写方式。你可以写 `x += 1`，而不必写 `x = x + 1`。

```python
total = 10

total += 5    # 等同于：total = total + 5   -> total 现在是 15
total -= 3    # 等同于：total = total - 3   -> total 现在是 12
total *= 2    # 等同于：total = total * 2   -> total 现在是 24
total /= 4    # 等同于：total = total / 4   -> total 现在是 6.0

print(total)  # 6.0
```

在维护累计总量或计数器时，这些写法非常常见。

---

## `print()` 与 `input()`

### `print()`

`print()` 将输出显示在屏幕上。你可以直接传给它一个值、一个变量，或用逗号分隔的多个值（`print` 会用空格把它们隔开显示）。

```python
print("Hello, world!")

name = "Sam"
age = 30
print(name, "is", age, "years old")   # Sam is 30 years old
```

### `input()`

`input()` 会暂停你的程序，显示一条可选的提示信息，并等待用户输入内容后按下回车键。用户输入的内容会作为 `input()` 的返回值。

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

**关键事实：** `input()` **始终**返回一个 `str`（字符串）——即使用户输入的是数字！如果你想对用户输入的内容进行数学运算，必须先用 `int()` 或 `float()` 进行转换。

```python
age_text = input("How old are you? ")   # 例如：用户输入 25
print(type(age_text))                     # <class 'str'>  <-- 仍然是字符串！

age = int(age_text)                       # 现在它是一个 int 了
print(age + 1)                            # 26
```

---

## 常见陷阱（Common Pitfalls）

- **混淆 `=` 和 `==`。** 单个 `=` 是赋值（`x = 5`）。双等号 `==` 是比较两个值，并返回 `True`/`False`（`x == 5`）。在想要进行比较时误用 `=`，是非常常见的错误。
- **混淆 `/` 和 `//`。** `/` 总是返回 float（例如 `7 / 2` 是 `3.5`），而 `//` 返回向下取整后的整数结果（`7 // 2` 是 `3`）。只有在你确实想要舍去余数时，才使用 `//`。
- **忘记 `input()` 始终返回字符串。** 即使用户输入的是 `"25"`，`input()` 返回给你的也是文本 `"25"`，而不是数字 `25`。如果你没有先转换就尝试执行 `input("Age: ") + 1`，Python 会报错，因为字符串不能直接和整数相加。
- **违反变量命名规则。** 变量名不能以数字开头（`1st_place` 是无效的），不能包含空格，也不能是 Python 的保留关键字之一（例如 `True`、`for` 或 `if`）。
- **混淆 `True`/`False` 的大小写。** Python 的布尔值首字母要大写：`True` 和 `False`。写成小写的 `true` 或 `false` 会导致报错，因为 Python 会把它们当作未定义的变量名，而不是布尔值。
