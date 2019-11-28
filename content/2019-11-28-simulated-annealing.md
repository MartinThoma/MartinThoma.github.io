---
layout: post
title: Simulated Annealing
slug: simulated-annealing
author: Martin Thoma
date: 2019-11-28 20:00
category: Code
tags: Data Science
featured_image: logos/star.png
---
<div class="info">This article is not quite finished, but I recently wanted to share some ideas.</div>
Simulated Annealing is an optimization algorithm. It is well-suited for
combinatoric problems.


## Confusion Matrix Ordering

A confusion matrix contains the predictions of a classifier together with their
ground truth. The cell $(i, j)$ gives the information how often class $i$ was
predicted to be class $j$. So the diagonal $i=j$ contains the number of samples
where the classifier got it right.

In this matrix, the order of classes is irrelevant. You can change it. So
instead of the order [mouse, cat, dog] you can have [cat, dog, mouse]. But for
big matrices it might be interesting to get some more structure. For example,
you might want to push the high elements close to the diagonal. This way,
you can easier see the errors. An awesome side-effect is that classes which look
similar to the classifier are closer together in the list.

Changing the order of the classes can itself be seen as an optimization problem.
For example, a matrix can be scored with

$$E(C) = \sum_{i=1}^n \sum_{j=1}^n (i - j)^2$$

I've described the details in [Analysis and Optimization of Convolutional Neural Network Architectures, Chapter 5.2](https://arxiv.org/pdf/1707.09725.pdf).

The simplest way to approach this problem is:

```
def optimize_brute_force(c, steps=1000):
    # initialize
    best_permutation = [i for i in range(len(c))]
    best_score = calculate_score(best_permutation)

    for _ in range(steps):
        # Create new candidate
        permutation = [i for i in range(len(c))]
        random.shuffle(permutation)

        # Score candidate
        score = calculate_score(permutation)

        # Replace if it improved
        if score < best_score:
            best_score = score
            best_permutation = permutation
    return best_permutation
```

Now, this is super inefficient. The reason is that the matrix has
sub-structures which you destroy all the time. Instead of creating complete new
permutations, you could simply swap two elements of the best permutation so
far:

```
def optimize_greedy_swap(c, steps=1000):
    # initialize
    best_permutation = [i for i in range(len(c))]
    best_score = calculate_score(best_permutation)

    for _ in range(steps):
        # Create new candidate
        i, j = random.sample(best_permutation, 2)
        permutation = swap(copy(best_permutation), i, j)

        # Score candidate
        score = calculate_score(permutation)

        # Replace if it improved
        if score < best_score:
            best_score = score
            best_permutation = permutation
    return best_permutation
```

But this is still not good. This problem is of a structure that can lead to
local optima, where a single swap does not improve anything, but only two or
more swaps can. To fix this, one should allow at least equal solutions to change
the currently stored one. So if two solutions $s_1, s_2$ both have a score of
3141, then the `best_solution` should be allowed to switch between the two.

You will quickly figure out that this is not enough. You need to allow the
algorithm to make the solution temporarily worse. Still, you want to improve
overall. To weight this against each other we have simulated annealing.

To understand the idea, think about cooling metal. There are some constraints
on how the atoms can be arranged and what is engergetically preferable / more
stable. And while the metal is cooling, the atoms move less. To jump to a more
stable setting, the setting has to be closer to the current setting.

In the algorithm, you could say that making the score worse (e.g. from 1234 to
3141), you have to be at the beginning of the optimization process. Some steps
later, it might only be possible to make it worse from 1234 to 1300. Even later
maybe only to 1250. And in the end it has to be strictly better.

How does that look in code?

```
def optimize_greedy_swap(c,
                         steps=1000,
                         temperature=1000,
                         cooling_factor=0.995):
    # initialize
    best_permutation = [i for i in range(len(c))]
    best_score = calculate_score(best_permutation)

    for _ in range(steps):
        # Create new candidate
        i, j = random.sample(best_permutation, 2)
        permutation = swap(copy(best_permutation), i, j)

        # Score candidate
        score = calculate_score(permutation)

        # Replace if it improved
        is_better = score < best_score
        prob = exp(- (score - best_score) / temperature)
        is_hot_enough = prob > random.random()
        if is_better or is_hot_enough:
            best_score = score
            best_permutation = permutation
        temperature *= cooling_factor
    return best_permutation
```

For this specific problem, I noticed that the temperature-trick was way less
important than allowing to swap blocks. So once in a while, I don't swap single
elements but move a whole range.
