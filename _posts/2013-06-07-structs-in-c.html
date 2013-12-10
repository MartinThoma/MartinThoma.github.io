---
layout: post
status: publish
published: true
title: Structs in C++
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 69661
wordpress_url: http://martin-thoma.com/?p=69661
date: 2013-06-07 16:25:18.000000000 +02:00
categories:
- Code
tags:
- CPP
- struct
comments:
- id: 1211491
  author: Rene Pickhardt
  author_email: r.pickhardt@gmail.com
  author_url: http://www.rene-pickhardt.de
  date: !binary |-
    MjAxMy0wNi0xNCAxMjo1Mzo0MyArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0xNCAxMDo1Mzo0MyArMDIwMA==
  content: ! "I would say that structs are basically the same as classes only the
    standard data hiding is different. \r\nWhere in classes fields are private by
    standard in structs they are public. At least this is what I remember from my
    C++ class in high school. \r\n\r\nIf structs and classes are compiled differently
    to machine could is something that I would be interested in but doing a google
    search on the differences of structs and classes I could only find this stack
    overflow discussion http://stackoverflow.com/questions/92859/what-are-the-differences-between-struct-and-class-in-c
    which is basically stating what I already mentioned in the comment."
featured_image: 2012/05/CPP-thumb.png
---
I guess this article isn't very interesting, except if you have VERY little experience with C / C++. I only give some complete code examples. If you want some text, you could read <a href="http://en.wikibooks.org/wiki/C%2B%2B_Programming/Structures">C++ Programming/Structures</a> (a wikibook).

<h2>Point</h2>
<h3>Basic example</h3>
{% highlight cpp %}
#include <iostream>

using namespace std;

struct Point {
    double x;
    double y;
};

int main() {
    Point a = {12, 34};
    printf("(%.2f|%.2f)\n", a.x, a.y);
    return 0;
}
{% endhighlight %}

<h3>Functions</h3>
{% highlight cpp %}
#include <iostream>
#define ABS(a) (a < 0 ? -(a) : a)

using namespace std;

struct Point {
    double x;
    double y;
};

double getManhattanDistance(Point a, Point b) {
    return ABS(a.x-b.x) + ABS(a.y-b.y);
}

int main() {
    Point a = {1, 1};
    Point b = {3, -4};
    printf("(%.2f|%.2f)\n", a.x, a.y);
    printf("(%.2f|%.2f)\n", b.x, b.y);
    printf("Distance: %.2f\n", getManhattanDistance(a, b));
    return 0;
}
{% endhighlight %}

<h2>More stuff</h2>
<h3>Initialization</h3>
<code>Point a = {}</code> initializes all values of point to 0.

<h3>Constructors</h3>
You can write constructors for structs:

{% highlight cpp %}
#include <iostream>
#define ABS(a) (a < 0 ? -(a) : a)

using namespace std;

struct Point {
    double x;
    double y;

    Point():x(2.0),y(5.0) {}
    Point(double a, double b):x(9.0),y(9.0) {x=a; y=b;}
};

double getManhattanDistance(Point a, Point b) {
    return ABS(a.x-b.x) + ABS(a.y-b.y);
}

int main() {
    Point a = {};
    Point b = {3, -4};
    Point c;
    printf("(%.2f|%.2f)\n", a.x, a.y);
    printf("(%.2f|%.2f)\n", b.x, b.y);
    printf("(%.2f|%.2f)\n", c.x, c.y);
    printf("Distance: %.2f\n", getManhattanDistance(a, b));
    return 0;
}
{% endhighlight %}

Which gives:

{% highlight bash %}
./struct-example.out 
(2.00|5.00)
(3.00|-4.00)
(2.00|5.00)
Distance: 10.00
{% endhighlight %}

<h3>Functions in structs</h3>
You can also add functions to structs:

{% highlight cpp %}
#include <iostream>
#define ABS(a) (a < 0 ? -(a) : a)

using namespace std;

struct Point {
    double x;
    double y;

    Point():x(2.0),y(5.0) {}
    Point(double a, double b):x(9.0),y(9.0) {x=a; y=b;}

    double getZeroDist() {
        return ABS(x)+ABS(y);
    }
};

double getManhattanDistance(Point a, Point b) {
    return ABS(a.x-b.x) + ABS(a.y-b.y);
}

int main() {
    Point a = {3, -10};
    printf("(%.2f|%.2f)\n", a.x, a.y);
    printf("Distance: %.2f\n", a.getZeroDist());
    return 0;
}
{% endhighlight %}

Result:
{% highlight bash %}
./struct-example.out 
(3.00|-10.00)
Distance: 13.00
{% endhighlight %}

<h2>Read also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Struct_(C_programming_language)">struct (C programming language)</a></li>
  <li><a href="http://martin-thoma.com/c-operator-overloading/" title="C++ Operator overloading">Operator overloading</a></li>
  <li><a href="http://martin-thoma.com/a-practical-approach-to-floats/">A practical approach to floats</a>: An example for union</li>
  <li><a href="http://martin-thoma.com/how-do-hash-functions-work/">Connect four</a>: One usage example for structs</li>
</ul>

Is there anything interesting to say about structs?
