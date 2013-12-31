---
layout: post
title: Fitting linear data points with least squares method
author: Martin Thoma
date: 2013-09-08 06:40:21
categories: 
- Mathematics
tags: 
- Data
featured_image: 
---
Suppose you have [latex]n[/latex] 2D data points [latex]p_1, p_2, \dots, p_n[/latex] and you want to get the line that fits those data points best. A line has the format [latex]y = a \cdot x + b[/latex] where [latex]a[/latex] and [latex]b[/latex] describe the line.

Now we have to think about what "fits best" means. One way is to find [latex]a[/latex] and [latex]b[/latex] that minimize [latex]f: \mathbb{R}^2 \rightarrow \mathbb{R}[/latex] with [latex]f(a, b) := \sum_{i=1}^n \left ((a \cdot p_i[x] + b) - p_i[y] \right )^2[/latex].

Lets say [latex]a[/latex] was constant. Then we would be in a situation that should be familiar. This is a quadratic function in [latex]b[/latex]. So we can calculate [latex]b[/latex] like this: 

To make it easier to read I'll write [latex]x_i[/latex] for the [latex]x[/latex]-coordinate of the [latex]i[/latex]-th point (and the same for [latex]y[/latex]).

[latex]
\begin{align}
f(a,b) &= \sum_{i=1}^n \left ((a \cdot x_i + b) - y_i \right )^2\\
 &= \sum_{i=1}^n ((a x_i +b)^2 - 2 (a x_i+b) y_i + y_i^2)\\
 &= \sum_{i=1}^n ((a x_i)^2 + 2 a x_i b + b^2 -2 (a x_i+b) y_i + y_i^2)\\
\frac{\partial f(a,b)}{\partial b} &= \sum_{i=1}^n (2a x_i +2b - 2y_i)\\
 0 &\stackrel{!}{=} 2  \sum_{i=1}^n (a x_i +b - y_i)\\
\Leftrightarrow 0 &\stackrel{!}{=} \sum_{i=1}^n (a x_i +b - y_i)\\
\Leftrightarrow 0 &\stackrel{!}{=} a \sum_{i=1}^n x_i + n \cdot b - \sum_{i=1}^n y_i\\
\Leftrightarrow b &\stackrel{!}{=} \frac{\sum_{i=1}^n y_i -a \sum_{i=1}^n x_i}{n}\\
\Leftrightarrow b &\stackrel{!}{=} \bar y -a \bar x\\
\end{align}[/latex]

where [latex](\bar x, \bar y)[/latex] is the center of all points. Lets do the same with [latex]a[/latex]:

[latex]
\begin{align}
\frac{\partial f(a,b)}{\partial a} &= \sum_{i=1}^n (2a x_i^2 +2 x_i b - 2 x_i y_i)\\
 0 &\stackrel{!}{=} 2  \sum_{i=1}^n (a x_i^2 +x_i b - x_i y_i)\\
\Leftrightarrow 0 &\stackrel{!}{=} \sum_{i=1}^n (a x_i^2 +x_i b - x_i y_i)\\
\Leftrightarrow 0 &\stackrel{!}{=} a \sum_{i=1}^n x_i^2 + b \sum_{i=1}^n x_i -  \sum_{i=1}^nx_i y_i\\
\end{align}[/latex]