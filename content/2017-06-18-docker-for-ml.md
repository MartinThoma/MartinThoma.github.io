---
layout: post
title: Docker for ML
slug: docker-for-ml
author: Martin Thoma
status: draft
date: 2017-06-18 20:00
category: Machine Learning
tags: Machine Learning, Docker
featured_image: logos/ml.png
---
When you write software, you usually have dependencies. Often a lot of
dependencies. In order to make deployment / usage easier, you can create
container. Docker is a software which supports writing and using containers.


## Installing Docker

Just have a look at the [official guide](https://docs.docker.com/engine/installation/linux/ubuntu/).
It should be simple enough to get started.


## Usage Example

https://hub.docker.com/r/tensorflow/tensorflow/ : 

```
$ sudo docker run -it -p 8888:8888 tensorflow/tensorflow
```

