---
layout: post
title: Google Code Jam 2012 &ndash; Round 1A 2012
author: Martin Thoma
date: 2012-04-28 06:11:22.000000000 +02:00
category: Code
tags: Programming, Python, Google, Google Code Jam, competition
---
3691 people are listed in the scoreboard, but 3851 tried the first problem. So I guess the number of contestants might even be higher.

<ul>
  <li>Problem 1 (<a href="http://code.google.com/codejam/contest/1645485/dashboard#s=p0">Password Problem</a>):
  <ul>
     <li>Small Set: 3511/3851 users (91%)</li>
     <li>Large Set: 2329/3376 users (69%)</li>
  </ul>
  </li>
  <li>Problem 2 (<a href="http://code.google.com/codejam/contest/1645485/dashboard#s=p1">Kingdom Rush</a>):
  <ul>
     <li>Small Set: 1912/3466 users (55%)</li>
     <li>Large Set: 1617/1848 users (88%)</li>
  </ul>
  </li>
  <li>Problem 3 (<a href="http://code.google.com/codejam/contest/1645485/dashboard#s=p2">Cruise Control</a>):
  <ul>
     <li>Small Set: 65/312 users (21%)</li>
     <li>Large Set: 22/42 users (52%)</li>
  </ul>
  </li>
</ul>


Just as last time, you can execute these scripts by
```bash
python jam.py < A-small-practice.in > results.txt
```

<a id="more"></a><a id="more-23361"></a>

<h2>Passwords</h2>
This works only for the small input set:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def line2floatlist(line):
    """
    Convert integers in one line, separated by space to a list of integers.
    """
    list = line.split(" ")
    numbers = [float(x) for x in list]
    return numbers


def prob(A, B, probabilities):
    typesMin = float("inf")
    for i in range(0, A + 1):
        probKorrect = 1.0
        for el in probabilities[0 : (len(probabilities) - i)]:
            probKorrect *= el
        probWrong = 1.0 - probKorrect
        remainingTypes = i + (B - A + i) + 1
        remainingTypesErr = remainingTypes + B + 1
        types = probKorrect * remainingTypes + probWrong * remainingTypesErr
        # print types
        if types < typesMin:
            typesMin = types
    if (1 + B + 1) < typesMin:
        typesMin = 1 + B + 1

    return round(typesMin, 6)
    # return typesMin


if __name__ == "__main__":
    testcases = input()

    for caseNr in range(0, testcases):
        A, B = raw_input().split(" ")
        A = int(A)
        B = int(B)
        probabilities = line2floatlist(raw_input())
        # print ((A+1), B)
        # print probabilities
        print("Case #%i: %.6lf" % (caseNr + 1, prob(A, B, probabilities)))
```

<h2>Kingdom Rush</h2>
My solution works only for the small input set:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


def line2intlist(line):
    """
    Convert integers in one line, separated by space to a
    list of integers.
    """
    list = line.split(" ")
    numbers = [int(x) for x in list]
    return numbers


def isSolvable(starDict):
    """ Is it possible to solve this one? """
    intList = []
    for index in starDict:
        wasInFor = True
        one, two = starDict[index]
        intList.append(one)
        intList.append(two)
    intList.sort()

    for levelVar in range(0, len(intList)):
        if levelVar < intList[levelVar]:
            return False
    return True


def king(starDict, myLevel=0, myCompetes=0, partially=[]):
    somethingChanged = True
    while somethingChanged:
        removeList = []
        somethingChanged = False

        # all where i can do both
        for index in starDict:
            one, two = starDict[index]
            if two <= myLevel:
                removeList.append(index)
                somethingChanged = True

        # remove them
        for index in removeList:
            myCompetes += 1
            del starDict[index]
            if index in partially:
                myLevel += 1
                partially.remove(index)
            else:
                myLevel += 2

    if starDict:
        minCompetes = float("inf")
        for index in starDict:
            one, two = starDict[index]
            if one <= myLevel and (index not in partially):
                starDictTmp = deepcopy(starDict)
                partiallyTmp = deepcopy(partially)
                partiallyTmp.append(index)
                tmpCompetes = king(
                    starDictTmp, myLevel + 1, myCompetes + 1, partiallyTmp
                )
                if tmpCompetes < minCompetes:
                    minCompetes = tmpCompetes
        myCompetes = minCompetes
    return myCompetes


if __name__ == "__main__":
    testcases = input()

    for caseNr in range(0, testcases):
        levels = input()
        stars = []
        for i in range(0, levels):
            stars.append(line2intlist(raw_input()))

        # make stars dictionary
        starDict = {}
        level = 1
        for el in stars:
            starDict[level] = deepcopy(el)
            level += 1

        if not isSolvable(starDict):
            print("Case #%i: Too Bad" % (caseNr + 1))
        else:
            print("Case #%i: %s" % (caseNr + 1, king(starDict)))
```

