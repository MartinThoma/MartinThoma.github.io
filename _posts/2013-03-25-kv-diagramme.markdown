---
layout: post
status: publish
published: true
title: KV-Diagramme
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 62811
wordpress_url: http://martin-thoma.com/?p=62811
date: 2013-03-25 23:37:00.000000000 +01:00
categories:
- German posts
tags:
- Digitaltechnik
comments: []
featured_image: 2013/03/karnaugh-map-300x300.png
---
<div class="info">Ich setze im Folgenden vorraus, dass man schon mal was von KV-Diagrammen geh&ouml;rt hat und vielleicht schon ein paar gezeichnet hat. Insbesondere erkl&auml;re ich nicht wie man aus dem KV-Diagramm der Gr&ouml;&szlig;e 16 eines der Gr&ouml;&szlig;e 32 bekomt und was die Beschriftung bedeutet.</div>

KV-Diagramme sind f&uuml;r die TI-Klausur am KIT bei Herrn Prof. Dr. Asfour sehr wichtig. Im folgenden sind die wichtigsten Eigenschaften, die so explizit leider nicht in der Vorlesung genannt wurden.

<h2>Konstruktion aus Schaltfunktion</h2>
Gegeben sei folgende vollst&auml;ndig definierte Schaltfunktion:
$f(w,x,y,z) := (w \lor \bar y) (\bar w \lor x \lor y) (\bar w \lor \bar x \lor z)$

Nun kann man eine Funktionstabelle aufstellen:
<ol>
  <li>Dabei schreibt man sich erst das Ger&uuml;st hin, also eine Titelzeile mit den vier Variablen $w,x,y,z$ und $2^4 = 16$ Zeilen f&uuml;r die verschiedenen Funktionswerte. Wir brauchen jeweils eine Spalte f&uuml;r die vier Variablen, eine f&uuml;r den Funktionswert $f(w,x,y,z)$ und am besten noch eine mit der Nummer.</li>
  <li>Nun z&auml;hlen wir f&uuml;r die vier Variablen bin&auml;r hoch. Dabei einsprechen die konkatenierten Ziffern der Variablen der Spalte &bdquo;Nummer&ldquo;. Ich fine es am einfachsten, dies Spaltenweise zu schreiben. Also 8 Nullen, 8 Einsen f&uuml;r $w$. Dann 4 Nullen, 4 Einsen, 4 Nullen, 4 Einsen f&uuml;r $x$ usw.</li>
<li>Als letztes schauen wir uns die drei geklammerten Terme von oben an und schauen, wann diese jeweils Null sind. In die entsprechenden Zeilen der Tabelle tragen wir eine Null ein. In alle &Uuml;brigen kommt eine Eins.</li>
</ol>

<table>
  <thead>
    <tr>
      <th>Nr</th>
      <th>$w$</th>
      <th>$x$</th>
      <th>$y$</th>
      <th>$z$</th>
      <th>$f(w,x,y,z)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>11</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>13</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>14</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>15</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Will man diese Tabelle in ein KV-Diagramm &uuml;bernehmen, muss man nur die Spalte $f(w,x,y,z)$ in der richtigen Reihenfolge in die Tabelle f&uuml;llen. Das macht man, indem man immer bei einem Eckpunkt beginnt und dann eine Z-Form durchgeht:

