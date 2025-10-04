---
layout: post
title: When Is Matrix Multiplication Commutative?
slug: when-is-matrix-multiplication-commutative
lang: en
author: Martin Thoma
date: 2012-07-14 10:49:48.000000000 +02:00
category: Mathematics
tags: mathematics, Linear algebra
featured_image: 2012/01/vector-space.png
---
Matrix multiplication in general is not commutative. Here is an example:

Let $A, B \in \mathbb{R}^{2 \times 2}$:

$$A := \begin{pmatrix}
 1 & 2 \\
 3 & 4
\end{pmatrix}, \quad B := \begin{pmatrix}
 5 & 6 \\
 7 & 8
\end{pmatrix}$$

Then:

$$A \cdot B = \begin{pmatrix}
 19 & 22 \\
 43 & 50
\end{pmatrix} \neq
\begin{pmatrix}
 23 & 34 \\
 31 & 46
\end{pmatrix} = B \cdot A$$

## When Is 2×2 Matrix Multiplication Commutative?
$$\begin{pmatrix}
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
\end{pmatrix}$$

$$\begin{pmatrix}
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
\end{pmatrix}$$

So you get four equations:

$$\begin{align}
I) \quad   & ae + bg &= ae + cf &\Leftrightarrow bg &= cf \\
II) \quad  & af + bh &= be + df \\
III) \quad & ce + dg &= ag + ch \\
IV) \quad  & cf + dh &= bg + dh &\Leftrightarrow cf = bg
\end{align}$$

You might note that (I) is the same as (IV). So you have these equations:

$$\begin{align}
I) \quad   & bg &= cf \\
II) \quad  & af + bh &= be + df & \Leftrightarrow f (a - d) = b (e - h) \\
III) \quad & ce + dg &= ag + ch & \Leftrightarrow g (a - d) = c (e - h)
\end{align}$$

### Case #1: a ≠ d and e ≠ h

$$\begin{align}
I) \quad   & bg          &= cf \\
II) \quad  & \frac{f}{g} &= \frac{b}{c} \Leftrightarrow cf = bg
\end{align}$$

Now (I) and (II) are essentially the same. So we only demand that $bg = cf$ and $a \neq d$ and $e \neq h$ for commutative matrix multiplication of $2 \times 2$ matrices.

### Case #2.1: a = d

$$\begin{align}
I) \quad   & bg &= cf \\
II) \quad  & 0  &= b (e - h) \\
III) \quad & 0  &= c (e - h)
\end{align}$$

So you end up with: $(e = h \text{ and } bg = cf)$ or $(b = c = 0)$

### Case #2.2: e = h

$$\begin{align}
I) \quad   & bg &= cf \\
II) \quad  & f (a - d) &= 0 \\
III) \quad & g (a - d) &= 0
\end{align}$$

So you end up with: $(a = d \text{ and } bg = cf)$ or $(f = g = 0)$

## Special Cases

Matrix multiplication is always commutative if:

- One matrix is the [Identity matrix](http://en.wikipedia.org/wiki/Identity_matrix)
- One matrix is the [Zero matrix](http://en.wikipedia.org/wiki/Zero_matrix)
- Both matrices are $2 \times 2$ [rotation matrices](http://en.wikipedia.org/wiki/Rotation_matrix) (basically case #2)
- Both matrices are [Diagonal matrices](http://en.wikipedia.org/wiki/Diagonal_matrix)

## Simultaneous Diagonalization

Two matrices $A, B \in \mathbb{R}^{n \times n}$ are called **simultaneously diagonalizable** if and only if one matrix $S \in \mathbb{R}^{n \times n}$ exists, such that $D_A = S^{-1} \cdot A \cdot S$ and $D_B = S^{-1} \cdot B \cdot S$ where $D_A$ and $D_B$ are diagonal matrices.

**Theorem**: If $A, B \in \mathbb{R}^{n \times n}$ are simultaneously diagonalizable, then $A \cdot B = B \cdot A$.

**Proof**:
Since A and B are simultaneously diagonalizable, a matrix $S \in \mathbb{R}^{n \times n}$ exists such that $D_A = S^{-1} \cdot A \cdot S$ and $D_B = S^{-1} \cdot B \cdot S$ where $D_A$ and $D_B$ are diagonal matrices.

$$\begin{align}
\Rightarrow A \cdot B &= S \cdot D_A \cdot S^{-1} \cdot  S \cdot D_B \cdot S^{-1} \\
&= S \cdot D_A \cdot D_B \cdot S^{-1} \\
&= S \cdot D_B \cdot D_A \cdot S^{-1} \\
&= S \cdot D_B \cdot S^{-1} \cdot  S \cdot D_A \cdot S^{-1} \\
&= B \cdot A \quad \blacksquare
\end{align}$$

**Note**: The converse is not true: $A \cdot B = B \cdot A \nRightarrow A, B$ are simultaneously diagonalizable.

**Proof by counterexample**:
$$\begin{pmatrix}0 & 1 \\
0 & 0\end{pmatrix} \cdot
\begin{pmatrix}1 & 0 \\
0 & 1\end{pmatrix} =
\begin{pmatrix}1 & 0 \\
0 & 1\end{pmatrix} \cdot
\begin{pmatrix}0 & 1 \\
0 & 0\end{pmatrix}$$

but $\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}$ is not diagonalizable. $\blacksquare$

## See Also

- [When is matrix multiplication commutative?](http://math.stackexchange.com/q/170241/6876) on math.stackexchange.com
