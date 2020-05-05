---
layout: post
title: Maximum Contiguous Subarray Sum
slug: maximum-subarray-sum
author: Martin Thoma
date: 2020-05-03 20:00
category: Code
tags: Competitive Programming, Brute-Force, Dynamic Programming
featured_image: logos/python.png
---
The maximum contiguous subarray sum problem is one of the classics. Given an
1D array of numbers $a_1, \dots, a_n$ with $a_i \in \mathbb{R}$, find $s$ such that:

$$\exists l, r \in [1, \dots, n]: \forall p, q \in [1, \dots, n]: \sum_{i=p}^q \leq \sum_{i=l}^r a_i = s$$

In other words: Find the sum of the biggest continguous subarray.

## Edge Cases

To make the rest a bit simpler, I will only use integers. It is also guaranteed
that there is at least one element in the list.


## Examples

For any array without negative numbers, the sum of the whole array would be the
solution.

```python-repl
>>> max_contiguous_subarray_sum([11, -5, -5, -2, 1, 2, 3, 4, 5, 0, 1])
15

>>> max_contiguous_subarray_sum([9, -5, -5, -2, 1, 2, -1, 4, 5, 0, 1])
11

>>> max_contiguous_subarray_sum([-1, -2, -3, -4, -5])
-1

>>> max_contiguous_subarray_sum([-2])
-2

>>> max_contiguous_subarray_sum([3])
3
```


## Brute-Force

I like simple brute force solutions to make sure that more complex solutions
are correct:

```python
from typing import List
from itertools import accumulate


def max_contiguous_subarray_sum(nums: List[int]) -> int:
    max_sum = nums[0]
    for right in range(len(nums)):
        for left in range(right):
            sum_ = sum(nums[left : right + 1])
            max_sum = max(max_sum, sum_)
    return max_sum
```

Complexity analysis:

* Time Complexity: $\mathcal{O}(n^3)$
* Space Complexity: $\mathcal{O}(n)$

You might wonder why this has a time complexity of $\mathcal{O}(n^3)$, although
there are only two loops. The answer is simply the `sum` function.

You might also wonder if the fact that the inner loop does not do $n$
operations but only $\text{right}$ operations makes any difference. In this
case let's calculate the exact number of tumes we calculate `sum_`:

* right=0: 0x sum_ calculations
* right=1: 1x sum_ calculations
* right=2: 2x sum_ calculations
* ...
* right=n-1: (n-1)x sum_ calculations

Hence we calculate `sum_` exactly
$$\sum_{1}^{n-1} = \frac{(n-1)^2 + (n-1)}{2} = \frac{n^2 - n}{2}$$
times.

The amount of elements should also be considered:

* right=0: 0x sum_ calculations, sum-elements: up to 0
* right=1: 1x sum_ calculations, sum-elements: up to 1
* right=2: 2x sum_ calculations, sum-elements: up to 2
* ...
* right=n-1: (n-1)x sum_ calculations, sum-elements: up to (n-1)

Hence the `sum()` function needs to do

\begin{align}
\sum_{i=1}^n (\sum_{j=1}^i j) &= \sum_{i=1}^n \frac{i^2 + i}{2}\\
&= \frac{1}{2} \cdot \sum_{i=1}^n (i^2 + i) \\
&= \frac{1}{2} \cdot (\sum_{i=1}^n i + \sum_{i=1}^n i^2)) \\
&= \frac{1}{2} \frac{n^2 + n}{2} + \frac{1}{2} \cdot \frac{n \cdot (n + 1) \cdot (2n + 1)}{6}\\
\end{align}

Which means it's a time complexity of $\mathcal{O}(n^3)$.


## Cummulative Sum Brute-Force

There is a pretty neat trick using the cummulative sum to prevent one of those
loops

```python
from typing import List
from itertools import accumulate


def max_contiguous_subarray_sum(nums: List[int]) -> int:
    max_sum = nums[0]
    cumsum = [0] + list(accumulate(nums))
    for right in range(1, len(cumsum)):
        for left in range(right):
            sum_ = cumsum[right] - cumsum[left]
            max_sum = max(max_sum, sum_)
    return max_sum
```

Complexity analysis:

* Time Complexity: $\mathcal{O}(n^2)$
* Space Complexity: $\mathcal{O}(n)$

## Kadane's Algorithm

```python
from typing import List


def max_contiguous_subarray_sum(nums: List[int]) -> int:
    max_sum = float("-inf")
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

Complexity analysis:

* Time Complexity: $\mathcal{O}(n)$
* Space Complexity: $\mathcal{O}(1)$

There cannot be any asymptotically better solution. For space complexity, it
is obvious. For time complexity one can see that one needs to look at least
at each element.


## Things to Learn

* [Gauss Summation formula](https://hsm.stackexchange.com/q/384)
* [Prefix-sum](https://en.wikipedia.org/wiki/Prefix_sum) technique
* Sliding Window technique ([Dynamic Programming](https://martin-thoma.com/dynamic-programming/))


## See also

* Wikipedia: [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
* Geeks For Geeks: [Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
* [Leetcode 53](https://leetcode.com/problems/maximum-subarray/)
