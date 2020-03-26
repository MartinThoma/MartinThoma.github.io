---
layout: post
title: Reading and Writing Files with Python
author: Martin Thoma
date: 2015-02-12 22:11
category: Code
tags: Python
featured_image: logos/python.png
---
Reading (and writing) files with Python is very easy. Here are some
minimalistic code examples for beginners.

## Reading

A very common way to handle the contents of a file is by reading the file
completely and then working with a single big string. The only reason not to
do so is because your file is too big. For your information, this is how long
reading a file takes (all times are in seconds, reading is executed 100 times):

```text
file size         min       max    median   average
---------------------------------------------------
10 KiB         0.0000    0.0008    0.0000    0.0002
100 KiB        0.0000    0.0009    0.0001    0.0002
1 MiB          0.0003    0.0013    0.0005    0.0006
10 MiB         0.0041    0.0079    0.0047    0.0049
100 MiB        0.0627    0.0778    0.0655    0.0663
```

As you can see, reading files is quite fast. However, I would recommend the
start thinking if reading the complete file is appropriate when the file
size exceeds 100 MiB as you might get different problems then. For example,
the content of the file might not fit in your main memory (typically 4GiB,
type `cat /proc/meminfo | grep MemTotal` to get how much main memory your
computer has).

See [source code](https://gist.github.com/MartinThoma/eb1e56405009839804e7)
for details how I measured it.


### Completely

```python
with open("filename.txt") as f:
    content = f.read()
```

is all you need to read a text file completely in a Python string variable
`content`. You could, for example, split the whole string to a list of lines:

```python
lines = content.split("\n")
```


### Line by line
You can read a text file line by line, but keep in mind that this will still
have the endline character `\n` in each `line`!

```python
with open("filename.txt") as f:
    for line in f:
        print(line)
```


## Writing

To open files, you have to specify a mode. This is either reading, writing or
appending (binary or text data). If you don't specify it, the default value
is reading. So for writing you have to specify it:

```python
with open("filename.txt", "w") as f:
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

with open("file.txt", "w") as f:
    print("Hello World!", file=f)
```

The [`print`](https://docs.python.org/3.0/library/functions.html#print)
function has also a "end" parameter which defaults to `\n`. This means it adds
`\n` automatically at the end of each printed line. You might not want that
e.g. in a Windows environment where it should be `\r\n`.


## with

You might wonder what
[`with`](https://docs.python.org/3/reference/datamodel.html#context-managers)
does. My advice for newbees would be not to worry too much about it, it is
just the way you juse I/O with Python. If you come from the C / C++ world, you
might know that you have to close files when you opened them. The `with`
statement makes sure that the file is closed when the block is finished.


## See also

* [Python documentation: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
* [`print`](https://docs.python.org/3.0/library/functions.html#print)
* [`open`](https://docs.python.org/3.0/library/functions.html#open)
* [`with`](https://docs.python.org/3/reference/datamodel.html#context-managers)
* [File Objects](https://docs.python.org/2/library/stdtypes.html#file-objects)
* [Python and CSV](//martin-thoma.com/python-csv/)
* [How to parse command line arguments in Python](//martin-thoma.com/how-to-parse-command-line-arguments-in-python/)
