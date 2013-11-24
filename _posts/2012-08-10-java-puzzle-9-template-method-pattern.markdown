---
layout: post
status: publish
published: true
title: ! 'Java Puzzle #9: Template method pattern'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 38041
wordpress_url: http://martin-thoma.com/?p=38041
date: 2012-08-10 17:00:33.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- SWT I
- puzzle
- Design Pattern
comments: []
---
The following Java Puzzle is an example for the <a href="http://en.wikipedia.org/wiki/Template_method_pattern">template method pattern</a>. It is a design pattern by the <a href="http://en.wikipedia.org/wiki/Design_Patterns">Gang of Four</a>.

What is the output of the following snippet:
<strong>AbstractClass.java</strong>:
[java]public class AbstractClass {
    int templateMethod() {
        return simpleOperation1() * simpleOperation2();
    }

    int simpleOperation1() {
        return 2;
    }

    int simpleOperation2() {
        return 3;
    }
}[/java]

<strong>ConcreteClass.java</strong>:
[java]public class ConcreteClass extends AbstractClass {
    @Override
    int simpleOperation1() {
        return 5;
    }

    @Override
    int simpleOperation2() {
        return 7;
    }
}[/java]

<strong>test.java</strong>:
[java]public class test {
    public static void main(String[] args) {
        ConcreteClass t = new ConcreteClass();
        System.out.println(t.templateMethod());
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

<h2>Answer</h2>
[bash]35[/bash]

35

<h2>Explanation</h2>
You can think of it like this: First, you create the empty class <code>ConcreteClass</code>. It has only the methods inherited by <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Object.html">Object</a> like the <code>constructor</code>, <code>equals()</code> and <code>toString()</code>. Then it gets extended by AbstractClass with <code>templateMethod()</code>, <code>simpleOperation1()</code> and <code>simpleOperation2()</code>. After that, the method overrides <code>simpleOperation1()</code> and <code>simpleOperation2()</code>, but <code>templateMethod()</code> uses them. It uses the methods that are now in <code>ConcreteClass</code>.

I don't know what Java exactly does internally, but thats a good way to think about it. If somebody has more information, please share it as a comment!
