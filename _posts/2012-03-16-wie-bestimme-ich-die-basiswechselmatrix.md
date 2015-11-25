---
layout: post
title: Wie bestimme ich die Basiswechselmatrix?
author: Martin Thoma
date: 2012-03-16 17:06:11.000000000 +01:00
categories:
- German posts
tags:
- mathematics
- Linear algebra
- Matrix
featured_image: 2012/03/Basiswechselmatrix.png
---
Eine Basiswechselmatrix oder auch Übergangsmatrix dient dem Basiswechsel.

Angenommen man hat zwei Basen des $\mathbb{R}^2$-Vektorraumes:

\[B = \{\overbrace{\begin{pmatrix} 1 \\ 2 \end{pmatrix}}^{b_1}, \overbrace{\begin{pmatrix} 2 \\ 3 \end{pmatrix}}^{b_2} \}\]

und

\[\bar B = \{\underbrace{\begin{pmatrix} 3 \\ 5 \end{pmatrix}}_{\bar b_1}, \underbrace{\begin{pmatrix} 8 \\ 13 \end{pmatrix}}_{\bar b_2} \}\]

Sei nun $v := \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ ein Vektor zur Standardbasis.
Da $B$ und $\bar B$ auch Basen des $\mathbb{R}^2$ sind, kann man v auch zu diesen Basen darstellen:
$\Theta_{B}(v) = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$ und 
$\Theta_{\bar B}(v) = \begin{pmatrix} -5 \\ 2 \end{pmatrix}$

Wie kann man nun diese neue Darstellung berechnen?
Nun, wir bestimmen eine Matrix A für die gilt:
$A \cdot \Theta_B(v) = \Theta_{\bar B}(v) ~~~ \forall v \in \mathbb{R}^2$. Diese Matrix findet man, indem man beide geordneten Basen nebeneinander schreibt und die rechte Seite "durchgaußt":
$\left( \begin{array}{c c | c c} 
  1 & 2 & 3 &  8 \\
  2 & 3 & 5 & 13
\end{array} \right) 
\rightsquigarrow 
\left( \begin{array}{c c | c c} 
  \frac{1}{3} & \frac{2}{3} & 1 &  \frac{8}{3} \\
        2     & 3           & 5 & 13
\end{array} \right) 
\rightsquigarrow \\
\left( \begin{array}{c c | c c} 
  \frac{1}{3}   & \frac{2}{3}    & 1 &  \frac{8}{3} \\
  \frac{6-5}{3} & \frac{9-10}{3} & 0 & \frac{39-8 \cdot 5}{3}
\end{array} \right) 
\rightsquigarrow
\left( \begin{array}{c c | c c} 
  \frac{1}{3}   & \frac{2}{3}    & 1 &  \frac{8}{3} \\
  \frac{1}{3}   & -\frac{1}{3}   & 0 & -\frac{1}{3}
\end{array} \right) 
\rightsquigarrow \\
\left( \begin{array}{c c | c c} 
  \frac{9}{3}   & -\frac{6}{3}   & 1 & 0 \\
  \frac{1}{3}   & -\frac{1}{3}   & 0 & -\frac{1}{3}
\end{array} \right) 
\rightsquigarrow
\left( \begin{array}{c c | c c} 
  3 & -2 & 1 &  0 \\
  -1 & 1 & 0 &  1
\end{array} \right)$

Links steht die geordnete Basis B und rechts die geordnete Basis $\bar B$, also (von | nach) und rechts wendet man Gauß an.

Nun noch die Kontrolle, ob es stimmen kann:
\[\underbrace{\begin{pmatrix} 3 & -2 \\ -1 & 1 \end{pmatrix}}_{A_{B \bar B}} 
\cdot
\underbrace{\begin{pmatrix} -1 \\ 1 \end{pmatrix}}_{\Theta_{B}(v)} = \underbrace{\begin{pmatrix} -5 \\ 2 \end{pmatrix}}_{\Theta_{\bar B}(v)}\]

<h2>Siehe auch</h2>
<ul>
  <li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Basiswechsel_(Vektorraum)">Basiswechsel (Vektorraum)</a>, <a href="http://de.wikipedia.org/wiki/Standardbasis">Standardbasis</a></li>
  <li>Skript von Prof. Dr. Leuzinger, ab S. 82</li>
</ul>
