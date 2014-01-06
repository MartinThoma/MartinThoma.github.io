---
layout: post
title: How to visualize Graph algorithms with LaTeX
author: Martin Thoma
date: 2012-05-16 13:16:29.000000000 +02:00
categories:
- Code
tags:
- LaTeX
- Tikz
featured_image: 2012/01/latex-logo.png
---
Tkiz is a very powerful TeX package. You can easily create visualizations of graphs and graph algorithms (if you have a template ;-) ). This post should give you a template to visualize graph algorithms with LaTeX.
I recently found a great animation of Prim's algorithm done by <a href="http://www.texample.net/tikz/examples/prims-algorithm/">Kjell Magne Fauske</a>. I've edited his source files to show an eulerian path. This is how it looks like:
{% caption align="aligncenter" width="512" caption="LaTeX (Tikz) animation of an eulerian path" url="../images/2012/05/tikz-animation.gif" alt="LaTeX (Tikz) animation of an eulerian path"  height="228" class="size-full wp-image-24611" %}
This animation was automatically created. See <a href='../images/2012/05/LaTeX-example.zip'>Archive</a> and the intermediate <a href='../images/2012/05/tikz-animation.pdf'>PDF</a>.

<h2>The ideas</h2>
<h3>Draw the Graph</h3>
If you want to visualize a graph algorithm, you should first try to get the image of the graph with Tikz. 
First include all packages / create the general structure of the document:

```latex
\documentclass[hyperref={pdfpagelabels=false}]{beamer}
\usepackage{lmodern}

\usepackage[utf8]{inputenc} % this is needed for german umlauts
\usepackage[ngerman]{babel} % this is needed for german umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf

\usepackage{verbatim}
\usepackage{tikz}
\usetikzlibrary{arrows,shapes}

% see http://deic.uab.es/~iblanes/beamer_gallery/index_by_theme.html
\usetheme{Frankfurt}
\usefonttheme{professionalfonts}

\begin{document}
\begin{frame}
	Your content will be here.
\end{frame}
\end{document}
```

Simple graphs could look like this:

```latex
\begin{figure}
	\begin{tikzpicture}[->,scale=1.8, auto,swap]
		% Draw the vertices.
		\node (a) at (0,0) {$a (this is text)$};
		\node (b) at (0,1) {$b$};
		\node (c) at (1,1) {$c$};
		\node (d) at (1,0) {$d$};
		\node (e) at (3,1) {$d$};

		% Connect vertices with edges and draw weights
		\path (a) edge node {} (b);
		\path (b) edge node {} (c);
		\path (c) edge node {} (d);
		\path (d) edge node {} (a);
	\end{tikzpicture}
\end{figure}
```

You should get something similar to this:
{% caption align="aligncenter" width="300" caption="Simple example graph created with LaTeX and Tikz" url="../images/2012/05/simple-example-graph-300x105.png" alt="Simple example graph created with LaTeX and Tikz"  height="105" class="size-medium wp-image-24691" %}

<h3>Animate</h3>
Animations can be created with Tikz by working with layers. You don't want to redraw the whole graph every time. Most of the time you want to overlay/underlay some parts of the graph. This can be achieved by declaring a new layer:
{% highlight latex %}\pgfdeclarelayer{NAME}{% endhighlight %}
Then you need to tell PGF which layers are to use in the next figure:
{% highlight latex %}\pgfsetlayers{LAYER LIST}{% endhighlight %}
The layer main should always be part of the list. Here is an example:
{% highlight latex %}\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}{% endhighlight %}

Now the magic begins. You consecutively add frames to the layer:

```latex
	\begin{pgfonlayer}{background}
		\path<2->[draw,line width=5pt,-,red!50] (a.center) edge node {} (b.center);
		\path<10->[draw,line width=5pt,-,red!50] (b.center) edge node {} (d.center);
		\path<12->[draw,line width=5pt,-,red!50] (d.center) edge node {} (e.center);
	\end{pgfonlayer}
```

The number (2, 10 and 12 in this example) indicate the frame in which it should be added. This is the absolute frame, but 1 is the first frame of the figure environment!

<h3>Status quo</h3>
```latex
\documentclass[hyperref={pdfpagelabels=false}]{beamer}
\usepackage{lmodern}
 
\usepackage[utf8]{inputenc} % this is needed for german umlauts
\usepackage[ngerman]{babel} % this is needed for german umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf
 
\usepackage{verbatim}
\usepackage{tikz}
\usetikzlibrary{arrows,shapes}
 
% see http://deic.uab.es/~iblanes/beamer_gallery/index_by_theme.html
\usetheme{Frankfurt}
\usefonttheme{professionalfonts}
 
\begin{document}

\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}

\begin{frame}
\begin{figure}
    \begin{tikzpicture}[->,scale=1.8, auto,swap]
        % Draw the vertices.
        \node (a) at (0,0) {$a (this is text)$};
        \node (b) at (0,1) {$b$};
        \node (c) at (1,1) {$c$};
        \node (d) at (1,0) {$d$};
		\node (e) at (3,1) {$d$};
 
        % Connect vertices with edges and draw weights
        \path (a) edge node {} (b);
        \path (b) edge node {} (c);
        \path (c) edge node {} (d);
        \path (d) edge node {} (a);

		\begin{pgfonlayer}{background}
			\path<2->[draw,line width=5pt,-,red!50] (a.center) edge node {} (b.center);
			\path<10->[draw,line width=5pt,-,red!50] (b.center) edge node {} (d.center);
			\path<12->[draw,line width=5pt,-,red!50] (d.center) edge node {} (e.center);
		\end{pgfonlayer}
    \end{tikzpicture}
\end{figure}
\end{frame}
\end{document}
```

