---
layout: post
title: Lasagne for Python Newbies
author: Martin Thoma
date: 2015-04-17 19:26
category: Machine Learning
tags:
- Python
- Machine Learning
featured_image: logos/python.png
---
Lasagne is a Python package for training neural networks. The nice thing about
Lasagne is that it is possible to write Python code and execute the training
on nVidea GPUs with automatically generated CUDA code.

However, installing Lasagne is not that easy. Especially if you are not
familiar with Python. This article aims to guide you through the installation
process.

## Python

Ubuntu-based systems will have Python installed, but I'm not too sure about
pip. You can get it with

```
$ sudo apt-get install python-pip
```

Make sure you have Python and `pip`, the standard Python package installer.
Type the following commands to check if you have both:

```bash
$ python --version
Python 2.7.8

$ pip --version
pip 6.1.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)
```

## sklearn

[sklearn](http://scikit-learn.org/stable/) is a nice package for machine
learning. You can install it with

```bash
$ pip install scikit-learn
```

(When I write commands like this you either have to execute
`sudo pip install scikit-learn` or `pip install scikit-learn --user`).

This should work without problems.

Each classifier has a `fit` method and a `predict` method. See
[iris example](http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html)
to get a feeling how to use it. It provides a lot of useful functions like
[`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html)
and has an awesome documentation.

You don't need this for Lasagne, but it might be good to use sklearn and
Lasagne in combination.


## Graphics drivers and CUDA

Make sure CUDA runs on your system by the following commands.
If it doesn't run, you could try the following guides:

* [Installing and testing CUDA in Ubuntu 14.04](http://askubuntu.com/q/451672/10425)
* [Installing CUDA Toolkit 6.5 on Ubuntu 14.04 Linux](http://www.r-tutor.com/gpu-computing/cuda-installation/cuda6.5-ubuntu)
* [NVIDIA CUDA Getting Started Guide for Linux](http://docs.nvidia.com/cuda/cuda-getting-started-guide-for-linux/#axzz3XaMVcNwV)

Run

```bash
$ nvidia-smi -L
GPU 0: GeForce GTX TITAN Black (UUID: GPU-abcdef12-abcd-1234-1234-01234567890a)

$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2013 NVIDIA Corporation
Built on Thu_Mar_13_11:58:58_PDT_2014
Cuda compilation tools, release 6.0, V6.0.1

$ nvidia-smi -a

==============NVSMI LOG==============

Timestamp                           : Fri Apr 17 18:44:41 2015
Driver Version                      : 331.79

Attached GPUs                       : 1
GPU 0000:01:00.0
    Product Name                    : GeForce GTX TITAN Black
    Display Mode                    : N/A
    Display Active                  : N/A
    Persistence Mode                : Disabled
    Accounting Mode                 : N/A
    Accounting Mode Buffer Size     : N/A
    Driver Model
        Current                     : N/A
        Pending                     : N/A
    Serial Number                   : N/A
    GPU UUID                        : GPU-fcff168f-a045-2f95-7a4f-8e1cf26a24eb
    Minor Number                    : 0
    VBIOS Version                   : 80.80.4E.00.01
    Inforom Version
        Image Version               : N/A
        OEM Object                  : N/A
        ECC Object                  : N/A
        Power Management Object     : N/A
    GPU Operation Mode
        Current                     : N/A
        Pending                     : N/A
    PCI
        Bus                         : 0x01
        Device                      : 0x00
        Domain                      : 0x0000
        Device Id                   : 0x100C10DE
        Bus Id                      : 0000:01:00.0
        Sub System Id               : 0x106610DE
        GPU Link Info
            PCIe Generation
                Max                 : N/A
                Current             : N/A
            Link Width
                Max                 : N/A
                Current             : N/A
        Bridge Chip
            Type                    : N/A
            Firmware                : N/A
    Fan Speed                       : 26 %
    Performance State               : N/A
    Clocks Throttle Reasons         : N/A
    FB Memory Usage
        Total                       : 6143 MiB
        Used                        : 39 MiB
        Free                        : 6104 MiB
    BAR1 Memory Usage
        Total                       : N/A
        Used                        : N/A
        Free                        : N/A
    Compute Mode                    : Default
    Utilization
        Gpu                         : N/A
        Memory                      : N/A
    Ecc Mode
        Current                     : N/A
        Pending                     : N/A
    ECC Errors
        Volatile
            Single Bit
                Device Memory       : N/A
                Register File       : N/A
                L1 Cache            : N/A
                L2 Cache            : N/A
                Texture Memory      : N/A
                Total               : N/A
            Double Bit
                Device Memory       : N/A
                Register File       : N/A
                L1 Cache            : N/A
                L2 Cache            : N/A
                Texture Memory      : N/A
                Total               : N/A
        Aggregate
            Single Bit
                Device Memory       : N/A
                Register File       : N/A
                L1 Cache            : N/A
                L2 Cache            : N/A
                Texture Memory      : N/A
                Total               : N/A
            Double Bit
                Device Memory       : N/A
                Register File       : N/A
                L1 Cache            : N/A
                L2 Cache            : N/A
                Texture Memory      : N/A
                Total               : N/A
    Retired Pages
        Single Bit ECC              : N/A
        Double Bit ECC              : N/A
        Pending                     : N/A
    Temperature
        Gpu                         : 29 C
    Power Readings
        Power Management            : N/A
        Power Draw                  : N/A
        Power Limit                 : N/A
        Default Power Limit         : N/A
        Enforced Power Limit        : N/A
        Min Power Limit             : N/A
        Max Power Limit             : N/A
    Clocks
        Graphics                    : N/A
        SM                          : N/A
        Memory                      : N/A
    Applications Clocks
        Graphics                    : N/A
        Memory                      : N/A
    Default Applications Clocks
        Graphics                    : N/A
        Memory                      : N/A
    Max Clocks
        Graphics                    : N/A
        SM                          : N/A
        Memory                      : N/A
    Compute Processes               : N/A
```

to see if CUDA was installed correctly.

## Theano

The installation of Theano is a bit tricky (see [official page](http://deeplearning.net/software/theano/install.html)). I don't remember if I installed additional packages, but try

```bash
$ sudo -H pip install theano
```

Make sure that your `~/.theanorc` exists and looks like this:

```text
[global]
device=gpu
floatX=float32
```

Note that `float32` is required, even if you have a 64bit system.

To test your installation, save the following as `theanotest.py` and execute
it with `python theanotest.py`:

```python
#!/usr/bin/env python
from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print f.maker.fgraph.toposort()
t0 = time.time()
for i in xrange(iters):
    r = f()
t1 = time.time()
print 'Looping %d times took' % iters, t1 - t0, 'seconds'
print 'Result is', r
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')
```

It should print the following (well, something similar):

```text
Using gpu device 0: GeForce GTX TITAN Black
[GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
Looping 1000 times took 0.38205909729 seconds
Result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
  1.62323296]
Used the gpu
```

Especially "used the gpu" is important. Theano code work on both, CPU and GPU.
If you have a GPU and it does not currently work on a task and it is configured
correctly, then Theano should automatically use the GPU.

(Don't try to run two Theano scripts at a time ... weird things could happen.)


## Lasagne

Lasagne is hosted at Github: [https://github.com/Lasagne/Lasagne](https://github.com/Lasagne/Lasagne)

Currently, it is not on pip as Sander wants to wait until we get to version
1.0. So you have to install it manually:

```bash
$ git clone https://github.com/Lasagne/Lasagne.git
$ cd Lasagne
Lasagne$ sudo -H python setup.py install
```

Now you can test if it worked by executing the MNIST example in Lasagne
([MNIST](http://yann.lecun.com/exdb/mnist/) is a huge digit dataset). This
might first take some time to download, but should then run quite fast. If
your machine does not use the GPU it will take ages (e.g. on my laptop it takes
about a minute for one epoch)

```
Lasagne/examples$ python mnist.py
Loading data...
Downloading MNIST dataset
Building model and compiling functions...
/usr/local/lib/python2.7/dist-packages/Lasagne-0.1dev-py2.7.egg/lasagne/init.py:30: UserWarning: The uniform initializer no longer uses Glorot et al.'s approach to determine the bounds, but defaults to the range (-0.01, 0.01) instead. Please use the new GlorotUniform initializer to get the old behavior. GlorotUniform is now the default for all layers.
  warnings.warn("The uniform initializer no longer uses Glorot et al.'s "
/usr/local/lib/python2.7/dist-packages/Lasagne-0.1dev-py2.7.egg/lasagne/layers/helper.py:55: UserWarning: get_all_layers() has been changed to return layers in topological order. The former implementation is still available as get_all_layers_old(), but will be removed before the first release of Lasagne. To ignore this warning, use `warnings.filterwarnings('ignore', '.*topo.*')`.
  warnings.warn("get_all_layers() has been changed to return layers in "
Starting training...
Epoch 1 of 500 took 72.593s
  training loss:        1.330231
  validation loss:        0.470251
  validation accuracy:        87.54 %%
```


## nolearn

[nolearn](https://github.com/dnouri/nolearn) is another Python package. It was
created to make using Lasagne even simpler.

You can install it via

```bash
$ git clone https://github.com/dnouri/nolearn.git
$ cd nolearn
$ python setup.py install --user
```


For example, the following code downloads the MNIST dataset, trains a model on
it and evaluates the result for a single image:

```python
#!/usr/bin/env python

import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

import sys
import os
import gzip
import pickle
import numpy


PY2 = sys.version_info[0] == 2

if PY2:
    from urllib import urlretrieve

    def pickle_load(f, encoding):
        return pickle.load(f)
else:
    from urllib.request import urlretrieve

    def pickle_load(f, encoding):
        return pickle.load(f, encoding=encoding)

DATA_URL = 'http://deeplearning.net/data/mnist/mnist.pkl.gz'
DATA_FILENAME = 'mnist.pkl.gz'


def _load_data(url=DATA_URL, filename=DATA_FILENAME):
    """Load data from `url` and store the result in `filename`."""
    if not os.path.exists(filename):
        print("Downloading MNIST dataset")
        urlretrieve(url, filename)

    with gzip.open(filename, 'rb') as f:
        return pickle_load(f, encoding='latin-1')


def load_data():
    """Get data with labels, split into training, validation and test set."""
    data = _load_data()
    X_train, y_train = data[0]
    X_valid, y_valid = data[1]
    X_test, y_test = data[2]
    y_train = numpy.asarray(y_train, dtype=numpy.int32)
    y_valid = numpy.asarray(y_valid, dtype=numpy.int32)
    y_test = numpy.asarray(y_test, dtype=numpy.int32)

    return dict(
        X_train=X_train,
        y_train=y_train,
        X_valid=X_valid,
        y_valid=y_valid,
        X_test=X_test,
        y_test=y_test,
        num_examples_train=X_train.shape[0],
        num_examples_valid=X_valid.shape[0],
        num_examples_test=X_test.shape[0],
        input_dim=X_train.shape[1],
        output_dim=10,
    )


def nn_example(data):
    net1 = NeuralNet(
        layers=[('input', layers.InputLayer),
                ('hidden', layers.DenseLayer),
                ('output', layers.DenseLayer),
                ],
        # layer parameters:
        input_shape=(None, 28*28),
        hidden_num_units=100,  # number of units in 'hidden' layer
        output_nonlinearity=lasagne.nonlinearities.softmax,
        output_num_units=10,  # 10 target values for the digits 0, 1, 2, ..., 9

        # optimization method:
        update=nesterov_momentum,
        update_learning_rate=0.01,
        update_momentum=0.9,

        max_epochs=10,
        verbose=1,
        )

    # Train the network
    net1.fit(data['X_train'], data['y_train'])

    # Try the network on new data
    print("Feature vector (100-110): %s" % data['X_test'][0][100:110])
    print("Label: %s" % str(data['y_test'][0]))
    print("Predicted: %s" % str(net1.predict([data['X_test'][0]])))


def main():
    data = load_data()
    print("Got %i testing datasets." % len(data['X_train']))
    nn_example(data)

if __name__ == '__main__':
    main()
```

The output is

```text
# Neural Network with 79510 learnable parameters

## Layer information

  #  name      size
---  ------  ------
  0  input      784
  1  hidden     100
  2  output      10

  epoch    train loss    valid loss    train/val    valid acc  dur
-------  ------------  ------------  -----------  -----------  -----
      1       0.59132       0.32314      1.82993      0.90988  1.70s
      2       0.30733       0.26644      1.15348      0.92623  1.96s
      3       0.25879       0.23606      1.09629      0.93363  2.09s
      4       0.22680       0.21424      1.05865      0.93897  2.13s
      5       0.20187       0.19633      1.02827      0.94313  2.21s
      6       0.18129       0.18187      0.99685      0.94758  1.81s
      7       0.16398       0.16992      0.96506      0.95074  2.14s
      8       0.14941       0.16020      0.93265      0.95262  1.88s
      9       0.13704       0.15189      0.90222      0.95460  2.15s
     10       0.12633       0.14464      0.87342      0.95707  2.21s
Feature vector (100-110): [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
Label: 7
Predicted: [7]
```



## See also

* [Getting Started with Deep Learning and Python](http://www.pyimagesearch.com/2014/09/22/getting-started-deep-learning-python/)