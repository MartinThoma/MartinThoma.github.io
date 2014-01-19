---
layout: post
title: LaTeX Beamer
author: Martin Thoma
date: 2013-03-05 11:25:20.000000000 +01:00
categories:
- Cyberculture
tags:
- LaTeX
- Beamer
- Presentation
featured_image: 2012/01/latex-logo.png
---
I really enjoy creating presentations with LaTeX. The reasons are:

<ul>
  <li>You can use versioning (GIT, SVN, ...)</li>
  <li>You can use your favorite editor!</li>
  <li>When you've created an animation with Ti<em>k</em>Z, you can easily go one step back an go through it as fast as it is apropriate!</li>
  <li>Good separation of presentation and content</li>
  <li>It compiles to PDF
    <ul>
      <li>Everybody can open it</li>
      <li>It always looks the same (no moved elements or hidden bullet points)</li>
    </ul>
  </li>
  <li>You can use math mode :-)</li>
  <li>No need to buy anything. It's free and OpenSource.</li>
  <li>A big community (<a href="http://tex.stackexchange.com/questions/tagged/beamer">StackExchange</a> and <a href="http://www.latex-community.org/forum/viewforum.php?f=3">LateX-Community</a>) helps you, when you got questions.</li>
</ul>

I'll now introduce you to the basics of LaTeX beamer presentations. If you only look for example, please go to my <a href="https://github.com/MartinThoma/LaTeX-examples/tree/master/presentations">GitHub LaTeX Repository</a>.

<h2>Basics</h2>

This is a basic presentation:

```latex
\documentclass{beamer}
\usetheme{Frankfurt}
\usepackage{hyperref}
\usepackage[utf8]{inputenc} % this is needed for german umlauts
\usepackage[english]{babel} % this is needed for german umlauts
\usepackage[T1]{fontenc}    % this is needed for correct output 
                            % of umlauts in pdf

\begin{document}

\title{The title of your presentation}
\subtitle{A subtitle}
\author{Martin Thoma}
\date{25. March 2013}
\subject{Computer Science}

\frame{\titlepage}

\section{Introduction}
\subsection{A subsection!}
\begin{frame}{Slide title}
    Slide content
\end{frame}

\end{document}
```

<h2>Style</h2>
If you want to create nice-looking presentations like <a href="../images/2013/03/tutorium-05.pdf">this one</a> or <a href="../images/2013/03/google-presentation.pdf">that one</a>, you should probably adjust the style. Here is an overview of the default ones that LaTeX has: <a href="http://deic.uab.es/~iblanes/beamer_gallery/">Beamer theme gallery</a> or <a href="http://latex.simon04.net/">here</a>.

The important commands for changing the appearance, that should get included just after documentclass, are:

```latex
\usetheme{Frankfurt}
\usecolortheme{default}
```

When you're from KIT, you should use the <a href="https://sdqweb.ipd.kit.edu/wiki/Dokumentvorlagen">KIT theme</a>.

Here are some screenshots:
{% gallery size="medium" columns="2" %}
    ../images/2013/03/English-Titlepage.png "LaTeX Beamer: Example of a titlepage"
    ../images/2013/03/programmieren-tutorium-titlepage.png  "LaTeX Beamer: Example of a titlepage"
    ../images/2013/03/latex-beamer-quelltext-minted.png "LaTeX Beamer: Example of source code"
    ../images/2013/03/latex-beamer-uncover-list.png "LaTeX Beamer: Example of a slide"
{% endgallery %}

<h2>Sections and subsections</h2>
Take a look at the slides I've included above. Do you notice the little bubbles at the bottom that indicate how many slides are left?

You get the text over the bubbles with <code>\section{Your text}</code> and the bubbles with <code>frame</code>, but you need at least one <code>\subsection{bla}</code>! When you make more than one subsection, the frame-bubbles that belong to the same one get highlighted.

<h2>Reveal information</h2>
You might want to try those commands to hide and reveal information:

* `\pause`
* `\uncover`
* `\visible`
* `\onslide` and `\only`

You can use it like this:

```latex
\begin{frame}{Another title}
    Some text\\
    \uncover<2->{Uncover me on slide 2 (-)\\}
    \visible<3->{visible from slide 3 on (-)\\}
    \only<4->{only from slide 4 (-)\\} 
    \onslide<5->{on slide 5 and further (-)\\}
    \uncover<6>{Uncover me on slide 6 \\}
    \visible<7>{visible on 7\\}
    \only<8>{only on slide 8 \\} 
    \alt<8>{I am on slide 8\\}{I am not on slide 8\\}
    \onslide<9>{on slide 9\\}
\end{frame}
```

Note that the numbers work like `\uncover<n-m>{ELEMENT}`. If no `m` 
is specified, ELEMENT is visible until end of this frame.

When you have a list and you want to uncover it element by element, 
you can use this:

```latex
\begin{itemize}<+->
    \item one
    \item two
    \item three
\end{itemize}
```

<h2>Blocks</h2>
You can use <code>block</code>, <code>exampleblock</code> or <code>alertblock</code> inside your frame:

```latex
\begin{exampleblock}{Test}
  This is my text.
\end{exampleblock}
```

It looks like this:
{% caption align="aligncenter" width="300" caption="LaTeX Beamer blocks: block, exampleblock, alertblock" url="../images/2013/03/latex-beamer-block-300x117.png" alt="LaTeX Beamer blocks: block, exampleblock, alertblock"  height="117" class="size-medium wp-image-59391" %}

<h2>Images</h2>
Quite often, you want to have one big image.

You need `\usepackage{graphicx}` in your preamble.

This is how you get the image it:

```latex
\begin{frame}{My frame title}
    \includegraphics[width=\textwidth, height=0.8\textheight, keepaspectratio]{../relative/path/image.jpg}
\end{frame}
```

<h2>Further reading</h2>
<ul>
  <li><a href="../sizes-in-latex/" title="Sizes in LaTeX">Sizes in LaTeX</a></li>
  <li><a href="../how-to-visualize-graph-algorithms-with-latex/" title="How to visualize Graph algorithms with LaTeX">How to visualize Graph algorithms with LaTeX</a></li>
  <li><a href="http://www.math.umbc.edu/~rouben/beamer/beamer_guide.pdf">UMBC Beamer guide</a></li>
  <li><code>texdoc beameruserguide</code> or <a href="http://www.tex.ac.uk/tex-archive/macros/latex/contrib/beamer/doc/beameruserguide.pdf">online</a></li>
</ul>
