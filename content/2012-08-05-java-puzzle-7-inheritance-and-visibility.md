---
layout: post
lang: en
title: Java Puzzle #7: Inheritance and Visibility
author: Martin Thoma
date: 2012-08-05 17:00:38.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
You are given the following two classes:
<strong>Animal.java</strong>:
```java
public class Animal {
    private final int height = 120;
}
```

<strong>Tiger.java</strong>:
```java
public class Tiger extends Animal {
    public int height;
}
```

What is the output of the following three snippets:
<strong>test1.java</strong>:
```java
public class test1 {
    public static void main(String[] args) {
        Tiger t = new Tiger();
        System.out.println(t.height);
    }
}
```

<strong>test2.java</strong>:
```java
public class test2 {
    public static void main(String[] args) {
        Animal t = new Tiger();
        System.out.println(t.height);
    }
}
```

<strong>test3.java</strong>:
```java
public class test3 {
    public static void main(String[] args) {
        Animal t = new Animal();
        System.out.println(t.height);
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
.
.
.
.


<h2>Answer</h2>
<strong>test1.java</strong>:
```bash
0
```

<strong>test2.java</strong>:
```bash
Exception in thread "main" java.lang.Error: Unresolved compilation
      problem:
	The field Animal.height is not visible

	at test.main(test.java:4)
```

<strong>test3.java</strong>:
```bash
Exception in thread "main" java.lang.Error: Unresolved compilation
      problem:
	The field Animal.height is not visible

	at test.main(test.java:4)
```
