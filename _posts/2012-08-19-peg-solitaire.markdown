---
layout: post
status: publish
published: true
title: Peg Solitaire
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 41421
wordpress_url: http://martin-thoma.com/?p=41421
date: 2012-08-19 17:00:58.000000000 +02:00
categories:
- German posts
tags: []
comments:
- id: 194301
  author: Niklas B.
  author_email: white57@gmx.net
  author_url: ''
  date: !binary |-
    MjAxMi0wOC0yMSAyMjoyMDoyMyArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wOC0yMSAyMDoyMDoyMyArMDIwMA==
  content: ! 'Und wer''s ausprobieren will: http://www.freeware.de/download/solitaire3d_22105.html
    :D Das ist wohl im Jahre 2004 entstanden unter Windows 95 mit der VB6(!) Runtime,
    also keine Ahnung ob es unter heutigen Betriebssystemen noch l&auml;uft :P'
---
Solit&auml;r (auch Solitaire, Steck- oder Solohalma, Springer, Jumper, Nonnenspiel, Einsiedlerspiel) ist ein Brettspiel f&uuml;r eine Person. Das weitest verbreitete Spielfeld ist kreuzf&ouml;rmig und wird mit 32 Steinen auf 33 Felder gestartet.
In der Mitte fehlt die Kugel, alle anderen 32 Felder sind besetzt.

<h2>Die Bezeichnungen</h2>
[caption id="attachment_41441" align="alignright" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board.png"><img class=" wp-image-41441 " title="Peg Solitaire - Spielfeld" src="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board.png" alt="Peg Solitaire - Spielfeld" width="300" height="300" /></a> Peg Solitaire - Spielfeld[/caption]

Dieses Brett ist hier mit den Bezeichnungen f&uuml;r die Felder dargestellt. Der Buchstabe bezeichnet das Feld (<strong>o</strong>ben, <strong>u</strong>nten, <strong>l</strong>inks, <strong>r</strong>echts, <strong>m</strong>ittig) und die Zahl die genaue Position, wenn man das Brett so dreht, dass das aktuelle Feld oben nur zwei Kugeln hat, sind in der obersten Zeile die Zahlen 1 und 2, in der mittigen 3, 4 und 5 und in der untersten 6, 7 und 8:
<h2>Die Regeln</h2>
Es gibt vier verschiedene Spielz&uuml;ge: Der Sprung nach oben, unten, links und rechts. Es muss immer mit einer Kugel &uuml;ber eine andere Kugel auf ein freies Feld gesprungen werden.

<h2>Aufgabenstellung</h2>
Wie muss man ziehen, damit die letzte Kugel in der Mitte ubrig bleibt?
<h2>Die L&ouml;sung</h2>
Der erste Zug muss mit einer 2er-Kugel gemacht werden. Sagen wir, es ist o4.
<table>
<tbody>
<tr>
<td>l3</td>
<td>u3</td>
<td>r3</td>
<td>o3</td>
</tr>
<tr>
<td>o8</td>
<td>l8</td>
<td>u8</td>
<td>r8</td>
</tr>
<tr>
<td>o6</td>
<td>l6</td>
<td>u6</td>
<td>r6</td>
</tr>
<tr>
<td>l1</td>
<td>u1</td>
<td>r1</td>
<td>o1</td>
</tr>
<tr>
<td>o8</td>
<td>l8</td>
<td>u8</td>
<td>r8</td>
</tr>
</tbody>
</table>
Die momentane Situation sieht folgenderma&szlig;en aus:

[caption id="attachment_41461" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board-situation-1.png"><img class="wp-image-41461 " title="Peg Solitaire: Board Situation" src="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board-situation-1.png" alt="Peg Solitaire: Board Situation" width="300" height="300" /></a> Peg Solitaire: Board Situation[/caption]

Nun kann man u1 einmal im Krei (auf r3, r5, o1, l3, l5 und dann wieder auf u1) wandern lassen. Es bleibt eine T-Form &uuml;brig:

[caption id="attachment_41491" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board-situation-2.png"><img class=" wp-image-41491 " title="Peg Solitaire: Board Situation 2" src="http://martin-thoma.com/wp-content/uploads/2012/08/Peg-solitaire-board-situation-2.png" alt="Peg Solitaire: Board Situation 2" width="300" height="300" /></a> Peg Solitaire: Board Situation 2[/caption]

Nun muss nur noch m &uuml;ber l1, dann u4, r1 und schlie&szlig;lich l4.
