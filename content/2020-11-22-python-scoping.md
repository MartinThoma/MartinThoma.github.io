---
layout: post
lang: en
title: Pythons Scoping Rules
subtitle: The extraordinary short guide to Pythons crazy scoping rules
slug: python-scoping-rules
URL: https://towardsdatascience.com/but-its-not-declared-40501fb1e943
author: Martin Thoma
date: 2020-11-23 20:00
category: Code
tags: Code, Python, Scope
featured_image: logos/python.png
---
It’s obvious that you cannot access a variable before it was declared. But if
it was declared inside a loop, can you access it outside a loop? If it was
declared in a function, can you access the variable outside of the function?

This kind of “variable lifetime” is known as scoping. After reading this
article, you will know the scoping rules of Python. Let’s start!

## The 3 Scopes of Python

Python has 3 scopes:

* **Global**: In the main part of the script. By default, this already contains
  the built-ins. You can access all global variables with `globals()`
* **Enclosed**: In the outer function, if this is a nested function
* **Local**: Within the current function. You can access all local variables
  with `locals()`. Within the main script, `locals() == globals()`

You can see all three in action here:

```python
print(min([1, 2, 3]))


def foo():
    min = lambda n: "enclosing"

    def bar():
        """Bar is enclosed by 'foo'"""
        print(min([1, 2, 3]))

    def baz():
        """Baz is also enclosed by 'foo'"""
        min = lambda n: "local"
        print(min([1, 2, 3]))

    bar()
    baz()


min = lambda n: "global"
print(min([1, 2, 3]))

foo()
```

There is a crucial point here:
> # The scope of a variable is defined at compile-time!

For this reason, the following code throws an exception:

```python
def foo():
    print(min([1, 2, 3]))
    min = lambda n: "local"


foo()
```

throws the exception:

```text
Traceback (most recent call last):
  File "example.py", line 5, in <module>
    foo()
  File "example.py", line 2, in foo
    print(min([1, 2, 3]))
UnboundLocalError: local variable 'min' referenced before assignment
```

## The “global” statement

You can assign a value to a global variable in a function with the global
statement:

```python
x = "global"


def foo():
    global x
    x = "local"


foo()
print(x)  # gives "local"
```

I need this very rarely. To make sure that I don’t confuse anything, I like to
use the globals() dictionary. In this case, I would rather use:

```python
x = "global"


def foo():
    globals()["x"] = "local"


foo()
print(x)  # gives "local"
```

## The “nonlocal” statement

You can assign a value to an enclosed variable with the nonlocal statement:

```python
x = "global"


def foo():
    x = "enclosed"

    def bar():
        nonlocal x
        x = "local"

    bar()
    print(x)  # gives "local"


foo()
print(x)  # gives "local"
```

## Confusing Examples

### Append element vs ‘+= [element]’

```python
xs = []


def foo():
    xs.append(42)  # OK


foo()
```

vs

```python
xs = []


def foo():
    xs += [42]  # UnboundLocalError: local variable 'xs'
    # referenced before assignment


foo()
```

The reason why the first works but not the second is that the first one calls a
function of `xs`. It never assigns a value to `xs`. The second one is equal to

```python
xs = []


def foo():
    xs = xs + [42]


foo()
```

When Python parses the assignment `xs = ...`, the xs is assigned the local
scope. But in the local scope, `xs` does not exist before `xs = xs + [42]` is
executed. Hence the error.

In the first example with `xs.append(42)`, the global scope of xs is used.
Hence we don’t face any issue, because it is defined in the global scope.

### Global scope DOES fall back to built-ins

```python
# prints 1
print(min([1, 2, 3]))
min = lambda n: "local"
```

but the same does not work in a local scope

```python
# UnboundLocalError: local variable 'min' referenced before assignment
def foo():
    print(min([1, 2, 3]))
    min = lambda n: "local"


foo()
```

The reason is that `locals() == globals()` within the global scope. Although built-ins are a bit special, they kind of live in the global scope.

### Assignment

This one is confusing to people with a Java, C, or C++ background. This is
valid Python code:

```python
for x in range(10):
    y = 12
print(y)  # prints 12
```

But in Java you need to declare it upfront to be able to use the variable after
the loop:

```java
public class Main
{
 public static void main(String[] args) {
     int y = 0;
     for (int i=0; i < 10; i++) {
         y = 12;
     }
  System.out.println(y);
 }
}
```

### mypy

mypy is a wide-spread [type-checker for Python](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d).

```python
if external_service():
    y = 42
else:
    y = "foo"
    # error: Incompatible types in assignment (expression has type "str", variable has type "int")
```

So mypy doesn’t like that you assign the string “foo” to y , because it first
read took the `bool(external_service()) == True` path and assumed that y would
be an integer.

Then you might want to do this:

```python
if external_service():
    y: int = 42
else:
    y: str = "foo"
    # error: Name 'y' already defined on line 2
```

You can see that mypy assumes the y should be the same type in both cases. It’s
reasonable because otherwise the following analysis might get extremely
complicated.

The next try might be:

```python
y: Union[str, int] = None
# error: Incompatible types in assignment
# (expression has type "None", variable has type "Union[str, int]")

if external_service():
    y = 42
else:
    y = "foo"
```

That should have been expected. Assigning None is not possible to a type which
does not include None — and adding None to that type might cause many more
issues down the road.

You can do this:

```python
if external_service():
    y: Union[str, int] = 42
else:
    y = "foo"
```

But I can also see when this feels strange. What might be cleaner is this:

```python
y: Union[str, int]
if external_service():
    y = 42
else:
    y = "foo"
```

## Summary

We have seen the three types of scopes in Python: Local, Enclosed, and global.
We’ve seen that you can access globals with the global keyword or over the
globals() dictionary. Locals can be accessed with the locals() dictionary and
enclosed variables with the nonlocal keyword. Keep that in mind and Python
scoping should make sense 🙂
