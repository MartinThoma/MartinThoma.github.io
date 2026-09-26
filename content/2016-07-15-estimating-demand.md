---
layout: post
title: Estimating Demand
slug: estimating-demand
lang: en
author: Martin Thoma
date: 2016-07-15 20:00
category: Mathematics
tags: Statistics, Mathematics
featured_image: logos/mathematics.png
---
I've just had the problem that I'm helping to plan a group event, where the
participants should all have bikes. There are 170 participants and 80 bikes.
Some of the participants might be able to bring their own bikes. So we asked
them to tell us who can't bring a bike with them. Only 79 answered. Only 7 of
them can bring their own bike.

**How many bikes should we try to organize to be 95% sure that everybody will have a bike?**


## Modelling

Let $X$ be the random variable which represents the number of people who will
not bring their own bikes. I will assume that the participants bring or bring
not their bikes independently of each other. So we have a binomial distribution:

$$X \sim Bin(n=91, p=\frac{79-7}{79})$$

The sample of $n=79$ people who answered will be called $S$. Let $b \in \mathbb{N}_0$ be our guess of the number of people of those $91$ who do not bring their bikes. The higher we estimate $b$, the more conservative we are. This means a higher certainty (e.g. 99% instead of 95%) should result in a higher $b$.

We want to be $95\%$ confident that we have enough bikes.


## The task

$$
\begin{align}
P(X \leq b) &\geq 95\%\\
\sum_{k=0}^b \binom{n}{k} p^k {(1-p)}^{n-k} &\geq 95\%\\
b &= \lceil binom.ppf(95\%, n, p) \rceil
\end{align}
$$

I am lazy with calculating, so let's do it with Python:

```python
from scipy.stats import binom

confidence = 0.95
n = 91
p = 1 - 7.0 / 79
binom.ppf(confidence, n, p)
```

This gives 87. So we assume only 4 more people will bring their own bike.
