---
layout: post
title: Data Scientist Interviews
slug: ds-interview
author: Martin Thoma
date: 2018-06-14 20:00
category: Machine Learning
tags: Machine Learning,Data Science
featured_image: logos/data-science.png
---
Interviews for Data Scientists - which traits and skills are important for a
Data Scientist? Which questions should you be able to answer as a Data
Scientist?


## Skillset

The following is a typical skillset I expect from a data scientist. It might be
that there are some data scientists with a different skillset. This is
absolutely ok, but I would certainly ask why it is the case.

* Statistics: A/B Testing, Confidence intervalls
* Programming Languages: Python or R - the following points are only for
  Python, as I don't know R well enough for them.
* Exploratory Data Analysis: Pandas, Jupyter Notebooks


## Questions

### Conversation Starters

* What are you passionate about?
* How would you explain an A/B test to an engineer with no statistics background?
* Do you think Data Science is important? Why so?


### Concepts

* What is the curse of dimensionality? → [answer](https://martin-thoma.com/curse-of-dimensionality/)
* How can you reduce the dimensionality? → PCA, LDA, Auto-Encoders. See [Wikipedia](https://en.wikipedia.org/wiki/Dimensionality_reduction) for more.
* Is more data always better?
    * It depends on the quality of your data.
    * It depends on your model.
    * You have to deal with this amount as well (storage, memory, computational power)


### Classification

* Which scoring/distance/similarity functions do you know? → Euclidean distance, cosine distance, MSE, MAE, ...
* You do you deal with imbalenced data? → Oversampling; different error metrics


### EDA

* How can you start EDA?
    * CSV-data: Feature ranges, null-values, covariance
    * Image-data: Eigenfaces, Fisher-Faces, Average image, [t-SNE](https://ml4a.github.io/guides/ImageTSNEViewer/)
* When do you stop EDA?


### Model Building

This is about building regression models or classifiers

* Which models do you know → Linear Regression, Gradient Boosting, Neural Network, Random Forests, Decision Trees, ...
* How do you decide which model to use?
* How can you improve a model? → [page 15, point I1 to I7](https://arxiv.org/pdf/1707.09725.pdf)
* How can you determine which features are the most im- portant in your model? → [answer](https://martin-thoma.com/feature-importance/)