<h3>Simplify it</h3>
You can make some definitions, e.g.:
{% highlight latex %}draw,line width=5pt,-,red!50{% endhighlight %}
can be replaced by
{% highlight latex %}\tikzstyle{selected edge} = [draw,line width=5pt,-,red!50]{% endhighlight %}

You can make loops:

```latex
{% raw %}	% Draw the vertices.
	\foreach \pos / \identifier / \name in {{(0,0)/a/a (this is text)}, 
		{(0,1)/b/b}, {(1,1)/c/c}, {(1,0)/d/d}, {(3,1)/e/d}}
		\node (\identifier) at \pos {$\name$};{% endraw %}
```


<h2>The whole, working template</h2>
```latex
\documentclass[hyperref={pdfpagelabels=false}]{beamer}
\usepackage{lmodern}

\usepackage[utf8]{inputenc} % this is needed for german umlauts
\usepackage[ngerman]{babel} % this is needed for german umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf

\usepackage{verbatim}
\usepackage{tikz}
\usetikzlibrary{arrows,shapes}

% Define some styles for graphs
\tikzstyle{vertex}=[circle,fill=black!25,minimum size=20pt,inner sep=0pt]
\tikzstyle{selected vertex} = [vertex, fill=red!24]
\tikzstyle{blue vertex} = [vertex, fill=blue!24]
\tikzstyle{edge} = [draw,thick,-]
\tikzstyle{weight} = [font=\small]
\tikzstyle{selected edge} = [draw,line width=5pt,-,red!50]
\tikzstyle{ignored edge} = [draw,line width=5pt,-,black!20]

% see http://deic.uab.es/~iblanes/beamer_gallery/index_by_theme.html
\usetheme{Frankfurt}
\usefonttheme{professionalfonts}

% disables bottom navigation bar
\beamertemplatenavigationsymbolsempty

% http://tex.stackexchange.com/questions/23727/converting-beamer-slides-to-animated-images
\setbeamertemplate{navigation symbols}{}%

\begin{document}
\pgfdeclarelayer{background}
\pgfsetlayers{background,main}

\begin{frame}
	\begin{figure}
		\begin{tikzpicture}[->,scale=1.8, auto,swap]
			% Draw the vertices. First you define a list.
			\foreach \pos/\name in {% raw %}{{(0,0)/a}, {(0,2)/b}, {(1,2)/c},
				                    {(1,0)/d}, {(2,1)/e}, {(3,1)/f}, 
									{(4,2)/g}, {(5,2)/h}, {(4,0)/i},
									{(5,0)/j}}{% endraw %}
				\node[vertex] (\name) at \pos {$\name$};

			% Connect vertices with edges and draw weights
			\foreach \source/ \dest /\pos in {a/b/, b/c/, c/d/, d/a/,
										c/e/bend left, d/e/, e/c/,
										e/f/, f/g/, f/i/,
										g/f/bend right, i/f/bend left,
										g/h/, h/j/, j/i/, i/g/}
				\path (\source) edge [\pos] node {} (\dest);

			% Start animating the edge selection. 
			% For convenience we use a background layer to 
			% highlight edges. This way we don't have to worry about 
			% the highlighting covering weight labels. 
			\begin{pgfonlayer}{background}
				\foreach \source / \dest / \fr / \pos in {d/a/1/,
						a/b/2/, b/c/3/, c/d/4/, d/e/5/, e/c/6/, 
						c/e/7/bend left, e/f/8/, f/g/9/,
						g/f/10/bend right, f/i/11/, i/g/12/, g/h/13/, 
						h/j/14/, j/i/15/, i/f/16/bend left}
				    \path<\fr->[selected edge] (\source.center) edge 
										[\pos] node {} (\dest.center);
			\end{pgfonlayer}
		\end{tikzpicture}
	\end{figure}
	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
	sed diam nonumy eirmod tempor invidunt ut labore et dolore
	magna aliquyam erat, sed diam voluptua. At vero eos et 
	accusam et.
\end{frame}
\end{document}
```latex

<h2>Resources</h2>
<ul>
  <li><a href="http://paws.wcu.edu/tsfoguel/tikzpgfmanual.pdf">TikZ and pgf: Manual for version 1.18</a></li>
  <li><a href="http://www.texample.net/tikz/examples/">TeXamples.net</a>: Great page with many Tikz-Examples</li>
  <li><a href="http://www.tex.ac.uk/CTAN/macros/latex/contrib/beamer/doc/beameruserguide.pdf">The beamer class</a></li>
</ul>
