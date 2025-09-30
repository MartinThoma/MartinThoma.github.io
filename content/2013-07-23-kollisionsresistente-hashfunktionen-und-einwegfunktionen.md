---
layout: post
lang: de
title: Kollisionsresistente Hashfunktionen und Einwegfunktionen
slug: kollisionsresistente-hashfunktionen-und-einwegfunktionen
author: Martin Thoma
date: 2013-07-23 10:05:24.000000000 +02:00
category: German posts
tags: IT-Security
featured_image: 2013/04/cryptography-thumb.png
---
<h2>Definitionen</h2>
<div class="definition">
Sei $f:X \rightarrow Y$ eine Funktion.
$f$ heißt eine Einwegfunktion, genau dann wenn für alle $x \in X$ gilt:
<ul>
  <li>$y := f(x)$ kann in Polynomialzeit berechnet werden</li>
  <li>Für die Berechnung eines Urbildes $x$ aus $y$ existiert kein randomisierter Algorithmus, der in Polynomialzeit läuft.</li>
</ul>
</div>

<div class="definition">
Eine Funktion $H:\{0,1\}^* \rightarrow \{0,1\}^k$ heißt <strong>kollisionsresistente Hashfunktion</strong>, wenn gilt:

Jeder effiziente Algorithmus findet nur mit kleiner Wahrscheinlichkeit eine Kollision.
</div>

Was heißt &bdquo;kleine Wahrscheinlichkeit&ldquo;?
Nach dem Auswerten der Funktion $H$ für $x_1, x_2, \dots x_n$ sollte die Wahrscheinlichkeit nicht signifikant höher sein als $\displaystyle 1-\frac{n!\cdot{{2^k} \choose n}}{{2^k}^n}$
Diese Wahrscheinlichkeit kommt von dem <a href="http://de.wikipedia.org/wiki/Geburtstagsparadoxon">Geburtstagsparadoxon</a> bzw. dem <a href="http://de.wikipedia.org/wiki/Schubfachprinzip">Schubfachprinzip</a>. Wir haben $2^k$ Schubfächer (Funktionswerte) in die wir die $x_i$ (Urbilder) einordnen können.

<h2>Satz</h2>
<strong>Behauptung</strong>: Jede kollisionsresistente Hashfunktion ist eine Einwegfunktion.
<strong>Beweis</strong>: durch Widerspruch
Sei $f$ eine kollisionsresistente Hashfunktion
<u>Annahme</u>: $f$ ist keine Einwegfunktion

Dann existiert ein Angreifer $\mathcal{A}$, der für eine Bild $f(x)$ ein $x'$ findet, sodass $f(x) = f(x')$ gilt.

Der Angreifer $\mathcal{B}$ macht nichts anderes, als zufällig Werte $x \in \{0,1\}^{2k}$ zu wählen, $f(x)$ zu berechnen, den Angreifer $\mathcal{A}$ auf $f(x)$ anzuwenden und zu überprüfen, ob das von $\mathcal{A}$ gelieferte $x' \neq x$ ist. Sobald das ein mal der Fall ist, hat der Angreifer gewonnen.

Nun wenden wir $f$ auf $x \in \{0,1\}^{2k}$ an. Es gilt:

$Pr_x[\underbrace{|f^{-1}(f(x))|}_{\substack{\text{Anzahl der Urbilder}\\\text{zum Hashwert} f(x)} } = 1] \leq \frac{2^k}{2^{2k}} = \frac{1}{2^k}$.

Die $2^k$ im Zähler stehen für die Funktionswerte und die $2^{2k}$ für die Urbilder.

Nun ist $\frac{1}{2^k}$ eine vernachlässigbare Funktion.

$\Rightarrow$ Die Wahrscheinlichkeit, dass wir keine Kollsion finden ist vernachlässigbar.

$\Rightarrow$ Mit signifikanter Wahrscheinlichkeit hat $f(x)$ $k \geq 2$ Urbilder.

$\Rightarrow$ Die Wahrscheinlichkeit, dass $\mathcal{B}$ Kollisionen findet ist etwa $(1-\frac{1}{k}) \cdot m$, wobei $m$ die Anzahl der Widerholungen ist.
