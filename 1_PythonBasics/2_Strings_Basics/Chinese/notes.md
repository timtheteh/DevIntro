# 字符串基础

字符串（strings）是 Python 存储文本的方式。你已经在使用 `print()` 和 `input()` 时接触过一点字符串了——现在让我们来看看它们究竟是如何工作的。

## 字符串字面量：单引号 vs 双引号

你可以使用单引号 `'...'` 或双引号 `"..."` 来创建字符串。Python 对两者的处理方式完全相同——选择哪一种主要是为了方便，尤其是当你的文本本身包含引号字符时。

```python
name = 'Alice'
greeting = "Hello there"

# 当文本中包含撇号（apostrophe）时很方便：
sentence = "It's a sunny day"

# 或者当文本中包含双引号时：
quote = 'She said "hello" to me'

print(name)
print(greeting)
print(sentence)
print(quote)
```

## 使用 `+` 拼接字符串，使用 `*` 重复字符串

你可以使用 `+` 将字符串连接（拼接）在一起，也可以使用 `*` 将一个字符串重复多次。

```python
first = "Py"
second = "thon"
combined = first + second   # "Python"
print(combined)

# 在单词之间添加一个空格
full_name = "Ada" + " " + "Lovelace"
print(full_name)

# 重复
line = "-" * 10   # "----------"
print(line)

laugh = "ha" * 3  # "hahaha"
print(laugh)
```

## 索引（正向索引和负向索引）

字符串中的每个字符都有一个位置，称为索引（index）。索引从 **0** 开始，而不是 1。你也可以使用负数索引从字符串末尾往回数，其中 `-1` 表示最后一个字符。

```python
word = "Python"

print(word[0])    # 'P'  （第一个字符）
print(word[1])    # 'y'  （第二个字符）
print(word[5])    # 'n'  （最后一个字符）

print(word[-1])   # 'n'  （最后一个字符）
print(word[-2])   # 'o'  （倒数第二个字符）
```

## 切片（Slicing）：`s[start:end]`

切片可以让你截取字符串中的一段内容。`s[start:end]` 会返回从索引 `start` 开始，一直到（但**不包括**）索引 `end` 之间的所有字符。

```python
word = "Python"

print(word[0:2])   # 'Py'   （索引 0 和 1）
print(word[2:6])   # 'thon' （索引 2、3、4、5）

# 省略 start 表示"从头开始"
print(word[:4])    # 'Pyth'

# 省略 end 表示"直到末尾"
print(word[2:])    # 'thon'
```

## 字符串的 `len()`

`len()` 会告诉你一个字符串中有多少个字符（包括空格）。

```python
message = "Hello, world"
print(len(message))   # 12

empty = ""
print(len(empty))     # 0
```

## 常用字符串方法

方法（methods）是属于某个字符串的函数，通过点号（dot notation）来调用：`my_string.method_name()`。

```python
text = "  Hello World  "

print(text.upper())     # '  HELLO WORLD  '
print(text.lower())     # '  hello world  '
print(text.strip())     # 'Hello World'  （去除首尾空白字符）

sentence = "I like cats"
print(sentence.replace("cats", "dogs"))   # 'I like dogs'

words = "I like cats".split()
print(words)             # ['I', 'like', 'cats']  （默认按空白字符分割）

csv_line = "apple,banana,cherry"
print(csv_line.split(","))   # ['apple', 'banana', 'cherry']  （按指定字符分割）

# join() 的作用与 split() 相反——它使用一个分隔符把一个字符串列表拼接起来
parts = ["apple", "banana", "cherry"]
print(",".join(parts))       # 'apple,banana,cherry'
print(" ".join(["I", "like", "cats"]))  # 'I like cats'
```

### 使用 `in` 检查子字符串

`in` 运算符用于检查一个字符串是否出现在另一个字符串中，并返回 `True` 或 `False`。

```python
sentence = "The quick brown fox"

print("quick" in sentence)   # True
print("slow" in sentence)    # False
print("Quick" in sentence)   # False （区分大小写！）
```

## 使用 `str()` 将非字符串值转换为字符串

`+` 只能用来把字符串和字符串拼接在一起。如果你想把一个数字（或其他类型）拼接到字符串上，需要先用 `str()` 把它转换成字符串。

```python
age = 12
# print("I am " + age + " years old")   # 这样写会引发 TypeError！

message = "I am " + str(age) + " years old"
print(message)   # 'I am 12 years old'

price = 4.5
print("The price is $" + str(price))
```

> 提示：稍后你会学到 f-string 和 `.format()`，它们是把变量值组合进字符串的更强大、更方便的方法。现在，先专注于熟练掌握 `+` 和 `str()`。

## 常见易错点

- **字符串是不可变的（immutable）**——你不能就地修改字符串中的某个字符（例如 `word[0] = "J"` 会引发错误）。你需要创建一个*新*的字符串，例如通过切片、拼接或 `.replace()`。
- **索引/切片中的差一错误（off-by-one errors）**——记住索引从 `0` 开始，并且 `s[start:end]` **不**包括位于 `end` 处的字符。`word[0:3]` 得到的是 3 个字符（索引 0、1、2），而不是 4 个。
- **拼接数字时忘记使用 `str()`**——`"Score: " + 10` 会引发 `TypeError`。你必须写成 `"Score: " + str(10)`。
- **在包含撇号的文本中混用引号风格**——`'It's a test'` 是语法错误，因为 Python 会认为字符串在 `It` 之后就结束了。请改用双引号（`"It's a test"`），或者对撇号进行转义。
- **方法不会改变原始字符串**——`text.upper()` 返回的是一个*新*字符串，它并不会修改 `text` 本身。如果你想保留结果，需要重新赋值：`text = text.upper()`。
