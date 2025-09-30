---
layout: post
lang: en
title: The Absolute Value Function
slug: abs-function
author: Martin Thoma
date: 2017-02-20 20:00
category: Mathematics
tags: mathematics
featured_image: logos/mathematics.png
---
I was never really taught how to deal with the absolute value function, but
I need it from time to time. So here are a few hints.


## Solving Equations

Lets say you want to solve the equation

$$|x - a | = b$$

for $x$. Then you need to realize that this equation is equivalent to two
equations:

$$x - a = b \qquad \text{ and } \qquad -(x-a) = b$$

you can solve both of them independantly. You can get 0, 1 or 2 solutions
when the absolute function is involved:

$$x = a + b \qquad \text{ and } \qquad x = a - b$$
or shorter
$$x = a \pm b$$


## Solving Inequalities

Lets say you want to solve the inequality

$$|a - x| \leq b$$

for $x$. Again, this inequality is equivalent to the two inequalities

$$a - x \leq b \qquad \text{ and } \qquad -(a-x) \leq b$$

You can solve both of them independantly for $x$:

$$a - b \leq x \qquad \text{ and } \qquad -x \leq a + b$$

leading to

$$a - b \leq x \leq a + b$$

Note that both inequalities have to be fulfilled at the same time! Just try it
for $a = 0$ and $b = -5$!


## Derivatives

The function $f(x) = |x|$ is equivalent to $f(x) = \sqrt{x^2}$. Hence you can
derive the absolute value by deriving the root of the square function of its
argument. And the chain rule, of course:

\begin{align}
    f'(x) &= (\sqrt{x^2})'\\
          &= \frac{1}{2 \sqrt{x^2}} \cdot (2 x)\\
          &= \frac{x}{\sqrt{x^2}}\\
          &= \frac{x}{|x|}\\
          &= \text{sign}(x)
\end{align}

Note that the derivative is not devined at 0.


## See also

* [Wikipedia](https://en.wikipedia.org/wiki/Absolute_value)
