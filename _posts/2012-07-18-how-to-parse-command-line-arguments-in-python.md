---
layout: post
title: How to parse command line arguments in Python
author: Martin Thoma
date: 2012-07-18 17:00:03.000000000 +02:00
category: Code
tags: Python, command line arguments
featured_image: 2011/09/Python-Logo.png
---
<h2>Argparse</h2>
<blockquote>The <a href="http://docs.python.org/library/argparse.html">argparse module</a> makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.</blockquote>

<h3>Installation</h3>
I had to install <code>python-argparse</code> on my old Ubuntu machine before I could use it.

<h3>Usage</h3>
As far as I've just tried it, you can use argparse very similar to optparse. See this <a href="https://github.com/MartinThoma/matrix-multiplication/commit/7af938c54fd2effee3efe74352b76f01d2e817e5#Python/ikjMultiplication.py">diff</a> for my switch from optparse to argparse for a simple script.

It is very easy to add command line <del>options</del> argument (if you require an option, it would not be an option any more, would it? I'll try to call them arguments from now on):

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

parser = ArgumentParser()

# Add more options if you like
parser.add_argument("-f", "--file", dest="myFilenameVariable",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

args = parser.parse_args()

print(args.myFilenameVariable)
```

Every option has some values like:
<ul>
  <li><a href="http://docs.python.org/library/argparse.html#dest">dest</a>: You will access the value of option with this variable</li>
  <li><a href="http://docs.python.org/library/argparse.html#help">help</a>: This text gets displayed whey someone uses <code>--help</code>.</li>
  <li><a href="http://docs.python.org/library/argparse.html#default">default</a>: If the command line argument was not specified, it will get this default value.</li>
  <li><a href="http://docs.python.org/library/argparse.html#action">action</a>: Actions tell optparse what to do when it encounters an option on the command line. <code>action</code> defaults to <code>store</code>. These actions are available:
    <ul>
      <li><strong>store</strong>: take the next argument (or the remainder of the current argument), ensure that it is of the correct type, and store it to your chosen destination dest.</li>
      <li><strong>store_true</strong>: store <code>True</code> in dest if this flag was set.</li>
      <li><strong>store_false</strong>: store <code>False</code> in dest if this flag was set.</li>
      <li><strong>store_const</strong>: store a constant value</li>
      <li><strong>append</strong>: append this option&rsquo;s argument to a list</li>
      <li><strong>count</strong>: increment a counter by one</li>
      <li><strong>callback</strong>: call a specified function</li>
    </ul>
  </li>
  <li><a href="http://docs.python.org/library/argparse.html#nargs">nargs</a>: ArgumentParser objects usually associate a single command-line argument with a single action to be taken. The nargs keyword argument associates a different number of command-line arguments with a single action.</li>
  <li><a href="http://docs.python.org/library/argparse.html#required">required</a>: Mark a command line argument as non-optional (required).</li>
  <li><a href="http://docs.python.org/library/argparse.html#choices">choices</a>: Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a container object as the choices keyword argument to add_argument(). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values.</li>
  <li><a href="http://docs.python.org/library/argparse.html#type">type</a>: Use this command, if the argument is of another type (e.g. int or float).</li>
</ul>

argparse automatically generates a help text. So if you call <code>python myScript.py --help</code> you will get something like that:
```bash
usage: ikjMultiplication.py [-h] [-i FILE]

ikjMatrix multiplication

optional arguments:
  -h, --help  show this help message and exit
  -i FILE     input file with two matrices
```

<h3>Example 1: Fibonacci</h3>
It is absolutely no problem to calculate the 100,000st Fibonacci number.
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fibonacci-Script")
    parser.add_argument("-n", metavar='N', type=int,
                        help="print the N-th fibonacci number")

    args = parser.parse_args()
    print fib(args.n)
```

Note that it uses <code>type=int</code> not <code>type="int"</code> as it was in optparse.

<h3>Example 2: less</h3>

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n//2)
    else:          return mul(A, pow(mul(A, A), (n-1)//2))

def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="less script")
    parser.add_argument("-f", "--file", dest="filename",
                        help="write report to FILE", metavar="FILE")
    parser.add_argument("-n",
                        dest="n", default=10, type=int,
                        help="how many lines get printed")
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose",
                        default=True,
                        help="don't print status messages to stdout")

    args = parser.parse_args()
    if args.verbose:
        print("Will open file now and print %i lines." % args.n)

    f = open(args.filename, 'r')
    for i in xrange(args.n):
        print f.readline()
```

### Example 3: copy-paste template

This is how I use it most of the time. I want to show defaults in help:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example for a simple program with a command line parser."""

import os


def is_valid_file(parser, arg):
    """
    Check if arg is a valid file that already exists on the file system.

    Parameters
    ----------
    parser : argparse object
    arg : str

    Returns
    -------
    arg
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file",
                        dest="filename",
                        type=lambda x: is_valid_file(parser, x),
                        help="write report to FILE",
                        metavar="FILE")
    parser.add_argument("-n",
                        dest="n",
                        default=10,
                        type=int,
                        help="how many lines get printed")
    parser.add_argument("-q", "--quiet",
                        action="store_false",
                        dest="verbose",
                        default=True,
                        help="don't print status messages to stdout")
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
```


<h2>Optparse</h2>
<div class="info">Deprecated since version 2.7: The optparse module is deprecated and will not be developed further; development will continue with the argparse module.</div>

Parsing command line arguments with <a href="http://docs.python.org/library/optparse.html">optparse</a> was very easy, but as it is deprecated and argparse works almost the same way, I will not make any examples. Just use argparse.

<h2>See also</h2>
<ul>
  <li><a href="http://stackoverflow.com/q/3217673/562769">Why use argparse rather than optparse?</a></li>
  <li><a href="http://stackoverflow.com/q/8387924/562769">Python argparse and bash completion</a></li>
</ul>
