---
layout: post
status: publish
published: true
title: Das Quine-McCluskey-Verfahren
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 55431
wordpress_url: http://martin-thoma.com/?p=55431
date: 2013-01-29 14:34:06.000000000 +01:00
categories:
- German posts
tags:
- Digitaltechnik
comments: []
featured_image: 2013/01/quine-mccluskey.png
---
Das Quine-McCluskey-Verfahren wird angewendet, wenn man eine Schaltfunktion minimieren will. Es muss also eine Schaltfunktion gegeben sein. Es sollte eigentlich zus&auml;tzlich Kostenfunktion gegeben sein, aber meist ist das nicht der Fall.

<h2>Verfahren</h2>
<strong>Gegeben</strong>: Eine Schaltfunktion $f:\{0,1\}^n \rightarrow \{0,1\}, \; n \in \mathbb{N}$
<strong>Schritt 1:</strong> Aufstellen der Funktionstabelle. Sie hat die Spalten 
<ul>
  <li>&bdquo;Nr.&ldquo;, die bei 0 beginnt und bis $2^n - 1$ geht.</li>
  <li>Eine Spalte pro Funktionsparameter (z.B. $a, b, c, ...$)</li>
  <li>Eine Spalte f&uuml;r den Funktionswert $f(a,b,c,...)$</li>
</ul>

<strong>Schritt 2</strong>: Aufstellen der ersten Quinesche Tabelle 0ter Ordnung. 

Sie hat die Spalten
<ul>
  <li>&bdquo;Nr.&ldquo;</li>
  <li>Eine Spalte pro Parameter</li>
  <li>&bdquo;✓&ldquo; (H&auml;kchen)</li>
</ul>
In der ersten Quineschen Tabelle stehen nur noch die Zeilen, deren Funktionswert 1 ist. Das sind die sogenannten Minterme. Zus&auml;tzlich sind sie nach Anzahl der 1er geordnet.

<strong>Schritt 3</strong>: $i$-tes Zusammenfassen

Nun erstellt man die erste Quinesche Tabelle $i$-ter Ordnung. Also beim ersten mal erster Ordnung, beim zweiten Mal zweiter Ordnung, ...
Diese Tabellen haben alle die gleichen Spalten und die Zeilen-Anzahl kann sowohl wachsen als auch schrumpfen. Das $i$ gibt dabei die Anzahl der &bdquo;don't care&ldquo; Stellen an, also der Stellen die sowohl 0 als auch 1 sein k&ouml;nnen.

Um aus der ersten Quinesche Tabelle $(i-1)$-ter Ordnung die rsten Quinesche Tabelle $i$-ter Ordnung zu erstellen, geht man wie folgt vor:
<ul>
  <li>Vergleiche alle Zeilen, in denen sich die Anzahl der 1er um genau 1 unterscheidet:
    <ul>
      <li>Unterscheiden sich Zeile Nr. x und Zeile Nr. y an nur einer Stelle, so schreibe in die Tabelle $i$ter Ordnung eine neue Zeile. Die Nummer dieser Zeile ist &bdquo;x, y&ldquo; und sie hat an der Stelle, an der sich die Zeilen x und y unterschieden, ein don't care.</li>
      <li>Hake die Zeilen x und y in der Tabelle $(i-1)$-ter Ordnung ab</li>
    </ul>
  </li>
</ul>

Es ist m&ouml;glich, das Zeilen nicht abgehakt werden, weil sie sich mit keiner Zeile zusammenfassen lassen. Das ist ok.
Sobald in einem Schritt keine Zusammenfassung mehr m&ouml;glich ist, ist man hier fertig. Falls noch eine M&ouml;glich ist, geht man wieder in Schritt 3.

Nun schreibt man alle Zeilen auf, die nicht abgehakt sind. Das sind die Primimplikanten.

<strong>Schritt 4</strong>: Aufstellen der zweiten Quineschen Tabelle

Die zweite Quinesche Tabelle (auch &Uuml;berdeckungstabelle genannt) hat folgende Spalten:
<ul>
  <li>Primimplikanten</li>
  <li>Eine Spalte pro Minterm. Die Beschriftung ist dabei eine Nr.</li>
  <li>Eine Spalte &bdquo;Kosten&ldquo;</li>
</ul>

