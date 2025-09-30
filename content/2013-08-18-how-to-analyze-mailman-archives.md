---
layout: post
lang: en
title: How to analyze Mailman archives
slug: how-to-analyze-mailman-archives
author: Martin Thoma
date: 2013-08-18 21:23:49.000000000 +02:00
category: Cyberculture
tags: Bash, Mailman, discussion, email
featured_image: 2011/09/Gnome-Terminal.png
---
All mailing lists I use are <a
href="http://en.wikipedia.org/wiki/GNU_Mailman">GNU Mailman</a> lists. This
software provides archives of all Emails that were send over the list.

They look like this:

<figure class="aligncenter">
            <a href="../images/2013/08/mailman-list-archive-300x277.png"><img src="../images/2013/08/mailman-list-archive-300x277.png" alt="GNU Mailman list archive" style="max-width:300px;max-height:277px" class="size-medium wp-image-76298"/></a>
            <figcaption class="text-center">GNU Mailman list archive</figcaption>
        </figure>

Once in a while, I would like to search if a topic was already discussed. Here is how you can do it:

## Download archives

```bash
wget --save-cookies cookie.txt --post-data 'username=user&password=pass' -A gz -m -p -E -k -K -np https://lists.abc.org/mailman/blub/
```

## Rename archives

```bash
for file in *.txt.gz; do mv "$file" "${file%.txt.gz}.txt"; done
```

To make them sortable:

```bash
for file in *January.txt; do mv "$file" "${file%January.txt}01.txt"; done
for file in *February.txt; do mv "$file" "${file%February.txt}02.txt"; done
for file in *March.txt; do mv "$file" "${file%March.txt}03.txt"; done
for file in *April.txt; do mv "$file" "${file%January.txt}04.txt"; done
for file in *May.txt; do mv "$file" "${file%May.txt}05.txt"; done
for file in *June.txt; do mv "$file" "${file%June.txt}06.txt"; done
for file in *July.txt; do mv "$file" "${file%July.txt}07.txt"; done
for file in *August.txt; do mv "$file" "${file%August.txt}08.txt"; done
for file in *September.txt; do mv "$file" "${file%September.txt}09.txt"; done
for file in *October.txt; do mv "$file" "${file%October.txt}10.txt"; done
for file in *November.txt; do mv "$file" "${file%November.txt}11.txt"; done
for file in *December.txt; do mv "$file" "${file%December.txt}12.txt"; done
```

## Analyze them

To analyze the archives properly, you should perhaps first import all emails in
a relational database. But with <code>grep</code> you could also do simple
keyword searches.
