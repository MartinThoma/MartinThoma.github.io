---
layout: post
title: A fast solution for Range Minimum Query
author: Martin Thoma
date: 2012-05-22 11:48:43
categories:
- Code
tags:
- C
- ICPC
- TopCoder
featured_image: 2012/05/icpc-logo.png
---
A Range Minumum Query is a query for the minimum in a specified range.

Suppose you have the following set of numbers:
<table>
<tr>
<th>Indices</th>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
</tr>
<tr>
<th>Values</th>
<td>4</td>
<td>7</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>8</td>
<td>6</td>
<td>7</td>
<td>5</td>
</tr>
</table>

Now you get some queries, that ask for the minimum between two Indices i and j:
<table>
<tr>
<th>Query</th>
<th>Result</th>
<th>Query</th>
<th>Result</th>
</tr>
<tr>
<td>(1,5)</td>
<td>1</td>
<td>(5,5)</td>
<td>2</td>
</tr>
<tr>
<td>(2,4)</td>
<td>1</td>
<td>(5,8)</td>
<td>2</td>
</tr>
<tr>
<td>(6,8)</td>
<td>6</td>
<td>(7,9)</td>
<td>5</td>
</tr>
<tr>
<td colspan="2">many more</td>
</tr>
</table>

## Linear search
The easiest solution for this task is to go through all elements. This will
need a linear amount of time for each query. This is much to slow if you get
many queries.

## Building blocks
One possibility to make this one faster is to build blocks:
<table>
<tr>
<th>Indices</th>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
</tr>
<tr>
<th>Values</th>
<td>4</td>
<td>7</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>8</td>
<td>6</td>
<td>7</td>
<td>5</td>
</tr>
<th>Block</th>
<td colspan="2"> Block 1</td>
<td colspan="2"> Block 2</td>
<td colspan="2"> Block 3</td>
<td colspan="2"> Block 4</td>
<td colspan="2"> Block 5</td>
</tr>
</table>

## Two dimensional
If you don't have a one-dimensional array with numbers but a two-dimensional, you have to adjust your algorithms. I did some testing today. I took a small input set (1000 x 1000 numbers, 100.000 queries - file size of this set is 11.5 MB), a large set (1000 x 1000 numbers, 1.000.000 queries - file size of this set is 25.0 MB) and a huge one (1000 x 1000 numbers, 100.000.000 queries).

### Linear search
Small input set: real 0m30.390s
Large input set: 5m6.754s
Huge input set: aborted after two hours

### Building blocks
Small input set: real 0m30.298s
Large input set: real 1m8.186s
Huge input set: 107m56.560s = 1 hour 48 minutes

### Apply Sparse Tables Algorithm by rows
Small input set:
Large input set:
Huge input set:


## See also

* Wikipedia: [Range searching](http://en.wikipedia.org/wiki/Range_searching),
  [Range Minimum Query](http://en.wikipedia.org/wiki/Range_Minimum_Query)
* TopCoder article: <a href="http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=lowestCommonAncestor#Range_Minimum_Query_%28RMQ%29">Range Minimum Query and Lowest Common Ancestor</a>
* <a href="http://en.wikipedia.org/wiki/University_of_T%C3%BCbingen">University of Tübingen</a>: <a href="http://ab.inf.uni-tuebingen.de/people/fischer/amir07two.pdf">Two-Dimensional Range Minimum Queries</a>, a <a href="http://www.cs.ucr.edu/~stelo/cpm/cpm07/2D_range_queries_amir.pdf">very short presentation</a>
* <a href="http://en.wikipedia.org/wiki/Aarhus_University">Aarhus University</a>: <a href="http://www.cs.au.dk/~gerth/papers/algorithmica12min.pdf">On Space Efﬁcient Two Dimensional Range Minimum Data Structures</a>