Nun macht man in den Zellen ein Kreuz, in denen der Primimplikant den Minterm abdeckt (also wenn die Nr. im Namen des Minterms vorkommt). Die Kosten muss man pro Primimplikant berechnen.

<strong>Schritt 5</strong>: Vereinfachen der zweiten Quineschen Tabelle

Dieser Schritt erinnert mich irgendwie an Sudoku. 
<ul>
  <li><em>Zeilendominanz</em>: Hat eine Zeile a nur x-e an Stellen, wo auch eine andere Zeile b x-e hat und ist Zeile b nicht teurer als a, so kann Zeile a gestrichen werden. Also: Es wird die Zeile mit weniger x gestrichen</li>
  <li><em>Spaltendominanz</em>: &Uuml;berdeckt eine Spalte eine andere Spalte mit ihren x-en, so kann die Spalte mit <u>mehr</u> x-en gestrichen werden.</li>
</ul>

<strong>Schritt 6</strong>: Identifizieren von Kernprimimplikanten.

Wenn eine Zeile als einzige an einer bestimmten Spalte ein x hat, ist der zugeh&ouml;rige Primimplikant ein Kernprimimplikant. Er muss auf jeden Fall in der Minimalform vorkommen. Diesen schreibt man sich also auf, Streicht die Zeile und alle Spalten, an denen der Kernprimimplikant ein x hatte. Dann geht man zur&uuml;ck zu Schritt 5.

Gab es keinen Kernprimimplikanten, geht man zu Schritt 7.

<strong>Schritt 7</strong>: Handarbeit

Ich muss mal nach einem Beispiel suchen, aber ich glaube es ist m&ouml;glich, dass man die zweite Quinesche Tabelle ab einem gewissen Punkt nicht mehr vereinfachen kann, aber dennoch Zeilen und Spalten &uuml;brig sind. Dann muss man &bdquo;durch scharfes Hinsehen&ldquo; (also Brute-Force) die Minimalform finden, oder? Hier bin ich mir nicht ganz sicher.

<h2>Beispiele</h2>
Die folgende Aufgabe ist vom &Uuml;bungsblatt 7 (WS 2012/2013). Herr Terlemez hat mir freundlicherweise erlaubt, sie hier verwenden zu d&uuml;rfen.
(Die <a href="http://ti.ira.uka.de/TI-1/Uebungen/Uebungen.php">offiziellen Aufgaben und L&ouml;sungen</a> sind passwortgesch&uuml;tzt.)

<strong>Aufgabe</strong>:
Gegeben sei die Schaltfunktion

$g(d,c,b,a) := dc \bar b a \lor d \bar c ba \lor d \bar c \bar b a \lor \bar d ca \lor dcb$

<ol>
  <li>Bestimmen Sie alle Primimplikanten von $g$ mit Hilfe der 1. Quineschen Tabelle des Quine-McCluskey-Verfahrens.</li>
  <li>Geben Sie die &Uuml;berdeckungstabelle (2. Quinesche Tabelle) f&uuml;r die gefundenen Primimpikanten an (ohne Vereinfachung). Lesen Sie eine disjunktive Minimalform von $g$ ab.</li>
</ol>

<strong>L&ouml;sung</strong>:
(Habe gerade leider keine Zeit, diese abzutippen. Kommt vielleicht noch.)
[caption id="attachment_56641" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/digitaltechnik-aufgabe-7-2-1.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/digitaltechnik-aufgabe-7-2-1-300x236.jpg" alt="Handschriftliche L&ouml;sung der Aufgabe 7.2.1 aus DT" width="300" height="236" class="size-medium wp-image-56641" /></a> Handschriftliche L&ouml;sung der Aufgabe 7.2.1 aus DT[/caption]

[caption id="attachment_56651" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/digitaltechnik-aufgabe-7-2-2.jpg"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/digitaltechnik-aufgabe-7-2-2-300x253.jpg" alt="Handschriftliche L&ouml;sung der Aufgabe 7.2.2 aus DT" width="300" height="253" class="size-medium wp-image-56651" /></a> Handschriftliche L&ouml;sung der Aufgabe 7.2.2 aus DT[/caption]

<h2>Quellen</h2>
Ich habe diesen Artikel mit meinem Wissen aus den Folien (DT-VL12), der <a href="http://www.youtube.com/watch?v=K1NAj4ecPDw&list=PL025B377F9094FCB9&index=13">Vorlesung</a> und dem Tutorium erstellt. 
