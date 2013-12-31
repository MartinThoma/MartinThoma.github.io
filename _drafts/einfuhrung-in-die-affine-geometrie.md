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
<div class="definition">Eine <strong>Operation</strong> einer Gruppe [latex](G, \cdot)[/latex] auf einer Menge X ist eine Abbildung
[latex]\varphi: G \times X \rightarrow X; ~~~ (g, x) \mapsto \varphi(g, x)[/latex],
die folgende Eigenschaften besitzt:
<ul>
  <li>Ist [latex]e[/latex] das neutrale Element von [latex]G[/latex], so gilt [latex]\varphi(e, x) = x[/latex] für alle [latex]x \in X[/latex]</li>
  <li>Für alle [latex]g, h \in G[/latex] und alle [latex]x \in X[/latex] gilt [latex]\varphi(g \cdot h, x) = \varphi(g, \varphi(h,x))[/latex].</li>
</ul></div>

<h3>Verschiebung</h3>
Sei [latex]X[/latex] die Menge aller Punkte [latex](x, y) \in \mathbb{R^2}[/latex] und [latex](G, \circ)[/latex] eine Verschiebung. Das neutrale Element von [latex]G[/latex] ist [latex](0,0)[/latex].
Die Abbildung [latex]\varphi: G \times X \rightarrow X[/latex] sei definiert durch
[latex]((x,y), (a,b)) \mapsto (a+x, b+y)[/latex].

Erste Eigenschaft: [latex]\varphi((0,0), (a, b)) = (a+0, b+0) = (a,b)[/latex] gilt offensichtlich.
Zweite Eigenschaft: ist gilt genauso offensichtlich:
[latex]\begin{align}
  &\varphi((x_1, y_1) \circ (x_2, y_2), (a,b))\\
= &\varphi((x_1, y_1), \varphi((x_2, y_2), (a,b)))\\ 
= &\varphi((x_1, y_1), (a+x_2, b+y_2))\\
= &(a+x_1+x_2,b+y_1+y_2)
\end{align}[/latex] 

Was hat man hier also? Eine Operation ist eine Gruppe von Vorgängen, die auf einige Elemente angewendet werden können. Es ist in gewisser weise das <a href="http://de.wikipedia.org/wiki/Strategie_(Entwurfsmuster)">Strategie-Entwurfsmuster</a>. Keine Verschiebung macht genau das gleiche und auf verschiedene Elemente angewant bekommt man verschiedene Ergebnisse (bzw. kann verschiedene Ergebnisse bekommen).

<h3>Schachzug</h3>
Gehen wir mal von einer vereinfachten Schachversion aus, bei der immer nur eine einzelne <a href="http://de.wikipedia.org/wiki/Dame_(Schach)">Dame</a> auf einem unendlich großem Schachbrett betrachte. Das Schachbrett wird durch den [latex]\mathbb{Z}^2[/latex] repräsentiert, entsprechend sind die Positionen ganzzahlige Tupel.

Die Gruppe [latex](G, \circ)[/latex] beinhaltet Züge, also 
[latex]\begin{align}
G =     &\{(x|x)   | x \in \mathbb{Z}\}\\
\cup    &\{(x|-x)  | x \in \mathbb{Z}\}\\ 
\cup    &\{(x|0)   | x \in \mathbb{Z}\}\\
\cup    &\{(0|x)   | x \in \mathbb{Z}\}
\end{align}[/latex]

Das neutrale Element von [latex]G[/latex] ist natürlich wieder kein Zug, also [latex](0|0)[/latex].
Die beiden Eigenschaften folgen wieder ganz direkt.

<h2>Bahn</h2>
<div class="definition">Die <strong>Bahn</strong> eines Punktes [latex]x \in X[/latex] bzgl. [latex]\varphi[/latex] ist die Menge [latex]\{\varphi(g,x) \subset X | g \in G\}[/latex].</div>

<h3>Verschiebung</h3>
Die Bahn jedes Punktes ist wieder der gesamte [latex]\mathbb{R}^2[/latex]. Es gibt also genau eine Bahn, die jeder Punkt [latex]x \in X[/latex] hat.

<h3>Schachzug</h3>
Hier gibt es verschiedene Bahnen, je nach dem Startpunkt. Genauer gesagt gilt: Für jeden Punkt [latex]x \in X[/latex] gibt es eine eigene Bahn. Man kann sich das schnell klar machen, wenn man sich überlegt, ob zwei Damen an unterschiedlichen Punkten <em>genau</em> die gleichen Felder erreichen können. Das können sie offensichtlich nicht.

<h2>Transitive Operation</h2>
<div class="definition">Eine Gruppen-Operation heißt <strong>transitiv</strong>, wenn es genau eine Bahn gibt.</div>

Wie schon oben erläutert, hat die Verschiebung genau eine Bahn. Sie ist also eine transitive Operation. Im Gegensatz zum Schachzug.

<h2>Stabilisator</h2>
<div class="definition">Der <strong>Stabilisator</strong> von [latex]x \in X[/latex] bzgl. [latex]\varphi[/latex] ist die Untergruppe [latex]G_x := \{g \in G | \varphi(g, x) = x\}[/latex] von G.</div>

Der Stabilisator ist sozusagen das neutrale Element der Gruppenoperation

<h3>Verschiebung und Schachzug</h3>
Jedes Element [latex]x \in X[/latex] hat den gleichen Stabilisator [latex]\{(0,0)\}[/latex].