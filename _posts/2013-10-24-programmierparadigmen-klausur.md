---
layout: post
title: Programmierparadigmen Klausur
author: Martin Thoma
date: 2013-10-24 12:46:16.000000000 +02:00
categories:
- German posts
tags:
- Haskell
- Klausur
- Programmierparadigmen
featured_image: 2012/02/klausur-test-thumbnail.jpg
alias: /programmierparadigmen/index.html
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Programmierparadigmen&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei Herrn Prof. Dr. Snelting im Wintersemester 2013/2014 gehört.</div>

Der Artikel wird bis zur Klausur laufend aktualisiert.

## Behandelter Stoff ##
### Vorlesung ###
<table>
<tr>
<td style="border-bottom:1px solid black;">23.10.2013</td>
<td style="border-bottom:1px solid black;">Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/10_FunktionaleProgrammierung.pdf">10</a></td>
<td style="border-bottom:1px solid black;">Haskell: Quicksort, Listen, <a href="http://learnyouahaskell.com/higher-order-functions#maps-and-filters">Filter</a>, <a href="http://www.haskell.org/haskellwiki/Syntactic_sugar/Cons">Cons-Operator</a></td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">25.10.2013</td>
<td style="border-bottom:1px solid black;">Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/11_FunktionaleProgrammierung.pdf">11</a></td>
<td style="border-bottom:1px solid black;">Haskell: filter, map, iter, foldr, foldl, Currying, Extensionalitätsprinzip, Kombinatoren (Summe, Produkt), flatten, cons, zip</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">30.10.2013</td>
<td style="border-bottom:1px solid black;">Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/12_FunktionaleProgrammierung.pdf">12</a></td>
<td style="border-bottom:1px solid black;">Haskell: zipWith, short circuit evaluation, foldl, foldr, Unendliche Listen, Typen, Polymorphie</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">06.11.2013</td>
<td style="border-bottom:1px solid black;"></td>
<td style="border-bottom:1px solid black;">Backtracking, Algebraische und rekursive Datentypen, map for trees, Typklassen</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">08.11.2013</td>
<td style="border-bottom:1px solid black;"></td>
<td style="border-bottom:1px solid black;">Typklassen, Monaden</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">13.11.2013</td>
<td style="border-bottom:1px solid black;"></td>
<td style="border-bottom:1px solid black;">Sichtbarkeitsbereich $\subseteq$ Gültigkeitsbereich; $\alpha$ / $\eta$-Äqivalenz, Redex; Funktion, die sich als eigenes Argument nimmt; $\lambda$-Klakül ist Turing-Mächtig</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">29.11.2013</td>
<td style="border-bottom:1px solid black;">Logische Programmierung</td>
<td style="border-bottom:1px solid black;">Prolog</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">10.01.2014</td>
<td style="border-bottom:1px solid black;">Scala</td>
<td style="border-bottom:1px solid black;">Kein `;`, weniger verbose als Java, ...</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">15.01.2014</td>
<td style="border-bottom:1px solid black;">Scala</td>
<td style="border-bottom:1px solid black;">Concurrency in Scala: Actors, react; MPI, OpenMP</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">22.01.2014</td>
<td style="border-bottom:1px solid black;">-</td>
<td style="border-bottom:1px solid black;">X10: async, val, var</td>
</tr>
<tr>
<td style="border-bottom:1px solid black;">24.01.2014</td>
<td style="border-bottom:1px solid black;">-</td>
<td style="border-bottom:1px solid black;">C (<abbr title="Immer aus Hauptspeicher, nie aus Cache holen">volatile</abbr>)</td>
</tr>
</table>

### Übungsblätter ###
<table>
  <tr>
    <th>Übungsblatt</th>
    <th>Inhalt</th>
  </tr>
  <tr>
    <td><a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/blaetter/blatt0.pdf" rel="nofollow">ÜB 0</a>: Haskell</td>
    <td>Haskell installieren (siehe <a href="http://wiki.ubuntuusers.de/Haskell">UbuntuUsers</a>), Maximum dreier Zahlen berechnen</td>
  </tr>
  <tr>
    <td><a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/blaetter/blatt1.pdf" rel="nofollow">ÜB 1</a>: Rekursive Funktionen in Haskell</td>
    <td>Potenzen, Primzahlen, Sortieren</td>
  </tr>
