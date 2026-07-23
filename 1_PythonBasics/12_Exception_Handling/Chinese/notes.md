# Python 异常处理 (Exception Handling)

异常处理 (exception handling) 让你能够处理程序运行时发生的错误,而不是让程序直接崩溃。本课只专注于异常处理的**语法 (syntax)**,不涉及策略或设计模式。

---

## 1. `try` / `except` 语句块

最基本的形式:把*可能*引发错误的代码放在 `try` 中,把处理错误的代码放在 `except` 中。

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

如果没有发生错误,`except` 块会被直接跳过。如果发生的错误与 `except` 指定的类型不匹配,它会继续向上传播(也就是说程序仍然会崩溃)。

---

## 2. 捕获特定的异常类型

你可以指明你预期会发生的确切异常类 (exception class)。这是最佳实践 (best practice)——它可以避免你无意中掩盖了未曾预料到的错误 (bug)。

```python
try:
    number = int("not a number")
except ValueError:
    print("That wasn't a valid integer.")
```

你也可以使用 `as` 来捕获异常对象本身,这样就可以查看它的内容(例如打印它的错误信息):

```python
try:
    number = int("not a number")
except ValueError as e:
    print(f"Conversion failed: {e}")
```

---

## 3. 捕获多种异常类型

### 使用多个 `except` 块(对不同类型分别处理)

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
```

### 用一个 `except` 处理多种类型(相同处理方式)

当你想用相同的方式处理多种异常时,可以使用一个异常类型的元组 (tuple):

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Something went wrong: {e}")
```

---

## 4. 捕获基类 `Exception`

`Exception` 是几乎所有内置异常的基类 (base class)(不包括 `SystemExit` 和 `KeyboardInterrupt` 等,它们来自 `BaseException`)。捕获 `Exception` 几乎可以捕获所有异常。

```python
try:
    risky_operation()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

这在作为**最后手段 / 兜底处理 (catch-all)**时很有用,但它通常应该放在更具体的 `except` 子句*之后*,绝不能放在它们之前(参见"常见错误"部分)。

---

## 5. `else` 与 `finally`

- `else` 只有在 `try` 块**没有**引发异常并顺利完成时才会运行。
- `finally` **无论如何**都会运行——不管是否发生异常、异常是否被处理、还是完全没有被处理。

```python
try:
    number = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion succeeded: {number}")
finally:
    print("This always runs, no matter what.")
```

`finally` 的典型用途:执行无论成功还是失败都必须运行的清理代码(如关闭文件、释放资源)。

```python
try:
    file = open("data.txt")
    contents = file.read()
finally:
    file.close()
```

---

## 6. 完整的语句块顺序

完整语法,按照 Python 唯一允许的顺序排列:

```python
try:
    pass
except SomeError:
    pass
except AnotherError:
    pass
else:
    pass
finally:
    pass
```

`try` 是必需的;其余部分都是可选的,但如果存在,它们必须按以下顺序出现:`except` 子句(可以有多个) → `else` → `finally`。

---

## 7. `raise` 语句

### 抛出内置异常

你可以使用 `raise` 主动触发一个异常,并可以选择附带一条错误信息。

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

set_age(-5)
```

### 重新抛出当前异常

在 `except` 块内,不带参数的 `raise`(裸 `raise`)会重新抛出刚刚被捕获的异常——当你想记录 (log) 或响应一个错误,但仍希望让它继续传播时,这个方法很有用。

```python
try:
    1 / 0
except ZeroDivisionError:
    print("Logging the error before passing it on...")
    raise
```

### 抛出新异常的同时保留原始异常(`raise ... from ...`)

```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise RuntimeError("Calculation failed") from e
```

---

## 8. 定义并抛出自定义异常类

你可以通过继承(直接或间接继承)`Exception` 来定义自己的异常类型。按照惯例,自定义异常的名称以 `Error` 结尾。

```python
class InvalidAgeError(Exception):
    """Raised when an age value is invalid."""
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    print(f"Age set to {age}")

try:
    set_age(-1)
except InvalidAgeError as e:
    print(f"Custom error caught: {e}")
```

自定义异常也可以通过重写 `__init__` 来存储额外的数据:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Cannot withdraw {amount}, only {balance} available"
        super().__init__(message)

try:
    raise InsufficientFundsError(balance=50, amount=100)
except InsufficientFundsError as e:
    print(e)
    print(e.balance, e.amount)
```

---

## 常见错误 (Common Pitfalls)

- **使用裸 `except:`**——不指定任何异常类型的 `except:` 会捕获*所有*异常,包括 `KeyboardInterrupt` 和 `SystemExit`,这会导致你的程序无法用 Ctrl+C 停止,还可能掩盖真正的错误 (bug)。请始终指明一个异常类型,至少使用 `except Exception:`。
- **`except` 子句的继承顺序错误**——如果你在更具体的子类(如 `ValueError`)*之前*捕获了更通用的父类(如 `Exception`),那么更具体的子句将永远无法被执行到("死代码"),因为父类子句会先匹配上。更具体的异常必须放在更通用的异常之前。
- **混淆 `else` 和 `finally`**——`else` 只有在 `try` 成功(没有异常)时才会运行,如果异常被引发并被捕获,它**不会**运行。`finally` 无论成功还是失败都会运行,即使异常从未被捕获(它会在异常继续向上传播之前运行)。
- **默默地吞掉异常**——写 `except Exception: pass` 会完全隐藏错误,导致之后很难发现问题 (bug)。至少应该记录 (log) 或打印一些信息,让失败变得可见。
- **忘记 `raise` 在没有参数时只能在活跃的 `except` 块中使用**——在没有正在处理的异常的情况下(即在异常处理之外)使用裸 `raise`,会引发一个 `RuntimeError`。
