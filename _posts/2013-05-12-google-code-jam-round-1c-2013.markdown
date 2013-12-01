---
layout: post
status: publish
published: true
title: Google Code Jam &ndash; Round 1C 2013
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 65921
wordpress_url: http://martin-thoma.com/?p=65921
date: 2013-05-12 15:01:15.000000000 +02:00
categories:
- Code
tags:
- Google Code Jam
comments:
- id: 1190171
  author: wolf5x
  author_email: wolf5x1016@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xMiAxNzozNDowMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xMiAxNTozNDowMiArMDIwMA==
  content: Could you teach me how to prove the greedy part of problem Pogo?  Thank
    you in advance!!
- id: 1190371
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNS0xMyAwOTozMzowOCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xMyAwNzozMzowOCArMDIwMA==
  content: ! "What exactly do you want to prove?\r\n\r\n<ol type=\"A\">\r\n<li>A)
    The provided algorithm always finds the minimal solution.</li>\r\n<li>B) The
    problem can be approached with a greedy algorithm.</li>\r\n<li>C) The maximum
    number of steps (calculated in the while loop) is high enough and minimal.</li>\r\n</ol>"
- id: 1191131
  author: Edward
  author_email: edward.lockhart@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xNSAxNDo1Njo1NiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xNSAxMjo1Njo1NiArMDIwMA==
  content: ! 'This takes four minutes to solve C large on my desktop: <a href="https://gist.github.com/MartinThoma/5589820"
    rel="nofollow">Code on GitHub</a>'
- id: 1191561
  author: Edward
  author_email: edward.lockhart@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xNiAxMzo0MzoyNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xNiAxMTo0MzoyNiArMDIwMA==
  content: ! 'Some html problems with that. I''ve fixed it here: https://gist.github.com/ice7/5591136'
- id: 1191641
  author: stan
  author_email: stanislav.zholnin@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xNiAxNzozMTowMCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xNiAxNTozMTowMCArMDIwMA==
  content: ! "Mutlithreading is the way to go with Python. You can easily get 3.5
    faster on simple 4-core CPU. I updated my codejam template with multithreading
    specifically for participation in round 2.\r\n\r\nI know that 4 minutes is OK,
    but with codejam rules, when you have just one attempt, watching you program go
    and guessing if it finishes on time is very difficult. So if you can cut execution
    time from 4 minutes to 1.2 that's a bit win."
- id: 1191841
  author: Hamition
  author_email: yangjie0825@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xNyAwNTowMzowMCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xNyAwMzowMzowMCArMDIwMA==
  content: ! "How could you prove the correctness of the greedy part. Why we could
    always make x and y be zero by applying the greedy part:\r\n\"After you know the
    maximum number of steps, you can apply a greedy solution: Start from (x|y) and
    always go into the direction that is farer away from the origin.\""
- id: 1192041
  author: Quang Vu
  author_email: vhquang@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wNS0xOCAwMjowODoyMyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xOCAwMDowODoyMyArMDIwMA==
  content: ! "Like many others, I am interested in the proof of correctness of the
    greedy approach. So I guess let start with your option B.\r\n\r\nLet call s(i)
    the step number i. So, in the basic case, if our x+y = sum( s(i) for i:1->n )
    , with n is the number of steps. In this basic case, traversing the greedy route
    (the further of x or y), we will end up exactly in our destination point(x,y).
    This case is straight forward.\r\n\r\nBut our interesting case is when x + y >
    sum( s(i) for i:1->n ). \r\nSo that means we need to make one extra step s(n+1).
    \r\nMeaning sum( s(i) for i:1->n+1) > x+y. Let call k = that sum - (x+y).\r\nAnd
    because our sum is larger, at least there will be one j that s(j) is in opposite
    direction to our greedy direction. For example, if our greedy direction is NW,
    there will be at least one j that s(j) is stepping S or E.\r\n\r\nWith your above
    algorithm (and from most accepted solutions for round 1C), it looks like there
    is an assumption that j will be n-1 or n. In another word, there is an assumption
    that since you are greedily moving to your point (by subtracting your step from
    your total distance x+y), the last step you make should be that counter-greedy
    step. And now that sounds like an illogical assumption to me. (*)\r\n\r\nBut with
    most greedy approach, your solution works or fails depend on the input. And they
    specifically say that your destination(x,y) will always be reachable. How can
    that be used to show that if the point is reachable, your counter-greedy step
    should be at the end? (**)\r\n\r\n(*) and (**) are very similar and I don't know
    if I should differentiate those two. But I can't find explaination for both lead.
    And that is when I decide to Google to see if anyone has a better idea."
