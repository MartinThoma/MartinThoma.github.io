---
layout: post
status: publish
published: true
title: Wie wendet man den Transformationssatz an?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 51491
wordpress_url: http://martin-thoma.com/?p=51491
date: 2012-12-22 22:43:11.000000000 +01:00
categories:
- Cyberculture
tags:
- mathematics
- analysis
comments: []
featured_image: 2012/12/transformationssatz-thumb.png
---
<div class="info">Folgender Artikel basiert auf meinem Mitschrieb der Analysis III &Uuml;bung bei Herrn Bolleyer.</div>

Sei $A \in \mathfrak{B}_d$ mit $A^0 \neq \emptyset$ und $\lambda_d (A \setminus A^0) = 0$ sowie $\phi \in C^1(U, \mathbb{R}^d)$ mit $U \subseteq \mathbb{R}^d$ offen und $A \subseteq U$. Weiter sei $\phi$ auf $A^0$ injektiv und $\det(\phi'(x)) \neq 0$ f&uuml;r $x \in A^0$. Sei $f \in \mathfrak{L}^1(\phi(A))$ oder $f \geq 0$ auf $A$ so gilt $\int_{\phi(A)} f(x) dy = \int_A f(\phi(x)) | \det(\phi'(x)) | dx$

In Anwendungen: $Y \in \mathfrak{B}_d$ und $f: Y \rightarrow \overline{\mathbb{R}}$ messbar.

<strong>Aufgabe</strong>: Berechne $\int_Y f(x) dy$ falls es existiert.
<strong>Vorgehensweise:</strong>
<ol type="i" style="list-style-type:lower-roman;">
   <li>Zeige $f$ integrierbar oder $f \geq 0$ auf $Y$</li>
   <li>Finde $A \in \mathfrak{B}_d$ und $\phi: A \rightarrow \mathbb{R}^d$ mit $\phi(A) = Y$ und den obigen Eigenschaften<br/>
$\phi$ sollte so gew&auml;hlt sein, dass die sp&auml;teren Rechenwege relativ einfach werden.</li>
    <li>Berechne $\int_{Y} f(y) dy = \int_{\phi(A)} f(y) dy = \int_{A} f(\phi(x)) |\det (\phi'(x)) | dx$</li>
</ol>

<h2>Beispiele</h2>
Sei $Y := \{(x,y) \in \mathbb{R}^2 | 1 \leq \| (2,2) - (x,y)\| \leq 2\}$.
Setze $\phi : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ mit $\phi(r, \varphi) := \begin{pmatrix}2\\2\end{pmatrix} + r \cdot \begin{pmatrix}\cos(\varphi)\\ \sin(\varphi) \end{pmatrix}$

$\phi \in C^1(\mathbb{R}^2, \mathbb{R}^2)$ und f&uuml;r $r \in \mathbb{R}$ gilt $\det \phi'(r, \varphi) = \det \left ( \begin{array}{cc}
\cos(\varphi) & - r \sin(\varphi)\\
\sin(\varphi) & r \cos (\varphi)
\end{array} \right ) = r$

F&uuml;r $r \neq 0$ gilt also $\det \phi'(r, \varphi) \neq 0$ f&uuml;r jedes $\varphi \in \mathbb{R}$. $\phi$ ist nicht injektiv auf $\mathbb{R}^2$. Setze $A := [1,2] \times [0, 2\pi]$.

Dann ist $A^0 = (1,2) \times (0,2 \pi)$ und$ \phi$ auf $A^0$ injektiv. Au&szlig;erdem ist $\det \phi'(x) \neq 0$ f&uuml;r $x \in A^0$. 

F&uuml;r $f:Y \rightarrow \mathbb{R}$ mit $f(Y_1, Y_2) := Y_1 - Y_2$ gilt $f \in \mathfrak{L}^1(Y)$ ($Y$ kompakt, $f$ stetig)

Au&szlig;erdem: 
$\begin{align}
\int_Y f(y) dy &= \int_\phi(A) f(y) dy \\
&\stackrel{Tr}{=} \int_A f(\phi(r, \varphi)) |\det \phi'(r, \varphi)| d(r, \varphi) \\
&= \int_A r(2 + r \cos(y) - 2 - r \sin(\varphi)) d(r, \varphi) \\
&= \int_1^2 (\int_0^{2\pi} r^2 (\cos \varphi - \sin \varphi d \varphi) dr \\
&= \underbrace{(\int_1^2 r^2 dr)}_{< \infty} \underbrace{(\int_0^{2\pi} \cos \varphi - \sin \varphi d \varphi)}_{= 0}\\
&= 0
\end{align}$
