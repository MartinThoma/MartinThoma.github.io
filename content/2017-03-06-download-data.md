---
layout: post
title: How to download ImageNet
slug: download-data
author: Martin Thoma
date: 2017-03-06 20:00
category: Machine Learning
tags: download, machine learning
featured_image: logos/ml.png
---

Machine Learning algorithms for computer vision need huge amounts of data.
Here are a few remarks on how to download them.

1. Make sure you have enough space (`df -h`)
2. Get a download manager. I use aria2c (`sudo apt-get install aria2`)

For ImageNet, you have to register at [image-net.org](http://image-net.org/).

Download the files like this:

```
$ aria2c -s 16 [URL]
```

After downloading the file, use

```
$ md5sum [Filename]
```

and compare the hash with the provided hash. If it differs, download the file
again.

The ImageNet training data tar file contains 1000&nbsp;files of the form
`n01440764.tar`, `n01443537.tar`, ...

Each of those files contains JPEGs of one class. You can look the class label
up with

```
from nltk.corpus import wordnet as wn
print(wn._synset_from_pos_and_offset('n', 1440764))
print(wn._synset_from_pos_and_offset('n', 1443537))
```

which reveals

<ul>
    <li>Synset('tench.n.01')</li>
    <li>Synset('goldfish.n.01')</li>
</ul>

If you extract all 1000 of those tar files into one directory, this takes about
6 hours with a script like this:

```
#!/usr/bin/env python

import glob
import tarfile


def untar(fname, targetd_dir):
    with tarfile.open(fname) as tar:
        tar.extractall(path=targetd_dir)

files = glob.glob("ILSVRC2012_img_train/*.tar")

for f in files:
    untar(f, "extracted")
```

This gives 1281170 files in total.


## Datasets

* [Download ImageNet](http://image-net.org/download-images)
* [Download Places365](http://places2.csail.mit.edu/download.html)