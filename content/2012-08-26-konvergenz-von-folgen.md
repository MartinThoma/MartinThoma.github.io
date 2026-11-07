---
layout: post
title: Konvergenz von Folgen
slug: konvergenz-von-folgen
lang: de
author: Martin Thoma
date: 2012-08-26 18:04:36.000000000 +02:00
category: German posts
tags: Mathematics, Analysis
featured_image: 2012/08/limes-thumbnail.png
---
<figure class="ai-generated">
    <a href="../images/2012/08/konvergenz-folgen.jpg"><img src="../images/2012/08/konvergenz-folgen.jpg" alt="Zahlengerade mit Punkten, die sich einem Grenzwert nähern, um den ein schmales Band liegt, in dem alle späteren Punkte liegen" width="1376" height="768"></a>
    <figcaption>Eine Folge konvergiert, wenn fast alle Glieder in jeder Umgebung des Grenzwerts liegen.</figcaption>
</figure>

<div class="definition">Sei $(a_n)$ eine Folge.

$(a_n)$ heißt <strong>konvergent</strong> $:\Leftrightarrow \exists_{a \in \mathbb{R}} \forall_{ \varepsilon > 0} \exists_{n_0 = n_0(\varepsilon) \in \mathbb{N}}: |a_n - a | < \varepsilon~~~\forall n \geq n_0$.

In diesem Fall heißt a der <strong>Grenzwert</strong> von $(a_n)$ und man schreibt:
$\displaystyle \lim_{n \rightarrow \infty} (a_n) = a$.

Ist $(a_n)$ nicht konvergent, so heißt $(a_n)$ <strong>divergent</strong>.</div>

Ich werde im Folgenden ein paar wichtige Hinweise geben, wie man Konvergenz oder gegebenenfalls Divergenz zeigen kann.

<h2>Wichtige Folgen</h2>
<h3>Konvergent</h3>
$\displaystyle e := \lim_{n \rightarrow \infty}(1+\frac{1}{n})^n = \lim_{n \rightarrow \infty} \sum_{k=0}^n \frac{1}{n!}$.

$\displaystyle \lim_{n \rightarrow \infty} \frac{1}{n} = 0$.

$\displaystyle \lim_{n \rightarrow \infty} \sqrt[n]{c} = 1$, mit $c > 0$.

$\displaystyle \lim_{n \rightarrow \infty} \sqrt[n]{n} = 1$.

<h3>Divergent</h3>
$a_n = n$.

$a_n = (-1)^n$

<h2>Beschränktheit und Monotonie</h2>
Wenn man zeigen kann, dass eine Folge beschränkt ist und monoton steigt oder fällt (und die Schranke in der richtigen Richtung liegt), dann konvergiert die Folge.

<strong>Beispiel:</strong>
<div class="example">Sei $(a_n)_{n \in \mathbb{N}}$ eine Folge und definiert durch $a_n := 2 + \frac{1}{n}$.

0 ist eine untere Schranke für $(a_n)_{n \in \mathbb{N}}$:
$\underbrace{2}_{\geq 0} + \underbrace{\frac{1}{n}}_{\geq 0} \Rightarrow a_n \geq 0$

$(a_n)_{n \in \mathbb{N}}$ ist monoton fallend:
Beweis von $a_n \geq a_{n+1} ~~~ \forall_{n \in \mathbb{N}}$:

\begin{align}
                            1        & \geq 0 ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2n^2 + 3n + 1        & \geq 2 n^2 + 3n ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2n^2 + n + 2n + 1    & \geq n \cdot (2n + 3) ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow (2n + 1) \cdot (n+1) & \geq n \cdot (2n + 2 + 1) ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow \frac{2n+1}{n}       & \geq \frac{2 \cdot(n+1)+1}{n+1} ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow 2 + \frac{1}{n}      & \geq 2 + \frac{1}{n+1} ~~~ \forall_{n \in \mathbb{N}^+} \\
\Leftrightarrow a_n                  & \geq a_{n+1}~~~ \forall_{n \in \mathbb{N}^+}
\end{align}

$(a_n)_{n \in \mathbb{N}}$ ist also monoton fallend und hat eine untere Schranke. $(a_n)_{n \in \mathbb{N}}$ konvergiert also.

