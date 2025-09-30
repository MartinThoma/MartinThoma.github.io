---
layout: post
lang: en
title: Python Generators
slug: python-generators
author: Martin Thoma
date: 2011-11-10 08:24:00.000000000 +01:00
category: Code
tags: Python
featured_image: 2011/09/Python-Logo.png
---
Python has a quite mighty tool: Generators.

Generators help you to program iterators. They look almost like normal functions, but they have yield as a special keyword. yield is used instead of return.

Imagine you wanted to display n Fibonacci numbers. This could be your normal approach:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci(n):
    """ Build and return a list of the first
        n >= 2 Fibonacci numbers """

    fibList = [1, 1]
    while len(fibList) < n:
        newFib = fibList[-1] + fibList[-2]
        fibList.append(newFib)
    return fibList


for nr, fib in enumerate(fibonacci(100)):
    print("The %i-th Fibonacci-Nr is %i" % (nr, fib))
```

The disadvantage of this approach is that you have to keep every element of the sequence in memory. Of course, you could write something like this:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    """ Calculate the n-th fibonacci number. """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for nr in range(1, 100):
    print("The %i-th Fibonacci-Nr is %i" % (nr, fib(nr)))
```

This needs much less memory, but much more time. You have to recalculate the first few fibonacci numbers every time.

A generator could look like this:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibGenerator():
    """ A python fibonacci generator """
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


myGenerator = fibGenerator()

for nr in range(1, 100):
    print("The %i-th Fibonacci-Nr is %i" % (nr, myGenerator.next()))
```

<h2>Further Reading</h2>
<ul>
  <li><a href="http://docs.python.org/tutorial/classes.html#generators">Python documentation</a></li>
  <li><a href="http://wiki.python.org/moin/Generators">Python Wiki</a></li>
</ul>
