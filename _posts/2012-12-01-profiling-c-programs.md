---
layout: post
title: Profiling C programs
author: Martin Thoma
date: 2012-12-01 17:00:58.000000000 +01:00
categories:
- Code
tags:
- C
- profiling
featured_image: 2012/12/call-graph-thumb.png
---
If you have a working program and you want to improve its execution speed, you might want to profile it. An easy way to do so, is adding global variables, increasing them at interesting points and counting how often these points are executed. A more sophisticated way is using a profiler.

<h2>valgrind and kcachegrind</h2>
Install valgrind and kcachegrind. For Ubuntu users:
{% highlight bash %}sudo apt-get install valgrind kcachegrind{% endhighlight %}

Create a profile:
{% highlight bash %}valgrind --tool=callgrind ./connectfour{% endhighlight %}
(I've profiled a connect four application. Replace that with your application)
This command will create a file called similar to "callgrind.out.4846".

Take a look at the profile:
{% highlight bash %}kcachegrind callgrind.out.4846{% endhighlight %}

You can also create a call-graph:
{% caption align="aligncenter" width="512" caption="Call graph of connect four game graph creation program" url="../images/2012/11/call-graph2.png" alt="Call graph of connect four game graph creation program"  height="601" class="size-full wp-image-49691" %}

Just take a look at it by yourself. You will see much more than I could tell you now.
