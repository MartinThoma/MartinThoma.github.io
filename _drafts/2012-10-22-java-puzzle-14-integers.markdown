---
layout: post
status: publish
published: true
title: ! 'Java Puzzle #14: Integers'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 47201
wordpress_url: http://martin-thoma.com/?p=47201
date: 2012-10-22 12:00:44.000000000 +02:00
categories:
- Code
tags: []
comments: []
---
What is the output of the following script?
{% highlight java %}public class SomeClass {
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
}{% endhighlight %}

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
{% highlight text %}It's weird:
x   = 2147483647
2*x = -2{% endhighlight %}

<h2>Explanation</h2>
2*x is out of Java Integer range, so it comes back at the other end.
