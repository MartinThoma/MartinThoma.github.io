---
layout: post
title: Computer Science
slug: computer-science
lang: en
author: Martin Thoma
date: 2020-02-23 20:00
category: My bits and bytes
tags: Education, University, KIT
featured_image: logos/star.png
status: draft
---
I've written a lot of blog posts about Computer Science exams at KIT. I've also
written [Informatik am KIT](../informatik-am-kit/)
(Computer Science at KIT). This blog post is similar, but it focuses on key
ideas from computer science which I think every computer scientist should know
about. So instead of linking to exam preparation pages, I will link to
Wikipedia or other sources to learn the topic.


<figure class="ai-generated">
    <a href="../images/2020/05/computer-science.jpg"><img src="../images/2020/05/computer-science.jpg" alt="Laptop surrounded by computer science icons such as growth curves, binary tree, sorting bars, graph, Turing tape, database and padlock" width="1376" height="768"></a>
    <figcaption>Key ideas every computer scientist should know.</figcaption>
</figure>

## Theory

### Big-O Notation

[Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation) describes how the
runtime or memory of an algorithm grows with the size $n$ of the input,
ignoring constant factors. It answers "what happens if the input gets ten times
bigger?":

* $\mathcal{O}(1)$: constant, for example accessing an array element
* $\mathcal{O}(\log n)$: binary search in a sorted list
* $\mathcal{O}(n)$: one pass over the data
* $\mathcal{O}(n \log n)$: good sorting algorithms
* $\mathcal{O}(n^2)$: comparing every element with every other element
* $\mathcal{O}(2^n)$: trying every subset; hopeless beyond about 40 elements

