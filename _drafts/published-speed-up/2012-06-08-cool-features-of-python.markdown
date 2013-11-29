---
layout: post
status: publish
published: true
title: Cool features of Python
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 25881
wordpress_url: http://martin-thoma.com/?p=25881
date: 2012-06-08 17:30:10.000000000 +02:00
categories:
- Code
tags:
- Programming
- Python
comments:
- id: 156371
  author: Stefan Koch
  author_email: blog@stefan-koch.name
  author_url: http://stefan-koch.name
  date: !binary |-
    MjAxMi0wNi0wOCAxODoxMjoxOCArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNi0wOCAxNjoxMjoxOCArMDIwMA==
  content: ! "I think you wante to write \"The list did not contain a prime\".\r\n\r\nAs
    far as I understand it, else is executed if the for loop is terminated regularly
    (i.e. not using break). As you use break if a prime was found, you would want
    to display that there was no prime if the loop terminated normally.\r\n\r\nHowever,
    I have to say that I consider the for-else-feature in Python a bit strange. What
    I would expect from for-else is to execute else if the list is empty (and for
    is never run). But maybe that&rsquo;s only because we have this probably a hell
    a lot of times in web-development (list elements or show \"There are no elements
    yet, be the first to add one!\")."
- id: 156391
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNi0wOCAxODoxNzo1NCArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNi0wOCAxNjoxNzo1NCArMDIwMA==
  content: Thanks, you're right. I corrected the example. This feature was one of
    those I've just discovered. I haven't used it before and I don't know if I'll
    ever use it. But it's nice to know that this feature exists :-)
- id: 1237985
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0xMC0yMSAxNjo0ODo1NCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0xMC0yMSAxNDo0ODo1NCArMDIwMA==
  content: ! "I've just found a very good resource for understanding decorators in
    Python:\r\n\r\nhttp://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps"
---
A friend wanted to know why I enjoy programming in Python so much more than programming in other languages. So I will describe some special features of Python which make it much easier to quickly implement algorithms.

I also made drafts how the tasks would be solved in most programming languages. When I say most, I mean most languages that are widely spread (so C/C++/Java is much more important than almost any other languages combined). I know that those tasks would be solved completely different in functional programming languages.

<h2>Rapid, readable programming</h2>
<h3>Intuitive looping through lists</h3>
You can loop through every list-like datastructure like this:

{% highlight python %}for element in list:
    print(element){% endhighlight %}

<h3>Arbitrary Integer size</h3>
<strong>Description</strong>: Print the sum of the digits of $2^{100000}$.
<strong>Java</strong>:
{% highlight java %}import java.math.BigInteger;

public class test {
    public static void main(String[] args) {
        BigInteger a = new BigInteger("2");
        a = a.pow(100000);
        int sum = 0;
        for (int i=0; i < a.toString().length(); i++) {
            sum += a.toString().charAt(i);
        }
        System.out.println(sum);
    }
}{% endhighlight %}

<strong>Python</strong>: (was much faster in both computation and programming time!)
{% highlight python %}big = 2**100000
sumOfDigits = 0
for digit in str(big):
	sumOfDigits += int(digit)

print(sumOfDigits){% endhighlight %}

Python has no need for a special class as it has arbitrary length integers (see <a href="http://docs.python.org/release/3.1.5/c-api/long.html">source</a>)

<h3>Swich values of variables</h3>
<strong>Description</strong>: You want to make sure, that variable a is smaller than b ($a < b$). 
<strong>Most languages</strong>:
{% highlight python %}tmp = a
a = min(a, b)
b = max(tmp, b){% endhighlight %}

<strong>Python</strong>:
{% highlight python %}a, b = min(a, b), max(a,b){% endhighlight %}

<h3>Return more than one variable</h3>
<strong>Description</strong>: Evaluate $f: \mathbb{R}^2 \rightarrow \mathbb{R}^3, f(x, y) := (x^2, y^2, x+y)$
<strong>Most languages</strong>:
{% highlight python %}double function(double x, double y) {
  double returnValues[3];
  returnValues[0] = x*x;
  returnValues[1] = y*y;
  returnValues[2] = x + y;
  return returnValues;
}

double values[3] = function(4, 5);
printf("Part 1: %.2f", values[0]);
printf("Part 3: %.2f", values[2]);{% endhighlight %}

<strong>Python</strong>:
{% highlight python %}def function (x, y):
    return (x*x, y*y, x+y)

a, b, c = function(4, 5)
print("Part 1: %.2f" % a)
print("Part 3: %.2f" % b){% endhighlight %}

This is called "Argument Unpacking". In fact it does return only one variable (a tuple), but it creating the tuple is so easy that it does not feel like creating another variable.

<h3>Short initialisation</h3>
<strong>Description</strong>: Get a string representation of a list from the standard library
<strong>Java</strong>:
{% highlight java %}import java.util.LinkedList;
import java.util.List;

public class test {
    public static void main(String[] args) {
        List<Integer> myList = new LinkedList<Integer>();
        myList.add(1);
        myList.add(3);
        myList.add(3);
        myList.add(7);
        System.out.println(myList);
    }
}{% endhighlight %}

<strong>Python</strong>:
{% highlight python %}myList = [1, 3, 3, 7]
print(myList){% endhighlight %}

Both get the same result.

<h3>Chaining Comparisons</h3>
Description: You would like to check if $x \in [-5, 42]$.
<strong>Most languages</strong>:
{% highlight java %}if (-5 <= x &amp;&amp; x <= 42){% endhighlight %}

<strong>Python</strong>:
{% highlight python %}if -5 <= x <= 42:{% endhighlight %}

<h3>Enumeration</h3>
<strong>Description</strong>: You have a list and you would like to print it, prefixed with the index in the list.
<strong>Java</strong>:
{% highlight java %}List myList = (List initialisation and assignment, multiple lines)
int i = 0;
for (int element : myList) {
    System.out.printf("%i: %i", i, element);
    i++;
}{% endhighlight %}

<strong>Python</strong>:
{% highlight python %}myList = [1, 3, 3, 7]

for nr, element in enumerate(myList):
	print("%i: %i" % (nr, element)){% endhighlight %}

<h3>Named String formatting</h3>
Python allows you to give parameters names:
{% highlight python %}print("The %(foo)s is %(bar)i." % {'foo': 'answer', 'bar':42}){% endhighlight %}

<h3>any() and all()</h3>
<strong>Description</strong>: You have a very long list and you want to know, if a prime is in this list.
<strong>Most languages</strong>:
{% highlight java %}List myList = (List initialisation and assignment of many values)
boolean isPrimePresent = false;
for (int element : myList) {
    if (isPrime(element)) {
        isPrimePresent = true;
        break;
    }
}

if (!isPrimePresent) {
    System.out.println("The list did not containe a prime.");
}{% endhighlight %}

<strong>Python</strong>:
{% highlight python %}myList = [4, 4, 9, 12]

if not any(isPrime(x) for x in myList):
    print("The list did not contain a prime"){% endhighlight %}

See also: <a href="http://stackoverflow.com/questions/10958874/exists-keyword-in-python">StackOverflow answer from steveha</a>.


<h2>Testing and Documentation</h2>
<h3>Doctest</h3>
You can write Documentation and Unit-Tests at the same time! Take a look at <a href="http://docs.python.org/library/doctest.html">doctest &mdash; Test interactive Python examples</a>.

<h2>The Rest</h2>
<h3>Lists and Generators</h3>
I already wrote an article about <a href="http://martin-thoma.com/understanding-python-lists/" title="Understanding Python Lists">Python Lists</a> and <a href="http://martin-thoma.com/python-generators/" title="Python Generators">Python Generators</a>. I love Pythons lists :-)

