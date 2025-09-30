---
layout: post
lang: en
title: Python Projects
slug: python-projects
author: Martin Thoma
date: 2018-01-18 20:00
category: Code
tags: Architecture, Software Engineering, Python
featured_image: logos/python.png
---
I recently thought a bit about what makes software good. Not from a functional
perspective, but from a developers perspective. As I did quite some work with
data science, machine learning and Python my view is a bit biased. Having said
that, here is my personal "best practices" guide.


## Naming

> There are 2 hard problems in computer science: cache invalidation, naming
> things, and off-by-1 errors.

I prefer names which have the following properties:

* They can't be confused with something else and the name is available at PyPI.
  I'm looking at you, GTK ([source](https://stackoverflow.com/q/44213921/562769)).
* They are short, but can be googled. Looking at you `R`, `Go` and `C`.
* They are completely lowercase: Please don't make me think how to import your
  package. Is it `pypdf2`, `PyPDF2`, `pyPDF2`?
* They are either max 4 letters or pronouncable. Something like `tensorflow` is
  longer, but that's ok because I remember it as one thing. `lidtk` is
  borderline as I remember it as `lid..tk` - how I say it.

For now, assume your module is called `foo_module`


## Project structure

```text
foo_module : the git repository root dir
├── configs
│   └── module.yaml
├── docker-compose.yml
├── Dockerfile
├── foo_module
│   ├── api.py
│   ├── cli.py
│   ├── config.yaml
│   ├── controller.py
│   ├── credentials.yaml
│   ├── __init__.py
│   └── utils.py
├── tox.ini
├── README.md
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    └── test_utils.py
```

