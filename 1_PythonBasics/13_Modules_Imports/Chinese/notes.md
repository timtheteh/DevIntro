# 模块与导入（Modules & Imports）—— 语法笔记

**模块（module）** 其实就是一个包含代码（函数、类、变量等）的 Python 文件（或内置组件），你可以在其他文件中重复使用它。Python 自带了一个庞大的标准库，其中包含许多内置模块（如 `math`、`os`、`random`、`datetime` 等），因此我们将使用这些模块来演示语法，而不需要自己编写文件。

---

## 1. `import module` 语法

最基本的写法：`import module_name` 会加载整个模块，并将 **模块本身** 绑定到一个名字上。要使用模块内部的任何内容，你都必须在前面加上模块名和一个点：
`module_name.thing`。

```python
import math

print(math.sqrt(16))     # 4.0
print(math.pi)            # 3.141592653589793
print(math.floor(7.9))    # 7
```

要点：
- `math` 会成为你代码中的一个变量，指向该模块对象。
- 你 **不能** 直接调用 `sqrt(16)` —— 必须写成 `math.sqrt(16)`，因为 `sqrt` 存在于 `math` 这个命名空间中，而不是你自己的命名空间中。
- 你可以在一行中用逗号分隔来导入多个模块，不过每行导入一个模块是更常见、也更易读的写法：

```python
import math, random

print(math.pi)
print(random.randint(1, 6))
```

---

## 2. `from module import name` 语法

你也可以不导入整个模块，而是直接把特定的名字（函数、类、变量）导入到你自己的命名空间中。这样使用这些名字时就 **不需要** 加模块前缀了。

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0  —— 不需要 "math." 前缀
print(pi)          # 3.141592653589793
```

你可以用逗号分隔来导入多个名字。每个被导入的名字的行为就如同是你在当前文件中自己定义的一样——因此它也可能 **覆盖（shadow）** 一个同名的已有变量或内置对象，这一点需要注意。

```python
from os import getcwd

print(getcwd())   # 打印当前工作目录
```

---

## 3. `as` 别名

这两种导入方式都可以使用 `as` 来给导入的内容重新命名。这在缩短过长的模块名、避免命名冲突，或者遵循社区常见约定（例如数据科学代码中的 `numpy as np`，不过我们这里不需要用到 numpy）时非常有用。

### 3a. `import module as alias`

模块会被绑定到别名上，而不是它原本的名字。此后原来的名字（`math`）将完全不可用——只有别名才可以使用。

```python
import datetime as dt

now = dt.datetime.now()
print(now.year)
```

### 3b. `from module import name as alias`

只有被导入的名字会被重命名；模块本身仍然无法直接访问。

```python
from random import choice as pick_one

fruits = ["apple", "banana", "cherry"]
print(pick_one(fruits))
```

你甚至可以在同一条 `from ... import ...` 语句中为多个名字分别设置别名：

```python
from math import sqrt as square_root, floor as round_down

print(square_root(9))   # 3.0
print(round_down(4.8))  # 4
```

---

## 4. `if __name__ == "__main__":` 模式

每个 Python 文件都有一个内置变量，叫做 `__name__`。

- 如果该文件是被 **直接运行** 的（例如执行 `python myscript.py`），Python 会把 `__name__` 设为字符串
  `"__main__"`。
- 如果该文件是从别处作为模块被 **导入** 的（例如 `import myscript`），Python 会把 `__name__` 设为该模块自己的名字（例如
  `"myscript"`），而不是 `"__main__"`。

这使得一个文件可以根据自己是作为主程序运行，还是作为函数库在别处被复用，而表现出不同的行为。写在 `if __name__ == "__main__":`
代码块内的代码只会在该文件被直接执行时运行——当该文件被导入时，这部分代码会被跳过。

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # 这段代码只有在该文件被直接执行时才会运行，
    # 当其他文件执行 "import this_file" 时不会运行
    print(greet("World"))
```

这为什么重要：如果你写了一个包含实用函数的脚本，而别人 `import` 它来复用这些函数，你肯定不希望仅仅因为别人导入了这个文件，你自己的测试/演示代码（比如上面的 `print(greet("World"))`）就自动运行起来。`__name__` 判断正是用来防止这种情况的。

---

## 常见陷阱

- **`from module import *`** 会把模块中所有公开的内容全部导入到当前命名空间，且不带任何前缀。这可能会在不知不觉中覆盖你自己的变量或函数，并且在之后阅读代码时也很难看出某个名字究竟来自哪里。应当优先使用显式导入
  （`from module import specific_name`）或 `import module`。
- **循环导入（circular imports）**—— 如果 `file_a.py` 执行了 `import file_b`，而 `file_b.py` 又执行了
  `import file_a`，Python 可能会卡住或抛出 `ImportError`，因为这两个文件都在等待对方先完成加载，而自己却还没有完全加载好。
- **忘记加上 `__name__` 判断**，用在一个打算被复用的脚本中——如果没有它，只要该文件在别处被导入，所有顶层语句（包括测试用的
  print 或函数调用）都会自动执行，而这通常不是你想要的结果。
- **把模块名和文件名弄混**—— `import my_script` 会在 Python 能找到的位置（同一文件夹，或者 `sys.path` 上的某个位置）查找一个名为
  `my_script.py` 的文件。导入时使用的名字是 *不带* `.py` 后缀的，并且必须与文件名完全一致（区分大小写）。
- **把模块名当作变量名重复使用**——例如在 `import math` 之后又写了 `math = 5`，这会用整数
  `5` 替换掉你对该模块的引用，之后 `math.sqrt(...)` 就会因为 `AttributeError` 而报错。
