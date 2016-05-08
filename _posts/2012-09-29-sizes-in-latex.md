---
layout: post
title: Sizes in LaTeX
author: Martin Thoma
date: 2012-09-29 18:23:38.000000000 +02:00
category: Code
tags: LaTeX, Tikz
featured_image: 2012/09/tikz-sizes-thumb.png
---
Here is an overview of sizes in LaTeX:

<h2>TikZ</h2>
<figure class="aligncenter">
            <a href="../images/2012/09/tikz-sizes.png"><img src="../images/2012/09/tikz-sizes.png" alt="TikZ thicknes" style="max-width:500px;max-height:503px" class="size-full"/></a>
            <figcaption class="text-center">TikZ thicknes</figcaption>
        </figure>
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
<p style="text-align: center;"><a href="../images/2012/09/text-sizes-latex.png"><img class="size-full wp-image-45921 aligncenter" title="Text sizes in LaTeX" src="../images/2012/09/text-sizes-latex.png" alt="Text sizes in LaTeX" width="512" height="110" /></a></p>
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

## Math
### Formulas
<figure class="aligncenter">
            <a href="../images/2012/09/latex-math-sizes.png"><img src="../images/2012/09/latex-math-sizes.png" alt="Sizes of different math modes" style="max-width:309px;max-height:145px;" class="size-full wp-image-45931"/></a>
            <figcaption class="text-center">Sizes of different math modes</figcaption>
        </figure>
Usage example:
<code>$\scriptstyle \lim_{n \rightarrow \infty} (1 + \frac{1}{n})^n$</code>
<ul>
	<li><code>\scriptscriptstyle</code></li>
	<li><code>\scriptstyle</code></li>
	<li><code>\textstyle</code></li>
	<li><code>\displaystyle</code></li>
</ul>

### Parentheses
The size of brackets `[ ]`, (curly) braces `{ }` and parentheses `( )` can be 
adjusted with these commands:

```latex
$$-1+x ( x \big( 1+ x\Big(2 + x \bigg(3+ x\Bigg(4+x \Bigg) \bigg) \Big) \big) )$$
```

The result will look like this

<figure class="aligncenter">
            <a href="../images/2012/09/latex-parentheses-sizes.png"><img src="../images/2012/09/latex-parentheses-sizes.png" alt="Sizes of parentheses" style="max-width:500px;" class="size-full"/></a>
            <figcaption class="text-center">Sizes of parentheses</figcaption>
        </figure>