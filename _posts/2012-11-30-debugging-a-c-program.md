---
layout: post
title: Debugging a C program
author: Martin Thoma
date: 2012-11-30 17:00:15.000000000 +01:00
category: Code
tags: C, debug, valgrind, gdb
---
As I began with programming C, I had enormous difficulties to produce working code. Most of the time it didn't even compile, but when it compiled and I got a runtime error, I basically read my whole code again. I <strike>didn't</strike> don't know any good online resource for C, so I've always searched with Google for answers to questions that I couldn't properly formulate. One question that is important for beginners is <a href="http://stackoverflow.com/q/12949290/562769">How do I find missing C header files (without Internet)?</a> and another one might be: How can I debug my programs?

<h2>Compile time vs. runtime</h2>
A typical C workflow looks like this: You have an idea, you write your code, you compile it and you run it.
{% caption align="aligncenter" width="512" caption="C workflow" url="../images/2012/11/c-workflow.png" alt="C workflow"  height="229" class="size-full wp-image-49641" %}

You might make multiple errors. Simple typos or syntax errors are almost always detected at compile time. They are called "compile time errors". Others, like the access of an array-index that isn't in the array might only occur sometimes at runtime, depending on the input. Those are runtime errors and they are much more difficult to detect. Additionally, they can not be reproduced that easily as compile time errors can.

<h2>gdb</h2>
If you want to find runtime errors, you should deactivate all optimization flags and add debugging symbols. A gcc call might look like this:

{% highlight bash %}gcc mySourceFile.c -g{% endhighlight %}

This produces a binary file called "a.out".

Now should run gdb - GNU debug:
{% highlight bash %}gdb ./a.out{% endhighlight %}

Within the command line program GNU debug you have to enter:
{% highlight bash %}run ./a.out{% endhighlight %}

You should now be able to see the line in which the runtime-error occurs.

<h2>valgrind</h2>
You might want to give valgrind a try.

<em>Uninitialised value was created by a stack allocation at 0x80488BC</em>: This could mean that you used an uninitialized variable. Check your variable initializations from the given point. Add <code>--track-origins=yes</code and run valgrind again.
