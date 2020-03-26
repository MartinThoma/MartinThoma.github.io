---
layout: post
title: Document Classification
slug: document-classification
author: Martin Thoma
date: 2017-07-26 20:00
category: Machine Learning
tags: NLP, Machine Learning, Classification
featured_image: logos/ml.png
---
This article explains how to classify texts.

Suppose you have a text classification problem. For example, you want to
classify incoming emails as (C1) spam (C2) notifications (C3) personal. Hence each email belongs to exactly one of three classes.


## Basic Setup

Suppose **you have corpus** of 1000 emails. You make a **stratified split**
into 600 training emails and 400 test emails. The class C1 is 40% of the data,
C2 is 10% of the data and C3 is 50% of the data in both, the training and the
test set. Don't touch the test set until the very end.

Let $I_1 \subsetneq 1, \dots, 600$ be the set of indices of emails which belong
to class C1, $I_2 \subsetneq 1, \dots, 600$ be the set of indices of emails
which belong to set C2 and $I_3 \subsetneq 1, \dots, 600$ be the set of emails
which belong to set C3.

## Get Features

Now you **build a list of unique words** $w$. Let $W \in \mathbb{N}$ denote the total number of unique words in the training set. So you know which words appear in the documents in the training set. There are certainly words which you did not see in the training set. Don't worry about this.

Let the count how often word $w$ appears in email $i = 1, \dots, N$ be denoted by $n_{w,i} \in \mathbb{N}$. Let $n_{w, \text{total}} = \sum_{i=1}^N n_{w,i}$ be the count how often the word $w$ appears in all documents combined.

### Word Presence Feature
For each word, you can have a binary feature: Either the word is in the e-mail or not. I call this the "word presence feature".

Now you can calculate: If a word $w$ appears in a document, the probability that the e-mail belongs to class 1 is

$$P(C_1|w) = \frac{\sum_{i \in I_1} 1_{n_{w,i} \geq 1}}{n_{w, \text{u}} = \sum_{i \in I_1 \cup I_2 \cup I_3} 1_{n_{w,i} \geq 1}}$$

Hence you divide the number of e-mails of the first class in which the word $w$ appeared at least once by the total count of e-mails in which the word $w$ appeared at least once.

Ok, but you don't only have one feature, but many. You are interested in
$P(C_1 | w_1, \dots, w_N)$.

By applying Bayes Rule, we get:

\begin{align}
  P(C_1 | w_1, \dots, w_N) &= \frac{P(w_1, \dots, w_N | C_1) \cdot P(C_1)}{P(w_1, \dots, w_N)}\\
  &= \frac{P(w_1 | C_1) \cdot P(w_2 | w_2, C_1) \dots \cdot P( w_{N} |w_1, \dots, w_{N-1}, C_1) \cdot P(C_1)}{P(w_1, \dots, w_N)}
\end{align}

Now, $P(C_1) = 0.4$ is called the a priori probability of the class $C_1$. So
if we knew nothing about the content of the e-mail, we would guess $C_1$ has
a probability of 40% as it is the amout of e-mails in that class.

The other terms are more difficult. We don't have enough data for this. So we
make the simplifying (and wrong!) assumption that words are independant of each
other. Then we get:

\begin{align}
  P(C_1 | w_1, \dots, w_N) &= \frac{P(w_1 | C_1) \cdot P(w_2 | C_1) \dots \cdot P( w_{N} | C_1) \cdot P(C_1)}{P(w_1, \dots, w_N)}
\end{align}

As we know that

$$1 = \sum_{i=1}^3 P(C_i | w_1, \dots, w_N)$$

it is sufficient to calculate the nominators and divide each of the three
denominators by the sum of all three.

Congratulations, your first document classifier is working!

### Tf-idf

For each word, we can measure how often it appears in a given e-mail. Certainly,
the more often it appears the more important it is. But the longer the e-mail is,
the less important it is. So we should divide by the total count of words of
an e-mail. This is called the term frequency (Tf) of a word in a document (e-mail).
Sometimes, this is also denoted by $\text{tf}(w, d)$ where $w$ is the word (term)
and $d$ is the document (e-mail).

Next, we realize that some words contain more information than others. For
example, the word "the" might occur in almost every document. We do so by dividing by

$$\text{idf}(w, D) = \frac{N}{|d \in D: w \in d|}$$

where $N = 600$ is the total amount of documents we have in the training set.
The denominator is the total count of words in all documents in the training
set combined.

Hence we can get a Tf-idf feature for all words.

You can see that this allows us to apply the same Bayesian approach as before.
In fact, you should now see that the Bayesian approach is not part of the
features, but a classifier! And if you look at the [tf-idf Wikipedia page](https://en.wikipedia.org/wiki/Tf%E2%80%93idf#Definition) you can see that there are a couple of similar features!


### Terms instead of Words

I've only talked about words before, but you can calculate tf-idf for *terms*,
too.

Take "New York" as an example. You might see "New" in an e-mail and you might
see "York" in an e-mail. But the combined term "New York" is something
different than seeing both single words. Hence you might want to have the
tf-idf feature of "New York", too.


## Classifiers

I've introduced the Bayes Classifer, but there are a lot more. Most notably:

* [SVMs](https://martin-thoma.com/svm-with-sklearn/)
* Neural Networks
* Decision Trees (and Random Forests)

See my [Comparing Classifiers](https://martin-thoma.com/comparing-classifiers/)
for a lot more classifiers.


## Feature Engineering

One thing I would try to find out is which features are really good. You can
probably figure out keywords with this approach. Hence you can make sense of
the decision. And you might be able to throw away a lot of words.

PCA / LDA are two feature reduction methods that might be interesting. Other methods are:

* Forward Feature Construction:
    1. Start with an empty set of features.
    2. For each feature not in the feature list: Find the one where adding it leads to the best accuracy.
    3. If the desired accuracy is reached, stop. Otherwise continue with 2.
* Feature Elimination
    1. Start with all features.
    2. For each feature in the feature list: Try where removing it leads to the least loss in accuracy.
    3. If the accuracy dropped below the required accuracy, stop and take the last feature list. Otherwise, continue with 2.


## Evaluation

Last, but not least, I suggest the following approach to evaluate what you apply for your e-mail classifier:

* Split the training set into 500 e-mails for training and 100 e-mails for validation
* Traing all methods you guess on the 500 e-mails. Evluate on the 100 e-mails what is best.
* Make sure everything is what you think it should be like. Run your experiments with those 500 / 100 e-mails
* When you're finished, evaluate on the 400 e-mails your final setup. Only once. This is your estimate how good you really are.

You might also want to have a look at cross-validation.


## Public Datasets

I'm not aware of public datasets for document classification, but you can easily
create one by scraping wikipedia categories / subreddits.

Leave a comment if I forgot something / you know more details :-)


## Literature

* Juan Ramos: [Using TF-IDF to Determine Word Relevance in Document Queries ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.1424&rep=rep1&type=pdf)
