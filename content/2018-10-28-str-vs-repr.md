---
layout: post
title: Pythons str vs repr
slug: str-vs-repr
author: Martin Thoma
date: 2018-10-28 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
The goal of `__repr__` is to be unambiguous and the goal of `__str__` is to be readable. Bonus points, if `__repr__` returns what is needed to create the object. Some examples are:

```
>>> repr([42, 1337])
'[42, 1337]'
>>> repr({42, 1337})
'{1337, 42}'

>>> from collections import namedtuple
>>> Location = namedtuple('Location', ['lon', 'lat'])
>>> a = Location(12, 34)
>>> repr(a)
'Location(lon=12, lat=34)'

>>> import re; pattern = re.compile('foo')
>>> repr(pattern)
"re.compile('foo')"
```

In all of those cases the unambiguous representation and the readable string
are the same.


## Where it's used

The following code sample shows how `__repr__` and `__str__` are used:

```
class Foo(object):

    def __repr__(self):
        return '__repr__'

    def __str__(self):
        return '__str__'


if __name__ == '__main__':
    bar = Foo()

    print(bar)
    print(str(bar))
    print(repr(bar))
```

Playing with this gives the following insights:

* If neither `__repr__` nor `__str__` is implemented, then `bar` is printed as
  `<__main__.Foo object at 0x7f42319379e8>`
* If either of them is implemented, then `print(bar)` uses that one.
* If both of them are implemented, then `print(bar)` uses `__str__`.
* The REPL uses `__repr__`.


## 3rd Party Libraries

It's a bit different once you get to third party libraries:

```
>>> import numpy as np
>>> a = np.array([42, 1337])
>>> str(a)
'[  42 1337]'
>>> repr(a)
'array([  42, 1337])'
```

Some - like Pandas Dataframes have a very different string representation.

Others just don't care to implement somehting reasonable at all:

```
>>> from keras.models import Sequential
>>> model = Sequential()
>>> repr(model)
'<keras.engine.sequential.Sequential object at 0x7f8d86b8eb70>'
```


## Enums

Also - sadly - it is not done well with Enums:

```
class ExistsStrategy(enum.Enum):
    """Strategies what to do when a file already exists."""

    RAISE = 'raise'
    REPLACE = 'replace'
    ABORT = 'abort'

print(str(ExistsStrategy.RAISE))
print(repr(ExistsStrategy.RAISE))
```

The `str` gives `ExistsStrategy.RAISE` which is awesome. The `repr` gives
`<ExistsStrategy.RAISE: 'raise'>`. I don't understand why it doesn't give
the same result as the `str` representation.


## See also

* [Difference between `__str__` and `__repr__`?](https://stackoverflow.com/q/1436703/562769)
