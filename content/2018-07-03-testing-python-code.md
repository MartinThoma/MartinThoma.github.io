---
layout: post
lang: en
title: Testing in Python
slug: testing-python-code
author: Martin Thoma
date: 2018-07-03 20:00
category: Code
tags: Code, Testing, tox, pytest, coverage
featured_image: logos/python.png
---
Testing code is important for the following reasons:

* **Trust**: You checked at least some cases if they work. So others can have
  more trust in the quality of your work and youself can also put more trust in
  it.
* **Breaking Changes**: For a bigger project, it is sometimes hard to have
  every part in mind. By writing tests, you make it easier to change something
  and see if / where things break.
* **Code Style**: When you know that you have to write tests, you write some
  things slightly different. Those slight differences usually improve the
  coding style. Sometimes, they are crucial.

When testing, there are two important measures:

* Line coverage: How many of the lines of code were touched during the
  execution of tests?
* Branch coverage: For if-statements, how many of the branches were taken?

Usually, I aim for more than 95% line coverage.


## Why you should test

Besides trust, preventing breaking changes and code style, I want to give two
concrete examples how writing tests with the aim of a high test coverage
improved my code.

### Reproducibility

Suppose you have to test a function

```python
import datetime


def get_tomorrow():
    today = datetime.datetime.now()
    return today + datetime.timedelta(hours=24)
```

