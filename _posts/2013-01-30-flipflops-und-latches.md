---
layout: post
title: Flipflops und Latches
author: Martin Thoma
date: 2013-01-30 13:12:04.000000000 +01:00
category: German posts
tags: Digitaltechnik, Latch, Flipflop
featured_image: 2013/01/rs-flipflop.png
---
Flipflops und Latches sind 1-bit Datenspeicher. Es gibt sie als synchrone und als asynchrone Varianten, wobei &bdquo;synchron&ldquo; nur bedeutet, dass das Bauteil zus&auml;tzlich einen Takteingang hat. Der wichtigste (und einzige?) Unterschied zwischen Flipflops und Latches ist, dass Flipflops Taktflankengesteuert sind und Latches Pegelgesteuert sind. Das hei&szlig;t, Flipflops k&ouml;nnen nur dann ihren Wert &auml;ndern, wenn der anliegende Takt von 0 auf 1 wechselt. Latches hingegen k&ouml;nnen ihren Wert immer &auml;ndern, wenn der anliegende Takt auf 1 ist. Beide haben die gleichen Ansteuertabellen, k&ouml;nnen aber unterschiedliche Zeitdiagramme haben.

Interesannt sind vor allem die Ansteuertabellen. Dabei darf man sich nicht von der Art, wie diese aufgeschrieben werden, verwirren lassen: $q^t$ ist der Zustand des Flipflops zum Zeitpunkt $t$. Analog dazu ist $q^{t+1}$ der Zustand des Flipflops zum Zeitpunkt $t+1$. Nun steht rechts in der Tabelle, welche Signale man braucht um den Zustand $q^{t+1}$ zu erreichen, wenn man im Zustand $q^t$ ist.

<ul class="gallery mw-gallery-traditional">
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/01/d-latch.png" class="image">
                  <img src="../images/2013/01/d-latch.png" alt="D-Latch" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">D-Latch</div>
      </div>
   </li>
   <li class="gallerybox" style="width: 155px">
      <div style="width: 155px">
         <div class="thumb" style="width: 150px;">
            <div style="margin:21px auto;height: 113px;line-height: 150px;">
               <a href="../images/2013/01/d-flipflop1.png" class="image">
                  <img src="../images/2013/01/d-flipflop1.png" alt="D-Flipflop" style="max-width: 120px; max-height: 120px;">
               </a>
            </div>
         </div>
         <div class="gallerytext">D-Flipflop</div>
      </div>
   </li>
</ul>

<h2>D-Flipflops</h2>
<abbr title="Delay-Flipflops">D-Flipflops</abbr> ignorieren im Prinzip den aktuellen Zustand und setzt den neuen Zustand einfach auf das d-Signal.

D-Flipflops k&ouml;nnen aus D-Latches erstellt werden:
<figure class="aligncenter">
            <a href="../images/2013/01/d-flipflop.png"><img src="../images/2013/01/d-flipflop.png" alt="D-Flipflop" style="max-width:542px;max-height:182px" class="size-full wp-image-55641"/></a>
            <figcaption class="text-center">D-Flipflop</figcaption>
        </figure>

<h3>Ansteuertabelle</h3>
<table>
<tr>
<td>
<table style="width:auto">
  <tr>
    <th style="border-bottom:1px solid black;">$q^t$</th>
    <th style="border-bottom:1px solid black;border-right: 1px solid black;">$q^{t+1}$</th>
    <th style="border-bottom:1px solid black;">$d^t$</th>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>1</td>
  </tr>
</table>
</td>
<td>
<figure class="aligncenter">
            <a href="../images/2013/01/d-flipflop1-150x150.png"><img src="../images/2013/01/d-flipflop1-150x150.png" alt="D-Flipflop mit Eingang D, unbennanten Takt und Ausgang Q sowie Q negiert." style="max-width:150px;max-height:150px" class="size-thumbnail wp-image-55781"/></a>
            <figcaption class="text-center">D-Flipflop mit Eingang D, unbennanten Takt und Ausgang Q sowie Q negiert.</figcaption>
        </figure>
</td>
</tr>
</table>