<h3>for ... else</h3>
<strong>Description</strong>: You have a very long list and you want to know, if a prime is in this list.
<strong>Most languages</strong>:
{% highlight java %}List myList = (List initialisation and assignment of many values)
boolean isPrimePresent = false;
for (int element : myList) {
    if (isPrime(element)) {
        isPrimePresent = true;
        break;
    }
}

if (!isPrimePresent) {
    System.out.println("The list did not containe a prime.");
}{% endhighlight %}

<strong>Python</strong>:
{% highlight python %}myList = [1, 3, 3, 7]

for element in myList:
    if isPrime(element):
        break
else:
    print("The list did not containe a prime."){% endhighlight %}

<h3>Step through lists</h3>
<strong>Description</strong>: Print only every n-th element of an iterable.

{% highlight python %}for element in myList[::n]:
    print elemenet{% endhighlight %}

<h3>Dynamically add properties to objects and classes</h3>
{% highlight python %}class Node(object):
    value = 3

a = Node()
b = Node()

print a.value

""" colorize the node! """
#print a.color ==> AttributeError

# thats ok, although the object originally had no attribute "color"
a.color = "white" 
print a.color 

# You can even add a property to the class
Node.special = "here is it"
print b.special{% endhighlight %}

<h3>Imaginary numbers</h3>
Python directly supports usage of imaginary numbers:
{% highlight python %}(2j + 1)**2{% endhighlight %}
Output: (-3+4j)

<h2>Read also</h2>
<a href="http://docs.python.org/tutorial/introduction.html">An Informal Introduction to Python</a>
