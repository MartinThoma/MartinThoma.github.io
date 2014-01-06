---
layout: post
title: How to typeset chess games with LaTeX
author: Martin Thoma
date: 2012-09-11 08:18:38
categories: 
- Cyberculture
tags: 
- LaTeX
featured_image: 
---
<h2>Chessboard</h2>
<h3>Simple example</h3>
{% caption align="aligncenter" width="296" caption="Chessboard - simple example" url="../images/2012/09/chess-chessboard-simple-example.png" alt="Chessboard - simple example"  height="268" class="size-full wp-image-44411 "  %}

{% highlight text %}\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\setlength\PreviewBorder{5mm}

\usepackage{chessboard}

\begin{document}
\begin{preview}

\chessboard[setfen=5rk1/pp3N1p/4P3/2P5/3Q1PK1/P7/1Pr3pq/R3R3 w - - 0 0,
            showmover]

\end{preview}
\end{document}{% endhighlight %}


From <a href="http://tex.stackexchange.com/a/54192/5645">tex.stackexchange.com</a>.
<h2>Skak</h2>
<h3>Simple example</h3>
{% caption align="aligncenter" width="254" caption="Simple example with skak" url="../images/2012/09/chess-skak-simple-example.png" alt="Simple example with skak"  height="289" class="size-full wp-image-44401 "  %}

{% highlight text %}\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\setlength\PreviewBorder{5mm}

\usepackage{skak}

\begin{document}
\begin{preview}

% sets the internal board or a new game
\newgame
% typesets the moves and updates the board
\mainline{1.e4 e5 2. Nf3 Nc6 3.Bb5}\\
% show the current board position
\showboard

\end{preview}
\end{document}{% endhighlight %}
<h2>See also</h2>
<ul>
  <li><a href="ftp://ftp.rrzn.uni-hannover.de/pub/mirror/tex-archive/macros/latex/contrib/chessboard/chessboard.pdf">Chessboard documentation</a></li>
  <li><a href="ftp://ftp.tu-chemnitz.de/pub/tex/fonts/chess/skak/doc/skakdoc.pdf">Skak documentation</a> - <a href="ftp://ftp.mpi-sb.mpg.de/pub/tex/mirror/ftp.dante.de/pub/tex/fonts/chess/skak/doc/refman.pdf">short reference</a></li>
</ul>