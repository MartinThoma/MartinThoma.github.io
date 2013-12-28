---
layout: post
title: ! 'Java Puzzle #13: Absolute value weirdness'
author: Martin Thoma
date: 2012-10-19 17:00:00.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- puzzle
featured_image: 2012/07/java-thumb.png
---
What does the following snippet output?

{% highlight java %}public class SomeClass {
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
{% highlight text %}|a| >= -1
|b| < -1
|a| = 10
|b| = -2147483648{% endhighlight %}

<h2>Explanation</h2>
Integer values range (in Java) from -2147483648 to 2147483647. This means, the absolute value of -2147483648 is not in the integer range. For more details, see <a href="http://stackoverflow.com/a/5444634/562769">this SO answer</a>.
