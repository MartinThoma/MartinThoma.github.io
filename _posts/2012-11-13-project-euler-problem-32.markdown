---
layout: post
status: publish
published: true
title: ! 'Project Euler: Problem 32'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 48721
wordpress_url: http://martin-thoma.com/?p=48721
date: 2012-11-13 11:52:12.000000000 +01:00
categories:
- Code
tags:
- Challenge
- Project Euler
- brute-force
comments:
- id: 371511
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0xMyAxNTo0MjoyOCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xMyAxMzo0MjoyOCArMDEwMA==
  content: ! "The problem with the one-liner is not that it is a one-liner but that
    all intermediate results are inlined, where it would have been better to assign
    them to meaningful names.\r\n\r\nI solved this problem once with Scala and it
    would be possible to do it something like this:\r\n\r\nhttps://gist.github.com/4065631\r\n\r\nThe
    result is completely unreadable - instead I decided to format it like this:\r\n\r\nhttps://gist.github.com/4065585\r\n\r\nWhich
    is very readable in my opinion although there are no explicit loops and no mutable
    state. I don't think it is cool to write one-liners - I think it is cool to write
    code that could be one-liners when they are formatted different."
- id: 371871
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMS0xMyAyMzowMTo1NSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xMyAyMTowMTo1NSArMDEwMA==
  content: ! "Well, a one-liner is naturally inlined ...\r\n\r\nBut I definitely agree
    in every point you've mentioned:\r\n\r\n * You could solve this much shorter,
    but still readable\r\n * Scipping intermediate results without very good documentation
    and other reasons should not be done\r\n * Short, but readable code (sometimes
    also called \"elegant solution\") is cool\r\n\r\nCheers,\r\nMartin"
---
The task in Problem 32 of Project Euler is:

<blockquote>We shall say that an $n$-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, $39 \cdot 186 = 7254$, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</blockquote>

<h2>How to solve it</h2>
We have to get a check, if a number is pandigital. It could look like this:

{% highlight python %}def isPandigitalString(string):
    """ Check if string contains a pandigital number. """
    digits = len(string)

    if digits >= 10:
        return False

    for i in xrange(1,digits+1):
        if str(i) not in string:
            return False
    return True{% endhighlight %}

We also need a check if a product of two numbers is 9-pandigital:
{% highlight python %}def gives9PandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigitalString(numbers){% endhighlight %}

Now you need to figure out how to go through all possible combinations:
{% highlight python %}products = []
for a in xrange(0, 100000):
    for b in xrange(a, 100000):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if gives9PandigitalProduct(a, b):
            products.append(a*b)
            print("%i x %i = %i" % (a, b, a*b))

print(sum(set(products))){% endhighlight %}

<h2>One-liner</h2>
This is from Thaddeus Abiye from Ethiopia:
{% highlight python %}print sum(set(map(lambda x:int(x[0:4]),filter(lambda x:sorted([i for i in x])==map(str,range(1,10)),[str(a*b)+str(a)+str(b) for a in range(1,2000) for b in range(1,100)])))){% endhighlight %}

It needs one line and 173 characters, but I think it's hard to read.

<h2>Data about my solution</h2>
<ul>
  <li>It worked in less than a second.</li>
  <li>28 LOC (including whitespaces and comments)</li>
  <li>719 characters for this solution (including whitespace and comments)</li>
</ul>
