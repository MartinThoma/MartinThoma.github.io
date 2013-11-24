---
layout: post
status: publish
published: true
title: ! 'Python Puzzle #1: List multiplication'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 27261
wordpress_url: http://martin-thoma.com/?p=27261
date: 2012-06-18 15:06:48.000000000 +02:00
categories:
- Code
tags:
- Programming
- Python
- puzzle
comments: []
---
<h2>Basic concepts</h2>
Image you had to multiply two small matrices in Python. You could just use the definition of a matrix product:

$A, B \in \mathbb{R}^{n \times n}$:
$C = A \cdot B, C \in \mathbb{R}^{n \times n}$ where the components of C are definied by
$c_{i,j} = \sum_{k=1}^n a_{i,k} \cdot b_{k, j}$

Note that this means:
$\begin{pmatrix} 
1 & 2 \\
3 & 4
\end{pmatrix} \cdot 
\begin{pmatrix} 
5 & 6 \\
7 & 8
\end{pmatrix} = 
\begin{pmatrix} 
19 & 22 \\
43 & 50
\end{pmatrix}$

You might also have heard of Pythons overloaded multiplication:
{% highlight python %}print([0]*4)
print([[0]*4]*4)
print("abc"*4){% endhighlight %}
Output:
[text][0, 0, 0, 0]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
abcabcabcabc[/text]

<h2>Question</h2>
What do you think does the following piece of Python-Code print?
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

def standardMatrixProduct(A, B):
	n = len(A)
	C = [[0]*n]*n
	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				C[i][j] += A[i][k] * B[k][j]
	return C

A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
print standardMatrixProduct(A, B){% endhighlight %}


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
[text][[32, 32], [32, 32]][/text]
Python creates only one list and makes pointers to it!

So this is one that works:
{% highlight python %}def standardMatrixProduct(A, B):
	n = len(A)
	C = [[0 for i in xrange(n)] for j in xrange(n)]
	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				print C
				C[i][j] += A[i][k] * B[k][j]
	return C{% endhighlight %}
