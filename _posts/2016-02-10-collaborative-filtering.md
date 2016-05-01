---
layout: post
title: Collaborative Filtering
author: Martin Thoma
date: 2016-02-10 21:35
category: Machine Learning
tags: Rating
featured_image: logos/ai.png
---

Suppose you are in the Netflix setting: You have <span markdown="0">$M$</span>
movies, <span markdown="0">$N$</span> users and integer ratings
<span markdown="0">$1, \dots, K$</span> for some movies by some users.

You want to predict all missing values. This means you want to say how the
users would rate movies they have not actually rated.

Please note that ratings for products on Amazon might be a very similar
situation. It might also be similar to the StumbleUpon rating.


## The Problem

* **Much Data**: You have 17&thinsp;000 movies, 480&thinsp;000 users and
  100&thinsp;000&thinsp;000 ratings of movies by those users.
* **Missing Data**: Although you have a lot of ratings, a complete dataset
  would be <span markdown="0">$17\cdot 10^3 \cdot 480 \cdot 10^3 = 8160 \cdot 10^6$</span>
  ratings. This means you only have about 12% of all possible ratings. There
  is a lot of data missing.


## A Solution

Train one RBM per user, but share weights amongst the RBMs. This simply means
the weights are averaged.

The visible units are movies. But instead of having binary visible units, the
units have <span markdown="0">$K=5$</span> states on which softmax is applied.

The hidden units (about 100) model dependencies between movie ratings.

When you now want to predict the missing ratings, you can just perform a
sampling in the user-specific RBM. You calculate the values of the hidden units,
then you have a vector for this user which describes the users preferences.
You add the missing movies with the weights from the other users and sample
back.


## Material

* Salakhutdinov, Mnih and Hinton: [Restricted Boltzmann machines for collaborative filtering](http://www.cs.toronto.edu/~rsalakhu/papers/rbmcf.pdf). In Proceedings of the 24th international conference on Machine learning, 2007.
* Hinton: [5. RBMs for Collaborative Filtering
](https://www.youtube.com/watch?v=fzAuXMg_7n4) on YouTube. 9th of November 2013.
* [Netflix Prize Data Set](http://academictorrents.com/details/9b13183dc4d60676b773c9e2cd6de5e5542cee9a)