---
layout: post
title: Machine Learning Course - Notation
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Machine Learning
featured_image: logos/machine-learning.png
---

The following notation is used by Andrew Ng in the coursera Machine Learning
course.

## Neural Networks

* $L$: number of layers in a neural net
* $s_i$: number of nodes in layer $i$
* (x^{(i)}, y^{(i)}): $i$th training example with input vector $x$ and output
  vector $y$
* $h_\Theta(x)$: hypothesis with parameters $\Theta$ and input $x$
* $h_\Theta(x)_i$: $i$th element of the hypothesis $h_\Theta(x)$
* $\Theta_{To node nr, from node nr}^{(Layer of the source node)}$: Weight
* $\lambda$: Regularization parameter