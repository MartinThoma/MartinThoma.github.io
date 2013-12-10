---
layout: post
status: publish
published: true
title: Google Code Jam &ndash; Round 1B 2013
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 65421
wordpress_url: http://martin-thoma.com/?p=65421
date: 2013-05-05 16:15:32.000000000 +02:00
categories:
- Code
tags:
- Python
- Google Code Jam
comments:
- id: 1188201
  author: hashed
  author_email: mariomaresca@hotmail.it
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0wNiAwMTozNjoxOSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0wNSAyMzozNjoxOSArMDIwMA==
  content: ! "Wow that's almost exactly how I did the falling diamonds (after the
    2h:30). That formula is basic this formula:\r\n\r\nhttp://math.stackexchange.com/a/382123/32707"
- id: 1188431
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNS0wNyAyMjowODozMyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0wNyAyMDowODozMyArMDIwMA==
  content: ! "You might be interested in\r\n\r\nhttps://github.com/tmoertel/practice/blob/master/google-code-jam/2013/round-1B-B-falling-diamonds/diamonds.py"
- id: 1188761
  author: d
  author_email: blah@blah.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0wOSAwNTozMTo0MCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0wOSAwMzozMTo0MCArMDIwMA==
  content: ! "Here's a simple implementation of Osmos in Javascript:\r\n\r\nfunction
    rs(si) \r\n{\r\n  var a = Scanner.scanf('%d'), n = Scanner.scanf('%d');\r\n  count
    = 0, min = Infinity;\r\n  var m = Scanner.toArray('%d', n).sort(function(a, b){
    return a - b; })\r\n  \r\n  for (var i = 0; i  (count+(m.length-i))) ? (count+(m.length-i))
    : min;\r\n    if (min  m[i]) {\r\n      a+=m[i];\r\n    } else if (a < 2) {\r\n
    \     count = m.length;\r\n      break;\r\n    } else {\r\n      a+=(a-1); i-=1;
    count+=1;\r\n    }\r\n  }\r\n  \r\n  Scanner.printf(&#039;Case #&#039; + si +
    &#039;: &#039; + ((min < count) ? min : count));\r\n}\r\n\r\nScanner.read(&#039;input.txt&#039;,
    function() {\r\n  var rows = Scanner.scanf(&#039;%d&#039;);\r\n  for (var i =
    0; i < rows; ++i) { rs((i+1)); }\r\n});"
featured_image: 2012/04/code-jam-logo.png
---
<ul>
<li>Problem A (<a href="https://code.google.com/codejam/contest/2434486/dashboard#s=p0">Osmos</a>):
  <ul>
    <li>Small Set: 4668/7250 users (64%)</li>
    <li>Large Set: 3537/4578 users (77%)</li>
  </ul>
<li>Problem B (<a href="https://code.google.com/codejam/contest/2434486/dashboard#s=p1">Falling Diamonds</a>):
  <ul>
    <li>Small Set: 952/1882 users (51%)</li>
    <li>Large Set: 525/724 users (73%)</li>
  </ul>
</li>
<li>Problem C (<a href="https://code.google.com/codejam/contest/2434486/dashboard#s=p2">Garbled Email</a>):
  <ul>
    <li>Small Set: 444/896 users (50%)</li>
    <li>Large Set: 255/345 users (74%)</li>
  </ul>
</li>
</ul>

More information are on <a href="http://www.go-hero.net/jam/13/round/2">go-hero.net</a>.

<h2>Osmos</h2>
{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def howBigDoIget(A, motes):
    while len(motes) > 0 and A > min(motes):
        A += min(motes)
        motes.remove(min(motes))
    return A

def stepsNeededForNext(A, motes):
    m = min(motes)
    steps = 0
    if m >= 1 and A == 1:
        return 10**12
    while A <= m:
        A += (A-1)
        steps += 1
    return steps

def solve(A, motes):
    steps = 0
    A = howBigDoIget(A, motes)
    while len(motes) > 0 and A <= max(motes):
        if (stepsNeededForNext(A, motes) >= len(motes)):
            steps += len(motes)
            return steps
        else:
            A += (A-1)
        A = howBigDoIget(A, motes)
        steps += 1
    return steps
 
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        A, N = map(int,raw_input().split(" "))
        motes = sorted(map(int,raw_input().split(" ")))
        copyed = motes[:]
        solution = solve(A, motes)
        if solution > N:
            solution = N
        print("Case #%i: %s" % (caseNr, solution))
{% endhighlight %}

<h2>Falling Diamonds</h2>
Oncee you've read the task, you should understand some very basic ideas:

<ul>
  <li>First of all, diamonds only fall at $x=0$!</li>
  <li>If your target coordinates are $(x,y)$, you have the same output as for $(-x,y)$, as everything is symmetric.</li>
  <li>You have to get a basis for your diamonds pyramid. I've colored the basis in yellow in the images below.</li>
  <li>When your target is above the ground, you can let the diamond slide down to calculate the size of the basis.</li>
</ul>

{% caption align="aligncenter" width="512" caption="You have to get those yellow diamonds first, before you can get the orange one." url="../images/2013/05/falling-diamonds-base.jpg" alt="A basis for diamonds" title="" height="323" class="size-full wp-image-65431" %}

{% caption align="aligncenter" width="512" caption="Let Diamonds slide down" url="../images/2013/05/falling-diamonds-slide.jpg" alt="Let Diamonds slide down" title="" height="254" class="size-full wp-image-65441" %}

Note that you don't have to calculate a probabilty for the yellow pyramids. You get those with probability of 1.

What I've forgot: You should also catch the case that you can fill up the next bigger pyramid. If this is possible, you can guarantee that you will reach your target $(x,y)$.

The rest is simple math. You have $rest$ diamonds left after you've build the base (yellow). Then you need $y+1$ diamonds slide to the right side. The probability that you have exactly $k$ hits while making $N$ tries with a probability of 50% is $\binom{N}{k} \cdot (\frac{1}{2})^N$. You want at least $k$ hits, so you want $\sum_{i=k}^N \binom{N}{i} \cdot (\frac{1}{2})^N$.

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gmpy

""" Calculate the binomial coefficient """
def binomial(n, k):
    return gmpy.comb(n,k)

""" 
    @param N: Number of diamonds
    @param x,y: Target coordinate
    @return: possiblity, that a diamond will be at coordinate (x,y) 
"""
def solve(N, x, y):
    if x == 0:
        n = y+1
        if N >= (n*n+n)/2:
            return 1.0
        else:
            return 0.0

    # From this point, x != 0 is True

    xTmp = x + y # let target slide down

    n = xTmp-1
    baseDiamands = (n**2+n)/2

    # are there enough diamonds left after you've build the basis?
    rest = N - baseDiamands
    if rest <= 0:
        return 0.0

    # are there enough diamonds left so that you can guarantee that 
    # you will  fill up the next bigger pyramid at least to the 
    # target position?
    biggerBaseDiamonds = baseDiamands+n+2+y
    if N >= biggerBaseDiamonds:
        return 1.0

    # some math:
    # bernoulli
    prob = 0.0
    hitsNeeded = y+1

    for k in range(hitsNeeded, rest+1):
        prob += binomial(rest,k)
    
    return prob/2**rest
 
if __name__ == "__main__":
    testcases = input()
      
    for caseNr in xrange(1, testcases+1):
        N, x, y = map(int,raw_input().split(" "))
        print("Case #%i: %.9Lf" % (caseNr, solve(N, abs(x), y)))
{% endhighlight %}
