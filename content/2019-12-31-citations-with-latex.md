---
layout: post
title: Citations with LaTeX
slug: citations-with-latex
author: Martin Thoma
date: 2019-12-31 20:00
category: My bits and bytes
tags: LaTeX
featured_image: logos/latex.png
---
Managing citations is a core task when writing scientific documents. Of course,
there are lots of options to do this with LaTeX. This makes it super confusing.
If you need help, try [tex.stackexchange.com](https://tex.stackexchange.com/).
The guys there are super helpful and extremely knowledgable. If you don't even
know how to formulate your question properly, try the [tex webchat](https://chat.stackexchange.com/rooms/41/tex-latex-and-friends).

<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>

## Minimal Example

This is in my [LaTeX-examples](https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/seminar-paper)

The `main.tex` looks as follows:

```
\documentclass[a4paper,12pt]{scrartcl}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}

\usepackage[raiselinks=true,
            bookmarks=true,
            bookmarksopenlevel=1,
            bookmarksopen=true,
            bookmarksnumbered=true,
            breaklinks,
            hyperindex=true,
            plainpages=false,
            pdfpagelabels=true,
            pdfborder={0 0 0.5}]{hyperref}

\usepackage[
natbib,
backend=biber,
style=alphabetic,
citestyle=authoryear
]{biblatex}
\addbibresource{bibliography.bib}

\begin{document}
Reference sentences are too often Lorem Ipsum \parencites[p. 345]{alice}[p. 123]{bob}
\end{document}
```

and the `bibliography.bib` like this:

```
% Encoding: UTF-8
@article{alice,
  title={The Theory of Lorem},
  author={Al Alice},
  journal={Journal of Foo},
  volume={5},
  number={4},
  pages={123--456},
  year={1992},
  publisher={Springer}
}

@Book{bob,
  title     = {A guide to Ipsum},
  publisher = {Cambridge university press},
  year      = {2010},
  author    = {Bobby Bob},
}

```

Compile it with

```
pdflatex main.tex -output-format=pdf
biber main
pdflatex main.tex -output-format=pdf
```

## The bibliography file

This is the core for your citations. Your citation library, if you want so.
You can fill this file with [JabRef](https://www.jabref.org/) or by hand.

## Packages

* natbib
* biber

## Commands

```tex
% Normal one: Cite two elements
\cite{ref2007, ref2009}

% Cite in parenthesis
\citep{ref2007, ref2009}

% Cite only year in parenthesis
\citet{ref2007, ref2009}

% Change multiple options
\parencite[p. 123]{ref2007}[p. 456]{ref2009}
```


## See also

* tom: [Mulitple reference citation](https://texblog.org/2007/05/28/mulitple-reference-citation/) on texblog, 2007.
* [Bibliography management with natbib](https://da.overleaf.com/learn/latex/Bibliography_management_with_natbib) on overleaf
* [Put parentheses around year in citation](https://tex.stackexchange.com/q/104518/5645) on tex.stackexchange
* [Biblatex citation styles](https://www.overleaf.com/learn/latex/Biblatex_citation_styles) on overleaf
