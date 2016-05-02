---
layout: post
title: Java Puzzle #1: Pre- and Postincrement
author: Martin Thoma
date: 2012-07-11 16:07:02.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
<h2>The puzzle</h2>
What is the output of the following piece of code?

```java
public class test {
    public static void main(String[] args) {
        int i = 1;
        i += ++i + i++ + ++i;

        int j = 1;
        j += ++j + j++ + ++j;

        int k = 1;
        k += k++ + k++ + ++k;

        int m = 1;

        System.out.println("i = " + i);
        System.out.println("j = " + j);
        System.out.println("k = " + k);
        System.out.println("m = " + (m += 1));
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
The output is:
```bash
i = 9
j = 9
k = 8
m = 2
```

<h2>Explanation</h2>
<h3>Part one</h3>
First, take a look at statements of this structure:
```java
i += s
```
where <code>i</code> is the integer and s is a statement (e.g. <code>++i</code>). This gets evaluated to 
```java
i = a + s
```
Source: <a href="http://wordpress.org/extend/plugins/embed-github-gist/">docs.oracle.com</a>

<h3>Part two</h3>
Lets take a look at pre- and postincrement in Java.

You can quite easily figure out what the different increments do by this snippet:
```java
public class test {
    public static void main(String[] args) {
        int i = 0;
        int j = 0;
        int k = 0;

        System.out.println("i = " + ++i);
        System.out.println("i = " + i);

        System.out.println("j = " + j++);
        System.out.println("j = " + j);

        System.out.println("k = " + (k += 1));
    }
}
```
Output:
```bash
i = 1
i = 1
j = 0
j = 1
k = 1
```

Line 7 adds +1 to <code>i</code> and returns the value.
Line 10 returns the value of <code>j</code> and adds +1 to <code>j</code>.
Line 13 adds +1 to <code>k</code> and returns <code>k</code>.

Lets return to the original puzzle. Java parses your code from left to right (<a href="http://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html">Source 1</a>, <a href="http://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html#jls-15.1">Source 2</a>).

Most important:
<blockquote>Evaluation of an expression can also produce side effects, because expressions may contain embedded assignments, increment operators, decrement operators, and method invocations.</blockquote>

So:
```java
int i = 1;
i += ++i + i++ + ++i;
```
is the same as
```java
i = ((i + (++i)) + (i++)) + (++i);
```
The first <code>++i</code> increments <code>i</code> to 2 and returns 2. So you have:
```java
i = 2;
i = ((1 + 2) + (i++)) + (++i);
```
The <code>i++</code> returns 2, as it is the new value of <code>i</code>, and increments <code>i</code> to 3:

```java
i = 3;
i = ((1 + 2) + 2) + ++i;
```

The second <code>++i</code> increments <code>i</code> to 4 and returns 4:
```java
i = 4;
i += ((1 + 2) + 2) + 4;
```

So you end up with <code>9</code>.

A <a href="http://en.wikipedia.org/wiki/Parse_tree">parse tree</a> of this evaluation would look like this:
<figure class="aligncenter">
            <a href="../images/2012/07/evaluation-tree.gif"><img src="../images/2012/07/evaluation-tree.gif" alt="Parse tree" style="max-width:454px;max-height:638px" class="size-full wp-image-30711"/></a>
            <figcaption class="text-center">Parse tree</figcaption>
        </figure>

The explanation for the other three ones is similar.

<h2>See also</h2>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Increment_and_decrement_operators">Increment and decrement operators</a></li>
  <li><a href="http://stackoverflow.com/q/971312/562769">Why avoid increment (&ldquo;++&rdquo;) and decrement (&ldquo;--&rdquo;) operators in JavaScript?</a></li>
  <li><a href="http://stackoverflow.com/q/11431914/562769">Pre- and postincrement in Java</a></li>
</ul>
