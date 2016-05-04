Prerequisites
=============
* `git clone git@github.com:MartinThoma/MartinThoma.github.io.git --recursive` to get the blog data
* `pip install -r requirements.txt --user` to install the required software
* `make html-local` and `make serve` to see the result on http://127.0.0.1:8000/

TODO
=====

* add pagination for category pages / tag pages
* Semantic anchors created by TOC
* Newlines
  - e.g. 2013-03-16-c-puzzle-3.html (http://martinthoma.github.io/c-puzzle-3/)
* Don't check for Latex ($...$) inside of highlight environment or
  fenced code blocks (Abostrophes):
  - http://martinthoma.github.io/c-puzzle-3/
  - http://martin-thoma.com/plotting-graphs-with-pgfplots-latex-and-tikz/
  - http://martin-thoma.com/semantische-sicherheit/
  - http://martin-thoma.com/how-to-search-for-mathematical-symbols-in-latex/
  - http://martin-thoma.com/latex-versioning-a-great-experience/
  - All posts tagged with "PHP"
* Markdown rendered within fenced code tag: http://martin-thoma.com/how-to-print-source-code-with-latex/
* Fix posts:
  - http://martin-thoma.com/comparing-dates-in-php-and-mysql/
  - http://martin-thoma.com/algorithmen-ii-klausur/ (LaTeX)
  - http://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/ (LaTeX at bottom)
* Apply CSS Rules from [CSS Wizardry](https://github.com/csswizardry/CSS-Guidelines)


Improve
========
* Site speed
  * Minify results
  * Combine CSS / JS files
  * Remove JS files if possible
  * Remove parts of JS that are not used
* Excerpts


Testen
=======
* WordPress "Caption" tags
* RSS Feed


Required
========
First:

    sudo apt-get install rubygems ruby-dev libmagickwand-dev

Although there is a `jekyll` package on Debian-Systems, you should not install it. Rather do it this way:

Then

    sudo gem install juicer jekyll dimensions rmagick
    sudo juicer install jslint
    sudo juicer install yui_compressor


Install
========

See http://martin-thoma.com/jekyll-and-git/

## Sublime

The following snippets help to create new articles fast. To install them, go to
"Tools &rightarrow; New Snippet..." in Sublime&nbsp;Text&nsp;3.

### blog-article

```text
<snippet>
    <content><![CDATA[
---
layout: post
title: ${1:}
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- ${2:Cyberculture}
tags:
- ${3:Rating}
featured_image: logos/${4:star.png}
---
${5:}
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <tabTrigger>---</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```


### caption-tag

```text
<snippet>
    <content><![CDATA[
{% caption align="aligncenter" width="500" alt="${1:text}" text="${1:text}" url="../images/2015/01/${2:image.png}" %}
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
    <tabTrigger>captiontag</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```

### gallery-tag
