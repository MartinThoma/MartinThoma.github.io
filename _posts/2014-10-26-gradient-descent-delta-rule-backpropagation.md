---
layout: post
title: Gradient Descent, the Delta Rule and Backpropagation
author: Martin Thoma
date: 2014-10-26 21:06
category: Machine Learning
tags: Machine Learning, AI
featured_image: logos/ai.png
---

If you learn about machine learning you will stumble over three terms that are
related:

* Gradient descent,
* the Delta rule and
* backpropagation

Gradient descent is a way to find a minimum in a high-dimensional space. You
go in direction of the steepest descent.

The delta rule is an update rule for single layer perceptrons. It makes use
of gradient descent.

Backpropagation is an efficient implementation of gradient descent, where a
rule can be formulated which has some recursively defined parts. Those parts
belong to neurons of different layers and get calculated from the output-layer
(last layer) to the first hidden layer.

## See also

Wikipedia pages:

* [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
* [Delta rule](https://en.wikipedia.org/wiki/Delta_rule)
* [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)