- id: 1192101
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNS0xOCAxMToyMjoyNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNS0xOCAwOToyMjoyNiArMDIwMA==
  content: ! "Dear Quang Vu,\r\n\r\nthanks for your comment.\r\n\r\nWhat is \"n\"
    in your comment?\r\n\r\nI'm pretty sure that every (x,y) in Z^2 is reachable.
    See my proof for the number of steps below.\r\n\r\nI've started to write a <a
    href=\"https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/proof-of-correctness-pogo\"
    rel=\"nofollow\">proof of correctness for (A) and (C) on GitHub</a>. When
    I correctly prove (A) this will imply (B). But this will take some time. Suggestions
    are always welcome (even if it is only spelling as it is difficult for me to write
    this proof in English)"
---
<ul>
<li>Problem A (<a href="https://code.google.com/codejam/contest/2437488/dashboard#s=p0">Consonants</a>):
  <ul>
    <li>Small Set: 4305/4834 users (89%)</li>
    <li>Large Set: 1551/3778 users (41%)</li>
  </ul>
<li>Problem B (<a href="https://code.google.com/codejam/contest/2437488/dashboard#s=p1">Pogo</a>):
  <ul>
    <li>Small Set: 2537/3129 users (81%)</li>
    <li>Large Set: 121/638 users (19%)</li>
  </ul>
</li>
<li>Problem C (<a href="https://code.google.com/codejam/contest/2437488/dashboard#s=p2">The Great Wall</a>):
  <ul>
    <li>Small Set: 934/1260 users (74%)</li>
    <li>Large Set: 74/330 users (22%)</li>
  </ul>
</li>
</ul>

More information is on <a href="http://www.go-hero.net/jam/13/round/3">go-hero.net</a>.

<h2>Consonants</h2>
A solution from <a href="http://www.go-hero.net/jam/13/name/nip">nip</a>:
{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s, n):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    nvalue = 0
    count = 0 # how many consecutive consonants
    pos = -1 # position of the last substring of n consonants
    for i, c in enumerate(s):
        if c in vowels:
            count = 0
        else:
            count += 1
        if count >= n:
            pos = i + 2 - n
        if pos >= 0:
            nvalue += pos
    return nvalue
 
if __name__ == "__main__":
    testcases = input()
      
    for caseNr in xrange(1, testcases+1):
        name, n = raw_input().split(" ")
        print("Case #%i: %s" % (caseNr, solve(name, int(n))))
{% endhighlight %}

<h2>Pogo</h2>
This is a very clever solution from xiaowuc1 (translated from Java to Python).

The idea is to calculate at first the maximum number of steps you need and then go from your target destination to the origin.

How many steps do you need?
In the $i$ round, you will make $i$ steps. You need at least $x+y$ steps to get from $(0|0)$ to $(x|y)$. This means, you need to solve $\sum_{i=1}^n i = x + y$ for $n$. This is $\frac{n^2 + n}{2} = x+y$. You might also need to make one extra step if the parity of $\frac{n^2 + n}{2}$ is not the same as $x+y$.
You can calculate this with a simple loop (see code below).

