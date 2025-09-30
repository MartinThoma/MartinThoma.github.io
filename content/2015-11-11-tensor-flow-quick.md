---
layout: post
lang: en
title: Tensor Flow - A quick impression
slug: tensor-flow-quick
author: Martin Thoma
date: 2015-11-11 22:33
category: Machine Learning
tags: Machine Learning, Python, Tensorflow
featured_image: logos/tensor-flow.png
---
Tensor Flow is a machine learning toolkit which recently got published by
Google. They published it under [Apache License 2.0](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)). Looking at the source code overview, it seems to be mainly C++
with a significant bit of Python.

I guess the abstract of the
[Whitepaper](http://download.tensorflow.org/paper/whitepaper2015.pdf) is a good
description what TensorFlow is:

> TensorFlow is an interface for expressing machine learning algorithms, and an
> implementation for executing such algorithms. A computation expressed using
> TensorFlow can be executed with little or no change on a wide variety of
> heterogeneous systems, ranging from mobile devices such as phones and tablets
> up to large-scale distributed systems of hundreds of machines and thousands
> of computational devices such as GPU cards. The system is flexible and can be
> used to express a wide variety of algorithms, including training and
> inference algorithms for deep neural network models, and it has been used for
> conducting research and for deploying machine learning systems into
> production across more than a dozen areas of computer science and other
> fields, including speech recognition, computer vision, robotics, information
> retrieval, natural language processing, geographic information extraction,
> and computational drug discovery. This paper describes the TensorFlow
> interface and an implementation of that interface that we have built at
> Google. The TensorFlow API and a reference implementation were released as an
> open-source package under the Apache 2.0 license in November, 2015 and are
> available at www.tensorflow.org.

The core seems to be written in C++, but it has a Python front end.

By now, I couldn't test much because I just made my GPU machine unusable
(while trying to get the GPU General Computing practical software to run...).
I'll try to expand this article as soon as possible, but I guess it might
take several weeks until I have enough time. Lets see...


## Installation

The documentation about the installation makes a VERY good impression. Better
than anything I can write in a few minutes, so ... [RTFM](http://tensorflow.org/get_started/os_setup.md)
 😜

For Linux systems with CUDA and without root privileges, you can install it
with:

```bash
$ pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl --user
```

But remember you have to set the environment variable `LD_LIBRARY_PATH` and
`CUDA_HOME`. For many configurations, adding the following lines to your
`.bashrc` will work:

```bash
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME=/usr/local/cuda
```


## MNIST

The following code can be used to check if your Tensor Flow installation is
working. You have to have the [`get_mnist_data_tf.py`](https://gist.github.com/MartinThoma/f37150d0c521f598b08a)
in the same directory as the following script. I've - more or less - directly
copied it from [the tutorial](http://tensorflow.org/tutorials/mnist/pros/index.md).
Just execute the script below and see if it finishes without throwing errors.

```python
#!/usr/bin/env python
from get_mnist_data_tf import read_data_sets

mnist = read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf

sess = tf.InteractiveSession()
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
sess.run(tf.initialize_all_variables())
y = tf.nn.softmax(tf.matmul(x, W) + b)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
for i in range(1000):
    batch = mnist.train.next_batch(50)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")


W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(x, [-1, 28, 28, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
sess.run(tf.initialize_all_variables())
for i in range(1000):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(
            feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}
        )
        print("step %d, training accuracy %g" % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print(
    "test accuracy %g"
    % accuracy.eval(
        feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}
    )
)
```


## Observations

While looking at the MNIST example, I made a couple of observations. Let's
begin with the nice parts:

* Tensor Flow has a usable documentation (e.g. [The neural network part](http://tensorflow.org/api_docs/python/nn.md)). Not great, as Lasagne where you have lots of details (e.g. [activation functions](http://lasagne.readthedocs.org/en/latest/modules/nonlinearities.html#lasagne.nonlinearities.sigmoid))
* Seems to be quite easy to use.
* Seems to be well-tested by simply being used in many different projects by
  Google.
* Just like Theano (and thus Lasagne), Tensor flow has automatic
  differenciation.

Not sure:

* How easy is it to share trained models? In which format would you do so?
* How easy is it to understand a shared model?
* How easy is it to get something new to Tensor Flow like recurrent layers?
  (Actually, this seems rather to show that either the Whitepaper is a bit
  misleading or the documentation / Google search is not that good. In the
  whitepaper they write something about LTSM models, but I couldn't find any docs
  about that. Only by manually going through the manual,
  [I found it](http://tensorflow.org/tutorials/recurrent/index.md))


Not so nice:

* Doesn't work with Python&nbsp;3.
* They don't follow [PEP8](https://www.python.org/dev/peps/pep-0008/). I know
  that there is a [Python style guide by Google](https://google.github.io/styleguide/pyguide.html),
  but it does not seem to follow that one either. See the next section for
  some more detailed feedback.
* Just like the other Toolkits, you need CUDA. It doesn't work with OpenCL.


### PEP8

* Whitespace
  * `W = tf.Variable(tf.zeros([784, 10]))` should be
    `W = tf.Variable(tf.zeros([784, 10]))`.
    Missing whitespaces happened quite often.
  * Indent with 2&nbsp;spaces instead of 4&nbsp;spaces. The Google guide seems
    also to use 4.
  * Newlines between functions are missing.
* Print statement instead of a print function was used &rightarrow;
  only Python&nbsp;2, not Python&nbsp;3.
* I'm not sure why `y_` has the trailing underscore. According to
  [PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles),
  a single trailing underscore is used by convention to avoid conflicts with
  Python keyword.
* A mixture of different styles as pointed out on [Credric's Blog](http://beust.com/weblog/2015/11/09/tensorflows-rough-exterior/)


## Videos

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/oZikw5k_2FM?rel=0" frameborder="0" allowfullscreen></iframe>

Starting at 21m 2s:

<iframe width="512" height="288" src="https://www.youtube-nocookie.com/embed/90-S1M7Ny_o?rel=0" frameborder="0" allowfullscreen></iframe>


## Alternatives / Similar software

As I don't really know by now what Tensor Flow is doing, I can't pin-point
alternatives. But I have some educated guesses:

* [Theano](http://deeplearning.net/software/theano/) has been around for quite
  a while and seems to have a similar approach with its computational graph.
  Enhanced by [Lasagne](http://lasagne.readthedocs.org/en/latest/), it is a
  pretty good alternative when it comes to neural networks. Lasagne has an
  exceptionally good documentation, but parts of the tutorial could still be
  improved.
* [Caffe](http://caffe.berkeleyvision.org/) was something I recently tried.
  I didn't like it too much due to the lack of documentation, but it certainly
  is a big project. Especially when it comes to images.
* I haven't tried, but they look promising:
  * [Chainer](http://chainer.org/)
  * [MXNet](http://mxnet.readthedocs.org/en/latest/)
  * [CGT](http://rll.berkeley.edu/cgt/)
  * [Torch](http://torch.ch/) has a very nice example for [a character
    predictor](http://karpathy.github.io/2015/05/21/rnn-effectiveness/).


## See also

* [Official Website](http://tensorflow.org/)
  * [github.com/tensorflow](https://github.com/tensorflow/tensorflow)
  * [TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems](http://download.tensorflow.org/paper/whitepaper2015.pdf)
* [news.ycombinator.com](https://news.ycombinator.com/item?id=10532957)
* [reddit.com/r/programming](https://www.reddit.com/r/programming/comments/3s4vkn/google_brains_deep_learning_library_tensorflow_is/)
