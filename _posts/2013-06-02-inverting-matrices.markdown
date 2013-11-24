---
layout: post
status: publish
published: true
title: Inverting matrices
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 69101
wordpress_url: http://martin-thoma.com/?p=69101
date: 2013-06-02 14:01:57.000000000 +02:00
categories:
- Code
tags:
- mathematics
- Matrix
comments: []
---
Suppose you have a matrix $A \in \mathbb{R}^{n \times n}$ and you want to invert it. I've already explained <a href="http://martin-thoma.com/wie-bestimme-ich-das-inverse-einer-matrix/">how to invert a matrix</a> (<a href="http://www.purplemath.com/modules/mtrxinvr.htm">English explanation</a>), but I didn't provide any code and / or runtime analysis.

<h2>C++ Code</h2>
{% highlight cpp %}
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

void print(vector< vector<double> > A) {
    int n = A.size();
    for (int i=0; i<n; i++) {
        for (int j=0; j<2*n; j++) {
            cout << A[i][j] << "\t";
            if (j == n-1) {
                cout << "| ";
            } 
        }
        cout << "\n";
    }
    cout << endl;
}

void calculateInverse(vector< vector<double> >&amp; A) {
    int n = A.size();

    for (int i=0; i<n; i++) {
        // Search for maximum in this column
        double maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = A[k][i];
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k=i; k<2*n;k++) {
            double tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k=i+1; k<n; k++) {
            double c = -A[k][i]/A[i][i];
            for (int j=i; j<2*n; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    for (int i=n-1; i>=0; i--) {
        for (int k=n; k<2*n;k++) {
            A[i][k] /= A[i][i];
        }
        // this is not necessary, but the output looks nicer:
        A[i][i] = 1; 

        for (int rowModify=i-1;rowModify>=0; rowModify--) {
            for (int columModify=n;columModify<2*n;columModify++) {
                A[rowModify][columModify] -= A[i][columModify] 
                                             * A[rowModify][i];
            }
            // this is not necessary, but the output looks nicer:
            A[rowModify][i] = 0;
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<double> line(2*n,0);
    vector< vector<double> > A(n,line);

    // Read input data
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> A[i][j];
        }
    }

    for (int i=0; i<n; i++) {
        A[i][n+i] = 1;
    }

    // Print input
    print(A);

    // Calculate solution
    calculateInverse(A);

    // Print result
    cout << "Result:" << endl;
    print(A);
}
{% endhighlight %}

This code is VERY similar to the code of <a href="http://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/" title="Solving linear equations with Gaussian elimination">Gaussian elimination</a>. In fact, I've only changed all occurrences of <code>n+1</code> to <code>2*n</code>. I also had to change lines 57-70, as we need to do all operations now on a matrix instead of a vector.

<h3>Time complexity</h3>
Lines 43-52:

$\displaystyle Operations = \sum_{i=0}^{n-1} \left (\sum_{k=i+1}^{n-1} (\sum_{j=i}^{2n} 1) \right ) = \frac{5}{6} n^3 - \frac{5}{6} n$ (see <a href="http://www.wolframalpha.com/input/?i=sum_%7Bi%3D0%7D%5E%7Bn-1%7D+(sum_%7Bk%3Di%2B1%7D%5E%7Bn-1%7D+(sum_%7Bj%3Di%7D%5E%7B2n%7D+1))">Wolfram|Alpha</a>)

Lines 63-70:

$\displaystyle Operations = \sum_{i=0}^{n-1} \left (\sum_{k=0}^{i-1} (\sum_{j=n}^{2n} 1) \right ) = \frac{1}{2} n^3 - \frac{1}{2} n$ (see <a href="http://www.wolframalpha.com/input/?i=sum_%7Bi%3D0%7D%5E%7Bn-1%7D+%28sum_%7Bk%3D0%7D%5E%7Bi-1%7D+%28sum_%7Bj%3Dn%7D%5E%7B2n%7D+1%29%29"))">Wolfram|Alpha</a>)

So we need about $\frac{4}{3} n^3 + \mathcal{O}(n^2)$ operations to invert a matrix with Gau&szlig;-Elimination. 

<h3>Space complexity</h3>
My algorithm needs space for the inverse matrix, so it is in $\mathcal{O}(n^2)$.

<h2>Inverting an upper triangular matrix</h2>
Suppose you have an upper triangular matrix $A \in \mathbb{R^{n \times n}}$ that you would like to invert. It could look like this:

$\begin{pmatrix}
2 & 7 & 1 & 8 & 2\\
0 & 8 & 1 & 8 & 2\\
0 & 0 & 8 & 4 & 5\\
0 & 0 & 0 & 9 & 0\\
0 & 0 & 0 & 0 & 4
\end{pmatrix}$

How could we improve the algorithm from above to get speed it up?

Well, we don't need lines 24-53 any more, as those lines bring $A$ to an upper triangular form. But we still need lines 63-70. So we can improve the algorithm to a complexity of $\frac{1}{2} n^3 + \mathcal{O}(n^2)$.

<h2>See also</h2>
<a href="http://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra">Computational complexity of mathematical operations</a>
