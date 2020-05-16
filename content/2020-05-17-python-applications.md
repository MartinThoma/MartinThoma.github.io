---
layout: post
title: Python Application
slug: python-applications
author: Martin Thoma
status: draft
date: 2020-05-17 20:00
category: Code
tags: Python
featured_image: logos/star.png
---


## Create Executables

[pex](https://pex.readthedocs.io/en/stable/) provides a general purpose Python
environment virtualization solution similar in spirit to virtualenv. PEX files
have been used by Twitter to deploy Python applications to production since
2011.

Here is how you use it:

```shell
$ pip install pex
$ pex -vv --disable-cache --python-shebang="/usr/bin/env python3.6" --output-file=fooexecutable --requirement=requirements.txt -e modulename
```
