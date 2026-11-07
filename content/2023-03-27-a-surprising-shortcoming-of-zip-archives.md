---
layout: post
title: A surprising shortcoming of ZIP archives
slug: a-surprising-shortcoming-of-zip-archives
lang: en
author: Martin Thoma
date: 2023-03-27 18:01
category: Code
tags: File
summary: ZIP archives do not de-duplicate identical files, 7z does
medium_url: https://medium.com/@martinthoma/a-surprising-shortcoming-of-zip-archives-335a94a1a2cb
status: draft
---
I recently had to send a ZIP archive with duplicate files to another web service. I thought that the duplicates would not matter for the overall file size, because ZIP archives can use compression algorithms. And what would be easier to compress than plain duplicates?

## ZIP does not de-duplicate

It turns out, ZIP cannot de-duplicate files:

```shell
$ cp a.pdf b.pdf
$ zip -9 one.zip a.pdf
$ zip -9 two.zip a.pdf b.pdf
$ ls -sd --block-size=1 * | grep zip
 958464 one.zip
1912832 two.zip
```

The created zip file is almost double the size.

## 7z can de-duplicate

```shell
$ 7z a one.7z a.pdf
$ 7z a two.7z a.pdf b.pdf
$ ls -sd --block-size=1 * | grep 7z
 958464 one.7z
 958464 two.7z
```

It’s a little bit suspicious that the two files have exactly the same size. I would have expected at least a tiny difference for the file name that needs to be stored. The reason is that `ls -s` shows the allocated disk space in blocks, not the exact file size.

## Other archive formats

* BZIP2: Cannot deduplicate
* RAR: Cannot deduplicate

## How can you detect duplicates efficiently?

1. Create a hash of all files
1. Create a dictionary (aka map, HashMap, or associative array) of all files you have. It maps a file hash to a list of pointers of files that have this hash value.

You will need to check if the files with the same hash are duplicates, but that is likely the case.
