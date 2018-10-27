---
layout: post
title: Recommender Systems
slug: recommender-systems
author: Martin Thoma
date: 2018-10-07 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/ml.png
---
I recently became interested in recommender systems. You know, the thing on
Amazon that tells you which products you might be interested in. Or the stuff
on Spotify that gives you a song you might like. On YouTube the next videos
shown. On StumbleUpon, your next stumble. On a news page, another article.


## Conceptual Approaches

There are three basic approaches:

* Product Similarity: You watched Saw I, Saw II and Saw III. All of them are
  similar to Saw IV.
* User similarity: Users that liked Saw I, Saw II and Saw III usually also liked
  Saw IV.
* Basket analysis: You bought eggs and sugar, maybe you want to buy milk as
  well.

Recommender systems based on product similarity are also called "content-based recommender systems".
Recommander systems baed on user similarity are also called "collaborative filtering".


## Basic Content-based Recommendations

[Levenshteins edit distance](https://en.wikipedia.org/wiki/Edit_distance)
applied on the product name is probably the simplest approach that has a
mimimal chance of some reasonable results.

The next level in complexity are rules:

* Movies by a director you liked
* Movies with a actor you liked
* Count "links" (actors, directors, producers, ...) and rank by most links

One more level of complexity is using clustering algorithms. One way is to make
a product to a vector and use a similarity measure (e.g. cosine similarity). If
you have natural laguage descriptions you can use tf-idf features and then use
a similarity measure. You would then recommend the most similar products.


## Basic Collaborative Filtering

Users can have different scales on which they rate stuff:

* Binary: Like / Dislike (and "not seen")
* Ternary: Like / Neutral / Dislike (and "not seen")
* 5 Stars
* 100 points

So you want to find the utility function $u: C \times I \rightarrow R$ where
$C$ is the set of customers, $I$ is the set of items and $R$ is the *ordered*
set of ratings. By a simple transformation you can make it $R = [0, 1]$.

The utility function $u$ can be fully defined by a matrix. Most elements of the
matrix are not known, though.

See also: [Collaborative Filtering](https://martin-thoma.com/collaborative-filtering/)

In some sense, bestellsers are a special case of collaborative filtering:
Simply recommending what got sold most.


## Basic Basket Analysis

See [Association Rule Mining](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#association-rules)


## Evaluation

One way to evaluate if recommendation systems work is by the typical train-test split


## Typical Problems

### Cold-Start Problem

The cold-start problem is central and only fixable by content-based
recommendation. If there is a new product, not a single user has rated it. It
is not possible by collaborative filtering to recommend it.


### Wrong Recommendation Mode

* You have bought the DVD "Lord of the Rings" and get the Blue Ray recommended.
* You have liked the normal version of a song and you get the
  techno/rap/christmas version recommended


### The Bubble

* You will never be recommended a movie where you didn't like the genre before.
