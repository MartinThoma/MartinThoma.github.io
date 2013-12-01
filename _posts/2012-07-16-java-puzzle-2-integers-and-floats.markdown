---
layout: post
status: publish
published: true
title: ! 'Java Puzzle #2: Integers and Floats'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 32421
wordpress_url: http://martin-thoma.com/?p=32421
date: 2012-07-16 17:00:35.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- puzzle
comments: []
---
<h2>Basics</h2>
As you might know, Americans measure the temperature in <a href="http://en.wikipedia.org/wiki/Fahrenheit">Fahrenheit</a>. I'm not quite sure, but I guess the rest of the world uses <a href="http://en.wikipedia.org/wiki/Celsius">Celsius</a>.

0&deg; C is the temperature when water freezes.
100&deg; C is the temperature when water boils.

0&deg; F is the lowest temperature of the winter 1708/1709 in <a href="http://en.wikipedia.org/wiki/Gda%C5%84sk">Gdańsk</a>.
32&deg; F is the temperature when water boils.

If you want to calculate the temperature $T_C$ in &deg;C from $T_F$ in &deg;F you can use this formula:
$T_C = (T_F &minus; 32) &middot; \frac{5}{9}$

<h2>The puzzle</h2>
What is the output of the following script?

{% highlight java %}public class test {
    static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * (5 / 9);
    }

    public static void main(String[] args) {
        double fahrenheit = 100;
        double celsius = fahrenheitToCelsius(fahrenheit);
        System.out.format("%.2f&deg; Fahrenheit is %.2f&deg; C\n", 
                fahrenheit, celsius);

        fahrenheit = 30;
        celsius = fahrenheitToCelsius(fahrenheit);
        System.out.format("%.2f&deg; Fahrenheit is %.2f&deg; C\n", 
                fahrenheit, celsius);
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
.
.
.

<h2>Answer</h2>
{% highlight bash %}100.00&deg; Fahrenheit is 0.00&deg; C
30.00&deg; Fahrenheit is -0.00&deg; C{% endhighlight %}

<h2>Explanation</h2>
The problem is integer division.

{% highlight java %}public class test {
    public static void main(String[] args) {
        System.out.format("5 / 9 = %.2f\n", (double) (5 / 9));
    }
}{% endhighlight %}
This outputs:
{% highlight bash %}5 / 9 = 0.00{% endhighlight %}

So you are multiplying with $\pm 0$ instead of $0.55555$.
