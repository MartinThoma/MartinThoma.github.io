---
layout: post
title: Python Markov Chain Packages
author: Martin Thoma
date: 2015-05-12 20:45
category: Code
tags: Python, Markov Chain
featured_image: logos/python.png
---
Markov Chains are probabilistic processes which depend only on the previous
state and not on the complete history. One common example is a very simple
weather model: Either it is a rainy day (R) or a sunny day (S). On sunny days
you have a probability of 0.8 that the next day will be sunny, too. On rainy
days you have a probability of 0.6 that the next day will be rainy, too.
As you have only two possible weather conditions, the probability that it
changes from sunny do rainy is 0.2 and vice versa it is 0.4.

You can visualize this with a graph like this:

<figure class="aligncenter">
            <a href="../images/2015/05/markov-chain-rain-sun.png"><img src="../images/2015/05/markov-chain-rain-sun.png" alt="Simple Markov chain weather model" style="max-width:500px;" class=""/></a>
            <figcaption class="text-center">Simple Markov chain weather model</figcaption>
        </figure>

I am taking a course about markov chains this semester. Today, we've learned
a bit how to use R (a programming language) to do very basic tasks.


## R vs Python

The following will show some R code and then some Python code for the same
basic tasks. As an example, I'll use reproduction. The states are
$S_1 = \{AA, AA\}$, $S_2 = \{AA, Aa\}$, $S_3 = \{AA, aa\}$, $S_4=\{Aa,Aa\}$,
$S_5 = \{Aa, aa\}$ and $S_6 = \{aa, aa\}$.

The idea is that each pair of parents give birth to two children. The parents
$S_2 = \{AA, Aa\}$ can give birth to \{\{AA, AA\}, \{AA, Aa\}, \{Aa, Aa\}\}.
This results in the following state transition matrix.

$$\begin{pmatrix}1 & 0 & 0 & 0 & 0 & 0 \\
1/4 & 1/2 & 0 & 1/4 & 0 & 0\\
0 & 0 & 0 & 1 & 0 & 0\\
1/16 & 1/4 & 1/8 & 1/4 & 1/4 & 1/16\\
0 & 0 & 0 & 1/4 & 1/2 & 1/4\\
0 & 0 & 0 & 0 & 0 & 1\end{pmatrix}$$

The rows mean from which state you start, the colums are the states you can get
to.

Now, how would you define this matrix with R?

```r
P = matrix(c(1,0,0,0,0,0, 1/4,1/2,0,1/4,0,0, 0,0,0,1,0,0, 1/16, 1/4, 1/8, 1/4, 1/4, 1/16, 0,0,0, 1/4, 1/2, 1/4, 0,0,0,0,0,1), byrow=TRUE, nrow=6)
```

