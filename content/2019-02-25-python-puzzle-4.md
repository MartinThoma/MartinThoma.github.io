---
layout: post
title: Python Puzzle 4
slug: python-puzzle-4
author: Martin Thoma
date: 2019-02-25 20:00
category: Code
tags: Programming, Python, puzzle
featured_image: 2011/09/Python-Logo.png
---
What is the output of

```python
def foo(bar=None, **kwargs):
    print("\tbar={}".format(bar))
    print("\tkwargs={}".format(kwargs))


print("Test 1:")
foo(bar=12, holla=13)

print("Test 2:")
foo(holla=13, bar=12)
```

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.


Output:

```text
Test 1:
    bar=12
    kwargs={'holla': 13}
Test 2:
    bar=12
    kwargs={'holla': 13}
```