<h2>Cruise Controll</h2>
Only 22 people have a perfect solution for this one.

This is the solution of royf:
```python
import itertools
import math
import numpy


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_letters(f):
    return list(read_word(f))


def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]


def read_words(f, d=" "):
    return read_word(f).split(d)


def read_ints(f, b=10, d=" "):
    return [int(x, b) for x in read_words(f, d)]


def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res


def solve(solver, fn, out_fn=None):
    in_fn = fn + ".in"
    if out_fn is None:
        out_fn = fn + ".out"
    with open(in_fn, "r") as fi:
        with open(out_fn, "w") as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)


################################################################################


def read_case(f):
    N = read_int(f)
    Cs = []
    for i in range(N):
        (C, S, P) = read_words(f)
        Cs.append((C, int(S), int(P)))
    return (N, Cs)


def write_case(f, i, res):
    f.write("Case #%d: " % i)
    f.write("%s" % res)
    f.write("\n")


################################################################################

INF = float("inf")

import heapq


def solve_small(case):
    (N, Cs) = case
    col = []
    for i in range(N):
        (c1, s1, p1) = Cs[i]
        for j in range(i + 1, N):
            (c2, s2, p2) = Cs[j]
            if s1 == s2:
                if abs(p1 - p2) < 5:
                    heapq.heappush(col, (-1, True, i, j))
                continue
            t1 = (p2 - p1 + 5) / (s1 - s2)
            t2 = (p2 - p1 - 5) / (s1 - s2)
            if t1 > t2:
                (t1, t2) = (t2, t1)
            if t2 < 0:
                continue
            if t1 < 0:
                t1 = -1
            heapq.heappush(col, (t1, True, i, j))
            heapq.heappush(col, (t2, False, i, j))
    l = [None] * N
    act = []
    for i in range(N):
        act.append(set())
    cnt = 0
    while col:
        (t, c, i, j) = heapq.heappop(col)
        if c:
            act[i].add(j)
            act[j].add(i)
        else:
            act[i].remove(j)
            act[j].remove(i)
        if t == -1:
            l[i] = Cs[i][0] == "L"
            l[j] = Cs[j][0] == "L"
            continue
        if c:
            if l[i] is None:
                if l[j] is None:
                    l[i] = (cnt, True)
                    l[j] = (cnt, False)
                    cnt += 1
                elif l[j] is True:
                    l[i] = False
                elif l[j] is False:
                    l[i] = True
                else:
                    (k, b) = l[j]
                    l[i] = (k, not b)
            elif l[i] is True:
                if l[j] is None:
                    l[j] = False
                elif l[j] is True:
                    return t
                elif l[j] is False:
                    pass
                else:
                    (k, b) = l[j]
                    for x in range(N):
                        if isinstance(l[x], tuple) and l[x][0] == k:
                            l[x] = b != l[x][1]
            elif l[i] is False:
                if l[j] is None:
                    l[j] = True
                elif l[j] is True:
                    pass
                elif l[j] is False:
                    return t
                else:
                    (k, b) = l[j]
                    for x in range(N):
                        if isinstance(l[x], tuple) and l[x][0] == k:
                            l[x] = b == l[x][1]
            else:
                (k, b) = l[i]
                if l[j] is None:
                    l[j] = (k, not b)
                elif l[j] is True:
                    for x in range(N):
                        if isinstance(l[x], tuple) and l[x][0] == k:
                            l[x] = b != l[x][1]
                elif l[j] is False:
                    for x in range(N):
                        if isinstance(l[x], tuple) and l[x][0] == k:
                            l[x] = b == l[x][1]
                else:
                    (k_, b_) = l[j]
                    if k == k_:
                        if b == b_:
                            return t
                        else:
                            continue
                    for x in range(N):
                        if isinstance(l[x], tuple) and l[x][0] == k:
                            l[x] = (k_, not b ^ b_ ^ l[x][1])
        else:  # end col
            if not act[i]:
                l[i] = None
            if not act[j]:
                l[j] = None
    return "Possible"


solve_large = solve_small

##def solve_large(case):

DEBUG = "i"

from run import *
```

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Google_Code_Jam">Google Code Jam</a></li>
  <li><a href="http://www.go-hero.net/jam/12/">Google Code Jam Statistics</a></li>
</ul>
