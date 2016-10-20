---
layout: post
title: Average Distance of Random Points in a Unit Hypercube
slug: average-distance-of-points
author: Martin Thoma
date: 2016-10-20 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/ml.png
---
In machine learning, the "curse of dimensionality" is often stated but much
less often explained. At least not in detail. One just gets told that points
are farer away from each other in high dimensional spaces.


## Maximum minimal distance

One approach to this is to calculate the maximum minimal distance of $k$ points
in $[0, 1]^n$. So you try to place $k$ points in such a way, that the minimum
over the pairwise distances of those $k$ points is maximal.
Let's call this $\alpha(n, k)$. However, it is not easily possible
to calculate $\alpha(n, k)$ for arbitrary $n > 2$ and $k > 2$ (see [link](http://math.stackexchange.com/q/1976250/6876)).
But the special case $k = 2$ and $k = 2^n$ is easy:

* $\alpha(n, 2) = \sqrt{n}$
* $\alpha(n, 2^n) = 1$

So you can see that two points get can be farer apart in higher dimensions and
that it needs much more points in higher dimensions to force at least two of
them to have distance 1.


## Average distance

Another approach is to calculate the average distance of $k$ uniformly randomly
sampled points in $[0, 1]^n$. Let's call it $\beta(n, k)$.

One first insight is that $\beta(n, k) = \beta(n, j)$ for and $k, j \geq 2$.
Hence we will only use $\beta(n)$ in the following.

It is possible to
calculate this, but it is rather tedious ([link](http://math.stackexchange.com/a/1254154/6876)).

Just two calculated solutions for $k=2$ points:

* $\beta(1) = \frac{1}{3}$
* $\beta(2) = \frac{2+\sqrt{2}+5\operatorname{arcsinh}(1)}{15}=\frac{2+\sqrt{2}+5\log(1+\sqrt{2})}{15} \approx 0.52140543316472\ldots$

However, it is pretty easy to simulate it.


## Empirical results

```python
#!/usr/bin/env python

"""
Get the empirical statements about the distance of two points in [0, 1]^n.

The points are uniformly randomly sampled.
"""

import numpy.random


def random_points_dist(n):
    """Get the distance of one sample of 2 points in [0, 1]^n."""
    assert n >= 1
    points = []
    for _ in range(2):
        p = numpy.random.rand(n)
        points.append(p)
    return numpy.linalg.norm(points[0] - points[1])


def beta(n):
    """Calculate the average distance of 2 points in [0, 1]^n."""
    sum_ = 0.0
    count_ = 10**6
    less_one = 0
    max_d = 0
    for _ in range(count_):
        dist = random_points_dist(n)
        if dist < 1.0:
            less_one += 1
        max_d = max(max_d, dist)
        sum_ += dist
    return (sum_ / count_, float(less_one) / count_, max_d)


for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000]:
    avg_dist, pr, max_d = beta(n)
    tmp = ("beta(n=%i) = %0.4f; " % (n, avg_dist))
    print("%s Pr(d(p1, p2) < 1) = %0.4f; alpha(n=%i, 2) = %0.4f" %
          (tmp, pr, n, max_d))

```

One can easily see that points get spaced much farer away in average the higher
the dimension $n$ is. Now lets try to calculate the probability that two points
in the unit hypercube have a distance of less than 1.


Here are a couple of results:

<table>
    <tr>
        <th>n</th>
        <th>$\alpha(n, 2)$</th>
        <th>$\beta(n)$</th>
        <th>$Pr(d(p_1, p_2) &lt; 1)$</th>
    </tr>
    <tr>
        <td style="text-align: right;">1</td>
        <td>0.9994</td>
        <td>0.3332</td>
        <td>1.0000</td>
    </tr>
    <tr>
        <td style="text-align: right;">2</td>
        <td>1.3797</td>
        <td>0.5211</td>
        <td>0.9749</td>
    </tr>
    <tr>
        <td style="text-align: right;">3</td>
        <td>1.6116</td>
        <td>0.6616</td>
        <td>0.9100</td>
    </tr>
    <tr>
        <td style="text-align: right;">4</td>
        <td>1.8130</td>
        <td>0.7776</td>
        <td>0.8066</td>
    </tr>
    <tr>
        <td style="text-align: right;">5</td>
        <td>1.8645</td>
        <td>0.8786</td>
        <td>0.6787</td>
    </tr>
    <tr>
        <td style="text-align: right;">6</td>
        <td>1.9659</td>
        <td>0.9693</td>
        <td>0.5419</td>
    </tr>
    <tr>
        <td style="text-align: right;">7</td>
        <td>2.0891</td>
        <td>1.0515</td>
        <td>0.4125</td>
    </tr>
    <tr>
        <td style="text-align: right;">8</td>
        <td>2.1513</td>
        <td>1.1280</td>
        <td>0.3006</td>
    </tr>
    <tr>
        <td style="text-align: right;">9</td>
        <td>2.2888</td>
        <td>1.2002</td>
        <td>0.2096</td>
    </tr>
    <tr>
        <td style="text-align: right;">10</td>
        <td>2.3327</td>
        <td>1.2671</td>
        <td>0.1411</td>
    </tr>
    <tr>
        <td style="text-align: right;">100</td>
        <td>5.2152</td>
        <td>4.0753</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td style="text-align: right;">1000</td>
        <td>14.0719</td>
        <td>12.9073</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td style="text-align: right;">10000</td>
        <td>41.9675</td>
        <td>40.8245</td>
        <td>0.0000</td>
    </tr>
</table>

You can easily see that the average distance of two points gets less and less
different from the maximal distance of two points.


## See also

* [The Concentration of Fractional Distances](https://perso.uclouvain.be/michel.verleysen/papers/tkde07df.pdf)
* [How is the distance of two random points in a unit hypercube distributed?](http://math.stackexchange.com/q/1976842/6876)
* [Curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
