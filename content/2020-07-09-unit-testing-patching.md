---
layout: post
title: Unit Testing in Python — Patching, Mocks and Dependency Injection
slug: unit-testing-patching
lang: en
author: Martin Thoma
date: 2020-07-09 17:00
category: Code
tags: Python, Unit Testing, pytest, Mock, Dependency-injection, Software Engineering, Testing
featured_image: logos/python.png
medium_url: https://levelup.gitconnected.com/unit-testing-in-python-mocking-patching-and-dependency-injection-301280db2fed
---
Unit testing in general is trivial with Python and pytest, but a lot of
developers get frustrated when they have to patch dependencies away to make
code testable. In this article, you will learn how to patch and create mocks.
If you want to refresh the basics of unit testing in Python first, have a look
at the first part of this series: [Unit Testing in Python — The Basics](../unit-testing-basics/).

## The Abstract Pattern of the Problem

A dependency of the function we want to test can have an effect in three different ways: By side-effects, return values or exceptions.

Problem 1: A dependency's side effect

```python
def a_function():
    ...  # Application code to be tested
    a_dependency()
    ...  # Application code to be tested
```

Problem 2: A dependency's return value

```python
def a_function():
    ...  # Application code to be tested
    foo = a_dependency()
    ...  # Application code to be tested; it might use foo
```

Problem 3: A dependency throws an Exception

```python
def a_function():
    ...  # Application code to be tested
    try:
        foo = a_dependency()
    except:
        ...  # Application code to be tested
        ...  # this might depend on the type of Exception
    ...  # Application code to be tested
```


## The Problem — Simple Examples

Most examples in the wild are way more complex and usually they also need some
refactoring to make the code easier to maintain. So I created three examples
which are a bit closer to real applications while still keeping the bloat of
real applications away.

Example 1: We want to add a user to a database. You can see that `db` does not
return anything, but we change the state of our system. And we want to be sure
that we don’t actually change our production system when the unit tests are
running!

```python
import bcrypt
from models import db, User


def insert_user_into_db(username, password):
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))
    user = User(password=password_hash, username=username)
    db.session.add(user)
    db.session.commit()
```

Example 2: Generate a file name based on the current date. You can see that the dependency `datetime` returns a value:

```python
import datetime


def generate_filename():
    return f"{datetime.datetime.now():%Y-%m-%d}.png"
```

