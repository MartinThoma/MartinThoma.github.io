---
layout: post
lang: en
title: Type Systems
slug: type-systems
author: Martin Thoma
date: 2018-11-26 20:00
category: Code
tags: Programming Languages
featured_image: logos/star.png
---
The topic of type system keeps comming up when I hear people discuss
programming languages. So let's summarize it.

## Dynamic vs Static Typing

<div style="background-color: #cdcdcd">Rule of thumb: Statically typed languages check their types at compile time,
while dynamically typed languages check their types at runtime.</div>

I like the definition of [pythonconquerstheuniverse](https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/):

> In a **statically typed** language, every variable name is bound both
> a type (at compile time, by means of a data declaration) and an object.
>
> In a **dynamically typed** language, every variable name is bound only to an
> object.


Something you can do in a dynamic language, but not in a static language:

```python
foo = "bar"
foo = 9
```

So the model you have in mind is different. In statically typed languages you
imagine variables as containers for specific types of information. In dynamically
typed languages, you imagine variables as post-it notes.

The advantage of statically typed languages is less confusion.


## Strong vs Weak Typing

<div style="background-color: #cdcdcd">Rule of thumb: Weakly typed languages do type coercion.</div>

Continuing with the definition of [pythonconquerstheuniverse](https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/):

> In a weakly typed language, variables can be implicitly coerced to unrelated
> types, whereas in a strongly typed language they cannot, and an explicit
> conversion is required.

What you can do in weakly typed languages, but not in strongly typed languages:

```python
foo = "hello"
bar = 1337
foo + bar
```

Instead, the strongly typed language needs something like that:

```python
foo = "hello"
bar = 1337
foo + str(bar)
```

Note that this is a spectrum, but the example from above is where I draw the
line.

I'd say strong is to be prefered, but not too strong. For example, if I add
a float and a double I would not want to get an exception. Maybe.


## Explicit vs Implicit Typing

In an **explicitly typed** language, all variable types are directly given by
the developer.

In an **implicitly typed** language, the language can infer some of the types.

Note that dynamically typed languages are always implicitly typed. Python likes
to call that "duck typing": If it walks like a duck and quacks like a duck, it
is a duck.


## Overview

<table class="table">
    <tr>
        <th>Language</th>
        <th>Static</th>
        <th>Strength</th>
        <th>Type Expression</th>
    </tr>
    <tr>
        <td>Rust</td>
        <td>static</td>
        <td>strong</td>
        <td><a href="https://doc.rust-lang.org/book/first-edition/variable-bindings.html">implicit</a></td>
    </tr>
    <tr>
        <td>C++</td>
        <td>static</td>
        <td>strong</td>
        <td>explicit</td>
    </tr>
    <tr>
        <td>C</td>
        <td>static</td>
        <td>weak</td>
        <td>explicit</td>
    </tr>
    <tr>
        <td>Java</td>
        <td>static</td>
        <td>strong</td>
        <td>explicit</td>
    </tr>
    <tr>
        <td>Python</td>
        <td>dynamic</td>
        <td>strong</td>
        <td>implicit, since Python 3.5 optionally explicit</td>
    </tr>
    <tr>
        <td>JavaScript</td>
        <td>dynamic</td>
        <td>weak</td>
        <td><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var">implicit</a></td>
    </tr>
    <tr>
        <td>PHP</td>
        <td>dynamic</td>
        <td>weak</td>
        <td>implicit</td>
    </tr>
</table>


## See also

* Wikipedia: [Comparison of programming languages by type system](https://en.wikipedia.org/wiki/Comparison_of_programming_languages_by_type_system)
