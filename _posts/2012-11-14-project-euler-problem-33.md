---
layout: post
title: ! 'Project Euler: Problem 33'
author: Martin Thoma
date: 2012-11-14 15:43:35.000000000 +01:00
category: Code
tags: Programming, Python, Challenge, Project Euler
featured_image: 2012/04/leonhard-euler.jpg
---
The task in <a href="http://projecteuler.net/problem=33">Problem 33</a> of Project Euler is:

<blockquote>The fraction $\frac{49}{98}$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $\frac{49}{98} = \frac{4}{8}$, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, $\frac{30}{50} = \frac{3}{5}$, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</blockquote>

<h2>How to solve</h2>
The solution to this task is pretty straight forward. As the nominator has to have two digits and the denominator also has to be in [10, 99], we only have about $100 \cdot 100 = 10000$ that we have to check.

How do we check a given nominator / denominator pair? Well, we can go through each digit of the nominator and check if it is also in the denominator. If it is there, we have to check if the resulting fraction has the same value as before. If it has, we can print it.

<h2>My solution</h2>
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

def isCuriousFraction(numerator, denomiator):
    for digit in str(numerator):
        if digit in str(denomiator):
            for i, j in [(i,j) for i in range(0,2) for j in range(0,2)]:
                if str(numerator)[i] == digit == str(denomiator)[j]:
                    if int(str(denomiator)[(j+1)%2]) == 0:
                        continue # devision through 0 is bad
                    canceled = float(str(numerator)[(i+1)%2]) / \
                                        int(str(denomiator)[(j+1)%2])
                    divided = float(numerator) / denomiator
                    if abs(canceled-divided) < 0.0001:
                            print("%i/%i = %s/%s" % (numerator, \
                                denomiator, str(numerator)[(i+1)%2],\
                                str(denomiator)[(j+1)%2]))
                            return True

if __name__ == "__main__":
    for i in xrange(10, 100):
        if i % 10 == 0: # those are not interesting
            continue
        for j in xrange(i+1, 100):
            isCuriousFraction(i, j)
```

<h2>Solving it without programming</h2>
You can also solve this without programming at all: See <a href="http://projecteuler.net/thread=33;page=8#86864">post</a>.
