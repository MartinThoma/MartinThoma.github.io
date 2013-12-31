---
layout: post
title: Run Java Code fast
author: Martin Thoma
date: 2012-07-07 11:47:06
categories: 
- Code
tags: 
- Java
- JVM
featured_image: 2011/11/java-programming.png
---
<h2>Compile Java with GCJ</h2>
You can compile Java Code to a binary with GCJ. It works like this:
{% highlight bash %}gcj --main=Shell Shell.java{% endhighlight %}

If you get <code>gcj undefined reference to `main'</code> you didn't provide the (correct) <code>--main</code>.
If you get <code>exec 'ecj1': execvp</code>, you probably typed <code>gcc</code> instead of <code>gcj</code>.

It seems as if the binary (compiled with O3) was slower than using the normal Java Virtual Machine.

<h2>Different JVMs</h2>
A lot of different Java Virtual Machines do exist:
<ul>
  <li><a href="http://en.wikipedia.org/wiki/JamVM">JamVM</a>: </li>
</ul>


<h2>See also</h2>
<ul>
  <li><a href="http://gcc.gnu.org/java/compile.html">Compiling with GCJ</a></li>
  <li><a href="http://askubuntu.com/q/107278/10425">Changing JVM in Java</a></li>
  <li><a href="http://download.java.net/openjdk/jdk7/">Download OpenJDK 7</a></li>
  <li><a href="http://openjdk.java.net/groups/hotspot/">The HotSpot Group</a></li>
  <li><a href="http://nerds-central.blogspot.de/2009/09/tuning-jvm-for-unusual-uses-have-some.html">Tuning The JVM For Unusual Uses - Have Some Tricks Under Your Hat</a></li>
</ul>