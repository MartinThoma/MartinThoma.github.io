---
layout: post
status: publish
published: true
title: Profiling C programs
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 49681
wordpress_url: http://martin-thoma.com/?p=49681
date: 2012-12-01 17:00:58.000000000 +01:00
categories:
- Code
tags:
- C
- profiling
comments: []
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
[caption id="attachment_49691" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/11/call-graph2.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/11/call-graph2.png" alt="Call graph of connect four game graph creation program" title="Call graph of connect four game graph creation program" width="512" height="601" class="size-full wp-image-49691" /></a> Call graph of connect four game graph creation program[/caption]

Just take a look at it by yourself. You will see much more than I could tell you now.
