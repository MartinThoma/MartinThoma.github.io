---
layout: post
title: Polynomial interpolation
author: Martin Thoma
date: 2013-06-22 18:41:43.000000000 +02:00
category: Code
tags: mathematics, numerical analysis, JavaScript, numerics, polynomial, canvas
featured_image: 2013/06/polynom.png
---
Suppose you have a list of $n+1$ given point $(x_i, y_i)$ with $i \in \{0, \dots, n\}$ and $\forall i,j \in \{0, \dots, n\}: i \neq j \Rightarrow x_i \neq x_j$.

Now you want to find a polynomial $\displaystyle p(x) = \sum_{i=0}^n a_i \cdot x^i$ that goes through all of the given points. This means:

$\forall i \in \{0, \dots, n\}: p(x_i) = y_i$

<h2>Existence and uniqueness</h2>
<strong>Theorem</strong>: When you have a list of $n+1$ points with mutually different $x_i$ there is exactly one polynom of degree $\leq n$ that fits those points.

<strong>Proof</strong>:

You can formulate a linear system of equations:

$$\underbrace{\begin{pmatrix}
 x_0^0 & \cdots & x_0^n \\
\vdots & \ddots & \vdots \\
 x_n^0 & \cdots & x_n^n
\end{pmatrix}
}_{:= A \in \mathbb{R}^{(n+1) \times (n+1)}}
\begin{pmatrix}
a_0 \\
\vdots \\
a_n
\end{pmatrix}
=
\begin{pmatrix}
y_0 \\
\vdots \\
y_n
\end{pmatrix}$$

A matrix of the form of $A$ is called <a href="https://en.wikipedia.org/wiki/Vandermonde_matrix">Vandermonde matrix</a>. When the data points $x_i$ are mutually different, it is known that the Vandermonde matrix is invertible (<a href="http://math.stackexchange.com/q/426932/6876">source</a>).

This means, the solution $(a_0 \dots a_n)^T$ of this linear equation gives the polynom $p(x) = \sum_{i=0}^n a_i x^i$

So the solution exists and is unique $\blacksquare$

<h2>Straight forward interpolating polynomials</h2>
For this algorithm, I'll find the polynomial in its monomial from $p(x) = \sum_{i=0}^n a_i x^i$. I'll use the matrix $A$ from section "<a href="#Uniqueness">Uniqueness</a>".

You might want to take a look at my article about <a href="../solving-linear-equations-with-gaussian-elimination/" title="Solving linear equations with Gaussian elimination">Gaussian elimination</a>.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pprintGaus(A):
    """ Pretty print a n&times;n matrix with a result vector n&times;1. """
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n + 1):
            line += str(A[i][j]) + "\t"
            if j == n - 1:
                line += "| "
        print(line)
    print("")


def pprintPolynomial(A):
    """ Pretty print a polynomial. """
    line = ""
    for i in range(len(x) - 1, -1, -1):
        if x[i] != 0:
            if i == 0:
                line += "+" + str(x[i])
            else:
                if x[i] == 1:
                    line += "+ x^" + str(i) + "\t"
                elif x[i] == -1:
                    line += "- x^" + str(i) + "\t"
                else:
                    line += "+" + str(x[i]) + "&middot;x^" + str(i) + "\t"
    print(line)


def gauss(A):
    """ Solve a linear sysem of equations given by a n&times;n matrix
        with a result vector n&times;1. """
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = A[k][i]
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def setGauss(points):
    """ Create a system of equations for gaussian elimination from
        a set of points. """
    n = len(points) - 1
    A = [[0 for i in range(n + 2)] for j in range(n + 1)]
    for i in range(n + 1):
        x = points[i]["x"]
        for j in range(n + 1):
            A[i][j] = x ** j
        A[i][n + 1] = points[i]["y"]
    return A


if __name__ == "__main__":
    from fractions import Fraction

    # Read input data
    points = []
    points.append({"x": Fraction(-1), "y": Fraction(1)})
    points.append({"x": Fraction(1), "y": Fraction(1)})
    points.append({"x": Fraction(2), "y": Fraction(2)})

    A = setGauss(points)

    # Print input
    pprintGaus(A)

    # Calculate solution
    x = gauss(A)

    # Print result
    pprintPolynomial(x)
```

It is also interesting to get the value of $p(x)$ at any given point $x \in \mathbb{R}$:

```python
def evaluatePolynomial(p, x):
    y = 0
    xi = 1
    for i, a in enumerate(p):
        y += a * xi
        xi *= x
    return y
