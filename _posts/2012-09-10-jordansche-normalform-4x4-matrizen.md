---
layout: post
title: ! 'Jordansche Normalform: 4x4 Matrizen'
author: Martin Thoma
date: 2012-09-10 11:28:08.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra, Matrix
featured_image: 2012/08/jordan-normal-form-block1.png
---
<div class="info">Hier sind $4 \times 4$ Beispiele zum Hauptartikel <a href="../wie-berechnet-man-die-jordansche-normalform/" title="Wie berechnet man die Jordan&rsquo;sche Normalform?">Wie berechnet man die Jordan&rsquo;sche Normalform?</a>.</div>

<h2>Beispiel 1</h2>
Gegeben sei die Matrix $A \in \mathbb{R}^{4 \times 4}$:
$A := \begin{pmatrix}
1 & 2 & 47 & 11\\
3 & 2 &  8 & 15\\
0 & 0 &  3 &  1\\
0 & 0 &  8 & 1
\end{pmatrix}$.

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

Es gibt also genau drei Jordan-Bl&ouml;cke in der Jordannormalform. Zwei davon haben die Kantenl&auml;nge 1 und deshalb nur ein Jordan-K&auml;stchen.

<strong>2. Anzahl der Jordank&auml;stchen bestimmen:</strong>

$
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
$

Es gibt im Jordanblock zu $\lambda = -1$ also genau ein Jordank&auml;stchen.

Also ist die Jordansche Normalform festgelegt:

$J_A = 
\begin{pmatrix}
-1 &  1 & 0 & 0\\
 0 & -1 & 0 & 0\\
 0 &  0 & 4 & 0\\
 0 &  0 & 0 & 5
\end{pmatrix}$

<a href="http://www.wolframalpha.com/input/?i=%7B%7B1%2C2%2C47%2C11%7D%2C%7B3%2C2%2C8%2C15%7D%2C%7B0%2C0%2C3%2C1%7D%2C%7B0%2C0%2C8%2C1%7D%7D">Kontrolle mit Wolfram|Alpha</a>. Scheint zu stimmen.

<h3>Basiswechselmatrix bestimmen</h3>
F&uuml;r jedes Jordank&auml;stchen der L&auml;nge $i$ muss nun 1 Vektor gew&auml;hlt werden und $i-1$ Vektoren m&uuml;ssen bestimmt werden. Daf&uuml;r muss $\Omega(\lambda) := A - \lambda \cdot E$ bestimmt werden. 

<strong>Eigenwert -1</strong>:
$\Omega(-1) = \begin{pmatrix}
2 & 2 & 47 & 11\\
3 & 3 & 8  & 15\\
0 & 0 & 4  & 1\\
0 & 0 & 8  & 2
\end{pmatrix}$

$\begin{aligned}
K_1(-1) &= \text{Kern } \Omega(-1) \\
&= 
\text{Kern} \begin{pmatrix}
1 & 1 & 23.5  & 5.5\\
0 & 0 & -62.5 & -5.5\\
0 & 0 &   4   & 1\\
0 & 0 &   0   & 0\end{pmatrix} \\
&=
\text{Kern} \begin{pmatrix}
1 & 1 &   0 & 0\\
0 & 0 &   0 & 0\\
0 & 0 &   1 & 0\\
0 & 0 &   0 & 1\end{pmatrix} \\
&= \left [ \begin{pmatrix}1 \\ -1 \\ 0 \\ 0 \end{pmatrix} \right ]
\end{aligned}$.

$\Omega(-1)^2 = \begin{pmatrix}
10 & 10 & 386 & 121\\
15 & 15 & 317 & 116\\
 0 &  0 &  24 &   6\\
 0 &  0 &  48 &  12
\end{pmatrix}$.

Da das K&auml;stchen die Gr&ouml;&szlig;e 2 hat, ben&ouml;tigen wir noch $K_2$:

$K_2(-1) = \left [ 
\begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix},
\begin{pmatrix} \frac{49}{20} \\ 0 \\ \frac{1}{4} \\ -1 \end{pmatrix}
\right ] =
\left [ 
\begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix},
\begin{pmatrix} 49 \\ 0 \\ 5 \\ -20 \end{pmatrix}
\right ]  $.

(Check mit <a href="http://www.wolframalpha.com/input/?i=NullSpace+%7B%7B2%2C2%2C47%2C11%7D%2C%7B3%2C3%2C8%2C15%7D%2C%7B0%2C0%2C4%2C1%7D%2C%7B0%2C0%2C8%2C2%7D%7D%5E2">Wolfram|Alpha</a>. Scheint zu stimmen.)

