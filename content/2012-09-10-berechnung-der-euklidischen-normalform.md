---
layout: post
lang: de
title: Berechnung der euklidischen Normalform
slug: berechnung-der-euklidischen-normalform
author: Martin Thoma
date: 2012-09-10 07:57:50.000000000 +02:00
category: German posts
tags: Linear algebra, Matrix, normal form
featured_image: 2012/09/math-euklidische-normalform1.png
---
Die euklidische Normalform einer linearen Isometrie, manchmal auch lineare Normalform gennant, hat folgende Gestalt:

<figure class="aligncenter">
            <a href="../images/2012/09/math-euklidische-normalform.png"><img src="../images/2012/09/math-euklidische-normalform.png" alt="Euklidische Normalform" style="max-width:512px;max-height:291px;" class="size-full wp-image-43911 "/></a>
            <figcaption class="text-center">Euklidische Normalform</figcaption>
        </figure>

Bei einer <span>$n \times n$</span>-Matrix gilt also folgende Gleichung:
<span>$n = p + q + 2r$</span>

<h2>Bestimmung der Normalform</h2>
Sei <span>$\Phi$</span> eine lineare Isometrie eines euklidischen Vektorraumes. Dann habe <span>$\Phi$</span> die Abbildungsmatrix <span>$A$</span>.
Sei <span>$B := A + A^T$</span>.
Wenn man die euklidische Normalform bilden will, bestimmt man zuerst das charakteristische Polynom von <span>$B$</span>. Die Nullstellen davon sind die Eigenwerte. Die algebraische Vielfachheit des Eigenwertes 2 von <span>$B$</span> (die Potenz im charakteristischen Polynom) gibt die Anzahl der 1er an, genauso gibt die Vielfachheit des Eigenwertes -2 die Anzahl der -1er an.

Die restlichen Eigenwerte <span>$\lambda_1, \dots, \lambda_r$</span> geben die Drehkästchen an.

Es gilt:
<span>$\cos \omega = \frac{\lambda}{2}$</span>
<span>$\sin \omega = \sqrt{1 - \frac{\lambda^2}{4}}$</span>

Mit diesen Angaben kann man direkt die euklidische Normalform angeben.


## Bestimmung der Transformationsmatrix
<h3>Eigenräume bestimmen</h3>
Die Eigenräume berechnet man wie gewohnt:

<span>$\text{Eig}(\lambda_i) = \text{Kern}(B- \lambda_i \cdot E)$</span>

<h3>ONB bestimmen</h3>
Nun wählt man für jeden Eigenraum eine Basis Orthonormalbasis aus Eigenvektoren. Das kann man mit dem Gram-Schmidtsches Orthogonalisierungsverfahren machen, also:
Wähle ein beliebiges <span>$w_1 \in \text{Eig}(\lambda_i)$</span>.

<div>$$w_j = v_j - \sum_{i=1}^{j-1} \frac{\langle v_j, w_i \rangle}{\langle w_i, w_i \rangle} \cdot w_i$$</div>


## Quellen
<ul>
	<li>Skript von Prof. Dr. Leuzinger, S. 228 ff.</li>
	<li>Klausur &bdquo;Lineare Algebra und analytische Geometrie&ldquo; vom Frühjahr 2007, Aufgabe II.4</li>
</ul>
