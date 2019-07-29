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
filtering". <a href="https://movielens.org/">movielens.org</a> is an example
for that.

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
    <dt>Centered Cosine Similarity</dt>
    <dd>Subtract the mean value from all elements. If you have null values, don't change anything there. Then apply the cosine similarity.</dd>
    <dt>Jaccard Similarity</dt>
    <dd>Let $x$ and $y$ be items and $r_x, r_y$ be their attributes. Their jaccard similarity is defined as $$f(x, y) := \frac{|r_x \cap r_y|}{|r_x \cup r_y|}$$</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Minkowski_distance">Minkowski Distance</a></dt>
    <dd>$$f(x, y) := \left ( \sum_{i=1}^n {|x_i - y_i|}^p \right )^{1/p}$$</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Mahalanobis_distance">Mahalanobis distance</a></dt>
    <dd>The Mahalanobis distance of an observation <math>\vec{x} = ( x_1, x_2, x_3, \dots, x_N )^T</math> from a set of observations with mean $\vec{\mu} = ( \mu_1, \mu_2, \mu_3, \dots , \mu_N )^T$ and covariance matrix $S$ is defined as:
    $$D_M(\vec{x}) = \sqrt{(\vec{x} - \vec{\mu})^T S^{-1} (\vec{x}-\vec{\mu})}$$</dd>
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

Based on the user-item rating matrix $R$ you build up a user-user similarity matrix.

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

## More Collaborative Filtering

There are many <a href="https://en.wikipedia.org/wiki/Collaborative_filtering">Collaborative filtering</a> (CF) approaches

<dl>
    <dt>Item-based collaborative filtering</dt>
    <dd>"users who liked what you liked, also like..."<ol>
        <li>Build an item-item matrix determining relationships between pairs of items</li>
        <li>Infer the tastes of the current user by examining the matrix and matching that user's data</li>
    </ol><a href="https://en.wikipedia.org/wiki/Slope_One">Slope One</a> is an example</dd>
    <dt>Matrix Factorization</dt>
    <dd>Factorize the rating matrix $R$ into a user-embedding matrix $U$ and an item embedding matrix $V$ such that $R = U \times \Sigma \times V$.</dd>
    <dt>User-based collaborative filtering</dt>
    <dd><ol>
        <li>Look for users who share the same rating patterns with the active user (the user whom the prediction is for).</li>
        <li>Use the ratings from those like-minded users found in step 1 to calculate a prediction for the active user</li>
    </ol>
    <a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">k-NN</a> is one example.
    </dd>
</dl>

One line of work goes in the direction of matrix factorization with alternating
least squares (ALS).[^5,^6] They have a training algorithm with has a time complexity
of $\mathcal{O}(MNK^2)$ for one iteration, where $M$ is the number of users,
$N$ is the number of items and $K$ is the dimension of the latent space.



## Evaluation

There are two conceptually very different ways to think about recommender systems[^4]:

* Matrix Completion: You have a matrix of user-item ratings. This matrix has
  many NULL values. You want to fill them.
* Ranking: Recommend the top-k items for a given user.

### Matrix Completion

One way to evaluate if recommendation systems work is by the typical train-test split.

Possible Metrics, where $y$ is the real value and $p(x)$ is the predicted value:

<dl>
    <dt>Mean Absolute Error (MAE)</dt>
    <dd>$\frac{1}{n} \sum_{i=1}^n |y_i - p(x_i)| \in [0, 1]$, where lower is better</dd>
    <dt>Root Mean Square Error (RMSE)</dt>
    <dd>$\sqrt{\frac{1}{n} \sum_{i=1}^n {(y_i - p(x_i))}^2} \in [0, \infty)$, where lower is better</dd>
</dl>

### Ranking

The problem with those two ways is that low-rated items don't matter much. If
95% of the users look at $n$ items, then you want the Top-$n$ recommendations
to be (1) more relevant than the rest for the user and (2) the order of the
top-$n$ elements to be correct.

Metrics for top-n recommenders:

