---
layout: post
title: Google Code Jam 2012 - Qualification Round
author: Martin Thoma
date: 2012-04-15 13:35:40.000000000 +02:00
category: Code
tags: Programming, Python, Google, Google Code Jam, competition
featured_image: 2012/04/code-jam-logo.png
---
I've passed the <a href="https://code.google.com/codejam/contest/1460488/dashboard">Qualification Round</a> of Google Code Jam 2012. I've learned, that I am not allowed to submit the large dataset after the first 8 minutes. 

18,365 programmers took part in this contest. 15,692 had at least 20 points and advanced to the First Rounds.

These are my solutions:

<h2>Problem A: Speaking in Tongues</h2>
This one was easy. It's a <a href="http://en.wikipedia.org/wiki/Simple_substitution#Simple_substitution">simple substitution cipher</a>:

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def decode(ciphertext, key="ynficwlbkuomxsevzpdrjgthaq", 
                  alphabet="abcdefghijklmnopqrstuvwxyz"):
    dic={}  
    for i in range(0,len(key)):  
        dic[key[i]] = alphabet[i]  
  
    plaintext=""  
    for l in ciphertext:  
        if l in dic:  
            l=dic[l]  
        plaintext+=l
  
    return plaintext 

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in range(0, testcases):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr+1, decode(cipher)))
```

A minimalistic python solution for this one was suggested by Niklas B. He makes use of <a href="http://docs.python.org/reference/expressions.html#lambda">Lambdas</a>, <a href="http://docs.python.org/library/stdtypes.html#str.translate">str.translate()</a> and <a href="http://docs.python.org/library/string.html#string.maketrans">str.maketrans()</a>:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import string as s

testcases = input()

key = "ynficwlbkuomxsevzpdrjgthaq"
decode= lambda c: s.translate(c, s.maketrans(key, s.ascii_lowercase))

for i in range(0, testcases):
	print decode(raw_input())
```

<h2>Problem B: Dancing With the Googlers</h2>
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import ceil, floor
 
def line2intlist(line):
	list = line.split(' ')
	numbers = [ int(x) for x in list ]
	return numbers

def getDist(points, isSurprising=False):
	p = floor(points / 3.0)
	trip = [p, p, p]
	if 3*p < points:
		trip[0] += 1
	if (3*p + 1) < points:
		trip[1] += 1

	trip.sort(reverse=True)

	if isSurprising and (trip[1] == trip[0]) and trip[1] > 0:
		trip[1] -= 1
		trip[0] += 1
		trip.sort(reverse=True)

	return trip
 
def maxGooglers(nrOfGooglers, surprising, p, points):
	mg = 0
	surp = 0
	for pi in points:
		trip = getDist(pi, True)
		if ceil(pi/3.0) >= p:
			mg += 1
		elif trip[0] >= p:
			surp += 1
	
	mg += min(surp, surprising)

	return mg
 
if __name__ == "__main__":
	testcases = input()
 
	for caseNr in range(0, testcases):
		originalList = line2intlist(raw_input())
		nrOfGooglers = originalList[0]
		surprising = originalList[1]
		p = originalList[2]
		points = originalList[3:]
		print("Case #%i: %i" % (caseNr+1, maxGooglers(nrOfGooglers, surprising, p, points)))
```

<h2>Problem C: Recycled Numbers</h2>
The small dataset of this one was easy, but I had to change my code a bit to make it work for the large dataset. Sadly, I didn't know that I only have 8 minutes to get it work ☹

I've tried cPickle for the 2,000,000 list. It took 128.7 MB and 1 minute 6.287s for the large data set after it was pickled. Without pickling it took 1 minute 31.900s.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import cPickle as pickle
except:
    import pickle

def line2intlist(line):
	list = line.split(' ')
	numbers = [ int(x) for x in list ]
	return numbers

def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return c
	#return n * (n - 1) / 2

def rot(num, rot):
	num = str(num)
	num = num[len(num)-rot:len(num)] + num[0:len(num)-rot]  
	return int(num)

def getRotList(num):
	""" Only return bigger rotated ones """
	rotList = [num]
	for i in range(1, len(str(num))):
		tmp = rot(num, i)
		if tmp not in rotList and len(str(tmp)) == len(str(num)):
			rotList.append(tmp)
	return sorted(rotList)

def inBorder(rotations, A, B):
	count = 0
	for el in rotations:
		if A <= el and el <= B:
			count += 1
	return count

def recycled(A, B, liste):
	pairs = 0
	minList = range(0, B+1)

	for tmpList in liste[A:B+1]:
		if minList[tmpList[0]]:
			nrInBorder = inBorder(tmpList, A, B)
			pairs += binomialCoefficient(nrInBorder, 2)
			minList[tmpList[0]] = 0
			

	return pairs

if __name__ == "__main__":
	liste = []
	try:
		liste = pickle.load(open( "save.p", "rb" ))
	except IOError:
		for i in range(0, 2000001):
			tmp = getRotList(i)
			liste.append(tmp)
		pickle.dump(liste, open( "save.p", "wb" ))

	testcases = input()
 
	for caseNr in range(0, testcases):
		A, B = line2intlist(raw_input())
		print("Case #%i: %i" % (caseNr+1, recycled(A, B, liste)))
```

<h2>Problem D: Hall of Mirrors</h2>
This one was very hard. I had some ideas, but none of them seemed to work. 

This is a solution based on the solution of "dwenzel". At the moment, I've only made some comments and broke some lines to let them fit into my blog. This solution needs about 2 minutes 42 seconds for the small input set and 2 minutes 12 seconds for the large input set.

