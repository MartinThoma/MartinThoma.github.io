---
layout: post
title: Regular Expressions with Python
author: Martin Thoma
date: 2015-01-20 13:35
categories: 
- Code
tags: 
- Python
- RegEx
featured_image: logos/python.png
---
Python supports regular expressions (RegEx) just as any other general purpose
programming language. This mini article shows two examples how to use them.

The package which gives RegEx support is called
[`re`](https://docs.python.org/3/library/re.html).


## Replacing Spaces

Replace multiple whitespace characters (spaces, tabs, newlines, ...) by a
single space (by [Nasir](http://stackoverflow.com/a/1546245/562769)):

```python
import re
text = "The   fox jumped   over    the log."
replaced = re.sub("\s\s+", " ", text)
```

To speed things up you can also
[`compile`](https://docs.python.org/3/library/re.html#re.compile) the pattern.
This has also the advantage that you can specify that you want to match newline
characters (`\n` and `\r`) with the dot by setting the
[`re.DOTALL`](https://docs.python.org/3/library/re.html#re.DOTALL) flag.

```python
import re

pattern = re.compile("\s\s+", re.DOTALL)
text = "The   fox jumped   over    the log."
pattern.sub(" ", text)
```

## Unquoting

```python
import re

def remove_quotes(text):
    """Remove 'test'."""
    def unquote(m):
        return u' %s ' % str(m.group(1))
    pattern = re.compile(" '([^ ]+?.*[^ ]+?)' ")
    return pattern.sub(unquote, text)

text = "The quoted 'text piece' will get unquoted."
remove_quotes(text)
```


## All paragraphs

If you want to get the content within all paragraph tags (`<p> ... </p>` in
arbitrary spacing) you can use:

```python
import re

pattern = re.compile("<p>(.*?)</p>", re.IGNORECASE | re.DOTALL)
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus placerat
turpis vitae malesuada tempor. Fusce cursus condimentum leo, ut bibendum justo
varius sit amet. In accumsan interdum nibh at fermentum. Nulla commodo, mi vel
ultricies efficitur, nulla tortor sagittis tortor, quis laoreet augue orci
vitae justo.

sasdf <p>Suspendisse porttitor risus et est consequat condimentum.
In in eleifend ipsum, eu pulvinar nunc. Nullam vel imperdiet eros.
Phasellus vel arcu convallis, semper quam eu, convallis velit.

</p>


<P>Sed tempus magna quis neque varius aliquam. Quisque maximus et augue non
dapibus. Nullam et ante imperdiet, fringilla diam nec, mattis quam.</p>

<P>Ut fermentum lacus id semper imperdiet. Donec et purus consectetur,
fermentum mi nec, viverra dolor. Quisque posuere ultricies leo et efficitur.
Aliquam venenatis quis mi ac tempus.</p>

Maecenas in nisl lacinia, finibus velit eu, aliquet elit. Morbi orci libero,
interdum id vehicula vitae, <p>congue vel</p>p> lectus. Morbi lobortis eros
mollis, cursus velit at, convallis dolor. Nullam volutpat neque at risus
porttitor, faucibus tristique tellus suscipit. In sed purus quis sem tincidunt
lobortis. Vivamus ut blandit erat, sed sollicitudin felis. Etiam placerat,
sapien et vulputate placerat, mi lectus tristique nisi, vitae finibus tellus
nisi a massa. Nullam sit amet scelerisque lectus. Fusce porta justo ac
scelerisque auctor. Integer vestibulum tellus at quam molestie dapibus.
Suspendisse quis quam tortor. Nullam consequat tempus orci eget scelerisque. Ut
auctor lorem enim, id rutrum eros congue varius. In justo lacus, molestie vitae
nibh eu, venenatis auctor ex.
"""

matches = pattern.findall(text)
```

Matches is the following list (breaked at some points for easier reading):

```text
['Suspendisse porttitor risus et est consequat condimentum.\n
  In in eleifend ipsum, eu pulvinar nunc. Nullam vel imperdiet eros.\n
  Phasellus vel arcu convallis, semper quam eu, convallis velit.\n\n',
 'Sed tempus magna quis neque varius aliquam. Quisque maximus et augue non\n
  dapibus. Nullam et ante imperdiet, fringilla diam nec, mattis quam.',
 'Ut fermentum lacus id semper imperdiet. Donec et purus consectetur,\n
  fermentum mi nec, viverra dolor.
  Quisque posuere ultricies leo et efficitur.\n
  Aliquam venenatis quis mi ac tempus.',
 'congue vel']

```