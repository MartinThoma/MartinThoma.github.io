---
layout: post
title: Plot runtime in LaTeX from CSV
author: Martin Thoma
date: 2012-06-23 12:37:04
categories: 
- Code
tags:
- LaTeX
- CSV
featured_image: 2012/01/latex-logo.png
---
I am currently analyzing how fast matrix multiplications are. I execute the program with this command:

{% highlight bash %}python library-numpy.py -i 100.txt > /dev/null{% endhighlight %}

You can get the time with the <a href="http://en.wikipedia.org/wiki/Time_(Unix)">time tool</a>:
{% highlight bash %}/usr/bin/time -f "%U" python library-numpy.py -i $i >/dev/null{% endhighlight %}

Now loop over every input file in this folder:
{% highlight bash %}for i in *.txt; do /usr/bin/time -f "%U" python library-numpy.py -i $i >/dev/null; done{% endhighlight %}

And now prefix the results.
{% highlight bash %}for i in *.txt; do echo "${i%.txt}" >> time.csv; /usr/bin/time -o time.csv -a -f "%U" python library-numpy.py -i $i >/dev/null; done{% endhighlight %}

http://latex-community.org/know-how/437-tufte-charts
