---
layout: post
title: Wie bestimme ich den Kern einer linearen Abbildung?
author: Martin Thoma
date: 2012-08-16 15:54:15.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra
featured_image: 2012/03/Matrix-Inverses.png
---
<h2>Definition</h2>
Der Kern einer linearen Abbildung ist eine Menge von Vektoren. In diesem Artikel erkl&auml;re ich kurz und b&uuml;ndig, wie man den Kern einer linearen Abbildung bestimmt.

<div class="definition">Sei $\Phi: V \rightarrow W$ eine lineare Abbildung. Der <strong>Kern</strong> von $\Phi$ ist die Menge aller Vektoren von V, die durch $\Phi$ auf den Nullvektor $0 \in W$ abgebildet werden, also:

$\text{Kern } \Phi := \{v \in V | \Phi(v) = 0\}$</div>

<h2>Vorgehen</h2>
Jede lineare Abbildung $\Phi$ l&auml;sst sich in dieser Form beschreiben:

$\Phi: V \rightarrow W$ mit $\dim V = m$ und $\dim W = n$
$\Phi(x) = A \cdot x, ~~~ A \in R^{n \times m}, x \in V$

Also muss man, um den Kern von $\Phi$ zu bestimmen, nur das folgende homogene Gleichungssystem nach x aufl&ouml;sen:
$A \cdot x = 0$

In Wolfram|Alpha ben&ouml;tigt man daf&uuml;r &uuml;brigens das Schl&uuml;sselwort <code>null space</code>. Hier ist <a href="http://www.wolframalpha.com/input/?i=nullspace+%7B%7B-1%2C-1%2C-2%2C-2%2C-1%7D%2C%7B3%2C0%2C2%2C1%2C2%7D%2C%7B0%2C1%2C1%2C1%2C0%7D%2C%7B-1%2C-1%2C-2%2C-2%2C-1%7D%2C%7B2%2C1%2C3%2C3%2C2%7D%7D">Beispiel #2 in Wolfram|Alpha</a>.

<h2>Beispiel #1</h2>
<h3>Aufgabenstellung</h3>
Sei $A \in \mathbb{R}^{3 \times 3}$ und definiert als

$A := \begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix}$

Sei $\Phi: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ eine lineare Abbildung und definiert als

$\Phi(x) := A \cdot x$.

Was ist der Kern von $\Phi$?

<h3>Rechnung</h3>
$
\begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix} 
\leadsto
\begin{pmatrix}
1 &  2 &  3\\
0 & -3 & -6\\
0 & -6 & -12
\end{pmatrix} 
\leadsto
\begin{pmatrix}
1 & 2 & 3\\
0 & 1 & 2\\
0 & 1 & 2
\end{pmatrix} 
\leadsto
\begin{pmatrix}
1 & 0 & -1\\
0 & 1 &  2\\
0 & 0 &  0
\end{pmatrix} 
$

Man sieht direkt, dass die Matrix den Rang 2 hat. Also muss der L&ouml;sungsraum 1-dimensional sein. Mit dem -1-Trick kommt nam auf den L&ouml;sungsraum:

$\mathcal{L} = \left [
\begin{pmatrix}
-1\\
2\\
-1
\end{pmatrix} 
\right ]$

Also:

$\text{Kern } \Phi = \left [
\begin{pmatrix}
-1\\
2\\
-1
\end{pmatrix} 
\right ]$

<h2>Beispiel #2</h2>
<h3>Aufgabenstellung</h3>
Sei $A \in \mathbb{R}^{5 \times 5}$ und definiert als

$A := \begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
3  &  0 &  2 &  1 &  2\\
0  &  1 &  1 &  1 &  0\\
-1 & -1 & -2 & -2 & -1\\
 2 &  1 &  3 &  3 &  2
\end{pmatrix}$

Sei $\varphi: \mathbb{R}^5 \rightarrow \mathbb{R}^5$ eine lineare Abbildung und definiert als

$\varphi(x) := A \cdot x$.

Was ist der Kern von $\varphi$?

<h3>Rechnung</h3>
$\begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
3  &  0 &  2 &  1 &  2\\
0  &  1 &  1 &  1 &  0\\
-1 & -1 & -2 & -2 & -1\\
 2 &  1 &  3 &  3 &  2
\end{pmatrix} \cdot
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{pmatrix} = 
\begin{pmatrix}
0 \\
0 \\
0 \\
0 \\
0
\end{pmatrix}$

$\leadsto 
\begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
3  &  0 &  2 &  1 &  2\\
0  &  1 &  1 &  1 &  0\\
-1 & -1 & -2 & -2 & -1\\
 2 &  1 &  3 &  3 &  2
\end{pmatrix}
\leadsto 
\begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
 0 & -3 & -4 & -5 & -4\\
 0 &  1 &  1 &  1 &  0\\
 0 &  0 &  0 &  0 &  0\\
 0 & -1 & -1 & -1 &  0
\end{pmatrix}$

$\leadsto 
\begin{pmatrix}
 1 &  1 &  2 &  2 &  1\\
 0 &  1 &  1 &  1 &  0\\
 0 &  0 & -1 & -2 & -1\\
 0 &  0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 &  0
\end{pmatrix}
\leadsto 
\begin{pmatrix}
 1 &  0 &  0 & -1 &  0\\
 0 &  1 &  0 & -1 & -1\\
 0 &  0 &  1 &  2 &  1\\
 0 &  0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 &  0
\end{pmatrix}$

Die Matrix hat Rang 3, daraus folgt, dass die Dimension des L&ouml;sungsraumes 2 ist.
Wieder &uuml;ber den -1-Trick kann man den L&ouml;sungsraum direkt ablesen:

$\mathcal{L} =
\left [
\begin{pmatrix}
  -1\\
  -1\\
   2\\
  -1\\
   0
\end{pmatrix},
\begin{pmatrix}
   0\\
  -1\\
   1\\
   0\\
  -1
\end{pmatrix}
\right ]
=
\text{Kern} \varphi
$
