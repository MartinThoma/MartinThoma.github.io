---
layout: post
lang: en
title: Google Code Jam 2012 &ndash; Round 1C 2012
author: Martin Thoma
date: 2012-05-06 14:03:54.000000000 +02:00
category: Code
tags: Programming, Python, Google, Google Code Jam, competition
featured_image: 2012/04/code-jam-logo.png
---
4230 tried the first problem, but only 3189 people are listed in the <a href="http://code.google.com/codejam/contest/1781488/scoreboard?c=1781488">scoreboard</a>.

<ul>
  <li>Problem 1 (<a href="http://code.google.com/codejam/contest/1781488/dashboard#s=p0">Diamond Inheritance</a>):
  <ul>
     <li>Small Set: 3077/4230 users (73%)</li>
     <li>Large Set: 2387/3044 users (78%)</li>
  </ul>
  </li>
  <li>Problem 2 (<a href="http://code.google.com/codejam/contest/1781488/dashboard#s=p1">Out of Gas</a>):
  <ul>
     <li>Small Set: 471/766 users (61%)</li>
     <li>Large Set: 73/253 users (29%)</li>
  </ul>
  </li>
  <li>Problem 3 (<a href="http://code.google.com/codejam/contest/1781488/dashboard#s=p2">Box Factory</a>):
  <ul>
     <li>Small Set: 1071/1810 users (59%)</li>
     <li>Large Set: 308/788 users (39%)</li>
  </ul>
  </li>
</ul>

<h2>Diamond Inheritance</h2>
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psyco

psyco.full()

testcases = input()


def line2intlist(line):
    list = line.split(" ")
    numbers = [int(x) for x in list]
    return numbers


def getAnswer(classDict, N):
    for startPoint in range(1, N):
        reachable = [startPoint]
        justAppended = [startPoint]
        while len(justAppended) > 0:
            newJustAppended = []
            for node in justAppended:
                for new in classDict[node]:
                    if new in reachable:
                        return "Yes"
                    else:
                        newJustAppended.append(new)
                        reachable.append(new)
            justAppended = newJustAppended
    return "No"


for i in range(0, testcases):
    N = input()
    classDict = {}
    for classNr in range(1, N + 1):
        liste = line2intlist(raw_input())
        classDict[classNr] = liste[1:]
    print("Case #%i: %s" % (i + 1, getAnswer(classDict, N)))
```

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Google_Code_Jam">Google Code Jam</a></li>
  <li><a href="http://www.go-hero.net/jam/12/">Google Code Jam Statistics</a></li>
</ul>
