---
layout: post
title: Get PDF pages
slug: get-pdf-pages
lang: en
author: Martin Thoma
date: 2016-02-29 09:51
category: Cyberculture
tags: PDF, Command Line, Linux
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
3. `bc` calculates the expression which is now a string like `18+42+9`

## Update 2026: pdfly

Nowadays I use [pdfly](https://github.com/py-pdf/pdfly), a command line tool
written in pure Python on top of [pypdf](https://github.com/py-pdf/pypdf). You
can install it with `pip install pdfly`. Its `meta` command shows the number
of pages together with other metadata:

```text
$ pdfly meta document.pdf
                     Operating System Data
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Attribute ┃ Value                                   ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         File Name │ /home/moose/Documents/Mega/document.pdf │
│  File Permissions │ -rw-rw-r--                              │
│         File Size │ 427,286 bytes                           │
│     Creation Time │ 2026-09-13 21:54:16                     │
│ Modification Time │ 2026-09-13 21:53:42                     │
│       Access Time │ 2026-09-26 08:15:15                     │
└───────────────────┴─────────────────────────────────────────┘
                                    PDF Data
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Attribute ┃ Value                                                   ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│            Creator │ Simple Scan 46.0                                        │
│              Pages │ 1                                                       │
│          Encrypted │ None                                                    │
│   PDF File Version │ %PDF-1.3                                                │
│        Page Layout │                                                         │
│          Page Mode │                                                         │
│             PDF ID │ ID1=b'm\xc2\xbf\xe2\x80\xba_>|I\xe2\x80\x9a.\xc3\xbe\x… │
│                    │ ID2=b'm\xc2\xbf\xe2\x80\xba_>|I\xe2\x80\x9a.\xc3\xbe\x… │
│ Fonts (unembedded) │                                                         │
│   Fonts (embedded) │                                                         │
│        Attachments │ []                                                      │
│             Images │ 1 images (425,148 bytes)                                │
└────────────────────┴─────────────────────────────────────────────────────────┘
```

For scripts, pdfly can print the metadata as JSON, so `jq` can pick the page
count:

```bash
$ pdfly meta --output json document.pdf | jq .pages
1
```

The page count of all documents within a folder:

```bash
$ for i in *.pdf; do pdfly meta --output json "$i"; done | jq -s 'map(.pages) | add'
```

It works like this:

1. The loop prints one JSON object per document.
2. `jq -s` (slurp) reads all of them into one array.
3. `map(.pages)` takes the page count of each document and `add` sums them up.
