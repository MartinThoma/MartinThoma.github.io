---
layout: post
lang: en
title: pyproject.toml
slug: pyproject-toml
author: Martin Thoma
date: 2019-07-30 20:00
category: Code
tags: Python,packaging
featured_image: logos/python.png
---
The `pyproject.toml` file allows package creators to define the build system as
a dependency as well as a projects metadata.
Also, other kinds of meta-data and the install requirements can be
defined in it.

If you are interested in a sample project, try [pypa/sampleproject](https://github.com/pypa/sampleproject) or try the [packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/).


## Example

```ini
[project]
name = "infer_pyproject"
version = "0.1.0"
description = "Create a pyproject.toml file for an existing project."
authors = [
    {name = "Martin Thoma", email="info@martin-thoma.de"},
    {email = "info@example.com"}
]
license = {file = "LICENSE.txt"}
readme = "README.md"
requires-python = ">=3.6"

keywords = ["packaging", "dependency", "infer", "pyproject.toml"]

classifiers = [
    "Topic :: Software Development"
]

# Requirements: This is done differently by poetry!
dependencies = [
    "Click>=7.0"
]

[project.optional-dependencies]
dev = [
    "black>=18.3-alpha.0",
]

[project.urls]
homepage = "https://github.com/MartinThoma/infer_pyproject"
documentation = "https://github.com/MartinThoma/infer_pyproject"
repository = "https://github.com/MartinThoma/infer_pyproject"

[project.scripts]
poetry = "infer_pyproject.cli:main"

[build-system]
requires = [
    "setuptools >= 35.0.2",
    "setuptools_scm >= 2.0.0, <3"
]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target_version = ['py36']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```


## History

* 1990-08-09: First commit of [cpython](https://github.com/python/cpython/commit/7f777ed95a19224294949e1b4ce56bbffcb1fe9f)
* 1998: distutils was drafted in IPC7 ([source](https://www.python.org/community/sigs/current/distutils-sig/doc/ipc7_devday/))
* 1999-03-22: First [distutil commit to cpython](https://github.com/python/cpython/commit/2689e3ddce7)
* 2000-11-16: [PEP 229 -- Using Distutils to Build Python](https://www.python.org/dev/peps/pep-0229/#implementation)
* 2003-07-06: First capture of pypi.org found on [waybackmachine](https://web.archive.org/web/20030706220147/http://www.pypi.org/)
* 2004-03-19: First commit of [setuptools](https://github.com/pypa/setuptools/commit/8423e1ed14ac1691c2863c6e8cac9230cf558d7b)
* 2006-05-13: First version of [setuptools](https://pypi.org/project/setuptools) was released
* 2007-09-14: First commit of [virtualenv](https://github.com/pypa/virtualenv/commit/e02aa46f4f0eb5321c31641e89bde2c9b92547bb)
* 2008-10-16: First commit of [pip](https://github.com/pypa/pip/commit/c2000d7de68ef955a85cf8f5f6e78d4f25c10103)
* 2013-08-13: First commit of [twine](https://github.com/pypa/twine/commit/fafe960cae661ab9e3ac8837803777ba9aadd831)
* 2015-01-24: First commit of [PyPI warehouse](https://github.com/pypa/warehouse/commit/41358eaf559c1011fc3e94149e716e1dfc79e391)
* 2015-03-16: First version of [flit](https://pypi.org/project/flit) was released
* 2015-09-30: [PEP 517 -- A build-system independent format for source trees](https://www.python.org/dev/peps/pep-0517/) (provisional)
* 2015-10-26: [PEP 516 -- Build system abstraction for pip/conda etc](https://www.python.org/dev/peps/pep-0516/) (rejected)
* 2015-11-11: [PEP 508 -- Dependency specification for Python Software Packages](https://www.python.org/dev/peps/pep-0508/) (active)
* 2016-05-10: [PEP 518 -- Specifying Minimum Build System Requirements for Python Projects](https://www.python.org/dev/peps/pep-0518/) (provisional)
* 2016-11-18: First commit of [pipfile](https://github.com/pypa/pipfile/commit/8bfff2988d0575cacae8a15ae22fd3f9749c5055)
* 2017-01-20: First commit of [pipenv](https://github.com/pypa/pipenv/commit/be4b70e646e6232834e9f9917fdc1adde2156f47)
* 2018-02-28: First version of [Poetry](https://pypi.org/project/poetry) was released
* 2020-06-22: [PEP 621](https://peps.python.org/pep-0621/) - still not supported by poetry in August 2022 ([#3332](https://github.com/python-poetry/poetry/issues/3332))

## Tools

<dl>
    <dt>Python Package</dt>
    <dd>A bundle of software. This includes code and meta-data, such as requirements, a short and a long description, the license. It also contains instructions how to build the software. Formerly this was done with distutils.</dd>
    <dt id="distutils">distutils</dt>
    <dd>Lets you create source distributions (<code>python setup.py sdist</code>). Sometime building takes a long time, so you might want to share already built distributions. You can do that with <code>python setup.py bdist</code>.</dd>
    <dt id="setuptools">setuptools</dt>
    <dd>Like distutils, but a 3rd party library. It is de-facto standard, but does not come with Python.</dd>
    <dt id="setup.py"><code>setup.py</code> <span class="label label-danger">dependency declaration</span></dt>
    <dd>Python file which specifies a package. As it can be arbitrary code, there is no way to know the dependencies of a package for sure without executing <code>setup.py</code>.</dd>
    <dt id="pypi">PyPI (Python Packaging Index) <span class="label label-secondary">software repository</span></dt>
    <dd>PyPI is the official third-party software repository for Python. Here people can share their code in form of Python packages.</dd>
    <dt><code>easy_install</code></dt>
    <dd>Easy_install is a package manager which is replaced by pip, because it could not uninstall and did not know what was installed. Other <a href="https://packaging.python.org/discussions/pip-vs-easy-install/">reasons</a> as well.</dd>
    <dt>egg distribution <span class="label label-primary">distribution format</span></dt>
    <dd>"Egg" is a single-file importable distribution format for Python-related projects. Eggs are to Pythons as Jars are to Java, but eggs are richer than jars; they hold interesting metadata such as licensing details, release dependencies, ... (<a href="https://wiki.python.org/moin/egg">source</a>). It is a zip file.</dd>
    <dt id="pip"><code>pip</code></dt>
    <dd>pip is a de facto standard package manager for Python. It allows to install packages and installs required packages. pip introduced <code>requirements.txt</code></dd>
    <dt id="requirements.txt"><code>requirements.txt</code> <span class="label label-danger">dependency declaration</span></dt>
    <dd>It allows pinning versions of a dependency. The <code>setup.py</code> includes abstract requirements, the <code>requirements.txt</code> includes concrete ones. Abstract requirements are more flexible, concrete ones are stable.</dd>
    <dt id="wheel">wheel distribution  <span class="label label-primary">distribution format</span></dt>
    <dd>The wheel binary package format is specified in <a href="https://www.python.org/dev/peps/pep-0427/">PEP 427</a>. It is similar to egg distributions. It is a zip file.</dd>
    <dt id="twine">twine</dt>
    <dd>Allowed to securely upload a package to PyPI.</dd>
    <dt id="conda">conda</dt>
    <dd>conda is a Python-agnostic packaging tool and installer. If you need more than Python / if you don't have Python installed. It supports C, Fortran, R, Perl, Java, ...</dd>
    <dt id="pipfile">pipfile and pipfile.lock <span class="label label-danger">dependency declaration</span></dt>
    <dd>A pipfile should be easier to maintain than multiple <code>requirements.txt</code> files, e.g. for testing / environments (dev, stage, prod). The pipfile.lock is automatically generated and tracks interdependencies of the required packages; it is similar to <a href="https://bundler.io/v1.7/rationale.html#checking-your-code-into-version-control"><code>gemfile.lock</code></a> in Ruby and <a href="https://yarnpkg.com/lang/en/docs/yarn-lock/"><code>yarn.lock</code></a> in JavaScript. pipenv is the tool to use with those files. SO-Questions: <a href="https://stackoverflow.com/questions/tagged/pipfile">28 for pipfile</a>, <a href="https://stackoverflow.com/questions/tagged/pipenv">485 for pipenv</a></dd>
    <dt id="pyproject.toml"><code>pyproject.toml</code> <span class="label label-danger">dependency declaration</span></dt>
    <dd>A build-system independent way to specify project dependencies. <code>setup.py</code> is bad as it is 3rd party and requires code execution. It is a way to step away from distutils / setuptools. The specified build system can be setuptools as well. The pyproject.toml is similar to the <a href="https://doc.rust-lang.org/cargo/reference/manifest.html">Cargo.toml of Rust</a></dd>
    <dt id="pyenv"><a href="https://github.com/pyenv/pyenv">pyenv</a></dt>
    <dd>Install different Python versions. It is similar to rbenv from Ruby.</dd>
    <dt id="pipenv">pipenv</dt>
    <dd>Wrapper for virtualenv. Has <a href="https://stackoverflow.com/questions/tagged/pipenv">485 questions on SO</a>. See pipfile for more info.</dd>
    <dt id="virtualenvwrapper"><a href="https://virtualenvwrapper.readthedocs.io/en/latest/">virtualenvwrapper</a></dt>
    <dd>Another virtuelenv wrapper. Has <a href="https://stackoverflow.com/questions/tagged/virtualenvwrapper">570 questions on SO</a>.</dd>
    <dt id="poetry"><a href="https://poetry.eustace.io/docs/pyproject/">Poetry</a></dt>
    <dd>Meant to be a successor of pipenv, but seems not production-ready yet (<a href="https://frostming.com/2019/01-04/pipenv-poetry">source</a>, <a href="https://stackoverflow.com/questions/tagged/python-poetry">13 SO questions</a>).</dd>
    <dt id="dephell"><a href="https://dephell.org/">DepHell</a></dt>
    <dd>A Python project management tool. Can convert between setup.py <-> pyproject.toml.</dd>
    <dt><a href="https://flit.readthedocs.io/en/latest/">flit</a></dt>
    <dd>Flit is a way to put Python packages and modules on PyPI. It is a 3rd party replacement for setuptools, but has <a href="https://stackoverflow.com/questions/tagged/flit">no SO tag</a>.</dd>
</dl>


## See also

* Jeff Triplett: [Why Python devs should use Pipenv](https://opensource.com/article/18/2/why-python-devs-should-use-pipenv), 2018-02-28.
* Sarahan, McCormick, Fillion-Robin: [The Sheer Joy of Packaging](https://www.youtube.com/watch?v=xiI1i525ljE), 2018.
* Poetry: [The pyproject.toml file](https://poetry.eustace.io/docs/pyproject/)
* Frost Ming: [A deeper look into Pipenv and Poetry](https://frostming.com/2019/01-04/pipenv-poetry), 2019-01-04.
* Chad Smith: [Five Myths About Pipenv](https://medium.com/@grassfedcode/five-myths-about-pipenv-698c5f198e4b), 2018-11-30.
