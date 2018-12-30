---
layout: post
title: Techniques for Analyzing ML models
slug: model-analysis
author: Martin Thoma
date: 2018-12-30 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/ml.png
---
<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>

Techniques for model analysis:

* Decision boundaries
* [ELI 5](https://eli5.readthedocs.io/en/latest/overview.html)
* LIME
* [Feature importance](https://martin-thoma.com/feature-importance/)
* Confusion matrix
* [SHAP values](https://www.kaggle.com/dansbecker/shap-values)
* [Partial Dependence Plots](https://www.kaggle.com/dansbecker/partial-plots)
* Sensitivity analysis / perturbation importance
* Dimensionality reduction
* Attention mapping / saliency mapping
* Model parameter analysis
* Feature correlations

If you're interested in analysis of CNNs, have a look at my masters thesis:

> [Analysis and Optimization of Convolutional Neural Network Architectures](https://arxiv.org/pdf/1707.09725.pdf)


## Decision boundaries

Drawing this is only an option if you have 3 or less features. So not really
useful in most problem settings.


## SHAP values

SHAP Values (an acronym from SHapley Additive exPlanations) go in the direction
of feature importance.

Let me explain them with an example of the Titanic dataset: You have a survival
probability of a given person, e.g. 76%. You want to understand why it is 76%.

So what you can do is to twiddle the features. How does the survival
probability change when the person has less / more siblings? When the person
has the median number of siblings?

There is the [`shap` package](https://github.com/slundberg/shap) for
calculating the shap values.
