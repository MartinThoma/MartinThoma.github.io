---
layout: post
title: Critique of Python 3
slug: python-3-critique
author: Martin Thoma
date: 2014-11-22 17:19
category: Code
tags: Python, Consistency, Programming
featured_image: logos/python.png
---

Consistency is an important quality property of a language. One of my main
points of critic agains PHP was inconsistency (see [PHP: A strange language](//martin-thoma.com/php-a-strange-language/#tocAnchor-1-1)). Let's see where Python is inconsistant.

## Naming


### Underscores or not

PEP 8 recommends underscores for functions, if I remember it correctly.
However, some built-in functions do not follow this naming scheme:

* [`float.fromhex`](https://docs.python.org/3/library/stdtypes.html#float.fromhex)
* [`bytes.startswith`](https://docs.python.org/3/library/stdtypes.html#bytes.startswith)
* [`str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)
* `str.is_digit`
* [`os.path.isfile`](https://docs.python.org/2/library/os.path.html#os.path.isfile) and probably all other `os` functions.


### snake_case or camelCase

<table class="table">
    <tr>
        <th>Where</th>
        <th>Is</th>
        <th>Should be</th>
    </tr>
    <tr>
        <td><a href="https://docs.python.org/3/library/logging.html">Logging module</a> (everywhere)</td>
        <td>logging.getLogger</td>
        <td>logging.get_logger</td>
    </tr>
</table>


### Methods / Properties / Functions

* `len`: Each container type should have a property `length`. One the one hand,
  this is done in many other languages. On the other hand, it indicates that
  getting the length is a constant-time operation.


## Tutorial

> A tutorial is a method of transferring knowledge and may be used as a part of a learning process. More interactive and specific than a book or a lecture; a tutorial seeks to teach by example and supply the information to complete a certain task.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Tutorial)

Tutorials are very important for programming languages. Especially the ones
which introduce the core concepts of a language. I think Python should have
3 tutorials:

* How to install: Detailed instructions for all major systems. At the
  beginning, the user should be asked about his system (and get help how to
  find out which system he has) and then get only the instructions necessary
  for his system.
* Programming beginners Python tutorial: Python is probably the first
  programming language some people use. And I think it is suited well for them.
  However, there should be an official Python tutorial for people who have to
  learn what a variable is and what functions are. This tutorial might contain
  information which over-simplifies stuff.
  [wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide)
  is similar to that, but it seems not to be very well structured.
* Advanced programmers Python tutorial: For people who know the basic concepts
  of programming.

These three tutorials should be linked from python.org/tutorials.


## Documentation

Every function / object / method should have examples. So the
[`len`](https://docs.python.org/3/library/functions.html?highlight=len#len)
function should additionally have this:

```python
>>> some_list = [23, 12, -3, 0]
>>> len(some_list)
4
>>> other_list = [[12, 32, 456], [1, 2, 3]]
>>> len(other_list)
2
```

I think the PHP documentation is awesome. Take a look at
[`strlen`](http://php.net/manual/en/function.strlen.php). It is immediately
clear how to use it, which versions are supported, what types the parameters
should have and what the return value is. Functions which you might have
looked for can be found under "See Also" and some difficulties can be found
under "User Contributed Notes". I have never seen a similar well-structured
and written documentation of a programming language (not for [Java](http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#length()), C, [C++](http://www.cplusplus.com/reference/string/string/length/),
[Haskell](http://hackage.haskell.org/package/base-4.7.0.2/docs/Prelude.html#v:length), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/count))

Also, runtime information in big-O notation as well as space information would
be nice.

## PyPI

`gi` is for GTK, but the module https://pypi.python.org/pypi/gi "overrides" it.
That should not be possible. So there is an issue with namespaces.

## Joining lists

Joining a list of strings works like this in Python 3:

```python
>>> a = [str(el) for el in range(5)]
>>> a.join(" ")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'join'
>>> " ".join(a)
'0 1 2 3 4'
```

However, I think it is much more logical to apply a `join` method of a list
with a string argument than a `join` method of a string with a list argument.
This might be the case because I know
[how join is done in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join).


## Module specific

### Base64

The module `base64` contains the functions `b16decode`, `b16encode`,
`b32decode`, `b32encode`, `b64decode`, `b64encode`, `decode`, `decodestring`,
`encode`, `encodestring`, `standard_b64decode`, `standard_b64encode`,
`urlsafe_b64decode`, `urlsafe_b64encode`.

It is not good to have a module called `base64` and give it `base32decode`.
But that is probaly for historic reasons and I cannot think of a better name
by now. `text_encoding`? That would have "encoding" in the name.

However, I think the module should only have the functions

* str encode(str s, int base=64)
* str decode(str s, int base=64, casefold)

I don't see a good reason why reading and writing should be done by this
module.


### Scipy - PIL

PIL uses `(width, height)` (e.g. in `Image.new`) and SciPy uses `(height, width)`.


## See also

* [Critique of Python by Vladimir Keleshev](https://www.youtube.com/watch?v=CpjUoYcaUu8)