Nun muss ein Vektor aus $K_2(-1)$ gew&auml;hlt werden, der nicht in $K_1(-1)$ ist. Das ist dann der erste Basisvektor f&uuml;r unsere Basiswechselmatrix. Die Wahl ist hier eindeutig:

$b_1 := \begin{pmatrix}49\\0\\5\\-20\end{pmatrix}$
$b_2 := \Omega(-1) \cdot b_1 = \begin{pmatrix}113\\-113\\0\\0\end{pmatrix}$


<strong>Eigenwert 4</strong>:
$\Omega(4) = \begin{pmatrix}
-3 &  2 & 47 & 11\\
 3 & -2 &  8 & 15\\
 0 &  0 & -1 &  1\\
 0 &  0 &  8 & -3
\end{pmatrix}$

$K_1(4) = \left [
\begin{pmatrix} -\frac{2}{3} \\ - 1 \\ 0 \\ 0\end{pmatrix}
\right ] = \left [
\begin{pmatrix} 2 \\ 3 \\ 0 \\ 0\end{pmatrix}
\right ] 
\Rightarrow
b_3 := \begin{pmatrix} 2 \\ 3 \\ 0 \\ 0\end{pmatrix}$

<strong>Eigenwert 5</strong>:
$\Omega(5) = \begin{pmatrix}
-4 &  2 & 47 & 11\\
 3 & -3 &  8 & 15\\
 0 &  0 & -2 &  1\\
 0 &  0 &  8 & -4
\end{pmatrix}$

$K_1(5) = \left [
\begin{pmatrix} -\frac{283}{12} \\ - \frac{359}{12} \\ -\frac{1}{2} \\ -1\end{pmatrix}
\right ] = \left [
\begin{pmatrix} 283 \\ 359 \\ 6 \\ 12\end{pmatrix}
\right ] 
\Rightarrow
b_4 := \begin{pmatrix} 283 \\ 359 \\ 6 \\ 12\end{pmatrix}$

Nun muss man die Vektoren noch in der richtigen Reihenfolge zusammensetzen. Da wir zuerst das -1 Jordank&auml;stchen, dann das 4er Jordank&auml;stchen und dann das 5er-K&auml;stchen wollen, schreiben wir sie in dieser Reihenfolge auf:
$S = \begin{pmatrix}b_2 & b_1 & b_3 & b_4\end{pmatrix} = \begin{pmatrix}
 113 & 49 & 2 & 283\\
-113 &  0 & 3 & 359\\
   0 &  5 & 0 &   6\\
   0 & -20& 0 &  12\end{pmatrix}$

Dann gilt:

$S^{-1} = \frac{1}{101700} \cdot \begin{pmatrix}
  540 &  -360 &    -4384 & 227\\
    0 &     0 &     6780 & -3390\\
20340 & 20340 & -1517364 & -329508\\
    0 &     0 &     1130 &  2825\end{pmatrix}$ (<a href="http://www.wolframalpha.com/input/?i=inverse+%7B%7B113%2C49%2C2%2C283%7D%2C%7B-113%2C0%2C3%2C359%7D%2C%7B0%2C5%2C0%2C6%7D%2C%7B0%2C-20%2C0%2C12%7D%7D">Wolfram|Alpha</a>)

Nun sollte
$J = S^{-1} \cdot A \cdot S$ gelten. Also, Schritt f&uuml;r Schritt:

$S^{-1} \cdot A \cdot S = \frac{1}{101700} \cdot \begin{pmatrix}
 -540 &   360 &     1164 &    -3617\\
    0 &     0 &    -6780 &     3390\\
81360 & 81360 & -6069456 & -1318032\\
    0 &     0 &    56500 &    14125
\end{pmatrix} \cdot S = 
\begin{pmatrix}
-1 &  1 & 0 & 0\\
 0 & -1 & 0 & 0\\
 0 &  0 & 4 & 0\\
 0 &  0 & 0 & 5
