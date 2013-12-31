---
layout: post
title: "Jordansche Normalform: 5x5 Matrizen"
author: Martin Thoma
date: 2012-08-17 12:25:51
categories: 
- German posts
tags: 
- Linear algebra
- mathematics
featured_image: 2012/08/jordan-normal-form-block1.png
---
Ein Beispiel von <a href="http://www.matheraum.de/read?t=164350&v=t">matheraum.de</a>
<a href="http://www.wolframalpha.com/input/?i=%7B%7B5%2C-1%2C-3%2C2%2C-5%7D%2C%7B0%2C2%2C0%2C0%2C0%7D%2C%7B1%2C0%2C1%2C1%2C-2%7D%2C%7B0%2C-1%2C0%2C3%2C1%7D%2C%7B1%2C-1%2C-1%2C1%2C1%7D%7D">Wolfram|Alpha</a>


Gegeben sei die Matrix $A \in \mathbb{R}^{5 \times 5}$:
$A := \begin{pmatrix}
-3 & -1 & -2 & -2 & -1\\
3  & -2 &  2 &  1 &  2\\
0  &  1 & -1 &  1 &  0\\
-1 & -1 & -2 & -4 & -1\\
 2 &  1 &  3 &  3 &  0
\end{pmatrix}$.

<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_A(\lambda) = -(\lambda+2)^5$.

Daraus folgt: $\lambda = -2$ ist einziger Eigenwert mit der algebraischen Vielfachheit 5
Daraus folgt: Es gibt genau einen Jordan-Block in der Jordannormalform.

<strong>2. Anzahl der Jordankästchen bestimmen</strong>:
$
\begin{align}
\dim E_{-2} &= \dim \text{Kern}(A +2 \cdot I) \\
&= \dim \text{Kern} \begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
3  &  0 &  2 &  1 &  2\\
0  &  1 &  1 &  1 &  0\\
-1 & -1 & -2 & -2 & -1\\
 2 &  1 &  3 &  3 &  2
\end{pmatrix}\\
&=
\dim \text{Kern} \begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
 0 & -3 & -4 & -5 & -1\\
 0 &  1 &  1 &  1 &  0\\
 0 &  0 &  0 &  0 &  0\\
 0 & -1 & -1 & -1 &  0
\end{pmatrix} \\
&=
\dim \text{Kern} \begin{pmatrix}
 1 &  1 &  2 &  2 &  1\\
 0 &  1 &  1 &  1 &  0\\
 0 &  0 & -1 & -2 & -1\\
 0 &  0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 &  0
\end{pmatrix} \\
&=
\dim \text{Kern} \begin{pmatrix}
 1 &  0 &  0 & -1 &  0\\
 0 &  1 &  0 & -1 & -1\\
 0 &  0 &  1 &  2 &  1\\
 0 &  0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 &  0
\end{pmatrix} \\
&= 2
\end{align}
$

Es gibt also 2 Jordankästchen im Jordanblock zu $\lambda = -2$. Das bedeutet, entweder ist ein Kästchen $4 \times 4$ und das andere $1 \times 1$, oder eines ist $3 \times 3$ und das andere $2 \times 2$.

Als Jordansche Normalform kommen also nur diese beiden Matrizen in Frage:

$J_1 =
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  1 &  0\\
 0 &  0 &  0 & -2 &  0\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix}$

$J_2 =
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  0 &  0\\
 0 &  0 &  0 & -2 &  1\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix}$

Ähnliche Matrizen haben den gleichen Rang. Also müsste die Jordan Normalform der Matrix A den gleichen Rang haben, wie die Matrix A. Leider ist dieses Kriterium hier nicht hilfreich:

$
\begin{align}
\text{Rang } J_1 
&= \text{Rang }
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  1 &  0\\
 0 &  0 &  0 & -2 &  0\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix} \\
&= \text{Rang }
\begin{pmatrix}
 1 & -0.5 & 0  &  0 &  0\\
 0 &  1 & -0.5  &  0 &  0\\
 0 &  0 &  1 &  -0.5 &  0\\
 0 &  0 &  0 &  1 &  0\\
 0 &  0 &  0 &  0 & 1
\end{pmatrix} \\
&= \text{Rang }
\begin{pmatrix}
 1 &  0 &  0 &  0 & 0\\
 0 &  1 &  0 &  0 & 0\\
 0 &  0 &  1 &  0 & 0\\
 0 &  0 &  0 &  1 & 0\\
 0 &  0 &  0 &  0 & 1
\end{pmatrix} \\
&= 5
\end{align}$

Testen wir $J_2$:
$
\begin{align}
\text{Rang } J_2 
&= \text{Rang }
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  0 &  0\\
 0 &  0 &  0 & -2 &  1\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix} \\
&= \text{Rang }
\begin{pmatrix}
 1 & -0.5 & 0  &  0 &  0\\
 0 &  1 & -0.5  &  0 &  0\\
 0 &  0 &  1 &  0 &  0\\
 0 &  0 &  0 &  1 &  -0.5\\
 0 &  0 &  0 &  0 & 1
\end{pmatrix} \\
&= \text{Rang }
\begin{pmatrix}
 1 &  0 &  0 &  0 & 0\\
 0 &  1 &  0 &  0 & 0\\
 0 &  0 &  1 &  0 & 0\\
 0 &  0 &  0 &  1 & 0\\
 0 &  0 &  0 &  0 & 1
\end{pmatrix} \\
&= 5
\end{align}$

Bei Ähnlichen Matrizen muss die Determinante gleich sein.

$
\begin{align}
\det J_1 
&= \det
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  1 &  0\\
 0 &  0 &  0 & -2 &  0\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix} \\
&= \det (-2)^5
\begin{pmatrix}
 1 &  0 & 0  &  0 &  0\\
 0 &  1 &  0  &  0 &  0\\
 0 &  0 &  1 &  0 &  0\\
 0 &  0 &  0 &  1 &  0\\
 0 &  0 &  0 &  0 & 1
\end{pmatrix} \\
&= -32 = \det J_2
\end{align}$

Auch dieses Kriterium ist also nicht hilfreich.
