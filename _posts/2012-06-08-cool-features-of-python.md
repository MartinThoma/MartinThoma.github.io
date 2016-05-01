---
layout: post
title: Cool features of Python
author: Martin Thoma
date: 2012-06-08 17:30:10.000000000 +02:00
category: Code
tags: Programming, Python
featured_image: 2011/09/Python-Logo.png
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

### Named String formatting
Python allows you to give parameters names:
{% highlight python %}print("The %(foo)s is %(bar)i." % {'foo': 'answer', 'bar':42}){% endhighlight %}

### any() and all()
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


## Testing and Documentation

### Doctest
You can write Documentation and Unit-Tests at the same time! Take a look at <a href="http://docs.python.org/library/doctest.html">doctest &mdash; Test interactive Python examples</a>.

### Sphinx
Documentation can be generated from partially docstrings, partially rst files
with [Sphinx](http://sphinx-doc.org/tutorial.html).
It can be uploaded to [pythonhosted.org](http://pythonhosted.org/) just like [neurolab](https://pythonhosted.org/neurolab/index.html) did it (see also [sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)).


## The Rest

### Lists and Generators
I already wrote an article about <a href="../understanding-python-lists/" title="Understanding Python Lists">Python Lists</a> and <a href="../python-generators/" title="Python Generators">Python Generators</a>. I love Pythons lists ☺

### for ... else
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

### Step through lists
<strong>Description</strong>: Print only every n-th element of an iterable.

{% highlight python %}for element in myList[::n]:
    print elemenet{% endhighlight %}

### Dynamically add properties to objects and classes

```python
class Node(object):
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
print b.special
```

### Imaginary numbers
Python directly supports usage of imaginary numbers:

```python
(2j + 1)**2
```

Output: `(-3+4j)`

## Read also
<a href="http://docs.python.org/tutorial/introduction.html">An Informal Introduction to Python</a>
