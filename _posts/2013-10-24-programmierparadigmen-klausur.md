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

## Behandelter Stoff ##
### Vorlesung ###
<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
<td>23.10.2013</td>
<td>Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/10_FunktionaleProgrammierung.pdf">10</a></td>
<td>Haskell: Quicksort, Listen, <a href="http://learnyouahaskell.com/higher-order-functions#maps-and-filters">Filter</a>, <a href="http://www.haskell.org/haskellwiki/Syntactic_sugar/Cons">Cons-Operator</a></td>
</tr>
<tr>
<td>25.10.2013</td>
<td>Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/11_FunktionaleProgrammierung.pdf">11</a></td>
<td>Haskell: filter, map, iter, foldr, foldl, Currying, Extensionalitätsprinzip, Kombinatoren (Summe, Produkt), flatten, cons, zip</td>
</tr>
<tr>
<td>30.10.2013</td>
<td>Funktionale Programmierung <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/intern/12_FunktionaleProgrammierung.pdf">12</a></td>
<td>Haskell: zipWith, short circuit evaluation, foldl, foldr, Unendliche Listen, Typen, Polymorphie</td>
</tr>
<tr>
<td>06.11.2013</td>
<td></td>
<td>Backtracking, Algebraische und rekursive Datentypen, map for trees, Typklassen</td>
</tr>
<tr>
<td>08.11.2013</td>
<td>&nbsp;</td>
<td>Typklassen, Monaden</td>
</tr>
<tr>
<td>13.11.2013</td>
<td>&nbsp;</td>
<td>Sichtbarkeitsbereich $\subseteq$ Gültigkeitsbereich; $\alpha$ / $\eta$-Äqivalenz, Redex; Funktion, die sich als eigenes Argument nimmt; $\lambda$-Klakül ist Turing-Mächtig</td>
</tr>
<tr>
<td>29.11.2013</td>
<td>Logische Programmierung</td>
<td>Prolog</td>
</tr>
<tr>
<td>10.01.2014</td>
<td>Scala</td>
<td>Kein `;`, weniger verbose als Java, ...</td>
</tr>
<tr>
<td>15.01.2014</td>
<td>Scala</td>
<td>Concurrency in Scala: Actors, react; MPI, OpenMP</td>
</tr>
<tr>
<td>22.01.2014</td>
<td>-</td>
<td>X10: async, val, var</td>
</tr>
<tr>
<td>24.01.2014</td>
<td>-</td>
<td>C (<abbr title="Immer aus Hauptspeicher, nie aus Cache holen">volatile</abbr>)</td>
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
* [Inoffizielles Skript](https://github.com/MartinThoma/LaTeX-examples/blob/master/documents/Programmierparadigmen/Programmierparadigmen.pdf?raw=true) in A5 ([LaTeX-Quellen](https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/Programmierparadigmen)): Wer das gerne für ca. 10 Euro in SW gedruckt mit Ringbindung hätte, soll mir eine Email schreiben
* [Vorlesungswebsite](http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/) und [Übungsblätter](http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/#unterlagen)
* Ein [Anki-Deck](https://ankiweb.net/shared/info/3121773115) (NICHT meines!)
* Stackexchange:
  * [What is the meaning of M ⊨ φ?](http://math.stackexchange.com/q/704401/6876)
  * [How can I compile the x10 example?](http://stackoverflow.com/q/22283936/562769)
  * [What is the difference of 'async' before or after 'for' in X10?](http://stackoverflow.com/q/22643004/562769)
  * [How do I generate and print Fibonacci numbers in X10?](http://stackoverflow.com/q/22709063/562769)
  * [What is the difference between ifne and ifnonnull?](http://stackoverflow.com/q/22731293/562769)
  * [Haskell list comprehension - list of all list splits](http://stackoverflow.com/q/22594719/562769)
  * [How can I ask questions on a family tree in Prolog?](http://stackoverflow.com/q/22177931/562769)

## Klausurvorbereitung
* [H-99: Ninety-Nine Haskell Problems](http://www.haskell.org/haskellwiki/H-99:_Ninety-Nine_Haskell_Problems)
* [P-99: Ninety-Nine Prolog Problems](https://sites.google.com/site/prologsite/prolog-problems)
* Scala
  * [S-99: Ninety-Nine Scala Problems](http://aperiodic.net/phil/scala/s-99/)
  * [Learning Scala](http://joelabrahamsson.com/learning-scala/) by Joel Abrahamsson

## Übungsbetrieb

* Wo sind die Übungsblätter: [Link](http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/uebung/#unterlagen)
* Abgabeform: auf Papier und via E-Mail
* Abgabe: Datum steht auf den Übungsblättern; Ort: Kasten im Keller des Infobaus
* Rücknahme: im Tutorium
* Turnus: wöchentlich, erscheint am Donnerstag.
* Übungsschein verpflichtend: Es gibt keinen Übungsschein.
* Bonus durch Übungsschein: Es gibt keinen Klausurbonus.

## Termine und Klausurablauf
**Datum**: Donnerstag, den 10. April 2014 von 14:00 bis 16:00 Uhr ([Quelle](https://pp.info.uni-karlsruhe.de/lehre/WS201314/paradigmen/))<br/>
**Ort**: Audimax ([Quelle](https://pp.info.uni-karlsruhe.de/lehre/WS201314/paradigmen/#klausuren))<br/>
**Punkte**: 120<br/>
**Punkteverteilung**: Vermutlich etwas in dieser Richtung:

* 25 Punkte: Haskell / Scala
* 20 Punkte: Logische Programmierung
* 25 Punkte: Typinferenz / Lambda-Kalkül
* 10 Punkte: C
* 10 Punkte: MPI
* 10 Punkte: X10
* 20 Punkte: Compilerbau

**Bestehensgrenze**: ?<br/>
**Übungsschein**: Gibt es nicht.<br/>
**Bonuspunkte**: Gibt es nicht.<br/>
**Ergebnisse**: stehen seit dem 17.04.2014 fest<br/>
**Einsicht**: am Mittwoch den 30.04.2014, 14:00 Uhr - 16:00 in Raum 010, Informatik Gebäude (Geb. 50.34)  (bekanntgegeben über [Vorlesungswebsite](http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/index.php) am 17.04.2014)<br/>
**Erlaubte Hilfsmittel**: (siehe <a href="http://pp.ipd.kit.edu/lehre/WS201314/paradigmen/">Website</a>)

<blockquote>Erlaubte Hilfsmittel für die Klausur sind alle Quellen in Papierform, insbesondere
<ul>
<li>Vorlesungsfolien der Veranstaltung Programmierparadigmen</li>
<li>Übungszettel und Beispiellösungen der Veranstaltung Programmierparadigmen</li>
<li>Bücher, Ausdrucke und beliebige eigenen Aufzeichnungen</li>
</ul>
</blockquote>

## Ergebnisse
Stehen seit dem 17.04.2014 fest.
