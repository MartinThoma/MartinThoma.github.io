---
layout: post
title: Solving equations of upper triangular matrices
author: Martin Thoma
date: 2013-05-20 10:41:49.000000000 +02:00
categories:
- Code
tags:
- Python
- mathematics
- Matrix
- systems of equations
- numerics
featured_image: 2013/05/upper-triangular-matrix.png
---
Suppose you have an equation like $R \cdot x = b$ with $R \in \mathbb{R}^{n \times n}$ and $x,b \in \mathbb{R}^n$. $b$ and $R$ are given and you want to solve for $x$.

<h2>Example</h2>
With $n=5$, the problem could look like this:

$\begin{pmatrix}
2 & 7 & 1 & 8 & 2\\
0 & 8 & 1 & 8 & 2\\
0 & 0 & 8 & 4 & 5\\
0 & 0 & 0 & 9 & 0\\
0 & 0 & 0 & 0 & 4
\end{pmatrix} \cdot 
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix} =
\begin{pmatrix}   3 \\ 1   \\ 4   \\ 1   \\ 5   \end{pmatrix}$

This is only a shorthand for:
$
\begin{align}
2 \cdot x_1 + 7 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + 2 \cdot x_5 &= 3\\
              8 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + 2 \cdot x_5 &= 1\\
                            8 \cdot x_3 + 4 \cdot x_4 + 5 \cdot x_5 &= 4\\
                                          9 \cdot x_4 + 0 \cdot x_5 &= 1\\
                                                        4 \cdot x_5 &= 5
\end{align}
$

<h3>First step: Solve for $x_5$</h3>
First you see that $x_5 = \frac{5}{4}$. So you divide $b$ by the current row.

<div class="important">Don't divide through 0. When you would have to divide by 0 and b is 0, this system has an infinite amount of solutions. When you would have to divide by 0 and b is not 0, then this system has no solution.</div>

Now you replace every occurrence of $x_5$ in the system of equations above:

$
\begin{align}
2 \cdot x_1 + 7 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + 2 \cdot \frac{5}{4} &= 3\\
              8 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + 2 \cdot \frac{5}{4} &= 1\\
                            8 \cdot x_3 + 4 \cdot x_4 + 5 \cdot \frac{5}{4} &= 4\\
                                          9 \cdot x_4 + 0 \cdot \frac{5}{4} &= 1\\
                                                        4 \cdot \frac{5}{4} &= 5
\end{align}
$

Now you make the multiplications and remove the first trivial line.

$
\begin{align}
2 \cdot x_1 + 7 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + \frac{5}{2} &= 3\\
              8 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 + \frac{5}{2} &= 1\\
                            8 \cdot x_3 + 4 \cdot x_4 + \frac{25}{4} &= 4\\
                                          9 \cdot x_4 + 0 &= 1\\
\end{align}
$

<h3>Second step: update</h3>
Get the constant factors to the right side of the equations:
$
\begin{align}
2 \cdot x_1 + 7 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 &= \frac{1}{2} \\
              8 \cdot x_2 + 1 \cdot x_3 + 8 \cdot x_4 &= -\frac{3}{2} \\
                            8 \cdot x_3 + 4 \cdot x_4 &= -\frac{9}{4}\\
                                          9 \cdot x_4 &= 1\\
\end{align}
$

You're now in the same situation as in the first step. Next you will solve for $x_4$, then for $x_3, x_2$ and finally for $x_1$.

This is called "back substitution".

<a href="http://www.wolframalpha.com/input/?i=%7B%7B2%2C7%2C1%2C8%2C2%7D%2C%7B0%2C8%2C1%2C8%2C2%7D%2C%7B0%2C0%2C8%2C4%2C5%7D%2C%7B0%2C0%2C0%2C9%2C0%7D%2C%7B0%2C0%2C0%2C0%2C4%7D%7D%5E-1*%7B%7B3%7D%2C%7B1%7D%2C%7B4%7D%2C%7B1%7D%2C%7B5%7D%7D">According to Wolfram|Alpha</a>, the solution is:

$x = \frac{1}{4608} \cdot \begin{pmatrix}4017\\-1182\\-1552\\512\\5760\end{pmatrix} = 
\begin{pmatrix}\frac{1339}{1536} \\ -\frac{197}{768} \\ -\frac{97}{288} \\ \frac{1}{9} \\ \frac{5}{4}\end{pmatrix}$

<h2>Python straightforward algorithm</h2>
I will use <a href="http://docs.python.org/2/library/fractions.html">fractions</a> for operations as I don't want to lose precision while dividing.

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solveUpperTriangularMatrix(R, b):
    # Convert R and b to Fraction
    from fractions import Fraction
    fR, fb = [], []
    for x, line in enumerate(R):
        fLine = []
        for y, el in enumerate(line):
            fLine.append(Fraction(el))
        fR.append(fLine)
    for el in b:
        fb.append(Fraction(el))

    # The solution will be here
    x = [Fraction(0)] * len(b)
    for step in range(len(b)-1, 0-1, -1):
        if fR[step][step] == 0:
            if fb[step] != 0:
                return "No solution"
            else:
                return "Infinity solutions"
        else:
            x[step] = fb[step] / fR[step][step]

        for row in range(step-1, 0-1, -1):
            fb[row] -= fR[row][step]*x[step]
    return x

