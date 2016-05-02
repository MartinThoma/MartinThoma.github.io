---
layout: post
title: ! 'Python Puzzle #3: Associativity'
author: Martin Thoma
date: 2012-10-02 21:31:50.000000000 +02:00
category: Code
tags: Programming, Python, puzzle
featured_image: 2011/09/Python-Logo.png
---
What is the output of

```python
1 in [] in 'a'
```

and what is the output of

```python
(1 in []) in 'a'
```

or

```python
1 in ([] in 'a')
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

<h2>Answer</h2>
The first expression evaluates to <code>False</code>, because it gets evaluated as <code>(1 in []) and ([] in 'a')</code> (<a href="http://docs.python.org/reference/expressions.html#not-in">Manual</a>, <a href="http://stackoverflow.com/a/12660938/562769">Source</a>).

The second two expressions are invalid; they throw an error.
