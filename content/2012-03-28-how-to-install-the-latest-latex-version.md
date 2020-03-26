---
layout: post
title: How to install the latest LaTeX Version
author: Martin Thoma
date: 2012-03-28 11:29:41.000000000 +02:00
category: My bits and bytes
tags: LaTeX
featured_image: 2012/01/latex-logo.png
alias: /install-latex/index.html
---
I recently had <a href="http://tex.stackexchange.com/questions/49543/how-can-i-place-numbers-into-marks-of-a-plot">some problems</a> with TikZ because of my outdated LaTeX-Version. Ubuntu does only provide TeX Live 2009. The latest one is TeX Live 2013. As Ubuntu doesn't provide the latest LaTeX-Code, I'll explain how to install it by yourself on an Ubuntu System.

## What is LaTeX? ##
LaTeX is a document markup language. So with LaTeX you're able to write math formula like $\sum_{i=0}^\infty \frac{1}{2^i} = 2$. The term LaTeX refers only to the language in which documents are written, not to the editor used to write those documents. In order to create a document in LaTeX, a .tex file must be created using some form of text editor. While most text editors can be used to create a LaTeX document, a number of editors have been created specifically for working with LaTeX.

A number of TeX distributions are available, including TeX Live (multiplatform) and MiKTeX (Windows). When I write "LaTeX" I think of "TeX Live".

## LaTeX: an Hello World example ##
This is the template I use when I want to write a minimal LaTeX PDF document. You can use it as an example.

```latex
\documentclass[a4paper,10pt]{article}
\usepackage{amssymb}		% needed for math
\usepackage{amsmath}		% needed for math
\usepackage{amsthm}   		% needed for proof environment
\usepackage[utf8]{inputenc} % this is needed for umlauts
\usepackage[ngerman]{babel} % this is needed for umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output of umlauts in pdf
\usepackage{geometry}
\geometry{top=1cm,left=1cm,right=1cm,bottom=1cm}

\pdfinfo{
   /Author (Martin Thoma)
   /Title  (Analysis I)
   /Subject (Analysis I)
   /Keywords (Analysis I; Venn-Diagramm)
}

\newtheorem*{vor}{Voraussetzung}
\newtheorem*{beh}{Behauptung}

  \begin{document}
\section{Hello World}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

\subsection{This is an subsection}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse

\end{document}
```

If LaTeX is available on your system, you can create the PDF file from this myDocument.tex file with this command:

```bash
pdflatex myDocument.tex -output-format=pdf
```

This will create a .log file, an .aux file

Here is the <a href='../images/2012/03/latex-template.zip'>LaTeX template</a> with the resulting PDF.

## Install the latest LaTeX ##
<div class="important">Follow the instructions on <a href="http://tug.org/texlive/acquire-netinstall.html">tug.org</a>.</div>
It's a Network installation, so it will need Internet access. It needs to download about 2 GB so it will take some time. But everything is done automatically.

You should remove your old installation before you start the new one:

```bash
sudo apt-get purge texlive-*
sudo apt-get autoremove
```

```bash
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -zxvf install-tl-unx.tar.gz
cd install-tl-*
sudo ./install-tl
I
```


After you've started your installation, you can choose options (O). Then you should choose "create symlinks in standard directories" (L).

If you didn't do so, add the path to your PATH (See <a href="http://askubuntu.com/a/60221/10425">How to add a directory to my path?</a>, <a href="http://askubuntu.com/a/60769/10425">How do I add a directory to MANPATH or INFOPATH?</a> and <a href="http://askubuntu.com/a/59127/10425">Reload .profile</a>):

```bash
PATH=$PATH:/usr/local/texlive/2013/bin/i386-linux/
```

That's it. So my <code>.profile</code> got these additional lines:

```text
if [ -d "/usr/local/texlive/2013/bin/i386-linux" ] ; then
    PATH="/usr/local/texlive/2013/bin/i386-linux:$PATH"
fi

if [ -d "/usr/local/texlive/2013/bin/x86_64-linux" ] ; then
    PATH="/usr/local/texlive/2013/bin/x86_64-linux:$PATH"
fi

if [ -d "/usr/local/texlive/2013/texmf/doc/man" ] ; then
    MANPATH="/usr/local/texlive/2013/texmf/doc/man:$MANPATH"
fi

if [ -d "/usr/local/texlive/2013/texmf/doc/info" ] ; then
    INFOPATH="/usr/local/texlive/2013/texmf/doc/info:$INFOPATH"
fi
```

edit: I've just installed TeX-Live 2013 and had to do this:

```bash
moose@pc07:/usr/bin$ rm latex
moose@pc07:/usr/bin$ sudo ln -s /usr/local/texlive/2013/bin/i386-linux/pdflatex latex
```

You can try if your installation works by `latex --version`:

```text
pdfTeX 3.1415926-1.40.10-2.2 (TeX Live 2009/Debian)
kpathsea version 5.0.0
Copyright 2009 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
There is NO warranty.  Redistribution of this software is
covered by the terms of both the pdfTeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the pdfTeX source.
Primary author of pdfTeX: Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).
Compiled with libpng 1.2.42; using libpng 1.2.42
Compiled with zlib 1.2.3.3; using zlib 1.2.3.3
Compiled with poppler version 0.12.4
```

If an old version is shown, you might want to see where it is located:

```bash
which latex
```

## Update ##
```bash
cd /usr/local/texlive/2013/bin/i386-linux
sudo ./tlmgr update --self
sudo ./tlmgr update --all
```

## See also ##
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/LaTeX">LaTeX</a>, <a href="http://en.wikipedia.org/wiki/TeX_Live">TeX Live</a></li>
  <li>Wikibooks: <a href="http://en.wikibooks.org/wiki/LaTeX">LaTeX</a>, <a href="http://de.wikibooks.org/wiki/LaTeX-Kompendium">LaTeX-Kompendium</a> (German)</li>
  <li>UbuntuUsers (German): <a href="http://wiki.ubuntuusers.de/LaTeX">LaTeX</a></li>
</ul>
