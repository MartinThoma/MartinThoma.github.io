---
layout: post
status: publish
published: true
title: PDF-Printing on Windows 7
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 52851
wordpress_url: http://martin-thoma.com/?p=52851
date: 2012-12-31 17:23:10.000000000 +01:00
categories:
- Cyberculture
tags:
- PDF
- windowsrage
- Windows 7
comments: []
featured_image: 2012/10/pdf-icon.png
---
"Printing" files on PDF-printers is useful as you can save everything as a digital PDF file instead of printing it. 

I've just installed <a href="http://www.heise.de/download/typing-test-tq-1128987.html">Typing Test TQ</a> for testing my typing speed and I wanted to save my results. This wasn't possible, but I could print them. So I thought I could print it to a PDF file and store it this way on my computer. Once again, I didn't think of Microsoft. 

<h2>The Linux-Way</h2>
How would you solve this problem on a Debian machine? Well, most Debian machines would have a PDF printer pre-installed. So you would simply click on print, choose the PDF printer and be happy.

If it is not pre-installed, type:
{% highlight bash %}sudo apt-get install cups-pdf{% endhighlight %}
Now you can use a PDF printer.

Done. It works.

<h2>The Windows-Way</h2>
Windows 7 does not have a PDF printer, but it has a "Microsoft XPS Document Writer". Lets see what this is:

<h3>XPS</h3>
<h4>General Information</h4>
<a href="http://en.wikipedia.org/wiki/Open_XML_Paper_Specification">Open XML Paper Specification</a> is an open specification for a page description language and a fixed-document format originally developed by Microsoft as XML Paper Specification (XPS) that was later standardized by Ecma International as international standard ECMA-388. It is an XML-based specification, based on a new print path and a color-managed vector-based document format that supports device independence and resolution independence. OpenXPS was standardized as an open standard document format on June 16, 2009.

<h4>XPS vs. PDF</h4>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Comparison_of_OpenXPS_and_PDF">Comparison of OpenXPS and PDF</a></li>
  <li><a href="http://superuser.com/questions/73206/xps-vs-pdf-whats-the-status">XPS vs PDF. What's the status?</a> on superusers</li>
</ul>

<h4>TL;DR</h4>
XPS is an alternative for PDF. It lacks program support compared to PDF.

<h3>Getting a PDF-Printer</h3>
After a quick search, I found <a href="http://www.cutepdf.com/Products/CutePDF/writer.asp">CutePDF</a>. Seems to work, but I don't give any malware-freeness-guarantees.

Although I don't know if there is malware, there is definitely some spam content:
[caption id="attachment_52891" align="aligncenter" width="518"]<a href="http://martin-thoma.com/wp-content/uploads/2012/12/windows-7-browser-toolbar.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/12/windows-7-browser-toolbar.png" alt="Windows 7: Install another browser toolbar" width="518" height="413" class="size-full wp-image-52891" /></a> Windows 7: Install another browser toolbar[/caption]

Why can't it simply only install a PDF-printer without getting annoyed with toolbars? I never had this problem on Linux...
