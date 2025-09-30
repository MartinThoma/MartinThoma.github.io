---
layout: post
lang: en
title: Python Puzzle #2: None and False
slug: python-puzzle-2-none-and-false
author: Martin Thoma
date: 2012-08-01 17:00:55.000000000 +02:00
category: Code
tags: Programming, Python, puzzle, boolean expression
featured_image: 2011/09/Python-Logo.png
---
Python automatically casts to boolean if you use another type of variable for a boolean expression.

Here is an example:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

if [1]:
    print("Crazy, ")
if 1:
    print("this ")
if 2:
    print("is ")
if True:
    print("also ")
if "a string":
    print("true.")

print("")

if not None:
    print("This ")
if not False:
    print("is ")
if not 0:
    print("not ")
if not []:
    print("true.")
```

Everything gets printed.

Now the riddle. What is the output of the following script:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

if None == False:
    print("None is false.")
else:
    print("None and false are not equal.")
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

<h2>Answer</h2>
```bash
None and false are not equal.
```

<h2>Explanation</h2>
Although <code>None</code> and <code>False</code> evaluate to <code>False</code> if they are used in a boolean expression, <code>None</code> is not the same as <code>False</code>.
