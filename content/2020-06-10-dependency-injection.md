---
layout: post
title: Dependency Injection
slug: dependency-injection
lang: en
author: Martin Thoma
date: 2020-06-10 20:00
category: My bits and bytes
tags: Dependency-injection, Software Engineering, Design Pattern
featured_image: logos/star.png
status: draft
---
[Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) (DI)
is a technique in which an object receives other objects that it depends on.

Whenever I read this during my software engineering courses or in Java-related
contexts, I was confused. I didn't quite understand what it is and why
people make such a fuss about it.

Now, I think it is just a super simple idea which does not really deserve its
own name. In its simplest form, it's turning the implicit dependency on outside
state into an explicit dependency on a parameter. For functions, that makes them
closer to pure functions. For objects, it means that a class doesn't create the
services it needs (a database connection, an HTTP client, a clock), but gets
them handed in.


## Examples

### Time

I often write functions which depend on the current time / date. Let's say
we want to just get a filename. The simple solution is:

```python
import datetime


def get_filename() -> str:
    """Get something like '2020-06-10-13-06-31.txt'."""
    now = datetime.datetime.now()
    return f"{now:%Y-%m-%d-%H-%M-%S}.txt"
```

That is super straightforward, but maybe you want to test it. Then you
suddenly have to use mocking for `datetime`.

Or, you make the function a bit different:

```python
import datetime


def get_filename(now=None) -> str:
    """Get something like '2020-06-10-13-06-31.txt'."""
    if now is None:
        now = datetime.datetime.now()
    return f"{now:%Y-%m-%d-%H-%M-%S}.txt"
```

So you inject the dependency `now`. Due to Python's handling of default
parameters you cannot assign it as a default value, but that is a different
topic.

Although you use the function exactly the same way, you can test it by setting
the `now` parameter. The dependency on `datetime` was removed for the important
code path. Instead, the dependency on an explicitly set parameter `now` was
added.

More details on this in [^1].


### Database Connection

```python
def execute_query(db, sql):
    connection = db.connect()
    connection.execute(sql)
```

Here, the dependency is the database object `db`. It is injected in the
function. In a test, `db` can be an in-memory SQLite database instead of the
production database.

### Constructor Injection

With classes, the dependencies are usually passed to the constructor:

```python
class InvoiceService:
    def __init__(self, repository, mailer):
        self.repository = repository
        self.mailer = mailer

    def send_reminders(self):
        for invoice in self.repository.overdue_invoices():
            self.mailer.send(invoice.customer_email, "Your invoice is overdue")
```

The class doesn't know whether `repository` talks to PostgreSQL or is a list in
a test, and whether `mailer` sends emails or just records them. The code that
creates the objects decides that, in one place:

```python
service = InvoiceService(PostgresRepository(db_url), SmtpMailer(smtp_host))
```

For the test, the fakes are a few lines:

```python
class FakeMailer:
    def __init__(self):
        self.sent = []

    def send(self, to, text):
        self.sent.append((to, text))
```

### Pytest Fixtures

> Fixtures allow test functions to easily receive and work against specific
> pre-initialized application objects without having to care about
> import/setup/cleanup details. It’s a prime example of dependency injection
> where fixture functions take the role of the injector and test functions are
> the consumers of fixture objects.

Source: [Fixtures: a prime example of dependency injection](https://docs.pytest.org/en/stable/explanation/fixtures.html)


## Why is it used?

Dependency injection can be used instead of global state. The advantages of
dependency injection compared to having global state are:

* Flexibility: Dependency injection can make your code usable in a broader
  range of scenarios
* Testing: Dependency injection can make testing easier. With global state, you
  need to mock. However, please note that the unit test with dependency
  injection does not test if the interface of the dependency changed. This
  means with dependency injection you might want to add an explicit interface
  test (aka boundary test). See also the dependency injection section in
  [Unit Testing in Python — Patching, Mocks and Dependency Injection](../unit-testing-patching/).
* Clear dependencies: The signature shows what a function or class needs. Hidden
  dependencies on global state are discovered only when something breaks.


## When not to use it

You can apply dependency injection whenever some kind of global state is
involved, even when it doesn't help:

```python
from typing import Callable


def hello_world(output_function: Callable, name: str):
    output_function(f"Hello, {name}")


hello_world(output_function=print, name="world")
```

Please don't do that. Only use it if you need it. [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it),
if you want to sound cool.

In this example, you don't make testing easier. You might have added
flexibility, but the cost of it is that your code becomes harder to read. Code
readability matters because we read code often. When the function looks
complicated, other people (including yourself in the future) might just decide to
implement the thing from scratch.


## Inversion of Control

> [Inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)
> (IoC) is a programming principle. [...] with inversion of control,
> [a framework] calls into the custom, or task-specific, code.

See [Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html) by Martin Fowler.

Dependency injection is one way to achieve inversion of control: the code that
uses a dependency no longer decides which implementation it gets. In the Java
world, frameworks like Spring do the wiring automatically with a *DI container*:
you declare which classes exist, and the container creates them and passes them
to each other. In Python, this is rarely needed: passing objects explicitly is
easy, and modules are already singletons. There are libraries like
[dependency-injector](https://python-dependency-injector.ets-labs.org/), and web
frameworks have built-in variants, for example
[FastAPI's `Depends`](https://fastapi.tiangolo.com/tutorial/dependencies/) and
pytest's fixtures shown above.

Injected dependencies only work well if the replacements really behave like the
original: a fake mailer must accept the same calls and not raise different
exceptions. That is the
[Liskov substitution principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle).
With type hints and a `typing.Protocol`, a type checker can verify at least the
interface.

## See also

* Stack Overflow:
    * tux21b: [Why is IoC / DI not common in Python?](https://stackoverflow.com/q/2461702/562769), 2011
    * bagrat: [What is a Pythonic way for Dependency Injection?](https://stackoverflow.com/q/31678827/562769), 2015
* Yeray Díaz: [Import as an antipattern - Demystifying Dependency Injection in modern Python](https://www.youtube.com/watch?v=qkGxy4c64Jg) at PyCon UK, 2019. On YouTube (21 minutes).
* Ilya Pekelny: [Inversion of Control — Python anti-pattern](https://medium.com/@pekelny/inversion-of-control-python-anti-pattern-eff3943f64f), 2018.


## Footnotes

[^1]: Haki Benita: [Stop Using datetime.now!](https://hakibenita.com/python-dependency-injection), 2020.
