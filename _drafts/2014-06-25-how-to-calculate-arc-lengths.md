---
layout: post
title: How to calculate arc lengths
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Mathematics
tags:
- calculus
featured_image: logos/calculus.png
---

In the following article I will assume that every reader knows how to integrate
simple formulas like \\(\int x^2 \mathrm{d}x\\). This is absolutely necessary to
understand how to calculate arc lengths.

So, as you know the blue area can be calculated fairly easy:

{% caption align="aligncenter" width="500" alt="quadratic function" text="quadratic function" url="../images/2014/06/x-2-quadratic-function.png" %}

It is:

$$\begin{align}
\int_0^1 x^2 \mathrm{d}x &= [\frac{1}{3} x^3]_0^1
&= \frac{1}{3}
\end{align}$$

But do you know how to calculate the length of the red arc between 0 and 1?
I guess you might have to think a second about it.

## The mind model

Do you remember how integrals were introduced? Quite probably you got to see
a function and a lot of rectangles that were right below the function. Then
the side length of those rectangles was reduced and more rectancles were
introduced. So we reduced the complex problem of calculating the area under a
function to calculating many squares.

Now try to apply that mind model to a curve. The most natural way to do this
is by thinking about a way somebody goes. So you transform the function to
its parametric form:

\[x(t) = t\]
\[y(t) = (x(t))^3 = t^3\]

with \\(t \in [0,1]\\).

Now we know that if we walked a straight line from \\((x_1, y_1)\\) to \\(x_2, y_2\\)
we would walk

\[\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}}\]

Now we can take \\(n\\) intermediate points to approximate the arc length of the
curve:

\[\sum_{i=1}^{n-1} \sqrt{(x_{i}-x_{i+1})^2 + (y_{i}-y_{i+1})^2}}\]

This will be equal to the arc length when we build the limes:

\[\lim_{n\rightarrow\infty}\sum_{i=1}^{n-1} \sqrt{(x_{i}-x_{i+1})^2 + (y_{i}-y_{i+1})^2}}\]

Now remember the Mean Value Theorem:

There is a point \\(x_i^* \in [x_i, x_{i+1}]\\) such that:

\[\begin{align}f(x_{i+1}) - f(x_{i}) &= f'(x_i^*) (x_{i+1} - x_i)\\
\Leftrightarrow y_{i+1} - y_{i} &= f'(x_i^*) (x_{i+1} - x_i)
\end{align}\]

thus

\[\begin{align}
\text{arc length} &= \lim_{n\rightarrow\infty}\sum_{i=1}^{n-1} \sqrt{(x_{i}-x_{i+1})^2 + (f'(x_i^*) (x_{i+1} - x_i))^2}}\\
&= \lim_{n\rightarrow\infty}\sum_{i=1}^{n-1} \sqrt{(1 + f'(x_i^*)^2)} \cdot (x_{i+1} - x_i))^2}\\
\end{align}\]

So the length of a curve in parametric form is

\[\text{arc lenght} = \int_a^b \sqrt{\left ( \frac{\mathrm{d} x}{\mathrm{d} t} \right )^2 + (\frac{\mathrm{d} y}{\mathrm{d} t})^2}\mathrm{d} t\]


## Circle

Take a circle with radius \\(r\\) with center \\((0, 0)\\) for example:

\[x(t) = r \cdot \cos(t)\]
\[y(t) = r \cdot \sin(t)\]

with \\(t \in [0, 1]\\). Then

\[\begin{align}
\text{arc} &= \int_0^{2 \pi} \sqrt{((-r \cdot \sin(t))^2 + (r \cdot \cos(t))^2} \mathrm{d} t\\
&= r \int_0^{2 \pi} \sqrt{1} \mathrm{d} t\\
&= r \int_0^{2 \pi} 1 \mathrm{d} t\\
&= r [t]_0^{2 \pi}\\
&= 2 \pi r\\
\end{align}\]
