---
layout: post
title: Iterables in Python
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- Python
featured_image: logos/python.png
---
You can define your own iterables with Python by implementing `__iter__`.
The most simple example is

```python
class BlaBla(object):
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.my_list.__iter__()
```