Similarly, you could imagine a function which returns the weather in an English sentence and uses an API to get the actual weather ([example](https://gist.github.com/MartinThoma/5c7224ceae47e74645e0145d26dc03ec)).

Example 3: In my project [edapy](https://github.com/MartinThoma/edapy) I looked at metadata from PDF files. I use the dependency `PdfReader` and have the file itself as a dependency. As the PDF file could be broken, pypdf (the successor of PyPDF2) might throw an exception. So you can imagine code like this:

```python
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def get_pdf_info(pdf_path):
    info = {}
    try:
        pdf_toread = PdfReader(pdf_path, strict=False)
    except PdfReadError:
        info["is_erroneous"] = True
        return info

    # a lot more
    return info
```

When you want to test such functions, you have the problem that the expected output is not only dependent on the function itself, but also on something external. In the cases above, the system time, an external service, and the file system.

## Examples of External Dependencies

There are lots of external dependencies your tests might have:

* Date or time
* Internet: A web service you need to use
* File System: A file you need to create / read / edit / delete
* Database: Data you select / insert / update / delete
* Randomness: Your code might make use of `random` or `np.random`

Just like the example above, they make isolated unit testing hard or even impossible.

## The solution: Patching!

The overall strategy to test this is always the same: Replace the external dependency that is causing headaches with something in your control. The act of replacing the dependency is called ***patching***, the replacement is called a ***mock***. Depending on what exactly the mock does, you might also hear this being called a Test Double, Test Stub, Test Spy or a Fake Object. In practice in Python, the distinction does not matter. If you’re interested, I recommend [Martin Fowler: The Difference Between Mocks and Stubs](https://martinfowler.com/articles/mocksArentStubs.html#TheDifferenceBetweenMocksAndStubs). I will call all of them just mocks.

Let’s make a tiny example of how to use patch!

`fraud_example.py`:

```python
from external_dependency import dark_magic


def is_credit_card_fraud(transaction):
    fraud_probability = dark_magic(transaction)
    if fraud_probability > 0.99:
        return True
    else:
        return False
```

`external_dependency.py`:

```python
def dark_magic(transaction):
    raise ValueError()
```

No matter which transaction you would use, the function `is_credit_card_fraud` would throw a `ValueError`.

This is how you patch that dependency away with a decorator `@patch`:

`test_fraud_example.py`:

```python
from unittest.mock import patch, MagicMock


def the_mock(input):
    return 0.999


@patch("fraud_example.dark_magic", the_mock)
def test_is_credit_card_fraud():
    import fraud_example

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud == True
```

And this is how you patch the dependency `fraud_example.dark_magic` away with a context manager (`with ...`):

```python
def test_is_credit_card_fraud_context_handler():
    import fraud_example

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    with patch("fraud_example.dark_magic", the_mock):
        is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud == True
```

When you now execute `pytest`, the test will succeed. You will always get 0.999 as a return value of `dark_magic` 🎉

A part that might be surprising in this example is the first parameter of the patch decorator: It’s `"fraud_example.dark_magic"` and NOT `"external_dependency.dark_magic"`! The target of your replacement is always what was loaded within the file you want to test, not where it was loaded from. Lisa Roach has pointed this out elegantly in her talk [Demystifying the Patch Function](https://www.youtube.com/watch?v=ww1UsGZV8fQ).

## Direct replacement: Don’t do this!

The following is an example which does not use patch and seems to work, but it has a big flaw. If you directly replace `datetime.datetime` instead of patching it, it will be overwritten in all other contexts after that as well! ⚠️

```python
# Core Library modules
import datetime
from unittest import mock

# First party modules
from mock_example import generate_filename


class NewDate(datetime.datetime):
    @classmethod
    def now(cls):
        return cls(1990, 4, 28)


def test_generate_filename():
    datetime.datetime = NewDate
    assert generate_filename() == "1990-04-28.png"
```


## Mock and MagicMock

You now know how to replace a dependency, hence it is time to talk about what to replace it with. This is where `unittest.mock.Mock` and `unittest.mock.MagicMock` come into play.

Everything you do with Mock will return a Mock. Call a function? Get a Mock as a return value. Access an attribute? Get a Mock as a value.

Python has so-called “magic” methods. I like the term “dunder” methods better — it just means all methods which start and end with a **d**ouble **under**score. Examples are `__iter__` or `__contains__`. `MagicMock` has those defined, `Mock` doesn’t. I would use MagicMock everywhere, except if the mocked object doesn’t define any of the magic functions.

A core feature of mock classes is that they allow you to not only remove a dependency which is hard to test, but also to assert on the way the mock was interacted with. Typical methods are [assert_called](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called)(), [assert_called_with](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with)(), [assert_not_called](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_not_called)().

## spec, autospec & spec_set

A part that is really bad about MagicMock is that you can do anything with it — including accessing non-existing attributes, calling non-existing methods or calling existing methods with the wrong number of parameters. The mock object is missing a **spec**ification. If you don’t like that, use `autospec=True` when patching the object:

```python
patch.object(Foo, "foo", autospec=True)
```

Or you can create a Mock like this:

```python-repl
>>> import datetime
>>> from unittest.mock import Mock
>>> a = Mock(spec=datetime)

# Not Ok!
>>> a.foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/moose/.pyenv/versions/3.8.1/lib/python3.8/unittest/mock.py", line 635, in __getattr__
    raise AttributeError("Mock object has no attribute %r" % name)
AttributeError: Mock object has no attribute 'foo'

# That is ok:
>>> a.datetime
<Mock name='mock.datetime' id='139883597784544'>
```

The next parameter of `patch` is `autospec`. Where `spec` looks at the mocked object, `autospec` also looks at the attributes of that object (and their attributes and those attributes, …).

Finally, there is `spec_set`. That one prevents you from setting attributes that don’t exist.

Usually, I would use `autospec=True` and `spec_set=True` everywhere. Code which uses introspection might be an example where you don’t want that.

## pytest's monkeypatch

monkeypatch is a fixture from pytest. I will explain what a fixture is in the next article. For now, just accept it as a parameter you can give to your tests without specifying it and pytest will take care of it. You don’t even need to import anything.

For the credit card fraud example, it looks like this:

```python
def test_is_credit_card_fraud_monkeypatch(monkeypatch):
    monkeypatch.setattr("fraud_example.dark_magic", the_mock)
    import fraud_example

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud == True
```

The question of when you should use `unittest.mock.patch` and — if necessary — `unittest.mock.Mock` or pytest's `monkeypatch` pretty much boils down to personal taste nowadays. The core Python `patch` / `Mock` have only existed since Python 3.3, which, I guess, is a big part of the reason why monkeypatch exists in the first place.

## External Packages

There are a couple of packages designed for simplifying the patching and giving better mocks for well-known dependencies.

For example, you can use [freezegun](https://pypi.org/project/freezegun/) for mocking the system time:

```python
from freezegun import freeze_time
from mock_example import generate_filename


def test_generate_filename():
    with freeze_time("1990-04-28"):
        assert generate_filename() == "1990-04-28.png"
```

For boto3 / botocore (cloud stuff), there is [moto](https://pypi.org/project/moto/).

For [requests](https://pypi.org/project/requests/), there is [responses](https://pypi.org/project/responses/):

`requests_example.py`:

```python
import requests


def get_ip():
    resp = requests.get("http://ip.jsontest.com/")
    return resp.json()


if __name__ == "__main__":
    print(get_ip())
```

`test_requests_example.py`:

```python
from requests_example import get_ip
import responses


@responses.activate
def test_get_ip():
    responses.add(
        responses.GET,
        "http://ip.jsontest.com/",
        json={"ip": "123.456.789.0"},
        status=404,
    )
    assert get_ip() == {"ip": "123.456.789.0"}
```


## Dependency Injection

If the above sounded complicated, there is a simpler alternative: Dependency Injection. It essentially means adding the external state explicitly as a parameter, which makes it easy to adjust in tests. For example, the code from above could be:

```python
import datetime


def generate_filename(now=None):
    if now is None:
        now = datetime.datetime.now()
    return f"{now:%Y-%m-%d}.png"
```

Now testing is trivial:

```python
import datetime
from mock_example import generate_filename


def test_generate_filename():
    now = datetime.datetime(1990, 4, 28)
    assert generate_filename(now) == "1990-04-28.png"
```

In some cases, it feels very natural to apply such a pattern, in others it
doesn’t. Do this only when it feels natural. For example, it’s very unlikely
that I would ever pass a module as a parameter although it’s possible. That
would just feel very weird.

## Temporary files: Are Mocks a Code Smell?

It depends very much on the details, but I like to mock as little as possible.
Simply for the reason that not mocking means that you test more of your system.
Strictly speaking, you can’t call the test a *unit test* anymore if you test
more than one unit. It would be an integration test then — but that is also
essential, right? You wouldn’t be happy with BMW selling you a motor, some
seats and a steering wheel and claiming “all units work”. They need to work
together. Extensive mocks might prevent you from testing how things work
together.

In an ideal world, you would have both: Unit tests which are very controlled
and in case of failure make it easy to narrow down the source of the error. And
integration / end-to-end tests which show that the complete system works.

There are also people who think that the need to mock is an indicator for a
need to refactor
([discussion](https://github.com/pytest-dev/pytest/issues/4576#issuecomment-449865322)).
Harry Percival gave the talk [Stop Using Mocks (for a
while)](https://www.youtube.com/watch?v=rk-f3B-eMkI) at PyCon 2020 and pointed
out that testing code which is using mocks tends to be brittle as it is tightly
coupled to implementation details.

A good example where I usually don’t mock anything are file system
interactions. If possible, I write the file just like it would be in the real
application. When the test is finished, the test needs to clean up as well. I
use the [tempfile](https://docs.python.org/3/library/tempfile.html) module for
that.

## Dependency Injection: Randomness

Just like adding a time parameter for functions which use the current time by default might make your code way easier to test, adding a `random_state` parameter or a seed parameter to functions which use randomness helps.

Here are some ways to seed random number generators:

```python-repl
>>> import random
>>> random.seed(0)
>>> random.random()
0.8444218515250481

>>> import numpy as np
>>> np.random.seed(0)
>>> np.random.random()
0.5488135039273248

>>> random_state = np.random.RandomState(seed=0)
>>> random_state.random()
0.5488135039273248
```

Setting a random state / seed is also very helpful for debugging. If you
haven’t heard of the Heisenbug or the Higgs-Bugson, you missed some
[programming jargon](https://blog.codinghorror.com/new-programming-jargon/).
And if you're interested in research, reproducibility matters.

## Terminology

* **Patching vs Mocking**: Patching a function is adjusting its functionality. In the context of unit testing, we patch a dependency away; so we replace the dependency. Mocking is imitating. Usually we patch a function to use a mock we control instead of a dependency we don’t control.
* **Monkey patching vs Mocking**: Within a development context, mocking is pretty clearly about unit testing ([example](https://stackoverflow.com/a/2666006/562769)). However, monkey patching has several applications besides unit testing. For example, you can patch third party code during runtime if there is a small functionality missing or a part of the code is broken. You just extend the code. Monkey patching is used in the PyCharm debugger ([source](https://youtu.be/ZpJxwpyJpq4?t=367)).
* **Monkey patching vs pytest.monkeypatch**: The first one is a general concept, the second one is a concrete function within pytest which applies monkey patching for unit tests.
* **unittest.mock.patch vs pytest.monkeypatch**: This is personal preference. I prefer to stick with built-ins whenever the third-party option does not have big advantages. In this case, I even think that the core Python unittest.mock.patch is cleaner. For this reason, I didn’t focus on `pytest.monkeypatch` so far. If you like to see the differences, there is a nice [blog post](https://krzysztofzuraw.com/blog/2016/mocks-monkeypatching-in-python.html) about it.

## A note about Architecture

To keep your code clean, it is often a good idea to wrap third party
dependencies. For example, you could have one module which deals with I/O. Or a
module which deals with API requests. Then you have a couple of modules which
might require a lot of mocking or where unit tests are pointless because the
interesting part is the integration with the third party. The rest of your code
stays easy to test, keeps the language you defined and cares about the objects
you know. This is called the [Adapter
pattern](https://en.wikipedia.org/wiki/Adapter_pattern).

## What else is there?

* Other types of Mocks, such as [PropertyMock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock)
* [pytest-mock](https://pypi.org/project/pytest-mock/) which provides the mocker fixture; I’m not really sure though if this is mainly a leftover from the time before Python 3.3 or if it actually makes things easier.
* The 3rd party package [mock](https://pypi.org/project/mock/), which should not be installed with Python 3.3+ as it was put in the standard library.

If you want to learn more about the default mocks, have a look at the awesome
article by Yeray Diaz: [What the mock? — A cheatsheet for mocking in Python](https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832).

## More in this series

This article is part of my series about unit testing in Python:

* Part 1: [The basics of Unit Testing in Python](../unit-testing-basics/)
* Part 2: **Patching, Mocks and Dependency Injection**
* Part 3: [How to test Flask applications](../test-flask-applications/) with Databases, Templates and Protected Pages
* Part 4: [tox and nox](../tox-and-nox/)
* Part 5: [Structuring Unit Tests](../unit-testing-structure/)
* Part 6: [CI-Pipelines](../ci-pipelines/)
* Part 7: [Property-based Testing](../property-based-testing/)
* Part 8: [Mutation Testing](../mutation-testing/)
* Part 9: [Static Code Analysis: Linters, Type Checking, and Code Complexity](../static-code-analysis/)

Let me know if you’re interested in other topics around testing with Python or professional software development with Python: info@martin-thoma.de
