---
layout: post
title: Wie berechnet man die Jordan'sche Normalform?
author: Martin Thoma
date: 2012-08-17 12:59:27.000000000 +02:00
category: German posts
tags: Wolfram|Alpha, mathematics, Linear algebra, normal form
featured_image: 2012/08/jordan-normal-form-block1.png
---
Dieser Artikel beschreibt, wie die Jordansche Normalform einer Matrix sowie die dazugehörige Basiswechselmatrix gefunden werden kann. Dabei wird hier eine Jordansche Normalform erzeugt, bei der die 1er auf der oberen Nebendiagonale sind und die größten Jordankästchen zuerst kommen.

Ich werde hier nicht erklären, warum es so funktioniert.

Hier sind zwei <a href="../jordansche-normalform-2x2-matrizen/" title="Jordansche Normalform: 2&times;2 Matrizen">Beispiele mit 2x2-Matrizen</a> und <a href="../jordansche-normalform-4x4-matrizen/" title="Jordansche Normalform: 4&times;4 Matrizen">Beispiele mit 4x4-Matrizen</a>.

Gegeben sei eine Matrix <span>$A \in \mathbb{C}^{n \times n}$</span>.

<h2>Berechnung der Jordanschen Normalform</h2>
<h3>Charakteristisches Polynom bestimmen</h3>
Als ersten Schritt muss man das charakteristische Polynom <span>$p_A(\lambda)$</span> der Matrix <span>$A$</span> bestimmen.

&rarr; <a href="../wie-berechnet-man-das-charakteristische-polynom/" title="Wie berechnet man das charakteristische Polynom?">Wie berechnet man das charakteristische Polynom?</a>

<h3>Zerlegung in Linearfaktoren</h3>
Die Zerlegung des charakteristischen Polynoms <span>$p_A(\lambda)$</span> in Linearfaktoren kann ziemlich schwer sein. Dafür muss man unbedingt die Mitternachtsformel <span>$\lambda_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$</span> können und eventuell wissen, wie eine <a href="http://de.wikipedia.org/wiki/Polynomdivision#Manueller_Ablauf">Polynomdivision</a> funktioniert. Eventuell muss man dazu auch Nullstellen erraten. Wenn es ums raten geht, würde ich folgendes ausprobieren: 0, 1, -1, 2, -2, 3, -3.

Sobald man diese Zerlegung hat, kann man die Eigenwerte und die algebraische Vielfachheit der Eigenwerte direkt ablesen. Die Eigenwerte stehen in der Jordanmatrix auf der Diagonalen. Die algebraische Vielfachheit entspricht der Seitenlänge des quadratischen Jordanblocks.

<h3>Anzahl der Jordankästchen bestimmen</h3>
Jeder Eigenwert hat genau einen Jordanblock. Jeder Jordanblock hat wiederum Jordankästchen. Das sieht so aus:

<span>\(  J =
    \left(
      \begin{array}{*4{c}}
        A_{\lambda_1} &               &        & 0\\
                      & A_{\lambda_2} &        &  \\
                      &               & \ddots &  \\
           0          &               &        & A_{\lambda_k}
      \end{array}
    \right)\)</span>

<span>$A_{\lambda_i}$</span> sind die Jordanblöcke zu den Eigenwerten <span>$\lambda_i$</span>.

Die Einzelnen Jordanblöcke schauen etwa so aus:
{% caption align="aligncenter" width="500" caption="Einzelner Jordanblock mit zwei hervorgehobenen Jordankästchen" url="../images/2012/08/jordan-normal-form-block.png" alt="Einzelner Jordanblock mit zwei hervorgehobenen Jordankästchen"  height="260" class="size-full wp-image-40381" %}

Jedes Jordankästchen ist quadratisch, hat auf der Diagonalen den Eigenwert und auf der oberen Nebendiagonale 1er. Sonst sind nur 0er im Jordankästchen. Außerhalb der Jordankästchen sind im Jordanblock nur 0er. Insbesondere können also auf der oberen Nebendiagonalen des Jordanblocks 0er stehen!

Es gilt:
<span>$\text{geometrische Vielfachheit des Eigenwertes } \lambda := \dim E_\lambda \leq \text{algebraische Vielfachheit des Eigenwertes } \lambda$</span>
<span>$\dim E_\lambda = \dim \text{Kern}(A - \lambda \cdot I) = \text{Anzahl der Jordankästchen im Jordanblock zu } \lambda$</span>

&rarr; <a href="../wie-bestimme-ich-den-kern-einer-linearen-abbildung/" title="Wie bestimme ich den Kern einer linearen Abbildung?">Wie bestimme ich den Kern einer linearen Abbildung?</a>

Außerdem gilt:
Die Größe des größten Jordankästchens zum Eigenwert <span>$\lambda_i$</span> ist gleich der Potenz, mit der der Linearfaktor <span>$(x-\lambda_i)$</span> im Minimalpolynom (leider NICHT das charakteristische Polynom ☹ ) vorkommt.

