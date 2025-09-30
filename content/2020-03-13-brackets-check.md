---
layout: post
lang: en
title: Code Golf: Brackets Check
slug: brackets-check
author: Martin Thoma
date: 2020-03-13 20:00
category: Code
tags: Code, Python, Code Golf
featured_image: logos/star.png
---
Write a function `check_bracket_validity` which takes a sequence of brackets as
input and determines if it is valid.

A sequence is valid, iff:

* All opened brackets close
* Brackets come in pairs - only what was opened can be closed again
* The 3 styles which should be supported are:
    * Round brackets: `(` and `)`
    * Square brackets: `[` and `]`
    * Curly brackets: `{` and `}`
* Brackets must be ordered: Either the opening and the closing brackets are
  within another pair of brackets or not. Something like this is invalid:
  `[(])`

Restrictions:

* The formatter `black` will be applied to any solution
* The signature, the docstring and the doctest is fixed.


## Solution: 846 characters

```python
def check_bracket_validity(brackets: str):
    """
    Check if a sequence of brackets is valid.

    Examples
    --------
    >>> check_bracket_validity("()[]{}")
    True
    >>> check_bracket_validity("([{([{}])}])")
    True
    >>> check_bracket_validity("([{([{}])}]")
    False
    >>> check_bracket_validity("([{([{}])}]))")
    False
    >>> check_bracket_validity("([)]")
    False
    """
    opening = "([{"
    pair = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if pair[popped] != bracket:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```


## Minified Solution: 766 characters

Just using one-letter variable names:

```python
def check_bracket_validity(brackets: str):
    """
    Check if a sequence of brackets is valid.

    Examples
    --------
    >>> check_bracket_validity("()[]{}")
    True
    >>> check_bracket_validity("([{([{}])}])")
    True
    >>> check_bracket_validity("([{([{}])}]")
    False
    >>> check_bracket_validity("([{([{}])}]))")
    False
    >>> check_bracket_validity("([)]")
    False
    """
    o, p, s = "([{", {"(": ")", "[": "]", "{": "}"}, []
    for b in brackets:
        if b in o:
            s.append(b)
        else:
            if len(s) == 0:
                return False
            q = s.pop()
            if p[q] != b:
                return False
    return len(s) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

## See also

* [Codegolf](https://codegolf.stackexchange.com/)
    * [Bracket balancing](https://codegolf.stackexchange.com/q/65526/5240)
    * [Are the brackets fully matched?](https://codegolf.stackexchange.com/q/77138/5240)
