---
layout: post
title: Dynamic Programming
slug: dynamic-programming
author: Martin Thoma
date: 2020-03-31 20:00
category: Algorithms
tags: Algorithms, Code, Fibonacci, Python, COP, CSP
featured_image: logos/ai.png
---
Dynamic Programming is a technique to find the solution to a problem by
computing the solution of one or more sub-problems. So the problem needs to
have [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure).

If you compute the solution bottom-up, then it is Dynamic Programming. If you
compute it top-down, then you might use memoization.

## Terminology

I don't think the distinction here is important. It is important to understand
the concept: You can solve a big problem by solving smaller sub-problems and
combining the answers. This is not necessarily done by a recursive function
call, but could also happen by storing sub-problems in a dictionary and
iterating over a sequence of numbers.

### Memoization

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

### Backtracking

Both, Backtracking and Dynamic Programming, are used to solve discrete
constraint problems. Dynamic Programming typically solves constraint
optimization problems (COPs) and backtracking constraint satisfaction problems
(CSPs).

Usually *Dynamic Programming* is bottom-up and *Backtracking* uses top-down approaches.


### Divide and Conquer

Divide and Conquer algorithms, such as [merge sort](https://en.wikipedia.org/wiki/Merge_sort), [quicksort](https://en.wikipedia.org/wiki/Quicksort),
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

The best solution to this is the following dynamic programming solution:

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


## 0/1 Knapsack

You have a list of items which have a weight and a value. You have a maximum
weight you can carry. What is the maximum value you can get?

```python
from typing import List, Tuple


def solve_knapsack(items: List[Tuple[int, int]], max_weight: int) -> int:
    """
    The items have (weight, value) as order

    >>> items = [(2, 2), (5, 7), (4, 3)]
    >>> solve_knapsack(items, max_weight=10)
    10
    >>> solve_knapsack(items, max_weight=11)
    12
    """
    # A non-positive weight is a no-brainer: we would always add it
    assert all(weight > 0 for weight, value in items)

    # ... except if the value is negtive
    assert all(value >= 0 for weight, value in items)

    # c[i][j] is the optimal solution if you have
    # a maximum weight of j and only the items items[:(i+1)]
    c = [[0 for weight in range(max_weight + 1)] for item in range(len(items))]
    for item_index in range(len(items)):
        for remaining_weight in range(max_weight + 1):
            # Can the item at item_index be added?
            item = items[item_index]
            not_adding = c[item_index - 1][remaining_weight]
            if item[0] > remaining_weight:
                # This works even for item_index = 0 as the matrix is
                # initialized with zeroes. Hence looking at the last element is
                # zero.
                c[item_index][remaining_weight] = not_adding
            else:
                # Yes we can!
                adding_it = item[1] + c[item_index - 1][remaining_weight - item[0]]
                c[item_index][remaining_weight] = max(not_adding, adding_it)
    return c[len(items) - 1][max_weight]
```

You can see that the solution has a time complexity of $\mathcal{O}(n \cdot m)$
where $n$ is the number of items and $m$ is the maximum weight. It also has this
space complexity.

You can also see that this solution would fail if <code>max_weight</code> was
not an integer. While one could simply multiply everything with large enough
numbers, this might make


### Climbing Stairs

There are n stairs and you can take either one or two stairs. How many unique
ways exist to climb the stairs?

First, a recursive solution:

```python
from functools import lru_cache


@lru_cache(maxsize=512)
def stairs(n: int) -> int:
    """
    >>> stairs(1)
    1
    >>> stairs(2)
    2
    >>> stairs(3)
    3
    >>> stairs(4)
    5
    """
    assert n >= 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n - 2) + stairs(n - 1)
```

You should directly notice that this looks VERY similar to the fibonacci sequence.
Only the starting numbers are different. Hence the solution is the same, except
for the starting numbers:

```python
def stairs(n: int) -> int:
    """
    >>> stairs(1)
    1
    >>> stairs(2)
    2
    >>> stairs(3)
    3
    >>> stairs(4)
    5
    """
    assert n >= 1
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

## Egg Drop

Given $n$ eggs and $m$ floors, how often do you need to let an egg drop to know
for sure the highest floor at which the eggs still don't break?

Some clarifications:

* Floors start at zero.
* The eggs are guaranteed not to break at floor 0.
* The eggs are guaranteed to break from floor $m +1$.
* If an egg does not break at floor $i$, it will not break at floor $i-1$.
* If an egg breaks at floor $i$, it will also break at floor $i+1$.

I know this sounds very simple and a was about to just drop the problem. I
thought it was simply binary search, hence with applying the logarithm you
could solve it. I was wrong, though. Think about the situation where you have
20 floors and 2 eggs. If you use the first egg for the 10th floor, the worst case
is that the searched floor is the 9th one:

* 1st egg breaks at 10th floor
* 2nd egg needs to be dropped from floor 1, 2, 3, 4, 5, 6, 7, 8, 9

Hence binary search needs 10 egg drops for 2 eggs and 20 floors

Now consider this:

* 1st egg is dropped from 7th floor
    * It breaks: 2nd egg needs to be dropped from floor 1,2,3,4,5,6 => 7 egg drops
    * It doesn't break: 1st egg is dropped from floor 14
        * It breaks: 2nd egg needs to be dropped from floor 8, 9, 10, 11, 12, 13 => 8 egg drops
        * It doesn't break: Try floor 15, 16, 17, 18, 19 => 7 egg drops

Obviously, binary search is not the best solution.

```python
def egg_drop(eggs: int, floors: int) -> int:
    """
    >>> egg_drop(42, 0)
    0
    >>> egg_drop(42, 1)
    1
    >>> egg_drop(1, 5)
    5
    >>> egg_drop(2, 100)
    14
    """
    s = []  # s[remaining_floors][remaining_eggs]
    for floor in range(floors + 1):
        row = []
        for reduced_eggs in range(eggs + 1):
            if floor <= 1:
                el = floor
            elif reduced_eggs == 0:
                el = None
            elif reduced_eggs == 1:
                el = floor
            else:
                el = None
            row.append(el)
        s.append(row)

    for floor in range(2, floors + 1):
        for n_egg in range(2, eggs + 1):
            # The number of eggs we need here at least, if we throw the egg
            # from the optimal floor. Throwing it in a conservative way
            # would mean we start in the lowest floor and go upwards. That is
            # always possible.
            best_choice = floors
            for chosen_floor in range(1, floor + 1):
                breaks = 1 + s[chosen_floor - 1][n_egg - 1]
                no_break = 1 + s[floor - chosen_floor][n_egg]
                worst_case = max(breaks, no_break)
                if worst_case < best_choice:
                    # This reads weird ... we just found a better choice where
                    # to throw eggs from
                    best_choice = worst_case
            s[floor][n_egg] = best_choice
    return s[floors][eggs]
```

This algorithm has a time complexity of $\mathcal{O}(m^2 \cdot n)$ and need
$\mathcal{O}(n \cdot m)$ in additional space. You can improve the runtime by
looking at the sequence of worst_case. It should go down and then up again. If
you notice that it went down but starts to go up again, you can abort the
<code>chosen_floor</code> loop. I don't think that changes the worst-case
asymptotical runtime, though.

Now that we have a solution which is correct, we can look for patterns in the
pure numbers:

* 2 eggs, starting with 0 floors: 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, ...: [A123578](https://oeis.org/A123578) - 1 times one, 2 times two, 3 times three, ...
* 3 eggs, starting with 0 floors: 0, 1, 2x 2, 4x 3, 7x 4, 11x 5, 16x 6

Another observation is that if we have enough eggs, we can perform binary
search and more eggs will not result in less egg drops.


## See also

* Wikipedia: Some example for Dynamic Programming algorithms
    * [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm): single-source shortest path (SSSP)
    * [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm): single-source shortest-path algorithm (SSSP), $\mathcal{O}(V^2 E)$
    * [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm): all-pairs shortest path algorithm, $\mathcal{O}(V^3)$
    * [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem)
* Karpathy: [GridWorld: Dynamic Programming Demo](https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html)
* StackOverflow:
    * [Difference between back tracking and dynamic programming](https://stackoverflow.com/q/3592943/562769)
    * [What is the difference between dynamic programming and branch and bound?](https://stackoverflow.com/q/16814830/562769)
* 🇩🇪 Martin Thoma: [Probabilistische Planung](https://martin-thoma.com/probabilistische-planung/#dynamic-programming)
