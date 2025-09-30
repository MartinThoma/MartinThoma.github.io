---
layout: post
lang: de
title: Jordansche Normalform: 4x4 Matrizen
author: Martin Thoma
date: 2012-09-10 11:28:08.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra, Matrix
featured_image: 2012/08/jordan-normal-form-block1.png
---
<div class="info">Hier sind $4 \times 4$ Beispiele zum Hauptartikel <a href="../wie-berechnet-man-die-jordansche-normalform/" title="Wie berechnet man die Jordan&rsquo;sche Normalform?">Wie berechnet man die Jordan&rsquo;sche Normalform?</a>.</div>

<h2>Beispiel 1</h2>
Gegeben sei die Matrix $A \in \mathbb{R}^{4 \times 4}$:
$$A := \begin{pmatrix}
1 & 2 & 47 & 11\\
3 & 2 &  8 & 15\\
0 & 0 &  3 &  1\\
0 & 0 &  8 & 1
\end{pmatrix}$$

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_A(\lambda) = (\lambda - 5) \cdot (\lambda - 4) \cdot (\lambda + 1)^2$.

(&rarr; <a href="http://www.wolframalpha.com/input/?i=%7B%7B1%2C2%2C47%2C11%7D%2C%7B3%2C2%2C8%2C15%7D%2C%7B0%2C0%2C3%2C1%7D%2C%7B0%2C0%2C8%2C1%7D%7D">Wolfram|Alpha</a> und &bdquo;<a href="../wie-berechnet-man-das-charakteristische-polynom/">Wie berechnet man das charakteristische Polynom?</a>&ldquo;)

Daraus folgt:
<ul>
  <li>$\lambda = 5$ ist Eigenwert mit der algebraischen Vielfachheit 1.</li>
  <li>$\lambda = 4$ ist Eigenwert mit der algebraischen Vielfachheit 1.</li>
  <li>$\lambda = -1$ ist Eigenwert mit der algebraischen Vielfachheit 2.</li>
</ul>

Es gibt also genau drei Jordan-Bl&ouml;cke in der Jordannormalform. Zwei davon haben die Kantenlänge 1 und deshalb nur ein Jordan-Kästchen.

<strong>2. Anzahl der Jordankästchen bestimmen:</strong>

\begin{align}
\dim \text{Eig}(-1) &= \dim \text{Kern}(A +1 \cdot I) \\
&= \dim \text{Kern} \begin{pmatrix}
2 & 2 & 47 & 11\\
3 & 3 &  8 & 15\\
0 & 0 &  4 &  1\\
0 & 0 &  8 & 2
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
1 & 1 & -3 & 13\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
0 & 0 & -4.5 & 13\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 & 1.5 &  0\\
0 & 0 &  0 & 14 \frac{1}{8}\\
0 & 0 &  1 &  \frac{1}{4}\\
0 & 0 &  0 & 0
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
1 & 1 &  0 & 0\\
0 & 0 &  0 & 0\\
0 & 0 &  1 & 0\\
0 & 0 &  0 & 1
\end{pmatrix} = \dim \left [ \begin{pmatrix}1\\-1\\0\\0 \end{pmatrix}\right ]\\
&= 1
\end{align}

Es gibt im Jordanblock zu \begin{align}
\dim \text{Eig}(1) &= \dim \text{Kern}(A-E)\\
 &= \dim \text{Kern }\begin{pmatrix}
-2 & -2 &  2 &  2\\
 2 & -1 &  1 &  1\\
 2 &  1 & -1 & -1\\
 0 & -2 &  2 &  0 \end{pmatrix}\\
 &= \dim \text{Kern }\begin{pmatrix}
 1 &  1 & -1 & -1\\
 0 & -3 &  3 &  3\\
 0 & -1 &  1 &  1\\
 0 &  1 & -1 &  0 \end{pmatrix}\\
 &= \dim \text{Kern }\begin{pmatrix}
 1 &  0 &  0 & -1\\
 0 &  1 & -1 &  0\\
 0 &  0 &  0 &  0\\
 0 &  0 &  0 &  1 \end{pmatrix}