After you know the maximum number of steps, you can apply a greedy solution: Start from $(x|y)$ and always go into the direction that is farer away from the origin.

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculateSteps(x, y):
    s = 0
    dist = abs(x) + abs(y)
    while (s**2 + s)/2 < dist or ((s**2 + s)/2)%2 != dist%2:
        s += 1
    return s
 
def solve(x,y):
    """ starting at (0|0) and going i steps, 
        how can you reach (x|y)? """   
    s = calculateSteps(x, y)
 
    solution = ""
    for i in range(s, 1-1,-1):
        if abs(x) > abs(y):
            if x > 0:
                solution += "E"
                x -= i
            else:
                solution += "W"
                x += i
        else:
            if y > 0:
                solution += "N"
                y -= i
            else:
                solution += "S"
                y += i
    return solution[::-1]

if __name__ == "__main__":
    testcases = input()
 
    for caseNr in xrange(1, testcases+1):
        x,y = raw_input().split(" ")
        x,y = int(x),int(y)
        print("Case #%i: %s" % (caseNr, solve(x,y)))
{% endhighlight %}

<h2>The Great Wall</h2>
The following solution is not applicable for the large input set, but it works fine for the small one:

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def prepareTribes(tribes):
    tribeStack = []
    for tribe in tribes:
        for attackNumber in range(0, tribe["ni"]):
            tribeStack.append({
                "day" :tribe["di"]+attackNumber*tribe["delta_di"],
                "west":2*(tribe["wi"]+attackNumber*tribe["delta_pi"]),
                "east":2*(tribe["ei"]+attackNumber*tribe["delta_pi"]),
                "height":tribe["si"]+attackNumber*tribe["delta_si"]
            })
    return sorted(tribeStack, key=lambda tribe: tribe["day"])

def runAttack(wall, tribe):
    increase = []
    for i in xrange(tribe["west"], tribe["east"] + 1):
        if wall[i] < tribe["height"]: # wall-ee
            increase.append({"wallPos" : i, "height" : tribe["height"]})

    return increase

def solve(tribes):
    wall = defaultdict(int)
    tribeStack = prepareTribes(tribes)
    #for tribe in tribeStack:
    #    print tribe["day"], "[" + str(tribe["west"]) + "," + str(tribe["east"])+"]", tribe["height"]
    successes = 0
    increase = []
    for i, tribe in enumerate(tribeStack):
        increaseTmp = runAttack(wall, tribe)
        #print wall
        #print tribe
        if len(increaseTmp) > 0:
            successes += 1

        increase += increaseTmp

        if i+1==len(tribeStack) or tribeStack[i+1]["day"] > tribe["day"]:
            for el in increase:
                if wall[el["wallPos"]] < el["height"]:
                    wall[el["wallPos"]] = el["height"]
    return successes

if __name__ == "__main__":
    testcases = input()
      
    for caseNr in xrange(1, testcases+1):
        N = input() # Number of tribes attacking the wall
        tribes = []
        for tribe in range(N):
            di, ni, wi, ei, si, delta_di, delta_pi, delta_si = raw_input().split(" ")
            tribes.append({"di":int(di), # the day of the tribe's first attack
            "ni": int(ni), # the number of attacks from this tribe
            "wi": int(wi), # the westmost 
            "ei": int(ei), # and eastmost points respectively of the Wall attacked on the first attack
            "si": int(si), # the strength of the first attack
            "delta_di": int(delta_di), # the number of days between subsequent attacks by this tribe
            "delta_pi": int(delta_pi), # the distance this tribe travels to the east between subsequent attacks (if this is negative, the tribe travels to the west)
            "delta_si": int(delta_si) # the change in strength between subsequent attacks
            })
        print("Case #%i: %s" % (caseNr, solve(tribes)))
{% endhighlight %}

By the way, nobody has solved the large input set of this one with Python! But here is a <a href="http://www.go-hero.net/jam/13/name/eatmore">Java solution</a>.
