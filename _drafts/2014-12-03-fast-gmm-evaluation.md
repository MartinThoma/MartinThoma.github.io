---
layout: post
title: Fast Evaluation of GMMs
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- GMM
- Naive Bayes classifier
featured_image: logos/ai.png
---

Gaussian Mixture Models (GMMs) can be used for classification tasks in
naive bayes classifiers.

A GMM is a probability distribution function which consists of multiple
gaussian distributions. A single
<abbr title="multiple random variables which can be combined in a vector">multivariate</abbr>
Gaussian distribution $f$ is defined as

$$f_i(x) = \frac{1}{\sqrt{(2 \pi)^d |\Sigma_i|}} \cdot e^{- \frac{1}{2} (x - \mu_i)^T \Sigma_i^{-1} (x - \mu_i)}$$

where $x \in \mathbb{R}^d$ is the feature vector,
$\mu_i \in \mathbb{R}^d$ is the mean and
$\Sigma_i \in \mathbb{R}^{d \times d}$ is the covariance matrix. $|\Sigma_i|$
is the determinant and $\Sigma_i^{-1}$ is the inverse matrix.

Multiple gaussians can be combined by coefficients $c_i \in \mathbb{R}$ with
$i = 1, ..., n$ with $\sum_{i=1}^n c_i = 1$:

$$g(x) = \sum_{i=1}^n c_i f_i(x)$$

Now you see that calculating each GMM involves $n$ calculations of the
$e$ function.

In speech recognition this is done very often, so you want to calculate it
fast. To do so, the kNN algorithm can be combined with


## Exp-function

As I heard that the $e$ function is computationally expensive, I was curious
if this is (still) true. I searched for the implementation of
[`math.exp(x)`](https://docs.python.org/2/library/math.html#math.exp) in Python
to figure this out. According to
[Martijn Pieters](http://stackoverflow.com/a/15322395/562769), the function
is defined in [`mathmodule.c`](https://hg.python.org/cpython/file/tip/Modules/mathmodule.c).
According to him, "the C function implementation itself is entirely platform dependent, and on modern hardware is usually taken care of in hardware".

Well, that is interesting. Lets see if I can find information by CPU
producers:
