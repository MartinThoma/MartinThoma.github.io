---
layout: post
status: publish
published: true
title: Eigenschaften von Abbildungsmatrizen
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 13981
wordpress_url: http://martin-thoma.com/?p=13981
date: 2012-03-26 17:30:44.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- Linear algebra
- Matrix
comments: []
---
Eine Abbildungsmatrix beschreibt eine lineare Abbildungs zwischen zwei endlichdimensionalen Vektorr&auml;umen. Sie ist abh&auml;ngig von der Basis des Urraums und des Zielraumes.
<h2>Formale Definition</h2>
<div class="definition">Eine <strong>Lineare Abbildung</strong> $\Phi$ muss folgende Eigenschaften erf&uuml;llen:
<ul>
	<li>$\Phi: V \rightarrow W$ ist eine Abbildung</li>
	<li>$\forall x, y \in W : \Phi(x+y) = \Phi(x) + \Phi(y)$</li>
	<li>$\forall x \in W : \forall a \in \mathbb{K}: \Phi(a \cdot x) = a \cdot \Phi(x)$</li>
</ul>
</div>
Sei V ein n-dimensionaler $\mathbb{K}$-Vektorraum mit der Basis $B = \{b_1, b_2, ..., b_n\}$ und W ein m-dimensonaler $\mathbb{K}$-Vektorraum mit der Basis $C = \{c_1, c_2, ..., c_m\}$.
<div class="definition">

Sei $\Phi:V \rightarrow W$ eine lineare Abbildung.

Dann ordnen wir der linearen Abbildung $\Phi$ in folgender Weise eine Matrix A zu:
$\Phi (b_k) = \sum_{i=1}^{m} a_{ik}c_i, ~~ k = 1, ..., n, ~~ a_{ik}\in \mathbb{K}$

Dann gilt:
$\Phi(x) = A \cdot x ~~~\text{ mit } x \in V$

Diese Matrix A nennt man <strong>Abbildungsmatrix</strong>.

</div>
<h2>Beispiele</h2>
Sei $\Phi: \mathbb{R}^4 \rightarrow \mathbb{R}^3$.
<h3>Nullzeile</h3>
$A_1 = \left . \underbrace{\begin{pmatrix} 0 &amp; 0 &amp; 0 &amp; 0 \\1 &amp; 2 &amp; 3 &amp; 4 \\5 &amp; 6 &amp; 7 &amp; 8 \end{pmatrix}}_\text{dim V} \right \} \text{dim W}$
<h4>Standardbasis</h4>
Sei $B_S = (\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix})$ und
$C_S = (\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix})$
Also sind B und C die geordnete Standardbasis des $\mathbb{R}^4$ bzw. des $\mathbb{R}^3$.

Was macht nun eine Abbildung $\Phi$ mit der Matrix $A_1$?

Ich denke ist ist leicht ersichtlich, dass bei einer Abbildungsmatrix dieser Form die erste Komponente des Bildvektors immer 0 ist.

$\Phi_1(\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}) = \begin{pmatrix} 0 \\ 30 \\ 70 \end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B0%2C0%2C0%2C0%7D%2C%7B1%2C2%2C3%2C4%7D%2C%7B5%2C6%2C7%2C8%7D%7D.%7B%7B1%7D%2C%7B2%7D%2C%7B3%7D%2C%7B4%7D%7D">Wolfram|Alpha</a>)
$\Phi_1(\begin{pmatrix} 5 \\ -2 \\ 7 \\ -1 \end{pmatrix}) = \begin{pmatrix} 0 \\ 18 \\ 54 \end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B0%2C0%2C0%2C0%7D%2C%7B1%2C2%2C3%2C4%7D%2C%7B5%2C6%2C7%2C8%7D%7D.%7B%7B5%7D%2C%7B-2%7D%2C%7B7%7D%2C%7B-1%7D%7D">Wolfram|Alpha</a>)
<h4>Andere Basis</h4>
Sei $B_1 = (\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \\ 3 \\ 7 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \\ 4 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ 7 \\ 1 \\ 8 \end{pmatrix})$ und
$C_1 = (\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}, \begin{pmatrix} 3 \\ 5 \\ 7 \end{pmatrix}, \begin{pmatrix} 5 \\ 7 \\ 11 \end{pmatrix})$

