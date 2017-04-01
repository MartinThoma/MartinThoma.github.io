---
layout: post
title: How to use arXiv data
slug: arxiv-data
author: Martin Thoma
date: 2017-01-06 06:30
category: Code
tags: arXiv, Amazon, AWS, Machine Learning
featured_image: logos/arxiv.png
---

<div class="info">I've written a draft for this in June 2014 and recently decided to publish it. The article is certainly not of high quality, but I want to keep it as a reminder for some of the problems I ran into and the solutions I've used.</div>

I've recently talked to my bachelors thesis advisers. *A short reminder:*
I write a thesis about the recognition of handwritten mathematical symbols. As
a practical part I implement everything on [write-math.com](http://write-math.com).

My advisers said me that I need at least 100 training examples per symbol.
As I currently have about 1070 symbols in the database, including symbols
like [`\bat`](http://www.martin-thoma.de/write-math/symbol/?id=1196) or
[`\Mundus`](http://www.martin-thoma.de/write-math/symbol/?id=1197). As they
are extremely unlikely to be used in math mode, I will simply skip them. The
more symbols I can skip, the less training symbols I need to get. So I want to
skip as many as possible. I think `\up[greek letter]` like [`\updelta`](http://www.martin-thoma.de/write-math/symbol/?id=851) and [`\Updelta`](http://www.martin-thoma.de/write-math/symbol/?id=857)
are also rare. But my adviser doesn't think so. This means I need to prove it.

One way to prove it is by looking at much data and counting. One of the biggest
datasources for LaTeX is [arXiv](http://arxiv.org/), a repository of electronic
preprints of scientific papers in the fields of mathematics, physics, astronomy,
computer science, quantitative biology, statistics, and quantitative finance,
which can be accessed online.

## Why parsing LaTeX is hard

Special cases. Lots of them.

At first you would think: Dude, it's only counting strings in documents. Is that
really worth writing an article?

Yes, it is.

Just think about the many ways you can define your own commands (called macros):

* `\newcommand{[search]}{[replace]}`
* `\newcommand{[search]} {[replace]}`
* `\def[search]{[replace]}`
* `\newcommand*{[search]}{[replace]}`
* `\newenvironment`
* ...

Then remember that you can import files

* `\input{package}`
* `\input package.sty`
* `\include`
* `\usepackage`

and weird commands like `\begin{filecontents*}`. And even more weird self-defined
ones:

* `\def\be{\begin{equation}}`
* `\def\ee{\end{equation}}`
* `\newcommand{\beq}{\begin{equation}}`
* `\newcommand{\eeq}{\end{equation}}`
* `\def\bea{\begin{eqnarray}}`
* `\def\eea{\end{eqnarray}}`
* `\newcommand\beq{\begin{equation}}`
* `\newcommand\eeq{\end{equation}}`
* `\newcommand\beqa{\begin{eqnarray}}`
* `\newcommand\eeqa{\end{eqnarray}}`
* `\def\({\left(}`
* `\def\){\right)}`
* `\def\[{\left[}`
* `\def\]{\right]}`
* `\def\<{\left\langle}`
* `\def\>{\right\rangle}`

As some of these were quite common, `sed` and `find` saved me some work:

```bash
find . -type f -print0 | xargs -0  \
sed -i 's/\\newcommand{\\beq}{\\begin{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\newcommand\\eeq{\\end{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\newcommand{\\eeq}{\\end{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\newcommand{\\be}{\\begin{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\newcommand{\\ee}{\\end{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\def\\ee{\\end{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\def\\be{\\begin{equation}}/%%%%%%%%%%%%%%/g'

find . -type f -print0 | xargs -0  \
sed -i 's/\\def\\ee{\\end{equation}}/%%%%%%%%%%%%%%/g'
```

## What I currently don't check

Commands with parameters:

```latex
\makeatletter
\def\imod#1{\allowbreak\mkern10mu({\operator@font mod}\,\,#1)}
\makeatother
```

## Structure of arXiv

arXiv uses Amazon S3 with the "requester pays" option. The storage containers
of S3 are called "buckets" and they are adressed in an URI style:

```bash
s3://arxiv/pdf/arXiv_pdf_manifest.xml
```

A tool to get data from S3 under Linux is `s3cmd`. It can be used like this:

```bash
$ s3cmd ls --add-header="x-amz-request-payer: requester" s3://arxiv/pdf/arXiv_pdf_manifest.xml
2011-02-15 04:12    246144   s3://arxiv/pdf/arXiv_pdf_manifest.xml

$ s3cmd get --add-header="x-amz-request-payer: requester" s3://arxiv/pdf/arXiv_pdf_manifest.xml
s3://arxiv/pdf/arXiv_pdf_manifest.xml -> ./arXiv_pdf_manifest.xml  [1 of 1]
 246144 of 246144   100% in    0s   377.85 kB/s  done

$ s3cmd ls --add-header="x-amz-request-payer: requester" s3://arxiv/pdf/\*
```

The manifest contains all information about the real data. Remember, you have
to pay for the downloads! According to arXiv, it's about &#36;0.12/GB transferred.
This means for 150 GB I would have to pay at least &#36;18.

The manifest is an XML file, which looks like this:

```xml
<?xml version='1.0' standalone='yes'?>
<arXivSRC>
  <file>
    <content_md5sum>cacbfede21d5dfef26f367ec99384546</content_md5sum>
    <filename>src/arXiv_src_0001_001.tar</filename>
    <first_item>astro-ph0001001</first_item>
    <last_item>quant-ph0001119</last_item>
    <md5sum>949ae880fbaf4649a485a8d9e07f370b</md5sum>
    <num_items>2364</num_items>
    <seq_num>1</seq_num>
    <size>225605507</size>
    <timestamp>2010-12-23 00:13:59</timestamp>
    <yymm>0001</yymm>
  </file>
  <file>
    <content_md5sum>d90df481661ccdd7e8be883796539743</content_md5sum>
    <filename>src/arXiv_src_0002_001.tar</filename>
    <first_item>astro-ph0002001</first_item>
    <last_item>quant-ph0002094</last_item>
    <md5sum>4592ab506cf775afecf4ad560d982a00</md5sum>
    <num_items>2365</num_items>
    <seq_num>1</seq_num>
    <size>227036528</size>
    <timestamp>2010-12-23 00:18:09</timestamp>
    <yymm>0002</yymm>
  </file>
  <file>
    <content_md5sum>3388afd7bfb2dfd9d3f3e6b353357b33</content_md5sum>
    <filename>src/arXiv_src_0003_001.tar</filename>
    <first_item>astro-ph0003001</first_item>
    <last_item>quant-ph0003151</last_item>
    <md5sum>b5bf5e52ae8532cdf82b606b42df16ea</md5sum>
    <num_items>2600</num_items>
    <seq_num>1</seq_num>
    <size>230986882</size>
    <timestamp>2010-12-23 00:22:15</timestamp>
    <yymm>0003</yymm>
  </file>
  ...
```

The differrent files mean:

* `content_md5sum`: MD5 sum of all the files in the tar package concatenated but not packaged. Use md5sum for the md5sum of the tar package which should match the S3 MD5 sum.
* `filename`:
Name of file within bucket, prefix bucket name s3://arxiv/ for complete identifier
* `first_item` and `last_item`:
arXiv identifier of article PDF first in tar package, and last in tar package
* `md5sum`:
MD5 sum of tar package, can be used as check against downloaded file
* `num_items`:
Number of PDF files in tar package
* `seq_num`:
Sequence number within month yymm
* `size`:
Size of tar package in bytes
* `timestamp`:
Timestamp of tar package (unix mtime when created, expressed at YYYY-MM-DD HH:MM::SS)
* `yymm`: Two digit year and month of items in the tar package. Starts with 9108 for 1991-08, rolls past y2k to 0001 for 2000-01, 1008 for 2010-08 etc.