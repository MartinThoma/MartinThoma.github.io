---
layout: post
status: publish
published: true
title: Manipulating PDF files
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 46801
wordpress_url: http://martin-thoma.com/?p=46801
date: 2012-10-13 10:24:01.000000000 +02:00
categories:
- Cyberculture
tags:
- PDF
- pdftk
comments: []
featured_image: 2012/10/pdf-icon.png
---
I just wanted to get some pages out of a bigger PDF file. The tool that can be used for this task is called <code>pdftk</code>. It is in the standard Ubuntu repsitory.

<h2>Usage</h2>
Split the file, so that every page becomes a new PDF file:
{% highlight bash %}pdftk myfile.pdf burst{% endhighlight %}

Extract pages 10 to 12 from <tt>bigPDF.pdf</tt>:
{% highlight bash %}pdftk bigPDF.pdf cat 10-12 output output.pdf{% endhighlight %}
