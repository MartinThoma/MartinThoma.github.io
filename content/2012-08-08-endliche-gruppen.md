---
layout: post
lang: de
title: Endliche Gruppen
slug: endliche-gruppen
author: Martin Thoma
date: 2012-08-08 12:03:42.000000000 +02:00
category: German posts
tags: Linear algebra
featured_image: 2012/08/endliche-gruppe-thumb.png
---
Endliche Gruppen haben ein paar interessante Eigenschaften. Unter anderem gibt es nur zwei Gruppen mit vier Elementen. alle anderen Gruppen sind isomorph zu diesen Gruppen. Das zeige ich im folgendem.

<h2>Gruppen mit vier Elementen</h2>
Es gibt genau zwei Gruppen mit vier Elementen. Das sind:
$G_1 = (\mathbb{Z}/4\mathbb{Z}, +)$ und
$G_2 = (\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}, +)$

<h3>Beweis Teil 1: G<sub>1</sub> und G<sub>2</sub> sind Gruppen</h3>
Eine Gruppe $(A, \circ)$ m&uuml;ssen drei Eigenschaften erf&uuml;llen:
<ul>
  <li>(G1) <strong>Assoziativit&auml;t</strong>: $\forall a,b,c \in A: (a \circ b) \circ c = a \circ (b \circ c)$</li>
  <li>(G2) <strong>Neutrales Element</strong>: $\exists e \in A \forall a \in A: e \circ a = a \circ e = a$</li>
  <li>(G3) <strong>Inverses Element</strong>: $\forall a \in A \exists a^{-1} \in A: a \circ a^{-1} = a^{-1} \circ a = e$</li>
</ul>

Die Verkn&uuml;pfungstafel f&uuml;r $G_1$ lautet:
<table class="wikitable" style="width:300px">
  <tr>
    <th>+</th>
    <th>0</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <th>0</th>
    <td class="hintergrundfarbe9">0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <th>1</th>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td class="hintergrundfarbe9">0</td>
  </tr>
  <tr>
    <th>2</th>
    <td>2</td>
    <td>3</td>
    <td class="hintergrundfarbe9">0</td>
    <td>1</td>
  </tr>
  <tr>
    <th>3</th>
    <td>3</td>
    <td class="hintergrundfarbe9">0</td>
    <td>1</td>
    <td>2</td>
  </tr>
</table>

Man sieht direkt an der Tabelle, dass <strong>0</strong> das neutrale Element ist und jedes Element ein Inverses hat. F&uuml;r die Assoziativit&auml;t f&auml;llt mir nichts besseres ein, als die 64 M&ouml;glichkeiten alle auszuprobieren. Geht das k&uuml;rzer?

Die Verkn&uuml;pfungstafel f&uuml;r $G_2$ lautet:
<table class="wikitable" style="width:300px">
  <tr>
    <th>+</th>
    <th>(0,0)</th>
    <th>(0,1)</th>
    <th>(1,0)</th>
    <th>(1,1)</th>
  </tr>
  <tr>
    <th>(0,0)</th>
    <td class="hintergrundfarbe9">(0,0)</td>
    <td>(0,1)</td>
    <td>(1,0)</td>
    <td>(1,1)</td>
  </tr>
  <tr>
    <th>(0,1)</th>
    <td>(0,1)</td>
    <td class="hintergrundfarbe9">(0,0)</td>
    <td>(1,1)</td>
    <td>(1,0)</td>
  </tr>
  <tr>
    <th>(1,0)</th>
    <td>(1,0)</td>
    <td>(1,1)</td>
    <td class="hintergrundfarbe9">(0,0)</td>
    <td>(0,1)</td>
  </tr>
  <tr>
    <th>(1,1)</th>
    <td>(1,1)</td>
    <td>(1,0)</td>
    <td>(0,1)</td>
    <td class="hintergrundfarbe9">(0,0)</td>
  </tr>
</table>

Das neutrale Element ist hier also <strong>(0,0)</strong>.

<h3>Beweis Teil 2: Es gibt keine weiteren Gruppen</h3>
Hierf&uuml;r ist es sehr hilfreich zu wissen, dass die Verkn&uuml;pfungstafel einer Gruppe immer alle Elemente sowohl in jeder Spalte, als auch in jeder Zeile hat. Dann kann man es Sudoku-m&auml;&szlig;ig beweisen.

Folgendes Skelett gilt immer:
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

<h4>#1: e auf (1,1)</h4>
Wir haben nun folgende Tabelle:
<table>
<tr>
<td>
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td class="hintergrundfarbe7">e</td>
    <td class="hintergrundfarbe8">c</td>
    <td class="hintergrundfarbe8">b</td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td class="hintergrundfarbe8">c</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td class="hintergrundfarbe8">b</td>
    <td></td>
    <td></td>
  </tr>
</table>
</td>
<td>
<ul>
  <li>$b + a = c$ (da a und e in dieser Spalte sind und b in der Zeile ist)</li>
  <li>$c + a = b$ (nur b fehlt in der Spalte)</li>
  <li>$a + b = c$ (da a und e in dieser Zeile und b in der Spalte bereits vorkommt)</li>
  <li>$a + c = b$ (nur b fehlt in der Zeile)</li>
