---
layout: post
title: Trickreiche Matheaufgaben
author: Martin Thoma
date: 2014-12-30 21:30
category: German posts
tags: mathematics
featured_image:
---

<div class="info">This is a quick article I had for quite a while as a draft.
It might not be finished or have other problems, but I still want to share
it.</div>

Ich finde immer wieder ein paar einfache, aber irgendwie trickreiche Matheaufgaben. Was genau ich damit meine, seht ihr am besten am folgendem Beispiel.

<h2>Wechselgeld</h2>
<h3>Aufgabe</h3>
<blockquote>Drei Kinder haben je 10 Euro und kaufen sich dafür gemeinsam einen Ball für 30 Euro. Nach dem Verkauf stellt der Ladeninhaber fest, dass der Ball nur 25 Euro kostet und schickt seinen Lehrling mit den überzähligen 5 Euro den Kindern nach. Der Lehrling gibt jedem Kind 1 Euro und behält für seine Bemühungen die restlichen 2 Euro. Damit hat jedes Kind nur 9 Euro für den Ball bezahlt, insgesamt zahlten die Kinder 27 Euro. Mit den 2 Euro des Lehrlings ergibt das aber erst 29 Euro.</blockquote>
Quelle: <a href="http://dsm-faq.wikidot.com/denksport">dsm-faq.wikidot.com/denksport</a>

<h3>Auflösung</h3>
Das Problem dieser Aufgabe ist, dass man sich nicht klar macht, wo man hin will. Man will scheinbar herausfinden, wo das Geld geblieben ist. Das vermischt man aber mit dem Geld, das man hatte:

Situation vor dem Kauf:
<ul>
<li>Kinder: je 10 Euro</li>
<li>Lehrling: 0 Euro</li>
<li>Ladeninhaber: 0 Euro</li>

Situation nach der Geschichte:
<ul>
<li>3 Kinder: je 1 Euro</li>
<li>Lehrling: 2 Euro</li>
<li>Ladeninhaber: 25 Euro</li>
</ul>

Der Lehrling ist also derjenige, der das Problem trickreich macht, wenn man nicht aufpasst. Er bestiehlt die Kinder, deshalb zahlen sie praktisch 27 Euro anstelle der 25 Euro und von diesen 27 Euro hat der Ladeninhaber 25 Euro.

<h2>Mücke und Elefant</h2>
<h3>Aufgabenstellung</h3>
<blockquote>Sei $x$ das Gewicht des Elefanten und $y$ das Gewicht der Mücke. Sei $d$ der Unterschied.<br/>

\begin{align}
x             &= y + d | \cdot (x-y)\\
x^2 - xy      &= xy + xd - y^2 - yd | -xd \\
x^2 - xy - xd &= xy - y^2 - yd\\
x(x-y-d)      &= y \cdot (x-y-d) |:(x-y-d)\\
x             &=y
\end{align}

Das Gewicht der Mücke ist also gleich dem Gewicht des Elefanten!</blockquote>
Quelle: <a href="http://dsm-faq.wikidot.com/denksport">dsm-faq.wikidot.com/denksport</a>

<h3>Auflösung</h3>
Es empfiehlt sich, wie immer bei Umformungen, sich klar zu machen durch was man teilt. Es gilt: $(x-y-d) = 0$, es wurde also durch 0 geteilt. Dabei passieren schlimme Dinge. Unter anderem kann man aus einer Mücke einen Elefanten machen 😉

<h2>Jeder Mensch hat sein Idealgewicht</h2>
<h3>Aufgabenstellung</h3>
Sei $x$ das Körpergewicht in kg eines Menschen, $y$ sein Idealgewicht und $u$ das Übergewicht. Bei Untergewicht kann u also auch negativ sein!

Dann gilt offensichtlich:
$x = y + u$

Nun kann man umformen:
\begin{align}
                x             &= y + u | \cdot (x - y)\\
\Leftrightarrow x^2 - xy      &= xy + xu - y^2 - uy | -xu\\
\Leftrightarrow x^2 - xy - xu &= xy - y^2 - uy\\
\Leftrightarrow x \cdot (x - y - u) &= y \cdot (x - y - u) | : (x-y-u)\\
\Leftrightarrow x &= y
\end{align}

Jeder Mensch hat also sein Idealgewicht!

<h3>Auflösung</h3>
Das Problem der Umformung ist das Gleiche wie oben: $(x-y-u) = 0$.
