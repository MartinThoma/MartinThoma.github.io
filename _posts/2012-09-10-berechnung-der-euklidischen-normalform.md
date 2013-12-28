---
layout: post
title: Berechnung der euklidischen Normalform
author: Martin Thoma
date: 2012-09-10 07:57:50.000000000 +02:00
categories:
- German posts
tags:
- Linear algebra
- Matrix
- normal form
featured_image: 2012/09/math-euklidische-normalform1.png
---
Die euklidische Normalform einer linearen Isometrie, manchmal auch lineare Normalform gennant, hat folgende Gestalt:

[caption id="attachment_43911" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/09/math-euklidische-normalform.png"><img class="size-full wp-image-43911 " title="Euklidische Normalform" src="http://martin-thoma.com/wp-content/uploads/2012/09/math-euklidische-normalform.png" alt="Euklidische Normalform" width="512" height="291" /></a> Euklidische Normalform[/caption]

Bei einer $n \times n$-Matrix gilt also folgende Gleichung:
$n = p + q + 2r$

<h2>Bestimmung der Normalform</h2>
Sei $\Phi$ eine lineare Isometrie eines euklidischen Vektorraumes. Dann habe $\Phi$ die Abbildungsmatrix $A$.
Sei $B := A + A^T$.
Wenn man die euklidische Normalform bilden will, bestimmt man zuerst das charakteristische Polynom von $B$. Die Nullstellen davon sind die Eigenwerte. Die algebraische Vielfachheit des Eigenwertes 2 von $B$ (die Potenz im charakteristischen Polynom) gibt die Anzahl der 1er an, genauso gibt die Vielfachheit des Eigenwertes -2 die Anzahl der -1er an.

Die restlichen Eigenwerte $\lambda_1, \dots, \lambda_r$ geben die Drehk&auml;stchen an.

Es gilt:
$\cos \omega = \frac{\lambda}{2}$
$\sin \omega = \sqrt{1 - \frac{\lambda^2}{4}}$

Mit diesen Angaben kann man direkt die euklidische Normalform angeben.

<h2>Bestimmung der Transformationsmatrix</h2>
<h3>Eigenr&auml;ume bestimmen</h3>
Die Eigenr&auml;ume berechnet man wie gewohnt:

$\text{Eig}(\lambda_i) = \text{Kern}(B- \lambda_i \cdot E)$

<h3>ONB bestimmen</h3>
Nun w&auml;hlt man f&uuml;r jeden Eigenraum eine Basis Orthonormalbasis aus Eigenvektoren. Das kann man mit dem Gram-Schmidtsches Orthogonalisierungsverfahren machen, also: 
W&auml;hle ein beliebiges $w_1 \in \text{Eig}(\lambda_i)$.
$w_j = v_j &ndash; \sum_{i=1}^{j-1} \frac{\langle v_j, w_i \rangle}{\langle w_i, w_i \rangle} \cdot w_i$

<h2>Quellen</h2>
<ul>
	<li>Skript von Prof. Dr. Leuzinger, S. 228 ff.</li>
	<li>Klausur &bdquo;Lineare Algebra und analytische Geometrie&ldquo; vom Fr&uuml;hjahr 2007, Aufgabe II.4</li>
</ul>
