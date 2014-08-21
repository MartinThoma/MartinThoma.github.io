---
layout: post
title: Sharing large files in Science
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
- Dropbox
featured_image: logos/python.png
---

I am currently writing my bachelors thesis about on-line handwriting recognition
of mathematical symbols. It is a supervised machine learning task. Hence I
have lots of data on which I run my experiments. This data changes.
And I want to share the data so that the results of my experiments can be
checked by others.

That is a problem. The complete dataset without any modifications is about
1.6GB big. And I want to upload variations of that dataset, too.
That means I cannot simply put it on my server.

An alternative is [Dropbox](https://www.dropbox.com/home).

They offer a lot of space for free (I currently have over 75GB!) and they
seem to have a good uptime.

And the best of it: They have a Python API :-)
Just install it via pip (see [pypi](https://pypi.python.org/pypi/dropbox/2.1.0)):

```bash
$ sudo pip install dropbox
```

They support many languages / platforms:

* Python
* Ruby
* PHP
* Java
* Android
* iOS
* OS X

## See also

* [Core API for many languages](https://www.dropbox.com/developers/core)
* [Using the Core API in Python](https://www.dropbox.com/developers/core/start/python): A pretty good tutorial how to get started in Python.
* [Core API for Python Documentation](https://www.dropbox.com/developers/core/docs/python)