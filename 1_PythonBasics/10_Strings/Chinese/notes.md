# 字符串语法（String Syntax）— 辅导笔记

这份笔记假设你已经熟悉字符串这种数据类型，以及基本操作（索引、切片、拼接）。
这里的重点纯粹是**语法**：Python 提供的各种编写、格式化和处理字符串字面量
（string literal）的方式。

---

## 1. f-字符串（f-strings，格式化字符串字面量）

f-字符串是在字符串字面量前加上 `f`（或 `F`）前缀。`{}` 内的任何表达式都会
被求值并插入到字符串中。

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")   # Ada is 36 years old
```

### 嵌套表达式
你可以在花括号内放入任意表达式——包括函数调用、算术运算，甚至其他字符串。

```python
items = ["pen", "book", "cup"]
print(f"First item (upper): {items[0].upper()}")
print(f"Total items: {len(items) * 2}")
```

### 格式说明符（format spec）— `f"{x:.2f}"`
在 `:` 后面，你可以添加一个**格式说明符**来控制宽度、精度、对齐方式、千位
分隔符、百分比等。

```python
pi = 3.14159265
price = 1234.5

print(f"{pi:.2f}")        # 3.14   -> 保留 2 位小数
print(f"{price:,.2f}")    # 1,234.50 -> 千位分隔符 + 2 位小数
print(f"{price:>10.2f}")  # 在宽度为 10 的字段中右对齐
print(f"{0.4567:.1%}")    # 45.7%  -> 百分比，保留 1 位小数
print(f"{42:08d}")        # 00000042 -> 补零的整数，宽度为 8
print(f"{42:b}")          # 101010 -> 二进制
```

### 转换标志（conversion flags）— `f"{x!r}"`
`!r`、`!s` 和 `!a` 会在格式化*之前*对值分别调用 `repr()`、`str()` 或
`ascii()`。

```python
text = "line\n"
print(f"{text}")     # 打印时会出现真正的换行
print(f"{text!r}")   # 'line\n'  -> 显示 repr，转义符可见
```

### `=` 调试说明符 — `f"{x=}"`
Python 3.8 新增。它会同时打印表达式的文本和其值——非常适合快速调试，而
不用再写 `print("x:", x)`。

```python
width = 10
height = 4
print(f"{width=}")               # width=10
print(f"{width * height=}")      # width * height=40
print(f"{width=:.2f}")           # width=10.00  （与格式说明符结合使用）
```

---

## 2. `.format()` 方法语法

这是较早、更明确的字符串格式化方式。字符串中的占位符 `{}` 会由 `.format()`
的参数填充。

```python
# 位置参数（隐式顺序）
print("{} is {} years old".format("Ada", 36))

# 位置参数（显式索引）— 允许重复使用/重新排序
print("{0} scored {1}, {0} wins!".format("Ada", 95))

# 关键字参数
print("{name} is {age} years old".format(name="Ada", age=36))

# 格式说明符的用法与 f-字符串相同，都写在冒号之后
print("{:.2f}".format(3.14159))     # 3.14
print("{:,.2f}".format(1234.5))     # 1,234.50
print("{:>10}".format("hi"))        # 在宽度为 10 的字段中右对齐
```

---

## 3. 字符串方法（语法模式）

关于常用字符串方法的快速语法复习。这些方法都作用在字符串实例上，并且
（除了 `join`）大多数都会返回一个**新的**字符串或列表——因为字符串是不可变
（immutable）的。

```python
s = "  Hello, World, Foo  "

s.strip()            # "Hello, World, Foo"   -> 去除首尾空白字符
s.strip(" H")         # 从两端去除指定的字符
s.lstrip(); s.rstrip()  # 只去除左边 / 只去除右边

s.split(",")          # ["  Hello", " World", " Foo  "]
s.split(",", maxsplit=1)  # 限制拆分的次数

",".join(["a", "b", "c"])   # "a,b,c"  -> 注意：是在分隔符上调用该方法

