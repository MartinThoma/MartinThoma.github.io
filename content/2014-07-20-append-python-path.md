---
layout: post
title: Append Python PATH
slug: append-python-path
lang: en
author: Martin Thoma
date: 2014-07-20 14:04
category: Code
tags: Python
featured_image: logos/python.png
---
Python has a `PATH` in which it looks for modules. You can display the current
module PATH with

```python
import sys

print(sys.path)
```

and append something to it with

```python
import sys

sys.path.append("/some/path/to/a/module")
```

However, the clean way would be to write a module and install that module.
