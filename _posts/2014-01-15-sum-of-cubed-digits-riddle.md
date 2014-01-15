---
layout: post
title: Sum of cubed digits riddle
author: Martin Thoma
date: 2014-01-04 14:53
categories:
- Code
tags:
- Python
- mathematics
featured_image: 2014/01/math-riddle-thumb.png
---

Let $N \in \mathbb{N}$ be a number with digits $a_k$, where $a_0$ is the least
significant digit and $n$ is the most significant digit.

Find all numbers with the following property:

$$N = \sum_{k=0}^n a_k \cdot 10^k = \sum a_k^3$$

I call this "*-property".

Lower and upper bounds
======================
* The lower bound is 0
* The upper bound is $2916$ since $4\cdot 9^3 = 2916$

You can find better upper bounds, but as we've just reduced the 
possible number space to only 2917 numbers, it doesn't really matter

Find all solutions
==================

```python
#!/usr/bin/env python3

def find_sum_of_cubes():
    """Returns all numbers N with the following property
        N = \sum_{k=0}^n a_k \cdot 10^k = \sum a_k^3
    """
    def sum_of_cubes_check(n):
        digits = map(int, list(str(n)))
        s = sum(map(lambda n: n**3, digits))
        return s == n

    i=0
    return list(filter(sum_of_cubes_check, range(2917)))

if __name__ == "__main__":
    print(find_sum_of_cubes())
```

which gives

```bash
[0, 1, 153, 370, 371, 407]
```
