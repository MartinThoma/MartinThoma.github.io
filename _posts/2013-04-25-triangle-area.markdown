---
layout: post
status: publish
published: true
title: Triangle area
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 64181
wordpress_url: http://martin-thoma.com/?p=64181
date: 2013-04-25 10:13:15.000000000 +02:00
categories:
- My bits and bytes
tags:
- mathematics
comments:
- id: 1184621
  author: Mike
  author_email: mike@turbogeek421.co.uk
  author_url: http://www.turbogeek421.co.uk
  date: !binary |-
    MjAxMy0wNC0yNSAxMDoxOTozMCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yNSAwODoxOTozMCArMDIwMA==
  content: Points for showing your working out, but -2 for incorrectly labelling your
    diagram. ;)
- id: 1184631
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNC0yNSAxMDozOTozOSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yNSAwODozOTozOSArMDIwMA==
  content: Thank you for your comment. I've corrected the typo.
- id: 1186711
  author: Hsn
  author_email: hassen.benayed@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0yOSAwOTo0NDoxMSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yOSAwNzo0NDoxMSArMDIwMA==
  content: The diagram would be much more intuitive if each triangle is shown as a
    set of two triangle of 3x4x5 side to side (but the side varies)
- id: 1186731
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNC0yOSAxMDowMToxMyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0yOSAwODowMToxMyArMDIwMA==
  content: I'm sorry, I don't understand what you mean. Could you make a scribble,
    upload it e.g. to http://imgur.com/ and post another comment, please?
- id: 1187001
  author: Platty
  author_email: plattytehpwn@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0zMCAwNjoxMDo1NiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0zMCAwNDoxMDo1NiArMDIwMA==
  content: Just draw two 3-4-5 triangles that share the side of length 4 and two 3-4-5
    triangles that share the side of length 3.  These triangles formed are equivalent
    to the 5-5-6 and 5-5-8 triangles, respectively, demonstrating that they have the
    same area.
- id: 1187591
  author: kmwho
  author_email: iamkmwho@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0wMyAwODo1MDoyMCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0wMyAwNjo1MDoyMCArMDIwMA==
  content: You can divide both the (isosceles) triangles into two equal right triangles
    of 3x4x5, and depending on whether you place them side by side with common side
    as 4 or 3 you get the first or second triangle
featured_image: 2013/04/triangle-heron-tricky-thumb.png
---
I've just seen the following image on spikedmath.com:

{% caption align="aligncenter" width="512" caption="Some geometry questions.<br />Source: <a href="http://spikedmath.com/549.html">spikedmath.com</a>" url="../images/2013/04/549-simple-area-quizz.png" alt="Some geometry questions" title="" height="109" class="size-full wp-image-64221" %}

The second answers seem to be obviously the correct ones, right? Wrong.

According to <a href="http://en.wikipedia.org/wiki/Heron%27s_formula">Heron's formula</a> you can calculate a triangles area like this:

Let $a, b, c$ be the side lengths of the triangle.
$s := \frac{a+b+c}{2}$
$T = \sqrt{s \cdot (s-a) \cdot (s-b) \cdot (s-c)}$

So the area of the first triangle is
$s_1 := \frac{16}{2} = 8$
$T_1 := \sqrt{8 \cdot (8-5) \cdot (8-5) \cdot (8-6)} = \sqrt{8 \cdot 3 \cdot 3 \cdot 2} = 3 \cdot 4 = 12$

The area of the second one is
$s_1 := \frac{18}{2} = 9$
$T_1 := \sqrt{9 \cdot (9-5) \cdot (9-5) \cdot (9-8)} = \sqrt{9 \cdot 4 \cdot 4 \cdot 1} = 3 \cdot 4 = 12$

Both triangles have the same area!

When you draw it, it looks like this:

{% caption align="aligncenter" width="512" caption="Both triangles in one picture" url="../images/2013/04/triangle-heron-tricky1.png" alt="Both triangles in one picture" title="" height="423" class="size-full wp-image-64341" %}