then you have a problem. The execution of this depends on the current state of
the world. That is hard to test. While there is [`freezegun`](https://github.com/spulec/freezegun),
the simpler change is to add an argument:

```python
import datetime


def get_tomorrow(today=None):
    if today is None:
        today = datetime.datetime.now()
    return today + datetime.timedelta(hours=24)
```

Now the code is easy to test. As a side effect, the function is more flexible.
You could generate the "today" datetime object before, log its value and rerun
everything.


### Complexity

Imagine you have a function with 300&nbsp;lines of code, conditionally executed
code in multiple levels and for loops. It will be a mess to test everything.

A very extreme point of view is hold [here](https://softwareengineering.stackexchange.com/a/195992/25699):

> If, when describing the activity of the code to another programmer you use
> the word 'and', the method needs to be split into at least one more part.


## How to Test


### Doctests

Python has a module called [`doctest`](https://docs.python.org/3/library/doctest.html).
It executes code which is after the promt `>>> `.

A simple example:

```python
def fibonacci(n):
    """
    Calculate the n-th fibonacci number.

    >>> fibonacci(0)
    0
    >>> fibonacci(6)
    8
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

If you execute this, it will directly check if the documentation matches actual
execution. Try it by changing `8` to something else.


Why it is nice:

* It's simple
* You have written both, documentation and a test
* It's guaranteed not to get outdated (otherwise the tests will fail)


The drawbacks of this solution:

* It compares directly the output as shown on the console. If this is not
  deterministic (e.g. as with the set datatype), you need to check for
  equality.
* In many cases, it is hard to set things up.


My recommendation: Use doctests when it looks simple and you don't have to
set up a lot of initial variables. Once you need to interact with anything,
this is not a good solution anymore.


### unittests

Python comes with [`unittest`](https://docs.python.org/3/library/unittest.html),
which is the default module for unit testing. It is inspired by JUnit. The
following text is partially directly copied from the documentation.

Unit tests are the fundament of the testing pyramid. The should be isolated
from other software, be fast to execute, relatively easy to write and thus
rather cheap. If the test is not isolated, then it is an integration test. A
typical integration test is when you interact with a database.

There are four concepts which are supported by `unittest`:

<dl>
    <dt>test case</dt>
    <dd>A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.</dd>
    <dt>test fixture</dt>
    <dd>A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.</dd>
    <dt>test suite</dt>
    <dd>A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.</dd>
    <dt>test runner</dt>
    <dd>A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.</dd>
</dl>

To put it into context:

* You write a test case.
* It might be neccessary or convenient to `setUp` things. This is the test
  fixture.
* You combine tests to a test suite.
* The test runner executes the tests.

Your [project structure](https://martin-thoma.com/python-projects/) should be:

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
└── tests <--------------------------
    ├── __init__.py
    └── test_utils.py
```

A simple unittest is usually stored in `tests/test_themodule_name.py` and might
look like this:

```python
#!/usr/bin/env python

import unittest


class ThemoduleNameTest(unittest.TestCase):
    def setUp(self):
        """Set things up for the test."""
        # e.g. initialize database mock

    def tearDown(self):
        """Clean things up after the test."""
        # e.g. remove a file

    # test routine A
    def test_abc(self):
        """Test routine A"""
        print("FooTest:testA")

    # test routine B
    def testB(self):
        """Test routine B"""
        print("FooTest:testB")
```


### pytest

[`pytest`](https://docs.pytest.org/en/latest/) is a framework which makes
testing with Python WAY easier. You can simply add files `test_<modulename>.py`
with `text_xyz()` functions and assert statements:

```python
def text_xy():
    import mymodule

    assert mymodule.f(1) == 2
```

Then you execute `pytest` in the project folder (without any arguments) and
it runs your tests!

#### pytest plugins

pytest also comes with some neat plugins:

* [`pytest-ordering`](https://github.com/ftobia/pytest-ordering): Executing
  tests in a given order is nice when you have some super fast ones and some
  rather slow ones.
* [`pytest-dependency`](https://pypi.org/project/pytest-dependency/): I hate it
  when I break one thing and a thousand tests fail. This makes it hard to find
  the root cause. By defining dependencies you can skip tests conditionally
  on the outcome of another test.
* [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/): Creating coverage
  reports with pytest.
* [`pytest-mccabe`](https://pypi.org/project/pytest-mccabe/): Check which
  functions are too complex.

I recommend to add the following to your `setup.cfg`:

```ini
[tool:pytest]
addopts = ./tests/ --doctest-modules --mccabe --cov=./mpu --cov-append --cov-report html:tests/reports/coverage-html --cov-report xml:tests/reports/coverage.xml --pep8 --ignore=docs/
doctest_encoding = utf-8
mccabe-complexity=10

[pydocstyle]
ignore = D104, D105, D107, D301, D413, D203, D212, D100
match_dir = mpu
```

You might wonder how it relates to `nose`. The main thing you should remember
is that [nose is no longer maintained](https://nose.readthedocs.io/en/latest/#note-to-users).


### radon

[`radon`](https://pypi.org/project/radon/) computes several maintainability
measures. The best one is the maintainability index. Here is how I use it
for my `mpu` package:

```shell
$ radon mi mpu
```


### tox

[`tox`](https://en.wikipedia.org/wiki/Tox_(Python_testing_wrapper)) is a
testing tool which helps you to discover if you forgot to add dependencies to
your `setup.py`.

You can install [`tox`](https://pypi.org/project/tox/) via

```shell
$ pip install tox
```


## Coverage Reports

The [`coverage`](http://coverage.readthedocs.io/en/latest/) package and its
[`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) plugin allow you
to generate coverage reports.

I recommend creating a `.coveragerc` file in your projects root directory:

```ini
[run]
source = mpu  # folder where your project is
branch = True

[report]
# Regexes for lines to exclude from consideration
exclude_lines =
    # Have to re-enable the standard pragma
    pragma: no cover

    # Don't complain about missing debug-only code:
    def __repr__
    def __str__
    if self\.debug

    # Don't complain if tests don't hit defensive assertion code:
    raise AssertionError
    raise NotImplementedError

    # Don't complain if non-runnable code isn't run:
    if 0:
    if __name__ == .__main__.:
```

The `branch = True` enables the creation of branch coverage reports.


## The Tricky Cases


### File System Interactions

The two solutions are temporary files with [`tempfile`](https://docs.python.org/3/library/tempfile.html)
and [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html).

See also: [How do I mock the filesystem in Python unit tests?](https://stackoverflow.com/q/19672138/562769)


### Web Interactions

See [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)


### Credentials

Having credentials as environment variables seems to be the cleanest solution
so far. You might want to have a look at [`direnv`](https://direnv.net). To
give later developers (including yourself) later a hint, you could create a
`template.envrc` file which contains all relevant attributes, but not the
values.

For example:

```bash
export AWS_USERNAME="foobar"
export AWS_PASSWORD="foobar"
export FOOBAR="foobar"
```

Of course, you should *not* add the `.envrc` file to your git repository.

For AWS, there is <a href="https://aws.amazon.com/kms/">KMS</a> to store
credentials.

## Mutation Testing

Mutation Testing is a nice idea how to test your tests. You "mutate" your code
slightly and want at least one test to fail.

So you change constants (off-by-one), you change the order of operations.

There is [`cosmic-ray`](https://github.com/sixty-north/cosmic-ray), but last
time I checked it didn't quite help me.

There is also [`mutmut`](https://pypi.org/project/mutmut/), but I haven't even
tried that one.


## See also

* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* The Hitchhiker’s Guide to Python: [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/)


<!-- https://www.360logica.com/blog/sneak-peek-test-framework-test-pyramid-testing-pyramid/ -->
