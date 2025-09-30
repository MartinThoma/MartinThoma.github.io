---
layout: post
lang: de
title: Pr&auml;dikatenlogik: Aussagen formalisieren
slug: pradikatenlogik-aussagen-formalisieren
author: Martin Thoma
date: 2011-10-29 15:12:33.000000000 +02:00
category: German posts
tags: mathematics, lecture-notes
featured_image: 2011/10/eulers-formula.png
---
Es ist h&auml;ufig von Vorteil, wenn man Aussagen formalisieren kann. Es ist beispielsweise gar nicht so leicht das exakte Gegenteil einer Aussage zu finden.

<h2>Allgemeines zur Pr&auml;dikatenlogik</h2>
x sei im folgenden eine Aussage
$\neg x$: Die Negation der Aussage x

$\exists x$: Es existiert mindestens ein x (Quantor)
$\forall x$: Alle x (Quantor)

$\land$: und (eine Verkn&uuml;fung zweier Aussagen)
$\lor$: oder (eine Verkn&uuml;fung zweier Aussagen). Im Deutschen wird oder meistens exklusiv, also im Sinne "entweder ... oder ..." verwendet. Dieses oder ist inklusiv, also "entweder ... oder ... oder beides".

Ich habe die Symbole bewusst in diesen Paragraphen angeordnet. Wird die Negation eines Ausdrucks gebildet, werden alle Symbole im Inneren durch das jeweils andere Symbol ersetzt. Beispielsweise wird das logische "und" zu einem "oder".

Ein kleiner Nachtrag: Was macht man, wenn man sagen will, dass eine Aussage A f&uuml;r genau ein Element x einer Menge M gilt?
$\exists x \in M: A(x) \land \forall (y \in M, y \neq x): \neg A(y)$

<h2>Karlsruher und die Verkehrsmittel</h2>
Folgendes Beispiel hatte ich in einem Tutorium am KIT:
<blockquote>(i) Alle Karlsruher fahren mit dem Rad oder der Stra&szlig;enbahn.</blockquote>
Was ist das Gegenteil dieser Aussage? Folgendes w&auml;re denkbar:
<ol>
	<li>Kein Karlsruher f&auml;hrt mit dem Rad oder der Stra&szlig;enbahn.</li>
	<li>Kein Karlsruher f&auml;hrt mit dem Rad und der Stra&szlig;enbahn.</li>
	<li>Alle Karlsruher fahren mit dem Rad und der Stra&szlig;enbahn.</li>
	<li>Alle Karlsruher fahren nicht mit dem Rad und der Stra&szlig;enbahn.</li>
	<li>Es fahren nicht alle Karlsruher mit dem Rad oder der Stra&szlig;enbahn.</li>
        <li>Es fahren nicht alle Karlsruher mit dem Rad und der Stra&szlig;enbahn.</li>
        <li>...</li>
</ol>
Nun wurde mir beigebracht, dass folgendes eine "saubere" Formalisierung der ersten Aussage ist:

Sei K die Menge aller Karlsruher.
Sei F Aussageform auf K und definiert durch $F(k) := \text{"k f&auml;hrt mit dem Fahrrad"} (k \in K)$
Sei analog S Aussageform auf K mit $S(k) := \text{"k f&auml;hrt mit der Stra&szlig;enbahn"}$

Dann lautet (i) formalisiert:
$\forall k \in K: F(k) \lor S(k)$ <small>(sprich: "F&uuml;r alle k in K gilt: F von k oder S von k")</small>

Negiert:
$\exists k \in K: \neg F(k) \land \neg S(k)$ <small>(sprich: "Es existiert mindestens ein k in K f&uuml;r das gilt: Es ist F von k nicht wahr und zugleich S von k nicht wahr.")</small>

&Uuml;bersetzt man das in einen sch&ouml;neren deutschen Satz kann man sagen:
Mindestens ein Karlsruher f&auml;hrt weder mit dem Rad noch mit der Bahn.

Wenn man das nun auf die oben angegebenen L&ouml;sungen bezieht, k&ouml;nnte es Aussage 5 oder 6 sein. Der Sinngem&auml;&szlig; muss es hei&szlig;en:
Es fahren nicht alle Karlsruher entweder mit dem Rad, der Stra&szlig;enbahn oder beidem.
Ich tendiere stark dazu, Satz 5 zu nehmen. Allerdings bin ich mir nicht sicher, ob mein Sprachgef&uuml;hl mich t&auml;uscht.

<h2>W&ouml;chentliches Fernsehprogramm</h2>
Noch ein Beispiel aus meinem Tutorium:
<blockquote>(ii) Im Fernsehen l&auml;uft jede Woche "Die Simpsons", "Die Ludolfs" und "Telekolleg".</blockquote>

Sei W die Menge aller Wochen.
Sei A Aussageform auf W.

A(w) := In der Woche w l&auml;uft "Die Simpsons". $w \in W$
B(w) := In der Woche w l&auml;uft "Die Ludolfs". $w \in W$
C(w) := In der Woche w l&auml;uft "Telekolleg". $w \in W$

Dann lautet (ii) formalisiert:
$\forall w \in W: A(w) \land B(w) \land C(w)$

Negiert:
$\exists w \in W: \neg A(w) \lor \neg B(w) \lor \neg C(w)$

<h2>Teilbarkeit</h2>
Nun mal etwas eigenes:

<blockquote>(iii) Jede gerade Zahl ist durch zwei teilbar.</blockquote>

Sei M die Menge der geraden Zahlen.
Dann lautet (iii) formalisiert:
$\forall m \in M: x = \frac{m}{2} \implies x \in \mathbb{N}$

<h2>Weitere Materialien</h2>
<ul>
  <li><a href="http://lrb.cs.uni-dortmund.de/~tick/Lehre/WS10/Logik/01-introw.pdf">Uni Dortmund</a>: 15 Seiten zum Formalisieren vom Aussagen</li>
  <li><a href="http://page.math.tu-berlin.de/~schmitt/lina0910/loesungen/loesung01.pdf">TU-Berlin</a> (Aufgabe 4 - " Jeder, der ein gutes Gehor hat, kann richtig singen[...]")</li>
</ul>
