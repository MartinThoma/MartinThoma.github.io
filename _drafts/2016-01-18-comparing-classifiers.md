---
layout: post
title: Comparing Classifiers
author: Martin Thoma
date: 2014-11-22 17:19
category: Cyberculture
tags:
- Python
- Machine Learning
- Classification
featured_image: logos/ml.png
---
The sklearn tutorial contains a very nice example where classifiers are
compared ([source](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html))


## Tutorial example

The sklearn tutorial creates three datasets with 100&nbps;points per dataset and
2&nbsp;dimensions per point:

1. **Moons**: Two interleaving half-circles
2. **Circles**: A larger circle containing the smaller one
3. **Linear**: A linearly seperable dataset

Each of those three datasets has added noise. This means for some points there
might be no way of classifying them correclty.

Here are the results

{% caption align="aligncenter" width="500" alt="k nearest neighbors, linear and RBFSVM" text="k nearest neighbors, linear and RBFSVM" url="../images/2016/01/ml-classifiers-1.png" %}

One can see that k nearest neighbors gives arbitrary decision boundaries.
Overall, they look reasonable. However, there are often strange zig-zag
patterns.

The linear SVM in contrast has a very easy decision boundary: a line. It is no
suprise that it can't deal with the moons dataset. Note that a random guess
would be right in 50% of the cases.

The RBF SVM has very nice decision boundary. It is smooth, matches the pattern
and is able to adjust to all three examles.

{% caption align="aligncenter" width="500" alt="Decision Tree, Random Forest, AdaBoost" text="Decision Tree, Random Forest, AdaBoost" url="../images/2016/01/ml-classifiers-2.png" %}

Decision Trees, Decision Forests and AdaBoost all show very similar
patterns. The boundaries change in parallel to the coordinate axes which looks
very unnatural.


{% caption align="aligncenter" width="500" alt="Naive Bayes, LDA, QDA" text="Naive Bayes, LDA, QDA" url="../images/2016/01/image.png" %}

Naive Bayes shows nice, smooth patterns. However, those patterns seem to be
a bit too simple. LDA is again linear (see linear SVM). Comparing QDA to
Naive Bayes is interesting. Although they get similar performance for the first
dataset, I would argue that the naive bayes classifier is much better as it is
much more confident for its classification. Even more extrem is the last example.
I'm astonished that the QDA gets 93% with that boundary; Naive Bayes seems to
find a much better boundary.

## MNIST

