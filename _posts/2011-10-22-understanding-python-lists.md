---
layout: post
title: Understanding Python Lists
author: Martin Thoma
date: 2011-10-22 23:01:55.000000000 +02:00
category: Code
tags: Python
featured_image: 2011/09/Python-Logo.png
---
This article is about Python lists. I just want to show you some examples of the unexpected behavior (for non-python-programmers) of lists in Python.

Imagine you have the following Python source code:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

example1 = [[1,5,7],[3,6],[], [8,1,6]]
example2 = example1[:]
example3 = list(example1)
example4 = copy.deepcopy(example1)

example1[1][0] = 0
example1.append(1)

print example1
print example2
print example3
print example4{% endhighlight %}

How should the output look like? Think about it a second, then scroll down.
























{% highlight bash %}[[1,5,7],[0,6],[],[8,1,6],1]
[[1,5,7],[0,6],[],[8,1,6]]
[[1,5,7],[0,6],[],[8,1,6]]
[[1,5,7],[3,6],[],[8,1,6]]{% endhighlight %}

The reason for this strange behavior is how lists are handled in Python. The variable itself is basically only the pointer to the list. If you slice the list (myList[:]) you copy each value of the list into another list. If myList was a nested list, it contained the pointers to the sublists. So, if you want to make a deep copy, you have to use the copy module.

<h2>Scoping</h2>
phimuemue added this example in my old blog:

Another issue I ran into concerns the scoping of Python:
{% highlight python %}i=0
[i for i in [1,2,3]]
print (i) # yields 3{% endhighlight %}
That means, python doesn't create a new variable for the list comprehension but uses the outer i.

<h2>Recursive Lists</h2>
{% highlight python %}a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)
[1, 2, 3, [4, 5, 6]]
b.append(a)
print(b)
[4, 5, 6, [1, 2, 3, [...]]]
print(a)
[1, 2, 3, [4, 5, 6, [...]]]
{% endhighlight %}

Do you know more examples of unexpected behavior of python lists? Please share them in the comments!
