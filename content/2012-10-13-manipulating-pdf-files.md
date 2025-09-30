---
layout: post
lang: en
title: Manipulating PDF files
slug: manipulating-pdf-files
author: Martin Thoma
date: 2012-10-13 10:24:01.000000000 +02:00
category: Cyberculture
tags: PDF, pdftk
featured_image: 2012/10/pdf-icon.png
---
I just wanted to get some pages out of a bigger PDF file. The tool that can be used for this task is called <code>pdftk</code>. It is in the standard Ubuntu repsitory.

<h2>Usage</h2>
Split the file, so that every page becomes a new PDF file:
```bash
pdftk myfile.pdf burst
```

Extract pages 10 to 12 from <tt>bigPDF.pdf</tt>:
```bash
pdftk bigPDF.pdf cat 10-12 output output.pdf
```
