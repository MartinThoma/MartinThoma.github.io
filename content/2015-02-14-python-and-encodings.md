---
layout: post
title: Python and Encodings
author: Martin Thoma
date: 2015-02-14 14:28
category: Code
tags: Python, Encodings, UTF8
featured_image: logos/python.png
---
Working with encodings different from ASCII or UTF-8 has always been work
which I don't like. It doesn't feel very constructive to just make Python
read a file / print some output.

In the following, I will describe some strategies which might help you.


## Test script

Copy the following text to a text file `test.txt`:

```text
Die süße, kleine, lärmende Überfliegerin lebt in der Haute-Côte-Nord.
Dort hat es momemtan 32°C.
```

On Debian based systems you will get the information which type of encoding it
has like this:

```text
$ file test.txt
test.txt: UTF-8 Unicode text
```

This is probably the best result. But to make sure that we know how to deal
with other encodings, you can change the encoding like this:

```text
$ iconv -f UTF-8 -t ISO-8859-1 test.txt > test-iso-8859-1.txt
$ file test-iso-8859-1.txt
test-iso-8859-1.txt: ISO-8859 text
```


## Source code encoding

A first important step is to define the source code encoding. This is done
with a comment. The first lines of Python code should probably always look
like this:

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

[PEP-0263](https://www.python.org/dev/peps/pep-0263/) explains it.


## Printing encoding problems

The following error occurs when you try to print non-UTF-8 stuff with Python
via Sublime Text:

```text
[Decode error - output not utf-8]
```

The same code, executed via ZSH, gives:

```text
Die s��e, kleine, l�rmende �berfliegerin lebt in der Haute-C�te-Nord.
Dort hat es momemtan 32�C.
```

You can fix that by adjusting the code the following way:


```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Make it work with Python 2 and Python 3
import sys

PY3 = sys.version > "3"

if not PY3:
    from future.builtins import open

# Specify the encoding while opening it
with open("test-iso-8859-1.txt", encoding="ISO-8859-1") as f:
    content = f.read()
content = content.encode("UTF-8", "replace")
print(content)
```

The two important points are

1. Specifying the encoding while opening the file
2. Encode the content with UTF-8

These three little steps helped me to deal with non-UTF-8 encodings.


## See also
* [Unicode HOWTO](https://docs.python.org/2/howto/unicode.html)
* [codecs — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)
