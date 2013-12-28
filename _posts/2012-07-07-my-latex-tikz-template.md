---
layout: post
title: My LaTeX Tikz Template
author: Martin Thoma
date: 2012-07-07 17:38:13.000000000 +02:00
categories:
- Code
tags:
- LaTeX
- Tikz
featured_image: 2012/01/latex-logo.png
---
Sometimes I would like to create a single picture with Tikz for later usage on Wikipedia or my Blog. This is my LaTeX Tikz template I use in such a situation:

<h2>The templates</h2>
<h3>latex-document.tex</h3>
{% highlight text %}\documentclass[varwidth=true, border=2pt]{standalone}

\usepackage{tikz}
\usetikzlibrary{arrows,positioning} 

\begin{document}
\begin{tikzpicture}
    % Your Codes should be here
\end{tikzpicture}
\end{document}{% endhighlight %}

<h4>Standalone</h4>
<h4>Preview-Environment</h4>
{% highlight text %}\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\setlength\PreviewBorder{2mm}

\usepackage{tikz}
\usetikzlibrary{arrows,positioning} 

\begin{document}
\begin{preview}
\begin{tikzpicture}
    % Your Codes should be here
\end{tikzpicture}
\end{preview}
\end{document}{% endhighlight %}

<h3>Makefile</h3>
{% highlight text %}SOURCE = latex-document.tex

DELAY = 80
DENSITY = 300

make:
	pdflatex $(SOURCE).tex -output-format=pdf
	make clean

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux

animatedGif:
	pdfcrop $(SOURCE).pdf
	convert -verbose -delay $(DELAY) -loop 0 -density $(DENSITY) $(SOURCE)-crop.pdf $(SOURCE).gif
	make clean

transparentGif:
	convert $(SOURCE).pdf -transparent white result.gif
	make clean

svg:
	pdf2svg $(SOURCE).pdf $(SOURCE).svg
	# Necessary, as pdf2svg does not always create valid svgs:
	inkscape $(SOURCE).svg --export-plain-svg=$(SOURCE).svg
	# Alternatively, only this one (produces worse results):
	#inkscape $(SOURCE).pdf --export-plain-svg=$(SOURCE).svg{% endhighlight %}

<h2>Requirements</h2>
<ul>
    <li>LaTeX (<a href="http://martin-thoma.com/how-to-install-the-latest-latex-version/" title="How to install the latest LaTeX Version">How to install the latest LaTeX Version</a>)</li>
    <li>make</li>
    <li>Inkscape</li>
    <li>pdf2svg</li>
</ul>

<h2>Test if you meet these requirements</h2>
Make sure that you have a valid LaTeX installation. <code>pdflatex --version</code> should output something like:
{% highlight bash %}pdfTeX 3.1415926-2.3-1.40.12 (TeX Live 2011)
kpathsea version 6.0.1
Copyright 2011 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
There is NO warranty.  Redistribution of this software is
covered by the terms of both the pdfTeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the pdfTeX source.
Primary author of pdfTeX: Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
Compiled with libpng 1.5.2; using libpng 1.5.2
Compiled with zlib 1.2.5; using zlib 1.2.5
Compiled with xpdf version 3.02pl5
{% endhighlight %}

Make sure you can execute Makefiles. <code>make --version</code> should output something like this:
{% highlight bash %}GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i486-pc-linux-gnu{% endhighlight %}

The command <code>inkscape --version</code> should return:
{% highlight bash %}Inkscape 0.47 r22583 (Apr  4 2010){% endhighlight %}

And <code>pdf2svg --version</code> should return:
{% highlight bash %}Usage: pdf2svg <in file.pdf> <out file.svg> [<page no>]{% endhighlight %}

<h2>How to use it</h2>
You have to place the Makefile in the same folder as latex-document.tex. If you have done this and if you meet the requirements, you can execute:
<ul>
  <li><code>make</code>: Generates a PDF file from latex-document.tex</li>
  <li><code>make svg</code>: Generates a SVG file from the generated PDF file</li>
  <li><code>make transparentGif</code>: Generates a transparent Gif from the PDF file</li>
  <li><code>make animatedGif</code>: If you have used multiple slides, this will create an animated Gif file. See <a href="http://martin-thoma.com/how-to-visualize-graph-algorithms-with-latex/" title="How to visualize Graph algorithms with LaTeX">How to visualize Graph algorithms with LaTeX</a> for an example.</li>
</ul>

<h2>See also</h2>
<ul>
  <li><a href="http://martin-thoma.com/how-to-print-source-code-with-latex/" title="How to print Source Code with LaTeX">How to print Source Code with LaTeX</a></li>
  <li><a href="http://martin-thoma.com/briefe-mit-latex-schreiben/" title="Briefe mit LaTeX schreiben">Briefe mit LaTeX schreiben</a> (A template for letters)</li>
  <li><a href="http://martin-thoma.com/plotting-function-graphs-with-latex/" title="Plotting function graphs with LaTeX">Plotting function graphs with LaTeX</a></li>
</ul>
