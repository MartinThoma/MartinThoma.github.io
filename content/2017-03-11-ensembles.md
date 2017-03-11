---
layout: post
title: Ensembles
slug: ensembles
author: Martin Thoma
date: 2017-03-11 20:00
category: Machine Learning
tags: machine learning, ensembles
featured_image: logos/ml.png
---
Models which are combinations of other models are called an **ensemble**.
The simplest way to combine several classifiers is by averaging their predictions. Hence if you have

```
model 1(x1) = [0.1, 0.5, 0.4],
model 2(x1) = [0.5, 0.3, 0.2],
model 3(x1) = [0.4, 0.4, 0.2]
```

you predict $\left [\frac{0.1+0.5+0.4}{3}, \frac{0.5+0.3+0.4}{3}, \frac{0.4+0.2+0.2}{3} \right]$ for $x_1$.

According to Karparthy, this gives you about +2 percentage points in accuracy.
I've just tried this with three (almost identical) models for cifar 100. All of
them were trained with ADAM with the same training data (the same batches).
Model 1 and model 3 only differed in the second-last layer (one uses ReLU, the
other tanh), model 1 and model 2 only differed in the border mode for one
convolutional layer (valid vs same).

The accuracies of the single models were:

```
model 1: 57.02
model 2: 61.85
model 3: 48.59
```

The ensemble accuracy is 62.98%. Hence the ensemble is 1.13 percentage points
better than the best single model!

Although I have read things like this before, it is the first time I actually
tried it myself.