if __name__ == "__main__":
    R = [[2, 7, 1, 8, 2],
         [0, 8, 1, 8, 2],
         [0, 0, 8, 4, 5],
         [0, 0, 0, 9, 0],
         [0, 0, 0, 0, 4]]
    b =  [3, 1, 4, 1, 5]
    x = solveUpperTriangularMatrix(R, b)
    print(x)

    # Convert x to float
    x = map(float, x)
    print(x)
{% endhighlight %}

<h2>A better algorithm</h2>
Just like for <a href="../solving-equations-of-unipotent-lower-triangular-matrices/" title="Solving equations of unipotent lower triangular matrices">unipotent lower triangular matrices</a>, we can operate directly on the given input:

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solveUpperTriangularMatrix(R, b):
    # Convert R and b to Fraction
    from fractions import Fraction
    for x, line in enumerate(R):
        for y, el in enumerate(line):
            R[x][y] = Fraction(el)
    for x, el in enumerate(b):
        b[x] = Fraction(el)

    # The solution will be here
    for step in range(len(b)-1, 0-1, -1):
        if R[step][step] == 0:
            if b[step] != 0:
                return "No solution"
            else:
                return "Infinity solutions"
        else:
            b[step] = b[step] / R[step][step]

        for row in range(step-1, 0-1, -1):
            b[row] -= R[row][step]*b[step]

if __name__ == "__main__":
    R = [[2, 7, 1, 8, 2],
         [0, 8, 1, 8, 2],
         [0, 0, 8, 4, 5],
         [0, 0, 0, 9, 0],
         [0, 0, 0, 0, 4]]
    b =  [3, 1, 4, 1, 5]
    solveUpperTriangularMatrix(R, b)
    print(b)
{% endhighlight %}

<h2>Conversion to Fraction</h2>
You could think that the conversion to fraction is not necessary. But if you simply remove line 5 to 16, you will get:

{% highlight bash %}[1, 0, -1, 0, 1]{% endhighlight %}

because of integer arithmetic. When you convert the input to float before passing it to <code>solveUpperTriangularMatrix</code>, you will get 

{% highlight bash %}[0.8717447916666666, -0.25651041666666663, -0.3368055555555556, 0.1111111111111111, 1.25]{% endhighlight %}

which is almost the same as when we calculated with Fraction and converted to float afterwards:
{% highlight bash %}[0.8717447916666666, -0.2565104166666667, -0.3368055555555556, 0.1111111111111111, 1.25]{% endhighlight %}

So: Using Fractions needs some computing time, but you will get better results.

<h2>Time complexity</h2>
I'll analyze the second algorithm.

The conversion of our input data is obviously in $\mathcal{O}(n^2)$. Let's only analyse the part after the conversion.

Assume that there is exactly one solution and that line 15-21 take $c_1$ operations and line 24 takes $c_2$ operations.

Then we would have a total of 

$\begin{align}
\text{Operations} &= \sum_{i=1}^n \left ( c_1 +  \sum_{j=1}^{i-1} c_2 \right )\\
&= \sum_{i=1}^n c_1 + \sum_{i=1}^n \sum_{j=1}^{i-1} c_2\\
&= n \cdot c_1 + c_2 \cdot \left (\sum_{i=1}^n \sum_{j=1}^{i-1} 1 \right )\\
&= n \cdot c_1 + c_2 \cdot \left (\sum_{i=1}^n (i-1) \right )\\
&= n \cdot c_1 + c_2 \cdot \left ((\sum_{i=1}^n i) - (\sum_{i=1}^n 1) \right )\\
&= n \cdot c_1 + c_2 \cdot \left (\frac{n^2+n}{2} - n \right )\\
&= n \cdot c_1 + (n^2-n) \cdot \frac{c_2}{2}\\
\end{align}$

So the algorithms time complexity is in $\Theta(n^2) \subsetneq \mathcal{O}(n^2)$.

<h2>Space complexity</h2>
Please note that I take advantage of Pythons dynamic typing system. I think it's difficult to see space complexity in python programs. But when you make the same in C++, you will see that you will need space in $\mathcal{O}(n)$ when you do the conversion. Without the conversion, you're in $\mathcal{O}(1)$.

I guess you might want to leave this choice to the user of your functions. When he wants better results, he should give the input as Fraction. When he wants to get results rather faster, he should give the input as float.

<h2>Notes</h2>
In this algorithm, we don't need anything below the diagonal.
