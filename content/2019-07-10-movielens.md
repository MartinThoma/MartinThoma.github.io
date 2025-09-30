---
layout: post
lang: en
title: Movielens Data Set
slug: movielens-data-set
author: Martin Thoma
date: 2019-07-10 20:00
category: My bits and bytes
tags: Machine Learning, Recommendations, Movielens
featured_image: logos/ml.png
---
I'm recently thinking a lot about recommendations and about building the
[book recommendation portal](https://martin-thoma.com/projects-i-never-realized/#book-portal)
I had in mind since 2013.

However, for recommendation systems it is as hard as with any branch of machine
learning to find a good overview over techniques, their respective strengths
and drawbacks as well as hard performance measures.

So let's get started.


## The Data

The [Movielens 20M](https://grouplens.org/datasets/movielens/20m/) contains
20 million movie ratings. They were created by 138,000 users for 27,000 movies.

The data looks like this:

```text
     userId  movieId  rating   timestamp
0         1        2     3.5  1112486027
1         1       29     3.5  1112484676
2         1       32     3.5  1112484819
3         1       47     3.5  1112484727
4         1       50     3.5  1112484580
5         1      112     3.5  1094785740
6         1      151     4.0  1094785734
7         1      223     4.0  1112485573
8         1      253     4.0  1112484940
9         1      260     4.0  1112484826
10        1      293     4.0  1112484703
```

There is genres and tags as well.


## The Evaluation

The task is to predict the ratings. To do so, the data gets sorted by
timestamp. A 50% train data and 50% test data split is done. On the test data,
the mean average error (MAE) is calculated. Lower is better. The results have
to be given with exactly three decimal places.


## Baselines

All of the following evaluations took roughly 43s on my Thinkpad T460p. The
memory consumption of all of them is not relevant.

<div class="warning">Most of the following recommenders are completely useless. The constant recommender does not order the movies at all, the median user rating does not order for a user. And the median movie rating recommender is not personalized, which indicates that a content-based approach might be better. Still, you can see the MAE / MSE score is vastly different. This is an indicator that the evaluating function should be changed.</div>

<table class="table">
    <thead>
    <tr>
        <th>Name</th>
        <th>MAE</th>
        <th>MSE</th>
        <th>Comment</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="background-color: red">Constant 1</td>
        <td style="background-color: red">2.422</td>
        <td style="background-color: red">6.939</td>
        <td>I don't expect this to be awesome, but it should be better than MAE of 5.</td>
    </tr>
    <tr>
        <td style="background-color: red">Constant 5</td>
        <td>1.603</td>
        <td>3.761</td>
        <td>Together with Constant 5, this gives the range in which all recommenders will be.</td>
    </tr>
    <tr>
        <td style="background-color: red">Constant 2.5</td>
        <td>1.217</td>
        <td>1.996</td>
        <td>Predicting the middle is the best if you have absolute no prior knowledge and MAE.</td>
    </tr>
    <tr>
        <td style="background-color: red">Median User Rating</td>
        <td>0.733</td>
        <td>1.112</td>
        <td>Every user in the test set was also in the training set!</td>
    </tr>
    <tr>
        <td>Median Movie Rating</td>
        <td style="background-color: green">0.723</td>
        <td>1.061</td>
        <td>For known movies, predict their median value. For unknown ones, predict the median of all medians of movie ratings.</td>
    </tr>
    <tr>
        <td>User-adjusted movie rating</td>
        <td>0.825</td>
        <td style="background-color: green">1.042</td>
        <td>Use the Median movie rating, but add user bias</td>
    </tr>
    </tbody>
</table>

## Code

```python
#!/usr/bin/env python

"""Analyze the quality of recommendations."""

# 3rd party modules
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
import click
import pandas as pd


def load_data(rating_filepath="ratings.csv"):
    """Load extracted movie lense data."""
    nrows = None
    df = pd.read_csv(rating_filepath, nrows=nrows)
    df["rating"] = df["rating"].astype("int16")
    df = df.sort_values(by="timestamp")
    df_x = df[["timestamp", "userId", "movieId"]]
    df_y = df[["rating"]]
    df_train_x, df_test_x, df_train_y, df_test_y = train_test_split(df_x, df_y)
    return {
        "train": {"x": df_train_x, "y": df_train_y},
        "test": {"x": df_test_x, "y": df_test_y},
    }


class BaselineRecommender(BaseEstimator):
    """Create a baseline recommender."""

    def __init__(self, strategy="constant", constant=2.5):
        self.strategy = strategy
        if constant is not None and strategy != "constant":
            raise RuntimeError(
                "constant is only meaningful in the constant " "strategy."
            )
        self.constant = constant

    def fit(self, df_x, df_y):
        """Fit the recommender on movielens data."""
        df = df_x.join(df_y)
        self.median_by_user = (
            df.groupby(by="userId").aggregate({"rating": "median"})["rating"].to_dict()
        )
        self.median_by_movie = (
            df.groupby(by="movieId").aggregate({"rating": "median"})["rating"].to_dict()
        )
        self.avg_movie = sum(self.median_by_movie.values()) / len(self.median_by_movie)
        self.avg_user = sum(self.median_by_user.values()) / len(self.median_by_user)

    def predict(self, df_x):
        """Fit ratings for user/movie combinations."""
        results = []
        for entry in df_x.to_dict("records"):
            if self.strategy == "constant":
                prediction = self.constant
            elif self.strategy == "movie_median":
                movie = entry["movieId"]
                prediction = self.median_by_movie.get(movie, self.avg_movie)
            elif self.strategy == "user_median":
                user = entry["userId"]
                prediction = self.median_by_user[user]
            elif self.strategy == "user_ajdust_movie_median":
                movie = entry["movieId"]
                movie_median = self.median_by_movie.get(movie, self.avg_movie)

                user = entry["userId"]
                user_bias = self.median_by_user[user] - self.avg_user

                prediction = movie_median + user_bias
            else:
                raise NotImplemented()
            results.append(prediction)
        return results


def evaluate(true_ratings, predicted_ratings, func="mae"):
    """Evaluate the results of a rating prediction."""
    assert len(true_ratings) == len(predicted_ratings)
    if func == "mae":
        absolute_errors = sum(
            abs(a - b) for a, b in zip(true_ratings, predicted_ratings)
        )
        mae = absolute_errors / len(true_ratings)
        val = mae
    elif func == "mse":
        sq_errors = sum((a - b) ** 2 for a, b in zip(true_ratings, predicted_ratings))
        val = sq_errors / len(true_ratings)
    return val


@click.command()
@click.option(
    "--strategy",
    default="constant",
    type=click.Choice(
        ["constant", "movie_median", "user_median", "user_ajdust_movie_median"]
    ),
)
@click.option("--constant", default=None, type=float)
def main(strategy, constant):
    """Analyze recommenders on the Movielens 20M dataset."""
    data = load_data()
    m = BaselineRecommender(strategy=strategy, constant=constant)
    m.fit(data["train"]["x"], data["train"]["y"])
    y_pred = m.predict(data["test"]["x"])
    mae = evaluate(data["test"]["y"]["rating"], y_pred, func="mae")
    mse = evaluate(data["test"]["y"]["rating"], y_pred, func="mse")
    print("MAE of baseline: {:0.3f}".format(mae))
    print("MSE of baseline: {:0.3f}".format(mse))


if __name__ == "__main__":
    main()
```


## Problems

* **Ratings instead of Order**: For applications, we are not interested in the
  right rating but getting the order right. So a constant bias for a user is
  fine. MAE does not capture that fact.


## Publications

* Prateek Sappadla, Yash Sadhwani, Pranit Arora: [Movie Recommender System](http://www.codeheroku.com/static/workshop/hw/movie_recommendation/MovieRecommenderSystem.pdf): They claim to have reached MSE=0.65 with matrix factorization and 0.70 with k-nearest users.
* Shuyu Luo: [Introduction to Recommender System](https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26), 2018.
