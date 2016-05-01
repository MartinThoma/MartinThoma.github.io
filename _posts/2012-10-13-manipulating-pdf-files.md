---
layout: post
title: Manipulating PDF files
author: Martin Thoma
date: 2012-10-13 10:24:01.000000000 +02:00
category: Cyberculture
tags: PDF, pdftk
featured_image: 2012/10/pdf-icon.png
---
I just wanted to get some pages out of a bigger PDF file. The tool that can be used for this task is called <code>pdftk</code>. It is in the standard Ubuntu repsitory.

<h2>Usage</h2>
Split the file, so that every page becomes a new PDF file:
{% highlight bash %}pdftk myfile.pdf burst{% endhighlight %}

Extract pages 10 to 12 from <tt>bigPDF.pdf</tt>:
{% highlight bash %}pdftk bigPDF.pdf cat 10-12 output output.pdf{% endhighlight %}
