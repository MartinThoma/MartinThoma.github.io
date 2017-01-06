---
layout: post
title: Java Puzzle #12: Control-flow
author: Martin Thoma
date: 2012-10-17 17:00:19.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
What is the output of the following <strong>HelloWorld.java</strong>?

```java
public class HelloWorld {
    public static void main(String[] args) {
        if (2 < 1); {
            System.out.println("Yes");
        }
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

<h2>Answer</h2>
The output is "Yes". 

<h2>Explanation</h2>
The <code>;</code> means, that no block is executed. The <code>{ ... }</code> is just a code block and not really related to the <code>if</code>-statement.
