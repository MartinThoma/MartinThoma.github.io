---
layout: post
title: Einführung in die Affine Geometrie
author: Martin Thoma
date: 2012-08-31 03:43:19
categories: 
- German posts
tags: 
- Affine geometry
featured_image: 2012/01/vector-space.png
---
Ich habe mir seit zwei Tagen versucht klar zu machen, was bestimmte Grundbegriffe der affinen Geometrie überhaupt bedeuten. Im Folgenden werde ich die formalen Definitionen aus dem Skript von Herrn Prof. Dr. Leuzinger geben und versuchen das ganze verständlich zu erklären. Sehr ähnliche Definitionen sind übrigens in dieser <a href="http://www.math.hu-berlin.de/~kramer/laag-scr.pdf">Mitschrift zur Vorlesung Lineare Algebra und analytische Geometrie der HU-Berlin</a> zu finden.

<h2>Operation</h2>
<div class="definition">Eine <strong>Operation</strong> einer Gruppe $(G, \cdot)$ auf einer Menge X ist eine Abbildung
$\varphi: G \times X \rightarrow X; ~~~ (g, x) \mapsto \varphi(g, x)$,
die folgende Eigenschaften besitzt:
<ul>
  <li>Ist $e$ das neutrale Element von $G$, so gilt $\varphi(e, x) = x$ für alle $x \in X$</li>
  <li>Für alle $g, h \in G$ und alle $x \in X$ gilt $\varphi(g \cdot h, x) = \varphi(g, \varphi(h,x))$.</li>
</ul></div>

<h3>Verschiebung</h3>
Sei $X$ die Menge aller Punkte $(x, y) \in \mathbb{R^2}$ und $(G, \circ)$ eine Verschiebung. Das neutrale Element von $G$ ist $(0,0)$.
Die Abbildung $\varphi: G \times X \rightarrow X$ sei definiert durch
$((x,y), (a,b)) \mapsto (a+x, b+y)$.

Erste Eigenschaft: $\varphi((0,0), (a, b)) = (a+0, b+0) = (a,b)$ gilt offensichtlich.
Zweite Eigenschaft: ist gilt genauso offensichtlich:
$\begin{align}
  &\varphi((x_1, y_1) \circ (x_2, y_2), (a,b))\\
= &\varphi((x_1, y_1), \varphi((x_2, y_2), (a,b)))\\ 
= &\varphi((x_1, y_1), (a+x_2, b+y_2))\\
= &(a+x_1+x_2,b+y_1+y_2)
\end{align}$ 

Was hat man hier also? Eine Operation ist eine Gruppe von Vorgängen, die auf einige Elemente angewendet werden können. Es ist in gewisser weise das <a href="http://de.wikipedia.org/wiki/Strategie_(Entwurfsmuster)">Strategie-Entwurfsmuster</a>. Keine Verschiebung macht genau das gleiche und auf verschiedene Elemente angewant bekommt man verschiedene Ergebnisse (bzw. kann verschiedene Ergebnisse bekommen).

<h3>Schachzug</h3>
Gehen wir mal von einer vereinfachten Schachversion aus, bei der immer nur eine einzelne <a href="http://de.wikipedia.org/wiki/Dame_(Schach)">Dame</a> auf einem unendlich großem Schachbrett betrachte. Das Schachbrett wird durch den $\mathbb{Z}^2$ repräsentiert, entsprechend sind die Positionen ganzzahlige Tupel.

Die Gruppe $(G, \circ)$ beinhaltet Züge, also 
$\begin{align}
G =     &\{(x|x)   | x \in \mathbb{Z}\}\\
\cup    &\{(x|-x)  | x \in \mathbb{Z}\}\\ 
\cup    &\{(x|0)   | x \in \mathbb{Z}\}\\
\cup    &\{(0|x)   | x \in \mathbb{Z}\}
\end{align}$

Das neutrale Element von $G$ ist natürlich wieder kein Zug, also $(0|0)$.
Die beiden Eigenschaften folgen wieder ganz direkt.

<h2>Bahn</h2>
<div class="definition">Die <strong>Bahn</strong> eines Punktes $x \in X$ bzgl. $\varphi$ ist die Menge $\{\varphi(g,x) \subset X | g \in G\}$.</div>

<h3>Verschiebung</h3>
Die Bahn jedes Punktes ist wieder der gesamte $\mathbb{R}^2$. Es gibt also genau eine Bahn, die jeder Punkt $x \in X$ hat.

<h3>Schachzug</h3>
Hier gibt es verschiedene Bahnen, je nach dem Startpunkt. Genauer gesagt gilt: Für jeden Punkt $x \in X$ gibt es eine eigene Bahn. Man kann sich das schnell klar machen, wenn man sich überlegt, ob zwei Damen an unterschiedlichen Punkten <em>genau</em> die gleichen Felder erreichen können. Das können sie offensichtlich nicht.

<h2>Transitive Operation</h2>
<div class="definition">Eine Gruppen-Operation heißt <strong>transitiv</strong>, wenn es genau eine Bahn gibt.</div>

Wie schon oben erläutert, hat die Verschiebung genau eine Bahn. Sie ist also eine transitive Operation. Im Gegensatz zum Schachzug.

<h2>Stabilisator</h2>
<div class="definition">Der <strong>Stabilisator</strong> von $x \in X$ bzgl. $\varphi$ ist die Untergruppe $G_x := \{g \in G | \varphi(g, x) = x\}$ von G.</div>

Der Stabilisator ist sozusagen das neutrale Element der Gruppenoperation

<h3>Verschiebung und Schachzug</h3>
Jedes Element $x \in X$ hat den gleichen Stabilisator $\{(0,0)\}$.