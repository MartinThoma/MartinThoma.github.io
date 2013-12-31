---
layout: post
title: Jordansche Normalform: 5&#215;5 Matrizen
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


Gegeben sei die Matrix [latex]A \in \mathbb{R}^{5 \times 5}[/latex]:
[latex]A := \begin{pmatrix}
-3 & -1 & -2 & -2 & -1\\
3  & -2 &  2 &  1 &  2\\
0  &  1 & -1 &  1 &  0\\
-1 & -1 & -2 & -4 & -1\\
 2 &  1 &  3 &  3 &  0
\end{pmatrix}[/latex].

<strong>1. Charakteristisches Polynom berechnen:</strong>
[latex]p_A(\lambda) = -(\lambda+2)^5[/latex].

Daraus folgt: [latex]\lambda = -2[/latex] ist einziger Eigenwert mit der algebraischen Vielfachheit 5
Daraus folgt: Es gibt genau einen Jordan-Block in der Jordannormalform.

<strong>2. Anzahl der Jordankästchen bestimmen</strong>:
[latex]
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
[/latex]

Es gibt also 2 Jordankästchen im Jordanblock zu [latex]\lambda = -2[/latex]. Das bedeutet, entweder ist ein Kästchen [latex]4 \times 4[/latex] und das andere [latex]1 \times 1[/latex], oder eines ist [latex]3 \times 3[/latex] und das andere [latex]2 \times 2[/latex].

Als Jordansche Normalform kommen also nur diese beiden Matrizen in Frage:

[latex]J_1 =
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  1 &  0\\
 0 &  0 &  0 & -2 &  0\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix}[/latex]

[latex]J_2 =
\begin{pmatrix}
-2 &  1 & 0  &  0 &  0\\
 0 & -2 & 1  &  0 &  0\\
 0 &  0 & -2 &  0 &  0\\
 0 &  0 &  0 & -2 &  1\\
 0 &  0 &  0 &  0 & -2
\end{pmatrix}[/latex]

Ähnliche Matrizen haben den gleichen Rang. Also müsste die Jordan Normalform der Matrix A den gleichen Rang haben, wie die Matrix A. Leider ist dieses Kriterium hier nicht hilfreich:

[latex]
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
\end{align}[/latex]

Testen wir [latex]J_2[/latex]:
[latex]
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
\end{align}[/latex]

Bei Ähnlichen Matrizen muss die Determinante gleich sein.

[latex]
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
\end{align}[/latex]

Auch dieses Kriterium ist also nicht hilfreich.