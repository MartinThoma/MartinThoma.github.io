---
layout: post
title: Computer Science
slug: computer-science
author: Martin Thoma
status: draft
date: 2020-02-23 20:00
category: My bits and bytes
tags: study, education
featured_image: logos/star.png
---
I've written a lot of blog posts about Computer Science exams at KIT. I've also
written [Informatik am KIT](https://martin-thoma.com/informatik-am-kit/)
(Computer Science at KIT). This blog post is similar, but it focuses on key
ideas from computer science which I think every computer scientist should know
about. So instead of linking to exam preparation pages, I will link to
Wikipedia or other sources to learn the topic.


## Theory

### Big-O Notation

## DS and Algorithms

### Data Types

There are primite data types and data structures which are built from those
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
        <td>[-32767,&nbsp;+32767]<sup title="There is an unsigned variant as well">*</sup></td>
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


### Data Structures

#### Linear Data Structures

Linear Data Structures define an order over the elements. They can be divided
into direct access ones (arrays) and sequential access data structures:

* General: Lists (have a look at [mpu/datastructures](https://github.com/MartinThoma/mpu/tree/master/mpu/datastructures))
* LIFO: Stack
    * `push(1)`, `push(2)`, `push(3)`, `pop()` -> 3
* FIFO: Queue
    * `push(1)`, `push(2)`, `push(3)`, `pop()` -> 1
* Bit-Array ([python](https://github.com/ilanschnell/bitarray))

#### Non-Linear Data Structures

* Sets: Bloom filters ([video](https://www.youtube.com/watch?v=x2sLjRK56YU), [details](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/), [Python](https://github.com/hiway/python-bloom-filter))
* Graphs
    * Weighted
    * Acyclic
        * Trees
            * Binary Trees
* Dictionary / associative array / Maps
* [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter): (Python: [dablooms](https://github.com/bitly/dablooms) and [pybloomfiltermmap](https://github.com/axiak/pybloomfiltermmap))
* Prefix-Tree (Trie)
* Search Trees
    * [Binary search trees](https://en.wikipedia.org/wiki/Binary_search_tree): Aparently, they are used within databases, huffman coding, and the implementation of dictionaries
        * Red-black tree ([Python](https://pypi.org/project/rbtree/))
        * AVL Tree ([Python](https://pypi.org/project/pyavl/))
    * [B-Tree](https://en.wikipedia.org/wiki/B-tree)
* [H Tree](https://en.wikipedia.org/wiki/H_tree)
* [Rope](https://en.wikipedia.org/wiki/Rope_(data_structure)) ([python](https://github.com/DanielStutzbach/blist))


access / write /

* https://www.cseworldonline.com/data-structure/Introduction-Data-Structures.php


### String Algorithms

* [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm): Find first substring. In Python, simply do <code>index = text.index(pattern)</code>.


### Recursion and Dynamic Programming

* Tower of Hanoi
* [Can every recursion be converted into iteration?](https://stackoverflow.com/q/931762/562769)

### Sorting

See [my Germany article about roting algorithms](https://martin-thoma.com/ubersicht-uber-sortieralgorithmen/)

⇒ Link article: https://en.wikiversity.org/wiki/Algorithms/Overview



* Binary search

### Networks


* Graph Traversals
    * DFS
    * BFS
    * A\*
* Dijkstra: single-source shortest path; store previous target node, previous node, distance: [video](https://www.youtube.com/watch?v=pVfj6mxhdMw). It stores the unvisted nodes as a min-priority queue by distance to start
* Ford-Fulkerson: maximum flow

## Standards

* IEEE 754:
    * [A practical approach to floats](https://martin-thoma.com/a-practical-approach-to-floats/)
    * [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)
* [What every developer should know about time](https://zenodo.org/record/1443533#.XlIz6HVKgdg)

## Communication

### Pseudo-Code

TODO

### Architecture

Some components:

* API: REST, GraphQL
* Databases:
    * Relational (MySQL, MariaDB, PostgreSQL)
    * Graph (Neo4j) - just that they exist
    * document-oriented (MongoDB) - just that they exist
* [Key-Value Stores](https://martin-thoma.com/key-value-stores/)
* Storage



## Machine Learning

* https://medium.com/ml-research-lab/machine-learning-algorithm-overview-5816a2e6303


## Marvin

* TODO

## Questions

* How do teams organize? Scrum, Kanban? Meetings / ceremonies (daily, retro, planning, grooming)
