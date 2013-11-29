---
layout: post
status: publish
published: true
title: ! 'Python Puzzle #2: None and False'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 34931
wordpress_url: http://martin-thoma.com/?p=34931
date: 2012-08-01 17:00:55.000000000 +02:00
categories:
- Code
tags:
- Programming
- Python
- puzzle
- boolean expression
comments: []
---
Python automatically casts to boolean if you use another type of variable for a boolean expression.

Here is an example:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

if [1]:
    print("Crazy, ")
if 1:
    print("this ")
if 2:
    print("is ")
if True:
    print("also ")
if "a string":
    print("true.")

print("")

if not None:
    print("This ")
if not False:
    print("is ")
if not 0:
    print("not ")
if not []:
    print("true."){% endhighlight %}

Everything gets printed.

Now the riddle. What is the output of the following script:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

if None == False:
    print("None is false.")
else:
    print("None and false are not equal."){% endhighlight %}

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

<h2>Answer</h2>
{% highlight bash %}None and false are not equal.{% endhighlight %}

<h2>Explanation</h2>
Although <code>None</code> and <code>False</code> evaluate to <code>False</code> if they are used in a boolean expression, <code>None</code> is not the same as <code>False</code>.
