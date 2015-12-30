---
layout: post
title: Conditional Random Fields
author: Martin Thoma
date: 2014-11-22 17:19
category: Machine Learning
tags:
- Machine Learning
- CRF
- Dynamic Programming
featured_image: logos/ai.png
---

## Videos

The following video series of
[Hugo&nbsp;Larochelle](http://www.dmi.usherb.ca/~larocheh/index_en.html) shows
quite well and step-by-step what CRFs are.

### Part 1: Motivation

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/GF3iSJkgPbA" frameborder="0" allowfullscreen></iframe>


### Part 2: Linear Chain CRF

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/PGBlyKtfB74" frameborder="0" allowfullscreen></iframe>


### Part 3: Context Window

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/G4lnHc2M1CA" frameborder="0" allowfullscreen></iframe>

<dl>
    <dt><dfn>Context Window</dfn></dt>
    <dd>The context window contains all information at a given position that
        influence the preference of different labels.</dd>
    <dt><dfn>unary log factors</dfn></dt>
    <dd>The unary log factors \(a_u (y_k)\) express a preference of the value
        of \(y\) at the position of \(k\) only. (The \(u\) is for unary.)</dd>
</dl>

### Part 4: Computing the Partition Function

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/fGdXkVv1qNQ" frameborder="0" allowfullscreen></iframe>

The partition function is the normalization term which is the sum of the
activations of all possible sequences (called \(Z(X)\) in his videos).

Computing \(p(y | X)\) is in \(\mathcal{O}(k c^2)\) where \(c\) is the number
of classes and \(k\) is the length of the sequence.

The following algorihtms were covered:

* Forward Algorithm (a dynamic programming algorithm)
* Backward Algorithm (similar to Forward Algorithm)


### Part 5: Computing Marginals

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/hjkwp-eDwt8" frameborder="0" allowfullscreen></iframe>


### Part 6: Performing Classification

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/pQJvX9U-MyE" frameborder="0" allowfullscreen></iframe>

This seems to be the Viterbi decoding algorithm.

Computing \(\max_{y^*} p(y^* | X)\) (hence making a prediction) is in
\(\mathcal{O}(k c^2)\) where \(c\) is the number of classes and \(k\) is the
length of the sequence.


### Part 7: Factors, Sufficient Statistics and TODO

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/uXV2an9TdJY" frameborder="0" allowfullscreen></iframe>


### Part 8: Markov Network

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/ZYUnyyVgtyA" frameborder="0" allowfullscreen></iframe>


### Part 9: Factor Graph

<iframe width="512" height="384" src="https://www.youtube-nocookie.com/embed/Q5GTCHVsHXY" frameborder="0" allowfullscreen></iframe>


### Part 10: Belief Propagation

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/-z5lKPHcumo" frameborder="0" allowfullscreen></iframe>

<dl>
    <dt><dfn>Belief Propagation</dfn></dt>
    <dd>A general algorithm for performing inference in general conditional
        random fields. It is a message passing algorithm</dd>
</dl>



## Additional Material

* [Wikipedia](https://en.wikipedia.org/wiki/Conditional_random_field)
* [Complete Course of Hugo Larochelle](https://www.youtube.com/playlist?list=PL6Xpj9I5qXYEcOhn7TqghAJ6NAPrNmUBH)
* Papers
    * [Conditional Random Fields as Recurrent Neural Networks](http://arxiv.org/pdf/1502.03240.pdf)