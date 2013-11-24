---
layout: post
status: publish
published: true
title: Plotting function graphs with LaTeX
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 12731
wordpress_url: http://martin-thoma.com/?p=12731
date: 2012-01-28 00:17:26.000000000 +01:00
categories:
- My bits and bytes
tags:
- LaTeX
comments: []
---
It's crazy how much time I have wasted today just for searching for a working example how to plot a function within LaTeX. Here are two complete examples which worked for me. 

I have used this command to generate the PDF-file:
[bash]pdflatex latex.tex -output-format=pdf[/bash]

<h2>gnuplot</h2>
[caption id="attachment_12781" align="aligncenter" width="300" caption="gnuplot"]<a href="http://martin-thoma.com/wp-content/uploads/2012/01/gnuplot.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/gnuplot-300x246.png" alt="gnuplot" title="gnuplot" width="300" height="246" class="size-medium wp-image-12781" /></a>[/caption]
[text]\documentclass{article}

\usepackage{tikz}
\usepackage{pgfplots}

\begin{document}
    \begin{tikzpicture}
        \begin{axis}
            \addplot+[id=parable,domain=-5:5]
            gnuplot{4*x**2 - 5}
            node[pin=180:{$4x^2-5$}]{};
        \end{axis}
    \end{tikzpicture}
\end{document}[/text]

<h2>tikzpicture</h2>
[caption id="attachment_12821" align="aligncenter" width="180" caption="tikzpicture"]<a href="http://martin-thoma.com/wp-content/uploads/2012/01/tikzpicture1.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/01/tikzpicture1-180x300.png" alt="tikzpicture" title="tikzpicture" width="180" height="300" class="size-medium wp-image-12821" /></a>[/caption]
[text]\documentclass{article}
 
\usepackage{tikz}
 
\begin{document}
    \begin{tikzpicture}
          \draw[very thin,color=gray] (0.0,0.0) grid (1.8,3.8);

          \draw[->] (-0.5,0) -- (2,0) node[right] {$x$};
          \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

          \draw [domain=0:1/3,red] plot (\x,3*3*\x);
          \draw [domain=1/3:2/3,red] plot (\x,2*3-3*3*\x);
          \draw [domain=2/3:1.5,red] plot (\x,0);
 
          \draw [domain=0:1/4,orange] plot (\x,4*4*\x);
          \draw [domain=1/4:2/4,orange] plot (\x,2*4-4*4*\x);
          \draw [domain=2/4:1.5,orange] plot (\x,0);
    \end{tikzpicture}
\end{document}[/text]

<h2>Floating text</h2>
If you want to wrap the text around the graph, you can use wrapfigure:
[text]\documentclass{article}

\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{wrapfig}

\begin{document}
\begin{wrapfigure}{r}{.2\textwidth}
  \begin{center}
    \begin{tikzpicture}
          \draw[->] (-0.5,0) -- (2,0) node[right] {$x$};
          \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};
          \draw [domain=0:1/3,red] plot (\x,3*3*\x);
          \draw [domain=1/3:2/3,red] plot (\x,2*3-3*3*\x);
          \draw [domain=2/3:1.5,red] plot (\x,0);

          \draw [domain=0:1/4,orange] plot (\x,4*4*\x);
          \draw [domain=1/4:2/4,orange] plot (\x,2*4-4*4*\x);
          \draw [domain=2/4:1.5,orange] plot (\x,0);
    \end{tikzpicture}
  \end{center}
\end{wrapfigure}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis congue dictum elit. Morbi ultricies laoreet massa, sed sagittis lorem laoreet et. Donec at erat non sem tristique rutrum vel vel justo. Vestibulum tincidunt pulvinar mi, a congue purus dignissim vel. Ut porttitor dignissim neque eget rutrum. Nunc gravida varius semper. Quisque et purus quam. Quisque ultricies tristique magna sit amet egestas. Mauris bibendum lacus semper justo consectetur blandit vitae non nisi. Etiam non augue nec est facilisis tempor. Nullam non diam vel erat fermentum gravida. Proin tincidunt turpis lobortis ante elementum suscipit. Curabitur congue, dolor fringilla feugiat blandit, quam libero euismod purus, eget commodo erat nibh a augue. Vestibulum ut tellus ac arcu semper facilisis.
\end{document}[/text]

<h2>PSTricks</h2>
I have found <a href="http://www.tn-home.de/Tobias/Soft/TeX/TUG040611/presentation.pdf">some</a> <a href="http://en.wikipedia.org/wiki/PSTricks">very</a> <a href="http://www.siart.de/typografie/pstricks_20030809.pdf">nice</a> <a href="http://mirror.informatik.uni-mannheim.de/pub/mirrors/tex-archive/graphics/pstricks/contrib/pst-3dplot/pst-3dplot-doc.pdf">example</a> <a href="http://www.ursoswald.ch/LaTeXGraphics/pstricks/pstricks.html">images</a>, but no working LaTeX-Code.

<h2>Read more</h2>
<ul>
  <li>Wikibooks: <a href="http://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions">LaTeX/Floats, Figures and Captions</a></li>
  <li><a href="http://ftp.math.purdue.edu/mirrors/ctan.org/graphics/pgf/contrib/pgfplots/doc/latex/pgfplots/pgfplots.pdf">Manual for pgfplots</a> with lots of examples (as images and LaTeX in over 300 pages!)</li>
  <li>TeXample.net: <a href="http://www.texample.net/tikz/examples/gnuplot-basics/">GNUPLOT basics</a>, <a href="http://www.texample.net/tikz/examples/parameterized-plots/">Parameterized plots</a>, <a href="http://www.texample.net/tikz/examples/pgfplots/">Pgfplots</a></li>
</ul>
