---
layout: post
title: ! 'Java Puzzle #4: Parallel Programming'
author: Martin Thoma
date: 2012-08-02 11:00:36.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- SWT I
- puzzle
featured_image: 2012/07/java-thumb.png
---
What is the output of the following Java Snippet:

{% highlight java %}public class MyParallelClass implements java.lang.Runnable {
    public String name;

    public myParallelTry(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println(name);
    }
}{% endhighlight %}

{% highlight java %}public class test {
    public static void main(String[] args) {
        MyParallelClass a = new MyParallelClass("A");
        MyParallelClass b = new MyParallelClass("B");
        MyParallelClass c = new MyParallelClass("C");
        MyParallelClass d = new MyParallelClass("D");

        new Thread(a).start();
        new Thread(b).start();
        new Thread(c).start();
        new Thread(d).start();
        System.out.println("-");
        new Thread(a).start();
        new Thread(b).start();
        new Thread(c).start();
        new Thread(d).start();
        System.out.println("-");
        new Thread(a).start();
        new Thread(b).start();
        new Thread(c).start();
        new Thread(d).start();
        System.out.println("-");
        new Thread(a).start();
        new Thread(b).start();
        new Thread(c).start();
        new Thread(d).start();
    }
}{% endhighlight %}

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
.
.
.
.
.
.


<h2>Answer</h2>
<table>
<tr>
<th>First Try</th>
<th>Second Try</th>
<th>Third Try</th>
</tr>
<tr>
<td>{% highlight text %}A
C
B
-
D
A
B
C
-
D
A
-
C
A
C
D
B
B
D
{% endhighlight %}</td>
<td>{% highlight text %}A
B
C
-
D
A
B
C
-
D
A
B
C
-
D
A
B
C
D
{% endhighlight %}</td>
<td>{% highlight text %}A
B
C
-
D
A
B
C
-
D
A
B
C
-
D
A
B
C
D
{% endhighlight %}</td>
</tr>
</table>

<h2>Explanation</h2>
If you start threads like this, you don't get any guarantee that they will finish their execution in order. If you want them to execute in block of four, you could use <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#join()">join()</a>:

{% highlight java %}public class test {
    public static void main(String[] args) {
        myParallelTry a = new myParallelTry("A");
        myParallelTry b = new myParallelTry("B");
        myParallelTry c = new myParallelTry("C");
        myParallelTry d = new myParallelTry("D");

        Thread tA = new Thread(a); tA.start();
        Thread tB = new Thread(b); tB.start();
        Thread tC = new Thread(c); tC.start();
        Thread tD = new Thread(d); tD.start();
        try {
            tA.join();
            tB.join();
            tC.join();
            tD.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("-");
        tA = new Thread(a); tA.start();
        tB = new Thread(b); tB.start();
        tC = new Thread(c); tC.start();
        tD = new Thread(d); tD.start();
        try {
            tA.join();
            tB.join();
            tC.join();
            tD.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("-");
        tA = new Thread(a); tA.start();
        tB = new Thread(b); tB.start();
        tC = new Thread(c); tC.start();
        tD = new Thread(d); tD.start();
        try {
            tA.join();
            tB.join();
            tC.join();
            tD.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("-");
        tA = new Thread(a); tA.start();
        tB = new Thread(b); tB.start();
        tC = new Thread(c); tC.start();
        tD = new Thread(d); tD.start();
        try {
            tA.join();
            tB.join();
            tC.join();
            tD.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}{% endhighlight %}

<table>
<tr>
<th>First Try</th>
<th>Second Try</th>
<th>Third Try</th>
</tr>
<tr>
<td>{% highlight text %}A
B
D
C
-
A
B
C
D
-
A
B
C
D
-
A
B
C
D
{% endhighlight %}</td>
<td>{% highlight text %}A
B
C
D
-
A
B
C
D
-
A
B
C
D
-
A
B
C
D{% endhighlight %}</td>
<td>{% highlight text %}A
B
C
D
-
A
B
C
D
-
A
B
C
D
-
A
B
C
D{% endhighlight %}</td>
</tr>
</table>
