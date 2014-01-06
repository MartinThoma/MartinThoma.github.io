---
layout: post
title: Wie berechnet man die Jordan'sche Normalform?
author: Martin Thoma
date: 2012-08-17 12:59:27.000000000 +02:00
categories:
- German posts
tags:
- Wolfram|Alpha
- mathematics
- Linear algebra
- normal form
featured_image: 2012/08/jordan-normal-form-block1.png
---
Dieser Artikel beschreibt, wie die Jordansche Normalform einer Matrix sowie die dazugeh&ouml;rige Basiswechselmatrix gefunden werden kann. Dabei wird hier eine Jordansche Normalform erzeugt, bei der die 1er auf der oberen Nebendiagonale sind und die gr&ouml;&szlig;ten Jordank&auml;stchen zuerst kommen.

Ich werde hier nicht erkl&auml;ren, warum es so funktioniert.

Hier sind zwei <a href="../jordansche-normalform-2x2-matrizen/" title="Jordansche Normalform: 2&times;2 Matrizen">Beispiele mit 2x2-Matrizen</a> und <a href="../jordansche-normalform-4x4-matrizen/" title="Jordansche Normalform: 4&times;4 Matrizen">Beispiele mit 4x4-Matrizen</a>.

Gegeben sei eine Matrix $A \in \mathbb{C}^{n \times n}$.

<h2>Berechnung der Jordanschen Normalform</h2>
<h3>Charakteristisches Polynom bestimmen</h3>
Als ersten Schritt muss man das charakteristische Polynom $p_A(\lambda)$ der Matrix $A$ bestimmen.

&rarr; <a href="../wie-berechnet-man-das-charakteristische-polynom/" title="Wie berechnet man das charakteristische Polynom?">Wie berechnet man das charakteristische Polynom?</a>

<h3>Zerlegung in Linearfaktoren</h3>
Die Zerlegung des charakteristischen Polynoms $p_A(\lambda)$ in Linearfaktoren kann ziemlich schwer sein. Daf&uuml;r muss man unbedingt die Mitternachtsformel $\lambda_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ k&ouml;nnen und eventuell wissen, wie eine <a href="http://de.wikipedia.org/wiki/Polynomdivision#Manueller_Ablauf">Polynomdivision</a> funktioniert. Eventuell muss man dazu auch Nullstellen erraten. Wenn es ums raten geht, w&uuml;rde ich folgendes ausprobieren: 0, 1, -1, 2, -2, 3, -3.

Sobald man diese Zerlegung hat, kann man die Eigenwerte und die algebraische Vielfachheit der Eigenwerte direkt ablesen. Die Eigenwerte stehen in der Jordanmatrix auf der Diagonalen. Die algebraische Vielfachheit entspricht der Seitenl&auml;nge des quadratischen Jordanblocks.

<h3>Anzahl der Jordank&auml;stchen bestimmen</h3>
Jeder Eigenwert hat genau einen Jordanblock. Jeder Jordanblock hat wiederum Jordank&auml;stchen. Das sieht so aus:

$  J = 
    \left(
      \begin{array}{*4{c}}
        A_{\lambda_1} &               &        & 0\\
                      & A_{\lambda_2} &        &  \\
                      &               & \ddots &  \\
           0          &               &        & A_{\lambda_k}
      \end{array}
    \right)$

$A_{\lambda_i}$ sind die Jordanbl&ouml;cke zu den Eigenwerten $\lambda_i$.

Die Einzelnen Jordanbl&ouml;cke schauen etwa so aus:
{% caption align="aligncenter" width="500" caption="Einzelner Jordanblock mit zwei hervorgehobenen Jordank&auml;stchen" url="../images/2012/08/jordan-normal-form-block.png" alt="Einzelner Jordanblock mit zwei hervorgehobenen Jordank&auml;stchen"  height="260" class="size-full wp-image-40381" %}

Jedes Jordank&auml;stchen ist quadratisch, hat auf der Diagonalen den Eigenwert und auf der oberen Nebendiagonale 1er. Sonst sind nur 0er im Jordank&auml;stchen. Au&szlig;erhalb der Jordank&auml;stchen sind im Jordanblock nur 0er. Insbesondere k&ouml;nnen also auf der oberen Nebendiagonalen des Jordanblocks 0er stehen!

Es gilt:
$\text{geometrische Vielfachheit des Eigenwertes } \lambda := \dim E_\lambda \leq \text{algebraische Vielfachheit des Eigenwertes } \lambda$ 
$\dim E_\lambda = \dim \text{Kern}(A - \lambda \cdot I) = \text{Anzahl der Jordank&auml;stchen im Jordanblock zu } \lambda$

&rarr; <a href="../wie-bestimme-ich-den-kern-einer-linearen-abbildung/" title="Wie bestimme ich den Kern einer linearen Abbildung?">Wie bestimme ich den Kern einer linearen Abbildung?</a>