\end{pmatrix}$ (<a href="http://www.wolframalpha.com/input/?i=%7B%7B3%2F565%2C+-2%2F565%2C+-1096%2F25425%2C+227%2F101700%7D%2C+%7B0%2C+0%2C+1%2F15%2C+-1%2F30%7D%2C+%7B1%2F5%2C+1%2F5%2C+-373%2F25%2C+-81%2F25%7D%2C+%7B0%2C+0%2C+1%2F9%2C+1%2F36%7D%7D*%7B%7B1%2C2%2C47%2C11%7D%2C%7B3%2C2%2C8%2C15%7D%2C%7B0%2C0%2C3%2C1%7D%2C%7B0%2C0%2C8%2C1%7D%7D">Wolfram|Alpha</a> und <a href="http://www.wolframalpha.com/input/?i=%7B%7B-3%2F565%2C+2%2F565%2C+2791%2F25425%2C+-3617%2F101700%7D%2C+%7B0%2C+0%2C+-1%2F15%2C+1%2F30%7D%2C+%7B4%2F5%2C+4%2F5%2C+-1492%2F25%2C+-324%2F25%7D%2C+%7B0%2C+0%2C+5%2F9%2C+5%2F36%7D%7D*%7B%7B113%2C49%2C2%2C283%7D%2C%7B-113%2C0%2C3%2C359%7D%2C%7B0%2C5%2C0%2C6%7D%2C%7B0%2C-20%2C0%2C12%7D%7D">Schritt 2</a>)

<h3>Programmierung</h3>
Bei diesem Beispiel haben sowohl Python (numpy) als auch Wolfram|Alpha und Mathematica versagt:

