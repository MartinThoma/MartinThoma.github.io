---
layout: post
title: Reading Files with Python
author: Martin Thoma
date: 2015-02-12 22:11
categories: 
- Code
tags: 
- Python
featured_image: logos/python.png
---
Reading (and writing) files with Python is very easy. Here are some
minimalistic code examples for beginners.

## Reading

### Completely

```python
with open('filename.txt') as f:
    content = f.read()
```

is all you need to read a text file completely in a Python string variable
`content`. You could, for example, split the whole string to a list of lines:

```python
lines = content.split('\n')
```


### Line by line
You can read a text file line by line, but keep in mind that this will still
have the endline character `\n` in each `line`!

```python
with open('filename.txt') as f:
    for line in f:
        print(line)
```


## Writing

To open files, you have to specify a mode. This is either reading, writing or
appending (binary or text data). If you don't specify it, the default value
is reading. So for writing you have to specify it:

```python

with open('filename.txt', 'w') as f:
    f.write("Hello world!")
```

## Python 3

Python 3 has some new features which are very nice to have. To get them in
Python 2, you have to add

```python
from __future__ import print_function
```

at the beginning of your code before other imports happen. Now you can print to
files:

```python
from __future__ import print_function

with open('file.txt', 'w') as f:
    print("Hello World!", file=f)
```

The [`print`](https://docs.python.org/3.0/library/functions.html#print)
function has also a "end" parameter which defaults to `\n`. This means it adds
`\n` automatically at the end of each printed line. You might not want that
e.g. in a Windows environment where it should be `\r\n`.


## with

You might wonder what
[`with`](https://docs.python.org/3/reference/datamodel.html#context-managers)
does. My advise for newbees would be not to worry too much about it, it is
just the way you juse I/O with Python. If you come from the C / C++ world, you
might know that you have to close files when you opened them. The `with`
statement makes sure that the file is closed when the block is finished.


## See also

* [Python documentation: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
* [`print`](https://docs.python.org/3.0/library/functions.html#print)
* [`open`](https://docs.python.org/3.0/library/functions.html#open)
* [`with`](https://docs.python.org/3/reference/datamodel.html#context-managers)
* [File Objects](https://docs.python.org/2/library/stdtypes.html#file-objects)
* [Python and CSV](http://martin-thoma.com/python-csv/)
* [How to parse command line arguments in Python](http://martin-thoma.com/how-to-parse-command-line-arguments-in-python/)