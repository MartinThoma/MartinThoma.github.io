---
layout: post
title: ! '&Uuml;bersicht &uuml;ber Sortieralgorithmen'
author: Martin Thoma
date: 2012-07-15 15:00:12.000000000 +02:00
category: German posts
tags: algorithms, sorting
featured_image: 2012/07/insertion-sort-thumb.png
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
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="size-full wp-image-12931" /></a><small>[1]</small></td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Bubblesort">Bubblesort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\cal{O}(n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Insertionsort">Insertionsort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\Theta (n^2)$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Quicksort">Quicksort</a></th>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n^2)$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Heapsort">Heapsort</a></th>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td><a href="../images/2012/01/no.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Mergesort">Mergesort</a></th>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td>$\Theta (n \cdot log(n))$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="../images/2012/01/no.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a><small>[2]</small></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Timsort">Timsort</a></th>
  <td>$\Theta (n)$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td>$\cal{O}(n \cdot log(n))$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></td>
  <td><a href="../images/2012/01/no.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
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
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="../images/2012/01/no.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
</tr>
<tr>
  <th><a href="http://de.wikipedia.org/wiki/Countingsort">Countingsort</a></th>
  <td>$\cal{O}(n+k)$</td>
  <td><a href="../images/2012/01/yes.png"><img src="../images/2012/01/yes.png" alt="yes" title="yes" width="13" height="13" class="size-full wp-image-12931" /></a></td>
  <td><a href="../images/2012/01/no.png"><img src="../images/2012/01/no.png" alt="no" title="no" width="13" height="13" class="alignnone size-full wp-image-12961" /></a></td>
</tr>
</table>

<h2>Siehe auch</h2>
<ul>
  <li><a href="http://www.sorting-algorithms.com/">Sorting Algorithm Animations</a>: Eine tolle Website, die veranschaulicht, wie verschiedene Sortieralgorithmen funktionieren.</li>
  <li><a href="http://www.youtube.com/watch?v=t8g-iYGHpEA">What different sorting algorithms sound like</a></li>
</ul>
