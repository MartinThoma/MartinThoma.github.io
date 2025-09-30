---
layout: post
title: n Queens Problem
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
featured_image: logos/sublime-text.png
---

The $n$ queens problem is a very famous combinatorical problem: On a $n \times n$
board, find a configuration of $n$ queens such that no queen can capture another
queen.

## Idea 1

```python
#!/usr/bin/env python


def add_queen(queen_positions, size):
    """ Add a queen to a list of queens in such a way that no queen can capture
        another queen.
    @param queen_positions - a list of integers. The index is the y-position
                             of the queen and the value the x-position.
    @param size            - positive integer; the size of the square board
    @return a new list of queens or -1 if no queen could be added
    """
    candidates = set(list(range(size))) - set(map(lambda n: n[0], queen_positions))
    new_qeen_y = len(queen_positions)
    # Remove diagonal ones
    for queen_y, queen_x in enumerate(queen_positions):
        queen_x = queen_x[0]
        difference = new_qeen_y - queen_y
        if queen_x + difference in candidates:
            candidates.remove(queen_x + difference)
        if queen_x - difference in candidates:
            candidates.remove(queen_x - difference)
    if len(candidates) > 0:
        take = candidates.pop()
        queen_positions.append((take, candidates))
        return queen_positions
    else:
        return -1


def backtrack(queen_positions):
    """Get the next possible configuration of queens. """
    last_pos = queen_positions[-1]
    if len(last_pos[1]) == 0:
        queen_positions = backtrack(queen_positions[:-1])
    else:
        take = last_pos[1].pop()
        queen_positions[-1] = (take, last_pos[1])
    return queen_positions


def solve(n):
    """Get a board of queens of size n x n where no queen captures another
       queen.
    """
    queen_positions = []
    while len(queen_positions) != n:
        returnval = add_queen(queen_positions, n)
        if returnval == -1:
            queen_positions = backtrack(queen_positions)
    return queen_positions


if __name__ == "__main__":
    n = 22
    solution = solve(n)
    for y, x_meta in enumerate(solution):
        x = x_meta[0]
        print("o" * (x) + "#" + "o" * (n - x - 1))
```

```bash
#ooooooooooooooooooooo
oo#ooooooooooooooooooo
oooo#ooooooooooooooooo
o#oooooooooooooooooooo
ooo#oooooooooooooooooo
ooooooooo#oooooooooooo
ooooooooooooo#oooooooo
oooooooooooooooo#ooooo
ooooooooooooooooooo#oo
oooooooooooo#ooooooooo
oooooooooooooooooo#ooo
ooooooooooooooooooooo#
ooooooooooooooooo#oooo
ooooooo#oooooooooooooo
oooooooooooooooooooo#o
ooooooooooo#oooooooooo
oooooooo#ooooooooooooo
ooooo#oooooooooooooooo
ooooooooooooooo#oooooo
oooooo#ooooooooooooooo
oooooooooo#ooooooooooo
oooooooooooooo#ooooooo
./n-queens-problem.py  26,43s user 0,02s system 96% cpu 27,424 total
```

## Idea 2

My second idea was to use a 2D array with the values

* 0: queen can be placed here
* 1: queen is here
* -1: no queen can be here

but then I've seen that when you do the backtracking step, you cannot simply
remove the -1 caused by the queen there. So I thought about something different:

* 1: a queen is here
* 0: no queen can attack this field
* -1: 1 queen can attack this field
* -2: 2 queens can attack this field:
* -3: 3 queens can attack this field
* …

This way we can use a simple 2D array to figure out if a position is valid.
We will only check if queens from above can capture queens from below:

TODO
