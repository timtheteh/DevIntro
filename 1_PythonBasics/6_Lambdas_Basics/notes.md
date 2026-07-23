# Lambdas Basics — Syntax Notes

These notes assume you're already comfortable with variables, data types,
strings, control flow, lists, and dicts. You have **not** yet formally learned
`def` functions — that comes in a later lesson. This lesson just introduces
the *concept* and *basic syntax* of a lambda, so you have a mental model
before we go deeper.

---

## What Is a Function, Conceptually?

A function is a reusable block of code that can take some **input**, do
something with it, and give back an **output**. You've already been *using*
functions without writing your own — `len("hello")`, `print("hi")`, and
`sorted([3, 1, 2])` are all functions: you give them input (arguments), and
they hand back a result. A lambda is just a very small, quick way to write
your *own* tiny function — without the full `def` syntax you'll learn later.

---

## Lambda Syntax

The basic shape is:

```python
lambda arguments: expression
```

- `lambda` is the keyword that starts it.
- `arguments` is a comma-separated list of inputs (can be zero, one, or more).
- After the colon comes a **single expression** — this is what gets computed
  and automatically sent back as the result.

```python
lambda x: x * x
```

This creates a small anonymous (unnamed) function that squares its input. On
its own it doesn't do anything visible — we need to either store it or call
it, which is what the next sections cover.

---

## Assigning a Lambda to a Variable vs. Using It Inline

You can store a lambda in a variable, just like any other value, and then
call it later using parentheses — exactly like calling any function.

```python
square = lambda x: x * x

print(square(4))   # 16
print(square(9))   # 81
```

Alternatively, you can define and call a lambda **immediately**, all in one
line, by wrapping it in parentheses and calling it right away. This is less
common but shows that a lambda is just a value:

```python
print((lambda x: x * x)(5))   # 25
```

Most of the time, especially while learning, you'll assign lambdas to a
variable so they're easier to read and reuse.

---

## Lambdas With Zero Arguments

If a lambda needs no input at all, just leave the space before the colon
empty.

```python
greet = lambda: "Hello there!"

print(greet())   # Hello there!
```

---

## Lambdas With One Argument

This is the most common case — a single input, transformed into an output.

```python
double = lambda x: x * 2

print(double(3))    # 6
print(double(10))   # 20
```

---

## Lambdas With Multiple Arguments

Separate multiple arguments with commas, just like a normal function call.

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

## The Key Restriction: A Single Expression Only

A lambda's body must be **one expression** — something that evaluates to a
value. It **cannot** contain statements like assignments, `if`/`else`
statements, `for`/`while` loops, or multiple lines of code. There is also no
`return` keyword — the result of the expression is returned automatically.

A conditional *expression* (the `x if condition else y` form) is allowed,
because it's still a single expression:

```python
sign = lambda n: "positive" if n >= 0 else "negative"

print(sign(5))    # positive
print(sign(-3))   # negative
```

But something like this is **not allowed** and will raise a `SyntaxError`:

```python
# Invalid — a lambda body cannot contain a statement or multiple lines:
# broken = lambda x:
#     y = x + 1
#     return y
```

---

## Common Pitfalls

- **Trying to fit statements inside a lambda.** Assignments (`y = x + 1`),
  `if` statements (as opposed to conditional *expressions*), loops, and
  multiple lines are not allowed in a lambda body — only a single expression.
- **Adding `return`.** Unlike a `def` function, a lambda never uses the word
  `return`. The value of its expression is returned automatically.
- **Forgetting to call it.** `square = lambda x: x * x` just creates the
  function and stores it — `square` alone doesn't run anything. You need
  `square(4)` (with parentheses and an argument) to actually get a result.
- **Overusing lambdas where a named function would be clearer.** A lambda
  is meant to be small and quick. If the logic is doing something
  complicated, or you find yourself wanting to give it a descriptive name
  and reuse it in many places, a proper named function (which you'll learn
  soon) is usually easier to read and maintain.
- **Forgetting commas between multiple arguments.** `lambda a b: a + b` is a
  `SyntaxError` — it must be `lambda a, b: a + b`.
