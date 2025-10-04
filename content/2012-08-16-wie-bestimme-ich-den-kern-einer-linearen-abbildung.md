---
layout: post
title: Wie bestimme ich den Kern einer linearen Abbildung?
slug: wie-bestimme-ich-den-kern-einer-linearen-abbildung
lang: de
author: Martin Thoma
date: 2012-08-16 15:54:15.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra
featured_image: 2012/03/Matrix-Inverses.png
---
## Definition

Der Kern einer linearen Abbildung ist eine Menge von Vektoren. In diesem Artikel erkläre ich kurz und bündig, wie man den Kern einer linearen Abbildung bestimmt.

> **Definition**: Sei $\Phi: V \rightarrow W$ eine lineare Abbildung. Der **Kern** von $\Phi$ ist die Menge aller Vektoren von $V$, die durch $\Phi$ auf den Nullvektor $0 \in W$ abgebildet werden, also:
>
> $$\text{Kern } \Phi := \{v \in V \mid \Phi(v) = 0\}$$

## Vorgehen

Jede lineare Abbildung $\Phi$ lässt sich in dieser Form beschreiben:

$$\Phi: V \rightarrow W \text{ mit } \dim V = m \text{ und } \dim W = n$$
$$\Phi(x) = A \cdot x, \quad A \in \mathbb{R}^{n \times m}, x \in V$$

Also muss man, um den Kern von $\Phi$ zu bestimmen, nur das folgende homogene Gleichungssystem nach $x$ auflösen:
$$A \cdot x = 0$$

In Wolfram|Alpha benötigt man dafür übrigens das Schlüsselwort `null space`. Hier ist [Beispiel #2 in Wolfram|Alpha](http://www.wolframalpha.com/input/?i=nullspace+%7B%7B-1%2C-1%2C-2%2C-2%2C-1%7D%2C%7B3%2C0%2C2%2C1%2C2%7D%2C%7B0%2C1%2C1%2C1%2C0%7D%2C%7B-1%2C-1%2C-2%2C-2%2C-1%7D%2C%7B2%2C1%2C3%2C3%2C2%7D%7D).

## Beispiel #1

### Aufgabenstellung
Sei $A \in \mathbb{R}^{3 \times 3}$ und definiert als

$$A := \begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix}$$

Sei $\Phi: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ eine lineare Abbildung und definiert als

$$\Phi(x) := A \cdot x$$

Was ist der Kern von $\Phi$?

<h3>Rechnung</h3>
$$
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
$$

Man sieht direkt, dass die Matrix den Rang 2 hat. Also muss der Lösungsraum 1-dimensional sein. Mit dem "$-1$-Trick" kommt man auf den Lösungsraum:

$$\mathcal{L} = \left [
\begin{pmatrix}
-1\\
2\\
-1
\end{pmatrix}
\right ]$$

Also:

$$\text{Kern } \Phi = \left [
\begin{pmatrix}
-1\\
2\\
-1
\end{pmatrix}
\right ]$$

## Beispiel #2

### Aufgabenstellung
Sei $A \in \mathbb{R}^{5 \times 5}$ und definiert als

$$A := \begin{pmatrix}
-1 & -1 & -2 & -2 & -1\\
3  &  0 &  2 &  1 &  2\\
0  &  1 &  1 &  1 &  0\\
-1 & -1 & -2 & -2 & -1\\
 2 &  1 &  3 &  3 &  2
\end{pmatrix}$$

Sei $\varphi: \mathbb{R}^5 \rightarrow \mathbb{R}^5$ eine lineare Abbildung und definiert als

$$\varphi(x) := A \cdot x$$

Was ist der Kern von $\varphi$?

<h3>Rechnung</h3>
$$\begin{pmatrix}
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
\end{pmatrix}$$

$$\leadsto
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
\end{pmatrix}$$

$$\leadsto
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
\end{pmatrix}$$

Die Matrix hat Rang 3, daraus folgt, dass die Dimension des Lösungsraumes 2 ist.
Wieder über den "$-1$-Trick" kann man den Lösungsraum direkt ablesen:

$$\mathcal{L} =
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
$$
