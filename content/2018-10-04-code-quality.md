---
layout: post
title: Code Quality
slug: code-quality
author: Martin Thoma
status: draft
date: 2018-10-04 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
Here are some rules that help you to write code of high quality. They are
inspired by [Michael Toppa - 10 Tips For Clean Code](https://www.youtube.com/watch?v=UjhX2sVf0eg)

* Choose meaningful variable names
* Boy Scout Principle: Leave the code base cleaner than you found it
* Single Responsibility Principle: A function / method does only one thing
* Write Tests
* Independent Architecture
* Many arguments -> pass object, 
* Signal to noise ratio: How much of the desired signal is there compared to
  parts you don't want?

## Variable Names

### Make Variable Names Pronouncable

Bad: `cfg`

Good: `config`

## Comments

1. When you write a comment, could it rather be a better variable name?
2. When you write a comment, should it be a log statement?

## Readability

### NamedTuples instead of Tuples

Bad: tuple

```
(1337, 42)
```

Good: [`namedtuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple)

```
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point
<class '__main__.Point'>
>>> Point(133, 123)
Point(x=133, y=123)

```

### Keyword-Arguments instead of positional arguments

## Speed


### First List Pop

bad

```
del list_[0]
list_.pop(0)
list_.insert(0, 'foobar')
```

better:

Use [`deque`](https://docs.python.org/3/library/collections.html#collections.deque)


## ignored

```
try:
    os.remove('foobar')
except OSError:
    pass
```


with ignored:

```
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
```


only

```
with ignored(OSError):
    os.remove('foobar')
```