* Having a `Dockerfile` and a `docker-compose.yml` might be nice if you have
  not purely Python dependencies. See [my Docker article](https://martin-thoma.com/docker/).

the `foo_module/__init__.py` should look like this:

```python
from pkg_resources import get_distribution

try:
    __version__ = get_distribution("lidtk").version
except:
    __version__ = "Not installed"
```


The `setup.py` should look like this:

```python
from setuptools import find_packages
from setuptools import setup

config = {
    "install_requires": ["click>=6.7", "numpy>=1.14.0", "scipy>=1.0.0"],
    "tests_require": ["pytest>=3.3.2", "pytest-cov>=2.5.1", "pytest-pep8>=1.0.6"],
    "keywords": ["Machine Learning", "Data Science"],
    "download_url": "https://github.com/MartinThoma/language-identification",
    "classifiers": [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    "zip_safe": True,
}

setup(**config)
```

The `cli.py` could look like this:

```python
#!/usr/bin/env python

# Third party modules
import click

# First party modules
import foo_module


@click.group()
@click.version_option(version=foo_module.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
```

The setup.cfg should look like this:

```ini
[metadata]
name = foo_module
version = 0.1.0

author = Martin Thoma
author_email = info@martin-thoma.de
maintainer = Martin Thoma
maintainer_email = info@martin-thoma.de

platforms = Linux

url = https://github.com/MartinThoma/language-identification
license = MIT
description = Language identification Toolkit
long_description = file: README.md
long_description_content_type = text/markdown

[options]
packages = find:

[options.entry_points]
console_scripts =
    foo_module = foo_module.cli:entry_point

[tool:pytest]
addopts = ./tests/ --doctest-modules --cov=./foo_module --cov-report html:tests/reports/coverage-html --pep8
doctest_encoding = utf-8

[pydocstyle]
ignore = D104, D413, D212, D100
match_dir = foo_module
```


## Documentation

Documentation is important as Python does not have type information directly
visible in the code. So you want all functions to **have a Docstring** which
documents which type the parameter and the return value has.
Decide on a format. I like the [numpydoc convention](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).
Stick to that.

Every project should **have a README.md** which answers the following questions:

1. What is the project about?
2. What do I need to run it?
3. Usage example
4. Developer guide:
    1. What are TODOs / where can I find them?
    2. How do I run the tests


## Logging

Use the [`logging`](https://docs.python.org/3/library/logging.html) library.

Add the logging configuration to the modules configuration file (`configs/module.yaml`):

```yaml
LOGGING:
  version: 1
  disable_existing_loggers: False
  formatters:
      simple:
          format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

  handlers:
      console:
          class: logging.StreamHandler
          level: DEBUG
          formatter: simple
          stream: ext://sys.stdout

      info_file_handler:
          class: logging.handlers.RotatingFileHandler
          level: INFO
          formatter: simple
          filename: lidtk.info.log
          maxBytes: 10485760 # 10MB
          backupCount: 20
          encoding: utf8

      error_file_handler:
          class: logging.handlers.RotatingFileHandler
          level: ERROR
          formatter: simple
          filename: lidtk.errors.log
          maxBytes: 10485760 # 10MB
          backupCount: 20
          encoding: utf8

  loggers:
      my_module:
          level: ERROR
          handlers: [console]
          propagate: no

  root:
      level: INFO
      handlers: [console, info_file_handler, error_file_handler]
```

In your main script `bin/foo_module`, you should load this:

```python
# core modules
import logging.config
import pkg_resources
import yaml

filepath = pkg_resources.resource_filename("foo_module", "configs/module.yaml")
with open(filepath, "r") as stream:
    config = yaml.load(stream)
logging.config.dictConfig(config["LOGGING"])
```


## Tests

Tests are written for three purposes:

1. *Correctness*: Having more tests gives you more certainty that you actually
   did the right thing.
2. *Documentation*: If documentation is bad, developers can have a look at your
   tests. They might show what was not directly doucmented.
3. *Flexibility*: Once another developer gets to see code which is used in
   production, one hasitates to change it. You might break things. Having many
   tests and a high test coverage gives the project more flexibility as people
   see faster where things break. And keep in mind: That future developer might
   be yourself, after not having worked with your code for a while.

Use [`pytest`](https://docs.pytest.org/en/latest/) and [`tox`](http://tox.readthedocs.io/en/latest/index.html).
The `tox.ini` should look like this:

```ini
[tox]
envlist = py35, py36
skip_missing_interpreters = true

[testenv]
deps =
    pytest
    pytest-cov
    pytest-pep8
    pydocstyle
commands =
    pip install -e .
    pytest .
    pydocstyle
```


## Anti-Patterns

### Print vs Logging

* `logging.XY(msg)` should be used, when there is information about the flow
  of the program. The reason for having logging is to analyze why something
  went wrong or if everything went right. So debugging / monitoring.
* `print(msg)` should be used, when there is output by the program. So output
  that is the purpose of the program. The purpose of `print(msg)` is as the
  message is why the user called the program in the first place.

What I do quite often is to print stuff when I should actually use
`logging.debug(msg)`. I want to change it.


### assert vs Exception

To quote from [softwareengineering.stackexchange.com](https://softwareengineering.stackexchange.com/a/15518/25699):

> **Assertions** should only be used to verify conditions that should be
> logically impossible to be false (read: **sanity checks**). These conditions
> should only be based on inputs generated by your own code. Any checks based
> on external inputs should use exceptions.
>
> A simple rule that I tend to follow is verifying private functions' arguments
> with asserts, and using **exceptions for public/protected functions**'
> arguments.


### setup.py vs requirements.txt

The `setup.py` file defines abstract dependencies. `pip install` will look at
those and try to install them, if some are missing.

The `requirements.txt` is for deployment. It has concrete dependencies.

If you don't need this distinction, you can make a `requirements.txt` like this:

```text
--index-url https://pypi.python.org/simple/

-e .
```

See [this blogpost](https://caremad.io/posts/2013/07/setup-vs-requirement/) for
details.


### Multiple __main__

A Python package should at most contain one `__main__`. That should be the
`bin/foo_module`. All other files should either be pure "library files" or be
connected to the main command. I like [`click`](http://click.pocoo.org/6/) for
creating the CLI. See my [clana project](https://github.com/MartinThoma/clana)
as an example.


### Comments

Once in a while, I see many comments when there should be refactoring. If you
have to explain things, there might be a couple of reasons for it:

* Something is unintuitive. Make it intuitive.
* It's too complicated. Make it simpler. For example, split the function up.
* Your naming is bad. Rename your variables / functions.
* The damn thing is just complicated. You actually need a comment to clarify.


### Outdated dependencies

Check your dependencies with `piprot requirements.txt`.


### Bad package structure

Check your package with [`pyroma .`](https://github.com/regebro/pyroma).
