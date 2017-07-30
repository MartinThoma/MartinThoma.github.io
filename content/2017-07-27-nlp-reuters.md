---
layout: post
title: The Reuters Dataset
slug: nlp-reuters
author: Martin Thoma
date: 2017-07-27 20:00
category: Machine Learning
tags: NLP, Reuters, Classification
featured_image: logos/nlp.png
---
Reuters is a benchmark dataset for [document classification](https://martin-thoma.com/document-classification/).
To be more precise, it is a multi-class (e.g. there are multiple classes),
multi-label (e.g. each document can belong to many classes) dataset.
It has **90 classes**, **7769 training documents** and **3019 testing documents**.
It is the ModApte (R(90)) subest of the Reuters-21578 benchmark ([source](https://stackoverflow.com/a/25149714/562769)).

The mean number of words per document, grouped by class, is between 93 and 1263
on the training set.

The training set has a **vocabulary size of 35247**. Even if you restrict it to
words which appear at least 5 times and at most 12672 times in the training
set, there are still 12017 words. Those 12017 words were used as features in
the following.


## Classes and Labels

```
                              documents
        class name            train   test    mean number of words in train set
     1: earn                : 2877    1087    104.4
     2: acq                 : 1650     719    150.1
     3: money-fx            :  538     179    219.0
     4: grain               :  433     149    223.6
     5: crude               :  389     189    247.3
     6: trade               :  368     117    294.3
     7: interest            :  347     131    198.0
     8: wheat               :  212      71    225.6
     9: ship                :  197      89    203.7
    10: corn                :  181      56    259.1
    11: money-supply        :  140      34    170.5
    12: dlr                 :  131      44    230.4
    13: sugar               :  126      36    247.2
    14: oilseed             :  124      47    277.9
    15: coffee              :  111      28    264.1
    16: gnp                 :  101      35    372.8
    17: gold                :   94      30    188.5
    18: veg-oil             :   87      37    291.0
    19: soybean             :   78      33    347.9
    20: livestock           :   75      24    222.9
    21: nat-gas             :   75      30    257.7
    22: bop                 :   75      30    288.1
    23: cpi                 :   69      28    235.4
    24: cocoa               :   55      18    266.4
    25: reserves            :   55      18    216.1
    26: carcass             :   50      18    259.7
    27: copper              :   47      18    201.6
    28: jobs                :   46      21    232.7
    29: yen                 :   45      14    282.8
    30: ipi                 :   41      12    232.1
    31: iron-steel          :   40      14    220.5
    32: cotton              :   39      20    366.3
    33: barley              :   37      14    272.9
    34: gas                 :   37      17    209.4
    35: rubber              :   37      12    274.5
    36: alum                :   35      23    180.5
    37: rice                :   35      24    359.8
    38: palm-oil            :   30      10    234.5
    39: meal-feed           :   30      19    387.1
    40: sorghum             :   24      10    511.3
    41: retail              :   23       2    324.8
    42: zinc                :   21      13    189.9
    43: silver              :   21       8    221.0
    44: pet-chem            :   20      12    204.9
    45: wpi                 :   19      10    200.9
    46: tin                 :   18      12    322.1
    47: rapeseed            :   18       9    168.6
    48: orange              :   16      11    169.6
    49: strategic-metal     :   16      11    205.6
    50: housing             :   16       4    207.2
    51: hog                 :   16       6    162.3
    52: lead                :   15      14    216.7
    53: soy-oil             :   14      11    568.7
    54: heat                :   14       5    190.4
    55: fuel                :   13      10    194.6
    56: soy-meal            :   13      13    551.0
    57: lei                 :   12       3    134.7
    58: sunseed             :   11       5    425.1
    59: dmk                 :   10       4    212.1
    60: lumber              :   10       6    242.1
    61: tea                 :    9       4    365.1
    62: income              :    9       7    286.4
    63: nickel              :    8       1    193.6
    64: oat                 :    8       6    648.4
    65: l-cattle            :    6       2    298.0
    66: instal-debt         :    5       1    134.3
    67: platinum            :    5       7    174.8
    68: groundnut           :    5       4    258.0
    69: rape-oil            :    5       3    167.2
    70: sun-oil             :    5       2    201.9
    71: coconut-oil         :    4       3    471.4
    72: jet                 :    4       1    109.6
    73: coconut             :    4       2    264.5
    74: propane             :    3       3    352.0
    75: potato              :    3       3    161.2
    76: cpu                 :    3       1    133.2
    77: rand                :    2       1    345.7
    78: palmkernel          :    2       1    326.3
    79: copra-cake          :    2       1    495.0
    80: dfl                 :    2       1    764.7
    81: naphtha             :    2       4    206.7
    82: palladium           :    2       1    93.0
    83: nzdlr               :    2       2    508.8
    84: groundnut-oil       :    1       1    277.5
    85: castor-oil          :    1       1    194.0
    86: sun-meal            :    1       1    153.0
    87: lin-oil             :    1       1    262.5
    88: cotton-oil          :    1       2    1262.7
    89: rye                 :    1       1    383.0
    90: nkr                 :    1       2    122.3
```

By far most documents have either one or two labels, but some have up to 15:

```
labelcount= 1, documentcount=9160
labelcount= 2, documentcount=1173
labelcount= 3, documentcount= 255
labelcount= 4, documentcount=  91
labelcount= 5, documentcount=  52
labelcount= 6, documentcount=  27
labelcount= 7, documentcount=   9
labelcount= 8, documentcount=   7
labelcount= 9, documentcount=   5
labelcount=10, documentcount=   3
labelcount=11, documentcount=   2
labelcount=14, documentcount=   2
labelcount=12, documentcount=   1
labelcount=15, documentcount=   1
```


Let's look at the relationship between the classes. Which classes occur often
together? Are there classes which can be used to predict the presence of other
classes? For example, `wheat` should imply `grain`.

Here are the 50 strongest predictors:

```
castor-oil => cotton-oil (0.999742566611)
castor-oil => groundnut-oil (0.999742566611)
castor-oil => lin-oil (0.999742566611)
castor-oil => nkr (0.999742566611)
castor-oil => rye (0.999742566611)
castor-oil => sun-meal (0.999742566611)
copra-cake => palmkernel (0.999742566611)
cotton-oil => castor-oil (0.999742566611)
cotton-oil => groundnut-oil (0.999742566611)
cotton-oil => lin-oil (0.999742566611)
cotton-oil => nkr (0.999742566611)
cotton-oil => rye (0.999742566611)
cotton-oil => sun-meal (0.999742566611)
groundnut-oil => castor-oil (0.999742566611)
groundnut-oil => cotton-oil (0.999742566611)
groundnut-oil => lin-oil (0.999742566611)
groundnut-oil => nkr (0.999742566611)
groundnut-oil => rye (0.999742566611)
groundnut-oil => sun-meal (0.999742566611)
lin-oil => castor-oil (0.999742566611)
lin-oil => cotton-oil (0.999742566611)
lin-oil => groundnut-oil (0.999742566611)
lin-oil => nkr (0.999742566611)
lin-oil => rye (0.999742566611)
lin-oil => sun-meal (0.999742566611)
nkr => castor-oil (0.999742566611)
nkr => cotton-oil (0.999742566611)
nkr => groundnut-oil (0.999742566611)
nkr => lin-oil (0.999742566611)
nkr => rye (0.999742566611)
nkr => sun-meal (0.999742566611)
palmkernel => copra-cake (0.999742566611)
rye => castor-oil (0.999742566611)
rye => cotton-oil (0.999742566611)
rye => groundnut-oil (0.999742566611)
rye => lin-oil (0.999742566611)
rye => nkr (0.999742566611)
rye => sun-meal (0.999742566611)
sun-meal => castor-oil (0.999742566611)
sun-meal => cotton-oil (0.999742566611)
sun-meal => groundnut-oil (0.999742566611)
sun-meal => lin-oil (0.999742566611)
sun-meal => nkr (0.999742566611)
sun-meal => rye (0.999742566611)
castor-oil => copra-cake (0.999613849916)
castor-oil => dfl (0.999613849916)
castor-oil => naphtha (0.999613849916)
castor-oil => nzdlr (0.999613849916)
castor-oil => palladium (0.999613849916)
castor-oil => palmkernel (0.999613849916)
```


## Multi-label Scoring

I've never been in a multi-label context, so it was not directly clear to me
which scoring is used. Thanks to Chirag Nagpal who pointed me in the right
direction:

* **Accuracy**: For each document, one has to make a decision for each possible
  category. As most documents belong to one or two categories, the simplest
  classifier simply decides all the time that the document does not belong to
  any category. For the used dataset, this leads to an accuracy of 0.986. Hence
  accuracy is not suitable.
* Micro/macro averaged ROC or Precision/Recall curve:
    * Micro: Calculate metrics globally by counting the total true positives,
      false negatives and false positives.
    * Macro: Calculate metrics for each label, and find their unweighted mean.
      This does not take label imbalance into account.
* F1 score: See [user manual](http://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
* Coverage error: See [user manual](http://scikit-learn.org/stable/modules/model_evaluation.html#coverage-error)

A nice overview is given by [A Literature Survey on Algorithms for Multi-label Learning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.364.5612&rep=rep1&type=pdf#page=13).


## Classifier comparison (tf-idf)

The following are the accuracies as well as the training and test times. All
classifiers got the same tf-idf features.


```
vocabulary size = 26147
```

```
Classifier                      Acc     F1
-------------------------------------------------------------------------------
LinearSVC                     : 99.66% 86.61% in   31.00s train /    9.72s test
Logistic Regression (C=1000)  : 99.65% 86.33% in   38.70s train /    9.75s test
MLP (3 Layer)                 : 99.63% 86.00% in  439.13s train /    1.37s test
MLP (2 Layer)                 : 99.58% 83.02% in  328.98s train /    1.44s test
Logistic Regression (C=1)     : 99.44% 75.25% in   32.62s train /    9.44s test
k nn 5                        : 99.44% 78.43% in    8.80s train / 1087.94s test
k nn 3                        : 99.41% 77.32% in    9.34s train / 1174.55s test
Random Forest (200 estimators): 99.40% 72.73% in   56.71s train /    6.49s test
Random Forest (50 estimators) : 99.39% 72.56% in   13.55s train /    1.18s test
Decision Tree                 : 99.21% 63.86% in   12.42s train /    0.11s test
Naive Bayes                   : 98.75% 50.04% in  236.15s train /  102.17s test
SVM, linear                   :   (bad)       in 6875.84s train / 2501.81s test
```

There are a couple of things to notice here:

* **Speed**:
    * Naive Bayes and k-nn is slow
    * Random forests and MLP are fast
    * SVM depends extremely on the implementation (see [What is the difference between LinearSVC and SVC(kernel=“linear”)?](https://stackoverflow.com/q/45384185/562769))
* **Prediction Quality**:
    * LinearSVC, logistic regression and MLP are accurate
    * Achieving high accuracy seems to be easier than achieving high F1 scores.

The MLP has a reasonable prediction quality and test time.


### Multilayer Perceptron

When training a multilayer perceptron for a multi-label classification task, there
are two important things to look for:

* **Output layer**: Do not  use softmax, as the normalization does not make
  sense in this case.
* **Loss**: Use [``binary_crossentropy`](https://keras.io/losses/#binary_crossentropy)

When you print precision, recall, F1-score and accuracy you note the following:

* Accuracy gets to 98% in the first epoch and over 99% in the second. It stays
  that high.
* Precision is at about 4% in the first epoch and over 97% in the second. It
  stays that high.
* Recall needs about 15 epochs of steady progress to get over 98%.

As a consequence, the F1 score steadily increases. Hence by using other metrics
one can see that the classifier makes great improvements, although the accuracy
is pretty high from the beginning.


## Code

See [GitHub](https://github.com/MartinThoma/algorithms/blob/master/ML/nlp/).

If you use it, please cite this article or link to this blog post:

```
@Misc{Thom2017-reuters,
  Title                    = {The Reuters Dataset},

  Author                   = {Martin Thoma},
  Month                    = jul,
  Year                     = {2017},

  Url                      = {https://martin-thoma.com/nlp-reuters}
}
```

### Data loading

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility file for the Reuters text categorization benchmark dataset.

See also
--------
http://www.vision.caltech.edu/Image_Datasets/Caltech101/
"""

from nltk.corpus import reuters
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer

n_classes = 90
labels = reuters.categories()


def load_data(config={}):
    """
    Load the Reuters dataset.

    Returns
    -------
    Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    stop_words = stopwords.words("english")
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    mlb = MultiLabelBinarizer()

    documents = reuters.fileids()
    test = [d for d in documents if d.startswith('test/')]
    train = [d for d in documents if d.startswith('training/')]

    docs = {}
    docs['train'] = [reuters.raw(doc_id) for doc_id in train]
    docs['test'] = [reuters.raw(doc_id) for doc_id in test]
    xs = {'train': [], 'test': []}
    xs['train'] = vectorizer.fit_transform(docs['train']).toarray()
    xs['test'] = vectorizer.transform(docs['test']).toarray()
    ys = {'train': [], 'test': []}
    ys['train'] = mlb.fit_transform([reuters.categories(doc_id)
                                     for doc_id in train])
    ys['test'] = mlb.transform([reuters.categories(doc_id)
                                for doc_id in test])
    data = {'x_train': xs['train'], 'y_train': ys['train'],
            'x_test': xs['test'], 'y_test': ys['test'],
            'labels': globals()["labels"]}
    return data


if __name__ == '__main__':
    config = {}
    data = load_data(config)
    print("len(data['x_train'])={}".format(len(data['x_train'])))
    print("data['x_train'].shape={}".format(data['x_train'].shape))

```


### Experimenting with classifiers



## See also

* NLTK: [Other datasets](http://www.nltk.org/book/ch02.html)
* [Reuters-21578](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
* Publications:
    * [Text Categorization with Support Vector Machines: Learning with Many Relevant Features](http://www.cs.cornell.edu/people/tj/publications/joachims_98a.pdf)
* Blog posts:
    * Miguel Malvarez: [Classifying Reuters-21578 collection with Python: Representing the data](https://miguelmalvarez.com/2015/03/20/classifying-reuters-21578-collection-with-python-representing-the-data/)
    * Miguel Malvarez: [Classifying Reuters-21578 collection with Python](https://miguelmalvarez.com/2016/11/07/classifying-reuters-21578-collection-with-python/)