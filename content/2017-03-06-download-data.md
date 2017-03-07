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

Interesting download links:

* [Download ImageNet](http://image-net.org/download-images)
* [Download Places365](http://places2.csail.mit.edu/download.html)

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