Auch hier schauen wir uns wieder die Abbildung $\Phi$ mit der Abbildungsmatrix $A_1$ an.

$\Phi_1(\underbrace{\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}}_\text{in Basis C}) = A_1 \cdot \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} = \underbrace{\begin{pmatrix} 0 \\ 30 \\ 70 \end{pmatrix}}_\text{in Basis B}$

Auch hier ist also die erste Komponente jedes Bildvektors 0. Allerdings haben die Bildvektoren nun eine andere Basis. Sie werden sozusagen anders interpretiert.
<h3>Nullspalte</h3>
$A_2 = \begin{pmatrix} 0 &amp; 1 &amp; 2 &amp; 3 \\0 &amp; 4 &amp; 5 &amp; 6 \\0 &amp; 7 &amp; 8 &amp; 9 \end{pmatrix}$

Nun mal wieder zwei Beispiel-Abbildungen:
$\Phi_2(\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}) = \begin{pmatrix} 20 \\ 47 \\ 74 \end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B0%2C1%2C2%2C3%7D%2C%7B0%2C4%2C5%2C6%7D%2C%7B0%2C7%2C8%2C9%7D%7D.%7B%7B1%7D%2C%7B2%7D%2C%7B3%7D%2C%7B4%7D%7D">Wolfram|Alpha</a>)
$\Phi_2(\begin{pmatrix} 100 \\ 2 \\ 3 \\ 7 \end{pmatrix}) = \begin{pmatrix} 20 \\ 47 \\ 74 \end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B0%2C1%2C2%2C3%7D%2C%7B0%2C4%2C5%2C6%7D%2C%7B0%2C7%2C8%2C9%7D%7D.%7B%7B100%7D%2C%7B2%7D%2C%7B3%7D%2C%7B4%7D%7D">Wolfram|Alpha</a>)

Wenn die Abbildungsmatrix eine Nullspalte hat, ist es egal was der abzubildende Vektor als Eintrag an dieser Stelle hat.
<h2>Basiswechsel bei Abbildungen</h2>
Ich habe ja gerade veranschaulicht, dass bei einem Basiswechsel zwar die Abbildung gleich bleibt, es aber dennoch unterschiedliche Vektoren sind. Sie m&uuml;ssen halt unterschiedlich interpretiert werden.

Nun k&ouml;nnte man die Abbildung, also insbesondere die Matrix, so &auml;ndern, dass die Vektoren, die man als "gleich" interpretieren w&uuml;rde, gleich abgebildet werden.

Wir suchen also eine neue Abbildungsmatrix $A_1'$, die die gleiche Abbildung beschreibt wie $A_1$ mit den Standardbasen, nur von $B_1$ nach $C_1$.

Wenn man das machen will, kann man sich den Vorgang wie eine Ansammlung von Funktionen (im Sinne der Informatik) betrachten. Wir haben eine Funktion, die die Abbildung von der Standardbasis in die Standardbasis beschreibt. Als Input bekommen wir einen Vektor in der Basis $B_1$ und herauskommen soll ein Vektor in der Basis $C_1$. Wir m&uuml;ssen also den Input-Vektor von der Basis $B_1$ in die Standardbasis umwandeln und den Output-Vektor der gegebenen Funktion von der Standardbasis in die Basis $C_1$ konvertieren.

Dazu bestimmen wir zuerst die Basiswechselmatrix $T_S^{B1}$ von der Basis $B_1$ in die Standardbasis. Das ist genau die Basis selbst:
$T_{B1}^S =
\begin{pmatrix}
1 &amp; 1 &amp; 3 &amp; 2 \\
2 &amp; 3 &amp; 1 &amp; 7 \\
3 &amp; 3 &amp; 4 &amp; 1 \\
4 &amp; 7 &amp; 1 &amp; 8
\end{pmatrix}$ (siehe alten <a title="Wie bestimme ich die Basiswechselmatrix?" href="http://martin-thoma.com/wie-bestimme-ich-die-basiswechselmatrix/">Blogpost</a>)

