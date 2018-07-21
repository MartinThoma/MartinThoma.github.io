---
layout: post
title: Regression
slug: regression
author: Martin Thoma
date: 2018-07-18 20:00
category: Machine Learning
tags: Machine Learning, Regression
featured_image: logos/ml.png
---
<div class="info">A while ago, this link pointed to the content which is now in the <a href="https://martin-thoma.com/forecasting/">Forecasting article</a>.</div>

Regression is one of the core tasks in machine learning. In this task, you get
some input and your target variable is a single floating point number. For
example, predicting the price of a house, estimating the <a href="http://www.u.arizona.edu/~kuchi/Courses/MAT167/Files/LH_LEC.0710.Models.Regression.pdf">age of the universe</a> or calculating the probability that an image shows a dog. The age of the universe
example shows that it regression is not only used in machine learning and the
dog image example shows that regression and classification can be very similar.
A <a href="https://en.wikipedia.org/wiki/Logistic_regression">logistic regression</a>
can be converted to a classifier by choosing a threshold value (e.g. 0.5).

A big difference between regression and classification are scoring functions
and targets. The targets in classification are just a few finite ones, while
you have infinite possible targets for regression. Below, you can see a list
of scoring functions.


## Scoring functions

In the following, $y$ is the ordered list of target, $y^P$ is the list
of predictions in the same order and $\bar{y}$ is the mean of $y$.

<table class="table">
    <thead>
    <tr>
        <th>Name</th>
        <th>Image</th>
        <th>X is better</th>
        <th>Definition and Usage</th>
    </tr>
</thead>
    <tbody>
    <tr>
        <td>MAE</td>
        <td>$[0, \infty)$</td>
        <td>lower</td>
        <td>$f(y, y^P) = \frac{1}{|y|} \sum_{y_i, y_i^P \in (y, y^P)} |y_i - y_i^P|$</td>
    </tr>
    <tr>
        <td>MSE</td>
        <td>$[0, \infty)$</td>
        <td>lower</td>
        <td>$f(y, y^P) = \frac{1}{|y|} \sum_{y_i, y_i^P \in (y, y^P)} (y_i - y_i^P)^2$</td>
    </tr>
    <tr>
        <td>$R^2$</td>
        <td>$[0, 1]$</td>
        <td>higher</td>
        <td>$f(y, y^P) = 1 - \frac{\sum (y_i - y_i^P)^2}{\sum (y_i - \bar{y})^2}$</td>
    </tr>
    <tr>
        <td>Explained Variance</td>
        <td>$(-\infty, 1]$</td>
        <td>higher</td>
        <td>$f(y, y^P) = 1 - \frac{Var(y - y^P)}{Var(y)}$</td>
    </tr>
</tbody>
</table>

See also:

* [What is the difference between “coefficient of determination” and “mean squared error”?](https://stats.stackexchange.com/q/32596/25741)


## Regression Models

### Trivial Models

There are some straight-forward "models" for regression. They do learn, but
they ignore the input completely:

* [Arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean): $\frac{1}{n}\sum_{i=1}^n {y_i}$
* [Median](https://en.wikipedia.org/wiki/Median): Sort all $y_i$ and take the value in the middle
* minimum and maximum
* q-Quantile: Sort the $y_i$ and take the first value after going through $q \in [0, 1]$ of the input. For $q = 0.5$, this
  is the median.
* Other "means" like the geometric mean


### Linear regression

<a href="https://en.wikipedia.org/wiki/Linear_regression">Linear regression</a>
tries to fit a line to the input by minimizing the squared quadradic distance
between the input points and the line. This usually gives pretty good results.

The model looks like this:

$$\hat{y}(x) = \sum_{i=1}^n b_i \cdot x_i \text{ with }b_i \in \mathbb{R}$$

If one defines $X \in \mathbb{R}^n$ one can also write it in a vectorized form:

$$\hat{y}(X) = X \cdot \beta \text{ with }\beta \in \mathbb{R}^n$$

It can be "learned" (calculated) with

$$\beta = {(X^T X)}^{-1} X^T y$$


### Logistic regression

<a href="https://en.wikipedia.org/wiki/Logistic_regression">Logistic regression</a>
tries to fit the logistic function $y(x) = \frac{1}{1+e^{-x}}$ to the input.
This function is nice as it is within $[0, 1]$ and thus can be used to
represent a probability.


### Trees

You can also use trees for regression. One idea how to do that is by
"bucketing" observations and applying one of the trivial models to each bucket.
Such models can only predict values between what they observed before.

See also:

* [sklearn](http://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)
