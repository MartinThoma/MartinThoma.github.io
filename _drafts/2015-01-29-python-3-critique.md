---
layout: post
title: Critique of Python 3
author: Martin Thoma
date: 2014-11-22 17:19
categories: 
- Code
tags: 
- Python
featured_image: logos/python.png
---

Consistency is an important quality property of a language. One of my main
points of critic agains PHP was inconsistency (see [PHP: A strange language](http://martin-thoma.com/php-a-strange-language/#tocAnchor-1-1)). Let's see where Python is inconsistant.

## Method naming: Underscores or not

PEP 8 recommends underscores for functions, if I remember it correctly.
However, some built-in functions do not follow this naming scheme:

* [`float.fromhex`](https://docs.python.org/3/library/stdtypes.html#float.fromhex)
* [`bytes.startswith`](https://docs.python.org/3/library/stdtypes.html#bytes.startswith)
* [`str.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith)
* `str.is_digit`

Classes:

* `list`
* `tuple`
* `set`


## Stack and tail call optimization
Python makes use of a C stack which is limited (not by memory, but TODO).

Cython does also not do tail call optimization, according to Vladimir Keleshev.


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

## See also

* [Critique of Python by Vladimir Keleshev](https://www.youtube.com/watch?v=CpjUoYcaUu8)