<dl>
    <dt>Precision@k</dt>
    <dd>$\frac{\text{recommended items @k that are relevant}}{k}$. This gives
        you the portion of items that are relevant to your user.</dd>
    <dt>Recall@k</dt>
    <dd>$\frac{\text{recommended items @k that are relevant}}{total relevant items}$. If precision is high and recall is low, it might indicate that $k$ is just very small. If recall is high and precision is low it might show that not so many items are relevant in comparison to the choice of $k$.</dd>
    <dt>Average Precision@k</dt>
    <dd>TODO</dd>
    <dt>Hit Rate</dt>
    <dd>Number of hits in your $n$ recommendations, divided by the number of users</dd>
    <dt>Average Reciprocal Hit Rank (ARHR)</dt>
    <dd>$\frac{1}{|Users| \cdot \sum_{i=1}^n \frac{1}{rank_i}}$</dd>
    <dt>Cumulative Hit Rate (cHR)</dt>
    <dd>Throw away low-ranking stuff (hence you need a threshold)</dd>
</dl>


### Other

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


### User Feedback

Another way to evaluate is to ask the user:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/05/youtube-feedback-1.png"><img src="../images/2019/05/youtube-feedback-1.png" alt="A jellyfish" style="width: 512px;"/></a>
    <figcaption class="text-center">YouTube Asking for feedback: 1 Star</figcaption>
</figure>

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/05/youtube-feedback-2.png"><img src="../images/2019/05/youtube-feedback-2.png" alt="A jellyfish" style="width: 512px;"/></a>
    <figcaption class="text-center">YouTube Asking for feedback: 2 Star</figcaption>
</figure>

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/05/youtube-feedback-3.png"><img src="../images/2019/05/youtube-feedback-3.png" alt="A jellyfish" style="width: 512px;"/></a>
    <figcaption class="text-center">YouTube Asking for feedback: 3 Star</figcaption>
</figure>

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/05/youtube-feedback-4.png"><img src="../images/2019/05/youtube-feedback-4.png" alt="A jellyfish" style="width: 512px;"/></a>
    <figcaption class="text-center">YouTube Asking for feedback: 4 Star</figcaption>
</figure>

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/05/youtube-feedback-5.png"><img src="../images/2019/05/youtube-feedback-5.png" alt="A jellyfish" style="width: 512px;"/></a>
    <figcaption class="text-center">YouTube Asking for feedback: 5 Star</figcaption>
</figure>


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


## Matrix Factorization

Matrix Factorization is factorization in the same way as with natural numbers:
Take a matrix $R$ and factorize it in $U$ and $V$ such that $R = U \cdot V$. If
the complete matrix $R$ is given, $R$ can be factorized with Singular Value
Decomposition (SVD) or Probabilistic Latent Semantic Analysis (PLSA).

