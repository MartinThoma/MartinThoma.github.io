---
layout: post
title: Using SVMs with sklearn
slug: svm-with-sklearn
author: Martin Thoma
date: 2016-01-14 12:25
category: Machine Learning
tags: Python, Machine Learning, SVM, Classification, sklearn
featured_image: logos/ai.png
---

Support Vector Machines (SVMs) is a group of powerful classifiers. In this
article, I will give a short impression of how they work. I continue
with an example how to use SVMs with sklearn.


## SVM theory

<abbr title="Support Vector Machines">SVMs</abbr> can be described with
5&nbsp;ideas in mind:

<ol>
    <li><b>Linear, binary classifiers</b>: If data is linearly separable, it
        can be separated by a hyperplane. There is one hyperplane which
        maximizes the distance to the next datapoints (support vectors). This
        hyperplane should be taken:<br/>
        <div>
          $$
          \begin{aligned}
              \text{minimize}_{\mathbf{w}, b}\,&\frac{1}{2} \|\mathbf{w}\|^2\\
              \text{s.t. }& \forall_{i=1}^m y_i \cdot \underbrace{(\langle \mathbf{w}, \mathbf{x}_i\rangle + b)}_{\text{Classification}} \geq 1
          \end{aligned}$$</div></li>
    <li><b>Slack variables</b>: Even if the underlying process which generates
          the features for the two classes is linearly separable, noise can
          make the data not separable. The introduction of <i>slack&nbsp;variables</i>
          to relax the requirement of linear separability solves
          this problem. The trade-off between accepting some errors and a more
          complex model is weighted by a parameter $C \in \mathbb{R}_0^+$. The
          bigger $C$, the more errors are accepted. The new optimization
          problem is:
          $$
          \begin{aligned}
              \text{minimize}_{\mathbf{w}, b}\,&\frac{1}{2} \|\mathbf{w}\|^2 + C \cdot \sum_{i=1}^m \xi_i\\
              \text{s.t. }& \forall_{i=1}^m y_i \cdot (\langle \mathbf{w}, \mathbf{x}_i\rangle + b) \geq 1 - \xi_i
          \end{aligned}$$

          Note that $0 \le \xi_i \le 1$ means that the data point is within
          the margin, whereas $\xi_i \ge 1$ means it is misclassified. An
          SVM with $C > 0$ is also called a <i>soft-margin SVM</i>.</li>
    <li><b>Dual Problem</b>: The primal problem is to find the normal vector $\mathbf{w}$ and the
          bias $b$. The dual problem is to express $\mathbf{w}$ as a linear
          combination of the training data $\mathbf{x}_i$:
          $$\mathbf{w} = \sum_{i=1}^m \alpha_i y_i \mathbf{x}_i$$
          where $y_i \in \{-1, 1\}$ represents the class of the training
          example and $\alpha_i$ are Lagrange multipliers. The usage of
          Lagrange multipliers is explained with some examples
          in [<a href="#ref-smi04" name="ref-smi04-anchor">Smi04</a>]. The usage of the Lagrange multipliers
          $\alpha_i$ changes the optimization problem depend on the
          $\alpha_i$ which are weights for the feature vectors. It turns
          out that most $\alpha_i$ will be zero. The non-zero weighted vectors
          are called <i>support&nbsp;vectors</i>.

          The optimization problem is now, according to [<a href="#ref-bur98" name="ref-bur98-anchor">Bur98</a>] (a great read; if you really want to understand it I can recommend it!):
          $$
          \begin{aligned}
              \text{maximize}_{\alpha_i}\,& \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle\\
              \text{s.t. } & \forall_{i=1}^m 0 \leq \alpha_i \leq C\\
              \text{s.t. } & \sum_{i=1}^m \alpha_i y_i = 0
          \end{aligned}$$</li>
    <li><b>Kernel-Trick</b>: Not every dataset is linearly separable. This problem is approached
          by transforming the feature vectors $\mathbf{x}$ with a non-linear
          mapping $\Phi$ into a higher dimensional (probably
          $\infty$-dimensional) space. As the feature vectors $\mathbf{x}$
          are only used within scalar product
          $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$, it is not necessary to
          do the transformation. It is enough to do the calculation
          $$K(\mathbf{x}_i, \mathbf{x}_j) = \langle \mathbf{x}_i, \mathbf{x}_j \rangle$$

          This function $K$ is called a <i>kernel</i>. The idea of never
          explicitly transforming the vectors $\mathbf{x}_i$ to the higher
          dimensional space is called the <i>kernel&nbsp;trick</i>. Common kernels
          include the polynomial kernel
          $$K_P(\mathbf{x}_i, \mathbf{x}_j) = (\langle \mathbf{x}_i, \mathbf{x}_j \rangle + r)^p$$
          of degree $p$ and coefficient $r$, the Gaussian <abbr title="Radial Basis Function">RBF</abbr> kernel
          $$K_{\text{Gauss}}(\mathbf{x}_i, \mathbf{x}_j) = e^{\frac{-\gamma\|\mathbf{x}_i - \mathbf{x}_j\|^2}{2 \sigma^2}}$$
          and the sigmoid kernel
          $$K_{\text{tanh}}(\mathbf{x}_i, \mathbf{x}_j) = \tanh(\gamma \langle \mathbf{x}_i, \mathbf{x}_j \rangle - r)$$
          where the parameter $\gamma$ determines how much influence single
          training examples have.</li>
    <li><b>Multiple Classes</b>: By using the <i>one-vs-all</i> or the
        <i>one-vs-one</i> strategy it is possible to get a classifying system
        which can distinguish many classes.</li>
