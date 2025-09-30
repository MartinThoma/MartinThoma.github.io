---
layout: post
lang: en
title: Python Packages
slug: python-packages
author: Martin Thoma
date: 2018-05-17 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/python.png
---
<div class="info">You might be looking for a tutorial <a href="https://martin-thoma.com/python-projects/">how to create Python packages</a>.</div>
This article is about Python packages I use. Some of them are well known,
others might be new to you. Let me know if I missed some that are important to
you.


## Data Science

### Data Formats

* [Pypdf2](https://pythonhosted.org/PyPDF2/)
* [HDF5](https://support.hdfgroup.org/HDF5/): [read & write](https://stackoverflow.com/a/41586571/562769)
* [`msgpack`](https://msgpack.org): [read & write](https://stackoverflow.com/questions/43442194/how-do-i-read-and-write-with-msgpack)
* [PyYAML](http://pyyaml.org/wiki/PyYAML)


### Data Analysis

* [`matplotlib`](https://matplotlib.org)
* [seaborn](https://seaborn.pydata.org)
* [Pandas](https://pandas.pydata.org): Data analysis of tabular data
* [`edapy`](https://github.com/MartinThoma/edapy): Exploratory data analysis tool


### Scientific Computation

* [`numpy`](http://www.numpy.org): Use arrays for efficiency
* [`scipy`](https://www.scipy.org): Statistical functions, image manipulation and more


### Machine Learning

* [Tensorflow](https://www.tensorflow.org): Create neural networks
    * [Keras](https://keras.io): Create neural networks easier
* [sklearn](http://scikit-learn.org/stable/index.html): Various machine learning stuff
* [gym](https://gym.openai.com): Creating environments for reinforcement learning
* [`clana`](https://github.com/MartinThoma/clana)


## Web and Services

* [Flask](http://flask.pocoo.org): web framework
* [boto3](https://github.com/boto/boto3): AWS
* [moto](https://github.com/spulec/moto): Testing AWS boto3 code


## Datetime

* [`dateutil`](https://dateutil.readthedocs.io/en/stable/): Parsing datetime strings
* [`pytz`](https://pypi.org/project/pytz/): Timezones in Python
* [`freezegun`](https://github.com/spulec/freezegun): Fake time for testing


## Testing

* [`pytest`](https://docs.pytest.org/en/latest/): Writing unittests
* [`tox`](https://tox.readthedocs.io/en/latest/): Running tests


## Misc

* [`cfg_load`](https://github.com/MartinThoma/cfg_load): Loading of configuration files
* [`exchangelib`](https://github.com/ecederstrand/exchangelib): Interactions with Microsoft Exchange Server
* [`itertools`](https://docs.python.org/3/library/itertools.html): Iterating stuff
* [`natsort`](https://pypi.org/project/natsort/#description): natural sorting
* [Pillow](https://pillow.readthedocs.io/en/5.1.x/): Image manipulation
* [`pint`](https://pypi.org/project/Pint/#description): Units
* [`progressbar2`](https://pypi.org/project/progressbar2/#description)
* [`shutil`](https://docs.python.org/2/library/shutil.html): high-level operations on files and collections of files
* [`six`](https://pypi.org/project/six/#description): Backwards compatibility to Python 2.7



## Honorable Mentions

I know that the following Packages are popular, but I never really used them:

* Django
