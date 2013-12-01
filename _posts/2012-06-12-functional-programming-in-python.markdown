---
layout: post
status: publish
published: true
title: Functional Programming in Python
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 26171
wordpress_url: http://martin-thoma.com/?p=26171
date: 2012-06-12 17:00:09.000000000 +02:00
categories:
- Code
tags:
- Programming
- Python
comments: []
featured_image: 2011/09/Python-Logo.png
---
Python has a few functional programming tools: Lambda functions and the three higher-order functions map, filter and reduce. I'll explain them now and I'll give some usage examples.

<h2>lambda</h2>
A lambda creates an <a href="http://en.wikipedia.org/wiki/Anonymous_function">anonymous function</a>, that means a function without a name. A lambda may have any number of arguments.

Here are some examples for lambdas:
{% highlight python %}f = lambda x: x*x
print(f(7)){% endhighlight %}
Output: 49

{% highlight python %}g = lambda x, y: x + y*y + abs(x)
print(g(1,1), g(1, -1), g(-1, 1), g(10, 6), g(-10, 6)){% endhighlight %}
Output: (3, 3, 1, 56, 36)

{% highlight python %}h = lambda myVar, anotherVar: set([myVar, anotherVar])
print(h(1, 2), h('a', 1), h('a', 'a'), h(1, 1)){% endhighlight %}
Output: (set([1, 2]), set(['a', 1]), set(['a']), set([1]))

Sometimes you would like to get an if-statement in a lambda.
So imagine you would like to make a lambda function like this:
{% highlight python %}def f(x):
    if x == 0:
        return 42
    elif x == 1:
        return 1337
    else:
        return 0{% endhighlight %}

This is the way you would do it:
{% highlight python %}f = lambda x: x==0 and 42 or x==1 and 1337 or 0{% endhighlight %}

(Thanks to <a href="http://eikke.com/python-ifelse-in-lambda/">Ikke's blog</a> for the hint!)

<h2>map(function, sequence)</h2>
Map is a function with two parameters. The first parameter is another function, the second is a sequence. Map returns a list. It only applies function to every item of the sequence.

Here are some examples:
{% highlight python %}def square(x):
    return x*x

l = map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]){% endhighlight %}
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

This is equivalent to:
{% highlight python %}l = map(lambda x: x*x, xrange(1, 11)){% endhighlight %}

You can also use more than one list:
{% highlight python %}a = xrange(-10, 10)
b = xrange(0, 20)
l = map(lambda x,y: x*y, a, b){% endhighlight %}
Output: [0, -9, -16, -21, -24, -25, -24, -21, -16, -9, 0, 11, 24, 39, 56, 75, 96, 119, 144, 171]

<h2>reduce(function, sequence)</h2>
You can quite often reduce problems to an operation on two elements. Reduce takes two elements from sequence, uses function on them and saves the result. Then it takes the result and another element of the sequence and uses function...

Example: Imagine you would like to get the sum of a list. Then you need to add two elements of the list, save the result and add another element, save the result, add another element, ...
{% highlight python %}r = reduce(lambda x,y: x+y, [1, 2,63, 3, 5]){% endhighlight %}
r = 74

You can calculate the factorial n! like this:
{% highlight python %}fac = lambda n: reduce(lambda x,y:x*y,xrange(1,n+1))
print(fac(2))
print(fac(3))
print(fac(10)){% endhighlight %}
Output: 2
6
3628800

<h2>filter(function, sequence)</h2>
filter gets all elements from sequence, where function returns true:
{% highlight python %}def isPrime(element):
    if element == 2:
        return True
    elif element <= 1 or element % 2 == 0:
        return False
    else:
        for i in xrange(3, element, 2):
            if element % i == 0:
                return False
    return True

myList = [4, 4, 9, 12, 13, 2, 7, 9, 11, 11]
r = filter(isPrime, myList){% endhighlight %}
r = [13, 2, 7, 11, 11]

<h2>Some more examples</h2>
Task: What is the sum of digits of $2^n, n \in \mathbb{N}$?
{% highlight python %}sumOfDigits = lambda exp: reduce(
                                  lambda x,y: x+y, 
                                  map(lambda x: int(x), str(2**exp))
                                )
print(sumOfDigits(2))
print(sumOfDigits(3))
print(sumOfDigits(4))
print(sumOfDigits(10000)){% endhighlight %}
Output: 4
8
7
13561

Task: Encode and decode a string in the following way: Split Words by spaces. Every plaintext character gets a two-digit numerical representation in base 16. A is 01, B is 02 and Z is 1A.
{% highlight python %}# Thanks to lebenf: http://stackoverflow.com/a/3226719/562769
chunks = lambda l, n: [l[x: x+n] for x in xrange(0, len(l), n)]

decodeWord= lambda s: "".join(map(lambda x: chr(int(x,16)+64),chunks(s,2)))
decode    = lambda s: " ".join(map(decodeWord, s.split(" ")))
encodeWord= lambda p: "".join(map(lambda x: "%.2X" % (ord(x)-64), p))
encode    = lambda p: " ".join(map(encodeWord, p.split(" ")))

cipher = encode("HELLO WORLD")
print("Cipher Text: %s" % cipher)
print("Plain Text: %s" % decode(cipher)){% endhighlight %}

<h2>See also</h2>
<ul>
  <li>Wikipedia:
    <ul>
      <li><a href="http://en.wikipedia.org/wiki/Lambda_calculus">Lambda calculus</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Filter_(higher-order_function)">filter</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Map_(higher-order_function)">map</a></li>
      <li><a href="http://en.wikipedia.org/wiki/Reduce_(higher-order_function)">reduce</a></li>
    </ul>
  </li>
  <li><a href="http://www.python-kurs.eu/lambda.php">Python-Kurs: Lambda, filter, reduce und map</a> (German)</li>
</ul>
