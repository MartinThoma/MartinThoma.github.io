---
layout: post
lang: en
title: How do Bitmasks work?
slug: how-do-bitmasks-work
author: Martin Thoma
date: 2012-05-18 23:02:55.000000000 +02:00
category: Code
tags: C, OS, Operating Systems
featured_image: 2012/05/assembly-thumb.png
---
<h2>What are Bitmasks?</h2>
In computer science, a <a href="http://en.wikipedia.org/wiki/Mask_(computing)">mask</a> is data that is used for bitwise operations. Essentially it is a variable.

They are very often used in C programs.

<h2>Bit operators</h2>
These are the bit operators:

<ul>
  <li>~ Bitwise NOT (not to be confused with Logical NOT &lsquo;!&rsquo;)</li>
  <li>& Bitwise AND (not to be confused with Logical AND &lsquo;&&&rsquo;)</li>
  <li>| Bitwise OR (again, not to be confused with Logical OR &lsquo;||&rsquo;)</li>
  <li>^ Bitwise XOR</li>
  <li><< Bitwise left shift</li>
  <li>>> Bitwise right shift</li>
</ul>

This is how the operators work:
<table style="border:1px solid black;" border="1">
<tr style="background-color:#ccff99">
    <th>Bit A</th>
    <th style="border-right:1px solid #000;">Bit B</th>
    <th>A & B</th>
    <th>A | B</th>
    <th style="border-right:1px solid #000;">A ^ B</th>
    <th style="border-right:1px solid #000;">~A</th>
    <th>A << B</th>
    <th>A >> B</th>
</tr>
<tr style="background-color:#ffffcc;">
    <td>0</td>
    <td style="border-right:1px solid #000;">0</td>
    <td>0</td>
    <td>0</td>
    <td style="border-right:1px solid #000;">0</td>
    <td style="border-right:1px solid #000;">1</td>
    <td>0</td>
    <td>0</td>
</tr>
<tr>
    <td>0</td>
    <td style="border-right:1px solid #000;">1</td>
    <td>0</td>
    <td>1</td>
    <td style="border-right:1px solid #000;">1</td>
    <td style="border-right:1px solid #000;">1</td>
    <td>0</td>
    <td>0</td>
</tr>
<tr style="background-color:#ffffcc;">
    <td>1</td>
    <td style="border-right:1px solid #000;">0</td>
    <td>0</td>
    <td>1</td>
    <td style="border-right:1px solid #000;">1</td>
    <td style="border-right:1px solid #000;">0</td>
    <td>1</td>
    <td>1</td>
</tr>
<tr>
    <td>1</td>
    <td style="border-right:1px solid #000;">1</td>
    <td>1</td>
    <td>1</td>
    <td style="border-right:1px solid #000;">0</td>
    <td style="border-right:1px solid #000;">0</td>
    <td>2</td>
    <td>0</td>
</tr>
</table>

<h2>Some examples</h2>
Lets say I have any variable named "variable" with 32 bit.

Get the last bit:
```c
return variable &amp; 1;
```

Get the first bit:
```c
return variable >> 31;
```

Get the bits 4 - 14 (11 bits):
```c
return (variable  >> 4) &amp; ((1<<11) - 1);
```

Getting the pow(2,11):
```c
return 1<<11;
```

<h2>See also</h2>
<ul>
  <li><a href="http://stackoverflow.com/questions/231760/what-does-a-type-followed-by-t-underscore-t-represent/231807#231807">What does a type followed by _t (underscore-t) represent?</a>. Jonathan Leffler, Stackoverflow.</li>
  <li><a href="http://stackoverflow.com/a/9602958/562769">Why does mode_t use 4 byte?</a>. Niklas B., Stackoverflow.</li>
</ul>
