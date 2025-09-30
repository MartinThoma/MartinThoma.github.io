---
layout: post
lang: en
title: Pythons map, reduce and filter as list comprehensions
slug: python-map-reduce-filter
author: Martin Thoma
date: 2016-07-05 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
I recently was challenged to re-write Pythons `map`, `reduce` and `filter` as
list comprehensions.


## Examples

First of all, I want to make sure you understand what those functions do.
You might also want to have a look at my old article
[Functional Programming in Python](https://martin-thoma.com/functional-programming-in-python/).


### map

```python
numbers = list(range(10))
squares = map(lambda x: x ** 2, numbers)
print(squares)
```

gives

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```


### filter

```python
def is_prime(element):
    if element == 2:
        return True
    elif element <= 1 or element % 2 == 0:
        return False
    else:
        for i in range(3, element, 2):
            if element % i == 0:
                return False
    return True


myList = [4, 4, 9, 12, 13, 2, 7, 9, 11, 11]
r = filter(is_prime, myList)
print(r)
```

gives `[13, 2, 7, 11, 11]`.


### reduce

```python
numbers = list(range(10))
diff = reduce(lambda x, y: x - y, numbers)
print(diff)
```

gives `-45`, because

$$((((((((0-1)-2)-3)-4)-5)-6)-7)-8)-9 = -45$$



## Sequential solution

The standard way to do these tasks without `map`, `filter` and `reduce` is to
use loops.


### map

```python
numbers = list(range(10))
squares = []
for x in numbers:
    squares.append(x ** 2)
print(squares)
```


### filter

```python
def is_prime(element):
    if element == 2:
        return True
    elif element <= 1 or element % 2 == 0:
        return False
    else:
        for i in range(3, element, 2):
            if element % i == 0:
                return False
    return True


my_list = [4, 4, 9, 12, 13, 2, 7, 9, 11, 11]
r = []
for x in my_list:
    if is_prime(x):
        r.append(x)
print(r)
```

### reduce

```python
numbers = list(range(10))
x = numbers[0]
for y in numbers[1:]:
    x = x - y
print(x)
```

## List comprehensions

List comprehensions are - according to Guido van Rossum - the way to go. So
lets see how the code looks like without `map`, `reduce` and `filter`.


### map

```python
numbers = list(range(10))
squares = [x ** 2 for x in numbers]
print(squares)
```

I think that is much more readable than the map solution.


### filter

```python
def is_prime(element):
    if element == 2:
        return True
    elif element <= 1 or element % 2 == 0:
        return False
    else:
        for i in range(3, element, 2):
            if element % i == 0:
                return False
    return True


my_list = [4, 4, 9, 12, 13, 2, 7, 9, 11, 11]
r = [x for x in my_list if is_prime(x)]
print(r)
```

I also think this is more readable, as you can easily combine it with more
transformations.


### reduce

This is the tricky one. List comprehensions create lists again, so using only
list comprehensions is not going to work. However, you could cheat.
`sum(numbers)` is essentially `reduce(lambda x, y: x + y, numbers)`. So we only
have to change the sign, except for the first one:

```python
numbers = list(range(10))
diff = sum([numbers[0]] + [-x for x in numbers[1:]])
print(diff)
```

So, granted, the code using `reduce` looks much better. However, people argue
that you should use the sequential solution because it is simpler to
understand. By now, I understood every piece of code using `reduce`. But I
haven't seen it too often.
