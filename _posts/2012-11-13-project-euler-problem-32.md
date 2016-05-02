---
layout: post
title: Project Euler: Problem 32
author: Martin Thoma
date: 2012-11-13 11:52:12.000000000 +01:00
category: Code
tags: Challenge, Project Euler, brute-force
featured_image: 2012/04/leonhard-euler.jpg
---
The task in Problem 32 of Project Euler is:

<blockquote>We shall say that an $n$-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, $39 \cdot 186 = 7254$, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</blockquote>

<h2>How to solve it</h2>
We have to get a check, if a number is pandigital. It could look like this:

```python
def isPandigitalString(string):
    """ Check if string contains a pandigital number. """
    digits = len(string)

    if digits >= 10:
        return False

    for i in xrange(1,digits+1):
        if str(i) not in string:
            return False
    return True
```

We also need a check if a product of two numbers is 9-pandigital:
```python
def gives9PandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigitalString(numbers)
```

Now you need to figure out how to go through all possible combinations:
```python
products = []
for a in xrange(0, 100000):
    for b in xrange(a, 100000):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if gives9PandigitalProduct(a, b):
            products.append(a*b)
            print("%i x %i = %i" % (a, b, a*b))

print(sum(set(products)))
```

<h2>One-liner</h2>
This is from Thaddeus Abiye from Ethiopia:
```python
print sum(set(map(lambda x:int(x[0:4]),filter(lambda x:sorted([i for i in x])==map(str,range(1,10)),[str(a*b)+str(a)+str(b) for a in range(1,2000) for b in range(1,100)]))))
```

It needs one line and 173 characters, but I think it's hard to read.

<h2>Data about my solution</h2>
<ul>
  <li>It worked in less than a second.</li>
  <li>28 LOC (including whitespaces and comments)</li>
  <li>719 characters for this solution (including whitespace and comments)</li>
</ul>