Distinguish the worst case from the average case: quicksort is
$\mathcal{O}(n \log n)$ on average, but $\mathcal{O}(n^2)$ in the worst case.
The [Big-O cheat sheet](https://www.bigocheatsheet.com/) lists the complexities
of common data structures and algorithms.

### Computability and Complexity

* Some problems can't be solved by any program. The classic example is the
  [halting problem](https://en.wikipedia.org/wiki/Halting_problem): no program
  can decide for every program whether it terminates.
* [P vs NP](https://en.wikipedia.org/wiki/P_versus_NP_problem): for many problems
  a solution is easy to check, but nobody knows a fast way to find one (for
  example scheduling, packing, the traveling salesman problem). If a problem is
  NP-hard, look for heuristics or approximations instead of the perfect
  solution.


## DS and Algorithms

### Data Types

There are primitive data types and data structures which are built from those
primitive types.

<table class="table">
    <thead>
    <tr>
        <th>Type</th>
        <th>Size in C</th>
        <th>Value Range</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>char</td>
        <td>1 byte</td>
        <td>[-128, 127]<sup title="There is an unsigned variant as well">*</sup></td>
    </tr>
    <tr>
        <td>int</td>
        <td>4 bytes</td>
        <td>[-2147483648,&nbsp;+2147483647]<sup title="There is an unsigned variant as well">*</sup></td>
    </tr>
    <tr>
        <td>float</td>
        <td>4 bytes</td>
        <td>[1.2E-38, 3.4E+38]</td>
    </tr>
    <tr>
        <td>double</td>
        <td>8 bytes</td>
        <td>[2.3E-308, 1.7E+308]</td>
    </tr>
    <tr>
        <td>pointer</td>
        <td>8 bytes on 64 bit systems<sup title="4 bytes on 32 bit systems">*</sup></td>
        <td></td>
    </tr>
    </tbody>
</table>

The sizes are typical values on current desktop systems; the C standard only
guarantees minimums. The float ranges are the smallest and largest positive
normalized values.


### Data Structures

The choice of the data structure decides which operations are fast. The
questions are always: how fast can I access an element, search for one, insert
and delete?

#### Linear Data Structures

Linear Data Structures define an order over the elements. They can be divided
into direct access ones (arrays) and sequential access data structures:

* General: Lists (have a look at [mpu/datastructures](https://github.com/MartinThoma/mpu/tree/master/mpu/datastructures))
    * Array (Python's `list`): access by index in $\mathcal{O}(1)$, inserting at
      the front in $\mathcal{O}(n)$
    * Linked list: inserting in $\mathcal{O}(1)$ if you have the position,
      access by index in $\mathcal{O}(n)$
* LIFO: Stack
    * `push(1)`, `push(2)`, `push(3)`, `pop()` -> 3
* FIFO: Queue (in Python: `collections.deque`)
    * `push(1)`, `push(2)`, `push(3)`, `pop()` -> 1
* Bit-Array ([python](https://github.com/ilanschnell/bitarray))

#### Non-Linear Data Structures

* Dictionary / associative array / Maps: usually a hash table, access in
  $\mathcal{O}(1)$ on average (Python's `dict`)
* Sets: the same idea without values (Python's `set`)
* [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter): a probabilistic
  set. It answers "definitely not in the set" or "probably in the set" and needs
  only a few bits per element ([video](https://www.youtube.com/watch?v=x2sLjRK56YU),
  [details](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/))
* Graphs
    * Weighted
    * Acyclic
        * Trees
            * Binary Trees
* Heap / priority queue: the smallest element in $\mathcal{O}(1)$, insert and
  remove in $\mathcal{O}(\log n)$ (Python's `heapq`)
* Prefix-Tree (Trie): all words with a given prefix, for example for
  autocompletion
* Search Trees: sorted data with search, insert and delete in
  $\mathcal{O}(\log n)$
    * [Binary search trees](https://en.wikipedia.org/wiki/Binary_search_tree), kept
      balanced as red-black trees or AVL trees. Many standard libraries use them
      for sorted maps (C++ `std::map`, Java `TreeMap`). In Python,
      [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/) provides
      sorted lists and dicts.
    * [B-Tree](https://en.wikipedia.org/wiki/B-tree): the index structure of
      databases and file systems; many keys per node, so few disk accesses
* [H Tree](https://en.wikipedia.org/wiki/H_tree)
* [Rope](https://en.wikipedia.org/wiki/Rope_(data_structure)): a tree of strings
  that makes editing very long texts fast (text editors)


### String Algorithms

* [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm): Find first substring in $\mathcal{O}(n + m)$. In Python, simply do <code>index = text.index(pattern)</code>.
* Edit distance ([Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)):
  how many changes turn one string into another; a classic example of dynamic
  programming.
* Regular expressions and the finite automata behind them.


### Recursion and Dynamic Programming

* Tower of Hanoi
* [Can every recursion be converted into iteration?](https://stackoverflow.com/q/931762/562769)
  (Yes: with an explicit stack.)
* Dynamic programming: solve each subproblem once and store the result
  (memoization). It turns the exponential recursive Fibonacci into a linear one,
  and it is behind edit distance, shortest paths and the knapsack problem.

### Sorting

See [my German article about sorting algorithms](../ubersicht-uber-sortieralgorithmen/)
and the [algorithms overview on Wikiversity](https://en.wikiversity.org/wiki/Algorithms/Overview).

* Comparison-based sorting can't be faster than $\mathcal{O}(n \log n)$.
* Merge sort and heap sort guarantee $\mathcal{O}(n \log n)$; Python's built-in
  sort (Timsort, and Powersort since Python 3.11) is a merge sort that is very
  fast on partially sorted data.
* Binary search: find an element in a sorted list in $\mathcal{O}(\log n)$.

### Networks

* Graph Traversals
    * DFS: depth-first search, with a stack
    * BFS: breadth-first search, with a queue; finds shortest paths in
      unweighted graphs
    * A\*: like Dijkstra, but with a heuristic that guides the search towards
      the goal
* Dijkstra: single-source shortest path; store previous target node, previous node, distance: [video](https://www.youtube.com/watch?v=pVfj6mxhdMw). It stores the unvisited nodes as a min-priority queue by distance to start. It only works with non-negative edge weights.
* Ford-Fulkerson: maximum flow

## Standards

* IEEE 754: how computers store floating point numbers, and why
  `0.1 + 0.2 != 0.3`
    * [A practical approach to floats](../a-practical-approach-to-floats/)
    * David Goldberg: [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
* Unicode and UTF-8: text is not bytes
* [What every developer should know about time](https://zenodo.org/record/1443533)

## Communication

### Architecture

Some components:

* API: REST, GraphQL
* Databases:
    * Relational (MySQL, MariaDB, PostgreSQL)
    * Graph (Neo4j) - just that they exist
    * document-oriented (MongoDB) - just that they exist
* [Key-Value Stores](../key-value-stores/)
* Storage
* Caches and queues
* The [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem): a distributed
  system that is split by a network failure has to choose between consistency
  and availability.


## Machine Learning

* [medium.com/…/machine-learning-algorithm-overview-…](https://medium.com/ml-research-lab/machine-learning-algorithm-overview-5816a2e6303)


## Software Engineering

* How do teams organize? Scrum, Kanban? Meetings / ceremonies (daily, retro, planning, grooming)
* Version control with Git, code review, automated tests and continuous
  integration
