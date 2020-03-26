---
layout: post
title: Virtual Environments
slug: virtual-environments
author: Martin Thoma
date: 2020-02-08 20:00
category: Code
tags: Python, venv, virtualenv
featured_image: logos/python.png
---
A virtual environment is an isolated Python environments. It has it's own
installed `site-packages` which can be different from the systems
`site-packages`.

TL;DR: `pipenv` is your friend; it allows you to forget about the others.

## virtualenv

`virtualenv` was created by Ian Bicking. The first version on PyPI is from
2007.

## pyvenv

Was deprecated in favour of `python -m venv`. It was removed with Python 3.8.

## venv

The [`venv` module](https://docs.python.org/3/library/venv.html) was
added in Python 3.3 with [PEP 405](https://www.python.org/dev/peps/pep-0405/)
(2012).

## pyenv

pyenv lets you switch between multiple versions of Python.

Installation: See [GitHub](https://github.com/pyenv/pyenv#installation)

Usage:

```shell
$ pyenv install --list
Available versions:
  2.1.3
  [...]
  3.8.1
  3.9-dev
  activepython-2.7.14
  activepython-3.5.4
  activepython-3.6.0
  anaconda-1.4.0
  [... a lot more; including anaconda, miniconda, activepython, ironpython, pypy, stackless, ....]

$ pyenv install 3.8.1
Downloading Python-3.8.1.tar.xz...
-> https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
Installing Python-3.8.1...
Installed Python-3.8.1 to /home/moose/.pyenv/versions/3.8.1

$ pyenv versions
* system (set by /home/moose/.pyenv/version)
  2.7.16
  3.5.7
  3.6.9
  3.7.4
  3.8-dev

$ python --version
Python 2.7.17
$ pip --version
pip 19.3.1 from /home/moose/.local/lib/python3.6/site-packages/pip (python 3.6)

$ mkdir pyenv-experiment && echo "3.8.1" > "pyenv-experiment/.python-version"
$ cd pyenv-experiment

$ python --version
Python 3.8.1
$ pip --version
pip 19.2.3 from /home/moose/.pyenv/versions/3.8.1/lib/python3.8/site-packages/pip (python 3.8)
```


## pipenv

[`pipenv`](https://github.com/pypa/pipenv) automatically creates and manages a
virtualenv for your projects, as well as adds/removes packages from your
Pipfile as you install/uninstall packages. It also generates the Pipfile.lock,
which is used to produce deterministic builds. It helps creating reproducible
environments.

`pipenv` uses `virtualenv` and `pyenv`.

### Usage

First, create a virtual environment:

```shell
$ pipenv --python 3.8
Creating a virtualenv for this project…
Pipfile: /home/moose/GitHub/clana/Pipfile
Using /home/moose/.pyenv/versions/3.8.1/bin/python3.8 (3.8.1) to create virtualenv…
⠏ Creating virtual environment...Already using interpreter /home/moose/.pyenv/versions/3.8.1/bin/python3.8
Using base prefix '/home/moose/.pyenv/versions/3.8.1'
New python executable in /home/moose/.local/share/virtualenvs/clana-oPEDiD9W/bin/python3.8
Also creating executable in /home/moose/.local/share/virtualenvs/clana-oPEDiD9W/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /home/moose/.pyenv/versions/3.8.1/bin/python3.8

✔ Successfully created virtual environment! 
Virtualenv location: /home/moose/.local/share/virtualenvs/clana-oPEDiD9W
requirements.txt found, instead of Pipfile! Converting…
✔ Success! 
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
```

Activate the environment:

```shell
$ pipenv shell
Launching subshell in virtual environment…
 . /home/moose/.local/share/virtualenvs/clana-oPEDiD9W/bin/activate

$ pip --version
pip 20.0.2 from /home/moose/.local/share/virtualenvs/clana-oPEDiD9W/lib/python3.8/site-packages/pip (python 3.8)
```

Set your `Pipfile.lock`:

```shell
$ pipenv lock
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (310e7d)!
```

Make sure your environment has exactly the stuff installed that you need:

```shell
$ pipenv sync
Installing dependencies from Pipfile.lock (310e7d)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 14/14 — 00:00:06
All dependencies are now up-to-date!
```

## Docker

If you want more isolation, have a look at [Docker](https://martin-thoma.com/docker/).
I use the [`python:3.8-slim-buster`](https://hub.docker.com/_/python) (February 2020).

The `Dockerfile` can then look like this:

```dockerfile
FROM python:3.8-slim-buster

# Update and install extra packages
RUN apt-get update && apt-get install -y git build-essential

# Install project dependencies
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

# Install project
COPY . /opt/app
RUN pip install . --no-deps
```

## See also

* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
* [What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/a/41573588/562769)
* [Generate requirements.txt from Pipfile.lock](https://github.com/pypa/pipenv/issues/3493#issuecomment-511708312)
* [`virtualenvwrapper`](https://pypi.org/project/virtualenvwrapper/): extensions to virtualenv