{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
from numpy import linalg

A = [[1,2,47,11],[3,2,8,15],[0,0,3,1],[0,0,8,1]]
S = [[113,49,2,283],[-113,0,3,359],[0,5,0,6],[0,20,0,12]]

A = numpy.matrix(A)
S = numpy.matrix(S)

numpy.set_printoptions(precision=2, suppress=True, linewidth=120)
print("S^{-1} * A * S")
print(linalg.inv(S) * A * S){% endhighlight %}

Wolfram|Alpha hatte eine zu kleine Eingabegr&ouml;&szlig;e, Mathematica hat einfach gar nicht mehr reagiert und Python hat ein falsches Ergebnis ausgespuckt.

<h2>Beispiel 2</h2>
Gegeben sei die Matrix $B \in \mathbb{C}^{4 \times 4}$:
$B := \begin{pmatrix}
  -1 & -2 & 2 &  2\\
   2 &  0 & 1 & -1\\
   2 &  1 & 0 & -1\\
   0 & -2 & 2 & 1
\end{pmatrix}$

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_B(\lambda) = (1-\lambda)^2 \cdot (1+\lambda)^2$.

Daraus folgt: 
<ul>
  <li>$\lambda = 1$ ist Eigenwert mit der algebraischen Vielfachheit 2.</li>
  <li>$\lambda = -1$ ist Eigenwert mit der algebraischen Vielfachheit 2.</li>
</ul>

Es gibt also genau zwei Jordan-Bl&ouml;cke in der Jordannormalform. Beide haben die Kantenl&auml;nge 2.

<strong>2. Anzahl der Jordank&auml;stchen bestimmen:</strong>
$\begin{align}
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
\end{align}$

Analog:
$\begin{align}
\dim \text{Eig}(-1) &= \dim \text{Kern}(A-E)\\
 &= \dim \text{Kern }\begin{pmatrix}
 0 & -2 &  2 &  2\\
 2 &  1 &  1 &  1\\
 2 &  1 &  1 & -1\\
 0 & -2 &  2 &  2 \end{pmatrix}\\
 &= \dim \text{Kern }\begin{pmatrix}
 1 &  0 &  1 &  0\\
 0 &  1 & -1 & -1\\
 0 &  0 &  0 &  0\\
 0 &  0 &  0 &  0 \end{pmatrix}
\\
 &= \dim \left [\begin{pmatrix}1\\-1\\-1\\0\end{pmatrix}, \begin{pmatrix}0\\1\\0\\1\end{pmatrix} \right ] = 2
\end{align}$

Also ist die Jordansche Normalform festgelegt:

$J_B = 
\begin{pmatrix}
-1 &  0 & 0 & 0\\
 0 & -1 & 0 & 0\\
 0 &  0 & 1 & 1\\
 0 &  0 & 0 & 1
\end{pmatrix}$
&rarr; <a href="http://www.wolframalpha.com/input/?i=%7B%7B-1%2C-2%2C2%2C2%7D%2C%7B2%2C0%2C1%2C-1%7D%2C%7B2%2C1%2C0%2C-1%7D%2C%7B0%2C-2%2C2%2C1%7D%7D">Kontrolle mit Wolfram|Alpha</a>

<h3>Basiswechselmatrix bestimmen</h3>
F&uuml;r jedes Jordank&auml;stchen der L&auml;nge $i$ muss nun 1 Vektor gew&auml;hlt werden und $i-1$ Vektoren m&uuml;ssen bestimmt werden. Daf&uuml;r muss $\Omega(\lambda) := A - \lambda \cdot E$ bestimmt werden. 

<strong>Eigenwert 1:</strong>
$K_1(1) = \left [\begin{pmatrix}0\\1\\1\\0\end{pmatrix} \right ]$.
$\begin{align}
K_2(1) &= \text{Kern}(\Omega(1)^2) \\
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
\end{align}$

Nun muss ein Vektor aus $K_2(1)$ gew&auml;hlt werden, der nicht in $K_1(1)$ ist. Das ist dann der erste Basisvektor f&uuml;r unsere Basiswechselmatrix. Die Wahl ist hier eindeutig:

$b_1 = \begin{pmatrix}1\\0\\0\\1\end{pmatrix}$.
$b_2 = \Omega(1) \cdot b_1 = \begin{pmatrix}0\\1\\1\\0\end{pmatrix}$.
$b_3 = \begin{pmatrix}1\\-1\\-1\\0\end{pmatrix}, ~~~ b_4 = \begin{pmatrix}0\\1\\0\\1\end{pmatrix}$.

Nun muss man die Vektoren noch in der richtigen Reihenfolge zusammensetzen. Da wir zuerst den -1 Jordanblock und dann den 1er-Jordanblock wollen, schreiben wir sie in dieser Reihenfolge auf:
$S = \begin{pmatrix}b_3 & b_4 & b_2 & b_1\end{pmatrix} = \begin{pmatrix}
 1 & 0 & 0 & 1\\
-1 & 1 & 1 & 0\\
-1 & 0 & 1 & 0\\
 0 & 1 & 0 & 1\end{pmatrix}$

<h3>Programmierung</h3>
Hier kann man mal sch&ouml;n ein paar Variationen ausprobieren:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
from numpy import linalg

B = [[-1,-2,2,2],[2,0,1,-1],[2,1,0,-1],[0,-2,2,1]]
# b3, b4, b2, b1
S = [[1,0,0,1],[-1,1,1,0],[-1,0,1,0],[0,1,0,1]]
# b2, b1, b3, b4 - zuerst 1er Block
S = [[0,1,1,0],[1,0,-1,1],[1,0,-1,0],[0,1,0,1]] 

# Die Reihenfolge der Vektoren f&uuml;r die Jordank&auml;stchen innerhalb
# eines Jordanblocks ist egal
# b2, b1, b4, b3 = b2, b1, b3, b4 != alle anderen Reihenfolgen
S = [[0,1,0,1],[1,0,1,-1],[1,0,0,-1],[0,1,1,0]]
# Mit (b1, b2, b3, b4) ist die 1 auf der Nebendiagonale unten
S = [[1,0,1,0],[0,1,-1,1],[0,1,-1,0],[1,0,0,1]]

B = numpy.matrix(B)
S = numpy.matrix(S)

numpy.set_printoptions(precision=2, suppress=True, linewidth=120)
print("S^{-1} * B * S")
print(linalg.inv(S) * B * S){% endhighlight %}

<h2>Beispiel 3</h2>
Die Matrix aus diesem Beispiel ist aus der Klausur vom Fr&uuml;hjahr 2012 bei Prof. Dr. Wildericht Tuschmann.

Gegeben sei die Matrix $C \in \mathbb{R}^{4 \times 4}$:
$C := \begin{pmatrix}
 1 & 0 & -1 & -1\\
-1 & 0 &  0 &  0\\
 0 & 0 &  2 &  1\\
 1 & 1 &  0 &  1
\end{pmatrix}$.

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_C(\lambda) = (\lambda - 1)^4$.

Es gibt also genau einen Jordan-Block in der Jordannormalform.

<strong>2. Anzahl der Jordank&auml;stchen bestimmen:</strong>

$
\begin{align}
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
\end{align}
$.

$\begin{align}
  \text{Eig}(1) &= K_1(1) = \text{Kern}(\Omega) \\
  &= \text{Kern} \begin{pmatrix}
     1 & 1 & 0 & 0\\
     0 & 0 & 0 & 0\\
     0 & 0 & 1 & 1\\
     0 & 0 & 0 & 0
   \end{pmatrix}\\
  &= \left [ \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\0\\1\\-1\end{pmatrix} \right ]
\end{align}
$

Jetzt wissen wir, dass es zwei Jordank&auml;stchen gibt. Es gibt also zwei M&ouml;glichkeiten:
<ul>
  <li>Ein Jordank&auml;stchen hat die Gr&ouml;&szlig;e 1, dann muss das Andere die Gr&ouml;&szlig;e 3 haben.</li>
  <li>Ein Jordank&auml;stchen hat die Gr&ouml;&szlig;e 2, dann muss das Andere die Gr&ouml;&szlig;e 2 haben.</li>
</ul>

$\begin{align}
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
$

Da erst $K_3(1) = \mathbb{R}^4$ ist das gr&ouml;&szlig;te Jordank&auml;stchen von der Gr&ouml;&szlig;e 3. Damit ergibt sich folgende Jordannormalform:

$J = 
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 1 & 0\\
0 & 0 & 1 & 1\\
0 & 0 & 0 & 1
   \end{pmatrix}$

<h3>Basiswechselmatrix bestimmen</h3>
F&uuml;r jedes Jordank&auml;stchen der L&auml;nge $i$ muss nun 1 Vektor gew&auml;hlt werden und $i-1$ Vektoren m&uuml;ssen bestimmt werden. Daf&uuml;r muss $\Omega(\lambda) := C - \lambda \cdot E$ bestimmt werden. 

<strong>Eigenwert 1:</strong>
<strong>K&auml;stchengr&ouml;&szlig;e 3</strong>
$b_1 \in K_3(1) \land b_1 \notin K_2(1) \Rightarrow b_1 \in \left [ \begin{pmatrix}1\\0\\0\\0\end{pmatrix} \right ]$. W&auml;hle $b_1 = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}$.

