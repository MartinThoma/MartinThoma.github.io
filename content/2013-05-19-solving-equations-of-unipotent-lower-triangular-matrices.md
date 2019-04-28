---
layout: post
title: Solving equations of lower unitriangular matrices
slug: solving-equations-of-unipotent-lower-triangular-matrices
author: Martin Thoma
date: 2013-05-19 22:15:59.000000000 +02:00
category: Code
tags: Python, mathematics, Matrix, systems of equations, numerics
featured_image: 2013/05/unipotent-lower-triangular-matrix.png
---
Suppose you have an equation like $L \cdot x = b$ with $L \in \mathbb{R}^{n \times n}$ and $x,b \in \mathbb{R}^n$. $b$ and $L$ are given and you want to solve for $x$.

<h2>Example</h2>
With $n=5$, the problem could look like this:

$$\begin{pmatrix}
1 & 0 & 0 & 0 & 0\\
2 & 1 & 0 & 0 & 0\\
7 & 1 & 1 & 0 & 0\\
8 & 2 & 8 & 1 & 0\\
1 & 8 & 2 & 8 & 1
\end{pmatrix} \cdot 
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} =
\begin{pmatrix}   3 \\ 1   \\ 4   \\ 1   \\ 5   \end{pmatrix}$$

This is only a shorthand for:
\begin{align}
&1 \cdot x_1 &= 3 \\
&2 \cdot x_1 + 1 \cdot x_2 &= 1\\
&7 \cdot x_1 + 1 \cdot x_2 + 1 \cdot x_3 &= 4\\
&8 \cdot x_1 + 2 \cdot x_2 + 8 \cdot x_3 + 1 \cdot x_4 &= 1\\
&1 \cdot x_1 + 8 \cdot x_2 + 2 \cdot x_3 + 8 \cdot x_4 + 1 \cdot x_5 &= 5
\end{align}

This is easy to solve, isn't it?
<h3>First step: Solve for $x_1$</h3>
First you see that $x_1 = 3$. Now you replace every occurence of $x_1$ in the system of equations above:

\begin{align}
&1 \cdot 3 &= 3 \\
&2 \cdot 3 + 1 \cdot x_2 &= 1\\
&7 \cdot 3 + 1 \cdot x_2 + 1 \cdot x_3 &= 4\\
&8 \cdot 3 + 2 \cdot x_2 + 8 \cdot x_3 + 1 \cdot x_4 &= 1\\
&1 \cdot 3 + 8 \cdot x_2 + 2 \cdot x_3 + 8 \cdot x_4 + 1 \cdot x_5 &= 5
\end{align}

Now you make the multiplications and remove the first trivial line.

\begin{align}
&6 + 1 \cdot x_2 &= 1\\
&21 + 1 \cdot x_2 + 1 \cdot x_3 &= 4\\
&24 + 2 \cdot x_2 + 8 \cdot x_3 + 1 \cdot x_4 &= 1\\
&3 + 8 \cdot x_2 + 2 \cdot x_3 + 8 \cdot x_4 + 1 \cdot x_5 &= 5
\end{align}

<h3>Second step: update</h3>
Get the constant factors to the right side of the equations:

\begin{align}
&1 \cdot x_2 &= 1-6=-5\\
&1 \cdot x_2 + 1 \cdot x_3 &= 4-21=-17\\
&2 \cdot x_2 + 8 \cdot x_3 + 1 \cdot x_4 &= 1-24=-23\\
&8 \cdot x_2 + 2 \cdot x_3 + 8 \cdot x_4 + 1 \cdot x_5 &= 5-3=2
\end{align}

You can now easily see that you're in the same situation as in the first step! Next you will solve for $x_2$, then for $x_3, x_4$ and finally for $x_5$.

This is the reason why solving such a system of equations is sometimes called "forward substitution".

