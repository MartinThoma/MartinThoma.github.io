---
layout: post
title: Machine Learning Vocabulary
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Machine Learning
featured_image: logos/ai.png
---

Machine Learning is getting quite big. A lot of terms are used, but rarely
defined. This mini-article aimes to give short definitions of commonly used
terms.

* active learning: The algorithm gives a pattern and asks for a label.
* co-training: A form of semi-supervised learning. 2 independant classifiers are trained on different labeled datasets. The classifiers are applied to the unlabeled data. Data with high confidence will be added to the other classifiers data.
* deep learning: Depends on who you ask. Sometimes it means multi-layer perceptrons with more than N layers (some say N=2 is already deep learning, others want N>20). Often it is connected with auto-encoders.
* detection: You have something you search and you want to know where it is.
* inductive learning: same as semi-supervised learning (?)
* recognition: You have a pattern and you want to know what it is.
* self-learning: One form of semi-supervised learning, where you train an initial system on the labeled data, then label the unlabeled data where the classifier is 'sure enough'. After that, you train a new system on all data and re-label the unlabeled data. This is iterated.
* semi-supervised learning: Parts of the data have labels, others don't have labels.
* supervised learning: The learner has patterns and labels.
* transductive learning: label unlabeled data (the aim here is NOT to find a hypothesis)
* unsupervised learning: No labels are given


## Detection vs. Recognition

Face detection means you have an image and you want to get possible places
where faces are.

Face recognition means you have an image where (only) one face is and you want
to know who it is.


## Supervised, unsupervised and semi-supervised learning

The classical approach is that you have a lot of labeled data and you learn
from that. This is called supervised learning.

Another approach is that you don't have any labels. For example, you could have
a lot of photographs and you have a decent face detection algorithm. Then you
can eventually say which (parts of) images show the same person, but not the
name of that person.

Semi-supervised learning is what is probably most common today. You have lots
of unlabeled data and some labeled data. You want to use both, labeled and
unlabeled data for learning.


##