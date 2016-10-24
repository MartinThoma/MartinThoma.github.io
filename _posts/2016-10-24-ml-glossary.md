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
    <dt><dfn id="curse-of-dimensionality">Curse of dimensionality</dfn></dt>
    <dd>Various problems of high-dimensional spaces that do not occur in low-dimensional spaces.
        High-dimensional often means several 100 dimensions. See also: <a href="https://martin-thoma.com/average-distance-of-points">Average Distance of Points</a></dd>
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
    <dt><dfn id="feature-map">Feature Map</dfn></dt>
    <dd>A feature map is the result of a single filter of a convolutional layer
        being applied. So it is the activation of that filter over the given
        input.</dd>
    <dt><dfn id="generative-model">Generative model</dfn></dt>
    <dd>The model gives the relationship of variables: $P(x, y)$.
        This kind of model can be used for prediction, too.</dd>
    <dt><dfn id="gradient-descent">Gradient Descent</dfn></dt>
    <dd>An iterative optimization algorithm for differentiable functions.</dd>
    <dt><dfn id="object-recognition">Object recognition</dfn></dt>
    <dd>Classification on images.</dd>
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