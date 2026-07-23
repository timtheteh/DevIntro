# Lambda 基础 — 语法笔记

本笔记假设你已经熟悉变量 (variable)、数据类型 (data type)、字符串 (string)、
控制流程 (control flow)、列表 (list) 和字典 (dict)。你**还没有**正式学习过
`def` 函数——这部分内容会在后面的课程中讲解。本课只是介绍 lambda 的
*概念*和*基本语法*，让你在深入学习之前先建立一个大致的理解模型。

---

## 从概念上理解：什么是函数？

函数 (function) 是一段可重复使用的代码块，它可以接收一些**输入
(input)**，对其进行处理，然后返回一个**输出 (output)**。你其实早就在
*使用*函数了，只是还没有自己写过——`len("hello")`、`print("hi")` 和
`sorted([3, 1, 2])` 都是函数：你给它们提供输入（参数），它们就会返回一个
结果。lambda 就是一种非常简洁、快速的方式，让你可以编写*自己的*小函数
——而不需要用到你以后会学到的完整 `def` 语法。

---

## Lambda 语法

基本形式如下：

```python
lambda arguments: expression
```

- `lambda` 是用来开始定义 lambda 的关键字 (keyword)。
- `arguments` 是用逗号分隔的输入参数列表（可以是零个、一个或多个）。
- 冒号后面是一个**单一表达式 (expression)**——它会被计算，并自动作为
  结果返回。

```python
lambda x: x * x
```

这段代码创建了一个小型的匿名（没有名字的）函数，用于计算输入值的平方。
单独写出来时它不会产生任何可见的效果——我们需要把它存储起来，或者直接
调用它，这正是接下来几节要讲的内容。

---

## 将 Lambda 赋值给变量 vs. 直接内联使用

你可以像存储任何其他值一样，把 lambda 存储在一个变量中，之后再用括号
调用它——就像调用普通函数一样。

```python
square = lambda x: x * x

print(square(4))   # 16
print(square(9))   # 81
```

另外，你也可以**立即**定义并调用一个 lambda，全部写在同一行——只需要
用括号把它包起来，然后立刻调用即可。这种写法不太常见，但它说明了
lambda 本质上就是一个值：

```python
print((lambda x: x * x)(5))   # 25
```

大多数情况下，尤其是在学习阶段，你会把 lambda 赋值给一个变量，这样代码
更易读、也更容易复用。

---

## 零参数的 Lambda

如果一个 lambda 完全不需要输入，只需把冒号前面的位置留空即可。

```python
greet = lambda: "Hello there!"

print(greet())   # Hello there!
```

---

## 单参数的 Lambda

这是最常见的情况——一个输入，经过处理后转换为一个输出。

```python
double = lambda x: x * 2

print(double(3))    # 6
print(double(10))   # 20
```

---

## 多参数的 Lambda

多个参数之间用逗号分隔，就像普通函数调用一样。

```python
add = lambda a, b: a + b

print(add(2, 3))    # 5
print(add(10, 7))   # 17
```

```python
describe = lambda name, age: f"{name} is {age} years old"

print(describe("Ada", 30))   # Ada is 30 years old
```

---

## 核心限制：只能是单一表达式

lambda 的函数体必须是**一个表达式 (expression)**——也就是能计算出一个
值的内容。它**不能**包含语句 (statement)，比如赋值语句、`if`/`else`
语句、`for`/`while` 循环，或者多行代码。lambda 中也没有 `return`
关键字——表达式的结果会自动作为返回值。

条件*表达式*（也就是 `x if condition else y` 的形式）是允许的，因为它
本质上仍然是一个单一表达式：

```python
sign = lambda n: "positive" if n >= 0 else "negative"

print(sign(5))    # positive
print(sign(-3))   # negative
```

但下面这种写法是**不允许**的，会引发 `SyntaxError`（语法错误）：

```python
# 无效——lambda 函数体不能包含语句或多行代码：
# broken = lambda x:
#     y = x + 1
#     return y
```

---

## 常见误区

- **试图在 lambda 中塞入语句 (statement)。** 赋值语句（如
  `y = x + 1`）、`if` 语句（区别于条件*表达式*）、循环，以及多行代码，
  都不允许出现在 lambda 函数体中——只能是单一表达式。
- **添加 `return`。** 与 `def` 函数不同，lambda 从不使用 `return`
  关键字。其表达式的值会自动作为返回值。
- **忘记调用它。** `square = lambda x: x * x` 只是创建并存储了这个
  函数——单独写 `square` 并不会运行任何东西。你需要写 `square(4)`
  （带括号和参数）才能真正得到结果。
- **在更适合使用具名函数的场合过度使用 lambda。** lambda 的定位是
  简短、快速。如果逻辑比较复杂，或者你发现自己想给它起一个描述性的
  名字、并在多处复用它，那么一个正式的具名函数（你很快就会学到）通常
  会更易读、更易维护。
- **忘记在多个参数之间加逗号。** `lambda a b: a + b` 会引发
  `SyntaxError`（语法错误）——必须写成 `lambda a, b: a + b`。