Au&szlig;erdem gilt:
Die Gr&ouml;&szlig;e des gr&ouml;&szlig;ten Jordank&auml;stchens zum Eigenwert $\lambda_i$ ist gleich der Potenz, mit der der Linearfaktor $(x-\lambda_i)$ im Minimalpolynom (leider NICHT das charakteristische Polynom :-( ) vorkommt.

Nun kann man h&auml;ufig schon schlussfolgern, welche Gr&ouml;&szlig;e die einzelnen Jordank&auml;stchen haben. 
Zus&auml;tzlich haben &auml;hnliche Matrizen die gleiche Spur, die gleiche Determinante und den gleichen Rang. Das k&ouml;nnte helfen um "falsche" Jordanmatrizen auszuschlie&szlig;en.

Damit ist die Jordansche Normalform der Matrix h&auml;ufig schon bestimmt.

<h3>Gr&ouml;&szlig;e der Jordank&auml;stchen bestimmen</h3>
Sei $\Omega = \Phi - \lambda \cdot id$ und
$K_k = \text{Kern } ((\Omega)^k)$

Man w&auml;hle $q \in N^+$ so, dass $\dim K_q = \dim K_{q+1} = \dim K_{q+2} = ... = \dim V$ und q minimal.
Dann gilt: 
q ist die l&auml;nge des gr&ouml;&szlig;ten Jordank&auml;stchens in dem Jordanblock (und au&szlig;erdem der Exponent im Minimalpolynom zum betrachteten Eigenwert $\lambda$).

Es sei $a_0 = \dim K_0 = 0, a_1 = \dim K_1, a_i = \dim K_i$ mit $i \in 0, ..., q$.

Es gilt:
<ul>
  <li>Anzahl der K&auml;stchen der Gr&ouml;&szlig;e $1 \times 1$: $2 \cdot a_1 - a_0 - a_2$</li>
  <li>Anzahl der K&auml;stchen der Gr&ouml;&szlig;e $2 \times 2$: $2 \cdot a_2 - a_1 - a_3$</li>
  <li>Anzahl der K&auml;stchen der Gr&ouml;&szlig;e $3 \times 3$: $2 \cdot a_3 - a_2 - a_4$</li>
  <li>Anzahl der K&auml;stchen der Gr&ouml;&szlig;e $i \times i$: $2 \cdot a_i - a_{i-1} - a_{i+1}$</li>
</ul>

<h2>Berechnung der Basiswechselmatrix</h2>
Die Basiswechselmatrix wird manchmal auch Transformationsmatrix genannt. Es ist die invertierbare Matrix S, f&uuml;r die gilt:
$A = S \cdot J \cdot S^{-1}$

<h3>Kerne bestimmen</h3>
Bestimme $K_1, K_2, K_3, ... , K_q$, wobei 
$\dim K_{q-1} < \dim K_q = \dim K_{q+1} = \dim K_{q+2} ...$ 
gilt. Man kann also bei $K_q$ aufh&ouml;ren.

F&uuml;r jedes $K_k$ mit $k \in 1, ..., q$ bestimmt man eine m&ouml;glichst einfache Basis.

<h3>Zusammensetzen</h3>
An dieser Stelle sollte man wissen, wie gro&szlig; die Jordank&auml;stchen sind.

F&uuml;r ein Jordank&auml;stchen der Gr&ouml;&szlig;e $i$ w&auml;hlt man einen Basisvektor $v_i$ aus $K_i$, der jedoch nicht in $K_{i-1}$ liegt. Die restlichen $i-1$ Vektoren f&uuml;r dieses K&auml;stchen erh&auml;lt man, indem man die Abbildungsmatrix von $\Omega^{j}$, mit $j = 1, ..., i-1$, mit $v_i$ multipliziert. 

Also: 
$v_j = (A - \lambda \cdot E)^{i-j}$ mit $j = 1, ..., i$

Die Vektoren $v_j$ schreibt man mit aufsteigenden Indizes in die geordete Basis.
Beachte: Man w&auml;hlt nur den Vektor $v_i$, alle anderen Vektoren f&uuml;r dieses K&auml;stchen sind dadurch festgelegt! Au&szlig;erdem schreibt man $v_i$ erst am Ende in die Basis!

<h3>Inverse Matrix bestimmen</h3>
Sobald man $S$ bestimmt hat, muss man nur noch das Inverse davon bestimmen:
&rarr; <a href="../wie-bestimme-ich-das-inverse-einer-matrix/" title="Wie bestimme ich das Inverse einer Matrix?">Wie bestimme ich das Inverse einer Matrix?</a>

<h2>Interessante Eigenschaften der JNF</h2>
Im Zusammenhang mit der JNF (und einigen Klausuraufgaben) sind mir ein paar erw&auml;hnenswerte Eigenschaften aufgefallen:

<strong>Die Anzahl der Jordank&auml;stchen zum Eigenwert $\lambda = 0$ ist $n - \text{Rang}(A)$.</strong>
<em>Begr&uuml;ndung</em>: Die Anzahl der Jordank&auml;stchen zum Eigenwert $\lambda$ ist gleich der Dimension des Eigenraumes von $\lambda$. Der Eigenraum zum Eigenwert 0 hat die besonderheit, dass es der Kern ist. Nach der Dimensionsformel gilt: 
$\dim \text{Kern}(\Phi) + \dim \text{Bild}(\Phi) = n = \dim \text{Kern} + \text{ Rang}(A_\Phi)$.
