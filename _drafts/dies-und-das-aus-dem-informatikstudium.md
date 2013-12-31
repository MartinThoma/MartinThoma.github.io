---
layout: post
title: Dies und Das aus dem Informatikstudium
author: Martin Thoma
date: 2012-08-07 07:21:09
categories: 
- German posts
tags: []
featured_image: 2011/11/computer-fix-it-guy.jpg
---
<h2>XOR ist kommutativ und assoziativ</h2>
<a href="http://de.wikipedia.org/wiki/Kontravalenz">XOR</a> ist auf [latex]\mathbb{Z}/ 2 \mathbb{Z}[/latex] folgendermaßen definiert: 
<table>
<tr>
  <th>a</th><th>b</th>
  <th>a XOR b</th>
</tr>
<tr>
  <td>0</td><td>0</td>
  <td>0</td>
</tr>
<tr>
  <td>0</td><td>1</td>
  <td>1</td>
</tr>
<tr>
  <td>1</td><td>0</td>
  <td>1</td>
</tr>
<tr>
  <td>1</td><td>1</td>
  <td>0</td>
</tr>
</table>

Direkt aus dieser Tabelle folgt, dass XOR <a href="http://de.wikipedia.org/wiki/Kommutativgesetz">kommutativ</a> ist. Es gilt also: [latex]a~XOR~b = b~XOR~a[/latex].

Stellt man die folgende Tabelle auf, sieht man das XOR auch assoziativ ist:
<table>
<tr>
  <th>a</th><th>b</th><th style="border-right: 1px solid #000;">c</th>
  <th>b XOR c</th>
  <th>a XOR<br/>(b XOR c)</th>
  <th>a XOR b</th>
  <th>(a XOR b)<br/>XOR c</th>
</tr>
<tr>
  <td>0</td><td>0</td><td style="border-right: 1px solid #000;">0</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">0</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">0</td>
</tr>
<tr>
  <td>0</td><td>0</td><td style="border-right: 1px solid #000;">1</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">1</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">1</td>
</tr>
<tr>
  <td>0</td><td>1</td><td style="border-right: 1px solid #000;">0</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">1</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">1</td>
</tr>
<tr>
  <td>0</td><td>1</td><td style="border-right: 1px solid #000;">1</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">0</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">0</td>
</tr>
<tr>
  <td>1</td><td>0</td><td style="border-right: 1px solid #000;">0</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">1</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">1</td>
</tr>
<tr>
  <td>1</td><td>0</td><td style="border-right: 1px solid #000;">1</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">0</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">0</td>
</tr>
<tr>
  <td>1</td><td>1</td><td style="border-right: 1px solid #000;">0</td>
  <td>1</td>
  <td style="background-color:#cdcdcd;">0</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">0</td>
</tr>
<tr>
  <td>1</td><td>1</td><td style="border-right: 1px solid #000;">1</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">1</td>
  <td>0</td>
  <td style="background-color:#cdcdcd;">1</td>
</tr>
</table>

Das bedeutet: [latex](a~XOR~b)~XOR~c = a~XOR~(b~XOR~c)[/latex]

Aus alldem zusammen folgt: Wenn man n Variablen mit XOR verknüpft, kann man sich die Ausführungsreihenfolge aussuchen. Man braucht eigentlich sogar nur die 1er Zählen und diese Zahl modulo 2 nehmen.

Das Symbol dafür ist übrigens, laut meinem Skript für Lineare Algebra von Prof. Dr. Leuzinger, [latex]\veebar[/latex].