<em>Beachte</em>: Ich habe nicht die größte untere Schranke gewählt. Hatte ich das gemacht (und bewiesen, dass es keine größere untere Schranke gibt), dann hätte ich sogar den Grenzwert bestimmt.</div>

<h2>Cauchy-Folgen</h2>
In Banachräumen kann man auch nachweisen, dass eine Folge eine Cauchy-Folge ist um Konvergenz zu zeigen. Sie muss dazu dieser Bedingung genügen:

$\forall_{\varepsilon > 0} \exists_{n_0 \in \mathbb{N}}: \forall_{n,m\in\mathbb{N}, n>n_0, m>n_0}: |a_m- a_n| < \varepsilon$

Das Cauchy-Kriterium ist praktisch, wenn die Folge nicht monoton ist und man den Grenzwert nicht kennt: Man muss nur zeigen, dass die Folgenglieder beliebig nahe beieinander liegen.

<strong>Beispiel:</strong>
<div class="example">Sei $(a_n)_{n \in \mathbb{N}}$ definiert durch $a_n := \sum_{k=1}^n \frac{\sin(k)}{k^2}$.

Diese Folge ist nicht monoton: $\sin(k)$ wechselt immer wieder das Vorzeichen, so ist $a_1 \approx 0{,}841$, $a_3 \approx 1{,}085$ und $a_4 \approx 1{,}037$. Mit Beschränktheit und Monotonie kommt man hier also nicht weiter. Den Grenzwert (etwa $1{,}014$) muss man für das Cauchy-Kriterium aber gar nicht kennen.

Für $m > n \geq 1$ gilt wegen $|\sin(k)| \leq 1$ und $\frac{1}{k^2} \leq \frac{1}{k(k-1)} = \frac{1}{k-1} - \frac{1}{k}$:

\begin{align}
|a_m - a_n| &= \left| \sum_{k=n+1}^m \frac{\sin(k)}{k^2} \right|
             \leq \sum_{k=n+1}^m \frac{1}{k^2}
             \leq \sum_{k=n+1}^m \left( \frac{1}{k-1} - \frac{1}{k} \right) \\
            &= \frac{1}{n} - \frac{1}{m} < \frac{1}{n}
\end{align}

(Die Summe in der Mitte ist eine Teleskopsumme: Bis auf den ersten und den letzten Term heben sich alle Terme weg.)

Sei nun $\varepsilon > 0$ und $n_0 \in \mathbb{N}$ mit $n_0 \geq \frac{1}{\varepsilon}$. Dann gilt für alle $m > n > n_0$ (für $n > m$ vertauscht man die Rollen, für $m = n$ ist $|a_m - a_n| = 0$):
$|a_m - a_n| < \frac{1}{n} < \frac{1}{n_0} \leq \varepsilon$

$(a_n)_{n \in \mathbb{N}}$ ist also eine Cauchy-Folge in $\mathbb{R}$ und konvergiert damit.</div>

<h2>Weiteres</h2>

Bei Polynomen darf man den "Ausklammer-Trick" nicht vergessen:
$a_n = \frac{3 \cdot n^5 + 2 \cdot n^2 + 42}{1000 \cdot n^5 + n^3} = \frac{n^5}{n^5} \cdot \frac{3 + 2 \cdot \frac{1}{n^3} + 42 \cdot \frac{1}{n^5}}{1000 + \frac{1}{n^2}}= \frac{3 + 2 \cdot \frac{1}{n^3} + 42 \cdot \frac{1}{n^5}}{1000 + \frac{1}{n^2}}$

Das sieht zwar deutlich schlimmer aus als vorher, ist aber besser. Wir wissen, dass $\displaystyle \lim_{n \rightarrow \infty} \frac{1}{n} = 0$ gilt. Also gilt:

$\displaystyle a_n \xrightarrow{n \rightarrow \infty} \frac{3 + 2 \cdot \overbrace{\frac{1}{n^3}}^{\rightarrow 0} + 42 \cdot \overbrace{\frac{1}{n^5}}^{\rightarrow 0}}{1000 + \underbrace{\frac{1}{n^2}}_{\rightarrow 0}} = \frac{3}{1000}$
