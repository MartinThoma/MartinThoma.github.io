---
layout: post
title: Fibonacci, recursion and decorators
author: Martin Thoma
date: 2013-10-31 11:08:01.000000000 +01:00
categories:
- Code
tags:
- Python
- Fibonacci
- decorators
featured_image: 2011/09/Python-Logo.png
---
I think everybody who learned something about recursion has seen the Fibonacci sequence:

$
f(n) := \begin{cases}
n               &\text{if } n \leq 1\\
f(n-1) + f(n-2) &\text{otherwise}
\end{cases}
$

The simplest solution to get this number is:

{% highlight python %}
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
{% endhighlight %}

The problem is, of course, that the number of evaluations goes wild. Here is a table of the number of function calls

<table>
<tr>
  <th>n</th>
  <td>0</td>
  <td>1</td>
  <td>2</td>
  <td>3</td>
  <td>4</td>
  <td>5</td>
  <td>6</td>
  <td>7</td>
  <td>8</td>
  <td>9</td>
  <td>10</td>
  <td>20</td>
</tr>
<tr>
  <th>calls</th>
  <td>1</td>
  <td>1</td>
  <td>3</td>
  <td>5</td>
  <td>9</td>
  <td>15</td>
  <td>25</td>
  <td>41</td>
  <td>67</td>
  <td>109</td>
  <td>177</td>
  <td>21891</td>
</tr>
</table>

To be exact, the number of calls of the fib-function is:

$
f(n) := \begin{cases}
1               &\text{if } n \leq 1\\
f(n-1) + f(n-2) + 1 &\text{otherwise}
\end{cases}
$

This means the dumb function is in $\mathcal{O}(2^n)$! (I'm not quite sure, but this I think this is not only time complexity, but also space complexity. I think it is not <a href="https://en.wikipedia.org/wiki/Tail_recursion">tail recursive</a>, so the complete stackframe has to be saved.)

<h2>Memorization with decorators</h2>
One way to solve the problem much faster (in fact in $\mathcal{O}(n)$ time and space complexity) by storing values we already calculated.

A very neat way to achieve this are decorators. It might be a common problem that you have a recursive, mathematical function with no side effects. So you can write a wrapper that checks if the value has already been calculated. If not, the function proceeds as usual. It it has already been calculated, you can simply look it up:

{% highlight python %}
def memoize(obj):
    cache = {}

    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
{% endhighlight %}

Notice that I've only added <code>@memoize</code> over the function definiton of <code>fib</code>! I love Python ☺

By the way, this formula has also some limitations. Python has a fixed maximum recursion depth. So <code>fib(332)</code> worked fine, but <code>fib(333)</code> gave:
{% highlight bash %}
RuntimeError: maximum recursion depth exceeded in comparison
{% endhighlight %}

You can get around this limitation by successive calls of fib:

{% highlight python %}
# Call to fill array
fib(332)

# The number of recursive steps is now much smaller:
print(fib(500))
{% endhighlight %}

That gave 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125. A pretty big number.

<h2>Formula of Moivre-Binet</h2>
The formula of Moivre-Binet gives a closed form for calculating fibonacci numbers:

$\varphi = \frac{\sqrt{5}+1}{2}$
$\psi = 1 - \varphi$
$f(n) = \frac{\varphi^n - \psi^n}{\phi - \psi}$

Although this is mathematically exact, it will not work on computers due to a fixed floating point precision. Lets check how long it works:

{% highlight python %}
#!/usr/bin/env python

import functools
def memoize(obj):
    cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def moivreBinet(n):
    phi = (5**0.5+1)/2
    psi = 1 - phi
    return int((phi**n - psi**n)/(phi - psi))

from itertools import count
for i in count(0):
    exact = fib(i)
    constTime = moivreBinet(i)
    if exact != constTime:
        print(("The %i-th fibonacci number is %i. Moivre-Binet "
             + "gives due to precicion error %i (delta=%i).") 
                 % (i, exact, constTime, abs(exact-constTime)))
        break
{% endhighlight %}

So the answer is:

<blockquote>The 72-th fibonacci number is 498454011879264. Moivre-Binet gives due to precicion error 498454011879265 (delta=1).</blockquote>

This is a reason to prefer the $\mathcal{O}(n)$ solution over the $\mathcal{O}(1)$ solution. If you're only exact for 72 numbers, you could also simply store them. Looking number up form an array is always faster than any calculation.

<h2>Very high numbers</h2>
The following solution is fast and works 0.075 seconds for the 20000 Fibonacci number (which has 4180 digits).

{% highlight python %}
def fib(n):
    def accFib(n, Nm2=0, Nm1=1):
        for i in range(n):
            Nm2, Nm1 = Nm1, Nm1+Nm2
        return Nm2   
    return accFib(n)
{% endhighlight %}

<h2>Additional ressources</h2>
The article on <a href="http://en.literateprograms.org/Fibonacci_numbers_(Python)">literate programs</a> is worth reading. They show some very different programs that calculate Fibonacci numbers.
