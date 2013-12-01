---
layout: post
status: publish
published: true
title: ! 'Project Euler: Problem 35'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 48831
wordpress_url: http://martin-thoma.com/?p=48831
date: 2012-11-17 13:23:01.000000000 +01:00
categories:
- Code
tags:
- Programming
- Python
- Challenge
- Project Euler
comments:
- id: 381271
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0xNyAxNTo1ODozNiArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xNyAxMzo1ODozNiArMDEwMA==
  content: ! "You forgot the most important optimization: filtering out all primes
    containing even digits (that means about 96% less possibilities to check!).\r\n\r\nI'm
    interested in seeing how much time you can save by applying this optimization."
- id: 386411
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0xMS0xOCAxOTo0NDowOCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOCAxNzo0NDowOCArMDEwMA==
  content: ! "Hi Simon,\r\n\r\nI don't think that this is \"the most important optimization\".
    I've added it at the end (where it is easy to add), but the new code is only 0.2seconds
    faster.\r\n\r\nMaybe you could get it a little bit faster if you rewrote the whole
    code, but I don't think that the possible speed up of at most 1 second is worth
    about 10 minutes of programming.\r\n\r\nCheers,\r\nMartin"
- id: 391001
  author: Simon
  author_email: simon.schaefer4@student.kit.edu
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0xOSAxNjowNToyNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0xOSAxNDowNToyNyArMDEwMA==
  content: ! "Maybe you can save some time by using something like\r\n\r\n  prime%10%2
    == 0 or prime%10%5 == 0\r\n\r\ninstead of checking each searching each digit in
    str(prime). But that is probably only some premature optimization and not useful
    if one is not interested in the most efficient solution."
- id: 445571
  author: Tur1ng
  author_email: none@example.com
  author_url: ''
  date: !binary |-
    MjAxMi0xMS0yNSAyMDoyMzo0NCArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMS0yNSAxODoyMzo0NCArMDEwMA==
  content: ! "Change\r\nfor currentPrime in xrange(2, n):\r\nto\r\nfor currentPrime
    in xrange(3, n, 2):"
featured_image: 2012/04/leonhard-euler.jpg
---
The task in <a href="http://projecteuler.net/problem=35">Problem 35</a> of Project Euler is:

<blockquote>The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?</blockquote>

<h2>How to solve</h2>
If you have heard of the sieve of Eratosthenes, this one sounds quite easy:
<ol>
  <li>Find all primes below one million</li>
  <li>For each prime, do:
    <ol>
      <li>Generate all rotations</li>
      <li>Check for every rotation if it is a prime</li>
    </ol>
  </li>
  <li>Count the number of circular primes</li>
</ol>

<h2>The implementation</h2>
<h3>Sieve of Eratosthenes</h3>
The finds all primes below $n \in \mathbb{N}$. But you can make a lot of mistakes in the implementation.

First, this is the way the sieve of Eratosthenes works:

[caption id="attachment_48841" align="aligncenter" width="445"]<a href="http://martin-thoma.com/project-euler-problem-35/sieve_of_eratosthenes_animation/" rel="attachment wp-att-48841"><img src="http://martin-thoma.com/wp-content/uploads/2012/11/Sieve_of_Eratosthenes_animation.gif" alt="Sieve of Eratosthenes animation" title="Sieve of Eratosthenes animation" width="445" height="369" class="size-full wp-image-48841" /></a> Sieve of Eratosthenes: algorithm steps for primes below 121 (including optimization of starting from prime's square).
Source: <a href="http://commons.wikimedia.org/wiki/File:Sieve_of_Eratosthenes_animation.gif">Wikimedia</a>[/caption]

For example, this implementation is not good:
{% highlight python %}def getPrimesBelowN(n=1000000):
    """ Sieve of Eratosthenes """
    from math import ceil
    roundUp = lambda n, prime: int(ceil(float(n) / prime))

    primes = range(2, n)
    for currentPrime in primes:
        for multiplicant in xrange(2, roundUp(n, currentPrime)):
            noPrime = multiplicant * currentPrime
            if noPrime in primes: 
                primes.remove(noPrime)
    return primes{% endhighlight %}

Whats bad with this code? 
Well, just think about what it does: For every <code>noPrime</code> Python has to go through the whole list. I couldn't find how <code>in</code> is implemented, but I guess it is linear. So Python has to go through the whole list for <code>in</code>. Additionally, <code>remove</code> could also be expensive.

How could this get improved? Here is a better solution:
{% highlight python %}def getPrimesBelowN(n=1000000):
    """ Sieve of Eratosthenes """
    from math import ceil
    roundUp = lambda n, prime: int(ceil(float(n) / prime))

    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []

    for currentPrime in xrange(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in xrange(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primeList{% endhighlight %}

This solution does not need to search for <code>noPrime</code>, it simply jumps there in the list.

A generator version of the sieve of Erasthostenes can be found on <a href="http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/">code.activestate.com</a>.

<h3>isCircularPrime</h3>
Rotation the digits of a number is the same as cutting the number into two pieces and switching the position of the pieces:
{% highlight python %}def isCircularPrime(primes, number):
    number = str(number)
    for i in xrange(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if int(rotatedNumber) not in primes:
            return False
    return True{% endhighlight %}

Here is the same problem as above, in the sieving algorithm: Searching through the list takes much more time than jumping to a position in the list. So this one is better:

{% highlight python %}def isCircularPrime(primes, number):
    number = str(number)
    for i in xrange(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True{% endhighlight %}

<h3>Some more speedups</h2>
Every prime that contains one of the digits 0, 2, 4, 6 or 8 can't be a circular prime, because one rotation exist where that digit is at the end. This rotation would be divisible by 2 and thus not be a prime (except for 2, of course).
You can use the same thought for the digit 5.

So you can skip those digits

<h3>The final snippet</h3>
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def getPrimesBelowN(n=1000000):
    """Get all primes below n with the sieve of Eratosthenes. 
    @return: a list 0..n with boolean values that indicate if 
             i in 0..n is a prime.
    """
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in xrange(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in xrange(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes
 
def isCircularPrime(primes, number):
    """Check if number is a circular prime.
     
    Keyword arguments:
    primes -- a list from 0..n with boolean values that indicate if 
              i in 0..n is a prime
    number -- the integer you want to check
    """
    number = str(number)
    for i in xrange(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True
 
if __name__ == "__main__":
    print("Start sieving.")
    primes = getPrimesBelowN(1000000)
    print("End sieving.")
    numberOfPrimes = 2
    print(2)    # I print them now, because I want to skip all primes
    print(5)    # that contain one of those digits: 0,2,4,5,6,8
    for prime, isPrime in enumerate(primes):
        if (not isPrime) or ("2" in str(prime)) or \
           ("4" in str(prime)) or ("6" in str(prime)) or \
           ("8" in str(prime)) or ("0" in str(prime)) or \
           ("5" in str(prime)):
            continue
        if isCircularPrime(primes, prime):
            print(prime)
            numberOfPrimes += 1
 
    print("Number of circular primes: %i" % numberOfPrimes){% endhighlight %}

It takes about 1.096 seconds (in comparison: having the version of <code>isCircularPrime</code> that searches through the list of primes took over 5 minutes!)
