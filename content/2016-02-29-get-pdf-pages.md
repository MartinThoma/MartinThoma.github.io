---
layout: post
lang: en
title: Get PDF pages
slug: get-pdf-pages
author: Martin Thoma
date: 2016-02-29 09:51
category: Cyberculture
tags: PDF
featured_image: logos/pdf.png
---
Once in a while, I want to get the total number of PDF pages of a document.
You can do that with the command

```bash
$ pdfinfo document.pdf | grep Pages | awk -F':' '{gsub(/ /, "", $0);print $2}'
```

It works like this:

1. Call `pdfinfo` to get a lot of information, including a line which begins
   with the string "Pages".
2. Get only the line with the string "Pages"
3. Split that line at ":", remove all white space and print only that after the
   first ":" (and before a second ":")

Now we know how to get the number of pages of a PDF document for a single
document. But what if you want to get it for all documents within a folder?

```bash
$ for i in *.pdf; do pdfinfo $i | grep Pages | awk -F':' '{gsub(/ /, "", $0);print $2}'; done | paste -sd+ - | bc
```

It works like this:

1. `for i in *.pdf; do ...; done` goes through all files ending with `.pdf` and
   prints the number of pages of the single documents.
2. `paste -sd+ -` makes sure that the single lines have a `+` in between
3. `bc` calculates the expression which is now a string line `18+42+9`
