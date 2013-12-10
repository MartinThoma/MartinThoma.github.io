---
layout: post
status: publish
published: true
title: Solving linear equations with Gaussian elimination
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 67901
wordpress_url: http://martin-thoma.com/?p=67901
date: 2013-05-26 00:01:30.000000000 +02:00
categories:
- Code
tags:
- mathematics
- Linear algebra
- CPP
comments: []
featured_image: 2013/05/upper-triangular-matrix.png
---
<div class="info">Please note that you should use LU-decomposition to solve linear equations. The following code produces valid solutions, but when your vector $b$ changes you have to do all the work again. LU-decomposition is faster in those cases and not slower in case you don't have to solve equations with the same matrix twice.</div>

Suppose you have a system of $n \in \mathbb{N_{\geq 1}}$ linear equations and variables $x_1, x_2, \dots, x_n \in \mathbb{R}$:

$
\begin{align}
a_{1,1} \cdot x_1 + a_{1,2} x_2 + \dots + a_{1,n} \cdot x_{n} &= b_1\\
a_{2,1} \cdot x_1 + a_{2,2} x_2 + \dots + a_{2,n} \cdot x_{n} &= b_2\\
\vdots &= \vdots\\
a_{n,1} \cdot x_1 + a_{n,2} x_2 + \dots + a_{n,n} \cdot x_{n} &= b_n
\end{align}
$



All factors $a_{i,j} \in \mathbb{R}$ for $i,j \in 1, \dots, n$ can be written in one matrix $A \in \mathbb{R}^{n \times n}$ and all $b_i$ can be written as a vector $b$. You combine all $x_i$ in the same way to a vector $x$.

So you can write the system of equations as:

$A \cdot x = b$

<h2>How Gaussian elimination works</h2>
First, you write $A$ and $b$ in an augmented matrix $A|b$:

$
  \left(\begin{array}{cccc|c}
    a_{1,1} & a_{1,2} & \dots  & a_{1,n} & b_1\\
    a_{2,1} & a_{2,2} & \dots  & a_{2,n} & b_2\\
    \vdots  & \vdots  & \ddots  & \vdots  & \vdots \\
    a_{n,1} & a_{n,2} & \dots & a_{n,n}  & b_n
  \end{array}\right).
$

On this matrix you may make exactly three operations:

<ul>
  <li>Swap rows</li>
  <li>Add one row onto another</li>
  <li>Multiply every factor of one row with a constant</li>
</ul>


You want to get a triangular matrix. So you subsequently eliminate one variable from the system of equations until you have a matrix like this:

$
  \left(\begin{array}{ccccc|c}
    a_{1,1} & a_{1,2} & a_{1,3} & \dots & a_{1,n} & b_1\\
          0 & a_{2,2} & a_{2,3} & \dots & a_{2,n} & b_2\\
          0 &       0 & a_{3,3} & \dots & a_{3,n} & b_3\\
    \vdots  & \vdots  & \ddots  & \ddots& \vdots  & \vdots\\
          0 &       0 &  \dots  &     0 & a_{3,n} & b_n\\
  \end{array}\right).
$

It's actually quite simple to get this form:

{% caption align="aligncenter" width="500" caption="Pseudocode for Gaussian elimination" url="../images/2013/05/Gaussian-elimination.png" alt="Pseudocode for Gaussian elimination" title="" height="772" class="size-full wp-image-68071" %}

<h2>C++ Code</h2>
{% highlight cpp %}
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

void print(vector< vector<double> > A) {
    int n = A.size();
    for (int i=0; i<n; i++) {
        for (int j=0; j<n+1; j++) {
            cout << A[i][j] << "\t";
            if (j == n-1) {
                cout << "| ";
            } 
        }
        cout << "\n";
    }
    cout << endl;
}

