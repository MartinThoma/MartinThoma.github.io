---
layout: post
title: Writing Unittests in Python
author: Martin Thoma
date: 2012-07-07 09:21:46
categories: 
- Code
tags:
- Python
featured_image: 2011/09/Python-Logo.png
---
Python offers a package called "unittest" which allows writing unittests in Python. I will only give small examples. If you want to learn how to create Unittests, you should probably read the <a href="http://docs.python.org/library/unittest.html">documentation</a>.

<blockquote>The Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit, by Kent Beck and Erich Gamma. JUnit is, in turn, a Java version of Kent’s Smalltalk testing framework. Each is the de facto standard unit testing framework for its respective language.

unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework. The unittest module provides classes that make it easy to support these qualities for a set of tests.</blockquote>




<h2>First very basic example</h2>
This is a unittest for simple <a href="https://github.com/MartinThoma/matrix-multiplication/blob/master/Python/ikjMultiplication.py">ikj Matrix Multiplication</a>:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from ikjMultiplication import ikjMatrixProduct

class TestCase(unittest.TestCase):    
    def test2Multiplication(self):
        A = [[1,2],[3,4]]
        B = [[5,6],[7,8]]
        C = ikjMatrixProduct(A, B)
        self.assertEqual(C, [[19,22],[43,50]])
        
    def test3Multiplication(self):
        A = [[1, 2, 5],[3,4,6],[1,1,1]]
        B = [[5, 6, 7],[7,8,8],[0,9,3]]
        C = ikjMatrixProduct(A, B)
        self.assertEqual(C, [[19,67,38],[43,104,71], [12,23,18]])
        
if __name__ == '__main__':
    unittest.main(){% endhighlight %}

The important part is <a href="http://docs.python.org/library/unittest.html#unittest.TestCase.assertEqual">self.assertEquals</a>.

When you run this unittest, you get this output:
{% highlight bash %}..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK{% endhighlight %}

<h2>See also</h2>
<ul>
  <li>Documentation: <a href="http://docs.python.org/library/unittest.html">unittest — Unit testing framework</a></li>
  <li><a href="../matrix-multiplication-python-java-cpp/" title="Part I: Performance of Matrix multiplication in Python, Java and C++">Part I: Performance of Matrix multiplication in Python, Java and C++</a></li>
</ul>