</table>

### Tutorium ###
#### 16.12.2013 ####

```haskell
let f = \ x.plus x x in f (f c_2)    ^= (\ f. f (f c_2)) (\x. plus x x)
```

`let` wird wegen dem Typsystem benötigt (`let` ist polymorph, 
$\lambda$-Term nicht).

```haskell
let f = \x.1 in (f 7) + (f["a"])    ^= (\ f.   ) (\ x. 1)
    f: \alpha_5 -> int
    f: \forall \alpha_5. \alpha_5 \rightarrow int 
```


## Material ##
<ul>
  <li><a href="https://github.com/MartinThoma/LaTeX-examples/blob/master/documents/Programmierparadigmen/Programmierparadigmen.pdf?raw=true">Inoffizielles Skript</a> in A5 (<a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/Programmierparadigmen">LaTeX-Quellen</a>): Wer das gerne für ca. 10 Euro in SW gedruckt mit Klebebindung hätte, soll mir eine Email schreiben</li>
  <li><a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/">Vorlesungswebsite</a> und <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/#unterlagen">Übungsblätter</a></li>
  <li>Ein <a href="https://ankiweb.net/shared/info/3121773115">Anki-Deck</a> (NICHT meines!)</li>
</ul>

## Klausurvorbereitung
* [H-99: Ninety-Nine Haskell Problems](http://www.haskell.org/haskellwiki/H-99:_Ninety-Nine_Haskell_Problems)
* [P-99: Ninety-Nine Prolog Problems](https://sites.google.com/site/prologsite/prolog-problems)
* [S-99: Ninety-Nine Scala Problems](http://aperiodic.net/phil/scala/s-99/)

## Übungsbetrieb

<ul>
<li>Wo sind die Übungsblätter: <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/#unterlagen">Link</a></li>
<li>Abgabeform: ?</li>
<li>Abgabe: ?</li>
<li>Rücknahme: ?</li>
<li>Turnus: wöchentlich, erscheint am Donnerstag</li>
<li>Übungsschein verpflichtend: Es gibt keinen Übungsschein.</li>
<li>Bonus durch Übungsschein: Es gibt keinen Klausurbonus.</li>
</ul>

<h2>Termine und Klausurablauf</h2>
<strong>Datum</strong>: Donnerstag, den 10. April 2014 von 14:00 bis 16:00 Uhr ([Quelle](https://pp.info.uni-karlsruhe.de/lehre/WS201314/paradigmen/))<br/>
<strong>Ort</strong>: steht noch nicht fest (Stand: 02.03.2014)<br/>
<strong>Punkte</strong>: vermutlich 80 - 120<br/>
<strong>Bestehensgrenze</strong>: ?<br/>
<strong>Übungsschein</strong>: Gibt es nicht.<br/>
<strong>Bonuspunkte</strong>: Gibt es nicht.<br/>
<strong>Ergebnisse</strong>: steht noch nicht fest (Stand: 02.03.2014)<br/>
<strong>Einsicht</strong>: steht noch nicht fest (Stand: 02.03.2014)<br/>
<strong>Erlaubte Hilfsmittel</strong>: (siehe <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/">Website</a>)

<blockquote>Erlaubte Hilfsmittel für die Klausur sind alle Quellen in Papierform, insbesondere
<ul>
<li>Vorlesungsfolien der Veranstaltung Programmierparadigmen</li>
<li>Übungszettel und Beispiellösungen der Veranstaltung Programmierparadigmen</li>
<li>Bücher, Ausdrucke und beliebige eigenen Aufzeichnungen</li>
</ul>
</blockquote>

<h2>Ergebnisse</h2>
Stehen noch nicht fest (Stand: 02.03.2014).
