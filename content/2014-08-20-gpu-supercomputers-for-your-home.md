---
layout: post
lang: en
title: GPUs - Supercomputers for your home
slug: gpu-supercomputers-for-your-home
author: Martin Thoma
date: 2014-08-20 23:26
category: Machine Learning
tags: Python, Theano, GPU, nVidea, CUDA, AI, Machine Learning
featured_image: logos/nvidia.png
---
A few days ago I got some of my neural net code to work with a GPU.
The GPU is called "Tesla C2075". It is able to get 515 GFlops peak performance.
It has 448 CUDA cores that work with 1.15 GHz and it has 6GB GDDR5 memory.

My code needed about 10 hours to run before. After that, it only needed 10
minutes. That is 60 times faster! The library that did this miracle for me is
called [Theano](http://deeplearning.net/software/theano/))

Out of curiosity, I've searched for current high-end gamer graphic cards.
I found nVidia Titan Z:

<iframe width="512" height="288" src="//www.youtube.com/embed/2JjxgJcXVE0" frameborder="0" allowfullscreen></iframe>

The Titan Z has 5760 CUDA cores. It can get 4061 GFLOPS x2 and has 12 GB of
memory. That technological wonder-work costs only 2802 Euro.

To put that into perspective: In 2005, you would probably have been on place
68 of the TOP500 supercomputers world wide! ([source](http://www.top500.org/list/2005/06/?page=1)).

Isn't that crazy?

## See also:

* [Titan Z Specification](http://www.geforce.com/hardware/desktop-gpus/geforce-gtx-titan-z/specifications)
* [What are the differences between “scientific GPUs” and “gaming GPUs”?](http://superuser.com/questions/805217/what-are-the-differences-between-scientific-gpus-and-gaming-gpus)
