---
layout: post
status: publish
published: true
title: ! 'Jordansche Normalform: 2x2 Matrizen'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 41041
wordpress_url: http://martin-thoma.com/?p=41041
date: 2012-08-17 21:49:41.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- Linear algebra
comments: []
---
<div class="info">Hier sind $2 \times 2$ Beispiele zum Hauptartikel <a href="http://martin-thoma.com/wie-berechnet-man-die-jordansche-normalform/" title="Wie berechnet man die Jordan&rsquo;sche Normalform?">Wie berechnet man die Jordan&rsquo;sche Normalform?</a>.</div>

<h2>Beispiel 1</h2>
Gegeben sei die Matrix $A \in \mathbb{R}^{2 \times 2}$:
$A := \begin{pmatrix}
11 & -4\\
25 & -9
\end{pmatrix}$.

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_A(\lambda) = (\lambda - 1)^2$.

Daraus folgt: $\lambda = 1$ ist einziger Eigenwert
$\Rightarrow$ 1 Jordanblock

<strong>2. Anzahl der Jordank&auml;stchen bestimmen:</strong>

$
\begin{align}
\dim E_{1} &= \dim \text{Kern}(A -1 \cdot I) \\
&= \dim \text{Kern} \begin{pmatrix}
10 & -4\\
25 & -10
\end{pmatrix}\\
&= \dim \text{Kern} \begin{pmatrix}
10 & -4\\
0 & 0
\end{pmatrix}\\
&= \dim \left [ \begin{pmatrix}2\\5\end{pmatrix} \right ] \\
&= 1
\end{align}$

$\Rightarrow$ es gibt genau 1 Jordank&auml;stchen in diesem Jordanblock.

$\Rightarrow
J = 
\begin{pmatrix}1 & 1\\
0 & 1
\end{pmatrix}$.

<h3>Basiswechselmatrix bestimmen</h3>
<strong>Basisvektoren f&uuml;r den Eigenwert 1 bestimmen:</strong>
$\Omega = \Phi_{| H_\lambda} - \lambda \cdot id = 
\begin{pmatrix}
10 & - 4\\
25 & -10
\end{pmatrix}
$,

$K_1 = \text{Kern } \Omega^1 = \left [ \begin{pmatrix}2 \\ 5 \end{pmatrix} \right ]$
$K_2 = \text{Kern } \Omega^2 = \text{Kern } (\begin{pmatrix}10 & -4\\ 25 & -10 \end{pmatrix} \cdot \begin{pmatrix}10 & -4\\ 25 & -10 \end{pmatrix}) = \text{Kern } (\begin{pmatrix}0 & 0\\ 0 & 0 \end{pmatrix}) 
= 
\left[ 
\begin{pmatrix}1 \\ 0 \end{pmatrix}, 
\begin{pmatrix}0 \\ 1 \end{pmatrix}
\right]$

$K_2 \stackrel{!}{=} U_1 \oplus K_1 
\Rightarrow
\left [ 
\begin{pmatrix}
1 \\ 0
\end{pmatrix}
\right ] ~~~ U_0 = K_1$

