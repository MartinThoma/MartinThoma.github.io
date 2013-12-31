---
layout: post
title: How to build a spam filter with Bayes filter
author: Martin Thoma
date: 2013-08-05 12:55:38
categories: 
- Code
tags: 
- probability
featured_image: 
---
For a Bayes filter, you need training data. So you need emails that are labeled as "ham" and others that are labeled as "spam".

<h2>Laplace smoothing</h2>
I will use Laplace smoothing. This means, for every probability you add [latex]k[/latex] to the numerator and [latex]k \cdot d[/latex] to the denominator. [latex]k \in \mathbb{N}[/latex] is a smoothing factor (e.g. [latex]k=1[/latex]) and [latex]d \in \mathbb{N}[/latex] is the number of categories(so the number of different probabilities you could calculate).

<h2>Bayes filter</h2>
You have a message [latex]M[/latex] and want to know if it is spam. So you want to calculate [latex]P(Spam|M)[/latex]. Let [latex]M[i][/latex] be the [latex]i[/latex]-th word in [latex]M[/latex]. You do it like this:

[latex]\begin{align}
A &= P(Spam) \cdot P(M[1]|Spam) \cdot P(M[2]|Spam) \cdot \dots \cdot  \cdot P(M[n]|Spam)\\
B &= P(Ham) \cdot P(M[1]|Ham) \cdot P(M[2]|Ham) \cdot \dots \cdot  \cdot P(M[n]|Ham)\\
P(Spam|M) &= \frac{A}{A+B}
\end{align}[/latex]


<h2>See also</h2>
<ul>
  <li>Wikipedia:
    <ul>
      <li><a href="http://en.wikipedia.org/wiki/Bayes_filter">Bayes filter</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Laplace_smoothing">Laplace smoothing</a></li>
    </ul>
  </li>
  <li>Introduction to A.I. - Machine Learning
    <ul>
      <li><a href="https://www.youtube.com/watch?v=2Ar6jFKZhUM">Laplace Smoothing</a></li>
      <li><a href="https://www.youtube.com/watch?v=oh4uc-8O6Pc">Bayes filter</a></li>
    </ul>
</ul>