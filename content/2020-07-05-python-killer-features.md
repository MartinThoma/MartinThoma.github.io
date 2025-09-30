---
layout: post
lang: en
title: Killer Features by Python Version
slug: python-killer-features
URL: https://medium.com/python-in-plain-english/killer-features-by-python-version-c84ca12dba8
author: Martin Thoma
date: 2020-05-17 20:00
category: My bits and bytes
tags: Python
featured_image: logos/python.png
---
Are you wondering why you should switch from Python 3.6 to Python 3.7 or any other version combination? Or are you thinking about supporting Python 3.5 and want to know which features you have to avoid? Then this is your article.

There are, of course, way more features. But those are the ones I stumble over most of the time.

## pyenv

Before we start going into details, you must know about pyenv. It’s a super handy tool which let’s you easily switch the Python version. It downloads them automatically for you. Here is how you use it:

```bash
# See which Python versions are available:
$ pyenv install --list

# Install one
$ pyenv install 3.5.9

# Use one:
$ pyenv local 3.5.9
```

It’s pretty neat that it switches also the tools you install with it. For example, when you switch to 3.5.9, you also have pip for that version.

## Python 3.5

I really hope nobody is using Python versions below 3.3 anymore. Or, god forbid, even Python 2.7 😨.

There are so many new features and improvements in Python 3 compared to 2.7:

```python-repl
# python2 thinks this is fine, python3 throws an Exception
>>> True = False
>>> max(['foo', 2])
'foo'
>>> 'foo' > 2
True

# Advanced iterable unpacking:
a, b, *rest = range(10)
```

And there is more:

* [Better unicode handling](https://docs.python.org/3/howto/unicode.html#python-s-unicode-support) 🎉🎉🎉
* Range is the new xrange (the old range function was dropped)
* [PEP-380](https://docs.python.org/3/whatsnew/3.3.html#pep-380-syntax-for-delegating-to-a-subgenerator): yield from instead of iterating over a generator end yield -ing every value
* [enum](https://docs.python.org/3/library/enum.html) , [pathlib](https://docs.python.org/3/library/pathlib.html) and [unittest.mock](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)
* [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
* async and await ([source](https://docs.python.org/3/whatsnew/3.5.html#pep-492-coroutines-with-async-and-await-syntax))

Please also be aware that Python 2.7, Python 3.1 / 3.2 / 3.3 and 3.4 reached their end of life a while ago. And Python 3.5 will reach it in September 2020 ([source](https://devguide.python.org/#status-of-python-branches)).p

## Python 3.6

```python-repl
# Reasonable type annotation syntax
>>> from typing import List
>>> number : List[int] = [28, 4, 1990]

# f-string!
>>> bar = 3
>>> f"foo {bar}"
'foo 3'

# PEP 515: Underscores in Numeric Literals
>>> number = 1_000_000
```

The list of [new features in Python 3.6](https://docs.python.org/3/whatsnew/3.6.html) is way longer. One improvement to point out is that the internal representation of dictionaries became way more efficient, leading to a 20% size reduction in memory.

## Python 3.7

The **future annotations** are super handy when you want to properly annotate your classes.

```python
from __future__ import annotations


class Foo:
    def __init__(self, bar):
        self.bar = bar

    def foo(bar) -> Foo:
        self.bar = bar + bar
        return self
```

* Dictionaries have insertion order ([source](https://docs.python.org/3/whatsnew/3.7.html#whatsnew37-))
* async and await are reserved keywords ([source](https://docs.python.org/3/whatsnew/3.7.html))
* [PEP-557](https://www.python.org/dev/peps/pep-0557/): Dataclasses
* [PEP-589](https://www.python.org/dev/peps/pep-0589/): TypedDict 🎉

## Python 3.8

```python-repl
# f-strings for debugging
>>> bar = 3
>>> foo = "Hello World"
>>> f"{foo=}, {bar=}"
"foo='Hello World', bar=3"

# Assignment expressions (aka: The Walrus Operator)
>>> a = 6
>>> if is_positive := a > 0:
...     print("It's positive!")
... else:
...     print("It's negative")
...
It's positive!
```

TypedDict is also pretty cool (example taken from [PEP-589](https://www.python.org/dev/peps/pep-0589/)):

```python
from typing import TypedDict


class Movie(TypedDict):
    name: str
    year: int


movie: Movie = {"name": "Blade Runner", "year": 1982}
```

## Python 3.9

Dictionary Union:

```python-repl
>>> a = {'foo': 'bar', 42: 1337}
>>> b = {'x': 'y', 'a': 'b', 'c': 'd', 'foo': 'foo'}
>>> a | b
{'foo': 'foo', 42: 1337, 'x': 'y', 'a': 'b', 'c': 'd'}
>>> b | a
{'x': 'y', 'a': 'b', 'c': 'd', 'foo': 'bar', 42: 1337}
```
