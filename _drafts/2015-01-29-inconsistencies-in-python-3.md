---
layout: post
title: Inconsistencies in Python 3
author: Martin Thoma
date: 2014-11-22 17:19
categories: 
- Code
tags: 
- Python
featured_image: logos/python.png
---

Consistency is an important quality property of a language. One of my main
points of critic agains PHP was inconsistency (see [PHP: A strange language](http://martin-thoma.com/php-a-strange-language/#tocAnchor-1-1)). Let's see where Python is inconsistant.

## Method naming: Underscores or not

PEP 8 recommends underscores for functions, if I remember it correctly.
However, some built-in functions do not follow this naming scheme:

* [`float.fromhex`](https://docs.python.org/3/library/stdtypes.html#float.fromhex)
* [`bytes.startswith`](https://docs.python.org/3/library/stdtypes.html#bytes.startswith)
* [`str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)