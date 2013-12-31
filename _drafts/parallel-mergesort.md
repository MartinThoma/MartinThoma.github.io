---
layout: post
title: Parallel Mergesort
author: Martin Thoma
date: 2013-03-05 05:23:42
categories: 
- Code
tags: 
- Big Data
- concurrency
- Java
- parallel programming
- Python
featured_image: 2012/07/java-thumb.png
---
Before we start sorting huge amounts of numbers in parallel, we have to generate some numbers.

<h2>Generate numbers</h2>
I'll do the number generation in Python aka executable pseudocode:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

def generateNumbers(min=-1000, max=1000, n=1000000):
    f = open('numbers.txt', 'wb')
    for i in xrange(n):
        f.write(str(randint(min,1000)) + &quot;\n&quot;)
    f.close()

if __name__ == &quot;__main__&quot;:
    from argparse import ArgumentParser
     
    parser = ArgumentParser()
     
    # Add more options if you like
    parser.add_argument(&quot;-f&quot;, &quot;--file&quot;, dest=&quot;myFilenameVariable&quot;,
                      help=&quot;write report to FILE&quot;, metavar=&quot;FILE&quot;)
    parser.add_argument(&quot;-n&quot;, metavar='N', type=int, dest=&quot;n&quot;, 
                        default=1000000, help=&quot;The number of &quot;
                        + &quot;numbers you want to generate.&quot;)
    parser.add_argument(&quot;-min&quot;, metavar='N', type=int, dest=&quot;min&quot;, 
                        default=-1000, help=&quot;The minimum number &quot;
                        + &quot;that might get generated.&quot;)
    parser.add_argument(&quot;-max&quot;, metavar='N', type=int, dest=&quot;max&quot;, 
                        default=1000, help=&quot;The maximum number that &quot;
                        + &quot;might get generated.&quot;)
    args = parser.parse_args()
    print(&quot;Started generating&quot;)
    generateNumbers(args.min, args.max, args.n)
    print(&quot;Generating %i numbers finished&quot; % args.n){% endhighlight %}

I generated 100,000,000 numbers (this is a 418.8 MB file!).

<h2>The trivial approach</h2>
When I try to solve a problem, I always try the trivial things first. In this case, this means:
<ul>
  <li>Read the file with a <a href="http://docs.oracle.com/javase/7/docs/api/java/io/BufferedReader.html">BufferedReader</a>.</li>
  <li>Store numbers in a <a href="http://docs.oracle.com/javase/7/docs/api/java/util/List.html">List</a> (<a href="http://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html">ArrayList</a>).</li>
  <li>Sort them with <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Collections.html#sort(java.util.List)">Collections.sort</a></li>
  <li>Write the numbers with a <a href="http://docs.oracle.com/javase/7/docs/api/java/io/FileWriter.html">FileWriter</a></li>
</ul>

<h3>Initial problems</h3>
I've implemented this approach and added the executable to Github.
You can call it like this:
{% highlight bash %}java -jar Sort.jar -i numbers.txt -o outputsorted.txt{% endhighlight %}

This time, I got some unexpected problem:
{% highlight bash %}Read numbers
Not enough heap space.
Got 38647475 numbers.
java.lang.OutOfMemoryError: Java heap space
Exception in thread &quot;main&quot; java.lang.reflect.InvocationTargetException
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:616)
	at org.eclipse.jdt.internal.jarinjarloader.JarRsrcLoader.main(JarRsrcLoader.java:56){% endhighlight %}

Seems as ArrayList can only store 38,647,475 numbers. 

I also tried LinkedList, but it only stored 21,267,753 numbers and aborted after 3m14.704s - ArrayList only needed about a minute. This makes sense, as LinkedList needs more memory than ArrayList. Interestingly, this number differs. In a second execution it were 21,267,754 numbers.

Ok, let's increase the heap size:
{% highlight bash %}java -Xms2500m -Xmx2500m -jar Sort.jar -i numbers.txt -o outputsorted.txt{% endhighlight %}
2 GB was not enough for ArrayList. It could only store 86,956,820 numbers. We get closer. How much space do we need at minimum? $(\text{number of numbers}) \cdot (\text{size of one number}) = 32 \text{bit } \cdot 100,000,000 = 4 Byte \cdot 100,000,000 = 400 MB$. 

<h3>Use an array</h3>
Hmm ... ok, lets make it more efficient and use an array.

{% highlight bash %}moose@pc07:~$ time java -jar Sort.jar -i numbers.txt -o outputsorted.txt
Version 1.0.3
Read numbers
Needed 18.015201115 seconds for reading
Needed 10.138167991 seconds for sorting
Write numbers
Needed 26.830255831 seconds for writing
Finished

real	0m55.276s
user	0m50.131s
sys	0m2.868s{% endhighlight %}

It works :-)

<h2>The Task</h2>
Ok, the sorting process is too fast in my opinion. You might not see any improvement. So I have to get a bigger file to sort.

I will generate a file with 1,000,000,000 numbers. This means, only the numbers will add up to a size of 4 GB. As I store them as a text file in UTF-8, one character needs 1 Byte. So one line could have len("-1000\n") = 6 characters. We have 1,000,000,000 lines. This means we need $1 \frac{\text{byte}}{\text{character}} \cdot 6 \frac{\text{characters}}{\text{lines}} \cdot 1000000000 \text{ lines} = 6 GB$.

After 56 minutes Python got only 839,724,246 numbers. So I did the same in C++ which needed only 3m34.717s to generate the file with 1,000,000,000 numbers. Amazing.

This file needs $4,391,810,004 \text{ bytes} = 4.1 \text{ GB}$

<h2>Workflow for Big Data</h2>

<h2>Related pages</h2>
http://stackoverflow.com/questions/1062113/fastest-way-to-write-huge-data-in-text-file-java
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=sorting
https://plus.google.com/u/0/114317830537891572122/posts/KNE1a4GRDJb?cfem=1
http://stackoverflow.com/questions/tagged/external-sorting
https://code.google.com/p/externalsortinginjava/
http://stackoverflow.com/questions/7918060/how-do-i-sort-very-large-files
http://docs.oracle.com/javase/7/docs/api/java/nio/channels/FileChannel.html