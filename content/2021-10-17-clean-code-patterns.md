---
layout: post
title: 9 Clean Code Patterns I wish I knew earlier
slug: clean-code-patterns
lang: en
author: Martin Thoma
date: 2021-10-17 20:00
category: Code
tags: Python, Programming, Software Engineering
featured_image: logos/python.png
medium_url: https://towardsdatascience.com/9-clean-code-patterns-i-wish-i-knew-earlier-57ee56c5892
---
Do you know the feeling when you look back at code which you wrote early in
your career? I always feel a bit horrified. But there is a positive side to
it: I learned something new 😄

A core part of good software is readability. Keeping the mental complexity low
so that everybody (including the author) has an easy time understanding it.
Clean code patterns help to do so.

In this article, you will get to know 9 clean code patterns that make code
easier to read. Please see such patterns as tools. They don’t apply all the
time. Don’t get religious about them. The language I use is Python, but the
patterns apply outside of Python as well. Let’s start!

## №1: Explanatory Variables

This is probably the simplest trick which you can easily apply. If something
is hard to understand and you need a comment for it, try giving it a name.

```python
# Bad
if not (
    string.startswith('"""') and string.endswith('"""') and '"' not in string[3:-3]
):
    return string

# Good
is_triple_quoted_string = string.startswith('"""') and string.endswith('"""')
if not (is_triple_quoted_string and '"' not in string[3:-3]):
    return string
```

This applies mostly to boolean expressions, but also to regular expressions,
and sometimes to return values.

## №2: Follow Conventions and Style Guides

Every programming language has a syntax that you need to follow, otherwise, it
will not work. And then there are conventions. You don’t have to follow them;
it will still work. However, it makes the life of others way easier if you do
follow them.

