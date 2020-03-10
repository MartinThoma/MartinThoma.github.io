---
layout: post
title: Migrate to Python 3
slug: migrate
author: Martin Thoma
date: 2020-03-10 20:00
category: My bits and bytes
tags: Python, Migration
featured_image: logos/python.png
---
When I gave a Python Packaging Course, I advised my students to always use Python 3.
After all, [Python 2 is dead](https://pythonclock.org/). But one student said
she had to use Python 2 as there is a package she definitely needs to use. And
it's Python 2 only. What can one do in such a scenario?

I see the following options:

1. Ask the maintainer to move the package
2. Create a fork and move the package yourself
3. Use an interface

Don't forget to be polite when you ask. After all, you want something. And
you're most likely asking somebody who does this in their free-time.

When you have a program which has an interface (e.g. a web API like REST or a
command line interface), then you can execute it with Python 2 from Python 3.
Basically doing a system-level call, e.g. with
[`os.system`](https://docs.python.org/2/library/os.html#os.system). That is
rarely the case and pretty straight forward. So let's come to the interesting
part: Forking a package.


## Naming

The package [`propy`](https://code.google.com/archive/p/protpy/downloads) was
not maintained anymore and the original authors didn't reply. So I chose to
create a fork which I wanted to work with Python 3.

I thought about just keeping the name, but [`propy` on PyPI](https://pypi.org/project/propy/)
was already taken by an unrelated project. And, after all, making sure there
is some difference might not be the worst idea.

So I chose the name [propy3](https://pypi.org/project/propy3/) - a Python 3
compatible version of propy.


## Structure

I want all my projects to have this structure:

```
propy3
├── docs
│   ├── Makefile
│   ├── requirements.txt
│   └── source
├── Makefile
├── MANIFEST.in
├── propy
│   └── __init__.py
├── README.md
├── setup.cfg
├── setup.py
├── tests
└── tox.ini
```

with a setup.py like this:

```python
from setuptools import setup

setup()
```

and a setup.cfg like this:

```ini
[metadata]
# https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files
name = propy3
version = 1.0.0a2
author = Dongsheng Cao
author_email = oriental-cds@163.com
maintainer = Martin Thoma
maintainer_email = info@martin-thoma.de

license = GPL

url = http://cbdd.csu.edu.cn/index

description = Compute protein descriptors
long_description = file: README.md
long_description_content_type = text/markdown

keywords = Bio-Informatics, Protein

classifiers =
    License :: OSI Approved :: GNU General Public License (GPL)
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Topic :: Scientific/Engineering :: Bio-Informatics

[options]
include_package_data = True
packages = find:

[tool:pytest]
addopts = --doctest-modules --mccabe --cov=./propy --cov-append --cov-report html:tests/reports/coverage-html --cov-report xml:tests/reports/coverage.xml --cov-report term --flake8 --ignore=docs/ --ignore=propy/__main__.py --durations=3 --black
doctest_encoding = utf-8

# Just temporarily: Increase from 10 to 25
mccabe-complexity=25

[pydocstyle]
convention=numpy
match_dir = propy

[flake8]
match_dir = propy
max-line-length = 80
select = C,E,F,W,B,B950
# Just temporarily: E731
ignore = E501,W503,E203, E731

[mypy]
ignore_missing_imports=true
check_untyped_defs=true
disallow_untyped_defs=false
warn_redundant_casts=true
warn_unused_configs=true
disallow_untyped_calls=false
follow_imports=skip
mypy_path=typeshed/pyi:typeshed/imports
```

## General Cleanup

1. Move documentation to `/docs`
2. Remove generated files and add a [`.gitignore` file](https://www.gitignore.io/)
2. Apply [`black`](https://github.com/psf/black)
3. Apply [`isort`](https://github.com/timothycrosley/isort)
4. Remove trailing spaces


I do this by putting the following `.pre-commit-config.yaml` file in the root
directory of the project:

```
# pre-commit run --all-files
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/asottile/seed-isort-config
    rev: v1.9.3
    hooks:
    -   id: seed-isort-config
        args: [--application-directories=app]
-   repo: https://github.com/pre-commit/mirrors-isort
    rev: v4.3.21
    hooks:
    -   id: isort
-   repo: https://github.com/psf/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.6
```

And then executing `pre-commit run --all-files`.


## 2to3

The tool [2to3](https://docs.python.org/3/library/2to3.html) can help to make
the move.

However, it is not optimal:

* [It adds too many paranthesis for print sometimes](https://stackoverflow.com/q/55559825/562769)
* It sometimes wraps zip / map / filter unnecessarily in a `list`


## Unit Tests

Setting up pytest and continuous integration (e.g. Travis) is pretty helpful


## Sphinx and ReadTheDocs

Might help to make the tool discoverable.
