---
layout: post
title: Probability Theory in Laymans Terms
author: Martin Thoma
date: 2014-11-22 17:19
category: Mathematics
tags:
- Probability Theory
featured_image: logos/statistics.png
---

Here are some very simple explanations of terms in probability theory.


**Random Variable**: The thing which is changing, where you can only say how
likely some values are. For example, a random variable in a dice experiment
might be the outcome of a single dice throw. Or how often you had a 6 in three
dice throws. This does not have to be discrete like it is in dice throws, but
can be contiuous like how tall humans are (if you say you measure it very
precise... I know I'm 174.56789cm tall!)

**Distribution**: A table for the outcome of random variables. Like the
following for a non-fair dice:

| X := "Result of a dice throw" | Probability of that outcome |
| ----------------------------- | --------------------------- |
| 1                             | 0.1                         |
| 2                             | 0.2                         |
| 3                             | 0.3                         |
| 4                             | 0.2                         |
| 5                             | 0.1                         |
| 6                             | 0.1                         |
| ----------------------------- | --------------------------- |
| Sum:                          | 1                           |

For continous variables, this is more complicated. You have infinite possible
outcomes, so you can't simply give a table. But you can define a function.
(Then you have to make sure that the "sum", aka integral, of all is one.). This
is also called the "density".

## Joint Distribution

Think of the students example. You have three random variables: Intelligence
\(I\), difficulty of a test \(D\) and grade \(G\). The possible values of those
variables are \(I \in \{dumb, smart\}\),
\(D \in \{easy, hard\}\) and \(G \in \{A, B, C\}\). Then the joint distribution
is just a table over all combinations of those three variables:

| Intelligence I | Difficulty D | Grade G | P(I, D, G) |
| -------------- | ------------ | ------- | ---------- |
| dumb           | easy         | A       | 700/5441   |
| smart          | easy         | A       | 840/5441   |
| dumb           | hard         | A       | 0          |
| smart          | hard         | A       | 672/5441   |
| dumb           | easy         | B       | 600/5441   |
| smart          | easy         | B       | 480/5441   |
| dumb           | hard         | B       | 252/5441   |
| smart          | hard         | B       | 336/5441   |
| dumb           | easy         | C       | 315/5441   |
| smart          | easy         | C       | 280/5441   |
| dumb           | hard         | C       | 336/5441   |
| smart          | hard         | C       | 630/5441   |

## Conditioned Distribution

When you know something, you can assign some rows of this table the probability
0. Then you have to make sure that the sum is 1 again, so you divide all values
by the sum of the values before.

For example, assume you know that a student got the grade "B". Then you know
the new table is

| Intelligence I | Difficulty D | Grade G | P(I, D, G) | P(I, D | G=B) |
| -------------- | ------------ | ------- | ---------- | ------------- |
| dumb           | easy         | B       | 600/5441   | 600/1668      |
| smart          | easy         | B       | 480/5441   | 480/1668      |
| dumb           | hard         | B       | 252/5441   | 252/1668      |
| smart          | hard         | B       | 336/5441   | 336/1668      |
| -------------- | ------------ | ------- | ---------- | ------------- |
| Sum            |              |         | 1668/5441  | 1             |

Getting this new table consists of <i>reduction</i> (getting rid of all
rows which are obviously not the case) and <i>normalization</i> (dividing
the probability from before by the new sum; making sure the sum is 1 again).


## Marginalization

Marginalization is a simplification of such a probability table with many
variables. For example, say you marginalize to I. Then you would get:

| Intelligence I | P(I)       |
| -------------- | ---------- |
| dumb           | 2203/5441  |
| smart          | 3238/5441  |


## Factor

A function / table \(\phi(X_1, \dots, X_n)\) which maps the values of random
variables to real numbers:

\[\phi: Val(X_1, \dots, X_n) \rightarrow \mathbb{R}\]

So essentially, a factor is again a table.

Factors \(\phi_1\), \(\phi_2\) can also be multiplied. The new factor is
defined on the union of the random variables of \(\phi_1\) and \(\phi_2\).


## Abbreviations

* **CPD**: [Conditional probability distribution](https://en.wikipedia.org/wiki/Conditional_probability_distribution)
* **JPD**: Joint Probability Distribution


## See also

* [](https://class.coursera.org/pgm-003/lecture)