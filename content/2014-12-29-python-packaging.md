---
layout: post
lang: en
title: Packaging with Python
slug: python-packaging
author: Martin Thoma
date: 2014-12-29 21:05
category: Code
tags: Python
featured_image: logos/python.png
---
<div class="info">This is a quick article I had for quite a while as a draft. It might not be finished or have other problems, but I still want to share it.

I wrote this when I did not know much about packaging. I wrote a tutorial <a href="https://martin-thoma.com/python-projects/">how to create Python packages</a> in 2018 as well. In 2020, I gave a <a href="https://martin-thoma.com/python-packaging-course/">Python Packaging Course</a> which is better structured, up-to-date and has way more details.</div>

The following article is a wrap-up of the talk [Python Packages](https://www.youtube.com/watch?v=MSs3QmHhvpE)
from Daniel Hepper given at a German [PyCon 2013](https://2013.de.pycon.org/schedule/sessions/15/).

[PyPi](https://pypi.python.org/pypi) is the Python Package Index. They distribute
packages in form of "eggs". You can install them with easy_install or with pip.


## Package Management Tools

### Distutils
Distutils is part of the standard library. When you run

```bash
python setup.py install
```

then distutils is running.

Major disadvantages of distutils are:

* No Meta-data:
  * no deinstallation
  * no dependencies
* No Package listing (so you can't automatically search pypi)

### Setuptools

Setuptools is an extension for distutils. Setuptools offers dependency management.
With setuptools, so called 'egg files' were introduced. Those files are comparable
to jar files in Java.

### Distribute

Distribute was a fork of setuptools that got merged back to setuptools. So
don't use distribute, use setuptools.

## PIP and Creating packages

See [Python Packaging Course](https://martin-thoma.com/python-packaging-course/)

## Environments

See [Virtual Environments](https://martin-thoma.com/virtual-environments/)
