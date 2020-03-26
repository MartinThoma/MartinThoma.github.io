---
layout: post
title: Best practice for Machine Learning Projects
slug: ml-best-practice
author: Martin Thoma
date: 2017-11-15 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/ml.png
---
I did a couple of machine learning projects so far and there are some patterns
in the projects which turned out to be good ideas. In this post, I would like
to share those patterns with you.


## Know your problem

For me, a machine learning project really starts when you have a well-defined
problem, data, and a metric in which you want to measure your models goodness.
Just like Tom Mitchell defined Machine Learning:

> A computer program is said to learn from experience E with respect to some
> class of tasks T and performance measure P if its performance at tasks in T,
> as measured by P, improves with experience E.


## EDA

Exploratory Data Analysis should be the very first step. Know what your data
looks like. Which errors can be expected to be in the data? How is it
distributed?

For CSV files, I wrote the [Exploratory Data Analysis](https://martin-thoma.com/eda/)
article. Usually, this starts with having a look at examples and making some
graphs. EDA depends on what kind of data you have and which problem you want to
solve. I will not go into detail in this post.


## Project structure

```text
.
├── artifacts
│   ├── train : Logfiles, trained models
│   └── test  : Logfiles
├── datasets : Data loading scripts
├── experiments : Configuration files
├── models : Scripts defining how the model looks like
├── optimizers : Scripts defining the optimizeres
└── train : Script to run the training
```

The important part here is that you have an `experiments/` folder which
contains configuration files. So your scripts should not contain any
hyperparameters. All hyperparameters, including the complete model, should be
set in the configuration.


## Configuration files

An example from my masters thesis is `cifar10_opt.yaml`:

```yaml
dataset:
  script_path: ../datasets/cifar10_keras.py
model:
  script_path: ../models/optimized.py
optimizer:
  script_path: ../optimizers/adam_keras.py
  initial_lr: 0.0001
train:
  script_path: ../train/train_keras.py
  artifacts_path: ../artifacts/cifar10_opt/
  batch_size: 64
  epochs: 1000
  data_augmentation:
    samplewise_center: False
    samplewise_std_normalization: False
    rotation_range: 0
    width_shift_range: 0.1
    height_shift_range: 0.1
    horizontal_flip: True
    vertical_flip: False
    zoom_range: 0
    shear_range: 0
    channel_shift_range: 0
    featurewise_center: False
    zca_whitening: False
evaluate:
  batch_size: 1000
  augmentation_factor: 32
  data_augmentation:
    samplewise_center: False
    samplewise_std_normalization: False
    rotation_range: 0
    width_shift_range: 0.15
    height_shift_range: 0.15
    horizontal_flip: True
    vertical_flip: False
    zoom_range: 0
    shear_range: 0
    channel_shift_range: 0
    featurewise_center: False
    zca_whitening: False
```

I load it like this:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run an experiment."""

import logging
import sys
import os
import yaml
import imp
import pprint

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    stream=sys.stdout,
)


def main(yaml_filepath):
    """Example."""
    cfg = load_cfg(yaml_filepath)

    # Print the configuration - just to make sure that you loaded what you
    # wanted to load
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cfg)

    # Here is an example how you load modules of which you put the path in the
    # configuration. Use this for configuring the model you use, for dataset
    # loading, ...
    dpath = cfg["dataset"]["script_path"]
    sys.path.insert(1, os.path.dirname(dpath))
    data = imp.load_source("data", cfg["dataset"]["script_path"])


def load_cfg(yaml_filepath):
    """
    Load a YAML configuration file.

    Parameters
    ----------
    yaml_filepath : str

    Returns
    -------
    cfg : dict
    """
    # Read YAML experiment definition file
    with open(yaml_filepath, "r") as stream:
        cfg = yaml.load(stream)
    cfg = make_paths_absolute(os.path.dirname(yaml_filepath), cfg)
    return cfg


def make_paths_absolute(dir_, cfg):
    """
    Make all values for keys ending with `_path` absolute to dir_.

    Parameters
    ----------
    dir_ : str
    cfg : dict

    Returns
    -------
    cfg : dict
    """
    for key in cfg.keys():
        if key.endswith("_path"):
            cfg[key] = os.path.join(dir_, cfg[key])
            cfg[key] = os.path.abspath(cfg[key])
            if not os.path.isfile(cfg[key]):
                logging.error("%s does not exist.", cfg[key])
        if type(cfg[key]) is dict:
            cfg[key] = make_paths_absolute(dir_, cfg[key])
    return cfg


def get_parser():
    """Get parser object."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        help="experiment definition file",
        metavar="FILE",
        required=True,
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.filename)
```

## Starting small

Most machine learning tasks have a lot of computation. I'm speaking of many
hours for the "real" task you want to solve. You will not be able to do so
directly. You will make bugs. Maybe simple typos, maybe logical bugs, ...

Create a small toy example where you know how the output should look like. Just
to reduce the number of hours you waste by waiting for the script to finish /
break.


## Logging to files

Even if your script is working, you can make other mistakes:

* You close the terminal accidentially.
* Your computer freezes.
* Your you is cancelled from the cluster by the admin, just a couple of minutes
  before it would finish.
* Your model at some point diverges.

For this reason, you should make sure that you log results to a file when you
have really long running scripts. Store those files in the `artifacts/`
directory.


## Create a Trivial Solution

Most machine learning projects have trivial, simple and advanced solutions. For
example, instead of having a machine learning based approach you can usually
craft algorithms the traditional way. You should know how well those trivial
solutions are, because:

* **Baseline**: They give you a baseline. A score with which you start and from
  which you can evaluate if your more complex approaches are worth it.
* **Little effort**: They are usually comparatively fast to implement. If you
  see that the trivial solution is already very good, you might be able to stop
  faster.
* **Robustness**: They are robust against error in the data. The trivial ones
  because they don't use the data, the simple ones because they are usually to
  restricted to overfit.


Here are some examples:

<table class="table">
    <tr>
        <th>Problem</th>
        <th>Trivial</th>
        <th>Simple</th>
        <th>Advanced</th>
    </tr>
    <tr>
        <td>Classification</td>
        <td>Rules, Predict the most common class</td>
        <td>Decision Tree</td>
        <td>Neural Networks, SVMs, Gradient Boosting</td>
    </tr>
    <tr>
        <td>Regression</td>
        <td>Rules, Predict the average</td>
        <td>Linear Regression</td>
        <td>Neural Networks, Gaussian Mixture Models, ...</td>
    </tr>
    <tr>
        <td>Clustering</td>
        <td>Rules</td>
        <td>k-Means</td>
        <td>DBSCAN, OPTICS, SOMs</td>
    </tr>
    <tr>
        <td>Recommendations</td>
        <td>Rules</td>
        <td></td>
        <td>RBMs, ...</td>
    </tr>
    <tr>
        <td><abbr title="Reinforcement Learning">RL</abbr></td>
        <td>Rules</td>
        <td></td>
        <td>DQN, DDQN, ... (see <a href="https://martin-thoma.com/rl-agents/">post</a>)</td>
    </tr>
</table>




## Evaluation

Make sure that you have as few scoring numbers as possible. Sequences / example
output is not so easy to compare. You should be able to tell if you improved.
Ideally, it would be a single normalized score which also has a meaning and
a pre-defined threshold, e.g.

* Accuracy: Is in [0, 1] and you can probably say in advance how high you have
  to get to be useful / when you can consider improvements marginal.
* Precision, Recall, <abbr title="Mean Squared Error">MSE</abbr>
* Cross-Entropy
* ...


## Make it reproducible

Set seeds for all random number generators. And log on which hardware / with
which software version you executed your stuff.

The reason for this is simply that you can proof you actually got the results
you have. Or at least point to a reason why you can't get the results again.