Matrix Factorization is also one way to do collaborative filtering. It was done
for the Netflix prize and is described in [^3]. A [neat short description](https://surprise.readthedocs.io/en/stable/matrix_factorization.html#surprise.prediction_algorithms.matrix_factorization.SVD) is in
SurpriseLib.

**Input**: The ratings of $n$ users for $m$ movies in a matrix $R \in \mathbb{R}^{n \times m}$.

**Algorithm**: Singular value decomposition (SVD) takes $R$ and gives three matrices $U \in \mathbb{R}^{n \times r}$, a descendingly sorted diagonal matrix $\Sigma \in \mathbb{R}^{r \times r}$ and $V \in \mathbb{R}^{r \times m}$
such that $R = U \cdot \Sigma \cdot V$.

The rows in $U$ represent the users. It's called the "latent space". Latent is
math slang for "hidden" (see <a href="https://en.wikipedia.org/wiki/Latent_variable">latent variable</a>). This means we have a reasonable way to represent users.

The rows in $V$ represent the movies in the latent space.

You crop at some point of $\Sigma$ to the first $k$ singular features (with $k < r$).

The problem is that many values of $R$ are missing. Simon Funk found a solution
to that problem. Instead of imputing the values (filling the matrix), he re-formulated the problem
to

$$\min_{u_i, v_i} \sum_{p_{ij}} \left ( p_{ij} - u_i \cdot v_j \right )^2 \text{ with } u_i \in \mathbb{R}^{1 \times r}, v_j \in \mathbb{R}^{r \times 1}$$

This is a minimization problem that can be solved by gradient descent. As you
only consider values $p_{ij}$ that are not zero, you don't have to invent the
remainding ones.


## Code

* Github: [recommender-system](https://github.com/topics/recommender-system?l=python)
* [benfred/implicit](https://github.com/benfred/implicit)

## Datasets

* [MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/100k/)
* [Last.fm dataset](https://www.kaggle.com/neferfufi/lastfm) / [Last.fm 360k](https://www.upf.edu/web/mtg/lastfm360k) / [Last.fm 1k](https://gist.github.com/victorkohler/0931d181ef126e0740d8aac6933f13f4)


## Other Resources

* [Meaning of latent features?](https://datascience.stackexchange.com/q/749/8820)
* Simon Funk: [Netflix Update: Try This at Home](https://sifter.org/~simon/journal/20061211.html)
* Houtao Deng: [Recommender Systems in Practice](https://towardsdatascience.com/recommender-systems-in-practice-cef9033bb23a), 2019.
* Victor: [ALS Implicit Collaborative Filtering](https://medium.com/radon-dev/als-implicit-collaborative-filtering-5ed653ba39fe), 2017 - explains [^6] neatly.
* Implicit
    * Ben Frederickson: [Faster Implicit Matrix Factorization](http://www.benfrederickson.com/fast-implicit-matrix-factorization/), 12.12.2016.
    * Ben Frederickson: [Finding Similar Music using Matrix Factorization](http://www.benfrederickson.com/matrix-factorization/), 02.10.2017.

Not read so far:

* Leskovec, Rajaraman, Ullman: [Collaborative Filtering](https://www.youtube.com/watch?v=h9gpufJFF-0). Lecture 43 of "Mininig of Massive Datasets". Stanford University.
* Maher Malaeb: [The easy guide for building python collaborative filtering recommendation system](https://medium.com/@m_n_malaeb/the-easy-guide-for-building-python-collaborative-filtering-recommendation-system-in-2017-d2736d2e92a8), 2017.
* [surprise docs](https://surprise.readthedocs.io/en/stable/notation_standards.html#salakhutdinov2008a)
* [surprise gist](https://gist.githubusercontent.com/mahermalaeb/3d03feb1bbada7e7e1438f86b1a8abb9/raw/781f21f7591d99f5197a83799594a02f524dd6e4/surprise_tutorial.py)
* Houtao Deng: [Recommender Systems in Practice](https://towardsdatascience.com/recommender-systems-in-practice-cef9033bb23a), 2013
* Kaggle: [Tutorials Recommendation System](https://www.kaggle.com/duykhanh99/tutorials-recommendation-system), 2019.


## Papers

 [^1]: Paul Covington, Jay Adams, Emre Sargin: [Deep Neural Networks for YouTube Recommendations](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45530.pdf)
 [^2]: Yashar Deldjoo, Mehdi Elahi, Paolo Cremonesi: Using Visual Features and Latent Factors for Movie Recommendations, 2016.
 [^3]: Ruslan Salakhutdinov and Andriy Mnih: [Probabilistic Matrix Factorization](http://papers.nips.cc/paper/3208-probabilistic-matrix-factorization.pdf), 2008.
 [^4]: C. C. Aggarwal: Recommender systems, 2016. Springer International Publishing. Pages 1-28.
 [^5]: Xiangnan He, Hanwang Zhang, Min-Yen Kan, Tat-Seng Chua: [Fast Matrix Factorization for Online Recommendation with Implicit Feedback](https://arxiv.org/pdf/1708.05024.pdf), 2017.
 [^6]: Yifan Hu, Yehuda Koren, Chris Volinsky: [Collaborative Filtering for Implicit Feedback Datasets](http://yifanhu.net/PUB/cf.pdf), 2008. ([summary](https://www.shortscience.org/paper?bibtexKey=koren:icdm08&a=martinthoma))
 [^7]: Robert M. Bell, Yehuda Koren and Chris Volinsky: [The BellKor solution to the Netflix Prize](https://www.netflixprize.com/assets/ProgressPrize2007_KorBell.pdf), 2007.