vector<double> gauss(vector< vector<double> > A) {
    int n = A.size();

    for (int i=0; i<n; i++) {
        // Search for maximum in this column
        double maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k=i; k<n+1;k++) {
            double tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k=i+1; k<n; k++) {
            double c = -A[k][i]/A[i][i];
            for (int j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    vector<double> x(n);
    for (int i=n-1; i>=0; i--) {
        x[i] = A[i][n]/A[i][i];
        for (int k=i-1;k>=0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}

int main() {
    int n;
    cin >> n;

    vector<double> line(n+1,0);
    vector< vector<double> > A(n,line);

    // Read input data
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> A[i][j];
        }
    }

    for (int i=0; i<n; i++) {
        cin >> A[i][n];
    }

    // Print input
    print(A);

    // Calculate solution
    vector<double> x(n);
    x = gauss(A);

    // Print result
    cout << "Result:\t";
    for (int i=0; i<n; i++) {
        cout << x[i] << " ";
    }
    cout << endl;
}
{% endhighlight %}

You can call it like this:
{% highlight bash %}
./gauss.out < 3x3.in
1	2	3	| 1	
4	5	6	| 1	
1	0	1	| 1	

Result:	0 -1 1 
{% endhighlight %}

<h2>Python code</h2>
{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line +=  "| "
        print(line)
    print("")
 
def gauss(A):
    n = len(A)
 
    for i in range(0,n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1,n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k
 
        # Swap maximum row with current row (column by column)
        for k in range(i,n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
 
        # Make all rows below this one 0 in current column
        for k in range(i+1,n):
            c = -A[k][i]/A[i][i]
            for j in range(i,n+1):
                if i==j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
 
    # Solve equation Ax=b for an upper triangular matrix A
    x=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1,-1,-1):
            A[k][n] -= A[k][i] * x[i]
    return x
 
if __name__ == "__main__":
    from fractions import Fraction
    n = input()
 
    A = [[0 for j in range(n+1)] for i in range(n)]
 
    # Read input data
    for i in range(0,n):
        line = map(Fraction, raw_input().split(" "))
        for j, el in enumerate(line):
            A[i][j] = el
    raw_input()
 
    line = raw_input().split(" ")
    lastLine = map(Fraction, line)
    for i in range(0,n):
        A[i][n] = lastLine[i]
 
    # Print input
    pprint(A)
 
    # Calculate solution
    x = gauss(A)
 
    # Print result
    line = "Result:\t"
    for i in range(0,n):
       line += str(x[i]) + "\t"
    print(line)
{% endhighlight %}

<h2>JavaScript code</h2>
{% highlight javascript %}
/** Solve a linear system of equations given by a n&times;n matrix 
    with a result vector n&times;1. */
function gauss(A) {
    var n = A.length;

    for (var i=0; i<n; i++) {
        // Search for maximum in this column
        var maxEl = Math.abs(A[i][i]);
        var maxRow = i;
        for(var k=i+1; k<n; k++) {
            if (Math.abs(A[k][i]) > maxEl) {
                maxEl = Math.abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (var k=i; k<n+1; k++) {
            var tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (k=i+1; k<n; k++) {
            var c = -A[k][i]/A[i][i];
            for(var j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    var x= new Array(n);
    for (var i=n-1; i>-1; i--) {
        x[i] = A[i][n]/A[i][i];
        for (var k=i-1; k>-1; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}
{% endhighlight %}

<h2>Complexity</h2>
<h3>Time complexity</h3>
Time complexity is in $\mathcal{O}(n^3)$ (lines 44 - 53):
$
\begin{align}
Operations &= \sum_{i=0}^{n-1} \sum_{k=i+1}^{n-1} \sum_{j=i}^{n} 1\\
&= \sum_{i=0}^{n-1} \sum_{k=i+1}^{n-1} (n-i+1) \\
&= \left (\sum_{i=0}^{n-1} \sum_{k=i+1}^{n-1} (n+1) \right ) - \left (\sum_{i=0}^{n-1} \sum_{k=i+1}^{n-1} i \right )\\
&= \dots \\
&= \frac{1}{6} \cdot n \cdot (2 n^2+3 n-5)\\
&= \frac{1}{3} \cdot n^3 + \mathcal{O}(n^2)
\end{align}$

<h3>Space complexity</h3>
Space complexity of this implementation is in $\mathcal{O}(n)$, but you can easily come down to $\mathcal{O}(1)$ when you use <code>A[n]</code> for storing <code>x</code>.
