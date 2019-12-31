---
layout: post
title: How to Speed up Docker
slug: docker-speedup
author: Martin Thoma
status: draft
date: 2019-12-11 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/star.png
---
Building a Docker container can take quite a while. However, there are some
easy parts to speed them up.

## Install Early, Copy Late

Make sure you install dependencies early and copy code late during building
the container. This helps to cache the dependencies.

You might also want to look at dependency pinning.


## .dockerignore

Make sure you don't re-build the container with stuff you don't need.

You can check the included files via

```
sudo docker build -t test .
sudo docker run --entrypoint /usr/bin/find -it test
sudo docker images | grep ^test
```

When I started looking at the size of my Flask image, it was 357MB.
Without copying any of the code, it was `349MB`.

See also: 

* [Do not ignore .dockerignore](https://codefresh.io/docker-tutorial/not-ignore-dockerignore-2/)
* [Differences of Rules Between .gitignore and .dockerignore](https://zzz.buzz/2018/05/23/differences-of-rules-between-gitignore-and-dockerignore/)