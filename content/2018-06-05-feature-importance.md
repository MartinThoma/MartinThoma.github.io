---
layout: post
title: Feature Importance
slug: feature-importance
author: Martin Thoma
date: 2018-06-05 20:00
category: Machine Learning
tags: Machine Learning,Data Science
featured_image: logos/ml.png
---
Trust is important for a Data Scientist. If you are in a position where you can
apply a classification / regression model where the company used rules before,
you have to be able to build trust why your model is better than the old
system. Stakeholders want to understand what the model does. If you have a
rule-based system in your mind, a very natural question is:

**What is the most important feature?**

This question is problematic and having a feature importance example for trees in [sklearn](http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html) without a fat warning doesn't help. I failed to give a simple conclusive answer in
the past why this is problematic. This article fixes this issue.


## Feature Selection

Before I come to the examples, I want to introduce two simple ways of feature
selection. Feature selection is the process of selecting which features you
want to use for your models. The intention of having a small feature set is to
keep the model as simple as possible. Simpler models tend to be more robust and
easier to understand. In the simplest case, this is done manually. But there
are also two intuitive ways to do it automatically: A constructive approach and
a destructive approach.

Both are greedy algorithms.

You can find more [feature selection algorithms in sklearn](http://scikit-learn.org/stable/modules/feature_selection.html).


### Feature Construction

Let's say you have $n$ features in total and a model of type $m$ (e.g. a
Decision Tree). Then you train $n$ instances of $m$, each of them on a
different feature. You select the feature of the best model and repeat the
process. Stop once your improvement is below a threshold.


In pythonic Pseudocode:

```
def construct_features(feature_list, BaseModel, threshold, score):
    """
    Constructive feature selection algorithm

    Parameters
    ----------
    feature_list : list
    base_model : class
    threshold : float
    score : function
        Takes model as input and returns a float between 0 and infty, where
        higher is better.

    Returns
    -------
    features : list
    """
    trained_models = []
    features = []  # Set of current best features
    nb_features = 1
    condition = True
    last_score = 0
    while condition:
        for feature in feature_list:
            m = BaseModel(nb_features)
            m.train(features + [feature])
            trained_models.append((score(m), m, feature))
        features.append(sorted(trained_models)[0])

        # Check if it is time to stop
        condition = score(m) - last_score > threshold
        last_score = score(m)
    return features
```


### Feature Elimination

The same as construction, but the other way around: You start with the complete
feature set and remove one feature at a time, trying to keep the score as high
as possible.


## XOR-Example

### 2 Features

Let's start simple: We have 2 binary features and one target:

```
x1  x2    y
------------
0   0     0
0   1     1
1   0     1
1   1     0
```

Now, what is the most important feature in this case? x1 or x2?

You can easily see that having only one feature cannot be better than
random in this case!
**You need both features and a non-linear classifier to get better than random!**


### 3 Features

A similar setting as before: 3 binary features and the target is XOR of all
of them:

```
x1  x2  x3    y
---------------
0   0   0     0
0   0   1     1
0   1   0     1
0   1   1     0
1   0   0     1
1   0   1     0
1   1   0     0
1   1   1     1
```

Things to note here:

* If you take only one feature, then the target $y$ is exatly 50% of the time
  equal to that feature and exactly 50% of the time the opposite. No matter
  which feature you take.
* If you take two features, you don't get any more information as the target
  then completely depends on the last one.

From those observations, you can conclude that neither one nor two features can
be better than random at predicting the target. No matter which type of model
you take. It's plain and simple impossible. The important information is there,
but only in combination.


### n Features

The principle shown in the two examples above generalizes. If your target is
XOR of the features, then you need all features to be better than random!


### Soft-XOR

You might argue that this is an artificial example. I agree.

So let's make it less artificial. Take the features and labels from the 3-XOR
example. It is essentially a $8 \times 4$ matrix. Just add a random value in
$[-0.01, 0.01]$ to each value. The problem itself didn't change, but it looks
less artificial.

Now, you might argue that XOR-like feature behaviour is artificial. That might
be true as well, but especially business data could also simply count as
artificial.


## What are alternatives?

Now that I've explained why feature importance is misleading and needs to be
taken with big caution, what are alternatives to explain what the model does?

* **Model lab**: See [here](https://martin-thoma.com/ds-project-guide/#model-lab). Letting stakeholders poke the model.
* **lime**: [Local Interpretable Model-Agnostic Explanations](https://github.com/marcotcr/lime)
* **Common Language**: Use the same language as your stakeholders / the community to explain what your model does. Especially when it comes to the metrics you use.


## When can we use feature importance?

If the problem is linear / has a big linear part. So if a linear model gives
good results, then the feature importance makes sense. A linear model is of the
form

$$y := \sum_{i=1}^n a_i \cdot x_i$$

So each feature $x_i \in \mathbb{R}$ has a weight $a_i \in \mathbb{R}$. This
weight is the importance of the feature.


## TODOs

Explain how sklearn / [catboost](https://github.com/catboost/catboost) calculates feature importances


## TL;DR

Feature importances don't make any sense if the problem is non-linear enough.
Many problems, however, could potentially be described in a linear way.