s.replace("Hello", "Hi")    # 替换所有匹配项
s.replace("o", "0", 1)      # 只替换前 N 个匹配项

s.lower(); s.upper(); s.title(); s.capitalize()

s.startswith("  He")  # True
s.endswith("Foo  ")   # True

s.find("World")       # 返回索引，找不到则返回 -1
s.index("World")      # 返回索引，找不到则抛出 ValueError

s.count("o")           # 出现的次数
```

---

## 4. 多行字符串（三引号字符串）

用 `"""` 或 `'''` 括起来的字符串可以跨越多行。源代码中的换行符会被原样
保留在字符串的值里。

```python
message = """Dear Ada,

Thank you for your submission.
Regards,
The Committee"""

print(message)
```

三引号字符串也常用于文档字符串（docstring）：

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"
```

你可以将三引号语法与 `f` 或 `r` 前缀结合使用：

```python
name = "Ada"
note = f"""Hi {name},
this is line two."""
```

---

## 5. 原始字符串（Raw Strings，`r"..."`）

在字符串字面量前加上 `r`（或 `R`）前缀，可以让 Python 把反斜杠当作
**字面字符**处理，而不是转义序列的开始。字符串仍然会在遇到匹配的引号处
结束。

```python
path = r"C:\Users\Ada\Documents"
print(path)             # C:\Users\Ada\Documents  （反斜杠原样保留）

pattern = r"\d+\.\d+"   # 常用于正则表达式模式
print(pattern)          # \d+\.\d+
```

注意：原始字符串**不能以奇数个反斜杠结尾**，因为反斜杠仍然会转义引号
字符本身：

```python
# bad = r"C:\path\"   # SyntaxError（语法错误）
good = r"C:\path" + "\\"   # 如果需要末尾反斜杠，可用这种方式变通
```

---

## 6. 转义序列（Escape Sequences）

在普通（非原始）字符串内部，反斜杠会开始一个转义序列——用来表示那些难以
或无法直接输入的字符。

```python
print("Line one\nLine two")     # \n -> 换行
print("Col1\tCol2\tCol3")       # \t -> 制表符
print("She said \"hi\"")        # \" -> 字面双引号
print('It\'s fine')             # \' -> 字面单引号
print("Back\\slash")            # \\ -> 一个字面反斜杠
print("Bell sound: \a")         # \a -> ASCII 响铃符（很少使用）
print("Unicode: \u00e9")        # \uXXXX -> unicode 码点（é）
```

你也可以通过选择不同的外层引号样式，来表示另一种引号而无需使用反斜杠
转义：

```python
a = "It's fine"       # 在 "..." 内不需要转义 '
b = 'She said "hi"'   # 在 '...' 内不需要转义 "
```

---

## 常见陷阱（Common Pitfalls）

- **忘记为路径和正则表达式使用 `r"..."`。** 写成 `"C:\new\test"` 会
  悄悄破坏字符串，因为 `\n` 和 `\t` 会被解释为换行/制表符。应使用
  `r"C:\new\test"`（或改用正斜杠）代替。
- **混用 `.format()` 的位置索引** — 在同一个 `.format()` 调用中，重复
  使用 `{0}` 而没意识到后面的 `{}`（自动编号）占位符不能与显式的
  `{0}`/`{1}` 混用；Python 会抛出 `ValueError`。
- **格式不正确的 f-字符串格式说明符**，例如 `f"{x:.2}"`（只有精度而
  没有类型，会得到意料之外的通用格式）与 `f"{x:.2f}"`（定点浮点数）
  的区别——末尾的类型字符（`f`、`d`、`%`、`b` 等）很重要。
- **忘记 f-字符串是在运行时求值的**，而不像 `.format()` 那样——你不能
  像用 `.format()` 一样先构建一个 f-字符串模板，之后再用不同的变量值
  重复使用它。
- **原始字符串不能以单个反斜杠结尾**（`r"path\"` 会引发
  `SyntaxError`），因为反斜杠仍然会转义紧随其后的引号字符。
