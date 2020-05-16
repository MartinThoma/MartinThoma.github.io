---
layout: post
title: Python Code Documentation
author: Martin Thoma
date: 2015-04-08 19:39
category: Code
tags: Python, Documentation
featured_image: logos/python.png
---
Documentating your code is important when you make non-trivial projects. The
standard way to document Python code is with [Sphinx](http://sphinx-doc.org/).
You write the documentation files with [reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html).

One of the most important Sphinx plugins is
[autodoc](http://sphinx-doc.org/ext/autodoc.html). This allows you to generate
the documentation of modules, classes and functions automatically by using
their docstrings.

There are 3 standard ways to write docstrings: Sphinxy, Googley or NumPyDocy.

## The Sphinx Way

```python
from typing import List


def preprocessing(self, algorithms: List):
    """Apply preprocessing algorithms.

    :param algorithms: Preprocessing allgorithms which get applied in order.
    :type algorithms: a list objects

    >>> import preprocessing
    >>> a = HandwrittenData(...)
    >>> preprocessing_queue = [(preprocessing.scale_and_shift, []),
    ...                        (preprocessing.connect_strokes, []),
    ...                        (preprocessing.douglas_peucker,
    ...                         {'EPSILON': 0.2}),
    ...                        (preprocessing.space_evenly,
    ...                         {'number': 100,
    ...                          'KIND': 'cubic'})]
    >>> a.preprocessing(preprocessing_queue)
    """
    for algorithm in algorithms:
        algorithm(self)
```

## The Google Way

Google documented its format at [google.github.io](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

```python
from typing import List


def preprocessing(self, algorithms: List):
    """Apply preprocessing algorithms.

    Args:
      algorithms (a list objects): Preprocessing allgorithms which get
        applied in order.

    Examples:

      >>> import preprocessing
      >>> a = HandwrittenData(...)
      >>> preprocessing_queue = [(preprocessing.scale_and_shift, []),
      ...                        (preprocessing.connect_strokes, []),
      ...                        (preprocessing.douglas_peucker,
      ...                         {'EPSILON': 0.2}),
      ...                        (preprocessing.space_evenly,
      ...                         {'number': 100,
      ...                          'KIND': 'cubic'})]
      >>> a.preprocessing(preprocessing_queue)
    """
    for algorithm in algorithms:
        algorithm(self)
```

To get the google way render well in Sphinx, you need [Napoleon](https://pypi.python.org/pypi/sphinxcontrib-napoleon).


## The NumPyDoc Way

```python
from typing import List


def preprocessing(self, algorithms: List):
    """Apply preprocessing algorithms.

    Parameters
    ----------
    algorithms : a list objects
        Preprocessing allgorithms which get applied in order.

    Examples
    --------
    >>> import preprocessing
    >>> a = HandwrittenData(...)
    >>> preprocessing_queue = [(preprocessing.scale_and_shift, []),
    ...                        (preprocessing.connect_strokes, []),
    ...                        (preprocessing.douglas_peucker,
    ...                         {'EPSILON': 0.2}),
    ...                        (preprocessing.space_evenly,
    ...                         {'number': 100,
    ...                          'KIND': 'cubic'})]
    >>> a.preprocessing(preprocessing_queue)
    """
    for algorithm in algorithms:
        algorithm(self)
```

To make numpydoc render well, you need the [numpydoc sphinx extension](https://pypi.python.org/pypi/numpydoc).

## See also

* [A Guide to NumPy/SciPy Documentation](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
* [sphinxcontrib-napoleon.readthedocs.org](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_numpy.html): A longer numpydoc example
