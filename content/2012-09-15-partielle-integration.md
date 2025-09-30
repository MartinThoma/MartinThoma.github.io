---
layout: post
lang: de
title: Partielle Integration
author: Martin Thoma
date: 2012-09-15 19:02:03.000000000 +02:00
category: German posts
tags: mathematics, analysis, Integral calculus
featured_image: 2012/09/partielle-integration.png
---
Die partielle Integration bietet eine sch&ouml;ne M&ouml;glichkeit, Stammfunktionen von Integralen zu bestimmen. Dazu muss man folgende Regel k&ouml;nnen:

Seien $f, g$ stetig differenzierbare Funktionen.

$\displaystyle \int_a^b f'(x)\cdot g(x)\,\mathrm{d}x = \left [f(x)\cdot g(x) \right ]_{a}^{b} - \int_a^b f(x)\cdot g'(x)\,\mathrm{d}x$.

<h2>Beispiel</h2>
Folgendes <a href="http://de.wikipedia.org/wiki/Partielle_Integration#Beispiel_1">Beispiel aus Wikipedia</a> zeigt, wie man das geschickt nutzen kann:

<strong>Aufgabe</strong>:
Berechne $\int \sin(x) \cdot \cos(x) \,\mathrm{d}x$

<strong>L&ouml;sung</strong>:
Es sei $f(x) = \cos(x)$ und $g'(x)= \sin(x)$.
Es gilt: $f'(x) = - \sin(x)$ und $g(x)= - \cos(x)$.

Durch partielle Integration erh&auml;lt man:
$\int \sin(x) \cdot \cos(x) \,\mathrm{d}x = -\cos^2(x) - \int \sin(x) \cdot \cos(x) \,\mathrm{d}x. $


Addiert man auf beiden Seiten der Gleichung das Ausgangsintegral, ergibt sich:
\begin{align}
              2 \int \sin(x) \cdot \cos(x) \,\mathrm{d}x &= - \cos^2(x)\\
\Leftrightarrow \int \sin(x) \cdot \cos(x) \,\mathrm{d}x &= -\tfrac12\cos^2(x)
\end{align}
