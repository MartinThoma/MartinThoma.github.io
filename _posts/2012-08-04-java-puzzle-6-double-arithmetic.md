---
layout: post
title: ! 'Java Puzzle #6: Double Arithmetic'
author: Martin Thoma
date: 2012-08-04 17:00:27.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
What is the output of the following snippet?

{% highlight java %}public class test {
    public static void main(String[] args) {
        double a = 1.3378901234567877;
        double b = 0.0008901234567876;
        double c = a - b;

        if (c == 1.337) {
            System.out.println("Hallo doubles!");
        } else {
            System.out.println("Oh no! Comparison failed!");
        }
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
<h2>Solution</h2>
{% highlight bash %}Oh no! Comparison failed!{% endhighlight %}

<h2>Explanation</h2>
Doubles are internally represented using the <a href="http://en.wikipedia.org/wiki/IEEE_floating_point">IEEE 754 standard</a> (<a href="http://docs.oracle.com/javase/specs/jls/se7/html/jls-4.html">source</a>).
This means, doubles are not represented with arbitrary precision.

Just execute this snippet:
{% highlight java %}public class test {
    public static void main(String[] args) {
        double a = 1.3378901234567876;
        System.out.println("a = " + a);
        double b = 0.0008901234567876;
        System.out.println("b = " + b);
        double c = a - b;
        System.out.println("c = " + c);
    }
}{% endhighlight %}

Output:
{% highlight bash %}a = 1.3378901234567877
b = 8.901234567876E-4
c = 1.3370000000000002{% endhighlight %}

<h2>Resolve problem</h2>
Use an appropriate epsilon to compare floats/doubles:
{% highlight java %}public class test {
    public static void main(String[] args) {
        double a       = 1.3378901234567877;
        double b       = 0.0008901234567876;
        double c       = a - b;
        double EPSILON = 0.000000000000001;

        if (Math.abs(c - 1.337) < EPSILON) {
            System.out.println("Hallo doubles!");
        } else {
            System.out.println("Oh no! Comparison failed!");
        }
    }
}{% endhighlight %}
