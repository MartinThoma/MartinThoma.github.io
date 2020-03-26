---
layout: post
title: What are pfiles?
author: Martin Thoma
date: 2014-06-27 06:39
category: Code
tags: ASR, pfile, Machine Learning
featured_image: logos/ai.png
---

pfile is a binary file format that is used in
<abbr title="Automatic Speech Recognition">ASR</abbr>
for storing feature vectors and their corresponding labels.
This file format is sometimes also called
<abbr title="International Computer ScienceInstitute">ICSI</abbr>
feature file archive format. But this file format cannot be used for ASR only,
but also for many other <abbr title="Machine Learning">ML</abbr> tasks.

> The file consists of a fixed length ascii header followed by zero or more
variable length binary sections. Each parameter in the header has a name and a
list of zero or more value strings. The programmer's interface to pfiles (see
param.h and pfile.h) allows each parameter value to be interpreted as integer,
float, string, arrays, distributed vector, matrix, mapping tables, etc.
>
> Some special parameter names are associated with a section in the binary part
of the pfile. The value strings for these parameters give the size and offset
(from the end of the header) of the binary section.
>
> A binary section can be used as a one dimensional sequence of values, or as a
> sequence of fixed length rows in a two dimensional matrix.
>
>Some parameters are automatically added by the pfile command. For example,
> pfile_header is a parameter that contains the length and version number of
> the header.

Source: [old-site.clsp.jhu.edu/ws96/ris/man/pfile.doc](http://old-site.clsp.jhu.edu/ws96/ris/man/pfile.doc)

## pfile_utils

`pfile_utils` is a toolset to manage pfiles. It is part of the
[SPRACHcore software package](http://www1.icsi.berkeley.edu/~dpwe/projects/sprach/sprachcore.html).
The project is located at
[code.google.com/p/pfile-utilities](https://code.google.com/p/pfile-utilities)
and seems to be in version 0.51 by now. The code is written in C++.

`pfile_info` gives general information about the file:

```bash
$ pfile_info all.pfile
all.pfile
9581 sentences, 3158027 frames, 1 label(s), 42 features
```

### pfile_create

You can call pfile_create like this:

```bash
$ ./pfile_create -i - -f 1 -l 1 -o output.pfile
0 0 1 1
0 1 2 0
0 2 1 1
0 3 1 1
0 4 42 4
1 0 0 0
1 1 1337 0
1 2 2 2
2 0 3 3
```

You can end the input with <kbd>Ctrl</kbd> + <kbd>D</kbd>.

The numbers are:

```bash
[sentence-nr] [frame-nr] [feature 1] [feature 2] ... [feature n] [label 1] [label 2] ... [label n]
```

where the option `-f` defines the number of features and `-l` defines the number
of labels. Please note that within one sentence, the number of frames has to be
increasing by exactly one. One sentence can have an arbitrary number of
frames, but as soon as you make another sentence, you need to increase this
number by exactly one.

## See also

* [ICSI Speech FAQ: 3.3 What are the feature data formats?](http://www1.icsi.berkeley.edu/Speech/faq/ftrformats.html)
