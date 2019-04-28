---
layout: post
title: Recommender Systems
slug: recommender-systems
author: Martin Thoma
date: 2018-10-07 20:00
category: Machine Learning
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
The New York Times article recommendation is an example for that.

Recommander systems based on user similarity are also called "collaborative
filtering".

Pandora is an example for content-based recommendation + collaborative filtering.


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

<dl>
    <dt>Cosine-Similarity</dt>
    <dd>Let $x$ and $y$ be items. Their cosine similarity is defined as $$f(x, y) := \frac{\sum_i x_i y_i}{\sqrt{\sum_i x_i^2} \sqrt{\sum_i y_i^2}}$$</dd>
</dl>


## User-Based Collaborative Filtering

Users can have different scales on which they rate stuff:

* Binary: Like / Dislike (and "not seen")
* Ternary: Like / Neutral / Dislike (and "not seen")
* 5 Stars
* 100 points

So you want to find the utility function $u: C \times I \rightarrow R$ where
$C$ is the set of customers, $I$ is the set of items and $R$ is the *ordered*
set of ratings. By a simple transformation you can make it $R = [0, 1]$.

The utility function $u$ can be fully defined by a user-item rating matrix.
Most elements of the matrix are not known, though.

Based on the user-item rating matrix you build up a user-user similarity matrix.

You look up similar users, generate candidates for recommendation, score and filter candidates (items the user already knows).

See also: [Collaborative Filtering](https://martin-thoma.com/collaborative-filtering/)

In some sense, bestellsers are a special case of collaborative filtering:
Simply recommending what got sold most.

<dl>
    <dt>Adjusted Cosine</dt>
    <dd>$$f(x, y) := \frac{\sum_i (x_i -\bar{x}) (y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2} \sqrt{\sum_i (y_i - \bar{y})^2}}$$
    Applicable mostly to get a similar user based on ratings. The idea is that different people have different baselines from which they operate, e.g. in a 5 star rating you could always give 5 stars if nothing is wrong. Or always 3 stars and if there is something really good, give more.</dd>
    <dt>item-based pearson similarity</dt>
    <dd>$$f(x, y) := \frac{\sum_i (x_i - \bar{j})(y_i - \bar{j})}{\sqrt{\sum_i (x_i - \bar{j})^2} \sqrt{\sum_i (y_i - \bar{j})^2}}$$</dd>
    <dt>Spearman rank correlation</dt>
    <dd>Pearson similarity based on ranks (position in the recommendation), not ratings. Usually not use in practice.</dd>
    <dt>Mean Squared Difference Similarity</dt>
    <dd>$$MSD(x, y) := \frac{\sum_{i \in I_{x, y}} (x_i - y_i)^2}{|I_{x, y}|}$$
        and the similarity:
        $$MSDsim(x, y) := \frac{1}{MSD(x, y) + 1}$$</dd>
    <dt>Jaccard Similarity</dt>
    <dd>$$\frac{A \cap B}{A \cup B}$$</dd>
</dl>


## Basic Basket Analysis

See [Association Rule Mining](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/#association-rules)


## Evaluation

One way to evaluate if recommendation systems work is by the typical train-test split.

Possible Metrics, where $y$ is the real value and $p(x)$ is the predicted value:

<dl>
    <dt>Mean Absolute Error (MAE)</dt>
    <dd>$\frac{1}{n} \sum_{i=1}^n |y_i - p(x_i)| \in [0, 1]$, where lower is better</dd>
    <dt>Root Mean Square Error (RMSE)</dt>
    <dd>$\sqrt{\frac{1}{n} \sum_{i=1}^n {(y_i - p(x_i))}^2} \in [0, \infty)$, where lower is better</dd>
</dl>

The problem with those two ways is that low-rated items don't matter much. If
95% of the users look at $n$ items, then you want the Top-$n$ recommendations
to be (1) more relevant than the rest for the user and (2) the order of the
top-$n$ elements to be correct.

Metrics for top-n recommenders:

<dl>
    <dt>Hit Rate</dt>
    <dd>Number of hits in your $n$ recommendations, divided by the number of users</dd>
    <dt>Average Reciprocal Hit Rank (ARHR)</dt>
    <dd>$\frac{1}{|Users| \cdot \sum_{i=1}^n \frac{1}{rank_i}}$</dd>
    <dt>Cumulative Hit Rate (cHR)</dt>
    <dd>Throw away low-ranking stuff (hence you need a threshold)</dd>
</dl>

Other quality indicators for a recommendation system

<dl>
    <dt>Diversity</dt>
    <dd>How broad is the variety of items recommended to people?</dd>
    <dt>Novelty</dt>
    <dd>How many new/unfamiliar things do get recommended to a user? The higher the novelty, the more likely the user will discover something new. If it is too high, the user doesn't trust the recommendation anymore.</dd>
    <dt>Churn</dt>
    <dd>How often do recommendations for a user change?</dd>
    <dt>Responsiveness</dt>
    <dd>How quickly are recommendations adjusted?</dd>
</dl>

## Typical Problems

### Cold-Start Problem

The cold-start problem is central and only fixable by content-based
recommendation. If there is a new product, not a single user has rated it. It
is not possible by collaborative filtering to recommend it.

### Sparsity

You have so many items, that two users have no item in common and two items usually
don't have properties in common.

### Wrong Recommendation Mode

* You have bought the DVD "Lord of the Rings" and get the Blue Ray recommended.
* You have liked the normal version of a song and you get the
  techno/rap/christmas version recommended


### The Bubble

* You will never be recommended a movie where you didn't like the genre before.

### Surrogate-Problem

Ultimatively, we want to maximize user engagement. In order to achieve this, we
define a surrogate (e.g. accuracy of predicting user ratings).

The problem is that the choice of the surrogate matters a lot. A different
surrogate might have way bigger impact on our real goal than an improvement in
achieving the surrogate goal.

# Vocabulary

<dl>
    <dt>Top-N Recommendation</dt>
    <dd>Recommend N items</dd>
    <dt>mise en scène</dt>
    <dd>The idea in content-based filtering for movies to extract properties
        directly from the movie itself. It includes:
        Average shot length, color variance, mean motion average across all the
        frames, lightning, number of shots</dd>
</dl>


## Papers

* Paul Covington, Jay Adams, Emre Sargin: [Deep Neural Networks for YouTube Recommendations](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45530.pdf)
* Yashar Deldjoo, Mehdi Elahi, Paolo Cremonesi: Using Visual Features and Latent Factors for Movie Recommendations, 2016.