\\
 &= \dim \left [\begin{pmatrix}0\\1\\1\\0\end{pmatrix} \right ] = 1
\end{align}
$$J_B =
\begin{pmatrix}
-1 &  0 & 0 & 0\\
 0 & -1 & 0 & 0\\
 0 &  0 & 1 & 1\\
 0 &  0 & 0 & 1
\end{pmatrix}$$
\begin{align}K_2(1) &= \text{Kern}(\Omega(1)^2) \\
       &= \text{Kern }\begin{pmatrix}
-2 & -2 &  2 &  2\\
 2 & -1 &  1 &  1\\
 2 &  1 & -1 & -1\\
 0 & -2 &  2 &  0 \end{pmatrix}^2 \\
       &= \text{Kern }\begin{pmatrix}
 4 &  4 & -4 & -4\\
-4 &  0 &  0 &  4\\
-4 & -4 &  4 &  4\\
 0 &  4 & -4 &  0 \end{pmatrix}\\
       &= \text{Kern }\begin{pmatrix}\\
 1 &  0 &  0 & -1\\
 0 &  1 & -1 &  0\\
 0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 \end{pmatrix} \\
       &= \left [ \begin{pmatrix}0\\1\\1\\0\end{pmatrix}, \begin{pmatrix}1\\0\\0\\1\end{pmatrix} \right ]
\end{align}K_2(1)\begin{align}
\Omega &= \begin{pmatrix}
0  &  0 & -1 & -1\\
-1 & -1 &  0 &  0\\
 0 &  0 &  1 &  1\\
 1 &  1 &  0 &  0
\end{pmatrix}\\
\Omega^2 &= \begin{pmatrix}
-1 & -1 & -1 & -1\\
 1 &  1 &  1 &  1\\
 1 &  1 &  1 &  1\\
-1 & -1 & -1 & -1
\end{pmatrix}\\
\Omega^3 &= \begin{pmatrix}
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0\\
 0 & 0 & 0 & 0
\end{pmatrix}
\end{align}.

\begin{align}
  \text{Eig}(1) &= K_1(1) = \text{Kern}(\Omega) \\
  &= \text{Kern} \begin{pmatrix}
     1 & 1 & 0 & 0\\
     0 & 0 & 0 & 0\\
     0 & 0 & 1 & 1\\
     0 & 0 & 0 & 0
   \end{pmatrix}\\
  &= \left [ \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\0\\1\\-1\end{pmatrix} \right ]
\end{align}
\begin{align}
  K_2(1) &= \text{Kern}(\Omega^2) \\
  &= \text{Kern} \begin{pmatrix}
     1 & 1 & 1 & 1\\
     0 & 0 & 0 & 0\\
     0 & 0 & 0 & 0\\
     0 & 0 & 0 & 0
   \end{pmatrix}\\
  &= \left [ \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}, \begin{pmatrix}1\\0\\-1\\0\end{pmatrix}, \begin{pmatrix}1\\0\\0\\-1\end{pmatrix} \right ]\\
  K_3(1) &= \text{Kern}(\Omega^3) = \mathbb{R}^4\\
\end{align}

$K_3(1) = \mathbb{R}^4$ ist das gr&ouml;&szlig;te Jordankästchen von der Gr&ouml;&szlig;e 3. Damit ergibt sich folgende Jordannormalform:

$$J =
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 1 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & 0 & 1
   \end{pmatrix}$$

<h3>Basiswechselmatrix bestimmen</h3>
Für jedes Jordankästchen der Länge $i$ muss nun 1 Vektor gewählt werden und $i-1$ Vektoren müssen bestimmt werden. Dafür muss $\Omega(\lambda) := C - \lambda \cdot E$ bestimmt werden.

<strong>Eigenwert 1:</strong>
<strong>Kästchengr&ouml;&szlig;e 3</strong>
$$b_1 \in K_3(1) \land b_1 \notin K_2(1) \Rightarrow b_1 \in \left [ \begin{pmatrix}1\\0\\0\\0\end{pmatrix} \right ]$$
Wähle $$b_1 = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}$$

