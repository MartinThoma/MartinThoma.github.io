---
layout: post
title: When is matrix multiplication commutative?
author: Martin Thoma
date: 2012-07-14 10:49:48.000000000 +02:00
category: Mathematics
tags: mathematics, Linear algebra
featured_image: 2012/01/vector-space.png
---
Matrix multiplication in general is not commutative. Here is an example:

$A, B \in R^{2 \times 2}$
$A := \begin{pmatrix} 
 1 & 2 \\
 3 & 4
\end{pmatrix}$
$B := \begin{pmatrix} 
 5 & 6 \\
 7 & 8
\end{pmatrix}$

$A \cdot B = \begin{pmatrix} 
 19 & 22 \\
 43 & 50
\end{pmatrix} \neq 
\begin{pmatrix} 
 23 & 34 \\
 31 & 46
\end{pmatrix} = B \cdot A$

<h2>When is 2x2 matrix multiplication commutative?</h2>
$\begin{pmatrix} 
 a & b \\
 c & d
\end{pmatrix} \cdot 
\begin{pmatrix} 
 e & f \\
 g & h
\end{pmatrix} = 
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh
\end{pmatrix}$

$\begin{pmatrix} 
 e & f \\
 g & h
\end{pmatrix} \cdot
\begin{pmatrix} 
 a & b \\
 c & d
\end{pmatrix} = 
\begin{pmatrix}
ae + cf & be + df \\
ag + ch & bg + dh
\end{pmatrix}$

So you get four equations:
$\begin{eqnarray*}
I)   & ae + bg &= ae + cf &\Leftrightarrow bg = cf \\
II)  & af + bh &= be + df\\
III) & ce + dg &= ag + ch\\
IV)  & cf + dh &= bg + dh &\Leftrightarrow cf = bg
\end{eqnarray*}$

You might note that (I) is the same as (IV). So you have those equations:
$\begin{eqnarray*}
I)   & bg = cf \\
II)  & af + bh &= be + df & \Leftrightarrow f (a - d) = b (e - h)\\
III) & ce + dg &= ag + ch & \Leftrightarrow g (a - d) = c (e - h)
\end{eqnarray*}$

<h3>Case #1: a != d and e != h</h3>
$\begin{eqnarray*}
I)   & bg          &= cf \\
II)  & \frac{f}{g} &= \frac{b}{c} \Leftrightarrow cf = bg
\end{eqnarray*}$

Now (I) and (II) are essentially the same. So we only demand that $ bg = cf$ and $a \neq d$ and $e \neq h$ for commutative matrix multiplication of $2 \times 2$ matrices.

<h3>Case #2.1: a == d</h3>
$\begin{eqnarray*}
I)   & bg &= cf \\
II)  & 0  &= b (e - h)\\
III) & 0  &= c (e - h)
\end{eqnarray*}$

So you end up with:
($e = h$ and $bg = cf$) or ($b = c = 0$)

<h3>Case #2.2: e == h</h3>
$\begin{eqnarray*}
I)   & bg &= cf \\
II)  & f (a - d) &= 0\\
III) & g (a - d) &= 0
\end{eqnarray*}$

So you end up with:
($a = d$ and $bg = cf$) or ($f = g = 0$)

<h2>Special Cases</h2>
Matrix multiplication is always commutative if ...
<ul>
  <li>... one matrix is the <a href="http://en.wikipedia.org/wiki/Identity_matrix">Identity matrix</a>.</li>
  <li>... one matrix is the <a href="http://en.wikipedia.org/wiki/Zero_matrix">Zero matrix</a>.</li>
  <li>... both matrices are <a href="http://en.wikipedia.org/wiki/Rotation_matrix">rotation matrices</a>. (basically case #2)</li>
  <li>... both matrices are <a href="http://en.wikipedia.org/wiki/Diagonal_matrix">Diagonal matrices</a>.</li>
</ul>

<h2>Simultaneous diagonalization</h2>
Two matrices $A, B \in R^{n \times n}$ are called simultaneous diagonalizable $: \Leftrightarrow$ one matrix $S \in R^{n \times n}$ exists, such that $D_A = S^{-1} \cdot A \cdot S$ and $D_B = S^{-1} \cdot B \cdot S$ with $D_A$ and $D_B$ are diagonal matrices.

<strong>Statement</strong>: $A, B \in \mathbb{R}^{n \times n}$ are simultaneous diagonalizable $\Rightarrow A \cdot B = B \cdot A$
<strong>Proof</strong>:
As A and B are simultaneous diagonalizable, a matrix $T \in \mathbb{R}^{n \times n}$ exists, such that $D_A = S^{-1} \cdot A \cdot S$ and $D_B = S^{-1} \cdot B \cdot S$ with $D_A$ and $D_B$ are diagonal matrices.

$
\begin{align}
\Rightarrow A \cdot B &= S \cdot D_A S^{-1} \cdot  S \cdot D_B \cdot S^{-1} \\
&= S \cdot D_A \cdot D_B \cdot S^{-1} \\
&= S \cdot D_B \cdot D_A \cdot S^{-1} \\
&= S \cdot D_B \cdot S^{-1} \cdot  S \cdot D_A \cdot S^{-1} \\
&= B \cdot A \blacksquare
\end{align} 
$

<strong>Statement</strong>: $A \cdot B = B \cdot A \nRightarrow A, B \in \mathbb{R}^{n \times n}$ are simultaneous diagonalizable.
<strong>Proof</strong>: by Counter-Example
$\begin{pmatrix}0 & 1 \\
0 & 0\end{pmatrix} \cdot
\begin{pmatrix}1 & 0 \\
0 & 1\end{pmatrix} = 
\begin{pmatrix}1 & 0 \\
0 & 1\end{pmatrix} \cdot 
\begin{pmatrix}0 & 1 \\
0 & 0\end{pmatrix}$, but
$\begin{pmatrix}0 & 1 \\
0 & 0\end{pmatrix}$ is not diagonalizable. $\blacksquare$

<h2>See also</h2>
<ul>
  <li><a href="http://math.stackexchange.com/q/170241/6876">When is matrix multiplication commutative?</a> on math.stackexchange.com</li>
</ul>
