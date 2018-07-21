---
layout: post
title: Stages of Software Development
slug: software-development-stages
author: Martin Thoma
date: 2018-06-09 20:00
category: Code
tags: Software Development
featured_image: logos/code.png
---
Pythons Trove Classifiers have 7 stages of software development:

```
Development Status :: 1 - Planning
Development Status :: 2 - Pre-Alpha
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
Development Status :: 6 - Mature
Development Status :: 7 - Inactive
```

In this mini-article I try to describe what those stages are.


## Semantic Versioning

There are a couple of different ways to set a version string:

* git hash: `409b48b0d49c6b5d82ec8711b9341fc99b31ff98`
* Counting upwards: `1`, `2`, `3`, ...
* Yearly versions:
    * Ubuntu: `16.04`, `16.10`, `17.04`, `17.10`, ...
    * [pytz](https://pypi.org/project/pytz/): `2016.10`, `2017.2`, `2017.3`, `2018.3`, `2018.4`, ...
* Semantic versioning: `0.19.1`, `1.0.0`, `1.0.1`, `1.1.0`,... as used by [scipy](https://github.com/scipy/scipy/releases)

git hashes are only there to have an identifier for a commit which can be
(ab)used as a version string. The other versioning ways are better because
you can directly see which version is more recent.

Yearly versions and semantic versioning are better than simply counting
upwards, because the version string carries additional information. Instead of
only knowing that something is the next version, you either know how much time
has passed or which type of change was done.

I suggest taking 5 minutes to read [semver.org](https://semver.org), but the
bare minimum you need to know about it is:

```
Given a version number MAJOR.MINOR.PATCH, increment the:

MAJOR version when you make incompatible API changes,
MINOR version when you add functionality in a backwards-compatible manner, and
PATCH version when you make backwards-compatible bug fixes.
```


## Development Stages

### 1 - Planning
Having this trove classifier online basically means you only reserved the name
on PyPI.

* **Required properties**: There is no software package, no content whatsoever.
* **Typical steps**: Creating wireframes (e.g. with [Balsamiq](https://balsamiq.com)),
  drafting architectures and expected workflows (e.g. UML diagrams), writing user
  stories, defining features, defining which features NOT to have
* **Semantic version**: -
* **[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+1+-+Planning)**: 2172 projects - noting I know of


### 2 - Pre-Alpha
* **Required properties**: There is already some software that gives an idea what
  it is supposed to do.
* **Typical steps**: Drafting ideas, adding new features, refactoring a lot.
  Here, the complete architecture of the software might still change.
* **Semantic version**: 0.X.X
* **[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+2+-+Pre-Alpha)**: 5067 projects - noting I know of


### 3 - Alpha
* **Required properties**: The software has the minimal required set of features
  to be useful. The architecture of the software is clear.
* **Typical steps**: Internal testing. People close to the developers can use
  the software.
* **Semantic version**: 0.X.X
* **[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+3+-+Alpha)**: 10,000+ projects, including [Lasagne](https://pypi.org/project/Lasagne/)


### 4 - Beta
* **Required properties**: Software is feature complete
* **Typical steps**: External testing, fixing bugs and performance problems.
  Usability testing.
* **Semantic version**: 0.X.X
* **[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+4+-+Beta)**: 10,000+ projects, including [pint](https://pypi.org/project/Pint/)


### 5 - Production/Stable
* **Required properties**: No major bugs known, tests cover the most important
  cases.
* **Typical steps**: Fixing bugs, adding updates and new features.
* **Semantic version**: ≥ 1.0.0
**[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+5+-+Production%2FStable)**: 10,000+ projects, including [SQLAlchemy](https://pypi.org/project/SQLAlchemy/), [numpy](https://pypi.org/project/numpy/), [pandas](https://pypi.org/project/pandas/)


### 6 - Mature
* **Required properties**: Software was in production for more than a year. No
  new features were required, no major/critical bugs are open.
* **Typical steps**: Fixing minor bugs.
* **Semantic version**: ≥ 1.0.0
* **[PyPI](https://pypi.org/search/?c=Development+Status+%3A%3A+6+-+Mature)**: 415 projects, including [Zope](https://en.wikipedia.org/wiki/Zope), [pytz](https://pypi.org/project/pytz/) and [Pillow](https://pypi.org/project/Pillow/)


### 7 - Inactive
At some point the developers will not add updates to software. Maybe it was a
free-time project and they are not interested in it anymore. Maybe the company
doesn't get enough money from that project. It can still be valuable to keep
the software in the repository. Marking it as "inactive" tells developers that
it's unlikely known issues will be fixed.

**[PyPI](https://pypi.org/search/?q=&o=&c=Development+Status+%3A%3A+7+-+Inactive)**: 283 projects, including

* [async](https://pypi.org/project/async/): deprecated
* [aws-cyrpto](https://pypi.org/project/aws-cyrpto/), [aws-crytpo](https://pypi.org/project/aws-crytpo/), [awscrytpo](https://pypi.org/project/awscrytpo/): Trying to prevent users from typos
* [bs4](https://pypi.org/project/bs4/): A dummy package
* [`image_cleaner`](https://pypi.org/project/image_cleaner/), [`memtop`](https://pypi.org/project/memtop/), [`asr`](https://pypi.org/project/asr/), [`pyspell`](https://pypi.org/project/pyspell/), [`lumixmaptool`](https://pypi.org/project/lumixmaptool/), [`hwrt`](https://pypi.org/project/hwrt/), [`geocodertools`](https://pypi.org/project/geocodertools/), [TensorVision](https://github.com/TensorVision/TensorVision), [`vin_decoder`](): Projects I'm no longer interested in

Important to note here: It is, of course, always possible that it switches back
to any of the other development stages


## See also

* Coding Horror: [Alpha, Beta, and Sometimes Gamma](https://blog.codinghorror.com/alpha-beta-and-sometimes-gamma/)
* Wikipedia: [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
