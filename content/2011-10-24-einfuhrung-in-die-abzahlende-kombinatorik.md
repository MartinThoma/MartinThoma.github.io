---
layout: post
lang: de
title: Einf&uuml;hrung in die abz&auml;hlende Kombinatorik
slug: einfuhrung-in-die-abzahlende-kombinatorik
author: Martin Thoma
date: 2011-10-24 20:53:41.000000000 +02:00
category: German posts
tags: mathematics, lecture-notes
featured_image: 2011/10/eulers-formula.png
---
Die abz&auml;hlende Kombinatorik besch&auml;ftigt sich mit der Bestimmung der Anzahl m&ouml;glicher Anordnungen oder Auswahlen.

<h2>Begriffe</h2>
<h3>Permutation</h3>
Eine Permutation ist eine Ver&auml;nderung der Reihenfolge einer geordneten Anzahl von Objekten. <small>(Weil die Objekte in irgend einer Art geordnet sein m&uuml;ssen, damit sich eine Reihenfolge &auml;ndern kann, will ich diese Ansammlung nicht "Menge" nennen.)</small>

Beispiel:
Wir haben eine Liste von Zahlen: [1, 2, 5, -7, -1, 3]
Eine Permutation davon ist: [1, 2, 5, -7, 3, -1]

Anagramme sind Permutationen: "ANGSTBUDE" und "BUNDESTAG"

Das Wesentliche ist also, dass es bei Permutationen auf die Reihenfolge ankommt.

<h3>k-Permutation</h3>
Eine k-Permutation w&auml;hlt aus n Objekten k aus.

Wenn wir also die 6 Objekte [1, 2, 5, -7, -1, 3] haben, w&auml;ren [1, 2, 5], [5, 2, 1], [-7, 2, 3] und [-7, 3, 3] verschiedene 3-Permutationen davon.

<h3>Kombination und k-Kombination</h3>
Bei einer Kombination kommt es <em>nicht</em> auf die Reihenfolge an. Sonst ist alles analog zu den Permutationen.

<h2>Formeln</h2>
Es gibt nur vier Formeln, die man sich merken sollte. Dabei sei n die Anzahl aller w&auml;hlbaren Objekte:

<table>
<tr><th>&nbsp;</th><th>mit Wiederholungen</th><th>ohne Wiederholungen</th></tr>
<tr><th>k-Permutation</th><td>$n^k$</td><td>$\frac{n!}{(n-k)!}$</td></tr>
<tr><th>k-Kombination</th><td>$\binom{n-1+k}{k}$</td><td>$\binom{n}{k}$</td></tr>
</table>

Warum stimmt das?

Wenn man n Objekte hat und k-mal eines davon ausw&auml;hlt, wobei die Reihenfolge eine Rolle spielt und man das Objekt danach immer wieder zur&uuml;ck legt (also Wiederholungen haben kann), dann hat man beim ersten mal n verschiedene Wahlm&ouml;glichkeiten. Beim zweiten, dritten, ... k.-Zug auch. Es sind also $\underbrace{n \cdot n \cdot ... \cdot n}_\text{k mal} = n^k$ M&ouml;glichkeiten.

Wenn man die Objekte nicht wieder zur&uuml;ck legt, die Reihenfolge aber eine Rolle spielt, hat man beim ersten Zug wieder n M&ouml;glichkeiten. Beim zweiten Zug sind es (n-1), beim dritten (n-3), ... beim k.-Zug (n-k+1) M&ouml;glichkeiten. Also gilt:
$\underbrace{(n-0) \cdot (n-1) \cdot ... \cdot (n- (k-1))}_\text{k Faktoren} = \prod_{i=0}^{k-1} (n-i)=  \frac{n!}{(n-k)!}$

Angenommen es spielt nun nur eine Rolle, welche Objekte man ausgew&auml;hlt hat, aber nicht wann. Dann gibt es, wenn man die Objekte nicht wieder zur&uuml;cklegt, $\frac{n!}{(n-k)!}$ M&ouml;glichkeiten, abz&uuml;glich der M&ouml;glichkeiten, die nur bei Beachtung der Reihenfolge eine Rolle spielen. Das bedeutet, es muss noch durch k! geteilt werden. Das kann man sich klar machen, indem man eine bestimmte Menge an k ausgew&auml;hlten Objekten betrachtet. Dann muss man entscheiden, welches das erste ist. Daf&uuml;r gibt es k M&ouml;glichkeiten. F&uuml;r das zweite hat man (k-1) M&ouml;glichkeiten, usw. Das Bedeutet, es gibt f&uuml;r diesen Fall $\frac{n!}{(n-k)! \cdot k!} = \binom{n}{k}$ M&ouml;glichkeiten.

Der schwerste Fall sind k-Kombinationen mit zur&uuml;cklegen. Daf&uuml;r denkt man sich am besten, dass man eine Liste der Objekte hat. Nun macht man, um die n Objekte zu trennen, zwischen diese (n-1) Sternchen. Die Anzahl wird durch k Striche repr&auml;sentiert.
Nun kann man sich fragen, wie viele M&ouml;glichkeiten es gibt diese k Striche und (n-1) Sternchen anzuordnen.  Das sind, wenn man die k Striche auf (n-1)+k Pl&auml;tze verteilt:
$\frac{(n-1+k)!}{(n-1)!} \cdot \underbrace{\frac{1}{k!}}_\text{Reihenfolge ist egal} = \frac{(n-1+k)!}{(n-1)!k!}$

Dies entspricht genau dem Binomialkoeffizienten:
$\binom{n-1+k}{k} = \frac{(n-1+k)!}{k!((n-1+k)-k)!} = \frac{(n-1+k)!}{k!(n-1)!}$

<h2>Siehe auch</h2>
Wikipedia:
<ul>
  <li><a href="http://de.wikipedia.org/wiki/Kombinatorik">Kombinatorik</a> (Der Artikel ist leider sehr mager. Eventuell hat jemand lust ihn zu erg&auml;nzen?)</li>
  <li><a href="http://de.wikipedia.org/wiki/Abz%C3%A4hlende_Kombinatorik">Abz&auml;hlende Kombinatorik</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Permutation">Permutation</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Anagramm">Anagramm</a></li>
  <li><a href="http://de.wikipedia.org/wiki/Binomialkoeffizient">Binomialkoeffizient</a></li>
</ul>