Nun kann man häufig schon schlussfolgern, welche Größe die einzelnen Jordankästchen haben.
Zusätzlich haben ähnliche Matrizen die gleiche Spur, die gleiche Determinante und den gleichen Rang. Das könnte helfen um "falsche" Jordanmatrizen auszuschließen.

Damit ist die Jordansche Normalform der Matrix häufig schon bestimmt.

<h3>Größe der Jordankästchen bestimmen</h3>
Sei <span>$\Omega = \Phi - \lambda \cdot id$</span> und
<span>$K_k = \text{Kern } ((\Omega)^k)$</span>

Man wähle <span>$q \in N^+$</span> so, dass <span>$\dim K_q = \dim K_{q+1} = \dim K_{q+2} = ... = \dim V$</span> und q minimal.
Dann gilt:
q ist die länge des größten Jordankästchens in dem Jordanblock (und außerdem der Exponent im Minimalpolynom zum betrachteten Eigenwert <span>$\lambda$</span>).

Es sei <span>$a_0 = \dim K_0 = 0, a_1 = \dim K_1, a_i = \dim K_i$</span> mit <span>$i \in 0, ..., q$</span>.

Es gilt:
<ul>
  <li>Anzahl der Kästchen der Größe <span>$1 \times 1$</span>: <span>$2 \cdot a_1 - a_0 - a_2$</span></li>
  <li>Anzahl der Kästchen der Größe <span>$2 \times 2$</span>: <span>$2 \cdot a_2 - a_1 - a_3$</span></li>
  <li>Anzahl der Kästchen der Größe <span>$3 \times 3$</span>: <span>$2 \cdot a_3 - a_2 - a_4$</span></li>
  <li>Anzahl der Kästchen der Größe <span>$i \times i$</span>: <span>$2 \cdot a_i - a_{i-1} - a_{i+1}$</span></li>
</ul>

<h2>Berechnung der Basiswechselmatrix</h2>
Die Basiswechselmatrix wird manchmal auch Transformationsmatrix genannt. Es ist die invertierbare Matrix S, für die gilt:
<span>$A = S \cdot J \cdot S^{-1}$</span>

<h3>Kerne bestimmen</h3>
Bestimme <span>$K_1, K_2, K_3, ... , K_q$</span>, wobei
<span>$\dim K_{q-1} < \dim K_q = \dim K_{q+1} = \dim K_{q+2} ...$</span>
gilt. Man kann also bei <span>$K_q$</span> aufhören.

Für jedes <span>$K_k$</span> mit <span>$k \in 1, ..., q$</span> bestimmt man eine möglichst einfache Basis.

<h3>Zusammensetzen</h3>
An dieser Stelle sollte man wissen, wie groß die Jordankästchen sind.

Für ein Jordankästchen der Größe <span>$i$</span> wählt man einen Basisvektor <span>$v_i$</span> aus <span>$K_i$</span>, der jedoch nicht in <span>$K_{i-1}$</span> liegt. Die restlichen <span>$i-1$</span> Vektoren für dieses Kästchen erhält man, indem man die Abbildungsmatrix von <span>$\Omega^{j}$</span>, mit <span>$j = 1, ..., i-1$</span>, mit <span>$v_i$</span> multipliziert.

Also:
<span>$v_j = (A - \lambda \cdot E)^{i-j}$</span> mit <span>$j = 1, ..., i$</span>

Die Vektoren <span>$v_j$</span> schreibt man mit aufsteigenden Indizes in die geordete Basis.
Beachte: Man wählt nur den Vektor <span>$v_i$</span>, alle anderen Vektoren für dieses Kästchen sind dadurch festgelegt! Außerdem schreibt man <span>$v_i$</span> erst am Ende in die Basis!

<h3>Inverse Matrix bestimmen</h3>
Sobald man <span>$S$</span> bestimmt hat, muss man nur noch das Inverse davon bestimmen:
&rarr; <a href="../wie-bestimme-ich-das-inverse-einer-matrix/" title="Wie bestimme ich das Inverse einer Matrix?">Wie bestimme ich das Inverse einer Matrix?</a>

## Interessante Eigenschaften der JNF
Im Zusammenhang mit der JNF (und einigen Klausuraufgaben) sind mir ein paar erwähnenswerte Eigenschaften aufgefallen:

<strong>Die Anzahl der Jordankästchen zum Eigenwert <span>$\lambda = 0$</span> ist <span>$n - \text{Rang}(A)$</span>.</strong><br/>
<em>Begründung</em>: Die Anzahl der Jordankästchen zum Eigenwert <span>$\lambda$</span> ist gleich der Dimension des Eigenraumes von <span>$\lambda$</span>. Der Eigenraum zum Eigenwert 0 hat die besonderheit, dass es der Kern ist. Nach der Dimensionsformel gilt:
<span>$\dim \text{Kern}(\Phi) + \dim \text{Bild}(\Phi) = n = \dim \text{Kern} + \text{ Rang}(A_\Phi)$</span>.
