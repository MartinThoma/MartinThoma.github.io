---
layout: post
title: On-line Handwriting Recognition of Mathematical Symbols
author: Martin Thoma
date: 2014-10-17 12:25
category: Code
tags: Python, Project Management
featured_image: logos/write-math.png
---

On-line handwriting recognition systems get the information how a symbol is
written. In contrast, OCR only gets the pixel map.

I've created a system that can be used to work with handwriting recognition
systems in my bachelor's thesis.

## write-math.com

The website [write-math.com](http://write-math.com) was used to collect data.
The source is at [github.com/MartinThoma/write-math](https://github.com/MartinThoma/write-math).

## hwrt toolkit

The [`hwrt`](https://github.com/MartinThoma/hwrt) toolkit was created to
work with on-line handwritten symbols. The toolkit is documented at
[pythonhosted.org/hwrt](https://pythonhosted.org/hwrt/).

The raw data can be downloaded with this toolkit.

The toolkit can be used to classify data on your computer (without internet
connection):

<figure class="aligncenter">
            <a href="../images/2015/01/write-math-browser-ui.png"><img src="../images/2015/01/write-math-browser-ui.png" alt="Write math: Interactive Browser Interface (offline)" style="max-width:500px;" class=""/></a>
            <figcaption class="text-center">Write math: Interactive Browser Interface (offline)</figcaption>
        </figure>

## nntoolkit

The [`nntoolkit`](https://github.com/MartinThoma/nntoolkit) was created to
have a free software to create, train, test and evaluate neural networks.


## HWR experiments

All experiments configuration files are saved in the project
[github.com/MartinThoma/hwr-experiments](https://github.com/MartinThoma/hwr-experiments).


## Data

The data can be downloaded from <a href="http://write-math.com/data">write-math.com/data</a>.
I will try to keep a relatively recent version online. You can contact me if
you want the latest version. However, I should note that currently (2015-04-12)
this is about 3.7GB. This means sharing the data is not that easy.


## Presentations

* [27.08.2014](https://github.com/MartinThoma/LaTeX-examples/blob/master/presentations/Bachelor-Short/LaTeX/bachelor-short.pdf?raw=true)
* [06.11.2014](https://github.com/MartinThoma/LaTeX-examples/blob/master/presentations/Bachelor-Final-Presentation/LaTeX/Bachelor-Final-Presentation.pdf?raw=true):
  Final presentation for bachelor's thesis

## Bachelor's thesis

* [07.11.2014](http://arxiv.org/abs/1511.09030):
  My bachelor's thesis. I've got the best grade (1.0) for it ☺. Please note
  that the submission to arxiv was later and a couple of typos were fixed as
  well as the term "data multiplication" was replaced by "data augmentation".
* [29.06.2015](http://digbib.ubka.uni-karlsruhe.de/volltexte/1000048047): An
  updated, condensed version of my bachelor's thesis.

### Remarks

* What I called "data multiplication" is called "data augmentation" by others
  (e.g. [ImageNet Classification with Deep Convolutional Neural Networks](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf), [Deep Image: Scaling up Image Recognition](http://arxiv.org/abs/1501.02876), [Classifying plankton with deep neural networks](http://benanne.github.io/2015/03/17/plankton.html#data-augmentation))