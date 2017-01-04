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

Suppose you have a matrix $A \in \mathbb{R}^n$ and you want to find two matrices $L, U \in \mathbb{R}^n$, such that $A = L \cdot U$ and $L$ is a lower triangular matrix and $R$ is an upper triangular matrix.

<h2>Does a LU decomposition always exist?</h2>
Is this always possible to find such matrices $L, U \in \mathbb{R}^n$?

No. Lets say $n=2$:

$
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
$

$
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
= \begin{pmatrix}
l_{1,1} \cdot r_{1,1} & l_{1,1} \cdot r_{1,2} \\
l_{2,1} \cdot r_{1,1} & l_{2,1} \cdot r_{1,2} + l_{2,2} \cdot r_{2,2} \\
\end{pmatrix}
$

This means $l_{1,1}$ or $r_{1,1}$ has to be 0:

Case 1: Assume $l_{1,1} = 0$:

$
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
$

So $l_{1,1} \neq 0$

Case 2: Assume $r_{1,1} = 0$:

$
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
$

So $r_{1,1} \neq 0$

This means, for the given matrix does no $LU$ decomposition exist like I've defined it above.

But if you allow swapping of rows like it is done in Gaussian elimination, you can get a LU-decomposition of every non-singular matrix.

Swapping is a permutation of rows in the matrix. You can do this by multiplying $A$ with a permutation matrix $P$.

<h2>Permutation matrices</h2>
A permutation matrix $P \in \mathbb{R}^{n \times n}$ is a non-singular matrix with $p_{i,j} \in \{0,1\}$. So you have exactly one 1 in every row and exactly one 1 in every column.

Suppose you have a matrix $A \in \mathbb{R}^{n \times n}$ and $p_{a, \bar a} = 1 \forall a \in 1, \dots, n$. Now you multiply $C := P \cdot A$.

What does that mean?

$\forall i,j \in 1, \dots, n: c_{i,j} = \sum_{k=1}^n p_{i,k} \cdot a_{k,j} = 1 \cdot a_{\bar i, j} = a_{\bar i, j}$

So you can interpret $P$ like this:
<ul>
  <li>When for row $i$ the one is in column $\bar i$, then row $\bar i$ will move to line $i$.</li>
  <li>When you want to move row $\bar i$ to row $i$, you have to write a one in column $\bar i$, row $i$ a one.</li>
  <li>$P[b][a] = 1 \Leftrightarrow $ a line is moved from row a to row b</li>
</ul>

Example:

$
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
\end{pmatrix}$

As we are interested in efficient implementations, we don't need to store all those zeros for $P$. We only store an one dimensional array of size $n$. The index of this array indicates where a line will go to, the value means where it comes from.

<h2>LUP decomposition</h2>
A $LUP$ decomposition, with:
<ul>
    <li>$L \in \mathbb{R}^n$ is an unipotent lower triangular matrix, </li>
    <li>$U \in \mathbb{R}^n$ is an upper triangular matrix and </li>
    <li>$P \in \mathbb{R}^n$ is a permutation matrix.</li>
    <li>$L\cdot U = P \cdot A$</li>
</ul>

does always exist for a non-singular square matrices $A \in \mathbb{R}^{n \times n}$. 

<h3>Finding P</h3>
For some reasons I don't understand (yet) it is better when entries with big absolute values are on the top. This is called pivoting.

