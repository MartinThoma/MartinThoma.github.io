---
layout: post
title: Citations with LaTeX
slug: citations-with-latex
author: Martin Thoma
status: draft
date: 2019-12-28 20:00
category: My bits and bytes
tags: LaTeX
featured_image: logos/latex.png
---

## Minimal Example

TODO

## The bibliography file

This is the core for your citations. Your citation library, if you want so.
You can fill this file with JabRef or by hand.

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