$$b_2 = \Omega(b_1) = \begin{pmatrix}0\\-1\\0\\1\end{pmatrix}$$

$$b_3 = \Omega^2(b_1) = \Omega(b_2)= \begin{pmatrix}-1\\1\\1\\-1\end{pmatrix}$$

<strong>Kästchengr&ouml;&szlig;e 1</strong>
$$b_4 = \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}$$

Das 1-er Kästchen soll zuerst kommen, also muss $b_4$ zuerst in die Basiswechselmatrix.
Unsere gesuchte Matrix $S$ für die oben angegebene JNF ist also:
$$S = \begin{pmatrix}
b_4 & b_3 & b_2 & b_1
\end{pmatrix} = \begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix}$$

Nun sollte
$J = S^{-1} \cdot C \cdot S$ gelten. Also, Schritt für Schritt:

\begin{align}
S^{-1} \cdot C \cdot S &= \begin{pmatrix}
0 & -1 & 0 & -1\\
0 &  0 & 1 &  0\\
0 &  0 & 1 &  1\\
1 &  1 & 1 &  1
\end{pmatrix} \cdot \begin{pmatrix}
 1 & 0 & -1 & -1\\
-1 & 0 &  0 &  0\\
 0 & 0 &  2 &  1\\
 1 & 1 &  0 &  1
\end{pmatrix} \cdot
\begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix}\\
&=
\begin{pmatrix}
0 & -1 & 0 & -1\\
0 &  0 & 2 &  1\\
1 &  1 & 2 &  2\\
1 &  1 & 1 &  1
\end{pmatrix} \cdot
\begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix}
\\
&= \begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 1 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & 0 & 1
   \end{pmatrix}
\end{align}

<h3>Programmierung</h3>
Hier habe ich mal für Leute, die kein Python haben, als Kommentar das Ergebnis präsentiert. Ich denke damit ist klar, welchen Einfluss die Reihenfolge der Basisvektoren hat.
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from numpy import linalg

numpy.set_printoptions(precision=2, suppress=True, linewidth=120)

C = [[1, 0, -1, -1], [-1, 0, 0, 0], [0, 0, 2, 1], [1, 1, 0, 1]]
C = numpy.matrix(C)
b1 = [1, 0, 0, 0]
b2 = [0, -1, 0, 1]
b3 = [-1, 1, 1, -1]
b4 = [1, -1, 0, 0]

S = numpy.matrix([b4, b1, b2, b3]).transpose()  # [[ 1  0  0  0]
print("4123")  #                                   [ 0  1  0  0]
print(linalg.inv(S) * C * S)  #                    [ 0  1  1  0]
#                                                  [ 0  0  1  1]]

S = numpy.matrix([b4, b1, b3, b2]).transpose()  # [[ 1  0  0  0]
print("4132")  #                                   [ 0  1  0  0]
print(linalg.inv(S) * C * S)  #                    [ 0  0  1  1]
#                                                  [ 0  1  0  1]]

S = numpy.matrix([b4, b2, b1, b3]).transpose()  # [[ 1  0  0  0]
print("4213")  #                                   [ 0  1  1  0]
print(linalg.inv(S) * C * S)  #  [ 0  0  1  0]
#  [ 0  1  0  1]]

S = numpy.matrix([b4, b2, b3, b1]).transpose()  # [[ 1  0  0  0]
print("4231")  #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)  #  [ 0  1  1  0]
#  [ 0  0  0  1]]

S = numpy.matrix([b4, b3, b1, b2]).transpose()  # [[ 1  0  0  0]
print("4312")  #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)  #  [ 0  0  1  0]
#  [ 0  0  1  1]]

S = numpy.matrix([b4, b3, b2, b1]).transpose()  # [[ 1  0  0  0]
print("4321")  #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)  #  [ 0  0  1  1]
#  [ 0  0  0  1]]

S = numpy.matrix([b3, b2, b1, b4]).transpose()  # [[ 1  1  0  0]
print("3214")  #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)  #  [ 0  0  1  0]
#  [ 0  0  0  1]]
```