<h2>RS-Flipflops</h2>
Das <abbr title="Reset-Set-Flipflop">RS-Flipflop</abbr> bietet zwei M&ouml;glichkeiten: Entweder man resettet es, dann wird der neue Zustand 0, oder man setzt es. Dann ist der neue Zustand 1.

Ein RS-Flipflop hat zwei Eing&auml;nge und einen oder zwei Ausg&auml;nge.

<h3>Ansteuertabelle</h3>
<table>
<tr>
<td>
<table style="width:auto">
  <tr>
    <th style="border-bottom:1px solid black;">$q^t$</th>
    <th style="border-bottom:1px solid black;border-right: 1px solid black;">$q^{t+1}$</th>
    <th style="border-bottom:1px solid black;">$r^t$</th>
    <th style="border-bottom:1px solid black;">$s^t$</th>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>-</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>0</td>
    <td>-</td>
  </tr>
</table>
</td>
<td>
<figure class="aligncenter">
            <a href="../images/2013/01/rs-flipflop.png"><img src="../images/2013/01/rs-flipflop.png" alt="RS-Flipflop" style="max-width:128px;max-height:128px" class="size-full wp-image-55631"/></a>
            <figcaption class="text-center">RS-Flipflop</figcaption>
        </figure>
</td>
</tr>
</table>

<h2>T-Flipflop</h2>
<abbr title="Toggle-Flipflop">T-Flipflops</abbr> wechseln den Zustand, wenn T gesetzt ist.

<h3>Ansteuertabelle</h3>
<table>
<tr>
<td>
<table style="width:auto">
  <tr>
    <th style="border-bottom:1px solid black;">$q^t$</th>
    <th style="border-bottom:1px solid black;border-right: 1px solid black;">$q^{t+1}$</th>
    <th style="border-bottom:1px solid black;">$T^t$</th>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>0</td>
  </tr>
</table>
</td>
<td>
<figure class="aligncenter">
            <a href="../images/2013/01/t-flipflop-150x150.png"><img src="../images/2013/01/t-flipflop-150x150.png" alt="T-Flipflop mit Eingang T, unbenanntem Taktsignal, Ausgang Q und dem negiertem Ausgang Q." style="max-width:150px;max-height:150px" class="size-thumbnail wp-image-55831"/></a>
            <figcaption class="text-center">T-Flipflop mit Eingang T, unbenanntem Taktsignal, Ausgang Q und dem negiertem Ausgang Q.</figcaption>
        </figure>
</td>
</table>

<h2>JK-Flipflop</h2>
<abbr title="Jump-/Kill-Flipflops">JK-Flipflops</abbr> haben zwei Eing&auml;nge, &bdquo;J&ldquo; und &bdquo;K&ldquo;. Warum die allerdings Jump und Kill genannt werden, ist mir nicht klar. Habt ihr eine Merkregel f&uuml;r die Ansteuertabelle dieses Flipflops?

<h3>Ansteuertabelle</h3>
<table>
<tr>
<td>
<table style="width:auto">
  <tr>
    <th style="border-bottom:1px solid black;">$q^t$</th>
    <th style="border-bottom:1px solid black;border-right: 1px solid black;">$q^{t+1}$</th>
    <th style="border-bottom:1px solid black;">$j^t$</th>
    <th style="border-bottom:1px solid black;">$k^t$</th>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>0</td>
    <td>-</td>
  </tr>
  <tr>
    <td>0</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>1</td>
    <td>-</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">0</td>
    <td>-</td>
    <td>1</td>
  </tr>
  <tr>
    <td>1</td>
    <td style="border-right: 1px solid black;">1</td>
    <td>-</td>
    <td>0</td>
  </tr>
</table>
</td>
<td>
<figure class="aligncenter">
            <a href="../images/2013/01/jk-flipflop-150x150.png"><img src="../images/2013/01/jk-flipflop-150x150.png" alt="JK-Flipflop" style="max-width:150px;max-height:150px" class="size-thumbnail wp-image-55851"/></a>
            <figcaption class="text-center">JK-Flipflop</figcaption>
        </figure>
</td>
</tr>
</table>
