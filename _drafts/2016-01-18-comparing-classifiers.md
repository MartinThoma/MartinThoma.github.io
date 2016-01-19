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

### Neural Networks

#### Simple Network

```
Classifier: NN 500:200
Training time: 79.5696s
Predict time: 0.3480s
Confusion matrix:
[[2248    1    5    1    2    4    8    2    5    2]
 [   1 2565   10    1    1    0    2    7    1    0]
 [   7    2 2258   14    5    0    9    6   10    3]
 [   0    0   12 2294    0   23    0    6    3   10]
 [   0    3    3    0 2161    0    8    5    1   30]
 [   4    1    1   16    1 2014   17    1    5    9]
 [  11    7    1    0    5    6 2237    0    4    0]
 [   3    6   14    7    3    1    0 2355   10   18]
 [   3    7    3   14    2   17    4    1 2161    3]
 [   4    4    0    4   16    8    0    7    6 2340]]
Accuracy: 0.9798
```


#### Dropout Network

```
Classifier: NN 500:200 dropout
Training time: 118.2654s
Predict time: 0.3918s
Confusion matrix:
[[2250    1    7    1    1    1    5    4    4    4]
 [   1 2567    9    1    1    0    0    3    5    1]
 [   6    6 2272    3    2    1    3   10    8    3]
 [   0    0   26 2260    0   24    0   10   19    9]
 [   0    3    5    0 2152    0    7    3    1   40]
 [   8    3    3   12    2 1983   20    6   21   11]
 [  11    6    3    0    7    1 2237    0    6    0]
 [   2    7   13    3   11    0    1 2363    5   12]
 [   7    7    9    5    3    3    1    2 2170    8]
 [   3    3    1    3   13    2    0   19    8 2337]]
Accuracy: 0.9780
```


#### CNN

```
Classifier: CNN
Training time: 391.8810s
Predict time: 1.2035s
Confusion matrix:
[[2243    0    5    0    0    5    9    1   12    3]
 [   1 2548   20    4    2    0    1    6    6    0]
 [   3    8 2253    9    3    1    4   17   14    2]
 [   0    4   13 2290    0   12    0    9   11    9]
 [   2    4    5    0 2164    0    8    5    3   20]
 [   6    2    3   15    0 2016    9    3    9    6]
 [  12   12    1    1    6    6 2227    0    6    0]
 [   3    4   11    3    4    1    0 2374    4   13]
 [   3   15    6   13    4   11    3    8 2145    7]
 [   6    5    0   11   16    8    0   24   13 2306]]
Accuracy: 0.9769
```


### Adjusted SVM

```
Training time: 289.1019s
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
Training time: 140.6126
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


### Random Forest

Data:

* `n_estimators=50`
* `n_jobs=10`

```
Start fitting 'Random Forest' classifier. This may take a while.
Classifier: Random Forest
Training time: 2.0144s
Predict time: 0.1586s
Confusion matrix:
[[2242    0    3    1    5    7    6    2   12    0]
 [   0 2548   14    4    3    1    5    7    5    1]
 [  13    4 2231   16    9    1    8   14   15    3]
 [   2    2   41 2229    3   27    4   13   18    9]
 [   4    0    3    0 2140    3   14    2    5   40]
 [   7    3    4   24    3 1990   16    3    9   10]
 [  13   11    1    0   11   16 2215    0    4    0]
 [   5    6   25    2   16    0    0 2322    8   33]
 [   2   13   10   26   12   20    5    3 2110   14]
 [   9    6    5   22   23   12    1   16   19 2276]]
