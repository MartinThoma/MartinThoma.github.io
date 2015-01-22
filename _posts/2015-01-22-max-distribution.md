---
layout: post
title: Distribution of Random Variables when max gets applied
author: Martin Thoma
date: 2015-01-22 11:07
categories: 
- Mathematics
tags: 
- Probability Theory
- Python
- numpy
- matplotlib
featured_image: logos/mathematics.png
---

I just wanted to solve an exercise where I had random variables $X_1, \dots, X_n$
which were all $U([0, 1])$ distributed and $Y_n = \max(X_1, \dots, X_n)$.

I wondered what the distribution of $Y_n$ is (for big $n$), so I wanted to plot
it. How do I plot it? With Python, of course :-)

Here is the program:

```python
#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy.random


def main():
    # Generate Data
    n = 10000
    numbers_a = numpy.random.uniform(size=samples)
    numbers_b = numpy.random.uniform(size=samples)
    numbers_c = numpy.random.uniform(size=samples)
    numbers_max = [max(a, b, c)
                   for a, b, c in zip(numbers_a, numbers_b, numbers_c)]

    # Plot data
    plt.hist(numbers_max)
    plt.title("Histogram")
    plt.xlabel("value")
    plt.ylabel("count")
    plt.show()


if __name__ == '__main__':
    main()

```

and here is the plot for $n = 2$

{% caption align="aligncenter" width="500" alt="Plot of the maximum of 2 randomly distributed variables with 10000 samples" text="Plot of the maximum of 2 randomly distributed variables with 10000 samples" url="../images/2015/01/random-max-uniform-distribution-n-2.png" %}

If you increase to $n = 3$ you get:

{% caption align="aligncenter" width="500" alt="Plot of the maximum of 3 randomly distributed variables with 10000 samples" text="Plot of the maximum of 3 randomly distributed variables with 10000 samples" url="../images/2015/01/random-max-uniform-distribution-n-3.png" %}


## See also

* [List of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)
* [Basic Data Plotting with Matplotlib Part 3: Histograms](https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/)