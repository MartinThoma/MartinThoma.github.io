---
layout: post
title: LU decomposition of a matrix
author: Martin Thoma
date: 2013-05-20 03:18:30
categories: 
- Code
tags: 
- mathematics
- Matrix
- numerics
featured_image: 2013/05/upper-triangular-matrix.png
---
<div class="info">You have to know how <a href="http://en.wikipedia.org/wiki/Gaussian_elimination">Gaussian elimination</a> works to understand this article.</div>

Suppose you have a matrix [latex]A \in \mathbb{R}^n[/latex] and you want to find two matrices [latex]L, U \in \mathbb{R}^n[/latex], such that [latex]A = L \cdot U[/latex] and [latex]L[/latex] is a lower triangular matrix and [latex]R[/latex] is an upper triangular matrix.

<h2>Does a LU decomposition always exist?</h2>
Is this always possible to find such matrices [latex]L, U \in \mathbb{R}^n[/latex]?

No. Lets say [latex]n=2[/latex]:

[latex]
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
l_{1,1} & 0 \\
l_{2,1} & l_{2,2} \\
\end{pmatrix} \cdot
\begin{pmatrix}
r_{1,1} & r_{1,2} \\
0 & r_{2,2} \\
\end{pmatrix}
[/latex]

[latex]
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
l_{1,1} \cdot r_{1,1} & l_{1,1} \cdot r_{1,2} \\
l_{2,1} \cdot r_{1,1} & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix}
[/latex]

This means [latex]l_{1,1}[/latex] or [latex]r_{1,1}[/latex] has to be 0:

Case 1: Assume [latex]l_{1,1} = 0[/latex]:

[latex]
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
0 & 0 \cdot r_{1,2} \\
l_{2,1} \cdot r_{1,1} & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix} = 
\begin{pmatrix}
0 & 0 \\
l_{2,1} \cdot r_{1,1} & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix}
[/latex]

So [latex]l_{1,1} \neq 0[/latex]

Case 2: Assume [latex]r_{1,1} = 0[/latex]:

[latex]
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
0 & l_{1,1} \cdot r_{1,2} \\
l_{2,1} \cdot 0 & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix} =
\begin{pmatrix}
0 & l_{1,1} \cdot r_{1,2} \\
0 & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix} 
[/latex]

So [latex]r_{1,1} \neq 0[/latex]

This means, for the given matrix does no [latex]LU[/latex] decomposition exist like I've defined it above.

But if you allow swapping of rows like it is done in Gaussian elimination, you can get a LU-decomposition of every non-singular matrix.

Swapping is a permutation of rows in the matrix. You can do this by multiplying [latex]A[/latex] with a permutation matrix [latex]P[/latex].

<h2>Permutation matrices</h2>
A permutation matrix [latex]P \in \mathbb{R}^{n \times n}[/latex] is a non-singular matrix with [latex]p_{i,j} \in \{0,1\}[/latex]. So you have exactly one 1 in every row and exactly one 1 in every column.

Suppose you have a matrix [latex]A \in \mathbb{R}^{n \times n}[/latex] and [latex]p_{a, \bar a} = 1 \forall a \in 1, \dots, n[/latex]. Now you multiply [latex]C := P \cdot A[/latex].

What does that mean?

[latex]\forall i,j \in 1, \dots, n: c_{i,j} = \sum_{k=1}^n p_{i,k} \cdot a_{k,j} = 1 \cdot a_{\bar i, j} = a_{\bar i, j}[/latex]

So you can interpret [latex]P[/latex] like this:
<ul>
  <li>When for row [latex]i[/latex] the one is in column [latex]\bar i[/latex], then row [latex]\bar i[/latex] will move to line [latex]i[/latex].</li>
  <li>When you want to move row [latex]\bar i[/latex] to row [latex]i[/latex], you have to write a one in column [latex]\bar i[/latex], row [latex]i[/latex] a one.</li>
  <li>[latex]P[b][a] = 1 \Leftrightarrow [/latex] a line is moved from row a to row b</li>
</ul>

Example:

[latex]
\begin{pmatrix}
0 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 1\\
1 & 0 & 0 & 0 & 0\\
0 & 0 & 1 & 0 & 0\\
0 & 0 & 0 & 1 & 0
\end{pmatrix} \cdot
\begin{pmatrix}
1 & 1 & 1 & 1 & 1\\
2 & 2 & 2 & 2 & 2\\
3 & 3 & 3 & 3 & 3\\
4 & 4 & 4 & 4 & 4\\
5 & 5 & 5 & 5 & 5
\end{pmatrix} =
\begin{pmatrix}
2 & 2 & 2 & 2 & 2\\
5 & 5 & 5 & 5 & 5\\
1 & 1 & 1 & 1 & 1\\
3 & 3 & 3 & 3 & 3\\
4 & 4 & 4 & 4 & 4
\end{pmatrix}[/latex]

As we are interested in efficient implementations, we don't need to store all those zeros for [latex]P[/latex]. We only store an one dimensional array of size [latex]n[/latex]. The index of this array indicates where a line will go to, the value means where it comes from.

<h2>LUP decomposition</h2>
A [latex]LUP[/latex] decomposition, with:
<ul>
    <li>[latex]L \in \mathbb{R}^n[/latex] is an unipotent lower triangular matrix, </li>
    <li>[latex]U \in \mathbb{R}^n[/latex] is an upper triangular matrix and </li>
    <li>[latex]P \in \mathbb{R}^n[/latex] is a permutation matrix.</li>
    <li>[latex]L\cdot U = P \cdot A[/latex]</li>
</ul>

does always exist for a non-singular square matrices [latex]A \in \mathbb{R}^{n \times n}[/latex]. 

<h3>Finding P</h3>
For some reasons I don't understand (yet) it is better when entries with big absolute values are on the top. This is called pivoting.

