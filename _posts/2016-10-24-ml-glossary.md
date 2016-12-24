---
layout: post
title: Machine Learning Glossary
slug: ml-glossary
author: Martin Thoma
date: 2016-10-24 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/ml.png
---
The following is a list of short explanations of different terms in machine
learning. The aim is to keep things simple and brief, not to explain the terms
in full detail.

<dl>
    <dt><dfn id="backpropagation">Backpropagation</dfn></dt>
    <dd>A clever implementation of gradient descent for neural networks.</dd>
    <dt><dfn id="bilstm">BiLSTM</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn id="computer-vision">Computer Vision</dfn></dt>
    <dd>The academic discipline which deals with how to gain high-level understanding from digital images or videos. Common tasks include image classifiction, semantic segmentation, detection and localization.</dd>
    <dt><dfn id="curriculum-learning">Curriculum learning</dfn></dt>
    <dd>A method for pretraining. First optimize a smoothed objective and gradually consider less smoothing. So a curriculum is a sequence of training criteria. One might show gradually more diff<dt><dfn id="dcgan">DCGAN</dfn> (<dfn>DC Generative Adverserial Networks</dfn>)</dt>
    <dd>TODO</dd>icult training examples. See <a href="http://ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf">Curriculum Learning</a> by Benigo, Louradour, Collobert and Weston for details.</dd>
    <dt><dfn id="curse-of-dimensionality">Curse of dimensionality</dfn></dt>
    <dd>Various problems of high-dimensional spaces that do not occur in low-dimensional spaces.
        High-dimensional often means several 100 dimensions. See also: <a href="https://martin-thoma.com/average-distance-of-points">Average Distance of Points</a></dd>
    <dt><dfn id="dcgan">DCGAN</dfn> (<dfn>DC Generative Adverserial Networks</dfn>)</dt>
    <dd>TODO</dd>
    <dt><dfn id="dcign">DCIGN</dfn></dt>
    <dd>Deep Convolutional Inverse Graphic Network: TODO</dd>
    <dt><dfn id="object-detection">Detection in Computer Vision</dfn> (<dfn>Object detection</dfn>)</dt>
    <dd>Object detection in an image is a computer vision task. The input
        is an image and the output is a list with rectangles which contain
        objects of the given type. Face detection is one well-studied example.
        A photo could contain no face or hundrets of them. The rectangles
        can overlap.</dd>
    <dt><dfn id="discriminative-model">Discriminative Model</dfn></dt>
    <dd>The model gives a conditional probability of the classes $k$, given the
        feature vector $x$: $P(k | x)$.
        This kind of model is often used for prediction.</dd>
    <dt><dfn id="fc7-features">FC7-Features</dfn></dt>
    <dd>Features of an image which was run through a trained neural network.
        AlexNet called the last fully connected layer FC7. However, FC7
        features are not necessarily created by AlexNet.</dd>
    <dt><dfn id="feature-map">Feature Map</dfn></dt>
    <dd>A feature map is the result of a single filter of a convolutional layer
        being applied. So it is the activation of that filter over the given
        input.</dd>
    <dt><dfn id="gemm">GEMM</dfn> (<dfn>GEneral Matrix to Matrix Multiplication</dfn>)</dt>
    <dd>General Matrix to Matrix Multiplication is the problem of
        calculating the result of $C = A \cdot B$ with $A \in \mathbb{R}^{n \times m}, B \in \mathbb{R}^{m \times k}, C \in \mathbb{R}^{n \times k}$.</dd>
    <dt><dfn id="generative-model">Generative model</dfn></dt>
    <dd>The model gives the relationship of variables: $P(x, y)$.
        This kind of model can be used for prediction, too.</dd>
    <dt><dfn id="gradient-descent">Gradient Descent</dfn></dt>
    <dd>An iterative optimization algorithm for differentiable functions.</dd>
    <dt><dfn id="machine-vision">Machine Vision</dfn></dt>
    <dd>Computer vision applied for industrial applications.</dd>
    <dt><dfn id="mmd">MMD</dfn> (<dfn id="maximum-mean-descripancy">Maximum Mean Descrepancy</dfn>)</dt>
    <dd>MMD is a measure of the difference between a distribution $P$ and a distribution $Q$:

        $$MMD(F, p, q) = sup_{f \in F} (\mathbb{E}_{x \sim p} [f(x)] - \mathbb{E}_{y \sim q} [f(y)])$$

    </dd>
    <dt><dfn id="object-recognition">Object recognition</dfn></dt>
    <dd>Classification on images. The task is to decide in which class a given
        image falls, judging by the content. This can be cat, dog, plane or
        similar.</dd>
    <dt><dfn id="one-shot-learning"><a href="https://en.wikipedia.org/wiki/One-shot_learning">One-Shot learning</a></dfn></dt>
    <dd>Learn only with one or very few examples per class. See <a href="http://vision.stanford.edu/documents/Fei-FeiFergusPerona2006.pdf">One-Shot Learning of Object Categories</a>.</dd>
    <dt><dfn id="regularization">Regularization</dfn></dt>
    <dd>Regularization are techniques to make the fitted function smoother. This
        helps to prefent overfitting.<br/>
        Examples: L1, L2, Dropout, Weight Decay in Neural Networks. Parameter $C$ in SVMs.</dd>
    <dt><dfn id="semi-supervised-learning">Semi-supervised learning</dfn></dt>
    <dd>Some training data has labels, but most has no labels.</dd>
    <dt><dfn id="supervised-learning">Supervised learning</dfn></dt>
    <dd>All training data has labels.</dd>
    <dt><dfn id="spatial-pyramid-pooling">Spatial Pyramid Pooling</dfn> (<dfn>SPP</dfn>)</dt>
    <dd>SPP is the idea of dividing the image into a grid with a fixed number
        of cells and a variable size, depending on the input. Each cell computes
        one feature and hence leads to a fixed-size representation of a variable-sized
        input.<br/>
        See <a href="https://arxiv.org/abs/1406.4729v4">paper</a> and <a href="http://www.shortscience.org/paper?bibtexKey=journals/corr/1406.4729">summary</a></dd>
    <dt><dfn id="unsupervised-learning">Unsupervised learning</dfn></dt>
    <dd>No training data has labels.</dd>
    <dt><dfn id="zero-shot-learning">Zero-Shot learning</dfn></dt>
    <dd>Learning to predict classes, of which no example has been seen during
        training. For example, Flicker gets several new tags each day and they
        want to predict tags for new images. One idea is to use WordNet and
        ImageNet to generate a common embedding. This way, new words of WordNet
        could already have an embedding and thus new images categories could also automatically be classified the right way. See <a href="http://www.cs.cmu.edu/afs/cs/project/theo-73/www/papers/zero-shot-learning.pdf">Zero-Shot Learning with Semantic Output Codes</a> as well as <a href="https://www.youtube.com/watch?v=Pmv5JHKX2y4">this YouTube video</a>.</dd>