</ul>
</td>
</tr>
</table>

<h4>#1.1: e auf (2,2)</h4>
<table>
<tr>
<td>
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td>e</td>
    <td>c</td>
    <td>b</td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td>c</td>
    <td class="hintergrundfarbe7">e</td>
    <td class="hintergrundfarbe8">a</td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td>b</td>
    <td class="hintergrundfarbe8">a</td>
    <td class="hintergrundfarbe8">e</td>
  </tr>
</table>
</td>
<td>
<ul>
  <li>$c + c = e$ (genau 1 e pro Zeile / Spalte)</li>
  <li>$b + c = a$ (nur a fehlt in der Zeile)</li>
  <li>$c + b = a$ (nur a fehlt in der Zeile)</li>
</ul>
</td>
</tr>
</table>

Diese L&ouml;sung enstpricht $G_2$.

<h4>#1.2: a auf (2, 2)</h4>
<table>
<tr>
<td>
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td>e</td>
    <td>c</td>
    <td>b</td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td>c</td>
    <td class="hintergrundfarbe7">a</td>
    <td class="hintergrundfarbe8">e</td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td>b</td>
    <td class="hintergrundfarbe8">e</td>
    <td class="hintergrundfarbe8">a</td>
  </tr>
</table>
</td>
<td>
<ul>
  <li>$b + c = e$ (genau 1 e pro Zeile / Spalte)</li>
  <li>$c + b = e$ (genau 1 e pro Zeile / Spalte)</li>
  <li>$c + c = a$ (nur a fehlt in der Zeile)</li>
</ul>
</td>
</tr>
</table>

Das entspricht $G_1$. Das sieht man, wenn man ...
<ol>
 <li>... die Spalte a und b tauscht</li>
 <li>... die Zeilen a und b tauscht</li>
 <li>... die Elemente a und b tauscht</li>
</ol>

<h4>#2: b auf (1, 1)</h4>
<table>
<tr>
<td>
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td class="hintergrundfarbe7">b</td>
    <td class="hintergrundfarbe8">c</td>
    <td class="hintergrundfarbe8">e</td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td class="hintergrundfarbe8">c</td>
    <td class="hintergrundfarbe8">e</td>
    <td class="hintergrundfarbe8">a</td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td class="hintergrundfarbe8">e</td>
    <td class="hintergrundfarbe8">a</td>
    <td class="hintergrundfarbe8">b</td>
  </tr>
</table>
</td>
<td>
<ul>
  <li>$b + a = c$ (da $c + a \neq c$ und c noch nicht in der Spalte ist, aber dennoch vorkommen muss)</li>
  <li>$c+a =e$ (genau 1 e pro Zeile / Spalte)</li>
  <li>$c+b = a$ (da c und e in der Zeile bereits vorkommen und b in der Spalte ist)</li>
  <li>$c+c = b$ (da der Rest schon in der Zeile ist)</li>
  <li>$b+b = e$ (da a und b in der Spalte sind, c in der Zeile)</li>
  <li>$b+c = a$ (da der Rest in der Zeile schon vorkommt)</li>
  <li>$a+b = c$ ( - " - )</li>
  <li>$a+c = e$</li>
</ul>
</td>
</tr>
</table>

Das enspricht wieder $G_1$.

<h4>#3: c auf (1, 1)</h4>
<table>
<tr>
<td>
<table class="wikitable" style="width:250px">
  <tr>
    <th>+</th>
    <th>e</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
  </tr>
  <tr>
    <th>e</th>
    <td>e</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>a</th>
    <td>a</td>
    <td class="hintergrundfarbe7">c</td>
    <td class="hintergrundfarbe8">e</td>
    <td class="hintergrundfarbe8">b</td>
  </tr>
  <tr>
    <th>b</th>
    <td>b</td>
    <td class="hintergrundfarbe8">e</td>
    <td class="hintergrundfarbe8">c</td>
    <td class="hintergrundfarbe8">a</td>
  </tr>
  <tr>
    <th>c</th>
    <td>c</td>
    <td class="hintergrundfarbe8">b</td>
    <td class="hintergrundfarbe8">a</td>
    <td class="hintergrundfarbe8">e</td>
  </tr>
</table>
</td>
<td>
<ul>
  <li>$a+b = e$ (a, c bereits in Zeile, b in Spalte)</li>
  <li>$a+c = b$ (a, c, e in Zeile)</li>
  <li>$b+a = e$ (a, c in Spalte, b in Zeile)</li>
  <li>$c+c = e$ (letztes e)</li>
  <li>$b+c = a$ (b, c, e in Spalte)</li>
  <li>$b+b = c$ (b, e, a in Zeile)</li>
  <li>$c+a = b$ (a, c, e in Spalte)</li>
  <li>$c+b = a$ (b, e, c in Spalte)</li>
</ul>
</td>
</tr>
</table>

Das entspricht $G_1$. Das sieht man, wenn man ...
<ol>
 <li>... die Spalte b und c tauscht</li>
 <li>... die Zeilen b und c tauscht</li>
 <li>... die Elemente b und c tauscht</li>
</ol>
