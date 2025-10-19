---
layout: post
title: KV-Diagramme
slug: kv-diagramme
lang: de
author: Martin Thoma
date: 2013-03-25 23:37:00.000000000 +01:00
category: German posts
tags: Digitaltechnik
featured_image: 2013/03/karnaugh-map-300x300.png
---
<div class="info">Ich setze im Folgenden vorraus, dass man schon mal was von KV-Diagrammen gehört hat und vielleicht schon ein paar gezeichnet hat. Insbesondere erkläre ich nicht wie man aus dem KV-Diagramm der Größe 16 eines der Größe 32 bekomt und was die Beschriftung bedeutet.</div>

KV-Diagramme sind für die TI-Klausur am KIT bei Herrn Prof. Dr. Asfour sehr wichtig. Im folgenden sind die wichtigsten Eigenschaften, die so explizit leider nicht in der Vorlesung genannt wurden.

<h2>Konstruktion aus Schaltfunktion</h2>
Gegeben sei folgende vollständig definierte Schaltfunktion:
$f(w,x,y,z) := (w \lor \bar y) (\bar w \lor x \lor y) (\bar w \lor \bar x \lor z)$

Nun kann man eine Funktionstabelle aufstellen:
<ol>
  <li>Dabei schreibt man sich erst das Gerüst hin, also eine Titelzeile mit den vier Variablen $w,x,y,z$ und $2^4 = 16$ Zeilen für die verschiedenen Funktionswerte. Wir brauchen jeweils eine Spalte für die vier Variablen, eine für den Funktionswert $f(w,x,y,z)$ und am besten noch eine mit der Nummer.</li>
  <li>Nun zählen wir für die vier Variablen binär hoch. Dabei einsprechen die konkatenierten Ziffern der Variablen der Spalte &bdquo;Nummer&ldquo;. Ich fine es am einfachsten, dies Spaltenweise zu schreiben. Also 8 Nullen, 8 Einsen für $w$. Dann 4 Nullen, 4 Einsen, 4 Nullen, 4 Einsen für $x$ usw.</li>
<li>Als letztes schauen wir uns die drei geklammerten Terme von oben an und schauen, wann diese jeweils Null sind. In die entsprechenden Zeilen der Tabelle tragen wir eine Null ein. In alle Übrigen kommt eine Eins.</li>
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

Will man diese Tabelle in ein KV-Diagramm übernehmen, muss man nur die Spalte $f(w,x,y,z)$ in der richtigen Reihenfolge in die Tabelle füllen. Das macht man, indem man immer bei einem Eckpunkt beginnt und dann eine Z-Form durchgeht:

<figure class="aligncenter">
            <a href="../images/2013/03/karnaugh-map4-300x236.png"><img src="../images/2013/03/karnaugh-map4-300x236.png" alt="KV-Speed-Zeichnen" style="max-width:300px;max-height:236px" class="size-medium wp-image-63191"/></a>
            <figcaption class="text-center">KV-Speed-Zeichnen</figcaption>
        </figure>

Am Ende sieht es so aus:
<img src="../images/2013/03/karnaugh-map1.png" alt="KV-Diagramm" width="512" height="512" class="size-full wp-image-62871" />

<h2>Prim- und Kernprimimplikaten</h2>
Sei $g(w,x,y,z)$ eine Schaltfunktion.
$g$ ist ein Implikant von $f:\Leftrightarrow \forall_{(w,x,y,z) \in \{0,1\}^4}: g(w,x,y,z) \Rightarrow f(w,x,y,z)$.

Ist $g$ ist ein Implikant von $f$, so ist $f$ ein Implikat von $g$.


Das kann man nun sehr schön mit dem KV-Diagramm verknüpfen. Wenn man die beiden Funktionen $f$ und $g$ in das KV-Diagramm einzeichnet, muss $f$ überall dort eine 1 haben, wo $g$ eine 1 hat.

Was hat es nun mit Primimplikanten auf sich? Wenn man diese Kästchen um 1-Blöcke macht, dann müssen sie jeweils insgesamt genau $2^k, k \in \mathbb{N}_0$ Einsen umfassen und dürfen an den Rändern fortgesetz werden (siehe der grüne um 5 und 13). Wenn so ein Block ein Primimplikant ist, darf es keinen größeren Eins-Block geben.