Accuracy: 0.9655
```

Alternatively:

* `max_depth=5`
* `n_estimators=10`
* `max_features=1`

```
Start fitting 'Random Forest 2' classifier. This may take a while.
Classifier: Random Forest 2
Training time: 0.1462s
Predict time: 0.0535s
Confusion matrix:
[[1930   50   73   66   14   24   51   28   33    9]
 [   2 2468   15   53    1    1   34   10    4    0]
 [  91  268 1518  163   25   13  112   45   70    9]
 [  84  194  144 1675    3   29   28   58  115   18]
 [  40  232   89   47  879    3   55  406   95  365]
 [ 444  302   70  329   22  364   78  169  241   50]
 [  99  415  119   58   39   18 1514    4    5    0]
 [  36  226   28   42   53    0    9 1705   45  273]
 [ 159  382   69  333   29   45   77   64  967   90]
 [  44  184   25   20  214    1    2  612  195 1092]]
Accuracy: 0.6109
```


### k nearest neightbors

```
Start fitting 'k nn' classifier. This may take a while.
Classifier: k nn
Training time: 3.8013s
Predict time: 1033.7148s
Confusion matrix:
[[2260    1    4    0    0    1    6    2    2    2]
 [   0 2572    5    0    0    0    1    8    1    1]
 [  16   15 2235    9    1    0    5   26    5    2]
 [   2    5   14 2276    0   27    1    8    9    6]
 [   4   19    0    0 2131    0    8    4    0   45]
 [  10    5    3   28    5 1977   25    2    4   10]
 [  12    9    0    0    4    7 2239    0    0    0]
 [   1   18    4    1   12    0    0 2349    3   29]
 [  11   32    8   36   11   34    5    7 2053   18]
 [   6    8    4   14   26    4    0   19    5 2303]]
Accuracy: 0.9695
```


### Decision Tree

Data:

* `max_depth=5`

```
Training time: 2.6527s
Predict time: 0.0247s
Confusion matrix:
[[1767    0   11   25   12  120  137   71  114   21]
 [   1 2065  128  108   13   17   41   66  131   18]
 [  42   44 1248   37  121   21  227   76  339  159]
 [  33   22   32 1484   33  107   52   81  266  238]
 [   0   15   45   33 1284   42   42   45  213  492]
 [  42   10   21  229  166  577  137  123  254  510]
 [  34   33   66   24  103   65 1734   24  102   86]
 [  10   14  179   57   53   21   19 1775   79  210]
 [   1   98  129   43   43   42  160   29 1439  231]
 [   4    8   86   59  125   95   36   75  167 1734]]
Accuracy: 0.6540
```


### Adaboost

```
Training time: 32.4964s
Predict time: 0.7506s
Confusion matrix:
[[1994    0   75    8    6  113   51    3   15   13]
 [   0 2435   27   22    2   10   12   37   42    1]
 [  97   39 1341   85   39   38  416   39  196   24]
 [ 108   52   37 1508   13  313   66   64  122   65]
 [  11   16   48   23 1662   49   23  134   90  155]
 [  81   56   30  309   51 1255   57   17  129   84]
 [  29   28  151    7   80   43 1914    2   17    0]
 [  25   37   33   36   70   30    0 1761   37  388]
 [  30   80   48  215   16   85   30   19 1615   77]
 [  13   29   68   66  356   74    1  171   78 1533]]
Accuracy: 0.7367
```


### Naive Bayes

```
Training time: 0.3334s
Predict time: 0.9994s
Confusion matrix:
[[2094    4   11   10    6    7   56    3   69   18]
 [   4 2432    9   11    2    4   28    1   77   20]
 [ 278   64  703  143    6    4  558    4  528   26]
 [ 202  136   18  791    5    5  106   21  886  178]
 [  96   26   16   14  296    8  169   13  535 1038]
 [ 327   63   15   39   14   87  100    5 1253  166]
 [  34   51   17    1    1    5 2109    0   52    1]
 [  19   21    3   23   20    2    7  737  123 1462]
 [  39  326   13   16    8   18   25    7 1482  281]
 [  15   26    8    2   14    2    1   41   40 2240]]