Und die Basiswechselmatrix $T_S^{C1}$ von der Standardbasis in die Basis $C_1$. Das ist das Inverse der Basis $C_1$:
$T_S^{C1} = \frac{1}{2} \cdot
\begin{pmatrix}
-6 &amp; -2 &amp; 4 \\
-2 &amp; 3 &amp; -1 \\
4 &amp; -1 &amp; -1
\end{pmatrix}$ (siehe <a href="http://martin-thoma.com/?p=13981&amp;preview=true#hnlichkeit">Wolfram|Alpha</a>)

Insgesamt sieht das dann so aus: $T_S^{C1} \cdot (A_1 \cdot (T_{B1} \cdot x))$. Da f&uuml;r die Matrixmultiplikation das <a href="http://de.wikipedia.org/wiki/Assoziativgesetz">Assoziativgesetz</a> gilt, kann man das vereinfachen:

$A_1' = T_S^{C1} \cdot A_1 \cdot T_{B1}^S =
\begin{pmatrix}
110 &amp; 156 &amp; 93 &amp; 195 \\
10 &amp; 16 &amp; 3 &amp; 15 \\
-50 &amp; -72 &amp; -39 &amp; -87
\end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B-3%2C+-1%2C+2%7D%2C+%7B-1%2C+3%2F2%2C+-1%2F2%7D%2C+%7B2%2C+-1%2F2%2C+-1%2F2%7D%7D+*+%7B%7B0%2C0%2C0%2C0%7D%2C%7B1%2C2%2C3%2C4%7D%2C%7B5%2C6%2C7%2C8%7D%7D+*+%7B%7B1%2C1%2C3%2C2%7D%2C%7B2%2C3%2C1%2C7%7D%2C%7B3%2C3%2C4%2C1%7D%2C%7B4%2C7%2C1%2C8%7D%7D">Wolfram|Alpha</a>)

Ein Test ob es stimmen kann:
z.B. sind $\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}_S = 1 \cdot \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix} + 0 \cdot \begin{pmatrix} 1 \\ 3 \\ 3 \\ 7 \end{pmatrix} + 0 \cdot \begin{pmatrix} 3 \\ 1 \\ 4 \\ 1 \end{pmatrix} + 0 \cdot \begin{pmatrix} 2 \\ 7 \\ 1 \\ 8 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}_{B_1} $ und
$\begin{pmatrix} 0 \\ 30 \\ 70 \end{pmatrix}_S = 110 \cdot \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} + 10 \cdot \begin{pmatrix} 3 \\ 5 \\ 7 \end{pmatrix} -50 \cdot \begin{pmatrix} 5 \\ 7 \\ 11 \end{pmatrix} = \begin{pmatrix} 110 \\ 10 \\ -50 \end{pmatrix}_{C_1}$

$\begin{pmatrix}
110 &amp; 156 &amp; 93 &amp; 195 \\
10 &amp; 16 &amp; 3 &amp; 15 \\
-50 &amp; -72 &amp; -39 &amp; -87
\end{pmatrix} \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}_{B_1} = \begin{pmatrix} 110 \\ 10 \\ -50 \end{pmatrix}$ (siehe <a href="http://www.wolframalpha.com/input/?i=%7B%7B110%2C+156%2C+93%2C+195%7D%2C+%7B10%2C+16%2C+3%2C+15%7D%2C+%7B-50%2C+-72%2C+-39%2C+-87%7D%7D+*+%7B%7B1%7D%2C%7B0%7D%2C%7B0%7D%2C%7B0%7D%7D">Wolfram|Alpha</a>)

