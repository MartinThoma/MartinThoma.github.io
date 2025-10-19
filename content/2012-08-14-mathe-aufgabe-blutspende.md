---
layout: post
title: Mathe-Aufgabe: Blutspende
slug: mathe-aufgabe-blutspende
lang: de
author: Martin Thoma
date: 2012-08-14 17:00:16.000000000 +02:00
category: German posts
tags: mathematics
featured_image: 2012/08/blood.png
---
<h2>Aufgabenstellung</h2>
Ein Mensch hat ca. 5 Liter Blut. Bei einer Blutspende wird in der Regel etwa ein halber Liter Blut entnommen. Bis zur nächsten Blutspende ist wird dieses Blut wieder neu gebildet.

Wie häufig muss Blut gespendet werden, bis 95% des ursprünglichen Blutes gespendet wurde?

Die natürliche Neubildung von Blut auch ohne Blutspende wird vernachlässigt.

<h2>Berechnung</h2>
<h3>Die ersten Werte</h3>
$f: \mathbb{N}_0 \rightarrow \mathbb{R}_0^+$ sei die Menge des ursprünglichen Blutes in Liter, das nach $x$ Spenden gespendet wurde:

$f(0) = 0$

Beim ersten mal Blutspenden wird ein halber Liter des ursprünglichen Blutes gespendet:

$f(1) = 0{,}5 + f(0)$

Beim zweiten mal Blutspenden werden 0,45 Liter des ursprünglichen Blutes gespendet:

$f(2) = \frac{5-0{,}5}{5} \cdot 0{,}5 \text{ Liter} + f(1) + f(0) = 0{,}95 \text{ Liter}$

Beim dritten mal Blutspenden werden 0,405 Liter des ursprünglichen Blutes gespendet:

$f(3) = \frac{5-0{,}95}{5} \cdot 0{,}5 \text{ Liter} + f(2) + f(1) + f(0) = 1{,}355 \text{ Liter}$

<h3>Eine rekursive Formel</h3>
$$
        \begin{align}
            f(1) &= 0{,}5 \\
            f(x) &= \overbrace{\underbrace{\frac{5-f(x-1)}{5}}_{\text{Anteil}} \cdot 0{,}5}^{\text{neue Blutmenge}} + f(x-1) \\
                 &= 0{,}5 - \frac{1}{10} \cdot f(x-1) + f(x-1) \\
                 &=  0{,}5 + \frac{9}{10} \cdot f(x-1)
        \end{align}
$$

Dabei gilt:
<ul>
  <li>0,5 ist die gespendete Blutmenge in Liter einer Spende</li>
  <li>$\frac{9}{10} = \frac{\text{gespendete Blutmenge}}{\text{gesamte Blutmenge}}$</li>
</ul>

<h3>Auflösen der Rekursion</h3>
$$
        \begin{align}
             f(4) &= 0{,}5 + \frac{9}{10} \cdot (0{,}5 + \frac{9}{10} \cdot (0{,}5 + \frac{9}{10} \cdot 0{,}5))\\
                  &= 0{,}5 + \frac{9}{10} \cdot 0{,}5 + (\frac{9}{10})^2 \cdot (0{,}5 + \frac{9}{10} \cdot 0{,}5)\\
                  &= 0{,}5 + \frac{9}{10} \cdot 0{,}5 + (\frac{9}{10})^2 \cdot 0{,}5 + (\frac{9}{10})^3 \cdot 0{,}5\\
                  &= 0{,}5 \cdot (1 + \frac{9}{10} + (\frac{9}{10})^2 + (\frac{9}{10})^3)\\
              f(x)&= \frac{1}{2} \cdot \sum_{i=0}^{x} (\frac{9}{10})^i
        \end{align}
$$

<h3>Auflösen des Summensymbols</h3>
$$
        \begin{align}
            f(x) &= \frac{1}{2} \cdot \sum_{i=0}^{x} (\frac{9}{10})^i\\
                 &= \frac{1}{2}\cdot (\frac{0{,}9^{x+1} - 1}{0{,}9 - 1})\\
                 &= \frac{1}{2}\cdot (-10 \cdot 0{,}9^{x+1} + 10)\\
                 &= -5 \cdot 0{,}9^{x+1} + 5\\
                 &= 5 \cdot (1 - 0{,}9^{x+1})
        \end{align}
$$

<h2>Lösung</h2>
$$
        \begin{align}
            0{,}95 \cdot 5 &= 5 \cdot (1- 0{,}9^{x+1})\\
                    0{,}95 &= 1 - 0{,}9^{x+1}\\
              0{,}9^{x+1} &= 0{,}05\\
    \ln(0{,}9) \cdot {x+1} &= \ln(0{,}05) \\
                     x  &= \frac{\ln(0,05)}{\ln(0{,}9)} - 1\\
                     x  &= 27{,}43
        \end{align}
$$

<h2>Antwort</h2>
Nach dem 28. mal Blutspenden wurden 95% des ursprünglichen Blutes gespendet.
