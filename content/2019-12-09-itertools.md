---
layout: post
title: Python Itertools
slug: itertools
author: Martin Thoma
date: 2019-12-09 20:00
category: Code
tags: Python, itertools
featured_image: logos/python.png
---
[Itertools](https://docs.python.org/3/library/itertools.html) is a tiny Python
module with limited functionality. But when you can use it, it is awesome. I
need to look up the names quite often. Recently, I found an
[explanation by Ben Blank](https://stackoverflow.com/a/942551/562769) which is
simply beautiful.


## product

[`product(*iterables, repeat=1)`](https://docs.python.org/3/library/itertools.html#itertools.product) creates the cross product of two iterables. The length of the result is
the product of the length of all iterables.

```python
import itertools

list(itertools.product([1, 2, 3], ["A", "B"]))
```

results in

```python
[(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
```

**Ben Blanks Explanation**:

```python
import itertools

list(itertools.product([1, 2, 3, 4], [1, 2, 3, 4]))
```

results in

```text
1,1  1,2  1,3  1,4
2,1  2,2  2,3  2,4
3,1  3,2  3,3  3,4
4,1  4,2  4,3  4,4
```


## permutations

[`permutations(iterable, r=None)`](https://docs.python.org/3/library/itertools.html#itertools.permutations)
generates all unique orderings of unique elements. If `r` is not specified, all
all are taken. In an [urn model](https://en.wikipedia.org/wiki/Urn_problem),
this means taking `r` balls without replacement.


**Ben Blanks Explanation**:

```python
import itertools

list(itertools.permutations([1, 2, 3, 4], r=2))
```

results in

```text
 .   1,2  1,3  1,4
2,1   .   2,3  2,4
3,1  3,2   .   3,4
4,1  4,2  4,3   .
```


## combinations

[`combinations(iterable, r)`](https://docs.python.org/3/library/itertools.html#itertools.combinations)
generates each unique pair of elements in lexicographical order.

**Ben Blanks Explanation**:

```python
import itertools

list(itertools.combinations([1, 2, 3, 4], r=2))
```

results in

```text
 .   1,2  1,3  1,4
 .    .   2,3  2,4
 .    .    .   3,4
 .    .    .    .
```


## combinations_with_replacement

[`combinations_with_replacement(iterable, r)`](https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement)
is identical to combinations, except that one has duplicate elements.

```python
from itertools import combinations_with_replacement

list(combinations_with_replacement([1, 2, 3, 4], r=2))
```

results in

```text
 1,1  1,2  1,3  1,4
  .   2,2  2,3  2,4
  .    .   3,3  3,4
  .    .    .   4,4
```