---
layout: post
title: Formatting Strings in Python
slug: formatting-strings-python
author: Martin Thoma
date: 2013-11-07 20:05:33.000000000 +01:00
category: Code
tags: Python
featured_image: 2011/09/Python-Logo.png
---
In Python, you can use the following ways to format Strings:

## Print directly
Printing them directly (just like <a href="http://www.cplusplus.com/reference/cstdio/printf/">printf in C</a>):

```python
birthday = 28
month = "April"
year = 1990
print("My birthday is the %i-th %s %i." % (birthday, month, year))
```

The first string contains the rules how to format. <code>%i</code> means that the first argument in the following tuple should be interpreted as a integer. The second one <code>%s</code> should be interpreted as a string and the third one again as a integer.


## Save as string

```python
>>> a = "Why is %i the answer?" % 42
>>> a
'Why is 42 the answer?'
```


## Named formatting
You might prefer named formatting:

```python
>>> "{guy} loves {girl}.".format(girl="Marie", guy="Martin")
'Martin loves Marie.'
```

You can also store this first in a dictionary an unpack it:

```python
>>> myDictionary = {"girl":"Marie","guy": "Martin","other":"Internet"}
>>> "{guy} loves {girl}.".format(girl="Marie", guy="Martin")
'Martin loves Marie.'
```


## Date and Time
You can format time any way you like, just look at <a href="http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">this reference</a>.

<h2>Lists</h2>
Question: I would like to print a list! How do I do that?
Answer: Convert your list to a string

```python
>>> myList = [1,2,3]
>>> print("Your list: %s" % (str(myList)))
Your list: [1, 2, 3]
```


## __str__ and __repr__
When you build your own objects, you should add an implementation for the method <code>__str__</code> and <code>__repr__</code>. The first one should return a string representation that is human readable of the object, the second one should return a string that identifies the object.


## Formatters
<table>
<tr>
  <td><code>%i</code></td>
  <td>Integer</td>
  <td>

```python
>>> print("%i" % (123))
123

```

</td>
</tr>
<tr>
  <td><code>%s</code></td>
  <td>String</td>
  <td>

```python
>>> print("%s" % ("Martin"))
Martin

```

</td>
</tr>
<tr>
  <td><code>%o</code></td>
  <td>Int as octal</td>
  <td>

```python
>>> print("%o" % (123.123))
173
```

</td>
</tr>
<tr>
  <td><code>%x</code></td>
  <td>Int as hexadecimal (lower case)</td>
  <td>

```python
>>> print("%x" % (123.123))
7b
```

</td>
</tr>
<tr>
  <td><code>%X</code></td>
  <td>Int as hexadecimal (upper case)</td>
  <td>

```python
>>> print("%X" % (123.123))
7B
```

</td>
</tr>
<tr>
  <td><code>%f</code></td>
  <td>Floating point</td>
  <td>

```python
>>> print("%f" % (123.123))
123.123000
```

</td>
</tr>
<tr>
  <td><code>%.2f</code></td>
  <td>Floating point with two decimal places</td>
  <td>

```python
>>> print("%.2f" % (123.123))
123.12
```

</td>
</tr>
<tr>
  <td><code>%e</code></td>
  <td>Floating point in scientific notation</td>
  <td>

```python
>>> print("%e" % (123.123))
1.231230e+02
```

</td>
</tr>
<tr>
  <td><code>%%</code></td>
  <td>Percent sign</td>
  <td>

```python
>>> print("%i%%" % (65))
65%
```

</td>
</tr>
<tr>
  <td><code>%6.2f</code></td>
  <td>Print a float with 2 decimal places. Add spaces if this has less than 6 characters.</td>
  <td>

```python
>>> print("%6.2f" % (65.123))
 65.12
```

</td>
</tr>
</table>


## Columns

```python
my_list = [('Easybox 1234', 54, 'DC:9F:DB:B2:B1:1C'),
           ('FRITZ!Box 6360 Cable', 12, '24:65:11:06:71:54'),
           ('wkit-802.1x', 15, 'A0:D3:C1:9F:FF:11')]
header = u"{0:<20}{1:>6}{2:>20}".format('SSID',
                                        'Signal',
                                        'HwAddress')
print(header)
print("-"*len(header))
for ssid, signal, hwaddress in my_list:
    print(u"{0:<20}{1:>6}{2:>20}".format(ssid,
                                         str(signal)+'%',
                                         hwaddress))
```

results in

```text
SSID                Signal           HwAddress
----------------------------------------------
Easybox 1234           54%   DC:9F:DB:B2:B1:1C
FRITZ!Box 6360 Cable   12%   24:65:11:06:71:54
wkit-802.1x            15%   A0:D3:C1:9F:FF:11
```


## Resources
<ul>
  <li><a href="https://pyformat.info/">pyformat.info</a></li>
  <li><a href="http://docs.python.org/2/library/string.html#format-specification-mini-language">Format Specification Mini-Language</a></li>
  <li><a href="http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">Time formatting</a></li>
  <li><a href="http://docs.python.org/2/library/pprint.html">Pretty Print</a></li>
</ul>
