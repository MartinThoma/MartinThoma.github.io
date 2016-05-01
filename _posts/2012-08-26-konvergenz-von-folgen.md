---
layout: post
title: Konvergenz von Folgen
author: Martin Thoma
date: 2012-08-26 18:04:36.000000000 +02:00
category: German posts
tags: analysis
featured_image: 2012/08/limes-thumbnail.png
---
<div class="definition">Sei $(a_n)$ eine Folge.

$(a_n)$ hei&szlig;t <strong>konvergent</strong> $:\Leftrightarrow \exists_{a \in \mathbb{R}} \forall_{ \varepsilon > 0} \exists_{n_0 = n_0(\varepsilon) \in \mathbb{N}}: |a_n - a | < \varepsilon~~~\forall n \geq n_0$. 

In diesem Fall hei&szlig;t a der <strong>Grenzwert</strong> von $(a_n)$ und man schreibt:
$\displaystyle \lim_{n \rightarrow \infty} (a_n) = a$.

Ist $(a_n)$ nicht konvergent, so hei&szlig;t $(a_n)$ <strong>divergent</strong>.</div>

Ich werde im Folgendem ein paar wichtige Hinweise geben, wie man konvergenz oder gegebenenfalls divergenz zeigen kann.

<h2>Wichtige Folgen</h2>
<h3>Konvergent</h3>
$\displaystyle e := \lim_{n \rightarrow \infty}(1+\frac{1}{n})^n = \lim_{n \rightarrow \infty} \sum_{k=0}^n \frac{1}{n!}$.

$\displaystyle \lim_{n \rightarrow \infty} \frac{1}{n} = 0$.

$\displaystyle \lim_{n \rightarrow \infty} \sqrt[n]{c} = 1$, mit $c > 0$.

$\displaystyle \lim_{n \rightarrow \infty} \sqrt[n]{n} = 1$.

<h3>Divergent</h3>
$a_n = n$.

$a_n = (-1)^n$

<h2>Beschr&auml;nktheit und Monotonie</h2>
Wenn man zeigen kann, dass eine Folge beschr&auml;nkt ist und monoton steigt oder f&auml;llt (und die Schranke in der richtigen Richtung liegt), dann konvergiert die Folge.

<strong>Beispiel:</strong>
<div class="example">Sei $(a_n)_{n \in \mathbb{N}}$ eine Folge und definiert durch $a_n := 2 + \frac{1}{n}$.

0 ist eine untere Schranke f&uuml;r $(a_n)_{n \in \mathbb{N}}$:
$\underbrace{2}_{\geq 0} + \underbrace{\frac{1}{n}}_{\geq 0} \Rightarrow a_n \geq 0$

$(a_n)_{n \in \mathbb{N}}$ ist monoton fallend:
Beweis von $a_n \geq a_{n+1} ~~~ \forall_{n \in \mathbb{N}}$:

$\begin{align}
                            1        & \geq 0 ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2n^2 + 3n + 1        & \geq 2 n^2 + 3n ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2n^2 + n + 2n + 1    & \geq n \cdot (2n + 3) ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow (2n + 1) \cdot (n+1) & \geq n \cdot (2n + 2 + 1) ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow \frac{2n+1}{n}       & \geq \frac{2 \cdot(n+1)+1}{n+1} ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2 + \frac{1}{n}      & \geq 2 + \frac{1}{n+1} ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow a_n                  & \geq a_{n+1}~~~ \forall_{n \in \mathbb{N}^+}
\end{align}$

$(a_n)_{n \in \mathbb{N}}$ ist also monoton fallend und hat eine untere Schranke. $(a_n)_{n \in \mathbb{N}}$ konvergiert also.

<em>Beachte</em>: Ich habe nicht die gr&ouml;&szlig;te untere Schranke gew&auml;hlt. Hatte ich das gemacht (und bewiesen, dass es keine gr&ouml;&szlig;ere untere Schranke gibt), dann h&auml;tte ich sogar den Grenzwert bestimmt.</div>

<h2>Cauchy-Folgen</h2>
In Banachr&auml;umen kann man auch nachweisen, dass eine Folge eine Cauchy-Folge ist um Konvergenz zu zeigen. Sie muss dazu dieser Bedingung gen&uuml;gen:

$\forall_{\varepsilon > 0} \exists_{n_0 \in \mathbb{N}}: \forall_{n,m\in\mathbb{N}, n>n_0, m>n_0}: |a_m- a_n| < \varepsilon$

<strong>Beispiel:</strong>
Mir f&auml;llt gerade kein Beispiel ein, bei dem man die Konvergenz sch&ouml;ner &uuml;ber das Cauchy-Kriterium zeigen kann als &uuml;ber die Beschr&auml;nktheit / Monotonie. Falls dir eines einf&auml;llt, kannst du es ja in den Kommentar schreiben. (mit <span class="code">&#091;latex&#093; \lim_{n \rightarrow \infty} 123 &#091;/latex&#093;</span> wird es auch als LaTeX dargestellt ;-))

<h2>Weiteres</h2>

Bei Polynomen darf man den "Ausklammer-Trick" nicht vergessen:
$a_n = \frac{3 \cdot n^5 + 2 \cdot n^2 + 42}{1000 \cdot n^5 + n^3} = \frac{n^5}{n^5} \cdot \frac{3 + 2 \cdot \frac{1}{n^3} + 42 \cdot \frac{1}{n^5}}{1000 + \frac{1}{n^2}}= \frac{3 + 2 \cdot \frac{1}{n^3} + 42 \cdot \frac{1}{n^5}}{1000 + \frac{1}{n^2}}$

Das sieht zwar deutlich schlimmer aus als vorher, ist aber besser. Wir wissen, dass $\displaystyle \lim_{n \rightarrow \infty} \frac{1}{n} = 0$ gilt. Also gilt:

$\displaystyle a_n \xrightarrow{n \rightarrow \infty} \frac{3 + 2 \cdot \overbrace{\frac{1}{n^3}}^{\rightarrow 0} + 42 \cdot \overbrace{\frac{1}{n^5}}^{\rightarrow 0}}{1000 + \underbrace{\frac{1}{n^2}}_{\rightarrow 0}} = \frac{3}{1000}$
