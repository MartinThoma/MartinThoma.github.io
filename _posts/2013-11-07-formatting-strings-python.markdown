---
layout: post
status: publish
published: true
title: Formatting Strings in Python
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 76701
wordpress_url: http://martin-thoma.com/?p=76701
date: 2013-11-07 20:05:33.000000000 +01:00
categories:
- Code
tags:
- Python
comments: []
---
In Python, you can use the following ways to format Strings:

<h2>Print directly</h2>
Printing them directly (just like <a href="http://www.cplusplus.com/reference/cstdio/printf/">printf in C</a>):

{% highlight python %}
birthday = 28
month = "April"
year = 1990
print("My birthday is the %i-th %s %i." % (birthday, month, year))
{% endhighlight %}

The first string contains the rules how to format. <code>%i</code> means that the first argument in the following tuple should be interpreted as a integer. The second one <code>%s</code> should be interpreted as a string and the third one again as a integer.

<h2>Save as string</h2>
{% highlight python %}>>> a = "Why is %i the answer?" % 42
>>> a
'Why is 42 the answer?'{% endhighlight %}

<h2>Named formatting</h2>
You might prefer named formatting:

{% highlight python %}>>> "{guy} loves {girl}.".format(girl="Marie", guy="Martin")
'Martin loves Marie.'{% endhighlight %}

You can also store this first in a dictionary an unpack it:
{% highlight python %}>>> myDictionary = {"girl":"Marie","guy": "Martin","other":"Internet"}
>>> "{guy} loves {girl}.".format(girl="Marie", guy="Martin")
'Martin loves Marie.'{% endhighlight %}

<h2>Date and Time</h2>
You can format time any way you like, just look at <a href="http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">this reference</a>.

<h2>Lists</h2>
Question: I would like to print a list! How do I do that?
Answer: Convert your list to a string
{% highlight python %}>>> myList = [1,2,3]
>>> print("Your list: %s" % (str(myList)))
Your list: [1, 2, 3]{% endhighlight %}

<h2>__str__ and __repr__</h2>
When you build your own objects, you should add an implementation for the method <code>__str__</code> and <code>__repr__</code>. The first one should return a string representation that is human readable of the object, the second one should return a string that identifies the object.

<h2>Formatters</h2>
<table>
<tr>
  <td><code>%i</code></td>
  <td>Integer</td>
  <td>{% highlight python %}>>> print("%i" % (123))
123
{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%s</code></td>
  <td>String</td>
  <td>{% highlight python %}>>> print("%s" % ("Martin"))
Martin
{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%o</code></td>
  <td>Int as octal</td>
  <td>{% highlight python %}>>> print("%o" % (123.123))
173{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%x</code></td>
  <td>Int as hexadecimal (lower case)</td>
  <td>{% highlight python %}>>> print("%x" % (123.123))
7b{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%X</code></td>
  <td>Int as hexadecimal (upper case)</td>
  <td>{% highlight python %}>>> print("%X" % (123.123))
7B{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%f</code></td>
  <td>Floating point</td>
  <td>{% highlight python %}>>> print("%f" % (123.123))
123.123000{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%.2f</code></td>
  <td>Floating point with two decimal places</td>
  <td>{% highlight python %}>>> print("%.2f" % (123.123))
123.12{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%e</code></td>
  <td>Floating point in scientific notation</td>
  <td>{% highlight python %}>>> print("%e" % (123.123))
1.231230e+02{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%%</code></td>
  <td>Percent sign</td>
  <td>{% highlight python %}>>> print("%i%%" % (65))
65%{% endhighlight %}</td>
</tr>
<tr>
  <td><code>%6.2f</code></td>
  <td>Print a float with 2 decimal places. Add spaces if this has less than 6 characters.</td>
  <td>{% highlight python %}>>> print("%6.2f" % (65.123))
 65.12{% endhighlight %}</td>
</tr>
</table>

<h2>Resources</h2>
<ul>
  <li><a href="http://docs.python.org/2/library/string.html#format-specification-mini-language">Format Specification Mini-Language</a></li>
  <li><a href="http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior">Time formatting</a></li>
  <li><a href="http://docs.python.org/2/library/pprint.html">Pretty Print</a></li>
</ul>
