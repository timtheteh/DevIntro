# 杂项高级语法 — 笔记

本笔记假设你已经熟悉变量、数据类型、字符串、字典、lambda 表达式和排序。这里的重点纯粹是**语法**本身：装饰器（decorator）、上下文管理器（context manager）和海象运算符（walrus operator）——重点在于如何正确书写它们，而不是如何围绕它们设计程序。

---

## 装饰器 — 定义一个装饰器

装饰器（decorator）就是一个把函数作为输入、并返回一个（通常是新的）函数作为输出的函数。因为在 Python 中函数本身就是普通的对象，所以你可以把一个函数包装在另一个函数里面。

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def greet():
    return "hello"

greet = shout(greet)   # 手动“装饰” greet
print(greet())         # HELLO
```

`wrapper` 函数才是之后真正被调用的那个——它会调用原始的 `func`，并且可以在这次调用前后做一些额外的事情。

---

## 装饰器 — 用 `@` 语法应用装饰器

把 `@decorator_name` 直接写在 `def` 上方，是 `func = decorator_name(func)` 的简写形式。它是在函数**被定义的那一刻**应用的，而不是在函数被调用的时候。

```python
def shout(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())   # HELLO — 效果与 greet = shout(greet) 相同
```

如果被包装的函数需要接收参数，内部的 `wrapper` 就必须能够接收并转发这些参数（通常使用 `*args, **kwargs`，这样装饰器才能适用于任意函数）：

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))
# Before call
# After call
# 5
```

---

## 上下文管理器 — `with ... as ...:`

上下文管理器（context manager）能保证在一段代码块运行**之前**完成某些“准备工作”，并在代码块结束**之后**完成某些“收尾工作”——即使代码块内部抛出了异常也是如此。最常见的内置例子就是用于文件操作的 `open()`。

```python
with open("example.txt", "w") as f:
    f.write("Hello, file!")
# 即使上面发生了错误，f 也会在这里被自动关闭
```

`as f` 会把上下文管理器提供的值（这里是打开的文件对象）绑定到名字 `f` 上，而这个名字只能在缩进的代码块内部使用。

你也可以在同一个 `with` 语句中同时打开多个上下文管理器：

```python
with open("a.txt", "w") as fa, open("b.txt", "w") as fb:
    fa.write("data for a")
    fb.write("data for b")
```

---

## 上下文管理器 — 让你自己的类支持 `with`

任何类只要定义了两个特殊方法，就可以配合 `with` 使用：`__enter__`（在代码块开始时运行，其返回值就是 `as` 所绑定的内容）和 `__exit__`（在代码块结束时运行，即使发生了错误也会执行）。

```python
class Timer:
    def __enter__(self):
        print("Starting")
        return self   # 这就是绑定到 `as timer` 的内容

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stopping")
        # 返回 False（或 None）会让任何异常正常向外传播

with Timer() as timer:
    print("Doing work...")

# Starting
# Doing work...
# Stopping
```

---

## 海象运算符（`:=`） — 赋值表达式

普通的 `=` 是一条*语句（statement）*——它不能出现在另一个表达式内部。`:=` 则是一个*表达式（expression）*——它在给一个名字赋值的**同时**，也会求值为这个值，因此它可以被用在行内，例如放在 `if` 或 `while` 的条件当中。

```python
# 不使用海象运算符：先计算，再判断，分两步完成
value = 10
if value > 5:
    print(value)

# 使用海象运算符：在一个表达式中完成赋值和判断
if (value := 10) > 5:
    print(value)   # 10
```

---

## 海象运算符 — 可以使用的位置

`:=` 常用于 `while` 循环的条件中（在同一行内完成赋值和判断），也常用于推导式（comprehension）或 `if` 条件中，以避免重复计算同一个值。

```python
# while 循环：不断读取输入，直到用户输入 "quit"
inputs = ["a", "b", "quit"]
i = iter(inputs)

while (word := next(i)) != "quit":
    print("Got:", word)

# 列表推导式：复用已经计算过的值，避免重复调用函数
values = [1, 2, 3, 4, 5]
results = [y for x in values if (y := x * x) > 4]
print(results)   # [9, 16, 25]
```

除非周围的语法结构本身已经明确允许（例如直接出现在 `if`/`while` 的条件中，或者作为独立的一整条语句），否则 `:=` 必须用括号括起来。它**不能**当作普通的顶层赋值语句来替代 `=`，也不能用来给属性（attribute）、下标（subscript）赋值，或者用在某些其他位置，例如默认参数值：

```python
x := 5          # SyntaxError — 不允许单独一行的裸海象语句
# obj.attr := 5   # SyntaxError — 不能用海象运算符给属性赋值
```

---

## 常见陷阱

- **忘记装饰器必须返回一个可调用对象（callable）。** 如果你的外层函数没有 `return wrapper`（或返回其他可调用对象），被装饰的名字就会变成 `None`，调用它会引发 `TypeError`。
- **在 wrapper 中忘记写 `*args, **kwargs`。** 如果 `wrapper()` 不接收任何参数，但被装饰的函数需要参数，调用时就会引发 `TypeError`。使用 `def wrapper(*args, **kwargs):` 来通用地转发参数。
- **不使用 `with`，导致忘记关闭资源。** 如果只写 `f = open(...)` 而不使用 `with`（也没有手动调用 `f.close()`），可能会导致文件一直处于打开状态、句柄泄漏，或者在 `close()` 执行之前发生异常时丢失尚未写入的缓冲数据。
- **为了“可读性”而过度使用海象运算符。** `:=` 的本意是在循环/推导式中避免重复计算或笨拙的两步写法——如果只是为了少写一行代码，就把它硬塞进每一个 `if` 语句中，往往会让代码*更难*阅读，而不是更容易。
- **在只允许使用 `=` 的语法位置使用 `:=`。** 单独一行的裸 `name := value`，或者作为函数的默认参数值，都会引发 `SyntaxError`——海象运算符只能合法地出现在表达式上下文中（带括号，或者位于 `if`/`while`/推导式内部）。
