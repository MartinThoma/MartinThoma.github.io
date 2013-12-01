---
layout: post
status: publish
published: true
title: How to solve linear congruence equations
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 76368
wordpress_url: http://martin-thoma.com/?p=76368
date: 2013-09-01 17:43:49.000000000 +02:00
categories:
- Mathematics
tags:
- Python
- mathematics
comments: []
---
When you have a system of linear congruences like:
$
\begin{align}
x &\equiv 4 \mod 19\\
x &\equiv 12 \mod 37\\
x &\equiv 14 \mod 43
\end{align}
$

you can solve it quite easily.
Johannes Schickling has written a very nice <a href="http://schickling.github.io/algorithms/#/chinese-remainder-theorem">JavaScript Application</a> that applies the following algorithm online. I've used his source code to write the following Python code.

<h2>Pseudocode</h2>
[caption id="attachment_76382" align="aligncenter" width="500"]<a href="http://martin-thoma.com/wp-content/uploads/2013/09/SolveLinearCongruences.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/09/SolveLinearCongruences.png" alt="Solve a system of linear congruences" width="500" height="247" class="size-full wp-image-76382" /></a> Solve a system of linear congruences[/caption]

<h2>Python</h2>
{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ExtendedEuclideanAlgorithm(a, b):
	"""
		Calculates gcd(a,b) and a linear combination such that
		gcd(a,b) = a*x + b*y

		As a side effect:
		If gcd(a,b) = 1 = a*x + b*y
		Then x is multiplicative inverse of a modulo b.
	"""
	aO, bO = a, b

	x=lasty=0
	y=lastx=1
	while (b!=0):
		q= a/b
		a, b = b, a%b
		x, lastx = lastx-q*x, x
		y, lasty = lasty-q*y, y

	return {
		"x": lastx,
		"y": lasty,
		"gcd": aO * lastx + bO * lasty
	}

def solveLinearCongruenceEquations(rests, modulos):
	"""
	Solve a system of linear congruences.

	>>> solveLinearCongruenceEquations([4, 12, 14], [19, 37, 43])
	{'congruence class': 22804, 'modulo': 30229}
	"""
	assert len(rests) == len(modulos)
	x = 0
	M = reduce(lambda x, y: x*y, modulos)

	for mi, resti in zip(modulos, rests):
		Mi = M / mi
		s = ExtendedEuclideanAlgorithm(Mi, mi)["x"]
		e = s * Mi
		x += resti * e
	return {"congruence class": ((x % M) + M) % M, "modulo": M}

if __name__ == "__main__":
	import doctest
	doctest.testmod()
{% endhighlight %}

<h2>Links</h2>
<ul>
  <li><a href="http://schickling.github.io/algorithms/#/chinese-remainder-theorem">Try it online</a></li>
  <li><a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/source-code/Pseudocode/SolveLinearCongruences">Sources</a></li>
</ul>
