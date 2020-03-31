---
layout: post
title: Dynamic Programming
slug: dynamic-programming
author: Martin Thoma
date: 2020-03-30 20:00
category: Algorithms
tags: Code, Fibonacci, Python
featured_image: logos/python.png
---
Dynamic Programming is a technique to find the solution to a problem by
computing the solution of one or more sub-problems. So the problem needs to
have [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure).


## Memoization

It happens very often that you need to solve the same sub-problem multiple times.
Think of the Fibonacci sequence, where you might calculate

\begin{align}
f(7) &= f(6) + f(5)\\
&= f(5) + f(4) + f(5)\\
&= f(4) + f(3) + f(4) + f(4) + f(3)\\
&=\dots
\end{align}

In order to prevent this, you can memoize it. That means you store the
parameters of a function call and its result. Once you see these parameters
again, you can directly return the result without recalculating the function.

In Python, you can use the [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
decorator for that. See the Fibonacci example below for a concrete example.

TL;DR: Memoization is a technique to speed-up function calls by caching their
results.


## Terminology

I don't think the distinction here is important. It is important to understand
the concept: You can solve a big problem by solving smaller sub-problems and
combining the answers. This is not necessarily done by a recursive function
call, but could also happen by storing sub-problems in a dictionary and
iterating over a sequence of numbers.


### Backtracking

Both, Backtracking and Dynamic Programming, are used to solve discrete
constraint satisfaction problems (CSPs). I would call bottom-up approaches
*Dynamic Programming* and top-down approaches *Backtracking*


### Divide and Conquer

Divide and Conquer algorithms, such as [merge sort](https://en.wikipedia.org/wiki/Merge_sort),
Binary search,
and the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm),
also divide the original problem into smaller sub-problems.

The important point with divide and conquer is that the subproblems can be
solved independently.

For Dynamic Programming, two subproblems A and B might share a sub-subproblem C.


## Fibonacci Sequence

The Fibonacci sequence is defined as:

$$
f(n) := \begin{cases}
n               &\text{if } n \leq 1\\
f(n-1) + f(n-2) &\text{otherwise}
\end{cases}
$$

The inefficient, but straight-forward implementation is

```python
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)
```

The best solution to this one is:

```python
def f(n):
    """
    >>> f(0)
    0
    >>> f(1)
    1
    >>> f(2)
    1
    >>> f(3)
    2
    >>> f(5)
    5
    """
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
    return a
```

Have a look at [Fibonacci, recursion and decorators](https://martin-thoma.com/fibonacci-recursion-decorators/)
if you are interested in more details.


## Longest Increasing Subsequence

A sub-sequence of an sequence is any subset of a sequence in the same order.
Please note that a sub-sequence does not have to be contiguous.

For this example, I want a strictly increasing subsequence.

The brute-force solution is to generate all sub-sequences and check if they are
increasing. The generate-and-check pattern is in $\mathcal{O}(2^n)$. It is easy
to implement with Python:

```python
from itertools import chain, combinations


def longest_increasing_subsequence(numbers):
    lis = max(
        (len(subseq), subseq) for subseq in powerset(numbers) if is_increasing(subseq)
    )
    return lis[1]


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def is_increasing(sequence):
    return all(e1 < e2 for e1, e2 in zip(sequence, sequence[1:]))
```

The following Dynamic Programming approach takes $\mathcal{O}(n^2)$ in time
and additionally $\mathcal{O}(n)$ space.

```python
from typing import List


def longest_increasing_subsequence(numbers: List[int]) -> int:
    """
    >>> longest_increasing_subsequence([])
    0
    >>> longest_increasing_subsequence([4321])
    1
    >>> longest_increasing_subsequence([1,2,3,4,5])
    5
    >>> longest_increasing_subsequence([1,2,3,4,5,5])
    5
    >>> longest_increasing_subsequence([5,4,3,2,1])
    1
    >>> longest_increasing_subsequence([1,7,2,3,4])
    4
    """
    if len(numbers) <= 1:
        return len(numbers)

    # For each index, calculate the longest subsequence which ends with that index
    max_endswith = [1]  # include the index
    for i in range(1, len(numbers)):
        max_len_before = 0
        for j in range(0, i):
            if numbers[j] < numbers[i]:
                max_len_before = max(max_len_before, max_endswith[j])
        max_endswith.append(max_len_before + 1)
    return max(max_endswith)
```

Using [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting) is
a $\mathcal{O}(n \log(n))$ solution with additional $\mathcal{O}(n)$ space ([video](https://www.youtube.com/watch?v=22s1xxRvy28)).


## Edit Distance

The edit distance, also known as [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance),
calculates the number of operations two words are apart. Typically, one allows
removal of characters, adding characters or changing a character. And typically,
all of them have a count of 1.

A real-world application of the edit distance is in automatic speech recognition (ASR).
There the edit distance is used to calcuate the word error rate (WER): [Word Error Rate Calculation](https://martin-thoma.com/word-error-rate-calculation/)


\begin{align}
m &:= |w_1|\\
n &:= |w_2|\\
\end{align}

We want to compute a distance matrix $d \in \mathbb{N}_0^{m \times n}$:

\begin{align}
D_{0, 0} &= 0\\
D_{i, 0} &= i, \text{ for } 1 \leq i \leq m\\
D_{0, j} &= j, \text{ for } 1 \leq j \leq n
\end{align}

$$
\text{For } 1 \leq i\leq m, 1\leq j \leq n\\
D_{i, j} = \min \begin{cases}
D_{i - 1, j - 1}&+ 0 \ {\rm if}\ u_i = v_j\\
D_{i - 1, j - 1}&+ 1 \ {\rm(Replacement)} \\
D_{i, j - 1}&+ 1 \ {\rm(Insertion)} \\
D_{i - 1, j}&+ 1 \ {\rm(Deletion)}
\end{cases}
$$

Each cell $(i, j)$ of the matrix $D$ is a sub-problem of the original one:

```python
edit_distance(w1[: i + 1], w2[: j + 1]) = d[i][j]
```

The complete code looks as follows:

```python
def edit_distance(w1: str, w2: str) -> int:
    """
    >>> edit_distance("foobar", "")
    6
    >>> edit_distance("", "")
    0
    >>> edit_distance("foobar", "foobar")
    0
    >>> edit_distance("fobar", "foobar")
    1
    >>> edit_distance("foobar", "fobar")
    1
    >>> edit_distance("stackoverflow", "stackingoverflow")
    3
    >>> edit_distance("overflow", "stack")
    8
    >>> edit_distance("stack", "overflow")
    8
    """
    m = len(w1)
    n = len(w2)

    # Initialize
    d = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            if i == 0:
                el = j
            elif j == 0:
                el = i
            else:
                el = 0
            row.append(el)
        d.append(row)

    # Compute
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                options = [d[i - 1][j - 1] + 1, d[i][j - 1] + 1, d[i - 1][j] + 1]
                d[i][j] = min(options)
    return d[m][n]
```

A 16 minute video explanation is given by [Back To Back SWE](https://www.youtube.com/watch?v=MiqoA-yF-0M).


## Change Making Problem

Imagine your are the cashier at a supermarket. You have to give change to the
customer and you want to give the least number of coins possible.

There is a top-down and a bottom-up solution.

A recursive top-down solution is:

```python
from typing import Set, Optional
from functools import lru_cache


@lru_cache(maxsize=512)
def least_coins(coins: Set[int], amount: 11) -> Optional[int]:
    """
    >>> least_coins(frozenset({2,5,10,20,50,100}), 1)
    >>> least_coins(frozenset({1,2,5,10,20,50,100}), 0)
    0
    >>> least_coins(frozenset({1,2,5,10,20,50,100}), 3)
    2
    >>> least_coins(frozenset({1,2,5,10,20,50,100}), 4)
    2
    >>> least_coins(frozenset({1,2,5,10,20,50,100}), 8)
    3
    >>> least_coins(frozenset({1,2,5,10,20,50,100}), 18)
    4
    """
    if amount == 0:
        return 0
    if amount in coins:
        return 1
    possible_solutions = []
    for coin in coins:
        if coin < amount:
            solution = least_coins(coins, amount - coin)
            if solution is not None:
                possible_solutions.append(solution + 1)
    return min(possible_solutions, default=None)
```

Note that I used an LRU cache. This saves the 512 **l**east **r**ecently
**u**sed function calls and its output. So we don't have to re-compute too
much. That decorator requires hashable parameters, hence we have to use
frozenset. Set is not hashable.

Now the top-down iterative solution:

```python
from typing import Set, Optional


def least_coins(coins: Set[int], amount: 11) -> Optional[int]:
    """
    >>> least_coins({2,5,10,20,50,100}, 1)
    >>> least_coins({1,2,5,10,20,50,100}, 0)
    0
    >>> least_coins({1,2,5,10,20,50,100}, 3)
    2
    >>> least_coins({1,2,5,10,20,50,100}, 4)
    2
    >>> least_coins({1,2,5,10,20,50,100}, 8)
    3
    >>> least_coins({1,2,5,10,20,50,100}, 18)
    4
    """
    if amount == 0:
        return 0
    if amount in coins:
        return 1
    assert amount >= 0
    assert all(coin > 0 for coin in coins)
    # coins_used, remaining_amount
    partial_solutions = [(0, amount)]
    possible_solutions = []
    while partial_solutions:
        coins_used, remaining_amount = partial_solutions.pop()
        if remaining_amount == 0:
            possible_solutions.append(coins_used)
            continue
        for coin in coins:
            if coin <= remaining_amount:
                partial_solution = (coins_used + 1, remaining_amount - coin)
                partial_solutions.append(partial_solution)
    return min(possible_solutions, default=None)
```

I removed the LRU cache and used normal sets. I could have kept both, but
this makes the solution a bit shorter.

The bottom-up solution would calculate all the possible sums. Although that
would be the dynamic programming solution, I'm currently to lazy to write it
(aka: I leave it as an exercise to the reader).


## See also

* [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm): finding shortest paths in a weighted graph
* Karpathy: [GridWorld: Dynamic Programming Demo](https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html)
* StackOverflow: [Difference between back tracking and dynamic programming](https://stackoverflow.com/q/3592943/562769)
* 🇩🇪 Martin Thoma: [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/#dynamic-programming)
