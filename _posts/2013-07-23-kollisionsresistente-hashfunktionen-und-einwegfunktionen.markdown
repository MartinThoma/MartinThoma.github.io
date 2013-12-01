---
layout: post
status: publish
published: true
title: Kollisionsresistente Hashfunktionen und Einwegfunktionen
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 74821
wordpress_url: http://martin-thoma.com/?p=74821
date: 2013-07-23 10:05:24.000000000 +02:00
categories:
- German posts
tags:
- IT-Security
comments: []
featured_image: 2013/04/cryptography-thumb.png
---
<h2>Definitionen</h2>
<div class="definition">
Sei $f:X \rightarrow Y$ eine Funktion.
$f$ hei&szlig;t eine Einwegfunktion, genau dann wenn f&uuml;r alle $x \in X$ gilt:
<ul>
  <li>$y := f(x)$ kann in Polynomialzeit berechnet werden</li>
  <li>F&uuml;r die Berechnung eines Urbildes $x$ aus $y$ existiert kein randomisierter Algorithmus, der in Polynomialzeit l&auml;uft.</li>
</ul>
</div>

<div class="definition">
Eine Funktion $H:\{0,1\}^* \rightarrow \{0,1\}^k$ hei&szlig;t <strong>kollisionsresistente Hashfunktion</strong>, wenn gilt:

Jeder effiziente Algorithmus findet nur mit kleiner Wahrscheinlichkeit eine Kollision. 
</div>

Was hei&szlig;t &bdquo;kleine Wahrscheinlichkeit&ldquo;?
Nach dem Auswerten der Funktion $H$ f&uuml;r $x_1, x_2, \dots x_n$ sollte die Wahrscheinlichkeit nicht signifikant h&ouml;her sein als {% raw %}$\displaystyle 1-\frac{n!\cdot{{2^k} \choose n}}{{2^k}^n}${% endraw %}
Diese Wahrscheinlichkeit kommt von dem <a href="http://de.wikipedia.org/wiki/Geburtstagsparadoxon">Geburtstagsparadoxon</a> bzw. dem <a href="http://de.wikipedia.org/wiki/Schubfachprinzip">Schubfachprinzip</a>. Wir haben $2^k$ Schubf&auml;cher (Funktionswerte) in die wir die $x_i$ (Urbilder) einordnen k&ouml;nnen.

<h2>Satz</h2>
<strong>Behauptung</strong>: Jede kollisionsresistente Hashfunktion ist eine Einwegfunktion.
<strong>Beweis</strong>: durch Widerspruch
Sei $f$ eine kollisionsresistente Hashfunktion
<u>Annahme</u>: $f$ ist keine Einwegfunktion

Dann existiert ein Angreifer $\mathcal{A}$, der f&uuml;r eine Bild $f(x)$ ein $x'$ findet, sodass $f(x) = f(x')$ gilt.

Der Angreifer $\mathcal{B}$ macht nichts anderes, als zuf&auml;llig Werte $x \in \{0,1\}^{2k}$ zu w&auml;hlen, $f(x)$ zu berechnen, den Angreifer $\mathcal{A}$ auf $f(x)$ anzuwenden und zu &uuml;berpr&uuml;fen, ob das von $\mathcal{A}$ gelieferte $x' \neq x$ ist. Sobald das ein mal der Fall ist, hat der Angreifer gewonnen.

Nun wenden wir $f$ auf $x \in \{0,1\}^{2k}$ an. Es gilt:

$Pr_x[\underbrace{|f^{-1}(f(x))|}_{\substack{\text{Anzahl der Urbilder}\\\text{zum Hashwert} f(x)} } = 1] \leq \frac{2^k}{2^{2k}} = \frac{1}{2^k}$.

Die $2^k$ im Z&auml;hler stehen f&uuml;r die Funktionswerte und die $2^{2k}$ f&uuml;r die Urbilder.

Nun ist $\frac{1}{2^k}$ eine vernachl&auml;ssigbare Funktion.

$\Rightarrow$ Die Wahrscheinlichkeit, dass wir keine Kollsion finden ist vernachl&auml;ssigbar.

$\Rightarrow$ Mit signifikanter Wahrscheinlichkeit hat $f(x)$ $k \geq 2$ Urbilder.

$\Rightarrow$ Die Wahrscheinlichkeit, dass $\mathcal{B}$ Kollisionen findet ist etwa $(1-\frac{1}{k}) \cdot m$, wobei $m$ die Anzahl der Widerholungen ist.
