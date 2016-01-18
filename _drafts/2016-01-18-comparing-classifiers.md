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
Classification problems occur quite often and many different classification
algorithms have been described and implemented. But what is the best algorithm
for a given error function and dataset?

I read questions like "I have problem X. What is the best classifier?" quite
often and my first impulse is always to write: Just try them!

I guess people asking this question might think that it is super difficult to
do so. However, the sklearn tutorial contains a very nice example where
many classifiers are compared ([source](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)).

This article gives you an overview over some classifiers:

* [SVM](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [k-nearest neighbors](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
* [Random Forest](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
* [AdaBoost Classifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)
* [Naive Bayes](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)
* [LDA](http://scikit-learn.org/0.16/modules/generated/sklearn.lda.LDA.html)
* [QDA](http://scikit-learn.org/0.16/modules/generated/sklearn.qda.QDA.html)


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

MNIST is a dataset of \(28\text{px} \times 28\text{px}\) greyscale images.
Each of the images contains a digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). The
task is to classify the image into one of the 10 digit classes.

Guessing randomly will give an accuracy of \(\frac{1}{10} = 0.1\).


### Adjusted SVM

```
Fit time: 289.1019s
Confusion matrix:
[[2258    1    4    1    2    2    3    1    4    2]
 [   1 2566    9    1    1    0    0    7    3    0]
 [   4    1 2280    5    4    0    1    9    8    2]
 [   0    0   14 2304    1   13    0    6    8    2]
 [   2    2    2    0 2183    0    7    5    0   10]
 [   4    0    0   16    3 2026   12    1    4    3]
 [   7    5    3    0    5    2 2245    0    4    0]
 [   1    6   11    2    5    1    0 2373    5   13]
 [   3    9    4    9    4   10    2    3 2166    5]
 [   3    2    2    6   19    6    0   12   10 2329]]
Accuracy: 0.9840
```


### Linear SVM

```
Classifier: linear SVM
Fit time: 140.6126
Confusion matrix:
[[2226    0    9    2    6   12    8    3   11    1]
 [   1 2537   18    3    3    1    1    7   17    0]
 [  12   16 2158   25   24    6   27   19   25    2]
 [   3    7   46 2188    4   47    3   18   27    5]
 [   2    5   19    1 2117    1    8    6    3   49]
 [  18   13   11   73   20 1872   31    0   26    5]
 [  20    6   22    1   10   30 2179    0    3    0]
 [   5   10   32   11   30    5    0 2268    5   51]
 [  11   39   26   47   10   40    7    7 2018   10]
 [  11    9    9   24   64    8    0   61   14 2189]]
Accuracy: 0.9416
```

