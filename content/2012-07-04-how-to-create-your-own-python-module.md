---
layout: post
lang: en
title: How to create your own Python module
slug: how-to-create-your-own-python-module
author: Martin Thoma
date: 2012-07-04 16:11:54.000000000 +02:00
category: Code
tags: Python
featured_image: 2011/09/Python-Logo.png
---
A python module is a container for some definitions and statements. You generally call it like this:
```python
import math
```
or like that
```python
from math import ceil
```
or
```python
import math as mymath
```

Python modules can also be written in C or C++, but I'll only explain how to write the module in Python. Modules can be written in C++ for performance reasons. Just take a look at <code>/usr/lib/python3.1/lib-dynload</code> with all the *.so files (shared libraries).

<h2>Python Paths</h2>
When you try to import a module, Python looks at these directories in the given order:
<ul>
  <li>the PYTHONPATH</li>
  <li>the current working directory</li>
  <li>the default search path</li>
</ul>

You get your PYTHONPATH and your default search path like this:
```python
import os

os.environ["PATH"].split(os.pathsep)
os.environ["PYTHONPATH"].split(os.pathsep)
```

<h2>Example</h2>
I've just searched for a Python module for primes. It seems as if no such module existed. So I wrote the module <strong>primes.py</strong>.

```python
"""
This module offers some functions related to primes.
"""


def miller_rabin(n):
    import random

    """ Source: http://en.literateprograms.org/
                    Miller-Rabin_primality_test_(Python)
        """

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def getPrimeFactors(n):
    """Return the prime factors of n.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [getPrimeFactors(n) for n in range(11)]
    [[], [], [2], [3], [2, 2], [5], [2, 3], [7], [2, 2, 2], [3, 3], [2, 5]]

    >>> getPrimeFactors(36)
    [2, 2, 3, 3]
    """
    import math

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    elif n <= 2147483647:
        n = int(n)
    else:
        n = long(n)

    fact = []

    if n == 0:
        return fact

    while n % 2 == 0:
        fact.append(2)
        n /= 2

    if n == 1:
        return fact

    if miller_rabin(n):
        fact.append(n)
        return fact

    check = 3
    rootn = n ** 0.5
    while n != 1:
        while n % check == 0:
            fact.append(check)
            n /= check
        check += 2
    return fact


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

<h2>See also</h2>
<ul>
  <li><a href="http://docs.python.org/tutorial/modules.html">Modules</a></li>
  <li><a href="http://www.python-kurs.eu/modularisierung.php">Modularisierung</a> (German)</li>
  <li><a href="http://stackoverflow.com/q/7948494/562769">What's the difference between a Python module and a Python package?</a></li>
  <li>Packages:
      <ul>
          <li><a href="http://guide.python-distribute.org/creation.html">Creating a Package</a></li>
          <li><a href="http://docs.python.org/distutils/introduction.html">An Introduction to Distutils</a></li>
      </ul>
  </li>
</ul>
