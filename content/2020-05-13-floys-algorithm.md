---
layout: post
title: Floyds Algorithm
slug: floyds-algorithm
author: Martin Thoma
status: draft
date: 2020-05-13 20:00
category: Code
tags: algorithm, Python, two-pointer algorithms, graph-algorithm, Competitive Programming
featured_image: logos/star.png
---
[Floys cycle-detection algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
uses two pointers. Those two pointers are sometimes called *tortoise* and
*hare*. The turtoise is slow and just moves one step at a time. The hare is
fast and moves two steps at a time.

```python
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_loop(linked_list_head: Node) -> Optional[Node]:
    slow = linked_list_head
    fast = linked_list_head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow  # Found loop and return starting point
```

This is pretty nice as it need $\mathcal{O}(1)$ additional space and has a
time-complexity of $\mathcal{O}(n)$.

You can also use this for various competitive coding tasks if you are given an
unsorted array of $n$ numbers where the values are guaranteed to be in 1 to
$n$.

## Duplicate Number finding

> Given is an array with n+1 numbers, each being in the range 1 to n.
> There is one number apparing multiple times (could be more than twice).
> Find that number

See [Leetcode 287](https://leetcode.com/problems/find-the-duplicate-number/solution/)

You can interpret the list of numbers as a linked list. The value is the pointer
to the same index.

For example, the list `[1, 2, 3, 4, 2]` represents the graph below:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2020/05/singly-linked-list.svg"><img src="../images/2020/05/singly-linked-list.svg" alt="Graph represented by the list [1,2,3,4,2]" style="width: 512px;"/></a>
    <figcaption class="text-center">Graph represented by the list [1,2,3,4,2]</figcaption>
</figure>

The number `2` is the duplicate here. With the following algorithm we can
find it in $\mathcal{O}(n)$ with $\mathcal{O}(1)$ additional space.

```python
from typing import List


def find_duplicate(nums: List[int]) -> int:
    slow = 0
    fast = 0
    n = len(nums)
    while slow != fast or slow == fast == 0:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast
```