```

Time complexity to get the polynomial: $\frac{1}{3} n^3 + \mathcal{O}(n^2)$ (where $n$ is the number of points)
Space complexity for the polynomial: $\mathcal{O}(n^2)$ (where $n$ is the number of points)

Time complexity to evaluate the value of $p(x)$ for any $x \in \mathbb{R}$: $\mathcal{O}(n)$.

<h2>Polynomials</h2>
$\displaystyle \mathbb{R}_n[X] := \left \{p:\mathbb{R} \rightarrow \mathbb{R} | p(x) = \sum_{i=0}^n a_i \cdot x^i \text{ with } a_0, \dots, a_n \in \mathbb{R} \right \}$

So $\mathbb{R}_n[X]$ are all polynomials with real coefficients and degree not higher than latex]n$. $\mathbb{R}_n[X]$ forms a vector space for $n \in \mathbb{N}_0$. The degree of that vector space is $n+1$.

What does that mean?

This means you can use different bases for polynomials. The base we usually use for $\mathbb{R}_n[X]$ is $\{x^0, x^1, x^2, x^3, \dots\}$, but you can switch the base.

<h2>Lagrange interpolation</h2>
Define $n+1$ polynomials like this:

$\displaystyle L_{i}(x) := \prod_{j=0 \atop j \neq i}^n \frac{x-x_j}{x_i - x_j}$

This means:

$\displaystyle L_{i}(x_i) := \prod_{j=0 \atop j \neq i}^n \frac{x_i-x_j}{x_i - x_j} = 1$

and

$\displaystyle L_{i}(x_p) := \prod_{j=0 \atop j \neq i}^n \frac{x_p-x_j}{x_i - x_j} = 0 \;\; p \in \{0, \dots, n\} \setminus \{i\}$

So the polynomial $y_i \cdot L_{i}(x)$ fits the point $(x_i, y_i)$ and is zero for all other points. This implies that $\displaystyle p(x) = \sum_{i=0}^n y_i \cdot L_i(x)$ is an interpolation of our data points. The degree of $p(x)$ is not higher than $n$. You can see that easily when you take a look at the definition of $p(x)$ and $L_i(x)$.

The polynomials $L_i(x)$ form another base for $\mathbb{R}_n[X]$.

Lagranges way to interpolate polynomials can be implemented like this:

```python
def lagrangeInterpolation(points):
    p = []
    for i in range(len(points)):
        Li = {"y": points[i]["y"], "polynomial": []}
        for j in range(len(points)):
            if j == i:
                continue
            Li["polynomial"].append(
                {"sub": points[j]["x"], "divisor": points[i]["x"] - points[j]["x"]}
            )
        p.append(Li)
    return p


def evaluateLagrangePolynomial(p, x):
    y = 0
    for Li in p:
        prod = 1
        for term in Li["polynomial"]:
            prod *= (x - term["sub"]) / term["divisor"]
        y += Li["y"] * prod
    return y
```

Time complexity to get the polynomial: $n^2 + \mathcal{O}(n)$ (where $n$ is the number of points)
Space complexity for the polynomial: $\mathcal{O}(n^2)$ (where $n$ is the number of points)

Time complexity to evaluate the value of $p(x)$ for any $x \in \mathbb{R}$: $\mathcal{O}(n^2)$.

<h2>Newton interpolation</h2>
Define

$\displaystyle N_i(x) := \prod_{j=0}^{i-1} (x-x_j)$

So you know that

$N_i(x) = 0 \Leftrightarrow \exists p \in \{1, \dots, i\}: x = x_{i-p}$

So your polynomial is

$\displaystyle p(x) = \sum_{i=0}^n c_i \cdot N_i(x)$

for the correct $c_i$. You can do this by solving the following system of equations. Please note that you don't have to store that matrix to get those $c_i$, <a href="http://en.wikipedia.org/wiki/Divided_differences">divided differences</a> are better.

$$\begin{pmatrix}
1 & & & & 0 \\
1 & (x_1 - x_0) & & & \\
1 & (x_2 - x_0) & (x_2 - x_0)(x_2 - x_1) & & \\
\vdots & \vdots & & \ddots & \\
1 & (x_n - x_0) & \cdots & & \prod_{i=0}^{n-1}(x_n - x_i) \\
\end{pmatrix}
\cdot
  \begin{pmatrix} c_0 \\ \vdots \\ c_n \end{pmatrix}
= \begin{pmatrix} f_0 \\ \vdots \\ f_n \end{pmatrix}$$

You can get this lower triangular matrix like this:
```python
def getGaussSystemForNewton(points):
    n = len(points) - 1
    A = [[0 for i in range(n + 2)] for j in range(n + 1)]
    for j in range(0, n + 2):
        for i in range(j, n + 1):
            if j == 0:
                A[i][j] = 1
            else:
                A[i][j] = A[i][j - 1] * (points[i]["x"] - points[j - 1]["x"])
        if j == n + 1:
            for i in range(0, n):
                A[i][j] = points[i]["y"]
    return A
```

From my previous posts about <a href="../solving-equations-of-upper-triangular-matrices/">solving equations of upper triangular matrices</a> and <a href="../solving-equations-of-unipotent-lower-triangular-matrices/">lower unitriangular matrices</a> you know that the space complexity of this is in $\Theta(n^2)$.

According to Wikipedia, you can use <a href="http://en.wikipedia.org/wiki/Horner%27s_method">Horner's method</a> to evaluate this Polynom in $\mathcal{O}(n)$. But I really don't want to implement this today.

<h2>Interactive example</h2>
<iframe src="../html5/polynom-interpolation.htm" width="98%" height="700px"></iframe>

<ul>
  <li>Click to add points.</li>
  <li>Ctrl+Click to remove point.</li>
  <li>You can enter a function that is valid JavaScript in the text field.</li>
</ul>
