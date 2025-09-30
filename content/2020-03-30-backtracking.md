---
layout: post
lang: en
title: Backtracking
slug: backtracking
author: Martin Thoma
date: 2020-03-30 20:00
category: Code
tags: Algorithms, Constraint-satisfaction, COP, CSP, Operations Research, Backtracking, Branch-and-Bound
featured_image: logos/ai.png
---
Backtracking is a concept for solving discrete constraint satisfaction problems
(CSPs). Those problems don't have an optimal solution, but just solutions which
satisfy the constraints. The idea of backtracking is to try a solution. If it
doesn't work, go back and try something else.

Backtracking is often implemented with recursion, but does not need to use
recursion.

## The Structure

Typically, when you apply backtracking, it looks like this:

```python
partial_solutions = [initial_solution_draft]  # stack or queue
while partial_solutions:
    partial_solution = partial_solutions.pop()
    if is_complete(partial_solution):
        return partial_solution
    for choice in choices(partial_solution):
        extended_solution = extend(partial_solution, choice)
        if is_valid(extended_solution):
            partial_solutions.append(extended_solution)
return None  # Constraints could not be satisfied
```

As you can see, it is essentially just a way to brute-force the problem.

The rest of the article consists of examples. I checked the n-queens example
for correctness, but not the others.


## Backtracking vs DFS

When you apply Backtracking, you first define a solution space. This might
happen implicitly, e.g. by defining a data structure. For example, in the
n-queens problem the solution space is all permutations of the number from 0 to
(n-1). Everything else is guaranteed not to be a solution. And most of the
permutations are also no solutions.

Depth First Search (DFS) is a graph traversal algorithm. It is one way to
search in the solution space for a solution that satisfies the constraints. It
is the typical choice to iterate the solution space. Other search algorithms
are Breadth First Search (BFS) and A\*.


## Backtracking vs B&B

Branch-and-Bound (B&B) is a concept to solve discrete constrained optimization
problems (COPs). They are similar to CSPs, but besides having the constraints
they have an optimization criterion. In contrast to backtracking, B&B uses
Breadth-First Search.

