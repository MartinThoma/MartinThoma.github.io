---
layout: post
lang: de
title: Wie zeige ich Differenzierbarkeit?
author: Martin Thoma
date: 2012-12-05 11:59:08.000000000 +01:00
category: German posts
tags: mathematics, analysis
featured_image: 2012/12/ableitung-definition.png
---
Weil das Thema so wichtig ist und man es doch recht leicht vergisst:

<div class="definition">Sei $I \subseteq \mathbb{R}$ ein Intervall und $f:I \rightarrow \mathbb{R}$ eine Funktion.

<ol>
<li>$f$ hei&szlig;t in $x_0 \in I$ <strong>differenzierbar</strong> $\displaystyle  :\Leftrightarrow \lim_{x \rightarrow x_0} \frac{f(x) - f(x_0)}{x-x_0}$ existiert und ist in $\mathbb{R}$.<br/>
In diesem Fall hei&szlig;t $\displaystyle f'(x_0) = \lim_{x \rightarrow x_0} \frac{f(x) - f(x_0)}{x-x_0}$ die <strong>Ableitung von $f$ in $x_0$</strong>.</li>
<li>$f$ hei&szlig;t auf $I$ differenzierbar $:\Leftrightarrow \forall x \in I: f \text{ ist in } x$ differenzierbar.<br/>
In diesem Fall wird durch $x \mapsto f'(x)$ eine Funktion $f':I \rightarrow \mathbb{R}$ definiert, die <strong>Ableitung</strong> von $f$ auf $I$.</li>
</ol>
</div>

Und wie zeigt man die Existenz dieses Grenzwertes? Das ist eine andere Frage :-P Man sollte sich vielleicht nochmal den Artikel <a href="../konvergenz-von-folgen/">Konvergenz von Folgen</a> bzw. <a href="../konvergenz-von-reihen/">Konvergenz von Reihen</a> anschauen.

Ach ja, man kann auch zeigen, dass $\displaystyle \lim_{h \rightarrow 0} \frac{f(x_0+h)-f(x_0)}{h}$ existiert und in $\mathbb{R}$ ist. Das ist &auml;quivalent.
