---
layout: post
title: Type Annotations in Python 3.8
URL: https://medium.com/@MartinThoma/type-annotations-in-python-3-8-3b401384403d
slug: type-annotations
author: Martin Thoma
date: 2020-06-22 20:00
category: Code
tags: Python, mypy
featured_image: logos/python.png
---
One reason why Python is so easy to get started with is that it has dynamic types. You don’t have to specify the type of a variable, you just use variables as labels for containers of data. But in bigger projects, having types is helpful. If you have an undocumented function without types and maybe crappy variable naming, new developers will have a hard time. Luckily, variable annotations were added in Python 3.6 with [PEP 526](https://www.python.org/dev/peps/pep-0526) 🎉

This article is written in such a way that you can easily stop after the “mypy” section and take only a look at individual section then.

## Hello, Typed Annotated World!

```python
def fib(n: int = 0) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Print the first 10 Fibonacci numbers
for i in range(10):
    print(f"fib({i}) = {fib(i)}")
```

So you can simply use the pattern

```python
def some_function(param_name: typename) -> return_type_name:
    ...  # whatever the function does
```

Having type annotations is nice, but you need to check them! The Python runtimes do not do that, no matter if you use cPython, pypy or something more exotic.

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2020/06/mypy.svg"><img src="../images/2020/06/mypy.svg" alt="mypy logo" style="width: 512px;"/></a>
    <figcaption class="text-center">mypy logo</figcaption>
</figure>


## Type Checking with mypy

Install mypy via pip install mypy and run it:

```shell
$ mypy . --ignore-missing-imports
Success: no issues found in 1 source file
```

The [--ignore-missing-imports](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-ignore-missing-imports) flag is necessary, because otherwise you will get a lot of messages like this:

```plain
error: Skipping analyzing 'setuptools': found module but no type hints or library stubs
```

In order to make it more convenient, I usually add a setup.cfg file in which I specify that I always want this flag to be applied:

```ini
[mypy]
ignore_missing_imports=true
```

Then you can pip install pytest-mypy and make sure mypy is always executed when you run pytest by adding this section to your setup.cfg:

```ini
[tool:pytest]
addopts = --mypy
```

It is important to note that the Python community and also mypy assumes that you come from a non-type annotated code base. They want to make it easy to you to switch to an annotated code and thus support [gradual typing](https://en.wikipedia.org/wiki/Gradual_typing). However, this means that you might miss errors if you don’t annotate your code! Mypy has a lot of flags to help you to make the move. You don’t need to annotate everything.

## typing: List, Dict, Tuple, Any

The [typing](https://docs.python.org/3/library/typing.html) module adds support for type hints. It contains some of the types you will use most often: List, Dict, and Tuple.

```python
from typing import List


def fib_list(n: int = 0) -> List[int]:
    fib_numbers: List[int] = [0, 1]
    for _ in range(n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers


print(f"fib_list(10) = {fib_list(10)}")
```

Similarly, you can annotate that a dictionary maps strings to integers by Dict[str, int] . So List, Dict and Tuple are generics. Any is just a way to specify that you could have arbitrary data in those containers. It is reasonable to use Any in the beginning when you start to add type annotations to a bigger code base.

## Stop Type Checking

As mentioned before, mypy and Python support gradual typing. And sometimes you need to silence the type checker to be able to continue (and hopefully fix it later 🤞). There are a couple of ways to do this with typing :

typing.Any : Every type is of type Any.

[typing.cast](https://docs.python.org/3/library/typing.html#typing.cast)(SomeClass, variable) : Sometimes mypy is not smart enough, so you can tell it which type you have. I did that a couple of times before I knew about typing.overload . Alternatively, you can also add assert [isinstance](https://docs.python.org/3/library/functions.html#isinstance)(variable, Someclass)

# type: ingore : Explicitly tell the typechecker to ignore that line

## typing: Union and Optional

Pretty often, you want to accept multiple types. Then you use Union:

```python
from typing import Union


def upcase(s: Union[str, bytes]) -> Union[str, bytes]:
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, bytes):
        return bytes(x - 0x20 if 0x61 <= x <= 0x7A else x for x in s)
    else:
        raise TypeError("need str or bytes")
```

As it happens pretty often that you need to accept some type and None , there is also typing.Optional . Optional[SomeType] is the same as Union[SomeType, None] .

## typing: List vs Sequence

The type typing.List actually represents list . A typing.Sequence is “an iterable with random access” as [Jochen Ritzel](https://stackoverflow.com/a/2921465/562769) put it so nicely. For example, a string is a Sequence[Any] , but not a List[Any] .

## typing: Dict vs Mapping

Similarly to the example List vs Sequence, the typing.Dict is meant mainly to represent a dict whereas typing.Mapping is more general. [Stacksonstacks](https://stackoverflow.com/a/52487800/562769) gives a good answer.

## Many more Types



## Custom Types: Not all Strings are Created Equal

Not all strings contain the same type of content. They can represent anuser_id , a user_name , a password_hash , …

Especially for IDs I have seen this to become messy. I think it’s pretty ridiculous to create an own class for those different string types as creating a class is usually development and maintenance overhead. So, what do you do?

Don’t worry, [typing.NewType](https://docs.python.org/3/library/typing.html#newtype) got you covered!

```python
from typing import NewType

UserId = NewType("UserId", str)
```

## typing.overload

typing.Union is actually an anti-pattern sometimes, because you can also [overload](https://docs.python.org/3/library/typing.html#typing.overload) a function as [Josh Reed](https://github.com/python/mypy/issues/1693#issuecomment-618404849) shows:

```python
from typing import overload


@overload
def upcase(s: str) -> str:
    ...


@overload
def upcase(s: bytes) -> bytes:
    ...


def upcase(s):
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, bytes):
        return bytes(x - 0x20 if 0x61 <= x <= 0x7A else x for x in s)
    else:
        raise TypeError("need str or bytes")
```

## Type checking only imports

I've recently seen myself in the position that I made a pretty heavy import on
module level, just because of type checking. This felt wrong, so I asked for
help. The solution was simple:
[`typing.TYPE_CHECKING`](https://mypy.readthedocs.io/en/stable/common_issues.html#import-cycles).
This is `True` when running a type checker, but `False` during normal runs ❤️

## Protocols

[PEP 544](https://www.python.org/dev/peps/pep-0544/) introduced structural subtyping and was introduced in Python 3.8. It feels like Interfaces in Java and works like this:

```python
from typing import Protocol


class SupportsClose(Protocol):
    def close(self) -> None:
        ...


def finish_it(obj: SupportsClose):
    obj.close()


class Foo:
    def close():
        pass


foo = Foo()
finish_it(foo)
```

Note that there is no function body. After that definition, you can then use SupportsClose like any type.

The cool part is that the class Foo has no explicit relationship to SupportsClose ! It is only related by its structure!

## Type comments

Type hints which are given as comments like this are outdated since Python 3.6:

```python
from typing import List, Any, Sequence


def fib_list(n=0):
    # type: (int) -> Sequence[str]
    fib_numbers: List[int] = [0, 1]
    for _ in range(n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return "adf"


print(f"fib_list(10) = {fib_list(10)}")
```

However, you might want to disable type checking for single lines:

```python
# type: ignore
```

## Stub files

Stub files end in .pyi . If mypy finds a .py file and a .pyi file, it only loads the .pyi file. They are like header files in C++, but for Python. Instead of a function body, you use an Ellipsis ... :

```python
def fib_list(n: int) -> List[int]:
    ...
```

## pyright, pyre, pytype

[pyright](https://github.com/microsoft/pyright) is a Python static type checker written by Microsoft, [pyre](https://pyre-check.org/) is one by Facebook, and pytype is one by Google. All of them claim to be faster than mypy, all of them have lower adoption than mypy. I haven’t used them so far.

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2020/06/pyre.png"><img src="../images/2020/06/pyre.png" alt="pyre logo" style="width: 512px;"/></a>
    <figcaption class="text-center">pyre logo</figcaption>
</figure>

Install them:

```shell
$ pip install pyre-check pytype

# Yes, pyright is written in TypeScript...
$ npm install -g pyright
```

Run them:

```shell
$ pyright .
$ pytype .
```

pyright was complaining a lot about stuff that is actually correct.

## pydantic

Variable annotations can also be used to remove a lot of boilerplate code. For example, [pydantic](https://pydantic-docs.helpmanual.io/) can help you with serialization / deserialization:

```python
# Core Library modules
import json
from typing import List

# Third party modules
import pydantic.json
from pydantic import BaseModel, parse_obj_as


class User(BaseModel):
    name: str
    age: int


# Deserialize a JSON string
users_str = '[{"name": "user1", "age": 15}, {"name": "user2", "age": 28}]'
users = parse_obj_as(List[User], json.loads(users_str))

# Proof it!
print(users)

# Serialize
print(json.dumps([user.dict() for user in users]))
```

Which gives:

```plain
[User(name='user1', age=15), User(name='user2', age=28)]
[{"name": "user1", "age": 15}, {"name": "user2", "age": 28}]
```

[FastAPI](https://fastapi.tiangolo.com/features/#pydantic-features) uses pydantic directly.

A cool thing about pydantic are the [constrained types](https://pydantic-docs.helpmanual.io/usage/types/#constrained-types): PositiveFloat, NegativeInt, constr, …

## See also

1. Dustin Ingram: [Static Typing in Python](https://www.youtube.com/watch?v=2gBP1qN5T7I) at PyGotham, 2019. On YouTube.
2. Andreas Dewes: [Type Annotations in Python 3: Whats, whys & wows!](https://www.youtube.com/watch?v=vM2Zoy4Sxhk) at EuroPython Conference, 2017. On YouTube.
3. Carl Meyer: [Type-checked Python in the real world](https://www.youtube.com/watch?v=pMgmKJyWKn8) at PyCon, 2018. On YouTube.
