---
layout: post
title: Einführung in die abzählende Kombinatorik
slug: einfuhrung-in-die-abzahlende-kombinatorik
lang: de
author: Martin Thoma
date: 2011-10-24 20:53:41.000000000 +02:00
category: German posts
tags: mathematics, lecture-notes
featured_image: 2011/10/eulers-formula.png
---
Die abzählende Kombinatorik beschäftigt sich mit der Bestimmung der Anzahl möglicher Anordnungen oder Auswahlen.

<h2>Begriffe</h2>
<h3>Permutation</h3>
Eine Permutation ist eine Veränderung der Reihenfolge einer geordneten Anzahl von Objekten. <small>(Weil die Objekte in irgend einer Art geordnet sein müssen, damit sich eine Reihenfolge ändern kann, will ich diese Ansammlung nicht "Menge" nennen.)</small>

Beispiel:
Wir haben eine Liste von Zahlen: [1, 2, 5, -7, -1, 3]
Eine Permutation davon ist: [1, 2, 5, -7, 3, -1]

Anagramme sind Permutationen: "ANGSTBUDE" und "BUNDESTAG"

Das Wesentliche ist also, dass es bei Permutationen auf die Reihenfolge ankommt.

<h3>k-Permutation</h3>
Eine k-Permutation wählt aus n Objekten k aus.

Wenn wir also die 6 Objekte [1, 2, 5, -7, -1, 3] haben, wären [1, 2, 5], [5, 2, 1], [-7, 2, 3] und [-7, 3, 3] verschiedene 3-Permutationen davon.

<h3>Kombination und k-Kombination</h3>
Bei einer Kombination kommt es <em>nicht</em> auf die Reihenfolge an. Sonst ist alles analog zu den Permutationen.

<h2>Formeln</h2>
Es gibt nur vier Formeln, die man sich merken sollte. Dabei sei n die Anzahl aller wählbaren Objekte:

<table>
<tr><th>&nbsp;</th><th>mit Wiederholungen</th><th>ohne Wiederholungen</th></tr>
<tr><th>k-Permutation</th><td>$n^k$</td><td>$\frac{n!}{(n-k)!}$</td></tr>
<tr><th>k-Kombination</th><td>$\binom{n-1+k}{k}$</td><td>$\binom{n}{k}$</td></tr>
</table>

Warum stimmt das?

Wenn man n Objekte hat und k-mal eines davon auswählt, wobei die Reihenfolge eine Rolle spielt und man das Objekt danach immer wieder zurück legt (also Wiederholungen haben kann), dann hat man beim ersten mal n verschiedene Wahlmöglichkeiten. Beim zweiten, dritten, ... k.-Zug auch. Es sind also $\underbrace{n \cdot n \cdot ... \cdot n}_\text{k mal} = n^k$ Möglichkeiten.

Wenn man die Objekte nicht wieder zurück legt, die Reihenfolge aber eine Rolle spielt, hat man beim ersten Zug wieder n Möglichkeiten. Beim zweiten Zug sind es (n-1), beim dritten (n-3), ... beim k.-Zug (n-k+1) Möglichkeiten. Also gilt:
$\underbrace{(n-0) \cdot (n-1) \cdot ... \cdot (n- (k-1))}_\text{k Faktoren} = \prod_{i=0}^{k-1} (n-i)=  \frac{n!}{(n-k)!}$

Angenommen es spielt nun nur eine Rolle, welche Objekte man ausgewählt hat, aber nicht wann. Dann gibt es, wenn man die Objekte nicht wieder zurücklegt, $\frac{n!}{(n-k)!}$ Möglichkeiten, abzüglich der Möglichkeiten, die nur bei Beachtung der Reihenfolge eine Rolle spielen. Das bedeutet, es muss noch durch k! geteilt werden. Das kann man sich klar machen, indem man eine bestimmte Menge an k ausgewählten Objekten betrachtet. Dann muss man entscheiden, welches das erste ist. Dafür gibt es k Möglichkeiten. Für das zweite hat man (k-1) Möglichkeiten, usw. Das Bedeutet, es gibt für diesen Fall $\frac{n!}{(n-k)! \cdot k!} = \binom{n}{k}$ Möglichkeiten.

Der schwerste Fall sind k-Kombinationen mit zurücklegen. Dafür denkt man sich am besten, dass man eine Liste der Objekte hat. Nun macht man, um die n Objekte zu trennen, zwischen diese (n-1) Sternchen. Die Anzahl wird durch k Striche repräsentiert.
Nun kann man sich fragen, wie viele Möglichkeiten es gibt diese k Striche und (n-1) Sternchen anzuordnen.  Das sind, wenn man die k Striche auf (n-1)+k Plätze verteilt:
$\frac{(n-1+k)!}{(n-1)!} \cdot \underbrace{\frac{1}{k!}}_\text{Reihenfolge ist egal} = \frac{(n-1+k)!}{(n-1)!k!}$

Dies entspricht genau dem Binomialkoeffizienten:
$\binom{n-1+k}{k} = \frac{(n-1+k)!}{k!((n-1+k)-k)!} = \frac{(n-1+k)!}{k!(n-1)!}$

<h2>Siehe auch</h2>
Wikipedia:
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Kombinatorik">Kombinatorik</a> (Der Artikel ist leider sehr mager. Eventuell hat jemand lust ihn zu ergänzen?)</li>
  <li><a href="http://de.wikipedia.org/wiki/Abz%C3%A4hlende_Kombinatorik">Abzählende Kombinatorik</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Permutation">Permutation</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Anagramm">Anagramm</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Binomialkoeffizient">Binomialkoeffizient</a></li>
</ul>
