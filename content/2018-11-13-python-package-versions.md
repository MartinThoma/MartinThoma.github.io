---
layout: post
title: Python Package Versions
slug: python-package-versions
author: Martin Thoma
date: 2018-11-13 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
Python packages should (must?) have a version. It would be best if that
version string was a [semantic version](https://semver.org), but this article
is not about how your version string should look like. It's about how to have
a consistent **version string on PyPI** and **accessible via
`[yourpackage].__version__`** - and preferably make sure it is the same as used
in [`git tag`](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

`setup.py` should have the version string in the setup function:

```
from setuptools import setup

setup(version=__version__)
```

Having this makes sure that the correct version is on PyPI and you can work
with that version via pip (e.g. `pip freeze`). But if you import the package
via `import [yourpackage]` and execute `[yourpackage].__version__` it might not
be present. Also, if you have a command line application, you have to make sure
yourself that there is a `--version` command. And you definitely should do
that; it comes in handy.

There is an [official guide](https://packaging.python.org/guides/single-sourcing-package-version/)
for "single-sourcing the package version". So it is a know problem with known
solutions. I only wrap them up here.


## The Manual Approach

setup.py:

```
from setuptools import setup

setup(version='0.1.2')
```

[yourpackage]/__init__.py:

```
__version__ = '0.1.2'
```

Positive:

* No new dependencies
* It is super simple to understand

Negative:

* You can easily get inconsistencies by forgetting something


## Version Python File

setup.py:

```
from setuptools import setup

exec(open('[yourpackage]/_version.py').read())

setup(version=__version__)
```

[yourpackage]/__init__.py:

```
from [yourpackage]._version import __version__
```

[yourpackage]/_version.py:

```
__version__ = '0.1.2'
```


Positive:

* No new dependencies
* Relatively simple
* Consistent

Negative:

* You use `exec`, about which linters complain as it is a security risk if used
  wrong.
* `mypy` cannot know that the `__version__` variable is set in the `setup.py`.
  It will give `error: Name '__version__' is not defined`.


## Version Text File

Similar to the solution above, we use a text file which only contains the
version string.

setup.py:

```
from setuptools import setup

def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

setup(version=read('[yourpackage]/version.txt'))
```

[yourpackage]/__init__.py:

```
from [yourpackage]._version import __version__
```

[yourpackage]/_version.py:

```
__version__ = '0.1.2'
```


## Reading setup.py

This approach is so bad that I don't want to post an example here. The idea
is that you can have the version in the `setup(version='fooversion')` and read
that within the package to set the `__version__`.

Reasons why I strongly suggest not to do so:

* Your package source could be simply copied, not installed. For example, if
  things run on AWS Lambda. In this case, there is not `setup.py` file. So all
  solutions with this break.
* You have to write rather complex parsers to be robust to changes in
  `setup.py`


## External Build Tools

There are [bumpversion](https://pypi.org/project/bumpversion/),
[changes](https://pypi.org/project/changes/) and [zest.releaser](https://pypi.org/project/zest.releaser/).
I don't have experience with those tools, but from a very quick first look I
don't think they the first two look reliable enough to give them a try. And
`zest.releaser` looks a bit complicated.


## Package import


setup.py:

```
from setuptools import setup

import [yourpackage]

setup(version=[yourpackage].__version__))
```

[yourpackage]/__init__.py:

```
[yourpackage]._version = '0.1.2'
```

Positive:

* No new dependencies
* Very simple simple
* Consistent

Negative:

* Fails, if you import a dependency in the `__init__.py`.


## Version Control Integration

You can use [`setuptools_scm`](https://pypi.org/project/setuptools_scm/)
and do the following:


setup.py:

```
from setuptools import setup

setup(
    ...,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    ...,
)
```

[yourpackage]/__init__.py:

```
from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
```

Positive:

* git tags: You might have to / be able to use git tags to keep consistent
  versions. I'm not sure if this is the case, though.

Negative:

* Your package source could be simply copied, not installed. For example, if
  things run on AWS Lambda. In this case, there is not `setup.py` file. So all
  solutions with this break.

Reading [Version String Management in Python: Introducing python-versioneer](https://blog.mozilla.org/warner/2012/01/31/version-string-management-in-python-introducing-python-versioneer/), I want to highlight some parts:

> Thinking about how I use git these days, I realized that I want my release
> process to have one step: “git tag” (well, and a “git push” to tell the world
> about it). Everything else should be automated: building tarballs, uploading
> them to a release server, updating a web page, sending an announcement email,
> pypi registration, etc. What really matters is the release manager making the
> decision to bless some well-tested revision id with a public name of some
> sort.


## What others do


<table>
    <tr>
        <th>Package</th>
        <th>setup.py</th>
        <th>package</th>
        <th>Versioning Scheme</th>
    </tr>
    <tr>
        <td>Scipy</td>
        <td>Manual</td>
        <td>?</td>
        <td>Semantic</td>
    </tr>
    <tr>
        <td>Numpy</td>
        <td>Manual</td>
        <td>?</td>
        <td>Semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/python-pillow/Pillow">Pillow</a></td>
        <td>exec py</td>
        <td>manual</td>
        <td>Semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/boto/boto3">boto3</a></td>
        <td>regex `__init__.py`</td>
        <td>manual</td>
        <td>Semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/SethMMorton/natsort">natsort</a></td>
        <td>manual</td>
        <td>manual</td>
        <td>semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/matplotlib/matplotlib">mantplotlib</a></td>
        <td>versioneer</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://github.com/pandas-dev/pandas">Pandas</a></td>
        <td>versioneer</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://github.com/scikit-learn/scikit-learn">scikit-learn</a></td>
        <td>import of sklearn.__version__</td>
        <td>manual</td>
        <td>semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/tensorflow/tensorflow">tensorflow</a></td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://github.com/pytorch/pytorch">pytorch</a></td>
        <td>manual</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td>seaborn</td>
        <td>manual</td>
        <td>manual</td>
        <td>semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/pallets/flask">Flask</a></td>
        <td>regex `__init__.py`</td>
        <td>manual</td>
        <td>semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/django/django">Django</a></td>
        <td>import of django.__version__</td>
        <td>manual</td>
        <td>semantic</td>
    </tr>
    <tr>
        <td><a href="https://github.com/pytest-dev/pytest">pytest</a></td>
        <td>`use_scm_version`</td>
        <td>?</td>
        <td>?</td>
    </tr>
    <tr>
        <td><a href="https://github.com/tox-dev/tox">tox</a></td>
        <td>`use_scm_version`</td>
        <td>pluggy</td>
        <td></td>
    </tr>
</table>


## See also

* [Brian Warner](https://github.com/warner): [Version String Management in Python: Introducing python-versioneer](https://blog.mozilla.org/warner/2012/01/31/version-string-management-in-python-introducing-python-versioneer/)