[caption id="attachment_63191" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map4.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map4-300x236.png" alt="KV-Speed-Zeichnen" width="300" height="236" class="size-medium wp-image-63191" /></a> KV-Speed-Zeichnen[/caption]

Am Ende sieht es so aus:
<img src="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map1.png" alt="KV-Diagramm" width="512" height="512" class="size-full wp-image-62871" />

<h2>Prim- und Kernprimimplikaten</h2>
Sei $g(w,x,y,z)$ eine Schaltfunktion.
$g$ ist ein Implikant von $f:\Leftrightarrow \forall_{(w,x,y,z) \in \{0,1\}^4}: g(w,x,y,z) \Rightarrow f(w,x,y,z)$.

Ist $g$ ist ein Implikant von $f$, so ist $f$ ein Implikat von $g$.


Das kann man nun sehr sch&ouml;n mit dem KV-Diagramm verkn&uuml;pfen. Wenn man die beiden Funktionen $f$ und $g$ in das KV-Diagramm einzeichnet, muss $f$ &uuml;berall dort eine 1 haben, wo $g$ eine 1 hat.

Was hat es nun mit Primimplikanten auf sich? Wenn man diese K&auml;stchen um 1-Bl&ouml;cke macht, dann m&uuml;ssen sie jeweils insgesamt genau $2^k, k \in \mathbb{N}_0$ Einsen umfassen und d&uuml;rfen an den R&auml;ndern fortgesetz werden (siehe der gr&uuml;ne um 5 und 13). Wenn so ein Block ein Primimplikant ist, darf es keinen gr&ouml;&szlig;eren Eins-Block geben.

Beispiel:
[caption id="attachment_62901" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map2.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map2-300x300.png" alt="KV-Diagramm - Beispiel mit Primimplikanten" width="300" height="300" class="size-medium wp-image-62901" /></a> KV-Diagramm - Beispiel mit Primimplikanten[/caption]

Das Rosa-K&auml;stchen ist ein Implikant. Es ist jedoch kein Primimplikant, da das blaue K&auml;stchen gr&ouml;&szlig;er ist. Bis auf das rosa K&auml;stchen und das braune K&auml;stchen sind alle eingezeichenten K&auml;stchen Primimplikanten sein. Es gibt keine weiteren Primimplikanten in dieser Funktion.

Nun ist ein Primimplikant ein Kernprimimplikant, wenn er eine 1 &uuml;berdeckt, die von keinem anderen Primimplikanten &uuml;berdeckt wird. Das gilt f&uuml;r alle Primimplikanten au&szlig;er den hellgr&uuml;nen und den braunen K&auml;stchen.

Nochmals f&uuml;r das Beispiel:

Primimplikanten sind:
<ul>
 <li>(0,1,5,4) // ganz oben, ist auch Kernprimimplikant</li>
 <li>(10,11) // 3. Zeile, ist auch Kernprimimplikant</li>
 <li>(11,15) // 3. Zeile, ist kein Kernprimimplikant</li>
 <li>(15,13) // 3. Spalte, ist kein Kernprimimplikant</li>
 <li>(13,5) // 3. Spalte, ist kein Kernprimimplikant</li>
</ul>

Primimplikate sind:
<ul>
 <li>(2,3,7,6) // 2. Zeile, ist auch Kernprimimplikat</li>
 <li>(6,14) // 4. Spalte, ist kein Kernprimimplikat</li>
 <li>(14,12) //4. Spalte, ist kein Kernprimimplikat</li>
 <li>(8,9) // 4. Zeile, ist auch Kernprimimplikat</li>
 <li>(8, 12) // 4. Zeile, ist kein Kernprimimplikat</li>
</ul>

<h2>Hasards</h2>
Wie sieht man einen Hasard im KV-Diagramm? Man sucht sich eine Anfangsbelegung und eine Endbelegung. Wenn sich dazwischen $n$ Variablen &auml;ndern, gibt es $n!$ Pfade im KV-Diagram. Ist einer dieser Pfade nicht monoton, so ist dieser &Uuml;bergang Hasardbehaftet.

Nun kann man sich entweder die Funktion selbst im KV-Diagramm anschauen, oder die einzelnen Variablen mit dem Todzeitmodell aufsplitten. Untersucht man ersteres, kann man Funktionshasards finden, bei letzterem Strukturhasards.

Nun kann man jeden Hasard noch aufteilen, je nach dem was der Wert der Funktion mit der Anfangsbelegung A bzw. der Wert der Funktion bei der Endbelegung B ist:
<ul>
  <li>$f(A) = 0 \land f(B) = 0 \Rightarrow$ Statischer 0-Hasard</li>
  <li>$f(A) = 0 \land f(B) = 1 \Rightarrow$ Dynamischer 01-Hasard</li>
  <li>$f(A) = 1 \land f(B) = 0 \Rightarrow$ Dynamischer 10-Hasard</li>
  <li>$f(A) = 1 \land f(B) = 1 \Rightarrow$ Statischer 1-Hasard</li>
</ul>

<h3>Beispiel</h3>
Hier ist ein Beispiel f&uuml;r einen dynamischen 1-0-Hasard:

[caption id="attachment_63011" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map3.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/karnaugh-map3-300x251.png" alt="Beispiel eines dynamischen 1-0-Hasards" width="300" height="251" class="size-medium wp-image-63011" /></a> Beispiel eines dynamischen 1-0-Hasards[/caption]

<h2>Fallstricke</h2>
Bei dem Suchen nach Eins- oder Nullbl&ouml;cken darf man an den Spiegelachsen springen:

[caption id="attachment_63151" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/kv-diagramm-fallstrick-1.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/kv-diagramm-fallstrick-1-300x180.png" alt="KV Diagramm: Fallstrick 1" width="300" height="180" class="size-medium wp-image-63151" /></a> KV Diagramm: Fallstrick 1<br />Quelle: <a href="http://ti.ira.uka.de/Klausur/AlteKlausuren/m_ss_10.pdf#page=2">Klausur vom SS 2010 (KIT)</a>[/caption]

[caption id="attachment_63161" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/kv-diagramm-fallstrick-2.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/kv-diagramm-fallstrick-2-300x173.png" alt="KV Diagramm: Fallstrick 2" width="300" height="173" class="size-medium wp-image-63161" /></a> KV Diagramm: Fallstrick 2<br />Quelle: <a href="http://ti.ira.uka.de/Klausur/AlteKlausuren/m_ss_10.pdf#page=2">Klausur vom SS 2010 (KIT)</a>[/caption]
