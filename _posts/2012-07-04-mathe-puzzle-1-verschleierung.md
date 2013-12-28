---
layout: post
status: publish
published: true
title: ! 'Mathe Puzzle #1: Verschleierung'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 29671
wordpress_url: http://martin-thoma.com/?p=29671
date: 2012-07-04 20:54:42.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- Fibonacci
- puzzle
comments:
- id: 176051
  author: ThJ2704
  author_email: ThJ2704@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMi0wNy0wNyAwODo0NjoxNyArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNy0wNyAwNjo0NjoxNyArMDIwMA==
  content: ! "Servus Martin, \r\n\r\ntoller Artikel.\r\nDas Video ist spitze.\r\nEs
    zeigt einem wie tolle Mathe sein kann.\r\nVielen Dank f&uuml;r Deinen Artikel."
featured_image: 2012/07/math-symbol-thumb.png
---
<strong>Die folgende Funktion ist sehr bekannt. Wie lautet ihr Name?</strong>

Seien $\oplus, \otimes: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ Verkn&uuml;fungen auf $\mathbb{R}$ und definiert durch:
$\oplus(a, b) := a + b$
$\otimes(a, b) := a - b$

Sei $O:\mathbb{N} \rightarrow \mathbb{R}$ eine Abbildung und definiert durch 
$O(0) := 0, O(0^0) := 0^0, O(o) := O(o \otimes 0^0) \oplus O(o \otimes 0^0 \otimes 0^0)$.

.
.
.
.
.
.
.

Aufl&ouml;sung gibts weiter unten - die Abbildung ist wirklich sehr bekannt :-)

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

Schreiben wir das doch mal um. Wenn wir schon die normale Addition bzw. Subtraktion des K&ouml;rpers $\mathbb{R}$ benutzen, k&ouml;nnen wir auch die gewohnten Symbole verwenden:
$O:\mathbb{N} \rightarrow \mathbb{R}$
$O(0) := 0, O(0^0) := 0^0, O(o) := O(o - 0^0) + O(o - 0^0 - 0^0)$

Nun sind wir es gewohnt, dass die Funktionen $f$ hei&szlig;en und die Variablen x:
$f:\mathbb{N} \rightarrow \mathbb{R}$
$f(0) := 0, f(0^0) := 0^0, f(x) := f(x - 0^0) + f(x - 0^0 - 0^0)$

Au&szlig;erdem ist $0^0 = 1$:
$f:\mathbb{N} \rightarrow \mathbb{R}$
$f(0) := 0, f(1) := 1, f(x) := f(x - 1) + f(x - 1 - 1)$

Das ist wiederum:
Au&szlig;erdem ist $0^0 = 1$:
$f:\mathbb{N} \rightarrow \mathbb{R}$
$f(0) := 0$, 
$f(1) := 1$, 
$f(x) := f(x - 1) + f(x - 2)$

Diese Folge wird <a href="http://de.wikipedia.org/wiki/Fibonacci-Folge">Fibonacci-Folge</a> genannt. Es ist schon sehr erstaunlich, wie beeinflussbar wir von Symbolen und Konventionen sind.

Und weil sie so sch&ouml;n sind, hier noch ein kurzes Video zu den Fibonacci-Zahlen:
<iframe width="512" height="288" src="http://www.youtube.com/embed/kkGeOWYOFoA" frameborder="0" allowfullscreen></iframe>
