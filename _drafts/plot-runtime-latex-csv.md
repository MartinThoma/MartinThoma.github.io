---
layout: post
title: Plot runtime in LaTeX from CSV
author: Martin Thoma
date: 2012-06-23 12:37:04
categories: 
- Code
tags: []
featured_image: 2012/01/latex-logo.png
---
I am currently analyzing how fast matrix multiplications are. I execute the program with this command:

[bash]python library-numpy.py -i 100.txt &gt;/dev/null[/bash]

You can get the time with the <a href="http://en.wikipedia.org/wiki/Time_(Unix)">time tool</a>:
[bash]/usr/bin/time -f &quot;%U&quot; python library-numpy.py -i $i &gt;/dev/null[/bash]

Now loop over every input file in this folder:
[bash]for i in *.txt; do /usr/bin/time -f &quot;%U&quot; python library-numpy.py -i $i &gt;/dev/null; done[/bash]

And now prefix the results.
[bash]for i in *.txt; do echo &quot;${i%.txt}&quot; &gt;&gt; time.csv; /usr/bin/time -o time.csv -a -f &quot;%U&quot; python library-numpy.py -i $i &gt;/dev/null; done[/bash]

http://latex-community.org/know-how/437-tufte-charts