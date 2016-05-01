---
layout: post
title: Reference Management with JabRef
author: Martin Thoma
date: 2014-06-15 20:51
category: Science
tags: Science, References, Software, LaTeX
featured_image: logos/jabref.png
---

Keeping track of papers, articles and books or more general sources you can
cite is a task you will have to tackle when you're writing your thesis. One
way to store information is via BibTeX files.

BibTeX is a reference management software that is used together with LaTeX.
If you're new to BibTeX or references in LaTeX in general you could read the
followin articles:

* [bibtex vs. biber and biblatex vs. natbib](http://tex.stackexchange.com/q/25701/5645)
* [What is the difference between bibtex and biblatex?](http://tex.stackexchange.com/q/8411/5645) - I keep forgetting that all the time.

I've tried to create a [MWE for biblatex](https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/biblatex-mwe), but as I don't really know much about BibTeX it's probably not
the best resource to start with.

A longer [working example of BibTeX](https://github.com/MartinThoma/write-math/tree/master/bachelor-arbeit)
is my bachelors thesis (work is still in (slow) progress).

## What is JabRef?

[JabRef](https://en.wikipedia.org/wiki/JabRef) is a reference management
software that uses BibTeX as its native format. It looks like this:

{% caption align="aligncenter" width="500" alt="JabRef" text="JabRef" url="../images/2014/06/jabref.png" %}

## How can I get it?

JabRef 2.10 beta is part of the Debian sources. Thus it can be installed by

```bash
sudo apt-get install jabref
```

The official development page is [jabref.sourceforge.net](http://jabref.sourceforge.net/).
As it is written in Java it can be installed on all (or at least most) systems
where you have a JVM (thus: good news Windows / Mac users!).

## What's good about JabRef?

You can easily add the information where the PDF is located on your system and
open the PDF directly via JabRef:

{% caption align="aligncenter" width="500" alt="Adding PDF with JabRef" text="Adding PDF with JabRef" url="../images/2014/06/jabref-pdf.png" %}

This is especially powerfull with the search. As you can add quite a lot of
information to the entries (such as the abstract and comments) and searching
that is faster / easier than searching folders of PDFs, it's very convenient
to use JabRef for opening your PDFs:

{% caption align="aligncenter" width="500" alt="Searching with JabRef" text="Searching with JabRef" url="../images/2014/06/jabref-searching.png" %}

The preview also helps you to see how it might appear in your document:

{% caption align="aligncenter" width="500" alt="JabRef preview" text="JabRef preview" url="../images/2014/06/jabref-preview.png" %}

Another nice feature is the autocompletion of authors names and titles.

## What could be better?

It would be neat if you could automatically upload your BibTeX file and use
other peoples BibTeX files to **complete the information** or to get informed of
possible errors in your database.

Additionally, a good **PDF reader** that is fast and allows annotations of which
JabRef would be aware would be awesome.

**Speed** is quite often an issue with Java applications in my experience.
It takes about 5 seconds to open my BibTeX file of about 37 references. After
starting that it's ok.

**Shortcuts** are important for tools that get used often, too. Although
JabRef has some reasonable shortcuts like <kbd>Ctr</kbd>+<kbd>i</kbd> for
importing a BibTeX file and <kbd>Ctr</kbd>+<kbd>s</kbd> for saving the current
BibTeX file, I miss <kbd>Ctrl</kbd>+<kbd>f</kbd> for searching the database.

**Importing** other BibTeX files into the current BibTeX file is possible. But
I would also like to "import" BibTeX data by copy and pasting a single dataset.

## Alternatives

[Mendeley](https://en.wikipedia.org/wiki/Mendeley) is a closed-source alternative
with a built-in PDF reader. It seems to be fast and can complete information
when the title is given.