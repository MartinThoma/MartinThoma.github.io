---
layout: post
title: Sizes in LaTeX
author: Martin Thoma
date: 2012-09-29 18:23:38.000000000 +02:00
categories:
- Code
tags:
- LaTeX
- Tikz
featured_image: 2012/09/tikz-sizes-thumb.png
---
Here is an overview of sizes in LaTeX:

<h2>TikZ</h2>
{% caption align="aligncenter" width="500" caption="TikZ thicknes" url="../images/2012/09/tikz-sizes.png" alt="TikZ thicknes" title="TikZ thicknes" height="503" class="size-full" %}
Usage example:
<code>\draw[ultra thick, blue,dashed](a -| current plot begin) -- (a);</code>
<ul>
	<li><code>ultra thin</code></li>
	<li><code>very thin</code></li>
	<li><code>thin</code></li>
	<li><code>semithick</code></li>
	<li><code>thick</code></li>
	<li><code>very thick</code></li>
	<li><code>ultra thick</code></li>
</ul>
<h2>Text</h2>
<p style="text-align: center;"><a href="../images/2012/09/text-sizes-latex.png"><img class="size-full wp-image-45921 aligncenter" title="Text sizes in LaTeX" src="../images/2012/09/text-sizes-latex.png" alt="" width="512" height="110" /></a></p>
Usage example:
<code>\Huge $\varepsilon$</code>
<ul>
	<li><code>\tiny</code></li>
	<li><code>\scriptsize</code></li>
	<li><code>\footnotesize</code></li>
	<li><code>\small</code></li>
	<li><code>\normalsize</code></li>
	<li><code>\large</code></li>
	<li><code>\Large</code></li>
	<li><code>\LARGE</code></li>
	<li><code>\huge</code></li>
	<li><code>\Huge</code></li>
</ul>

<h2>Math</h2>
{% caption align="aligncenter" width="309" caption="Sizes of different math modes" url="../images/2012/09/latex-math-sizes.png" alt="Sizes of different math modes" title="" height="145" class="size-full wp-image-45931 " title="Sizes of different math modes" %}
Usage example:
<code>$\scriptstyle \lim_{n \rightarrow \infty} (1 + \frac{1}{n})^n$</code>
<ul>
	<li><code>\scriptscriptstyle</code></li>
	<li><code>\scriptstyle</code></li>
	<li><code>\textstyle</code></li>
	<li><code>\displaystyle</code></li>
</ul>
