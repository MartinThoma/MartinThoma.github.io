---
layout: post
title: Understanding Python Lists
slug: understanding-python-lists
lang: en
author: Martin Thoma
date: 2011-10-22 23:01:55.000000000 +02:00
category: Code
tags: Python
featured_image: 2011/09/Python-Logo.png
---
This article is about Python lists. I want to show you some examples of
unexpected behavior (for non-Python programmers) of lists in Python.

Imagine you have the following Python source code:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

example1 = [[1, 5, 7], [3, 6], [], [8, 1, 6]]
example2 = example1[:]
example3 = list(example1)
example4 = copy.deepcopy(example1)

example1[1][0] = 0
example1.append(1)

print(example1)
print(example2)
print(example3)
print(example4)
```

How should the output look like? Think about it for a moment, then scroll down.

<details>
<summary>Click to see the output</summary>

```bash
[[1,5,7],[0,6],[],[8,1,6],1]
[[1,5,7],[0,6],[],[8,1,6]]
[[1,5,7],[0,6],[],[8,1,6]]
[[1,5,7],[3,6],[],[8,1,6]]
```

</details>

## Explanation

The reason for this behavior is how lists are handled in Python. The variable itself is basically only a pointer to the list. When you slice the list (`myList[:]`), you copy each value of the list into another list. If `myList` was a nested list, it contained pointers to the sublists. So, if you want to make a deep copy, you have to use the `copy` module.

- **example1**: Original list, modified directly
- **example2**: Shallow copy via slicing - shares references to inner lists
- **example3**: Shallow copy via `list()` constructor - same as example2
- **example4**: Deep copy - completely independent copy

## Scoping (Historical Note)

> **Important**: This behavior was changed in Python 3! In modern Python, list comprehensions have their own scope.

phimuemue added this example in my old blog:

In Python 2, there was an issue with scoping:

```python
i = 0
[i for i in [1, 2, 3]]
print(i)  # yields 3 in Python 2, but 0 in Python 3
```

In Python 2, Python didn't create a new variable for the list comprehension but used the outer `i`. This was fixed in Python 3, where list comprehensions have their own scope.

## Recursive Lists

Python allows you to create recursive data structures, which can lead to interesting output:

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)
# Output: [1, 2, 3, [4, 5, 6]]

b.append(a)
print(b)
# Output: [4, 5, 6, [1, 2, 3, [...]]]

print(a)
# Output: [1, 2, 3, [4, 5, 6, [...]]]
```

The `[...]` represents the recursive reference to avoid infinite printing.

## Modern Python Alternatives

For modern Python development, consider using:

- **List comprehensions**: More Pythonic than traditional loops
- **`copy.deepcopy()`**: For creating independent copies
- **`collections.deque`**: For frequent append/pop operations
- **Type hints**: For better code documentation
