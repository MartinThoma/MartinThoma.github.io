---
layout: post
title: Integration durch Substitution
author: Martin Thoma
date: 2012-09-16 11:32:43.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- analysis
- Integral calculus
---
Integration durch Substitution ist eine elementare Methode zum finden von Stammfunktionen von Integralen bzw. zum berechnen von Integralen.

<h2>Unbestimmte Integrale</h2>
<h3>Beispiel 1</h3>
$\int e^{2x} dx = ?$

Substituiere $u = 2x$ und $u'(x) = \frac{du}{dx} = 2 \Rightarrow dx = \frac{du}{2}$
Also:
$\begin{align}
\int e^{2x} dx &\stackrel{sub}{=}\\
&= \int e^u \frac{du}{2}\\
&= \int \frac{1}{2} e^u du\\
&= \frac{1}{2} \int e^u du\\
&= \frac{1}{2} \int e^u du\\
&= \frac{1}{2} e^u + C \\
&\stackrel{resub}{=} \frac{1}{2} e^{2x} + C 
\end{align}$

<h3>Beispiel 2</h3>
$\int (x-1)^2 dx = ?$

Substituiere $u = x-1$ und $u'(x) = \frac{ \;\mathrm{d}u}{dx} 1 \Rightarrow dx =  \;\mathrm{d}u$
Also:
$\begin{align}
\int (x-1)^2 dx &\stackrel{sub}{=}\\
&= \int u^2 \;\mathrm{d}u\\
&= \frac{1}{3} u^3 + C
&\stackrel{resub}{=} \frac{1}{3} (x-1)^3 + C
\end{align}$

<h2>Bestimmte Integrale</h2>
Bei bestimmten Integralen muss man die Grenzen auch ersetzen.

<h3>Beispiel 1</h3>
Dieses Beispiel stammt aus der Klausur &bdquo;Analysis I&ldquo; vom Herbst 2010.

Berechne $\int_1^4 e^{\sqrt{x}} dx$.

Substituiere:
$\begin{align}
u  &= \sqrt x\\
\frac{\;\mathrm{d}u}{dx} &= u' = \frac{1}{2\sqrt{x}}\\
\Leftrightarrow dx &= 2 \sqrt{x} \;\mathrm{d}u = 2 u \;\mathrm{d}u
\end{align}$.

Es gilt:
$\int_1^4 e^{\sqrt{x}} dx = \int_1^2 e^u 2 u \;\mathrm{d}u = 2 \int_1^2 u \cdot e^u \;\mathrm{d}u$.

Nun wird eine <a href="http://martin-thoma.com/partielle-integration/" title="Partielle Integration">partielle Integration</a> durchgef&uuml;hrt mit $f'(u)=e^u$ und $g(u)=u$:

$\begin{align}
2 \int_1^2 u \cdot e^u \;\mathrm{d}u &= 2 ([e^u \cdot u]_1^2 - \int_1^2 e^u du) \\
&= 2((e^2 \cdot 2 - e) - [e^u]_1^2)\\ 
&= 2 \cdot (2e^2 -e - (e^2 - e)) \\
&= 2 \cdot e^2
\end{align}$