[caption id="attachment_40961" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2012/08/jordan-normal-form-scheme-small.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/08/jordan-normal-form-scheme-small.png" alt="Schema zum finden der Basiswechselmatrix" title="Schema zum finden der Basiswechselmatrix" width="300" height="116" class="size-full wp-image-40961" /></a> Schema zum finden der Basiswechselmatrix[/caption]

W&auml;hle $b_1^1 \in U_1: b_1^1 = \begin{pmatrix}1 \\0 \end{pmatrix} \Rightarrow \Omega(b_1^1) = \begin{pmatrix}10 \\ 25 \end{pmatrix}$
$\Rightarrow S = 
\begin{pmatrix}
10 & 1 \\
25 & 0
\end{pmatrix}$
$\Rightarrow S^{-1} = 
\begin{pmatrix}
0 & \frac{1}{25} \\
1 & -\frac{2}{5}
\end{pmatrix}$

$A = S \cdot J \cdot S^{-1}$
$\Leftrightarrow 
\begin{pmatrix}
11 & -4\\
25 & -9
\end{pmatrix}
=
\begin{pmatrix}
10 & 1 \\
25 & 0
\end{pmatrix}
\cdot 
\begin{pmatrix}1 & 1\\
0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
0 & \frac{1}{25} \\
1 & -\frac{2}{5}
\end{pmatrix}$

<h2>Beispiel 2</h2>
Gegeben sei die Matrix $A \in \mathbb{R}^{2 \times 2}$:
$A := \begin{pmatrix}
1 & 2\\
3 & 6
\end{pmatrix}$.

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
$p_A(\lambda) = \det \begin{pmatrix}
1 -\lambda & 2\\
3 & 6 - \lambda
\end{pmatrix} = (1- \lambda) \cdot (6 - \lambda) - 6 = 6-6\lambda-\lambda+\lambda^2-6=\lambda^2-7\lambda = \lambda \cdot (\lambda - 7)$
Daraus folgt: 0 und 1 sind Eigenwerte. Sie haben jeweils die algebraischen Vielfachheit 1.
Daraus folgt: Die Jordansche Normalform hat genau zwei Jordanbl&ouml;cke, die beide die Gr&ouml;&szlig;e 1x1 haben.
Daraus folgt: Beide Jordanbl&ouml;cke haben genau ein Jordank&auml;stchen der Gr&ouml;&szlig;e 1x1.
Daraus folgt: Die Jordansche Normalform der Matrix ist:

$J = \begin{pmatrix}
0 & 0\\
0 & 7
\end{pmatrix}$

<h3>Basiswechselmatrix bestimmen</h3>
<strong>Basisvektoren f&uuml;r den Eigenwert 0 bestimmen:</strong>
$K_1 = \text{Kern }(A- 0 \cdot E) = \text{Kern } \begin{pmatrix}
1 & 2\\
3 & 6
\end{pmatrix} = \left [ \begin{pmatrix}2 \\ -1 \end{pmatrix} \right ] $

<strong>Basisvektoren f&uuml;r den Eigenwert 7 bestimmen:</strong>
$K_1 = \text{Kern }(A- 7 \cdot E) = \text{Kern } \begin{pmatrix}
-6 & 2\\
3 & -1
\end{pmatrix} = \text{Kern } \begin{pmatrix}
1 & -\frac{1}{3}\\
0 & 0
\end{pmatrix} = \left [ \begin{pmatrix}1 \\ 3 \end{pmatrix} \right ] $

<strong>Zusammensetzen:</strong>
$S = \begin{pmatrix}2 & 1 \\ -1 & 3 \end{pmatrix}$
$S^{-1} = \frac{1}{7} \cdot \begin{pmatrix}3 & -1 \\ 1 & 2 \end{pmatrix}$

<h3>Anmerkung</h3>
Man h&auml;tte &uuml;brigens jeden Vektor aus $\left [ \begin{pmatrix}2 \\ -1 \end{pmatrix} \right ] $ nehmen k&ouml;nnen. Angenommen, man h&auml;tte den Vektor $\begin{pmatrix}-14 \\ 7 \end{pmatrix}$ gew&auml;hlt:

$S = \begin{pmatrix}-14 & 1 \\ 7 & 3 \end{pmatrix}$
$S^{-1} = \frac{1}{49} \cdot \begin{pmatrix}-3 & 1 \\ 7 & 14 \end{pmatrix}$

Das gleiche gilt nat&uuml;rlich f&uuml;r jeden anderen gew&auml;hlten Vektor. Die inverse Matrix &auml;ndert sich selbstverst&auml;ndlich, jedoch nicht die Jordansche Normalform oder die urspr&uuml;ngliche Matrix.