You might also be interested in the <a href="http://code.google.com/codejam/contest/1460488/dashboard#s=a&a=3">official Contest Analysis</a> with some hints to this challenge.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import floor, ceil, sqrt

precision = 0.01

def line2intlist(line):
    list = line.split(' ')
    numbers = [ int(x) for x in list ]
    return numbers

def seeReflection(x, v, m, d):
    cur_y = x[0]
    cur_x = x[1]
    vy = v[0]
    vx = v[1]
    dist = 0
    while dist <= d + precision:
        if abs(cur_x - x[1]) < precision and \
           abs(cur_y - x[0]) < precision and dist > 0:
            return True

        if vy == 0:
            if vx < 0:
                cur_x -= 0.5
            else:
                cur_x += 0.5
            if abs(cur_x - round(cur_x)) < precision:
                tmp = int(floor(cur_y))
                if vx < 0 and m[tmp][int(round(cur_x) - 1)] == 1:
                    vx = -vx
                elif vx > 0 and m[tmp][int(round(cur_x))] == 1:
                    vx = -vx
            dist += 0.5
        elif vx == 0:
            if vy < 0:
                cur_y -= 0.5
            else:
                cur_y += 0.5
            if abs(cur_y - round(cur_y)) < precision:
                tmp = int(floor(cur_x))
                if vy < 0 and m[int(round(cur_y) - 1)][tmp] == 1:
                    vy = -vy
                elif vy > 0 and m[int(round(cur_y))][tmp] == 1:
                    vy = -vy
            dist += 0.5
        else:
            # Find how far is the next time we hit something 
			# .0 or .5
            if vy < 0:
                dy = cur_y - floor(cur_y)
            else:
                dy = ceil(cur_y) - cur_y
            if dy > 0.5 + precision:
                dy -= 0.5
            elif dy < precision:
                dy += 0.5

            if vx < 0:
                dx = cur_x - floor(cur_x)
            else:
                dx = ceil(cur_x) - cur_x
            if dx > 0.5 + precision:
                dx -= 0.5
            elif dx < precision:
                dx += 0.5

            # See which will come up first
            ty = dy / abs(vy)
            tx = dx / abs(vx)
            if ty > tx:
                t = tx
            else:
                t = ty

            dy = vy * t
            dx = vx * t
            cur_y = cur_y + dy
            cur_x = cur_x + dx
            dist += sqrt(dy * dy + dx * dx)

            roundy = round(cur_y)
            roundx = round(cur_x)
            ybounce = False
            xbounce = False
            if abs(cur_y - roundy) < precision and \
               abs(cur_x - roundx) < precision:
                # Case we're at a corner
                neighbors = []
                intx = int(roundx)
                inty = int(roundy)
                neighbors.append(m[inty - 1][intx - 1] % 2)
                neighbors.append(m[inty - 1][intx] % 2)
                neighbors.append(m[inty][intx] % 2)
                neighbors.append(m[inty][intx - 1] % 2)
                sum = 0
                for neighbor in neighbors:
                    sum += neighbor
                if sum == 1:
                    if vy < 0:
                        nexty = inty - 1
                    else:
                        nexty = inty
                    if vx < 0:
                        nextx = intx - 1
                    else:
                        nextx = intx
                    if m[nexty][nextx] == 1:
                        return False
                elif sum == 3:
                    vy = -vy
                    vx = -vx
                elif sum == 2:
                    if neighbors[0] == neighbors[1]:
                        vy = -vy
                    elif neighbors[0] == neighbors[3]:
                        vx = -vx
            elif abs(cur_y - roundy) < precision:
                # Case we're middle of a top/bottom edge
                if vy < 0:
                    inty = int(roundy - 1)
                else:
                    inty = int(roundy)
                intx = int(floor(cur_x))
                if m[inty][intx] == 1:
                    vy = -vy
            elif abs(cur_x - roundx) < precision:
                # Case we're middle of a top/bottom edge
                if vx < 0:
                    intx = int(roundx - 1)
                else:
                    intx = int(roundx)
                inty = int(floor(cur_y))
                if m[inty][intx] == 1:
                    vx = -vx
    return False


def getMap(H, W):
    map = []
    for el in range(0, H):
        line = raw_input()
        tmp = []
        for char in line:
            if char == '.':
                 tmp.append(0)
            elif char == '#':
                tmp.append(1)
            else:
                tmp.append(2)
        map.append(tmp)
    return map

def process_case(m, H, W, D):
    vectors = set()
    ratios = set()
    for i in range(D + 1):
        for j in range(1, D + 1):
            if i <= j and i*i + j*j <= D * D:
                ratio = float(i) / float(j)
                if ratio not in ratios:
                    vectors.add((i, j))
                    vectors.add((i, -j))
                    vectors.add((-i, j))
                    vectors.add((-i, -j))
                    vectors.add((j, i))
                    vectors.add((j, -i))
                    vectors.add((-j, i))
                    vectors.add((-j, -i))
                    ratios.add(ratio)
    x = None
    for i in range(H):
        for j in range(W):
            if x == None and m[i][j] == 2:
                x = (i + 0.5, j + 0.5)
    count = 0
    for vector in vectors:
        if seeReflection(x, vector, m, D):
            count += 1
    return count

if __name__ == "__main__":
    testcases = input()
    for caseNr in range(0, testcases):
        H, W, D = line2intlist(raw_input())
        map = getMap(H, W)
        print("Case #%i: %i" % (caseNr+1, process_case(map, H, W, D)))
```

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Google_Code_Jam">Google Code Jam</a></li>
  <li><a href="http://www.go-hero.net/jam/12/">Google Code Jam Statistics</a></li>
</ul>
