---
layout: post
status: publish
published: true
title: ! 'Java Puzzle #7: Inheritance and Visibility'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 37871
wordpress_url: http://martin-thoma.com/?p=37871
date: 2012-08-05 17:00:38.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- puzzle
comments:
- id: 329761
  author: Tiny
  author_email: nobody2012855@gmail.com
  author_url: http://None
  date: !binary |-
    MjAxMi0xMC0yMiAyMTo1MDowNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0xMC0yMiAxOTo1MDowNiArMDIwMA==
  content: It's interesting. It's because unlike methods (except private, static and
    final), fields (members variables) in Java can not be implemented polymorphically.
    They can not have polymorphic behaviour even though in the second case, a subclass
    reference (Tiger) is assigned to Animal (superclass) and hence, t.height will
    point to height in Aminal which it finds private and issues a compile-time error.
    The rest of the cases are obvious.
---
You are given the following two classes:
<strong>Animal.java</strong>:
[java]public class Animal {
    private final int height = 120;
}[/java]

<strong>Tiger.java</strong>:
[java]public class Tiger extends Animal {
    public int height;
}[/java]

What is the output of the following three snippets:
<strong>test1.java</strong>:
[java]public class test1 {
    public static void main(String[] args) {
        Tiger t = new Tiger();
        System.out.println(t.height);
    }
}[/java]

<strong>test2.java</strong>:
[java]public class test2 {
    public static void main(String[] args) {
        Animal t = new Tiger();
        System.out.println(t.height);
    }
}[/java]

<strong>test3.java</strong>:
[java]public class test3 {
    public static void main(String[] args) {
        Animal t = new Animal();
        System.out.println(t.height);
    }
}[/java]

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
[bash]0[/bash]

<strong>test2.java</strong>:
[bash]Exception in thread "main" java.lang.Error: Unresolved compilation 
      problem: 
	The field Animal.height is not visible

	at test.main(test.java:4)[/bash]

<strong>test3.java</strong>:
[bash]Exception in thread "main" java.lang.Error: Unresolved compilation 
      problem: 
	The field Animal.height is not visible

	at test.main(test.java:4)[/bash]
