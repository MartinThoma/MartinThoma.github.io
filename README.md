## Prerequisites

- `git clone git@github.com:MartinThoma/MartinThoma.github.io.git --recursive` to get the blog data with all submodules
- `pre-commit install`
- `pip install -r requirements.txt --user` to install the required software
- `sudo apt-get install npm && sudo apt-get install nodejs && sudo npm install -g mediumexporter`
- `make html-local` and `make serve` to see the result on http://127.0.0.1:8000/

## Get article from medium

```bash
mediumexporter https://infosecwriteups.com/redos-denial-of-service-by-regex-59c7ffab4880 > 2022-03-07-redos.md
```

## TODO

- `linkchecker https://martin-thoma.com -F csv`
- add pagination for category pages / tag pages
- Semantic anchors created by TOC
- Newlines
    - e.g. 2013-03-16-c-puzzle-3.html (http://martinthoma.github.io/c-puzzle-3/)
- Don't check for Latex ($...$) inside of highlight environment or
  fenced code blocks (Abostrophes):
    - http://martinthoma.github.io/c-puzzle-3/
    - http://martin-thoma.com/plotting-graphs-with-pgfplots-latex-and-tikz/
    - http://martin-thoma.com/semantische-sicherheit/
    - http://martin-thoma.com/how-to-search-for-mathematical-symbols-in-latex/
    - http://martin-thoma.com/latex-versioning-a-great-experience/
    - All posts tagged with "PHP"
- Markdown rendered within fenced code tag: http://martin-thoma.com/how-to-print-source-code-with-latex/
- Fix posts:
    - http://martin-thoma.com/comparing-dates-in-php-and-mysql/
    - http://martin-thoma.com/algorithmen-ii-klausur/ (LaTeX)
    - http://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/ (LaTeX at bottom)
- Apply CSS Rules from [CSS Wizardry](https://github.com/csswizardry/CSS-Guidelines)

## Improve

- Site speed
    - Minify results
    - Combine CSS / JS files
    - Remove JS files if possible
    - Remove parts of JS that are not used
- Excerpts

## Testen

- WordPress "Caption" tags
- RSS Feed


## Sublime

The following snippets help to create new articles fast. To install them, go to
"Tools &rightarrow; New Snippet..." in Sublime&nbsp;Text&nsp;3.

Go to `/home/moose/.config/sublime-text-3/Packages/User` and copy the contents
of the `./sublime` folder in it. Or add symbolic links:

```bash
$ ln -s ~/Github/Martin/MartinThoma.github.io/sublime/blog-article.sublime-snippet /home/moose/.config/sublime-text-3/Packages/User
```

### blog-article

```text
<snippet>
    <content><![CDATA[
---
layout: post
title: ${1:}
slug: ${2:}
author: Martin Thoma
status: draft
date: ${3:2016}-${4:04}-${5:31} 20:00
category: ${6:Cyberculture}
tags: ${7:Rating}
featured_image: logos/${8:star.png}
---
${9:}
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
