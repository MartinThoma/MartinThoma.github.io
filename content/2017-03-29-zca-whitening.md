---
layout: post
title: ZCA Whitening
slug: zca-whitening
author: Martin Thoma
date: 2017-03-29 20:00
category: Machine Learning
tags: Computer Vision, Machine Learning
featured_image: logos/ml.png
---
Whitening is a transformation of data in such a way that its covariance matrix $\Sigma$
is the identity matrix. Hence whitening decorrelates features. It is used as a
preprocessing method.

When you have $N$ data points in $\mathbb{R}^n$, then the covariance matrix
$\Sigma \in \mathbb{R}^{n \times n}$ is estimated to be:
\[\hat{\Sigma}_{jk} = \frac{1}{N-1} \sum_{i=1}^N (x_{ij} - \bar{x}_j) \cdot (x_{ik} - \bar{x}_k)\]
where $\bar{x}_j$ denotes the $j$-th component of the estimated mean of the
samples $x$.

Any matrix $W \in \mathbb{R}^{n \times n}$ which satisfies the condition
\[W^T W = C^{-1}\]
whitens the data. <abbr title="Zero-phase Component Analysis">ZCA</abbr>
whitening is the choice $W = M^{- \frac{1}{2}}$. PCA is another choice.
According to "Neural Networks: Tricks of the Trade" PCA and ZCA whitening
differ only by a rotation.


## How to do it

When you look at the <a href="https://github.com/fchollet/keras/blob/master/keras/preprocessing/image.py#L670-L674">Keras code</a>, you can see the following:

```
# Calculate principal components
sigma = np.dot(flat_x.T, flat_x) / flat_x.shape[0]
u, s, _ = linalg.svd(sigma)
principal_components = np.dot(np.dot(u, np.diag(1. / np.sqrt(s + 10e-7))), u.T)

# Apply ZCA whitening
whitex = np.dot(flat_x, principal_components)
```

So, at first you compute the covariance matrix $\Sigma$. I'm not quite sure,
but I think they should divide by `flat_x.shape[0] - 1` for the unbiased
estimator.

Then you apply singular value decomposition to the estimated covariance matrix.
The matrix $u \in \mathbb{R}^{n \times n}$ is <a href="https://en.wikipedia.org/wiki/Unitary_matrix">unitary</a>
and $s \in \mathbb{R}^{n \times n}$ is a diagonal matrix with non-negative real numbers on the diagonal.
Those number are the <a href="https://en.wikipedia.org/wiki/Singular_value">singular values</a>
of $\Sigma$.

Next, the principal components are calculated:
\[u \cdot \frac{1}{\sqrt{s + 10^{-7}}} I \cdot u^T\]

By adding `10e-7` one prevents division by zero.

Whitening is then simply the multiplication with the principal components.

## See also

* [Optimal whitening and decorrelation](https://arxiv.org/abs/1512.00809)
