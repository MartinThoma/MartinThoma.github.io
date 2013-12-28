---
layout: post
title: ! 'Java Puzzle #10: Multiple Interfaces'
author: Martin Thoma
date: 2012-08-16 17:00:25.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- puzzle
featured_image: 2012/07/java-thumb.png
---
You have to following source code:

<strong>A.java</strong>:
{% highlight java %}public interface A {
    public int methodA(double a, int b, char c);
    public int methodB();
}{% endhighlight %}

<strong>B.java</strong>:
{% highlight java %}public interface B {
    public int methodB();
    public void methodC();
}{% endhighlight %}

<strong>test.java</strong>:
{% highlight java %}public class test implements A, B {
    public static void main(String[] args) {
        test t = new test();
        System.out.println(t.methodA(1, 2, '3'));
        System.out.println(t.methodB());
        t.methodC();
    }

    @Override
    public int methodA(double a, int b, char c) {
        return 42;
    }

    @Override
    public int methodB() {
        return 1337;
    }

    @Override
    public void methodC() {
        System.out.println("methodC executed.");
    }
}{% endhighlight %}

What is the output? Does it compile? Is there a <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/RuntimeException.html">RuntimeException</a>?

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
Output:
{% highlight bash %}42
1337
methodC executed.{% endhighlight %}

<h2>Explanation</h2>
If you use an Interface, it simply means you have to implement some methods. If more than one Interface forces you to implement the method, you still have to implement it only once. It just works fine.