B&B is a [label correction algorithm](https://martin-thoma.com/label-correction-algorithm/).
It is a search algorithm which uses a lower bound and an upper bound for the
search. Think of a shortest-path problem.

One part of the name, the bound, refers to the way B&B prunes the space of possible solutions: It gets a heuristic which gets an upper bound. If this cannot be improved, a sup-tree can be discarded.

With the lower bound, the minimum length of a given partial solution from
source to sink can be calculated. If that minimum length is longer than another
answer which was already found, then the calculation at that point can be
aborted.

With the upper bound, one can extend the partial solutons. Essentially, one can
make the pruning described before more efficient. We don't have to find a
concrete solution anymore, but for partial solutions we already know the
distance they will take at most.


## Runtime Complexity

Assume that you have to go $n$ steps and at every step you have $a \geq 2$
choices. This means the runtime is exponential - $\mathcal{O}(\alpha^n)$.

If you add more rules to `is_valid` - excluding more solutions - you reduce
$\alpha$. This can mean a huge speedup.

## n Queens

The [n Queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) is
probably the most common example. You have a n×n chess board and n queens. You
need to place the queens on the chess board in such a way that they don't
threaten each other.

A queen threatens another queen if it is…

* … in the same row
* … in the same column
* … in the same diagonal

If you say that the first coordinate x is the row and the second one, y, is the
column, then you can easily determine if they threaten each other:

```python
from typing import List, Tuple


def all_n_queens_solutions(n: int) -> List[Tuple[int, ...]]:
    """
    Find all possible solutions to the n-queens problem.

    Parameters
    ----------
    n : int

    Returns
    -------
    all_solutions : List[List[int]]
        Each inner list represents a single solution.
        The first digit of it is the column of the queen in the first row.
        The second digit is the column of the queen in the second row, ...

    Note
    ----
    Columns are 0-based.

    Examples
    --------
    >>> all_n_queens_solutions(1)
    [(0,)]
    >>> all_n_queens_solutions(2)
    []
    >>> all_n_queens_solutions(3)
    []
    >>> all_n_queens_solutions(4)
    [(1, 3, 0, 2), (2, 0, 3, 1)]
    """
    solutions = []
    solution_queue: List[Tuple[int, ...]] = [()]  # contains valid partial solutions
    while solution_queue:
        solution = solution_queue.pop(0)
        if len(solution) < n:
            for i in range(n):
                if not is_new_threatening(solution, x=len(solution), y=i):
                    new_solution = solution + (i,)
                    solution_queue.append(new_solution)
        else:
            # It's finished!
            solutions.append(solution)
    return solutions


def is_new_threatening(solution: Tuple[int, ...], x: int, y: int) -> bool:
    for x_old, y_old in enumerate(solution):
        if is_threatening(x_old, y_old, x, y):
            return True
    return False


def is_threatening(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Check if the positions are threatening each other.

    Examples
    --------
    >>> is_threatening(0, 1, 1, 0)
    True
    """
    same_row = x1 == x2
    same_col = y1 == y2

    delta1 = min(x1, y1)
    major_coords1 = (x1 - delta1, y1 - delta1)
    delta2 = min(x2, y2)
    major_coords2 = (x2 - delta2, y2 - delta2)
    same_diagonal_major = major_coords1 == major_coords2

    delta1 = x1
    delta2 = x2
    minor_coords1 = (x1 - delta1, y1 + delta1)
    minor_coords2 = (x2 - delta2, y2 + delta2)
    same_diagonal_minor = minor_coords1 == minor_coords2
    same_diagonal = same_diagonal_major or same_diagonal_minor
    return same_row or same_col or same_diagonal
```


<table class="table">
    <thead>
        <tr>
            <th>n</th>
            <th>solutions (<a href="https://oeis.org/A000170">A000170</a>)</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0</td>
    </tr>
    <tr>
        <td>3</td>
        <td>0</td>
    </tr>
    <tr>
        <td>4</td>
        <td>2</td>
    </tr>
    <tr>
        <td>5</td>
        <td>10</td>
    </tr>
    <tr>
        <td>6</td>
        <td>4</td>
    </tr>
    <tr>
        <td>7</td>
        <td>40</td>
    </tr>
    <tr>
        <td>8</td>
        <td>92</td>
    </tr>
    <tr>
        <td>9</td>
        <td>352</td>
    </tr>
    <tr>
        <td>10</td>
        <td>724</td>
    </tr>
    <tr>
        <td>11</td>
        <td>2680</td>
    </tr>
    <tr>
        <td>12</td>
        <td>14200</td>
    </tr>
    </tbody>
</table>


## Maze finding

In order to find a solution in a maze, one can apply depth first search (DFS).
DFS can be seen as a specific form of backtracking
([source](https://stackoverflow.com/a/1294741/562769)).

```python
from typing import Optional, List, Tuple


def find_way_out(
    maze, current_pos: Position, current_path: Tuple[Position, ...] = None
) -> Optional[Tuple[Position, ...]]:
    if is_exit(current_pos):
        return current_path
    if current_path is None:
        current_path = [current_pos]
    # Implement possible_paths for your problem
    for next_step in possible_paths(maze, current_pos):
        next_pos = step(current_pos, next_step)
        if next_pos == current_path[-1]:
            # We just came from this position
            continue
        solution = find_way_out(maze, next_pos, current_path + (next_pos,))
        if solution is None:
            return solution
    # We didn't find a way out
    return None
```

The reason why I used a tuple is to prevent modification. This way, I can be
sure that the recursive calls work on copies.

Once Python hits a recurision depth of about 500, you will see a
[RecursionError](https://docs.python.org/3/library/exceptions.html#RecursionError).
So if we need to make more than 500 steps, this will not work anymore. Hence an
iterative soltuion is better. Please note that it is still backtracking and
that it is still DFS. It's just not recursive anymore:

```python
from typing import Optional, List, Tuple


def find_way_out(
    maze, current_pos: Position, current_path: Tuple[Position, ...] = None
) -> Optional[Tuple[Position, ...]]:
    if is_exit(current_pos):
        return current_path
    if current_path is None:
        current_path = [current_pos]
    explore = [(current_pos, current_path)]
    while explore and not is_exit(current_pos):
        current_pos, current_path = explore.pop()
        for next_step in possible_paths(maze, current_pos):
            next_pos = step(current_pos, next_step)
            if next_pos == current_path[-1]:
                # We just came from this position
                continue
            explore.append((next_pos, current_path + (next_pos,)))
    return None
```

## Sudoku

```python
from collections import Counter
from typing import List, Iterable, Optional, Tuple


class SudokuBoard:
    def __init__(board: List[List[int]]):
        # A board is a 9x9 matrix which has values in 1 to 9.
        # The value 0 denotes that the cell is empty
        assert len(board) == 9
        for row in board:
            assert len(row) == 9
            for el in row:
                assert 0 <= el <= 9
        self.board = board
        assert self.is_valid()

    def set(self, x: int, y: int, digit: int):
        assert self.board[x][y] == 0
        assert digit in list(range(1, 10))
        self.board[x][y] = digit
        if not self.validate_position(x, y):
            raise ValueError(f"You can't set {digit} at ({x}, {y})")

    def is_valid(self) -> bool:
        """Check if the sudoku-rule is fulfilled."""
        # Check Rows and columns
        for index in range(9):
            if not (self.validate_row(index) and self.validate_column(index)):
                return False

        # Check blocks
        for i in range(3):
            for j in range(3):
                # (i, j) is the top-left element of the block
                if not is_valid_sudoku_set(get_block(self.board, i, j)):
                    return False
        # All fine :-)
        return True

    def validate_row(self, row_index: int) -> bool:
        return is_valid_sudoku_set(self.board[row_index])

    def validate_column(self, column_index: int) -> bool:
        col = []
        for row_index in range(9):
            col.append(self.board[row_index][column_index])
        return is_valid_sudoku_set(col)

    def validate_position(self, x: int, y: int) -> bool:
        """Make sure the given position doesn't break the board."""
        if not (self.validate_row(x) and self.validate_column(y)):
            return False

        i = (x // 3) * 3
        j = (y // 3) * 3
        if not is_valid_sudoku_set(get_block(self.board, i, j)):
            return False
        return True

    def is_solved(self) -> bool:
        return all(el != 0 for row in self.board for el in row) and self.is_valid()

    def get_first_zero_position(self) -> Optional[Tuple[int, int]]:
        for row_index, row in enumerate(self.board):
            for col_index, element in enumerate(row):
                if element == 0:
                    return (row_index, col_index)


def is_valid_sudoku_set(numbers: Iterable) -> bool:
    c = Counter(numbers)
    for digit, count in c.items():
        if digit == 0:
            continue
        elif digit in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if count > 1:
                return False
        else:
            raise RuntimeError(f"Value '{digit}' found, but expected int in [0, 9]")
    return True


def get_block(board: List[List[int]], i: int, j: int) -> Iterable[int]:
    for di in range(3):
        for dj in range(3):
            yield board[i + di][j + dj]


def solve_sudoko(board: SudokuBoard) -> Optional[SudokuBoard]:
    stack = [board]  # we want a DFS
    while stack:
        board = stack.pop()
        if board.is_solved():
            return board
        for x, y in board.get_first_zero_position():
            for digit in range(1, 10):
                new_board = SudokuBoard(copy(self.board))
                try:
                    new_board.set(x, y, digit)
                    stack.append(new_board)
                except ValueError:
                    # Setting digit at that position would make the board invalid
                    continue
```

You can solve Sudoku with [GLPK](https://gist.github.com/ymakino/4605973), the
GNU Linear Programming Kit, as well.


## See also

* Google OR-Tools: [The N-queens Problem](https://developers.google.com/optimization/cp/queens)
* cs.StackExchange: [Backtracking vs Branch-and-Bound](https://cs.stackexchange.com/q/123382/2914)
* StackOverflow: [Difference between 'backtracking' and 'branch and bound'](https://stackoverflow.com/q/30025421/562769)

## Footnotes

[^1]: [Kevin Buchin](https://www.win.tue.nl/~kbuchin/): [Backtracking / Branch-and-Bound](https://www.win.tue.nl/~kbuchin/teaching/2IL15/backtracking.pdf). In Algorithms (2IL15) – 2014.