Ich habe keine Ahnung, wie man nur mit den Basen B und C und der Abbildungsmatrix $A_1'$ wieder auf die Abbildungsmatrix $A_1$ kommt. Ich habe auf <a title="How can I determinate the bases for the most simple representation of a linear transformation?" href="http://math.stackexchange.com/q/123495/6876">Stackexchange</a> mal nachgefragt, aber das ist nicht von Erfolg gekr&ouml;nt gewesen.
<h2>Anzahl der Abbildungsmatrizen</h2>
F&uuml;r jede lineare Abbildungen $\Phi: V \rightarrow W$ (wobei V und W <strong>endliche</strong> Vektorr&auml;ume sind) gibt es eine Abbildungsmatrix.

Wie sieht dann die Abbildungsmatrix folgender Abbildung aus?
<blockquote>Sei $V:= \{p \in \mathbb{R}[t] | deg(t) \leq 5 \}$ der Vektorraum aller Polynome in t mit reellen Koeffizienten und Grad $ \leq 5$.
Sei $F: V \rightarrow V$ die Shift-Abbildung $(Fp)(t) = p(t+1)$
<p class="quote-source">(Quelle: <a href="http://matheraum.de/forum/Shift-Abbildung/t463098">Matheraum.de</a>)</p>
</blockquote>

Wenn V allerdings der $\mathbb{Z}/ 2 \mathbb{Z}$ und W der $\mathbb{Z}/ 3 \mathbb{Z}$ &uuml;ber jeweils den K&ouml;rper $\mathbb{Z}/ 2 \mathbb{Z}$ sind, dann ist die Abbildungsmatrix eine 1x1 Matrix. Das eine Element dieser 1x1 Matrix kann zwei verschiedene Werte - 0 und 1 - annehmen. Selbst wenn W der $\mathbb{Z}/ 41 \mathbb{Z}$ w&auml;re, w&uuml;rde es nur zwei verschiedene Abbildungen geben.

Wenn V der $\mathbb{Z}/ 3 \mathbb{Z}$ und W der $\mathbb{Z}/ 2 \mathbb{Z}$ ist, dann gibt es nur eine lineare Abbildung $\Phi: V \rightarrow W$(die Nullabbildung).
Die Abbildungsmatrix $\begin{pmatrix}1\end{pmatrix}$ bezeichnet keine lineare Abbildung $\Phi$, da 2 in V ist, aber nicht in W.

Es scheint also so zu sein, dass man im Allgemeinen nichts &uuml;ber die Anzahl der linearen Abbildungen sagen kann.
<h2>Dies und das</h2>
Zwei lineare Abbildungen k&ouml;nnen hintereinander ausgef&uuml;hrt werden, indem ihre Matrizen multipliziert werden:
$\Phi_1 : V \rightarrow W, \Phi_1(x) := A_1 \cdot x$
$\Phi_2 : W \rightarrow X, \Phi_2(x) := A_2 \cdot x$
$\Phi_2 \circ \Phi_1 : V \rightarrow X, x \mapsto \Phi_2 \circ \Phi_1(x) := \Phi_2(\Phi_1(x)) = A_2 \cdot (A_1 \cdot x) = (A_2 \cdot A_1) \cdot x$

Der Rang der Abbildungsmatrix entspricht der Dimension des Bildes der Abbildung.
<h2>Siehe auch</h2>
<ul>
	<li>Wikipedia: <a href="http://de.wikipedia.org/wiki/Vektorraum">Vektorraum</a>, <a href="http://de.wikipedia.org/wiki/Abbildungsmatrix">Abbildungsmatrix</a>, <a href="http://de.wikipedia.org/wiki/Rang_(Mathematik)">Rang</a></li>
	<li><a title="Wie bestimme ich die Basiswechselmatrix?" href="http://martin-thoma.com/wie-bestimme-ich-die-basiswechselmatrix/">Wie bestimme ich die Basiswechselmatrix?</a></li>
	<li>Skript von Prof. Dr. Leunzinger, ab S. 101 (im passwortgesch&uuml;tzten <a href="https://studium.kit.edu/sites/vab/0x869D2B3648EA0D498D68FE4A6098E555/Vorlesungsunterlagen/Forms/AllItems.aspx">VAB</a>)</li>
</ul>
