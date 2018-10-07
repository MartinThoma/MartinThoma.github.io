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

The principles layed out below can be grouped in several categories:

* <span class="label label-info">Mental Load</span>: Understanding code is
  difficult. Some principles help to reduce the difficulty.
* <span class="label label-info">Speed</span>: Make the code run faster
* <span class="label label-info">Extendability</span>: Code is rarely ever
  finished. New features have to be added all the time. Principles with this
  tag make it easier to extend the code in a clean way.
* <span class="label label-info">Debugging</span>


## Dictionaries

### Get

Bad:

```
if 'key' in a_dictionary:
    foobar = a_dictionary['key']
else:
    foobar = 'a default value'
```

Good:

```
foobar = a_dictionary.get('key', 'a default value')
```

Reasons:

* Easier to read, because less lines of code <span class="label label-info">Mental Load</span>
* Looking up 'key' only once <span class="label label-info">Speed</span>


## Error case checking

A common problem is to check many error-cases until you do whatever you want to
do.

Bad:

```
def foo(bar):
    if a(bar):
        b = c(bar)
        if b != 'xy':
            doit(bar)
```

Better:

```
def foo(bar):
    if not a(bar):
        return

    b = c(bar)
    if b == 'xy':
        return

    doit(bar)
```

The reason why code structured like this is because:

* <span class="label label-info">Mental Load</span> Easier to read - first
  error checking, then the stuff that needs to be done
* <span class="label label-info">Extendability</span>: Imagine there was
  another error case you forgot that needs to be checked in the beginning.
  Then, using the pattern above, you would need to reindent all of the code.


## Make Variable Names Pronouncable

Bad: `cfg`

Good: `config`

<span class="label label-info">Mental Load</span>


## Comments

1. <span class="label label-info">Mental Load</span> When you write a comment,
   could it rather be a better variable name?
2. When you write a comment, should it be a log statement?

## NamedTuples instead of Tuples

Bad: tuple

```
(1337, 42)
```

Better: [`namedtuple`](https://docs.python.org/2/library/collections.html#collections.namedtuple)

```
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point
<class '__main__.Point'>
>>> Point(133, 123)
Point(x=133, y=123)
```

* <span class="label label-info">Extendability</span> In places that might be
  far from the point of creation of the tuple, it is way easier to understand
  what this was about.
* <span class="label label-info">Debugging</span> In places that might be
  far from the point of creation of the tuple, it is way easier to understand
  what this was about


## Keyword-Arguments instead of positional arguments


## Minimum variable length

I use `grep` a lot when I develop. For projects I work on I have a very rough
call graph in mind, so I know a bit how my projects modules / objects interact
with each other. When I want to extend functionality, I grep for the part where
I need to adjust things (or I simply use <kbd>Ctrl</kbd> + <kbd>f</kbd>).
Hence, for every semantically meaningful variable it is good to have variables
which are not parts of other words. A common one where it is fine to have a
short name is having iterators that are just `i` (an index integer). A common
one which I don't like is `tmp`.


## Naming constants

Bad:

```
t0 = time.time()
some_code()
t1 = time.time()
execution_time = (t1 - t0) / 3600
```

Better:

```
t0 = time.time()
some_code()
t1 = time.time()
SECONDS_IN_A_HOUR = 3600
execution_time_in_hours = (t1 - t0) / SECONDS_IN_A_HOUR
```

Reasons why it is better:

* <span class="label label-info">Extendability</span> It is easier to
  understand which formats are converted here.


Even better: Use a unit library like [pint](https://pint.readthedocs.io/en/latest/index.html).
This way, it is guaranteed that the units will not accidentially be used in the
wrong way.

```
import pint
ureg = pint.UnitRegistry()

execution_time = (t1 - t0) * ureg.second
execution_time.to(ureg.hour).magnitude
```


## First List Pop

Bad:

```
del list_[0]
list_.pop(0)
list_.insert(0, 'foobar')
```

Better: use [`deque`](https://docs.python.org/3/library/collections.html#collections.deque)

Reason: <span class="label label-info">Speed</span> - see [time complexity of data structure operations](https://wiki.python.org/moin/TimeComplexity)


## Avoid Mental Mapping

Worst:

```
list_ = ['a@de.com', 'foobar@fg.com', 'hot@martin.com']
for i in range(len(list_)):
    send(list_[i])
```

Bad:

```
list_ = ['a@de.com', 'foobar@fg.com', 'hot@martin.com']
for el in list_:
    send(el)
```

Better:

```
email_addresses = ['a@de.com', 'foobar@fg.com', 'hot@martin.com']
for email_address in email_addresses:
    send(email_address)
```

<span class="label label-info">Mental Complexity</span> Here we don't iterate
over an integer number. We iterate over items. Those items have a semantic
type. What would we say in natural language to describe the code? Surely
something like:

> To each email address which we gathered before, we send a mail.

The last one is was closer to this natural form than the other two ones are.


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


## Don't add unnecessary prefixes / suffixes

For example, a `Person` class does not need a `person_id` property. It is
simply an id.


## Use at most 3 function parameters

This is not a hard rule, but certainly one that most often is a good idea.
Functions with many parameters are super hard to digest. Often, it makes more
sense to pass the function an object, e.g. a [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple). 