</ol>

A nice visualization of the transformation of the data in a higher-dimensional
space was done by

TeamGrizzly's channel: [Performing nonlinear classification via linear separation in higher dimensional space](https://youtu.be/9NrALgHFwTo) on YouTube. 22.11.2010.

See also:

* [What is an example of a SVM kernel, where one implicitly uses an infinity-dimensional space?](http://math.stackexchange.com/a/1620256/6876)
* [SVM - hard or soft margins?](http://stackoverflow.com/a/4630731/562769)


## sklearn

`sklearn` is the machine learning toolkit to get started for Python. It has
a very good documentation and many functions. You can find [installation
instructions](http://scikit-learn.org/stable/install.html) on their website.

It also includes [`sklearn.svm.SVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC).
SVC is short for *support vector classifier* and this is how you use it for
the MNIST dataset.

Parameters for which you might want a further explanation:

* `cache_size`: [datascience.stackexchange.com](http://datascience.stackexchange.com/a/996/8820)


```python
#!/usr/bin/env python

"""
Train a SVM to categorize 28x28 pixel images into digits (MNIST dataset).
"""

import numpy as np


def main():
    """Orchestrate the retrival of data, training and testing."""
    data = get_data()

    # Get classifier
    from sklearn.svm import SVC

    clf = SVC(probability=False, kernel="rbf", C=2.8, gamma=0.0073)  # cache_size=200,

    print("Start fitting. This may take a while")

    # take all of it - make that number lower for experiments
    examples = len(data["train"]["X"])
    clf.fit(data["train"]["X"][:examples], data["train"]["y"][:examples])

    analyze(clf, data)


def analyze(clf, data):
    """
    Analyze how well a classifier performs on data.

    Parameters
    ----------
    clf : classifier object
    data : dict
    """
    # Get confusion matrix
    from sklearn import metrics

    predicted = clf.predict(data["test"]["X"])
    print(
        "Confusion matrix:\n%s" % metrics.confusion_matrix(data["test"]["y"], predicted)
    )
    print("Accuracy: %0.4f" % metrics.accuracy_score(data["test"]["y"], predicted))

    # Print example
    try_id = 1
    out = clf.predict(data["test"]["X"][try_id])  # clf.predict_proba
    print("out: %s" % out)
    size = int(len(data["test"]["X"][try_id]) ** (0.5))
    view_image(
        data["test"]["X"][try_id].reshape((size, size)), data["test"]["y"][try_id]
    )


def view_image(image, label=""):
    """
    View a single image.

    Parameters
    ----------
    image : numpy array
        Make sure this is of the shape you want.
    label : str
    """
    from matplotlib.pyplot import show, imshow, cm

    print("Label: %s" % label)
    imshow(image, cmap=cm.gray)
    show()


def get_data():
    """
    Get data ready to learn with.

    Returns
    -------
    dict
    """
    simple = False
    if simple:  # Load the simple, but similar digits dataset
        from sklearn.datasets import load_digits
        from sklearn.utils import shuffle

        digits = load_digits()
        x = [np.array(el).flatten() for el in digits.images]
        y = digits.target

        # Scale data to [-1, 1] - This is of mayor importance!!!
        # In this case, I know the range and thus I can (and should) scale
        # manually. However, this might not always be the case.
        # Then try sklearn.preprocessing.MinMaxScaler or
        # sklearn.preprocessing.StandardScaler
        x = x / 255.0 * 2 - 1

        x, y = shuffle(x, y, random_state=0)

        from sklearn.cross_validation import train_test_split

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.33, random_state=42
        )
        data = {
            "train": {"X": x_train, "y": y_train},
            "test": {"X": x_test, "y": y_test},
        }
    else:  # Load the original dataset
        from sklearn.datasets import fetch_mldata
        from sklearn.utils import shuffle

        mnist = fetch_mldata("MNIST original")

        x = mnist.data
        y = mnist.target

        # Scale data to [-1, 1] - This is of mayor importance!!!
        x = x / 255.0 * 2 - 1

        x, y = shuffle(x, y, random_state=0)

        from sklearn.cross_validation import train_test_split

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.33, random_state=42
        )
        data = {
            "train": {"X": x_train, "y": y_train},
            "test": {"X": x_test, "y": y_test},
        }
    return data


if __name__ == "__main__":
    main()
```


## Results

The script from above gives the following results:

<table>
    <caption>Confusion matrix for an SVM classifier on the MNIST dataset</caption>
    <thead>
    <tr>
        <th></th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th>0</th>
        <td>2258</td>
        <td>1</td>
        <td>4</td>
        <td>1</td>
        <td>2</td>
        <td>2</td>
        <td>3</td>
        <td>1</td>
        <td>4</td>
        <td>2</td>
    </tr>
    <tr>
        <th>1</th>
        <td>1</td>
        <td>2566</td>
        <td>9</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>7</td>
        <td>3</td>
        <td>0</td>
    </tr>
    <tr>
        <th>2</th>
        <td>4</td>
        <td>1</td>
        <td>2280</td>
        <td>5</td>
        <td>4</td>
        <td>0</td>
        <td>1</td>
        <td>9</td>
        <td>8</td>
        <td>2</td>
    </tr>
    <tr>
        <th>3</th>
        <td>0</td>
        <td>0</td>
        <td>14</td>
        <td>2304</td>
        <td>1</td>
        <td>13</td>
        <td>0</td>
        <td>6</td>
        <td>8</td>
        <td>2</td>
    </tr>
    <tr>
        <th>4</th>
        <td>2</td>
        <td>2</td>
        <td>2</td>
        <td>0</td>
        <td>2183</td>
        <td>0</td>
        <td>7</td>
        <td>5</td>
        <td>0</td>
        <td>10</td>
    </tr>
    <tr>
        <th>5</th>
        <td>4</td>
        <td>0</td>
        <td>0</td>
        <td>16</td>
        <td>3</td>
        <td>2026</td>
        <td>12</td>
        <td>1</td>
        <td>4</td>
        <td>3</td>
    </tr>
    <tr>
        <th>6</th>
        <td>7</td>
        <td>5</td>
        <td>3</td>
        <td>0</td>
        <td>5</td>
        <td>2</td>
        <td>2245</td>
        <td>0</td>
        <td>4</td>
        <td>0</td>
    </tr>
    <tr>
        <th>7</th>
        <td>1</td>
        <td>6</td>
        <td>11</td>
        <td>2</td>
        <td>5</td>
        <td>1</td>
        <td>0</td>
        <td>2373</td>
        <td>5</td>
        <td>13</td>
    </tr>
    <tr>
        <th>8</th>
        <td>3</td>
        <td>9</td>
        <td>4</td>
        <td>9</td>
        <td>4</td>
        <td>10</td>
        <td>2</td>
        <td>3</td>
        <td>2166</td>
        <td>5</td>
    </tr>
    <tr>
        <th>9</th>
        <td>3</td>
        <td>2</td>
        <td>2</td>
        <td>6</td>
        <td>19</td>
        <td>6</td>
        <td>0</td>
        <td>12</td>
        <td>10</td>
        <td>2329</td>
    </tr>
    </tbody>
</table>

* Accuracy: 98.40%
* Error: 1.60%

Looks pretty good to me. However, note that there are much better results.
The best on [the official website](http://yann.lecun.com/exdb/mnist/) has an
error of 0.23% and is a committee of 35 convolutional neural networks.

The best SVM I could find has an error of 0.56% and applies a polynomial kernel
of degree&nbsp;9 as well as some preprocessing.


## References

* [<a href="#ref-smi04-anchor" name="ref-smi04">Smi04</a>] B. T. Smith, “Lagrange multipliers tutorial in the context of support
  vector machines,” Memorial University of Newfoundland St. John’s,
  Newfoundland, Canada, Jun. 2004.
* [<a href="#ref-bur98-anchor" name="ref-bur98">Bur98</a>] C. J. Burges, “[A tutorial on support vector machines for pattern recognition](http://research.microsoft.com/pubs/67119/svmtutorial.pdf)”, Data&nbsp;mining and knowledge discovery, vol. 2, no. 2, pp.
  121–167, 1998.


## See also

* [Recognizing hand-written digits](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)
* Trung Huynh's tech blog: [Digit Recognition using SVM in Python](http://www.trungh.com/2013/04/digit-recognition-using-svm-in-python/)
* [Classifier comparison](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)
* [Supervised learning](http://scikit-learn.org/stable/supervised_learning.html)
* [How can SVM 'find' an infinite feature space where linear separation is always possible?](http://stats.stackexchange.com/questions/80398/how-can-svm-find-an-infinite-feature-space-where-linear-separation-is-always-p)
