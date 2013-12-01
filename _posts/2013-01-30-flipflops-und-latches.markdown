---
layout: post
status: publish
published: true
title: Flipflops und Latches
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 55621
wordpress_url: http://martin-thoma.com/?p=55621
date: 2013-01-30 13:12:04.000000000 +01:00
categories:
- German posts
tags:
- Digitaltechnik
- Latch
- Flipflop
comments: []
---
Flipflops und Latches sind 1-bit Datenspeicher. Es gibt sie als synchrone und als asynchrone Varianten, wobei &bdquo;synchron&ldquo; nur bedeutet, dass das Bauteil zus&auml;tzlich einen Takteingang hat. Der wichtigste (und einzige?) Unterschied zwischen Flipflops und Latches ist, dass Flipflops Taktflankengesteuert sind und Latches Pegelgesteuert sind. Das hei&szlig;t, Flipflops k&ouml;nnen nur dann ihren Wert &auml;ndern, wenn der anliegende Takt von 0 auf 1 wechselt. Latches hingegen k&ouml;nnen ihren Wert immer &auml;ndern, wenn der anliegende Takt auf 1 ist. Beide haben die gleichen Ansteuertabellen, k&ouml;nnen aber unterschiedliche Zeitdiagramme haben.

Interesannt sind vor allem die Ansteuertabellen. Dabei darf man sich nicht von der Art, wie diese aufgeschrieben werden, verwirren lassen: $q^t$ ist der Zustand des Flipflops zum Zeitpunkt $t$. Analog dazu ist $q^{t+1}$ der Zustand des Flipflops zum Zeitpunkt $t+1$. Nun steht rechts in der Tabelle, welche Signale man braucht um den Zustand $q^{t+1}$ zu erreichen, wenn man im Zustand $q^t$ ist.

[gallery ids="55771,55781"]

<h2>D-Flipflops</h2>
<abbr title="Delay-Flipflops">D-Flipflops</abbr> ignorieren im Prinzip den aktuellen Zustand und setzt den neuen Zustand einfach auf das d-Signal.

D-Flipflops k&ouml;nnen aus D-Latches erstellt werden:
[caption id="attachment_55641" align="aligncenter" width="542"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/d-flipflop.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/d-flipflop.png" alt="D-Flipflop" width="542" height="182" class="size-full wp-image-55641" /></a> D-Flipflop[/caption]

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
[caption id="attachment_55781" align="aligncenter" width="150"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/d-flipflop1.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/d-flipflop1-150x150.png" alt="D-Flipflop mit Eingang D, unbennanten Takt und Ausgang Q sowie Q negiert." width="150" height="150" class="size-thumbnail wp-image-55781" /></a> D-Flipflop mit Eingang D, unbennanten Takt und Ausgang Q sowie Q negiert.[/caption]
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
[caption id="attachment_55631" align="aligncenter" width="128"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/rs-flipflop.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/rs-flipflop.png" alt="RS-Flipflop" width="128" height="128" class="size-full wp-image-55631" /></a> RS-Flipflop[/caption]
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
[caption id="attachment_55831" align="aligncenter" width="150"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/t-flipflop.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/t-flipflop-150x150.png" alt="T-Flipflop mit Eingang T, unbenanntem Taktsignal, Ausgang Q und dem negiertem Ausgang Q." width="150" height="150" class="size-thumbnail wp-image-55831" /></a> T-Flipflop mit Eingang T, unbenanntem Taktsignal, Ausgang Q und dem negiertem Ausgang Q.[/caption]
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
[caption id="attachment_55851" align="aligncenter" width="150"]<a href="http://martin-thoma.com/wp-content/uploads/2013/01/jk-flipflop.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/01/jk-flipflop-150x150.png" alt="JK-Flipflop" width="150" height="150" class="size-thumbnail wp-image-55851" /></a> JK-Flipflop[/caption]
</td>
</tr>
</table>