$b_2 = \Omega(b_1) = \begin{pmatrix}0\\-1\\0\\1\end{pmatrix}$.

$b_3 = \Omega^2(b_1) = \Omega(b_2)= \begin{pmatrix}-1\\1\\1\\-1\end{pmatrix}$

<strong>K&auml;stchengr&ouml;&szlig;e 1</strong>
$b_4 = \begin{pmatrix}1\\-1\\0\\0\end{pmatrix}$

Das 1-er K&auml;stchen soll zuerst kommen, also muss $b_4$ zuerst in die Basiswechselmatrix.
Unsere gesuchte Matrix $S$ f&uuml;r die oben angegebene JNF ist also:
$S = \begin{pmatrix}
b_4 & b_3 & b_2 & b_1
\end{pmatrix} = \begin{pmatrix}
1  & -1 &  0 & 1\\
-1 &  1 & -1 & 0\\
 0 &  1 &  0 & 0\\
 0 & -1 &  1 & 0
\end{pmatrix} $

Nun sollte
$J = S^{-1} \cdot C \cdot S$ gelten. Also, Schritt f&uuml;r Schritt:

$\begin{align}
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
\end{align}$

<h3>Programmierung</h3>
Hier habe ich mal f&uuml;r Leute, die kein Python haben, als Kommentar das Ergebnis pr&auml;sentiert. Ich denke damit ist klar, welchen Einfluss die Reihenfolge der Basisvektoren hat.
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import numpy
from numpy import linalg
numpy.set_printoptions(precision=2, suppress=True, linewidth=120)
 
C  = [[1,0,-1,-1],[-1,0,0,0],[0,0,2,1],[1,1,0,1]]
C = numpy.matrix(C)
b1 = [1,0,0,0]
b2 = [0,-1,0,1]
b3 = [-1,1,1,-1]
b4 = [1,-1,0,0]

S = numpy.matrix([b4,b1,b2,b3]).transpose() # [[ 1  0  0  0]
print("4123")                               #  [ 0  1  0  0]
print(linalg.inv(S) * C * S)                #  [ 0  1  1  0]
                                            #  [ 0  0  1  1]]

S = numpy.matrix([b4,b1,b3,b2]).transpose() #[[ 1  0  0  0]
print("4132")                               # [ 0  1  0  0]
print(linalg.inv(S) * C * S)                # [ 0  0  1  1]
                                            # [ 0  1  0  1]]

S = numpy.matrix([b4,b2,b1,b3]).transpose() # [[ 1  0  0  0]
print("4213")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  1  0  1]]

S = numpy.matrix([b4,b2,b3,b1]).transpose() # [[ 1  0  0  0]
print("4231")                               #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)                #  [ 0  1  1  0]
                                            #  [ 0  0  0  1]]

S = numpy.matrix([b4,b3,b1,b2]).transpose() # [[ 1  0  0  0]
print("4312")                               #  [ 0  1  0  1]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  0  1  1]]

S = numpy.matrix([b4,b3,b2,b1]).transpose() # [[ 1  0  0  0]
print("4321")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  1]
                                            #  [ 0  0  0  1]]

S = numpy.matrix([b3,b2,b1,b4]).transpose() # [[ 1  1  0  0]
print("3214")                               #  [ 0  1  1  0]
print(linalg.inv(S) * C * S)                #  [ 0  0  1  0]
                                            #  [ 0  0  0  1]]
{% endhighlight %}
