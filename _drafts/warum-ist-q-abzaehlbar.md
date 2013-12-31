---
layout: post
title: Warum ist Q abzählbar?
author: Martin Thoma
date: 2012-03-28 03:07:02
categories: 
- German posts
tags: 
- analysis
- mathematics
featured_image: 
---
<div class="definition">Eine Menge B heißt <strong>abzählbar</strong> [latex]: \Leftrightarrow \exists (a_n) \in B: B = \{a_1, a_2, a_3, ...\}[/latex]
[latex]\Leftrightarrow \exists f : \mathbb{N} \rightarrow B [/latex] mit [latex]f[/latex] surjektiv.</div>

Die natürlichen Zahlen sind abzählbar.
<strong>Beh.:</strong> [latex]\mathbb{N}[/latex] ist abzählbar.
<strong>Bew.</strong>: direkt
Sei [latex]f: \mathbb{N} \rightarrow \mathbb{N}[/latex] definiert durch [latex]f(n) := n[/latex]. [latex]f[/latex] ist also die identität und damit bijektiv und insbesondere surjektiv [latex]\blacksquare[/latex]

Die ganzen Zahlen sind abzählbar.
<strong>Beh.:</strong> [latex]\mathbb{Z}[/latex] ist abzählbar.
<strong>Bew.</strong>: direkt
Sei [latex]f: \mathbb{N} \rightarrow \mathbb{Z}[/latex] definiert durch [latex]f(n) := 
\begin{cases}
\frac{n-1}{2}   & \text{, falls n ungerade} \\
- \frac{n}{2} & \text{, falls n gerade}
\end{cases}[/latex].
Also:
[latex]\forall z \in \mathbb{Z}: \exists x \in \mathbb{N} : f(x) = z[/latex]
da:
[latex]\forall x \in \mathbb{Z}: n = 
\begin{cases}
- 2 \cdot x   & \text{, falls x negativ} \\
2 \cdot x + 1 & \text{, falls x positiv}
\end{cases}[/latex]

Es gibt also für jede ganze Zahl z eine natürliche Zahl n, die ich in [latex]f[/latex] stecken kann um z zu erhalten [latex]\blacksquare[/latex]

<strong>Beh.:</strong> [latex]\mathbb{N} \times \mathbb{N}[/latex] ist abzählbar.
<strong>Bew.</strong>: direkt
Sei [latex]f: \mathbb{N} \times \mathbb{N} \rightarrow \mathbb{N}[/latex] rekursiv definiert durch [latex]f(1,1) := 1[/latex] und 
[latex]f (m, n) := \begin{cases}
f(m + 1, n - 1) + 1 & \text{, falls } n \neq 1 \\
f(1, m - 1)         & \text{sonst}
\end{cases}[/latex]
Diese Abbildung sieht wie folgt aus:
[caption id="attachment_20501" align="aligncenter" width="322" caption="Abbildung, die N x N auf N abbildet"]<a href="http://martin-thoma.com/wp-content/uploads/2012/03/countable-set-n-times-n.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/03/countable-set-n-times-n.png" alt="Function that transforms N times N to N" title="Function that transforms N times N to N" width="322" height="288" class="size-full wp-image-20501" /></a>[/caption]

Ich finde es ist intuitiv klar, dass diese Funktion bijektiv ist. Hat jemand dafür einen sauberen Beweis?

Also gibt es eine Umkehrfunktion (die auch bijektiv ist). Also ist [latex]\mathbb{N} \times \mathbb{N}[/latex] abzählbar [latex]\blacksquare[/latex]

<strong>Beh.:</strong> [latex]\mathbb{Q}^+[/latex] ist abzählbar.
<strong>Bew.</strong>: über [latex]N \times N[/latex]
Jede Zahl [latex]x \in \mathbb{Q}^+[/latex] kann  mit zwei natürlichen Zahlen dargestellt werden: [latex]x = \frac{p}{q}[/latex]. Also gibt es eine Funktion [latex]f: \mathbb{N} \times \mathbb{N} \rightarrow \mathbb{Q}[/latex] mit 
[latex]f(m, n) := \frac{m}{n}[/latex]. Diese Abbildung ist offensichtlich surjektiv. [latex]\blacksquare[/latex]

<h2>Material</h2>
Die LaTeX-Dateien für die Bilder sind in diesem <a href='http://martin-thoma.com/wp-content/uploads/2012/03/countable-sets.zip'>Archiv</a> zu finden.