</dl>


## See also

* Lectures:
    * [Analysetechniken großer Datenbestände](https://martin-thoma.com/analysetechniken-grosser-datenbestaende/)
    * [Informationsfusion](https://martin-thoma.com/informationsfusion/)
    * [Machine Learning 1](https://martin-thoma.com/machine-learning-1-course/)
    * [Machine Learning 2](https://martin-thoma.com/machine-learning-2-course/)
    * [Mustererkennung](https://martin-thoma.com/mustererkennung-klausur/)
    * [Neuronale Netze](https://martin-thoma.com/neuronale-netze-vorlesung/)
    * [Lokalisierung Mobiler Agenten](https://martin-thoma.com/lma/)
    * [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/)
* [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)
* [scholarpedia](http://www.scholarpedia.org/)
* Other
    * [alumni.media.mit.edu](http://alumni.media.mit.edu/~tpminka/statlearn/glossary/)
    * [robotics.stanford.edu](http://robotics.stanford.edu/~ronnyk/glossary.html)
    * [ee.columbia.edu](http://www.ee.columbia.edu/~vittorio/Glossary.pdf)
    * [The Machine Learning Dictionary](http://www.cse.unsw.edu.au/~billw/mldict.html)
    * [37steps.com](http://37steps.com/glossary/)
    * [asimovinstitute.org](http://www.asimovinstitute.org/neural-network-zoo/): The Neural Network Zoo