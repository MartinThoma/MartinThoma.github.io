---
layout: post
title: Image Classification
slug: image-classification
author: Martin Thoma
date: 2017-03-15 20:00
category: Machine Learning
tags: machine learning, Computer Vision, ImageNet
featured_image: logos/ml.png
---
Image classification is the following task: You have an image and you want to
assign it one label. The set of possible labels is finite and typically not
bigger than 1000.

So for example, you might ask: What can you see in this image?

<figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2017/03/moon-jelly.jpg" alt="A jellyfish" style="width: 512px;"/>
    <figcaption class="text-center">A jellyfish</figcaption>
</figure>

It is one of the most common and probably simplest tasks in the intersection of
machine learning and computer vision. A commonly used dataset is <a href="https://en.wikipedia.org/wiki/ImageNet">ImageNet</a>,
which consists of exactly 1000&nbsp;classes and has more than 1&thinsp;000&thinsp;000
training samples. To be exact, it is the ImageNet Large Scale Visual Recognition Challenge (ILSVRC).

However, I miss easy to use examples. So here you are.


## Prerequisites

* [Tensorflow](https://www.tensorflow.org/install/)
    * [CUDA](http://askubuntu.com/q/799184/10425)
    * [CuDNN](http://askubuntu.com/q/767269/10425)
* [Keras](https://keras.io/#installation)


## Code

The following code is taken from [Keras](https://github.com/fchollet/keras/blob/master/keras/applications/resnet50.py) / [François Chollet](https://github.com/fchollet/deep-learning-models). Full credit to him for doing the difficult work.

The code defines one of the state of the art
models, a so called ResNet. See [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) for details. Then it downloads the weights, stores them for
subsequent uses and applies it to the data.

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ResNet50 model for Keras."""
from __future__ import print_function

import numpy as np
import json
import os

from keras import backend as K
from keras.preprocessing import image
from keras.applications import ResNet50
from keras.utils.data_utils import get_file

CLASS_INDEX = None
CLASS_INDEX_PATH = ('https://s3.amazonaws.com/deep-learning-models/'
                    'image-models/imagenet_class_index.json')


def preprocess_input(x, dim_ordering='default'):
    """
    Standard preprocessing of image data.

    1. Make sure the order of the channels is correct (RGB, BGR, depending on
       the backend)
    2. Mean subtraction by channel.

    Parameters
    ----------
    x : numpy array
        The image
    dim_ordering : string, optional (default: 'default')
        Either 'th' for Theano or 'tf' for Tensorflow

    Returns
    -------
    numpy array
        The preprocessed image
    """
    if dim_ordering == 'default':
        dim_ordering = K.image_dim_ordering()
    assert dim_ordering in {'tf', 'th'}

    if dim_ordering == 'th':
        x[:, 0, :, :] -= 103.939
        x[:, 1, :, :] -= 116.779
        x[:, 2, :, :] -= 123.68
        # 'RGB'->'BGR'
        x = x[:, ::-1, :, :]
    else:
        x[:, :, :, 0] -= 103.939
        x[:, :, :, 1] -= 116.779
        x[:, :, :, 2] -= 123.68
        # 'RGB'->'BGR'
        x = x[:, :, :, ::-1]
    return x


def decode_predictions(preds, top=5):
    """
    Decode the predictionso of the ImageNet trained network.

    Parameters
    ----------
    preds : numpy array
    top : int
        How many predictions to return

    Returns
    -------
    list of tuples
        e.g. (u'n02206856', u'bee', 0.71072823) for the WordNet identifier,
        the class name and the probability.
    """
    global CLASS_INDEX
    if len(preds.shape) != 2 or preds.shape[1] != 1000:
        raise ValueError('`decode_predictions` expects '
                         'a batch of predictions '
                         '(i.e. a 2D array of shape (samples, 1000)). '
                         'Found array with shape: ' + str(preds.shape))
    if CLASS_INDEX is None:
        fpath = get_file('imagenet_class_index.json',
                         CLASS_INDEX_PATH,
                         cache_subdir='models')
        CLASS_INDEX = json.load(open(fpath))
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
        results.append(result)
    return results


def is_valid_file(parser, arg):
    """
    Check if arg is a valid file that already exists on the file system.

    Parameters
    ----------
    parser : argparse object
    arg : str

    Returns
    -------
    arg
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    """Get parser object."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file",
                        dest="filename",
                        type=lambda x: is_valid_file(parser, x),
                        help="Classify image",
                        metavar="IMAGE",
                        required=True)
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()

    # Load model
    model = ResNet50(include_top=True, weights='imagenet')

    img_path = args.filename
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    print('Input image shape:', x.shape)
    preds = model.predict(x)
    for wordnet_id, class_name, prob in decode_predictions(preds)[0]:
        print("{wid}\t{prob:>6}%\t{name}".format(wid=wordnet_id,
                                                 name=class_name,
                                                 prob="%0.2f" % (prob * 100)))

```

Store it as `resnet50.py` and make it executable.

(In case the JSON becomes unavailable: <a href="https://github.com/MartinThoma/algorithms/blob/master/ML/ImageNet-classification/imagenet_class_index.json">Here you are</a>)


## How to use

```
$ ./resnet50.py -f honey-bee.jpg
```

alternatively, if you have a GPU but not that much memory:

```
$ CUDA_VISIBLE_DEVICES="" ./resnet50.py -f honey-bee.jpg
```

If you apply this to the jellyfish image from above, you get:

```
Input image shape: (1, 224, 224, 3)
n01910747    100.00%    jellyfish
n01496331      0.00%    electric_ray
n10565667      0.00%    scuba_diver
n01914609      0.00%    sea_anemone
n02607072      0.00%    anemone_fish
```

This takes about 6&nbsp;seconds on CPU on my laptop.


## Alternative Models

If you are building an application, you might want to look into alternatives:

<table class="table">
    <tr>
        <th>Modelname</th>
        <th>Input Size</th>
        <th>Top1-Accuracy</th>
        <th>Top5-Accuracy</th>
        <th>Time</th>
    </tr>
    <tr>
        <td><a href="https://arxiv.org/abs/1512.03385">ResNet50</a></td>
        <td>224 × 224</td>
        <td>77.15%</td>
        <td>93.29%</td>
        <td>5.59s</td>
    </tr>
    <tr>
        <td><a href="https://arxiv.org/abs/1409.1556">VGG16</a></td>
        <td>224 × 224</td>
        <td>73.0%</td>
        <td>91.2%</td>
        <td>6.56s</td>
    </tr>
    <tr>
        <td><a href="http://arxiv.org/abs/1512.00567">InceptionV3</a></td>
        <td>299 × 299</td>
        <td>78.8%</td>
        <td>94.4%</td>
        <td>7.62s</td>
    </tr>
    <tr>
        <td><a href="https://arxiv.org/abs/1610.02357">Xception</a></td>
        <td>299 × 299</td>
        <td>79.0%</td>
        <td>94.5%</td>
        <td>6.71s</td>
    </tr>
</table>

<div class="important">The speed is for the complete script. This includes loading the model. The model size is several 100&nbsp;MB. In a real application you can (1) load the model only once and (2) run the evaluation in batches to speed things up.</div>
