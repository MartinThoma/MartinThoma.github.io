---
layout: post
title: Google Code Jam &ndash; Round 1A 2013
author: Martin Thoma
date: 2013-04-27 07:15:17.000000000 +02:00
category: Code
tags: Python, Google Code Jam, NumPy, itertools
featured_image: 2012/04/code-jam-logo.png
---
<ul>
<li>Problem A (<a href="https://code.google.com/codejam/contest/2418487/dashboard#s=p0">Bullseye</a>):
  <ul>
    <li>Small Set: 5856/6195 users (95%)</li>
    <li>Large Set: 1806/4795 users (38%)</li>
  </ul>
<li>Problem B (<a href="https://code.google.com/codejam/contest/2418487/dashboard#s=p1">Manage your Energy</a>):
  <ul>
    <li>Small Set: 2323/3789 users (61%)</li>
    <li>Large Set: 456/1133 users (40%)</li>
  </ul>
</li>
<li>Problem C (<a href="https://code.google.com/codejam/contest/2418487/dashboard#s=p2">Good Luck</a>):
  <ul>
    <li>Small Set: 1366/1774 users (77%)</li>
    <li>Large Set: 31/605 users (5%)</li>
  </ul>
</li>
</ul>

More information might soon be on <a href="http://www.go-hero.net/jam/13/">go-hero.net</a>.

I'm too slow for Google Code Jam *sigh*. Nevertheless, here are my solutions:

<h2>Bullseye</h2>
<h3>Small</h3>
```php
<?

function solve($r, $t) {
    $circles = 0;
    while($t >= 0) {
        $circles++;
        $t -= ($r+1)*($r+1)-$r*$r;
        $r += 2;
    }
    return floor($circles) - 1;
}

$fp = fopen ($argv[1], 'r');
$testcases = fgets ($fp);
$caseNr=0;
while($line = fgets ($fp)) {
    $caseNr++;
    $a = explode(' ', $line);
    $r = $a[0];
    $t = $a[1];
    echo "Case #$caseNr: ".solve($r, $t)."\n";

}
?>
```

<h3>Large</h3>
*Argh* I've copied the wrong equation from my pad to my computer 

You basically have to solve this:
$\begin{align}
t - \sum_{i=0}^x ((r+1+2i)^2 - (r+2i)^2) &\geq 0\\
\Leftrightarrow t - (x+1)(2x+2r+1) &\geq 0 \\
\Leftrightarrow (-2)x^2 + (2r+3)x + (t-2r-1) &\geq 0 \\
\Rightarrow x_{1,2} = 0 \Leftrightarrow x_{1,2} &= \frac{1}{-4} \cdot (-(2r+3) \pm \sqrt{(2r+3)^2-4(-2)(t-2r-1)}) \\
&= -\frac{1}{4} \cdot (-2r-3 \pm \sqrt{4r^2+12r+9+8(t-2r-1)})\\
&= -\frac{1}{4} \cdot (-2r-3 \pm \sqrt{4r^2+12r+9+8t-16r-8})\\
&= -\frac{1}{4} \cdot (-2r-3 \pm \sqrt{4r^2-4r+1+8t})\\
&= \frac{1}{4} \cdot (2r+3 \pm \sqrt{(2r-1)^2+8t})\\
&= \frac{1}{4} \cdot (2r+3 \pm \sqrt{(2r-1)^2+8t})\\
\end{align}
$

I have to know that $1 \leq r$ and $1 \geq x \in \mathbb{N}$. So you have to round $x_1, x_2$ to the nearest solution.

Did you know that Python has (in numpy) a method to calculate roots of a quadratic equation? See <a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.roots.html">numpy.roots</a> for reference.

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from numpy import ceil, roots
 
def check(r, t, x):
    return t-(x+1)*(2*r+2*x+1) >= 0
 
def solveFast(r, t):
    myRoots = roots((2,2*r+3,2*r+1-t))
    for i in xrange(2):
        if myRoots[i] >= 0:
            answer = int(ceil(myRoots[i])) + 1
            while not check(r, t, answer):
                answer -= 1
            return answer + 1
  
if __name__ == "__main__":
    testcases = input()
       
    for caseNr in xrange(1, testcases+1):
        line = raw_input()
        r, t = map(int, line.split(' '))
        print("Case #%i: %s" % (caseNr, solveFast(r, t)))

```

<h2>Good Luck</h2>
This one solves at least the first test case, but not the second one.

I love <a href="http://docs.python.org/2/library/itertools.html">itertools</a> ☺

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import factorial
from itertools import combinations_with_replacement
import pprint
from copy import deepcopy

def mul(integers):
    s = 1
    for p in integers:
        s *= p
    return s

def merge(candidates, block):
    newCandidates = deepcopy(candidates)
    for el in set(block):
        diff = block.count(el) - newCandidates.count(el)
        for i in xrange(diff):
            newCandidates.append(el)
    return newCandidates

def canBeIn(b, candidates, N):
    merged = merge(candidates, b)
    return not (len(merged) > N)

""" 
    N: number of numbers in total that got randomly picked
    M: A_i in [2, M]
"""
def solve(N, M, products, productToBuildungs):
    candidates = []

    # Is there a simple answer?
    for p in products:
        if productToBuildungs[p][0] == 1:
            candidates = merge(candidates, productToBuildungs[p][1][0])
            if len(candidates) == N:
                return candidates

    for p in products:
        pos = filter(lambda b: canBeIn(b, candidates, N), productToBuildungs[p][1])
        if len(pos) == 1:
            candidates = merge(candidates, pos[0])

    while len(candidates) < N:
        candidates.append(2)

    return candidates

if __name__ == "__main__":
    testcases = input()
      
    for caseNr in xrange(1, testcases+1):
        print("Case #%i:" % caseNr)
        line = raw_input()
        arr = line.split(' ')
        R = int(arr[0])
        N = int(arr[1])
        M = int(arr[2])
        K = int(arr[3])

        # which products can I get
        productToBuildungs = {}
        for r in xrange(0, N+1):
            for product in combinations_with_replacement(range(2,M+1),r):
                s = mul(product)
                if s not in productToBuildungs:
                    productToBuildungs[s] = [1, [list(product)]]
                else:
                    productToBuildungs[s][0] += 1
                    productToBuildungs[s][1].append(list(product))

        for r in xrange(R):
            products = [int(el) for el in raw_input().split(' ') if int(el) != 1]
            print(''.join(map(str, sorted(solve(N, M, products, productToBuildungs)))))

```
