---
layout: post
title: ! 'Java Puzzle #5: Parallel Programming, Part 2'
author: Martin Thoma
date: 2012-08-03 17:00:58.000000000 +02:00
category: Code
tags: Programming, Java, SWT I, puzzle
featured_image: 2012/07/java-thumb.png
---
What is the output of the following script:

```java
public class test {
    public static int globalVar;

    public static void main(String[] args) {
        globalVar = 1;

        MyParallelClass a = new MyParallelClass();
        MyParallelClass b = new MyParallelClass();

        new Thread(a).start();
        new Thread(b).start();

        System.out.println(globalVar);
    }
}
```

```java
public class MyParallelClass implements java.lang.Runnable {
    public int counter = 0;

    @Override
    public void run() {
        if (test.globalVar > 0) {
            for (int i = 0; i < 1000000; i++) {
                counter++;
            }
            test.globalVar--;
        }
    }
}
```

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
<code>0</code>, <code>1</code> or <code>-1</code>.

<h2>Explanaition</h2>
First the simple ones:
<code>0</code> is the result you would expect. One thread executes and reduces <code>globalVar</code> to <code>0</code>, the other one does nothing and then <code>globalVar</code> gets printed.

If the main program is faster than any of the two threads, it prints <code>1</code> before <code>globalVar</code> gets reduced.

Now the most interesting one: <code>-1</code>. This is called a <a href="http://en.wikipedia.org/wiki/Race_condition">race condition</a>. You have to know that <code>globalVar--</code> is not an atomic operation. First you have to get the value, then you have to reduce it and after that you can save the value.

This is an order of execution which would lead to a wrong value:
<table>
<tr>
<th>First Thread</th>
<th>Second Thread</th>
<th>test.globalVar</th>
</tr>
<tr>
<td>```text
checks if (globalVar > 0)
looping ... 
looping ... 
execute test.globalVar--;
```</td>
<td>```text
.
checks if (globalVar > 0)
execute all four bytecode commands of "test.globalVar--;"
.
```</td>
<td>```text
1
1
0
-1
```</td>
</tr>
</table>

<h2>Resolve this problem</h2>
<ul>
  <li>Use <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#join()">join()</a> if you don't want to get <code>1</code> as output.</li>
  <li>If you don't want to get <code>-1</code>, you should take a look at the keyword <a href="http://docs.oracle.com/javase/tutorial/essential/concurrency/locksync.html">synchronised</a>.</li>
</ul>

<h2>A side note</h2>
With <code>javap -c MyParallelClass</code> you can view the <a href="http://en.wikipedia.org/wiki/Java_bytecode">bytecode</a> of the class <code>MyParallelClass</code>. It looks like this:
```java

Compiled from "MyParallelClass.java"
public class MyParallelClass extends java.lang.Object 
                        implements java.lang.Runnable{
public int counter;

public MyParallelClass();
  Code:
   0:	aload_0
   1:	invokespecial	#1; //Method java/lang/Object."<init>":()V
   4:	aload_0
   5:	iconst_0
   6:	putfield	#2; //Field counter:I
   9:	return

public void run();
  Code:
   0:	getstatic	#3; //Field test.globalVar:I
   3:	ifle	38
   6:	iconst_0
   7:	istore_1
   8:	iload_1
   9:	ldc	#4; //int 1000000
   11:	if_icmpge	30
   14:	aload_0
   15:	dup
   16:	getfield	#2; //Field counter:I
   19:	iconst_1
   20:	iadd
   21:	putfield	#2; //Field counter:I
   24:	iinc	1, 1
   27:	goto	8
   30:	getstatic	#3; //Field test.globalVar:I
   33:	iconst_1
   34:	isub
   35:	putstatic	#3; //Field test.globalVar:I
   38:	return

}
```

Some links to the reference: <a href="https://www.vmth.ucdavis.edu/incoming/Jasmin/ref--19.html">getstatic</a>, <a href="https://www.vmth.ucdavis.edu/incoming/Jasmin/ref--21.html">iconst_1</a>, <a href="https://www.vmth.ucdavis.edu/incoming/Jasmin/ref-_isub.html">isub</a>, <a href="https://www.vmth.ucdavis.edu/incoming/Jasmin/ref-putstati.html">putstatic</a>

The interesting part of the bytecode is:
```java
   30:	getstatic	#3; //Field test.globalVar:I
   33:	iconst_1
   34:	isub
   35:	putstatic	#3; //Field test.globalVar:I

```
You can see that the JVM has to execute 4 commands for <code>test.globalVar--;</code>. 

<h2>See also</h2>
<ul>
  <li><a href="http://docs.oracle.com/javase/tutorial/essential/concurrency/atomic.html">Atomic Access</a> in Java</li>
  <li><a href="http://docs.oracle.com/javase/7/docs/api/javax/management/monitor/Monitor.html">Class Monitor</a></li>
  <li><a href="http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html#jvms-6.5.monitorenter">monitorenter</a> and <a href="http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html#jvms-6.5.monitorexit">monitorexit</a></li>
  <li><a href="http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/package-summary.html">Package java.util.concurrent</a></li>
</ul>
