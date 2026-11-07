---
layout: post
title: The ‘Literal’ Annotation in Python
slug: the-literal-annotation-in-python
lang: en
author: Martin Thoma
date: 2021-01-08 17:35
category: Code
tags: Python, mypy
featured_image: logos/python.png
summary: Are you up-to-date with Python’s type annotation development?
medium_url: https://medium.com/@martinthoma/the-literal-annotation-in-python-f882c021ab53
---
```python
import pandas as pd
from typing import Literal


def normalize(
    df: pd.DataFrame, imputation: Literal[None, "fill0", "fillmean"]
): ...


with open("foo.txt", "q") as fp:
    fp.write("data")
```

Python keeps developing via Python Enhancement Proposals (PEPs). [PEP 586](https://www.python.org/dev/peps/pep-0586/) added a feature I love: Literal Types 😍

After reading this article you will know how to use that feature.

If you happen to be new to type annotations, I recommend reading my [introduction to type annotations in Python](../type-annotations/).

## Literal Annotation Example

The `Literal` type needs at least one parameter, e.g. `Literal["foo"]`. That means that the annotated variable can only take the string `"foo"`. If you want to accept `"bar"` as well, you need to write `Literal["foo", "bar"]`.

A complete example:

```python
from typing import Literal
# If you are on Python 3.7 and upgrading is not an option,
#   $ pip install typing_extensions
# to install the backport. Then import it:
#   from typing_extensions import Literal


def parse_bool_str(
    text: str, default: Literal["raise", False] = "raise"
) -> bool:
    if text.lower() in ["y", "yes", "true", "1", "on"]:
        return True
    if text.lower() in ["n", "no", "false", "0", "off"]:
        return False
    if default == "raise":
        raise ValueError(f"It's unclear: {text}")
    return False
```

We could also have annotated `default` with `Union[str, bool]`, but that would allow a big range of other values and different behavior.

Please note that you need to run `mypy` during development (best in your CI pipeline) to find such issues. It will NOT help you during runtime. Read my [introduction to type annotations in Python](../type-annotations/) for more about that.

## Enum in Python

Instead of using a Literal type, you could use an enum:

```python
from enum import Enum


class DefaultBehaviour(Enum):
    RAISE = "raise"
    BOOL = False


def parse_bool_str(
    text: str, default: DefaultBehaviour = DefaultBehaviour.RAISE
) -> bool:
    if text.lower() in ["y", "yes", "true", "1", "on"]:
        return True
    if text.lower() in ["n", "no", "false", "0", "off"]:
        return False
    if default == DefaultBehaviour.RAISE:
        raise ValueError(f"It's unclear: {text}")
    return False
```

You can see that this changes the code in multiple places. For this reason, it might be harder to use Enums for type annotations in an existing codebase.

## Pydantic and Literal

When it comes to (de)serialization and data validation, I recently fell in love with [pydantic](https://pydantic-docs.helpmanual.io/) 😍

Let’s test how pydantic deals with Literals:

```python
from typing import Literal, List
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    roles: List[Literal["Registered", "Moderator", "Admin"]] = Field(
        default_factory=list
    )


jon_doe = User.parse_obj({"name": "Jon Doe", "roles": []})
jon_skeet = User.parse_obj(
    {"name": "Jon Skeet", "roles": ["Registered", "Admin"]}
)
print(jon_skeet.dict())

# This fails - as expected!
# unexpected value; permitted: 'Registered', 'Moderator', 'Admin'
# (type=value_error.const;
#  given=foo;
#  permitted=('Registered', 'Moderator', 'Admin')
# )
User.parse_obj({"name": "Jon Doe", "roles": ["foo"]})
```

It works like a charm 🎉

## What should I use in new code?

One important part of type annotations is editor support. You want the editor to be able to autocomplete as much as possible. For VS Code + Pylance, I can say that Enums give better autocompletion:

```python
from typing import Literal, List
from dataclasses import dataclass
from enum import Enum


class EnumRoles(Enum):
    REGISTERED = "Registered"
    MODERATOR = "Moderator"
    ADMIN = "ADMIN"


LiteralRoles = Literal["Registered", "Moderator", "Admin"]


@dataclass
class User:
    name: str
    role_literal: LiteralRoles
    role_enum: EnumRoles


User(name="foo", role_literal="Moderator", role_enum=EnumRoles.MODERATOR)
```

In principle, both allow the developer to see the list of allowed values. The editor support could be very similar — but it isn’t. Hence I would prefer Enums for new code. It’s not a strong preference, though.

Here is a similar discussion for TypeScript: [Difference between string enums and string literal types in TS](https://stackoverflow.com/q/49761972/562769)
