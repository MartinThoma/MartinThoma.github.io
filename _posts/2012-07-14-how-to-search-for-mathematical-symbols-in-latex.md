---
layout: post
title: How to search for mathematical symbols in LaTeX
author: Martin Thoma
date: 2012-07-14 19:00:44.000000000 +02:00
categories:
- My bits and bytes
tags:
- mathematics
- LaTeX
featured_image: 2012/01/latex-logo.png
---
<h2>Detexify</h2>
The easiest way to search for a math symbol is <a href="http://detexify.kirelabs.org/classify.html">Detexify</a>. This webservices allows you to draw the symbol. It looks like this:

{% caption align="aligncenter" width="512" caption="Detexify - A webservice for finding LaTeX symbols." url="../images/2012/07/detexify.png" alt="Detexify - A webservice for finding LaTeX symbols." title="Detexify - A webservice for finding LaTeX symbols." height="332" class="size-full wp-image-31471" %}

<h2>Symbol tables</h2>
<h3>Arrows</h3>
<table>
<tr>
<td>$\rightarrow$</td><td>\rightarrow</td>
<td>$\leftarrow$</td><td>\leftarrow</td>
<td>$\Rightarrow$</td><td>\Rightarrow</td>
<td>$\Leftarrow$</td><td>\Leftarrow</td>
</tr>
<tr>
<td>$\leftrightarrow$</td><td>\leftrightarrow</td>
<td>$\Leftrightarrow$</td><td>\Leftrightarrow</td>
<td>$\nRightarrow$</td><td>\nRightarrow</td>
<td>$\nrightarrow$</td><td>\nrightarrow</td>
</tr>
<tr>
<td>$\leadsto$</td><td>\leadsto</td>
<td>$\mapsto$</td><td>\mapsto</td>
<td>.</td><td>.</td>
<td>.</td><td>.</td>
</tr>
</table>


<h3>Greek</h3>
<table>
<tr>
<td>$\alpha$</td><td>\alpha</td>
<td>$\beta$</td><td>\beta</td>
<td>$\gamma$</td><td>\gamma</td>
<td>$\delta$</td><td>\delta</td>
</tr>
<tr>
<td>$\zeta$</td><td>\zeta</td>
<td>$\eta$</td><td>\eta</td>
<td>$\theta$</td><td>\theta</td>
<td>$\epsilon, \varepsilon$</td><td>\epsilon, \varepsilon</td>
</tr>
<tr>
<td>$\iota$</td><td>\iota</td>
<td>$\kappa$</td><td>\kappa</td>
<td>$\lambda$</td><td>\lambda</td>
<td>$\mu$</td><td>\mu</td>
</tr>
<tr>
<td>$\nu$</td><td>\nu</td>
<td>$\xi$</td><td>\xi</td>
<td>o</td><td>o</td>
<td>$\pi$</td><td>\pi</td>
</tr>
<tr>
<td>$\rho$</td><td>\rho</td>
<td>$\sigma$</td><td>\sigma</td>
<td>$\tau$</td><td>\tau</td>
<td>$\upsilon$</td><td>\upsilon</td>
</tr>
<tr>
<td>$\phi$</td><td>\phi</td>
<td>$\chi$</td><td>\chi</td>
<td>$\psi$</td><td>\psi</td>
<td>$\omega, \Omega$</td><td>\omega, \Omega</td>
</tr>
<tr>
<td>$\Phi$</td><td>\Phi</td>
<td>$\varphi$</td><td>\varphi</td>
<td>.</td><td>.</td>
<td>.</td><td>.</td>
</tr>
<tr>
<td>$\Lambda$</td><td>\Lambda</td>
<td>$\Delta$</td><td>\Delta</td>
<td>.</td><td>.</td>
<td>.</td><td>.</td>
</tr>
</table>

<h3>Operations</h3>
<table>
<tr>
<td>$\cdot$</td><td>\cdot</td>
<td>$\oplus$</td><td>\oplus</td>
<td>$\times$</td><td>\times</td>
<td>$\nabla$</td><td>\nabla</td>
</tr>
<tr>
<td>$\pm$</td><td>\pm</td>
<td>$\mp$</td><td>\mp</td>
<td>$\cup$</td><td>\cup</td>
<td>$\cap$</td><td>\cap</td>
</tr>
</table>

<h3>Relations</h3>
<table>
<tr>
<td>$\approx$</td><td>\approx</td>
<td>$\sim$</td><td>\sim</td>
<td>$\cong$</td><td>\cong</td>
<td>$\neq$</td><td>\neq</td>
</tr>
</table>

<h3>Calligraphic Letters</h3>
<table>
<tr>
<td>$\cal{O}$</td><td>\cal{O}</td>
<td>$\mathfrak{M}$</td><td>\mathfrak{O}</td>
<td>$\mathfrak{R}$</td><td>\mathfrak{R}</td>
</tr>
</table>

<h3>Sets</h3>
<table>
<tr>
<td>$\mathbb{N}$</td><td>\mathbb{N}</td>
<td>$\mathbb{Z}$</td><td>\mathbb{Z}</td>
<td>$\mathbb{R}$</td><td>\mathbb{R}</td>
<td>$\mathbb{C}$</td><td>\mathbb{C}</td>
</tr>
<tr>
<td>$\mathbb{A}$</td><td>\mathbb{A}</td>
<td>$\cap$</td><td>\cap</td>
<td>$\cup$</td><td>\cup</td>
<td>$\in$</td><td>\in</td>
</tr>
<tr>
<td>$\subseteq$</td><td>\subseteq</td>
<td>$\subsetneq$</td><td>\subsetneq</td>
<td>$\notin$</td><td>\notin</td>
<td>$\bigcup$</td><td>\bigcup</td>
</tr>
</table>

<h3>Other</h3>
You might need \qed, \qedsymbol, \blacksquare for proofs. It is the <a href="http://en.wikipedia.org/wiki/Tombstone_(typography)">Tombstone</a> $\blacksquare$

I've recently needed $\dots, \ddots, \vdots$ (\dots, \ddots, \vdots) for a visualization in a matrix. Note that you can write ... instead of \dots, but you'll lose the semantics.

<h2>See also</h2>
<ul>
  <li><a href="http://www.tex.ac.uk/tex-archive/info/symbols/comprehensive/symbols-a4.pdf">List of symbols</a> - 164 pages of symbols</li>
  <li><a href="http://en.wikipedia.org/wiki/Help:Displaying_a_formula">Displaying a formula</a></li>
</ul>
