---
layout: post
title: "Mathematik: Wo ist der Unterschied?"
author: Martin Thoma
date: 2012-08-15 04:12:08
categories: 
- German posts
tags: 
- Linear algebra
- mathematics
featured_image: 2012/01/vector-space.png
---
Ich habe ein paar kurze Beispiele von sehr ähnlichen formalen Schreibweisen gesammelt, die gut klar machen, wo der Unterschied zwischen zwei Schreibweisen ist.

<h2>Beispiel 1</h2>
<table class="wikitable">
<tr>
  <th>$\text{Kern } \phi = \left \{
  \begin{pmatrix}
    -2 \lambda\\
    0\\
    4 \lambda
  \end{pmatrix}
\right \}, \lambda \in \mathbb{R}$</th>
  <th>$\text{Kern } \phi = \left \{
  \begin{pmatrix}
    -2 \lambda\\
    0\\
    4 \lambda
  \end{pmatrix}
| \lambda \in \mathbb{R} \right \}$</th>
</tr>
<tr>
  <td>$\lambda$ ist beliebig, aber fest. Nur ein Element ist in der Menge.</td>
  <td>$\lambda$ ist beliebig. Ein ganzer Vektorraum ist in der Menge.</td>
</tr>
</table>

<h2>Beispiel 2</h2>
<table class="wikitable">
<tr>
  <th>$\exists_{c > 0} \forall_{n \in \mathbb{N}}: f(n) < c \cdot g(n)$</th>
  <th>$\forall_{n \in \mathbb{N}} \exists_{c > 0}: f(n) < c \cdot g(n)$</th>
</tr>
<tr>
  <td>Es gibt ein c, für dass die Bedingung $f(n) < c \cdot g(n)$ für jedes $n \in \mathbb{N}$ erfüllt ist.</td>
  <td>Für jedes $n \in \mathbb{N}$ gibt es ein c, sodass die Bedingung $f(n) < c \cdot g(n)$ erfüllt ist. Die <code>c</code> müssen für unterschiedliche n nicht notwendigerweise gleich sein.</td>
</tr>
</table>

<h2>Beispiel 3</h2>
<table class="wikitable">
<tr>
  <th>$f:\mathbb{N} \rightarrow \mathbb{R}$</th>
  <th>$x \mapsto \sqrt{x}$</th>
</tr>
<tr>
  <td>Der Pfeil $\rightarrow$ wird für die Deklaration der Funktion benutzt.</td>
  <td>Der Pfeil $\mapsto$ wird für die Definition der Funktion benutzt</td>
</tr>
</table>
