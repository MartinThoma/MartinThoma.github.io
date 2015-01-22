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

and here is the plot:

{% caption align="aligncenter" width="500" alt="Plot of the maximum of 10000 randomly distributed variables" text="Plot of the maximum of 10000 randomly distributed variables" url="../images/2015/01/random-max-uniform-distribution.png" %}

It looks as if $Y_n \sim $

## See also

* [List of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)