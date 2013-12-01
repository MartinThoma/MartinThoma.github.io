---
layout: post
status: publish
published: true
title: ! 'Project Euler: Problem 26'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 39711
wordpress_url: http://martin-thoma.com/?p=39711
date: 2012-08-13 17:00:49.000000000 +02:00
categories:
- Code
tags:
- Challenge
- mathematics
- Project Euler
- brute-force
comments: []
---
The task in <a href="http://projecteuler.net/problem=26">Problem 26</a> of Project Euler is:

<blockquote>Find the value of d < 1000 for which $\frac{1}{d}$ contains the longest recurring cycle in its decimal fraction part.</blockquote>

<h2>How to solve</h2>
Think about how you divide with pen and paper. How do you recognize that you have a cycle?

You look at the rest. If you've seen the rest before, you are just about to get into the cycle.

<h2>My solution</h2>
This brute force solution finds the solution instantly.

{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

def getCycle(p, q):
    assert p >= 0
    assert q > 0

    while p >= q:
        p -= q

    if p == 0:
        # p/q is an integer
        return ""

    digits = {} # map rest to digit number
    # for 0.1234567, 1 is the digit #0, 2 digit #1, ...

    i = 0
    cycle = ""
    rest = p

    while True:
        digits[rest] = i
        rest *= 10
        tmp = rest / q
        rest -= tmp*q
        cycle += str(tmp)
        if rest in digits:
            return cycle[digits[rest]:]
        i += 1

def euler26(maximum=1000):
    maxCycleLength = 0
    number = 1
    for i in xrange(1, maximum +1):
        tmp = len(getCycle(1, i))
        if tmp > maxCycleLength:
            maxCycleLength = tmp
            number = i
    return (number, maxCycleLength)

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_simpleSequences(self):
        self.assertEqual(getCycle(4,2), "")
        self.assertEqual(getCycle(1,6), "6")
        for i in xrange(1,9):
            self.assertEqual(getCycle(i,9), str(i))
        self.assertEqual(getCycle(1,7), "142857")

if __name__ == '__main__':
    #unittest.main()
    print euler26(1000){% endhighlight %}
