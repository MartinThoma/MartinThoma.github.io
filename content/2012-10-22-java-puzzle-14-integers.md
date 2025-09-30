---
layout: post
lang: en
title: Java Puzzle #14: Integers
author: Martin Thoma
date: 2012-10-22 12:00:44.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
---
What is the output of the following script?

```java
public class SomeClass {
    public static void main(String[] args) {
        int x = 2147483647; // 2147483647 == 2**31 - 1
        if (x < 2*x) {
            System.out.println("Everything's ok:");
        } else {
            System.out.println("It's weird:");
        }

        System.out.println("x   = " + x);
        System.out.println("2*x = " + 2*x);
    }
}
```

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

<h2>Answer</h2>
```text
It's weird:
x   = 2147483647
2*x = -2
```

<h2>Explanation</h2>
`2*x` is out of Java Integer range, so it comes back at the other end.