Beispiel:
<figure class="aligncenter">
            <a href="../images/2013/03/karnaugh-map2-300x300.png"><img src="../images/2013/03/karnaugh-map2-300x300.png" alt="KV-Diagramm - Beispiel mit Primimplikanten" style="max-width:300px;max-height:300px" class="size-medium wp-image-62901"/></a>
            <figcaption class="text-center">KV-Diagramm - Beispiel mit Primimplikanten</figcaption>
        </figure>

Das Rosa-Kästchen ist ein Implikant. Es ist jedoch kein Primimplikant, da das blaue Kästchen größer ist. Bis auf das rosa Kästchen und das braune Kästchen sind alle eingezeichenten Kästchen Primimplikanten sein. Es gibt keine weiteren Primimplikanten in dieser Funktion.

Nun ist ein Primimplikant ein Kernprimimplikant, wenn er eine 1 überdeckt, die von keinem anderen Primimplikanten überdeckt wird. Das gilt für alle Primimplikanten außer den hellgrünen und den braunen Kästchen.

Nochmals für das Beispiel:

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
Wie sieht man einen Hasard im KV-Diagramm? Man sucht sich eine Anfangsbelegung und eine Endbelegung. Wenn sich dazwischen $n$ Variablen ändern, gibt es $n!$ Pfade im KV-Diagram. Ist einer dieser Pfade nicht monoton, so ist dieser Übergang Hasardbehaftet.

Nun kann man sich entweder die Funktion selbst im KV-Diagramm anschauen, oder die einzelnen Variablen mit dem Todzeitmodell aufsplitten. Untersucht man ersteres, kann man Funktionshasards finden, bei letzterem Strukturhasards.

Nun kann man jeden Hasard noch aufteilen, je nach dem was der Wert der Funktion mit der Anfangsbelegung A bzw. der Wert der Funktion bei der Endbelegung B ist:
<ul>
  <li>$f(A) = 0 \land f(B) = 0 \Rightarrow$ Statischer 0-Hasard</li>
  <li>$f(A) = 0 \land f(B) = 1 \Rightarrow$ Dynamischer 01-Hasard</li>
  <li>$f(A) = 1 \land f(B) = 0 \Rightarrow$ Dynamischer 10-Hasard</li>
  <li>$f(A) = 1 \land f(B) = 1 \Rightarrow$ Statischer 1-Hasard</li>
</ul>

<h3>Beispiel</h3>
Hier ist ein Beispiel für einen dynamischen 1-0-Hasard:

<figure class="aligncenter">
            <a href="../images/2013/03/karnaugh-map3-300x251.png"><img src="../images/2013/03/karnaugh-map3-300x251.png" alt="Beispiel eines dynamischen 1-0-Hasards" style="max-width:300px;max-height:251px" class="size-medium wp-image-63011"/></a>
            <figcaption class="text-center">Beispiel eines dynamischen 1-0-Hasards</figcaption>
        </figure>

<h2>Fallstricke</h2>
Bei dem Suchen nach Eins- oder Nullblöcken darf man an den Spiegelachsen springen:

<figure class="aligncenter">
            <a href="../images/2013/03/kv-diagramm-fallstrick-1-300x180.png"><img src="../images/2013/03/kv-diagramm-fallstrick-1-300x180.png" alt="KV Diagramm: Fallstrick 1" style="max-width:300px;max-height:180px" class="size-medium wp-image-63151"/></a>
            <figcaption class="text-center">KV Diagramm: Fallstrick 1<br />Quelle: <a href='http://ti.ira.uka.de/Klausur/AlteKlausuren/m_ss_10.pdf#page=2'>Klausur vom SS 2010 (KIT)</a></figcaption>
        </figure>

<figure class="aligncenter">
            <a href="../images/2013/03/kv-diagramm-fallstrick-2-300x173.png"><img src="../images/2013/03/kv-diagramm-fallstrick-2-300x173.png" alt="KV Diagramm: Fallstrick 2" style="max-width:300px;max-height:173px" class="size-medium wp-image-63161"/></a>
            <figcaption class="text-center">KV Diagramm: Fallstrick 2<br />Quelle: <a href='http://ti.ira.uka.de/Klausur/AlteKlausuren/m_ss_10.pdf#page=2'>Klausur vom SS 2010 (KIT)</a></figcaption>
        </figure>
