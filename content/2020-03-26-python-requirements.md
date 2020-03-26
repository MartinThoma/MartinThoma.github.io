---
layout: post
title: Python Requirements
slug: python-requirements
author: Martin Thoma
status: draft
date: 2020-01-08 20:00
category: Code
tags: Python, setup.py, requirements.txt, Software Development
featured_image: logos/star.png
---
Pythons package management is a constant source of confusion. There are [too many tools](https://stackoverflow.com/q/25337706/562769). [xkcd](https://xkcd.com/1987/) shows this pretty well:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="https://xkcd.com/1987/"><img src="https://imgs.xkcd.com/comics/python_environment.png" alt="The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages." style="width: 512px;"/></a>
    <figcaption class="text-center">xkcd The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages. (<a href="https://www.explainxkcd.com/wiki/index.php/1987:_Python_Environment">explanation</a>)</figcaption>
</figure>

## Glossary

The following is mostly taken from Wikipedia and <a href="https://docs.python.org/3/glossary.html">the Python glossary</a>:

<dl>
    <dt>Interpreter</dt>
    <dd>An interpreter is a computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program. <a href="https://en.wikipedia.org/wiki/CPython">CPython</a> is the standard Python interpreter.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop">REPL</a>, <dfn>Interactive Console</dfn></dt>
    <dd>A read–eval–print loop (REPL) is an interactive computer programming environment that takes single user inputs (i.e., single expressions), evaluates (executes) them, and returns the result to the user; a program written in a REPL environment is executed piecewise. When you just enter <code>python</code> in the console, then you start an interactive console.</dd>
    <dt>Script</dt>
    <dd>A single file that the interpreter can use as input and execute.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/Namespace">Namespace</a></dt>
    <dd>The place where a variable is stored. A namespace ensures that all the identifiers within it have unique names so that they can be easily identified</dd>
    <dt><a href="https://docs.python.org/3/tutorial/modules.html">Module</a></dt>
    <dd>An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing. A module is a <code>.py</code> file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__</dd>
    <dt><a href="https://docs.python.org/3/tutorial/modules.html#packages">Package</a></dt>
    <dd>A package is a folder with an <code>__init__.py</code> file. A package is a Python module with an <code>__path__</code> attribute.</dd>
    <dt>Subpackage</dt>
    <dd>If package B is contained in package A, then B is called a <dfn>subpackage</dfn> of A.</dd>
</dl>


## What we need

It's often easier to understand something if you had the same need as the
developers had when they created it. Imagine we start with an interactive console.
In principle, this is Python. But what if...

1. We want to be able to store functions/objects for later use: We need a **Python script**
2. We want to be able to group functions/objects to avoid naming colisions (open!): We need **Python modules**
3. We want to organize modules: We need **Python packages** which means we need a `__init__.py` file
4. We don't want to remember where packages are and we don't want to manipulate the [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path):
    * Install packages, e.g. with `pip`
    * Add a `setup.py`
        * [`distutils`](https://docs.python.org/3/library/distutils.html#module-distutils) (deprecated, use setuptools) - same for [`distribute`](https://pypi.org/project/distribute/0.7.3/) and [`distutils2`](https://pypi.org/project/Distutils2/)
        * [`setuptools`](https://setuptools.readthedocs.io/en/latest/)
            * declare dependencies
    * Metadata
        * [README](https://martin-thoma.com/python-projects/#documentation)
        * [License](https://tldrlegal.com/)
5. Create a package sceleton: [cookiecutter](https://github.com/MartinThoma/cookiecutter-python-package)

### Case 1: Writing a runnable

In this case, I mean anything that should be directly executed. It could be a
web service, it could be a command line program or something with a GUI.

6. We want our exact results to be repeatable (reproducibility): Version pinning in [requirements.txt](https://packaging.python.org/discussions/install-requires-vs-requirements/#requirements-files)
7. Dependencies of our dependencies might break: Version pinning of sub-dependencies with <code>pip freeze</code>, <code>pip-tools</code>
8. We don't want to maintain security updates: [pipenv](https://github.com/pypa/pipenv) (Pipfile / Pipfile.lock)

<table class="table">
    <thead>
    <tr>
        <th>Language</th>
        <th>Specification file for libraries</th>
        <th>Desired dependencies</th>
        <th>Locked dependencies</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Python</td>
        <td>setup.py</td>
        <td>Pipfile</td>
        <td>Pipfile.lock</td>
    </tr>
    <tr>
        <td>Ruby</td>
        <td>.gemspec</td>
        <td>Gemfile</td>
        <td>Gemfile.lock</td>
    </tr>
    <tr>
        <td>Rust</td>
        <td>Cargo.toml</td>
        <td>Cargo.toml</td>
        <td>Cargo.lock</td>
    </tr>
    </tbody>
</table>

### Case 2: Writing a Framework / Library

6. We want to share packages: PyPI as a package hosting service, `twine` as a program to upload
7. Different packages might need different versions of the same library, hence we want virtual environments: `virtualenv`


## Distribution formats

There are **source distributions** (sdist) and **built distributions** (bdist,
sometimes also called "binary distribution"). The format is usually [wheel](https://www.python.org/dev/peps/pep-0427/) (egg exists as well).


### Egg

* Contains .pyc files (might even only be that!) which could be incompatible
  with your python version

### Wheel

* Only Python Code
* May Target a Python version



## Dependency Formats

There are two common formats to denote dependencies: Within the `setup.py` and
`requirements.txt` files.

`setup.py` is used to install packages, whereas `requirements.txt` files are
used to prepare a development environment.

As an alternative to `requirements.txt`, you can use `Pipfile` + `Pipfile.lock`.
However, the `requirements.txt` is still the de facto standard.


### requirements.txt

The structure of a `requirements.txt` file is super simple:

```text
virtualenv==15.1.0
visitor==0.1.3
vtk==8.1.1
wadllib==1.3.2
watchdog==0.8.3
wcwidth==0.1.7
webencodings==0.5.1
websocket-client==0.54.0
Werkzeug==0.15.2
widgetsnbextension==3.3.0
wily==1.12.2
```

One line of the format `[package]==[version]`per requirement.

It can be installed via

```shell
$ pip install -r requirements.txt
```

It is meant to be used: TODO


There are nice tools like `piprot` which tells you how outdated the requirements are.


### setup.py

I usually end up using something like the following:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""mpu: Martins Python Utilities."""

# Core Library
import io
import os

# Third party
from setuptools import find_packages, setup


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(
        os.path.join(os.path.dirname(__file__), file_name), encoding="utf-8"
    ) as f:
        return f.read()


requires_datetime = ["pytz"]
requires_image = ["Pillow"]
requires_io = ["pytz", "tzlocal"]
requires_aws = ["boto3"]
requires_tests = [
    "pytest",
    "pytest-cov",
    "pytest-mccabe",
    "pytest-flake8",
    "simplejson",
]
requires_all = (
    ["pandas", "python-magic"]
    + requires_datetime
    + requires_image
    + requires_io
    + requires_aws
    + requires_tests
)

setup(
    name="mpu",
    version="0.21.0",  # keep in sync with mpu/_version.py
    author="Martin Thoma",
    author_email="info@martin-thoma.de",
    maintainer="Martin Thoma",
    maintainer_email="info@martin-thoma.de",
    packages=find_packages(),
    package_data={"mpu": ["units/currencies.csv", "data/*", "package/templates/*"]},
    extras_require={
        "all": requires_all,
        "aws": requires_aws,
        "datetime": requires_datetime,
        "image": requires_image,
        "io": requires_io,
        "tests": requires_tests,
    },
    tests_require=requires_tests,
    platforms=["Linux"],
    url="https://github.com/MartinThoma/mpu",
    license="MIT",
    description="Martins Python Utilities",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=[],
    keywords=["utility"],
    download_url="https://github.com/MartinThoma/mpu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    zip_safe=True,
)
```

For quite a while, I did create a `config` dictionary and used
`setup(**config)`. However, I'm not sure if this adds any benefit.


## Create requirements.txt

In order to create a `requirements.txt` where the requirements are pinned down,
even for requirements of my requirements, I usually do this:

### pip freeze

```shell
$ virtualenv venv
$ source venv/bin/activate

# Add additional targets, if wanted!
$ pip install .

$ pip freeze > requirements.txt
```

### pipreqs

If you think your setup.py might miss something, try [`pipreqs`](https://pypi.org/project/pipreqs/):

```shell
$ pip install pipreqs
$ pipreqs /project/path
```

A similar tool is [`pipdeptree`](https://pypi.org/project/pipdeptree/).

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


## See also

* [setuptools vs. distutils: why is distutils still a thing?](https://stackoverflow.com/q/25337706/562769)
* [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56), 07.05.2018.
* [How are Pipfile and Pipfile.lock used?](https://stackoverflow.com/q/46330327/562769)
* [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/#dependency-management-with-requirementstxt)
* [Comparison with Rust and Ruby](https://github.com/pypa/pipfile/issues/27#issuecomment-262264222), 22.11.2016.
* [Why to keep requirements.txt + pip-compile and not go to pipenv + Pipfile](https://github.com/jazzband/pip-tools/issues/679#issuecomment-418251444)
* [Managing Application Dependencies](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies): poetry, hatch, pip-tools
* [A Practical Guide to Using Setup.py](https://blog.godatadriven.com/setup-py)
* [Wheel vs Egg](https://packaging.python.org/discussions/wheel-vs-egg/)
* [The Many Layers of Packaging](http://sedimental.org/the_packaging_gradient.html)
