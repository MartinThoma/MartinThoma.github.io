---
layout: post
title: Python Packaging Course
slug: python-packaging-course
author: Martin Thoma
date: 2020-02-08 20:00
category: Code
tags: Python, git, black, isort
featured_image: logos/python.png
---
The Python Environment is old. Python development started before the internet.
Naturally, such a grown environment is messy:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="https://xkcd.com/1987/"><img src="https://imgs.xkcd.com/comics/python_environment.png" alt="The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages." style="width: 512px;"/></a>
    <figcaption class="text-center">Python Environment</figcaption>
</figure>

In this course, you will learn the details about Python packaging and how all
of the tools related.

## Application Types

* Library: Should be included in other code. It will never be executed
  directly. It does NOT have an entry point.
* CLI Application: Command line applications are supposed to be executed in
  their own environment. It receives input via the CLI, might access local
  storage or make web requests. It could read environment variables. It should
  be started, execute the tasks, and finish. It has an entry point.
* GUI Applications: Similar to command line applications, but with a GUI
  instead of a CLI.
* Service: Similar to a command line application, but it never finishes. It
  just runs in the background.
* Notebooks: Ad-hoc scripts which are primarily used for data analysis.


## Development Environment

I like the ZSH shell with the plugin [Oh My ZSH](https://github.com/ohmyzsh/ohmyzsh)
and [Sublime Text](https://www.sublimetext.com/) as an editor with many
different plugins.

A common alternatives to ZSH are [Fish](https://fishshell.com/). Common
alternatives to Sublime Text are [Atom](https://atom.io/) and [VS Code](https://code.visualstudio.com/).
If you want more, [PyCharm](https://www.jetbrains.com/de-de/pycharm/).

Make sure you have [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [`pipenv`](https://pypi.org/project/pipenv/), [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/installation.html#install-cookiecutter) and [`pre-commit`](https://pre-commit.com/) installed.

## Starting a Project
Suppose you want to develop a new `awesome_project`. Then you create a folder
and make it a git repository:

```
$ cookiecutter https://github.com/MartinThoma/cookiecutter-python-package
full_name [Martin Thoma]:
email [info@martin-thoma.de]:
github_username [MartinThoma]:
project_name [Awesome Project]:
project_slug [awesome_project]:
project_short_description [Awesome Project lets you feel the pure awesomeness of awesome.]:
version [0.1.0]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - Not open source
Choose from 1, 2, 3 (1, 2, 3) [1]:

$ cd awesome_project
$ git init
```

To make sure that a failing hard drive does cause only little loss of work and
to allow collaboration, we add a remote. [Github](https://github.com/)
and [Gitlab](https://about.gitlab.com/) are excellent choices. Once you created
an empty repository there, add it as a remote locally:

```
$ git remote add origin git@github.com:MartinThoma/awesome_project.git
```

Before starting development, it's a good idea to make sure that you don't get
into trouble for having different versions of Python / packages.
[`pipenv`](https://github.com/pypa/pipenv) is my tool of choice. At this point,
using Python 3.8 is a good idea ([current support status of Python versions](https://devguide.python.org/#status-of-python-branches)).

```bash
# Initialize the virtual environment
$ pipenv --python 3.8

# Import the requirements
$ pipenv install -r requirements-dev.txt

# Import the dev requirements
$ pipenv install --dev --pre -r requirements-dev.txt

# Make sure the repository stays that nice
$ pre-commit install
```

### Formatting

By the mentioned cookiecutter template, formatting is to a big extend already
handled:

* [black](https://github.com/psf/black): An opinionated formatter which respects PEP8 and implements a lot of [Flake8](https://flake8.pycqa.org/en/latest/)
* [isort](https://github.com/timothycrosley/isort): Sort imports

The only missing thing is a docstring style formatter. I like the
[numpydoc docstring format](https://numpydoc.readthedocs.io/en/latest/format.html)
a lot.

If you want to know more about formatting, I recommend to read my
[Python style guide](https://martin-thoma.com/python-style-guide/).

### Unit Testing

Before you start testing your application, you should decide which Python version
you want to support. An orientation should be which CPython versions currently
receive security updates (see [SO Question](https://stackoverflow.com/q/60126561/562769)).

Python has multiple testing frameworks. Use [pytest](https://docs.pytest.org/en/latest/).
It's extremely widespread, stable and super simple to use.

The cookiecutter template installs a couple of useful plugins:

* [`pytest-cov`](https://pypi.org/project/pytest-cov/): Generate a test
  coverage report. This helps you to identify sections where bugs cannot
  possibly be catched by a unittest.
* [`pytest-black`](https://pypi.org/project/pytest-black/): Check if black was
  applied.
* [`pytest-flake8`](https://pypi.org/project/pytest-flake8/): Another formatting test.
* [`pytest-mccabe`](https://pypi.org/project/pytest-mccabe/): Check if a
  section of your code might be too complicated.

You might also want to give [`mutmut`](https://pypi.org/project/mutmut/) a try.
It could help you to discover which lines have been checked, but maybe not
thoroughly enough.

To run all of your tests, execute `tox`.


### Documentation

If you develop a library, you need documentation. For the other application
types not so much.

[Sphinx](https://www.sphinx-doc.org/en/master/) as a documentation generator
and [readthedocs.org](https://readthedocs.org/) as a hosting platforms are the
tools of choice.

### Security

If you develop an application, you need to be sure to update your dependencies
if vulnerabilities occur. The package [`bandit`](https://pypi.org/project/bandit/)
and the services [snyk.io](https://snyk.io/) / [pyup.io](https://pyup.io/)
can help you to detect those cases.

### Versions

It is good practice to make `[module].__version__` available. Of course, it
should be the same as the version you see via `pip freeze`. And then it would
be nice if the git commit whould have a [git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

Of course, you can all of that manually. If you want a tool, [bumpversion](https://pypi.org/project/bumpversion/)
is pretty widespread. However, it is not maintained. So some people use [bump2version](https://pypi.org/project/bump2version/).
I'm not too sure if I would use that.


## See also

* Alexander VanTol: [Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/),
* packaging.python.org:
    * Tutorial: [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
    * [Glossary](https://packaging.python.org/glossary/)
* Knewton: [The Nine Circles of Python Dependency Hell](https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025), 2015
* Martin Thoma: [How does Python / pip handle conflicting transitive dependencies?](https://stackoverflow.com/q/60084441/562769), 2020
* [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
* [Tl;DR Legal](https://tldrlegal.com/): Compare licenses
* Conda
    * [Building conda packages from scratch](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html)
    * [Building conda packages with conda skeleton](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html#overview)
    * Martin Thoma: [Is there a point in creating a conda package from an PyPI package?](https://stackoverflow.com/q/59040271/562769), 2019.
