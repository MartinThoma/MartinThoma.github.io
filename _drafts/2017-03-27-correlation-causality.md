---
layout: post
title: Correlation and Causality
slug: correlation-and-causality
author: Martin Thoma
status: draft
date: 2017-03-27 20:00
category: Cyberculture
tags: Correlation, Causality
featured_image: logos/ml.png
---
Correlation and Causality are two phenomens which are often confused. This
fallacy is called *cum hoc ergo propter hoc*: "with this, therefore because of
this". In the following, I will first give you an overview over causal
relationships and over correlation, then I'll show some cases how causality and
correlation are related.


## Causality

If you observe $X$ and $Y$, there are multiple ways how they could be related:

* Case 1: $X$ and $Y$ are not causal related. Neither directly nor do they have a common cause.
* Case 2: $X \Rightarrow Y$: $X$ causes $Y$.
* Case 3: $Y \Rightarrow X$: $Y$ causes $X$.
* Case 4: $A \Rightarrow X$, $A \rightarrow Y$: There is a common cause which causes $X$ and $Y$
* Case 5: $X \Rightarrow Y$, $Y \Rightarrow X$: Bidirectional causation.
* Case 6: $X \Rightarrow A \Rightarrow Y$ (and vice versa)


## Correlation

> In statistics, dependence or association is any statistical relationship, whether causal or not, between two random variables or bivariate data. Correlation is any of a broad class of statistical relationships involving dependence, though in common usage it most often refers to the extent to which two variables have a linear relationship with each other.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Correlation_and_dependence)

Most of the time, people say that two random variables $X$ and $Y$ are correlated,
when the Pearson's product-moment coefficient is not zero:

\[\mathrm{corr}(X,Y)={\mathrm{cov}(X,Y) \over \sigma_X \sigma_Y} ={E[(X-\mu_X)(Y-\mu_Y)] \over \sigma_X\sigma_Y}\]


## Relationship between Causality and Correlation

I'll go through it by the 6 cases of causality.


### Case 1

I'm not absolutely sure about it, but without causation I can't see how $X$ and
$Y$ can be correlated. Hence no causation implies no correlation(?)


### Case 2

Let $X \sim \mathcal{N}(0, 1)$ be a random variable and $Y$ be defined as

\[Y = X + 1\]

This means $Y \sim \\mathcal{N}(1, 1)$.

Hence $\mathrm{corr}(X,Y) = $

See [Does no correlation imply no causality?](http://stats.stackexchange.com/q/221936/25741)
