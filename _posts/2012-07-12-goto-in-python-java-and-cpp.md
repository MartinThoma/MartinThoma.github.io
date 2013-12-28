---
layout: post
title: GOTO in Python, Java and C++
author: Martin Thoma
date: 2012-07-12 22:04:01.000000000 +02:00
categories:
- Code
tags:
- Python
- C
- Java
- GOTO
featured_image: 2012/05/CPP-thumb.png
---
<a href="http://en.wikipedia.org/wiki/Goto">GOTO</a> is a statement of the early beginnings of programming. It is rarely used in high-level code today. Code that makes use of it is called <a href="http://en.wikipedia.org/wiki/Spaghetti_code">Spaghetti code</a> by some people. I have almost never seen goto statements in code, so I've been curious about them.

{% caption align="aligncenter" width="533" caption="GOTO from xkcd.com" url="../images/2012/07/xkcd-goto.png" alt="GOTO from xkcd.com" title="" height="145" class=" wp-image-30341  " title="GOTO from xkcd.com" %}

<h2>Python</h2>
Python does NOT offer GOTO. However, somebody made a GOTO module for April Fools' Day. See <a href="http://stackoverflow.com/q/6959360/562769">`goto` in Python</a> if you're still interested.

<h2>Java</h2>
<blockquote>Java has no goto statement. Studies illustrated that goto is (mis)used more often than not simply "because it's there". Eliminating goto led to a simplification of the language--there are no rules about the effects of a goto into the middle of a for statement, for example. Studies on approximately 100,000 lines of C code determined that roughly 90 percent of the goto statements were used purely to obtain the effect of breaking out of nested loops. As mentioned above, multi-level break and continue remove most of the need for goto statements.</blockquote>
Source: <a href="http://java.sun.com/docs/white/langenv/Simple.doc2.html#5550">java.sun.com</a>


<h2>C++</h2>
GOTO works in C++. Here is a minimal example:

<h3>Minimal Example</h3>
{% highlight cpp %}#include <iostream>

using namespace std;

int main(){
    int test = 0;

    start:;
    if (test > 10) {
        goto end;
    } else {
        test += 7;
        goto start;
    }

    end:;

    cout << "test: " << test << endl;

    return 0;
}{% endhighlight %}

Output:
{% highlight bash %}test: 14{% endhighlight %}

<h3>Euclidean GCD algorithm</h3>
Most of you might know the <a href="http://en.wikipedia.org/wiki/Euclidean_algorithm">euclidean algorithm</a> for calculating the greatest common divisor in a version like this one:
{% highlight cpp %}#include <iostream>

using namespace std;

int euclidGCD(int a, int b) {
    while (b != 0) {
        int m = a % b;
        a = b;
        b = m;
    }
    return a;
}

int main(){
    // Outputs 20
    cout << "GCD of 340 and 32760: " << euclidGCD(340, 32760) <<endl;

    return 0;
}{% endhighlight %}

Here is a goto-version that works perfectly fine:
{% highlight cpp %}#include <iostream>

using namespace std;

int euclidGCD(int a, int b) {
    if (b > a) goto b_larger;
    while (1) {
        a = a % b;
        if (a == 0) return b;

        b_larger:
        b = b % a;
        if (b == 0) return a;
    }
}

int main(){
    cout << "GCD of 340 and 32760: " << euclidGCD(340, 32760) <<endl;

    return 0;
}{% endhighlight %}
Source: <a href="http://en.literateprograms.org/Euclidean_algorithm_(C)">literateprograms.org</a>

<h3>Try bad things</h3>
You can't jump into a function:
{% highlight cpp %}#include <iostream>

using namespace std;

int myFunction(int i) {
    i += 1;
    inFunctionLabel:;
    i += 1;
    return i;
}

int main(){
    int test = 0;

    goto inFunctionLabel;

    cout << "test: " << test << endl;

    return 0;
}{% endhighlight %}

Compiler error:
{% highlight bash %}gotoExample.cpp: In function &lsquo;int myFunction(int)&rsquo;:
gotoExample.cpp:7: warning: label &lsquo;inFunctionLabel&rsquo; defined but not used
gotoExample.cpp: In function &lsquo;int main()&rsquo;:
gotoExample.cpp:15: error: label &lsquo;inFunctionLabel&rsquo; used but not defined{% endhighlight %}

So goto is at least bound to its scope.
