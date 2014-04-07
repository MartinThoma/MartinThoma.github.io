---
layout: post
title: Packaging with Python
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
featured_image: logos/python.png
---

The following article is a wrap-up of the talk [Python Packages](https://www.youtube.com/watch?v=MSs3QmHhvpE)
from Daniel Hepper given at a German [PyCon 2013](https://2013.de.pycon.org/schedule/sessions/15/).

distutils have very limited functionality. This is the reason why you should
use setuptools. But 'distribute' is compatible to setuptools.

[PyPi](https://pypi.python.org/pypi) is the Python Package Index. They distribute
packages in form of "eggs". You can install them with easy_install or with pip.

virtualenv / virtualenvwrapper

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
Setuptools are startet when you install a package with `easy_install`:

```bash
easy_install package
```

Setuptools are an extension for distutils. Setuptools offers dependency management.
With setuptools, so called 'egg files' were introduced. Those files are comparable
to jar files in Java.

### Distribute

Distribute was a fork of setuptools that got merged back to setuptools. So 
don't use distribute, but use setuptools.

## Installer

### PIP
PIP is short for 'PIP installs Python'. It can only install files from sources;
so it does not support egg files.

PIP commands are

* install
* uninstall
* freeze
* search
* bundle
* unzip
* zip
* wheel
* help

## Environments
It might be the case that you have to have a Django 1.4 and a Django 1.5 project.
In that case, you need different environments.

### Virtualenv
```bash
$ pip freeze
$ virtualenv my_env
$ source my_env/bin/activate
```

### Virtualenvwrapper

## Creating packages

A project could have this structure:

```bash
$ tree
.
├── LICENSE
├── MANIFEST
├── pyconde2013news
│   └── __init__.py
├── README
└── setup.py

```

With this setup.py:

```python
from distutils.core import setup
setup(name="pycon2013news", version="0.1", py_modules=["pycon2013news"],)
```

This can directly be registered on PyPi:

```bash
python setup.py register
```

But a problem of this code is that it does not show the dependencies. So you
should rather use setuptools for your setup.py:

```python
from setuptools import setup
setup(name="pycon2013news",
      version="0.1",
      py_modules=["pycon2013news"],
      description="Reads latest news headlines from the PyCon.DE 2013 website")
      author="Daniel Hepper",
      author_email="daniel@butfriendly.com",
      url="https://github.com/dhepper/pyconde2013news",
      install_requires=[
          "beautifulsoup4==4.3.2",
          "requests==2.0.0"
      ]
```

When you add `scripts` argument to setup, you can later execute those.
Entry points are also interesting.


## Additional information

* http://guide.python-distribute.org/contributing.html