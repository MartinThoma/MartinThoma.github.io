---
layout: post
status: publish
published: true
title: ! '&Uuml;bersicht &uuml;ber Sortieralgorithmen'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 31801
wordpress_url: http://martin-thoma.com/?p=31801
date: 2012-07-15 15:00:12.000000000 +02:00
categories:
- German posts
tags:
- algorithms
- sorting
comments:
- id: 182341
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNy0yNiAwODo1OToxNyArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNy0yNiAwNjo1OToxNyArMDIwMA==
  content: ! "Ich habe gerade gesehen, dass ich etwas zu viel als \"stabil\" bezeichnet
    habe. Nun sollte es stimmen. Alle nicht-stabilen Sortierverfahren kann man stabil
    implementieren. Das ist dann aber auf keinen Fall mehr die typische Form des Algorithmus
    und geht auf Kosten der Laufzeit (allerdings teilweise nur als gro&szlig;e Konstante,
    also nicht im O-Kalk&uuml;l) oder des  zus&auml;tzlich ben&ouml;tigten Speichers.\r\n\r\nDas
    stabil-machen funktioniert so:\r\nMan nutzt ein zus&auml;tzliches Array A, um
    die Indizes der Eingabeschl&uuml;ssel zu speichern. Dann geht man nach dem Sortieralgorithmus
    nochmals durch die liste, schaut ob min. zwei benachbarte Elmente gleich sind.
    Die Menge der gleichen Elemente sortiert man dann nach der Index-Reihenfolge in
    Array A."
---
Eine &Uuml;bersicht &uuml;ber g&auml;ngige Sortieralgorithmen:

<h2>Vergleichsbasiert</h2>
<table>
<tr>
  <th rowspan="2" style="border-bottom: #000 double 3px;">Name</th>
  <th colspan="3" style="background-color:#cf3;text-align:center">Laufzeit</th>
  <th rowspan="2" style="border-bottom: #000 double 3px;">stabil</th>
  <th rowspan="2" style="border-bottom: #000 double 3px;">in-place</th>
</tr>
<tr>
  <th style="background-color:#cf3;border-bottom: #000 double 3px;">B</th>
  <th style="background-color:#cf3;border-bottom: #000 double 3px;">AVG</th>
  <th style="background-color:#cf3;border-bottom: #000 double 3px;">W</th>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Selectionsort">Selectionsort</a></th>
  <td>$\Theta (n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="size-full wp-image-12931" /></a><small>[1]</small></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Bubblesort">Bubblesort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\cal{O}(n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Insertionsort">Insertionsort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\Theta (n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Quicksort">Quicksort</a></th>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Heapsort">Heapsort</a></th>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/no.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Mergesort">Mergesort</a></th>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/no.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a><small>[2]</small></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Timsort">Timsort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/no.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
</tr>
</table>

Ich habe - bis auf Timsort - jeden dieser Algorithmen in Python implementiert, siehe <a href="https://github.com/MartinThoma/algorithms/blob/master/sorting.py">Python-Code f&uuml;r Sortieralgorithmen</a>.

<small>[1]</small>: Beispiel: A = [2, 2, 1]
<small>[2]</small>: in der regel nicht in-place, kann aber auch in-place implementiert werden.

<h2>Nicht Vergleichsbasiert</h2>
Es sei 
<ul>
  <li>$n$ die Anzahl der Zahlen, </li>
  <li>$d$ die maximale Anzahl der Stellen</li>
  <li>$k$ die Anzahl der m&ouml;glichen Zeichen (die Basis).</li>
</ul>

Dann gilt:
<table>
<tr>
  <th style="border-bottom: #000 double 3px;">Name</th>
  <th style="border-bottom: #000 double 3px;text-align:center">Worst-Case Laufzeit</th>
  <th style="border-bottom: #000 double 3px;">stabil</th>
  <th style="border-bottom: #000 double 3px;">in-place</th>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Radixsort">Radixsort</a></th>
  <td>$\cal{O}(d \cdot (n+k))$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/no.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Countingsort">Countingsort</a></th>
  <td>$\cal{O}(n+k)$</td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="http://martin-thoma.com/wp-content/uploads/2012/01/no.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
</tr>
</table>

<h2>Siehe auch</h2>
<ul>
  <li><a href="http://www.sorting-algorithms.com/">Sorting Algorithm Animations</a>: Eine tolle Website, die veranschaulicht, wie verschiedene Sortieralgorithmen funktionieren.</li>
  <li><a href="http://www.youtube.com/watch?v=t8g-iYGHpEA">What different sorting algorithms sound like</a></li>
</ul>