<h2>Python straightforward algorithm</h2>
```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solveLowerUnitriangularMatrix(L, b):
    x = [0] * len(b)
    for step in range(0, len(b)):
        x[step] = b[step]
        for row in range(0, len(b)):
            b[row] = b[row] - L[row][step]*x[step]
    return x

if __name__ == "__main__":
    L = [[1, 0, 0, 0, 0],
         [2, 1, 0, 0, 0],
         [7, 1, 1, 0, 0],
         [8, 2, 8, 1, 0],
         [1, 8, 2, 8, 1]]
    b =  [3, 1, 4, 1, 5]

    print(solveLowerUnitriangularMatrix(L, b))

```

Pretty easy, isn't it? But can we even do better?

<h2>Even better algorithm</h2>
Yes, we can!

Take a look at what's happening when row = 0 in line 9. We make a step that is not necessary. Also, we can take the space of b to store x!

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solveLowerUnitriangularMatrix(L, b):
    for step in range(0, len(b)):
        for row in range(step+1, len(b)):
            b[row] -= L[row][step]*b[step]

if __name__ == "__main__":
    L = [[1, 0, 0, 0, 0],
         [2, 1, 0, 0, 0],
         [7, 1, 1, 0, 0],
         [8, 2, 8, 1, 0],
         [1, 8, 2, 8, 1]]
    b =  [3, 1, 4, 1, 5]

    solveLowerUnitriangularMatrix(L, b)
    print(b)

```

Now it looks super clean, doesn't it ☺

Keep in mind that you have to store b if you need the values after you've applied this algorithm.
This is the reason why there here. This algorithm "returns" its value by manipulating b.

<h2>Time complexity</h2>
I'll analyze the second algorithm.

Let's assume that line 7 takes $c$ operations and $n$ is the size of $L \in \mathbb{R}^{n \times n}$.

Then we would have a total of 

\begin{align}
\text{Operations} &= \sum_{i=1}^n \left ( \sum_{j=i+1}^n c \right )\\
&= c \cdot \sum_{i=1}^n \left ( \sum_{j=i+1}^n 1 \right )\\
&= c \cdot \sum_{i=1}^n (n - i)\\
&= c \cdot \left ( \sum_{i=1}^n n - \sum_{i=1}^n i \right )\\
&= c \cdot \left ( n^2 - \frac{n^2+n}{2} \right )\\
&= \frac{c}{2} (n^2 - n)
\end{align}

So the algorithms time complexity is in $\Theta(n^2) \subsetneq \mathcal{O}(n^2)$.

<h2>Space complexity</h2>
Well, thats simple: $\mathcal{O}(1)$!

I do ignore the size of the input. So $\mathcal{O}(1)$ means: For variable sized input data I do need a constant amount of additional space.

<h2>More improvements</h2>
In the last algorithm I've presented you can see that we actually don't check the values on or above of the diagonal. 
This means, the following two function calls do give the same b:

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solveLowerUnitriangularMatrix(L, b):
    for step in range(0, len(b)):
        for row in range(step+1, len(b)):
            b[row] -= L[row][step]*b[step]
    return L

if __name__ == "__main__":
    L = [[1, 0, 0, 0, 0],
         [2, 1, 0, 0, 0],
         [7, 1, 1, 0, 0],
         [8, 2, 8, 1, 0],
         [1, 8, 2, 8, 1]]
    b =  [3, 1, 4, 1, 5]
    solveLowerUnitriangularMatrix(L, b)
    print(b)

    L = [[10, 9, 8, 7, 6],
         [2, 5, 4, 3, 2],
         [7, 1, 1, 0, 1],
         [8, 2, 8, 2, 3],
         [1, 8, 2, 8, 4]]
    b =  [3, 1, 4, 1, 5]
    solveLowerUnitriangularMatrix(L, b)
    print(b)

```

So, theoretically, we could store some other information on and above of the diagonal. We also don't change L. Keep this in mind, this might be important in later articles.