And this is how you do it with Python: You first need to
[install numpy](http://docs.scipy.org/doc/numpy/user/install.html). This is
very easy with Linux (`sudo apt-get install python-numpy`), but I've heard
it is not that easy with Windows systems.

```python
import numpy as np

P = np.matrix(
    [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0 / 4, 1.0 / 2, 0.0, 1.0 / 4, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [1.0 / 16, 1.0 / 4, 1.0 / 8, 1.0 / 4, 1.0 / 4, 1.0 / 16],
        [0.0, 0.0, 0.0, 1.0 / 4, 1.0 / 2, 1.0 / 4],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    ]
)
```

A common matrix operation is taking the $n$-th power. This is how you do it
with R: First, install the library "expm" by executing `install.packages("expm")`.
Then

```r
library("expm")
n = 5
Pn = P%^%n
```

and this is the Python way:

```python
n = 5
Pn = P ** n
```

Visualizing data is a very important tool. For example, we want to know the
probabilities for the current state for the next 20 steps when you started in
$S_3$.

```r
library("expm")
P = matrix(c(1,0,0,0,0,0,
             1/4,1/2,0,1/4,0,0,
             0,0,0,1,0,0,
             1/16, 1/4, 1/8, 1/4, 1/4, 1/16,
             0,0,0, 1/4, 1/2, 1/4,
             0,0,0,0,0,1), byrow=TRUE, nrow=6)
v = c(0,0,1,0,0,0)
for (step in 1:20) {
    matplot(t(sapply(1:20,
                     function (step) {v %*% (P %^% step)})),
                     cex=0.7,
                     ylab="")
}
```

This gives the following plot:

<figure class="aligncenter">
            <a href="../images/2015/05/reproductin-rplot.png"><img src="../images/2015/05/reproductin-rplot.png" alt="State probabilities starting in S3 after 1..20 steps (plotted with R)" style="max-width:500px;" class=""/></a>
            <figcaption class="text-center">State probabilities starting in S3 after 1..20 steps (plotted with R)</figcaption>
        </figure>

The Python equivalent is

```python
#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot

P = np.matrix(
    [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0 / 4, 1.0 / 2, 0.0, 1.0 / 4, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [1.0 / 16, 1.0 / 4, 1.0 / 8, 1.0 / 4, 1.0 / 4, 1.0 / 16],
        [0.0, 0.0, 0.0, 1.0 / 4, 1.0 / 2, 1.0 / 4],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    ]
)

v = np.matrix([[0, 0, 1, 0, 0, 0]])

# Get the data
plot_data = []
for step in range(20):
    result = v * P ** step
    plot_data.append(np.array(result).flatten())

# Convert the data format
plot_data = np.array(plot_data)

# Create the plot
pyplot.figure(1)
pyplot.xlabel("Steps")
pyplot.ylabel("Probability")
lines = []
for i, shape in zip(range(6), ["x", "h", "H", "s", "8", "r+"]):
    (line,) = pyplot.plot(plot_data[:, i], shape, label="S%i" % (i + 1))
    lines.append(line)
pyplot.legend(handles=lines, loc=1)
pyplot.show()
```

The result looks like this

<figure class="aligncenter">
            <a href="../images/2015/05/reproductin-python-plot.png"><img src="../images/2015/05/reproductin-python-plot.png" alt="State probabilities starting in S3 after 1..20 steps (plotted with Python)" style="max-width:500px;" class=""/></a>
            <figcaption class="text-center">State probabilities starting in S3 after 1..20 steps (plotted with Python)</figcaption>
        </figure>

I've played around with the [matplotlib markers](http://matplotlib.org/api/markers_api.html)
to make sure all points are visible.

## Python Markov Packages

There seem to be quite a few Python Markov chain packages:

```text
$ pip search markov
PyMarkovChain             - Simple markov chain implementation
autocomplete              - tiny 'autocomplete' tool using a "hidden markov model"
cobe                      - Markov chain based text generator library and chatbot
twitter_markov            - Create markov chain ("_ebooks") accounts on Twitter
markovgen                 - Another text generator based on Markov chains.
pyEMMA                    - EMMA: Emma's Markov Model Algorithms
pymc                      - Markov Chain Monte Carlo sampling toolkit.
hmmus                     - Posterior decoding with a hidden Markov model
marbl-python              - A Python implementation of the Marbl specification for normalized representations of Markov blankets in Bayesian networks.
pymdptoolbox              - Markov Decision Process (MDP) Toolbox
gibi                      - Generate random words based on Markov chains
markovgenerator           - Markov text generator
pythonic-porin            - Nanopore Data Analysis package. Provides tools for reading data,        performing event detection, segmentation, visualization, and
                            analysis using        hidden Markov models, and other tools. Designed for the UCSC Nanopore Group.
PyMarkovTextGenerator     - Random text generator base on Markov chains.
MCREPOGEN                 - Markov Chain Repository Generator
vokram                    - A toy Markov chain implementation.
MarkovEquClasses          - Algorithms for exploring Markov equivalence classes: MCMC, size counting
hmmlearn                  - Hidden Markov Models in Python with scikit-learn like API
twarkov                   - Markov generator built for generating Tweets from timelines
MCL_Markov_Cluster        - Markov Cluster algorithm implementation
pyborg                    - Markov chain bot for irc which generates replies to messages
pydodo                    - Markov chain generator
mwordgen                  - MWordGen is a Markov statistics based word generator.
Markov                    - Python library for Hidden Markov Models
markovify                 - Use Markov chains to generate random semi-plausible sentences based on an existing text.
treehmm                   - Variational Inference for tree-structured Hidden-Markov Models
PyMarkov                  - Markov Chains made easy
```

However, most of them are for hidden markov model training / evaluation.
There seems to be no package which can visualize markov chains just by taking
the state transition matrix.

There seems also not to be any package which makes it easy to classify states
as transient / recurrent, get the absorption time, ...

If somebody is interested in that, we could make a little project for it ☺


### PyMarkovChain

Source is on [github.com/TehMillhouse/PyMarkovChain](https://github.com/TehMillhouse/PyMarkovChain).
It is less than 150 lines of code and probably no functionality.

I asked the author to remove the package from PyPI (see [issue #13](https://github.com/TehMillhouse/PyMarkovChain/issues/13)).


### pyEMMA

I've found the [documentation](http://www.pythonhosted.org/pyEMMA/) and the
[project on PyPI](https://pypi.python.org/pypi/pyEMMA). The source is
on [github.com/markovmodel/PyEMMA](https://github.com/markovmodel/PyEMMA).


### MarkovEquClasses

[PyPI](https://pypi.python.org/pypi/MarkovEquClasses/1.0)


### PyMarkov

It is only about 100 lines of very simple code. It seems to be another
random sentence generator.
See [PyPI](https://pypi.python.org/pypi/PyMarkov).


### Hidden Markov Models

The following might be interesting, but I didn't take a close look at them
because I was looking for "normal" markov models:

* hmmus
* hmmlearn
* Markov
* treehmm

There are also quite a few other modules which seem to generate data with
markov chains.
