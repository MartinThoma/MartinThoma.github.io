---
layout: post
title: Get CUDA 6 on Ubuntu 14.04
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
featured_image: logos/sublime-text.png
---

Alex Burnap has written a [great tutorial how to install CUDA 6 on Ubuntu 14.04](http://crowdtheory.wordpress.com/2014/04/25/ubuntu-14-04-with-latest-nvidia-drivers/).
However, I would like to make sure that this doesn't get lost and expand it a
little bit.

## Preparation

### Downloads

Download the following files:

* http://developer.download.nvidia.com/compute/cuda/6_0/rel/installers/cuda_6.0.37_linux_64.run - CUDA toolkit
* 

### Installs

```bash
sudo apt-get install libglu1-mesa libxi-dev libxmu-dev
```

