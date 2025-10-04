---
layout: post
title: Java Puzzle #13: Absolute Value Weirdness
slug: java-puzzle-13-absolute-value-weirdness
lang: en
author: Martin Thoma
date: 2012-10-19 17:00:00.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
What does the following Java snippet output?

```java
public class SomeClass {
    public static void main(String[] args) {
        int a = -10;
        int b = -2147483648; // -2147483648 == -2**31

        if (Math.abs(a) < -1) {
            System.out.println("|a| < -1");
        } else {
            System.out.println("|a| >= -1");
        }

        if (Math.abs(b) < -1) {
            System.out.println("|b| < -1");
        } else {
            System.out.println("|b| >= -1");
        }

        System.out.println("|a| = " + Math.abs(a));
        System.out.println("|b| = " + Math.abs(b));
    }
}
```

<details>
<summary>Click to see the Answer</summary>

```text
|a| >= -1
|b| < -1
|a| = 10
|b| = -2147483648
```
</details>

## Explanation

Integer values in Java range from -2,147,483,648 to 2,147,483,647 (32-bit signed integer). This means the absolute value of -2,147,483,648 cannot be represented as a positive integer in the same data type.

When `Math.abs(-2147483648)` is called, it actually returns -2,147,483,648 because:

1. The mathematical absolute value would be 2,147,483,648
2. But this value exceeds the maximum positive integer (2,147,483,647)
3. Due to integer overflow, it wraps around to the minimum negative value

This is why `|b| < -1` evaluates to true - because `Math.abs(b)` returns a negative number!

### Modern Solutions

In modern Java, you can use:
- `Math.absExact()` - throws an exception on overflow
- `long` data type for larger ranges
- `BigInteger` for arbitrary precision

For more details, see [this Stack Overflow answer](http://stackoverflow.com/a/5444634/562769).
