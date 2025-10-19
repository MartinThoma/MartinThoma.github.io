---
layout: post
title: Jordansche Normalform: 2x2 Matrizen
slug: jordansche-normalform-2x2-matrizen
lang: de
author: Martin Thoma
date: 2012-08-17 21:49:41.000000000 +02:00
category: German posts
tags: mathematics, Linear algebra
featured_image: 2012/08/jordan-normal-form-block1.png
---
<div class="info">Hier sind <span>$2 \times 2$</span> Beispiele zum Hauptartikel <a href="../wie-berechnet-man-die-jordansche-normalform/" title="Wie berechnet man die Jordan&rsquo;sche Normalform?">Wie berechnet man die Jordan&rsquo;sche Normalform?</a>.</div>

<h2>Beispiel 1</h2>
Gegeben sei die Matrix <span>$A \in \mathbb{R}^{2 \times 2}$</span>:
<div>$$A := \begin{pmatrix}
11 & -4\\
25 & -9
\end{pmatrix}$$</div>.

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
<span>$p_A(\lambda) = (\lambda - 1)^2$</span>.

Daraus folgt: <span>$\lambda = 1$</span> ist einziger Eigenwert
<span>$\Rightarrow$</span> 1 Jordanblock

<strong>2. Anzahl der Jordankästchen bestimmen:</strong>

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
\end{align}

<span>$\Rightarrow$</span> es gibt genau 1 Jordankästchen in diesem Jordanblock.

<div>$$\Rightarrow
J =
\begin{pmatrix}1 & 1\\
0 & 1
\end{pmatrix}$$</div>.

<h3>Basiswechselmatrix bestimmen</h3>
<strong>Basisvektoren für den Eigenwert 1 bestimmen:</strong>
<div>$$\Omega = \Phi_{| H_\lambda} - \lambda \cdot id =
\begin{pmatrix}
10 & - 4\\
25 & -10
\end{pmatrix}
$$</div>,

<div>$$K_1 = \text{Kern } \Omega^1 = \left [ \begin{pmatrix}2 \\ 5 \end{pmatrix} \right ]$$</div>
<div>$$K_2 = \text{Kern } \Omega^2 = \text{Kern } (\begin{pmatrix}10 & -4\\ 25 & -10 \end{pmatrix} \cdot \begin{pmatrix}10 & -4\\ 25 & -10 \end{pmatrix}) = \text{Kern } (\begin{pmatrix}0 & 0\\ 0 & 0 \end{pmatrix})
=
\left[
\begin{pmatrix}1 \\ 0 \end{pmatrix},
\begin{pmatrix}0 \\ 1 \end{pmatrix}
\right]$$</div>

<div>$$K_2 \stackrel{!}{=} U_1 \oplus K_1
\Rightarrow
\left [
\begin{pmatrix}
1 \\ 0
\end{pmatrix}
\right ] ~~~ U_0 = K_1$$</div>

<figure class="aligncenter">
            <a href="../images/2012/08/jordan-normal-form-scheme-small.png"><img src="../images/2012/08/jordan-normal-form-scheme-small.png" alt="Schema zum finden der Basiswechselmatrix" style="max-width:300px;max-height:116px" class="size-full wp-image-40961"/></a>
            <figcaption class="text-center">Schema zum finden der Basiswechselmatrix</figcaption>
        </figure>

Wähle <div>$$b_1^1 \in U_1: b_1^1 = \begin{pmatrix}1 \\0 \end{pmatrix} \Rightarrow \Omega(b_1^1) = \begin{pmatrix}10 \\ 25 \end{pmatrix}$$</div>
<div>$$\Rightarrow S =
\begin{pmatrix}
10 & 1 \\
25 & 0
\end{pmatrix}$$</div>
<div>$$\Rightarrow S^{-1} =
\begin{pmatrix}
0 & \frac{1}{25} \\
1 & -\frac{2}{5}
\end{pmatrix}$$</div>

<div>$$A = S \cdot J \cdot S^{-1}$$</div>
<div>$$\Leftrightarrow
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
\end{pmatrix}$$</div>

<h2>Beispiel 2</h2>
Gegeben sei die Matrix <span>$A \in \mathbb{R}^{2 \times 2}$</span>:
<div>$$A := \begin{pmatrix}
1 & 2\\
3 & 6
\end{pmatrix}$$</div>.

<h3>Jordannormalform bestimmen</h3>
<strong>1. Charakteristisches Polynom berechnen:</strong>
<div>$$p_A(\lambda) = \det \begin{pmatrix}
1 -\lambda & 2\\
3 & 6 - \lambda
\end{pmatrix} = (1- \lambda) \cdot (6 - \lambda) - 6 = 6-6\lambda-\lambda+\lambda^2-6=\lambda^2-7\lambda = \lambda \cdot (\lambda - 7)$$</div>
Daraus folgt: 0 und 1 sind Eigenwerte. Sie haben jeweils die algebraischen Vielfachheit 1.
Daraus folgt: Die Jordansche Normalform hat genau zwei Jordanblöcke, die beide die Größe 1x1 haben.
Daraus folgt: Beide Jordanblöcke haben genau ein Jordankästchen der Größe 1x1.
Daraus folgt: Die Jordansche Normalform der Matrix ist:

<div>$$J = \begin{pmatrix}
0 & 0\\
0 & 7
\end{pmatrix}$$</div>

<h3>Basiswechselmatrix bestimmen</h3>
<strong>Basisvektoren für den Eigenwert 0 bestimmen:</strong>
<div>$$K_1 = \text{Kern }(A- 0 \cdot E) = \text{Kern } \begin{pmatrix}
1 & 2\\
3 & 6
\end{pmatrix} = \left [ \begin{pmatrix}2 \\ -1 \end{pmatrix} \right ] $$</div>

<strong>Basisvektoren für den Eigenwert 7 bestimmen:</strong>
<div>$$K_1 = \text{Kern }(A- 7 \cdot E) = \text{Kern } \begin{pmatrix}
-6 & 2\\
3 & -1
\end{pmatrix} = \text{Kern } \begin{pmatrix}
1 & -\frac{1}{3}\\
0 & 0
\end{pmatrix} = \left [ \begin{pmatrix}1 \\ 3 \end{pmatrix} \right ] $$</div>

<strong>Zusammensetzen:</strong>
<div>$$S = \begin{pmatrix}2 & 1 \\ -1 & 3 \end{pmatrix}$$</div>
<div>$$S^{-1} = \frac{1}{7} \cdot \begin{pmatrix}3 & -1 \\ 1 & 2 \end{pmatrix}$$</div>

<h3>Anmerkung</h3>
Man hätte übrigens jeden Vektor aus $$\left [ \begin{pmatrix}2 \\ -1 \end{pmatrix} \right ]$$ nehmen können. Angenommen, man hätte den Vektor <span>$$\begin{pmatrix}-14 \\ 7 \end{pmatrix}$$</span> gewählt:

<div>$$S = \begin{pmatrix}-14 & 1 \\ 7 & 3 \end{pmatrix}$$</div>
<div>$$S^{-1} = \frac{1}{49} \cdot \begin{pmatrix}-3 & 1 \\ 7 & 14 \end{pmatrix}$$</div>

Das gleiche gilt natürlich für jeden anderen gewählten Vektor. Die inverse Matrix ändert sich selbstverständlich, jedoch nicht die Jordansche Normalform oder die ursprüngliche Matrix.