Accuracy: 0.5615
```


### LDA

```
Training time: 17.2674s
Predict time: 0.0554s
Confusion matrix:
[[2131    2   10   14   12   47   20    4   36    2]
 [   0 2454   20   10    5   16    5    5   71    2]
 [  22   71 1873   77   51    8   82   20  101    9]
 [   5   32   56 1992   11   77   11   40   80   44]
 [   1   21   17    0 1983   12   12    2   21  142]
 [  19   18   11  112   18 1682   37   11  103   58]
 [  28   30   32    3   43   51 2046    0   37    1]
 [  16   57   25   20   70    8    0 1990   11  220]
 [   9  113   16   64   33  115   13   10 1781   61]
 [  15   10    6   35  133   14    0  122   22 2032]]
Accuracy: 0.8642
```


### QDA

```
Training time: 18.9276s
Predict time: 4.8853s
Confusion matrix:
[[2212    3   12   14    1    4   20    5    6    1]
 [  66 2409   12   10    0    0   32    2   39   18]
 [ 961   25  689  143    3    1  310    2  166   14]
 [1231   48   29  606    3   13   66   10  232  110]
 [ 810   22   25   27  250    4  143   17  345  568]
 [ 909   15   13   33    1  214  140    4  666   74]
 [  83   18   14    1    1    2 2146    0    6    0]
 [  81   13    6   52   14    2    1  776  120 1352]
 [ 487  181   18   20    6   17   58    3 1320  105]
 [  65   14   12    7   10    0    0   23   33 2225]]
Accuracy: 0.5561
```


## Summary

<table>
    <tr>
        <th></th>
        <th>Accuracy</th>
        <th>Training Time</th>
        <th>Testing Time</th>
    </tr>
    <tr>
        <td>MLP (500:200)</td>
        <td>97.98%</td>
        <td>79.5696s</td>
        <td>0.3480s</td>
    </tr>
    <tr>
        <td>Dropout NN (500:200)</td>
        <td>97.80%</td>
        <td>118.2654s</td>
        <td>0.3918s</td>
    </tr>
    <tr>
        <td>CNN (32 5x5 filters : 2x2 max pool : 64 5x5 filters : 2x2 max pool : 1024)</td>
        <td>97.69%</td>
        <td>391.8810s</td>
        <td>1.2035s</td>
    </tr>
    <tr>
        <td>Adjusted SVM</td>
        <td>98.4%</td>
        <td>347.1539s</td>
        <td>234.5724s</td>
    </tr>
    <tr>
        <td>Linear SVM</td>
        <td>94.16%</td>
        <td>140.6126s</td>
        <td>TODO</td>
    </tr>
    <tr>
        <td>Random Forest (n_estimators=50, n_jobs=10)</td>
        <td>96.55%</td>
        <td>2.0144s</td>
        <td>0.1586s</td>
    </tr>
    <tr>
        <td>Random Forest (n_estimators=10, max_features=1, max_depth=5)</td>
        <td>61.09%</td>
        <td>0.1462s</td>
        <td>0.0535s</td>
    </tr>
    <tr>
        <td>k nearest neightbors (k=3)</td>
        <td>96.95%</td>
        <td>3.8013s</td>
        <td>1033.7148s</td>
    </tr>
    <tr>
        <td>Decision Tree(max_depth=5)</td>
        <td>65.40%</td>
        <td>2.6527s</td>
        <td>0.0247s</td>
    </tr>
    <tr>
        <td>Adaboost</td>
        <td>73.67%</td>
        <td>32.4964s</td>
        <td>0.7506s</td>
    </tr>
    <tr>
        <td>Naive Bayes</td>
        <td>56.15%</td>
        <td>0.3334s</td>
        <td>0.9994s</td>
    </tr>
    <tr>
        <td>LDA</td>
        <td>86.42%</td>
        <td>17.2674s</td>
        <td>0.0554s</td>
    </tr>
    <tr>
        <td>QDA</td>
        <td>55.61%</td>
        <td>18.9276s</td>
        <td>4.8853s</td>
    </tr>
</table>
