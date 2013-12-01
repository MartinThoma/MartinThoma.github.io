---
layout: post
status: publish
published: true
title: Linux Memory Consumption
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 13581
wordpress_url: http://martin-thoma.com/?p=13581
date: 2012-02-10 21:04:45.000000000 +01:00
categories:
- Code
tags:
- Linux
- Command Line
- Memory
comments: []
featured_image: 2011/09/Tux.png
---
<h2>free</h2>
I've you want to check your memory consumption on a Linux machine, you can use free.
{% highlight bash %}moose@pc07:~$ free -m
             total       used       free     shared    buffers     cached
Mem:          3952       2832       1119          0        117       1565
-/+ buffers/cache:       1150       2802
Swap:         8656          0       8656
{% endhighlight %}
This means: I have a total of 3952 MB <a href="http://en.wikipedia.org/wiki/Random-access_memory">RAM</a>, used and free should be clear, shared is memory which is shared between processes, e.g. shared libraries. The "buffers" entry tells you how much of your RAM is being used for disk buffering. Over 8 GB got swapped out.

<h2>top</h2>
top will give you something like Windows' task manager in the command line. If you press "M" it gets sorted by memory utilization:

[caption id="attachment_13591" align="aligncenter" width="500" caption="top sorted by memory utilization"]<a href="http://martin-thoma.com/wp-content/uploads/2012/02/top-memory.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/02/top-memory.png" alt="top sorted by memory utilization" title="top sorted by memory utilization" width="500" height="497" class="size-full wp-image-13591" /></a>[/caption]

<h2>pmap</h2>
pmap reports a memory map of a process. Lets make an example. Eclipse has the process ID (pid) 4526 at the moment.
{% highlight bash %}pmap 4526{% endhighlight %}
gives the following output:
{% highlight bash %}4526:   /usr/lib/eclipse/eclipse
Address   Kbytes Mode  Offset           Device    Mapping
08048000      16 r-x-- 0000000000000000 008:00001 eclipse
0804c000       4 r