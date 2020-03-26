---
layout: post
title: How do I calculate a Histogram equalization?
slug: calculate-histogram-equalization
author: Martin Thoma
date: 2013-09-11 13:17:39.000000000 +02:00
category: My bits and bytes
tags: KogSys
featured_image: 2013/09/lena-testbild.png
---
Let's say you have the following greyscale image:

$A = \begin{pmatrix}
255 & 50 & 255\\
0   & 50 & 50
\end{pmatrix}$

<h2>Histogram</h2>
Now the histogram is a function $H: [0,255] \rightarrow \mathbb{N}_0$.

The histogram of $A$ is

$H(x) := \begin{cases}
1 &\text{, if } x = 0\\
3 &\text{, if } x = 50\\
2 &\text{, if } x = 255
\end{cases}$

<h2>Accumulated histogram</h2>
The accumulated histogram $H_\alpha: [0,255] \rightarrow \mathbb{N}_0$ is defined as

$H_\alpha(x) := \sum_{i=0}^x H(i)$

This means, in the given example you get

$H_\alpha(x) := \begin{cases}
1 &\text{, if } x < 50\\
4 &\text{, if } 50 \leq x < 255\\
6 &\text{, if } x = 255
\end{cases}$

<h2>Normalized histogram</h2>
The normalized histogram is defined as $H_n(x) := \mathrm{round}(\frac{255}{w \cdot h} \cdot H_\alpha(x))$ where $w$ is the width of the image and $h$ is the height of the image.

In our example it's:

$H_n(x) := \begin{cases}
43 &\text{, if } x < 50\\
170 &\text{, if } 50 \leq x < 255\\
255 &\text{, if } x = 255
\end{cases}$

So the resulting image is

$A = \begin{pmatrix}
255 & 170 & 255\\
43  & 170 & 170
\end{pmatrix}$

<h2>See also</h2>
<ul>
  <li><a href="http://www.songho.ca/dsp/histogram/histogram.html">Some code</a></li>
  <li><a href="http://www.csce.uark.edu/~jgauch/5683/notes/ch03b.pdf">Code and examples</a></li>
</ul>
