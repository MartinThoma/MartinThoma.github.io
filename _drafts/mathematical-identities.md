---
layout: post
title: Mathematical identities
author: Martin Thoma
date: 2012-09-15 12:26:50
categories: 
- My bits and bytes
tags: 
- mathematics
featured_image: 2011/10/eulers-formula.png
---
Some identities are really astonishing:
<h2>Geometry #1</h2>
$\sin^2(\alpha) + \cos^2(\alpha) = 1$

{% caption align="aligncenter" width="500" caption="Triangle with γ = 90°" url="../images/2012/09/right-triangle.png" alt="Rechtwinklinges Dreieck mit γ = 90°" title="" height="289" class="size-full wp-image-44511 " title="Rechtwinklinges Dreieck mit γ = 90°" %}



<strong>Proof</strong>:
(I) $\sin(\alpha) = \frac{a}{c}$
(II) $\cos(\alpha) = \frac{b}{c}$
(III) $a^2 + b^2 = c^2$

$\sin^2(\alpha) + \cos^2(\alpha) \stackrel{(I),(II)}{=} (\frac{a}{c})^2 + (\frac{b}{c})^2 = \frac{a^2 + b^2}{c^2} \stackrel{(III)}{=} \frac{c^2}{c^2} = 1$

<h2>Polynom #1</h2>
$\sum_{k=0}^n k^3 = \frac{1}{4} n^2 (n+1)^2 ~~~ \forall n \in \mathbb{N}_0$

<strong>Proof</strong>: by induction
<u>I.A.</u>: $n=0$:  $\sum_{k=0}^0 k^3 = 0 = \frac{1}{4} 0^2 (0+1)^2$.
<u>I.V.</u>: Let $n \in \mathbb{N}_0$ and for this $n: \sum_{k=0}^n k^3 = \frac{1}{4} n^2 (n+1)^2$
<u>I.S.</u>: 
$\begin{align}
\frac{1}{4}(n+1)^2(n+1+1)^2 &= \frac{1}{4}(n^2 + 2n+1)(n^2+4n+4)\\
&= \frac{1}{4}(n^4+2n^3+n^2+4n^3+8n^2+4n+4n^2+8n+4)\\
&= \frac{1}{4}(n^4+2n^3+n^2+4n^3+12n^2+12n+4)\\
&= \frac{1}{4}n^2(n+1)+n^3+3n^2+3n+1\\
&= \sum_{k=0}^n k^3 + (n+1)^3\\
&= \sum_{k=0}^{n+1} k^3
\end{align}$

<h2>Faculty #1</h2>
$n! + n^2 \cdot (n-1)! = (n+1)!$

<strong>Proof</strong>: $n! + n^2 \cdot (n-1)! = (n-1)! \cdot (n + n^2) = n! \cdot (1 + n) = (n+1)!$
<h2>See also</h2>
<ul>
	<li><a href="http://en.wikipedia.org/wiki/List_of_mathematical_identities">List of mathematical identities</a></li>
</ul>