One of the simplest conventions is **style guides**. In Python it’s [PEP 8](https://www.python.org/dev/peps/pep-0008/), Google published guides for [C++](https://google.github.io/styleguide/cppguide.html) / [Java](https://google.github.io/styleguide/javaguide.html), the [Oracle Java Code Conventions](https://www.oracle.com/technetwork/java/codeconventions-150003.pdf), in PHP there is [PSR-1](https://www.php-fig.org/psr/psr-1/), …

Other guides are implicit. For example, how a Django project is structured. Where you typically store views, models, and templates.
> # Find the style guide(s) that are relevant for you and follow them.

Typically, there are also **linters** or **static code analysis tools** that help you to get used to the guides. For example, in Python, there is flake8 with a lot of plugins. For the simplest part, the formatting, you can use tools that do it for you. A code autoformatter for Python which I love is [black](https://pypi.org/project/black/).

## №3: Type Checking

I love type annotations in Python. They are optional, but I highly recommend
using them. There are also differences in how to use them.

For example, if you have Dict[str, Any] you might want to consider using
NamedTuple / TypedDict / pydantic / dataclasses instead.

In some cases, when you use `str` as the type you might want to consider using
NewType to denote which kind of string you are using. Is it an `AuthorId`? Is
it a `UserId`?

Those two patterns apply to other languages as well. Let’s phrase it like this:
> # Make good use of the type system.

If you want to know more about type annotations in Python, please read:
[**Type Annotations in Python 3.8**
*Learn how to make Python code easier to read and less error-prone by gradual typing*](../type-annotations/)

If you want to know about the most recent improvements, read my [Python 3.10 article](../python-3-10/).

## №4: Consistent Terminology

I work at the FinTech company [Cashlink](https://cashlink.de/) as a Python backend developer. We handle digital securities, e.g. tokens that represent a real value like a part of a solar farm. Those tokens can be transferred. And here it starts to become interesting. Depending on the type of transfer, we must do different things. Either because of regulations or because of technical reasons. So we started to name different types of transfers differently to not be confused all the time:

* **Transfer**: Any action that changes a balance. All terms below are some kind of transfer (although I would hesitate to call minting and burning a transfer).
* **Minting**: The tokens are generated. This happens first.
* **Issuance**: The transfer from the issuer to the investor. This happens second.
* **Move**: A transfer from wallet A to wallet B, where A and B belong to the same investor.
* **Handover**: A transfer from wallet A to wallet B, where A and B belong to different investors.
* **Burn**: Removing tokens from an investor's account.

Those things are important, but there are other examples where the terminology can be different. For example, internal product names and external ones. Marketing might have different needs than development. Try to get a vocabulary that fits most of the company.

## №5: Meaningful Names

Think of your codebase like a book. The book has many, many different storylines. The variables are the characters. You can rely a bit on the context, but readers will be confused if you call everybody just “the friend”. They will be annoyed if they need to read half a page just for the name.

* **Avoid too short names** like `i` or `x`. They are hard to search for. If you
  write a mathematical function, they might make sense, though.
* **Avoid too long names** like
  InternalFrameInternalFrameTitlePaneInternalFrameTitlePaneMaximizeButtonWindowNotFocusedState.
  Java developers regularly fall into this trap. Yes, the name might be super
  exact. However, it makes all the logic around it super hard to understand.
  There is a nice middle ground between x and
  InternalFrameInternalFrameTitlePaneInternalFrameTitlePaneMaximizeButtonWindowNotFocusedState.
* **Be consistent** with the vocabulary from №4. Also in spelling. Decide if
  you want to use American English or British English. Decide if you want to
  write display/show/present/print in your codebase.
* **Avoid data structures in names** like `user_dict`. If you need that, it
  might be that you’re violating №6. Try to use only one representation of one
  object. But keep in mind that this is a general rule. It does make sense
  sometimes to use `user_dict`.
* **Make use of context**. For example, the
  `java.sql.SQLIntegrityConstraintViolationException` could simply be a
  `java.sql.IntegrityError`. Within the sql package, everything should be about
  SQL. And a ConstraintViolation simply is an Error.

A pattern I like when iterating is to use the plural form for the iterable
(ending in “s”) and the singular for the element (without the final “s”):

```python
# Bad
for tmp in users:
    ...

# Good
for user in registered_users:
    ...
```

By the way: Please share if you’ve seen [funny variable naming](https://www.reddit.com/r/ProgrammerHumor/comments/k1wdrt/whats_the_most_inappropriate_variable_name/) in the wild 😄

## №6: The step-down rule

Keeping a function at one abstraction level helps you to focus on one topic.
> Separate logic ↔ data collection/transfer ↔ presentation.

The presentation does not necessarily have to be visual. It can be print
statements or it could be an API response.

Marek Hudyma gives [a good example](https://marekhudyma.com/code-style/2021/03/02/step-down-rule.html) of the step-down rule.

In Python, you can sometimes see this when there is a lot of indentation.

## №7: Remove Dead Code

Code that isn’t there is code that cannot break. It’s code that will not cause
security issues. It’s code that doesn’t need to be maintained. Instead of
commenting code out, remove it.

You can use [vulture](https://pypi.org/project/vulture/) and
[flake8-eradicate](https://pypi.org/project/flake8-eradicate/) to find such
pieces in a Python codebase.

I know the feeling when you have stuff that might be necessary later. I
typically try to write a really thorough commit message, removing only those
comments/files to be able to find it later if I need it. But there is YAGNI:
[You aren’t gonna need
it!](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

## №8: Use containers

If you pass the same few values around in several places of your codebase you might want to consider writing a container. That could be a class, in Python you can use a [dataclass](https://docs.python.org/3/library/dataclasses.html), a [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple), or a [TypedDict](https://www.python.org/dev/peps/pep-0589/). If you need to serialize it, a Pydantic class is pretty nice as well.

A prime example where you should likely use a container format is
configuration.

## №9: Avoid Surprises

This is a no-brainer, but it is sometimes easy to forget. One core part is to
**avoid side effects**. It should be clear whether a function changes state.
Another part is to **document hacks**. Sometimes it is necessary to have
hacks, but at least leave a comment on why the hack is there.

Don’t try to do something smart. Follow the KISS principle — Keep it simple,
stupid!

## Summary

Writing good code is like writing good articles: It needs **practice** and you will always improve. Read a lot, [ask for feedback](https://codereview.stackexchange.com/) and encourage people to also give small little notes in feedback. The ones that don’t matter too much, but are just personal preferences.

Finally, understand what you hate when you read code. Avoid [those patterns](https://cs.fit.edu/~kgallagher/Schtick/How%20To%20Write%20Unmaintainable%20Code.html) 😄 — but [apply this](https://github.com/zedr/clean-code-python/blob/master/README.md) 😍 Practice, be open to feedback, look critically at your code. Then you will be an awesome software engineer 🥂
