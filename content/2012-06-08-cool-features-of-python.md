---
layout: post
title: Cool Features of Python
slug: cool-features-of-python
lang: en
author: Martin Thoma
date: 2012-06-08 17:30:10.000000000 +02:00
category: Code
tags: Programming, Python
featured_image: 2011/09/Python-Logo.png
---
A friend wanted to know why I enjoy programming in Python so much more than programming in other languages. So I will describe some special features of Python that make it much easier to quickly implement algorithms.

I also made drafts of how these tasks would be solved in most programming languages. When I say "most," I mean most languages that are widely spread (so C/C++/Java is much more important than almost any other languages combined). I know that these tasks would be solved completely differently in functional programming languages.

## Rapid, Readable Programming

### Intuitive Looping Through Lists
You can loop through every list-like datastructure like this:

```python
for element in list:
    print(element)
```

### Arbitrary Integer Size

**Task**: Print the sum of the digits of $2^{100000}$.

**Java**:
```java
import java.math.BigInteger;

public class test {
    public static void main(String[] args) {
        BigInteger a = new BigInteger("2");
        a = a.pow(100000);
        int sum = 0;
        for (int i=0; i < a.toString().length(); i++) {
            sum += a.toString().charAt(i);
        }
        System.out.println(sum);
    }
}
```

**Python**: (was much faster in both computation and programming time!)
```python
big = 2 ** 100000
sumOfDigits = 0
for digit in str(big):
    sumOfDigits += int(digit)

print(sumOfDigits)
```

Python has no need for a special class as it has arbitrary length integers (see [source](http://docs.python.org/release/3.1.5/c-api/long.html))

### Switch Values of Variables

**Task**: You want to make sure that variable `a` is smaller than `b` ($a < b$).

**Most languages**:
```python
tmp = a
a = min(a, b)
b = max(tmp, b)
```

**Python**:
```python
a, b = min(a, b), max(a, b)
```

### Return More Than One Variable

**Task**: Evaluate $f: \mathbb{R}^2 \rightarrow \mathbb{R}^3, f(x, y) := (x^2, y^2, x+y)$

**Most languages**:
```java
double[] function(double x, double y) {
    double[] returnValues = new double[3];
    returnValues[0] = x * x;
    returnValues[1] = y * y;
    returnValues[2] = x + y;
    return returnValues;
}

double[] values = function(4, 5);
System.out.printf("Part 1: %.2f%n", values[0]);
System.out.printf("Part 3: %.2f%n", values[2]);
```

**Python**:
```python
def function(x, y):
    return (x * x, y * y, x + y)


a, b, c = function(4, 5)
print(f"Part 1: {a:.2f}")
print(f"Part 3: {c:.2f}")
```

This is called "tuple unpacking". It actually returns only one variable (a tuple), but creating the tuple is so easy that it doesn't feel like creating another variable.

### Short Initialization

**Task**: Get a string representation of a list from the standard library

**Java**:
```java
import java.util.Arrays;
import java.util.List;

public class test {
    public static void main(String[] args) {
        List<Integer> myList = Arrays.asList(1, 3, 3, 7);
        System.out.println(myList);
    }
}
```

**Python**:
```python
my_list = [1, 3, 3, 7]
print(my_list)
```

Both get the same result.

### Chaining Comparisons

**Task**: You would like to check if $x \in [-5, 42]$.

**Most languages**:
```java
if (-5 <= x && x <= 42)
```

**Python**:
```python
if -5 <= x <= 42:
    pass
```

### Enumeration

**Task**: You have a list and you would like to print it, prefixed with the index in the list.

**Java**:
```java
List<Integer> myList = Arrays.asList(1, 3, 3, 7);
for (int i = 0; i < myList.size(); i++) {
    System.out.printf("%d: %d%n", i, myList.get(i));
}
```

**Python**:
```python
my_list = [1, 3, 3, 7]

for nr, element in enumerate(my_list):
    print(f"{nr}: {element}")
```

### Named String formatting
Python allows you to give parameters names:
```python
print("The %(foo)s is %(bar)i." % {"foo": "answer", "bar": 42})
```

### any() and all()

**Task**: You have a very long list and you want to know if a prime is in this list.

**Java**:
```java
List myList = (List initialisation and assignment of many values)
boolean isPrimePresent = false;
for (int element : myList) {
    if (isPrime(element)) {
        isPrimePresent = true;
        break;
    }
}

if (!isPrimePresent) {
    System.out.println("The list did not containe a prime.");
}
```

**Python**:
```python
my_list = [4, 4, 9, 12]

if not any(is_prime(x) for x in my_list):
    print("The list did not contain a prime")
```

See also: [StackOverflow answer from steveha](http://stackoverflow.com/questions/10958874/exists-keyword-in-python).


## Testing and Documentation

### Doctest
You can write documentation and unit tests at the same time! Take a look at [doctest — Test interactive Python examples](http://docs.python.org/library/doctest.html).

### Sphinx
Documentation can be generated from partially docstrings, partially rst files
with [Sphinx](http://sphinx-doc.org/tutorial.html).
It can be uploaded to [pythonhosted.org](http://pythonhosted.org/) just like [neurolab](https://pythonhosted.org/neurolab/index.html) did it (see also [sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html)).


## The Rest

### Lists and Generators
I already wrote an article about <a href="../understanding-python-lists/" title="Understanding Python Lists">Python Lists</a> and <a href="../python-generators/" title="Python Generators">Python Generators</a>. I love Pythons lists ☺

### for ... else

**Task**: You have a very long list and you want to know if a prime is in this list.

**Java**:
```java
List myList = (List initialisation and assignment of many values)
boolean isPrimePresent = false;
for (int element : myList) {
    if (isPrime(element)) {
        isPrimePresent = true;
        break;
    }
}

if (!isPrimePresent) {
    System.out.println("The list did not contain a prime.");
}
```

**Python**:
```python
my_list = [1, 3, 3, 7]

for element in my_list:
    if is_prime(element):
        break
else:
    print("The list did not contain a prime.")
```

### Step Through Lists

**Task**: Print only every n-th element of an iterable.

```python
for element in my_list[::n]:
    print(element)
```

### Dynamically add properties to objects and classes

```python
class Node(object):
    value = 3


a = Node()
b = Node()

print(a.value)

""" colorize the node! """
# print(a.color) ==> AttributeError

# thats ok, although the object originally had no attribute "color"
a.color = "white"
print(a.color)

# You can even add a property to the class
Node.special = "here is it"
print(b.special)
```

### Imaginary numbers
Python directly supports usage of imaginary numbers:

```python
(2j + 1) ** 2
```

Output: `(-3+4j)`

## Read Also

[An Informal Introduction to Python](http://docs.python.org/tutorial/introduction.html)
