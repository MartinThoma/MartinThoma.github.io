---
layout: post
status: publish
published: true
title: Basic Multithreading in Java
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 56011
wordpress_url: http://martin-thoma.com/?p=56011
date: 2013-02-04 00:44:11.000000000 +01:00
categories:
- Code
tags:
- Bash
- Java
- Operating Systems
- Multithreading
comments: []
---
A lot of computing power is wasted in many programs as most programs use only one core. If your program is computation intensive, you might want to put some extra effort in your program and make use of this wasted computing power.

There are two ways to execute your code on multiple cores: Multiprocessing and multithreading. Both, processes and threads, provide the possibility to execute code sequences independently and concurrently. But where is the difference? 
<ul>
  <li>When you execute code in <strong>multiple processes</strong>, the operating system handles the scheduling. It decides when which process gets executed and tries to find an optimal order. Every process has its own memory segment. A process is sometimes also called "kernel level thread".</li>
  <li>When you execute code in <strong>multiple threads</strong>, all threads have one process they belong to (see <a href="http://eliezerciriaco.blogspot.de/2009/07/multi-threading-models.html">Multi-Threading models</a>, also from <a href="http://docs.oracle.com/cd/E19455-01/806-3461/6jck06gqk/index.html">Java</a>). Every set of threads that have the same process share their memory.</li>
</ul>

In Java, you will use multithreading most of the time. I will only write about multithreading, but you can create multiple processes wiht <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/ProcessBuilder.html">ProcessBuilder</a>.

<h2>Java Basics for Multithreading</h2>
All important lessons you need to learn are covered in <a href="http://docs.oracle.com/javase/tutorial/essential/concurrency/">Java Concurrency Tutorial</a>. If you're really interested in multithreading, you should read this.

You can put the part that can get executed concurrently in a separate class that implements the interface <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Runnable.html">Runnable</a>. This class has a method called run(). You can create a new <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#Thread(java.lang.Runnable)">Thread(Runnable)</a> by calling <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html#start()">start()</a>.

Here is an example:

<h2>Sum</h2>
{% highlight java %}public class Sum implements Runnable {
    private final int UpperEnd;

    public Sum(int upperEnd) {
        UpperEnd = upperEnd;
    }

    @Override
    public void run() {
        for (int i = 0; i < UpperEnd; i++) {
            RaceCondition.bigSum++;
        }
    }
}{% endhighlight %}

<h2>Main</h2>
{% highlight java %}import java.util.ArrayList;
import java.util.List;

public class Main {
    public static int BIG_NR;
    public static int NR_THREADS;
    public static long bigSum;

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("You should specify the number "
                    + "of threads and BIG_NR. Call me like this:\n"
                    + "java -jar RaceCondition.jar 5 20000\n"
                    + "This will create 5 Threads which try to count"
                    + "up to 2000000.\n" + "-v will show status "
                    + "information ");
            return;
        }

        boolean verbose = false;

        if (args.length > 2) {
            verbose = true;
        }

        NR_THREADS = Integer.parseInt(args[0]);
        BIG_NR = Integer.parseInt(args[1]);

        List<Thread> threads = new ArrayList<Thread>();
        for (int i = 0; i < NR_THREADS; i++) {
            Runnable task = new Sum(BIG_NR);
            Thread worker = new Thread(task);
            worker.start();
            threads.add(worker);
        }

        int running = 0;
        do {
            running = 0;
            for (Thread thread : threads) {
                if (thread.isAlive()) {
                    running++;
                }
            }

            if (verbose) {
                System.out.println("Remaining threads: " + running);
            }
        } while (running > 0);

        System.out.println(RaceCondition.bigSum);

    }
}{% endhighlight %}

Call it like this:
{% highlight bash %}java Main 5 2000{% endhighlight %}

<h2>Race Conditions</h2>
When you execute the code above, the output will vary. Why is this the case?

In short: The execution order is not defined and <code>RaceCondition.bigSum++</code> is not atomic.

Let's imagine that you call this with two threads only: 
<code>java Main 2 2000</code>

Now you could get this execution order:
<ul>
  <li>Thread 1: Loads <code>RaceCondition.bigSum</code>. It is 0.</li>
  <li>Thread 2: Executes completely. Now <code>RaceCondition.bigSum</code> is 2000</li>
  <li>Thread 1: Increases the loaded value of <code>RaceCondition.bigSum</code> by 1. Now it is 1.</li>
  <li>Thread 1: Finishes it's execution. The Value of <code>RaceCondition.bigSum</code> is 2000 = BIG_NR.</li>
</ul>

Ok, we can obviously get values in $[\text{BIG}\_\text{NR}, \text{NR}\_\text{THREADS} \cdot \text{BIG}\_\text{NR}]$.

Can we get smaller values? Yes, we can!

Execute:
{% highlight bash %}java Main 50 20000{% endhighlight %}

<ul>
  <li>Thread 1 loads <code>bigSum</code>. It's 0.</li>
  <li>Thread 2 loads <code>bigSum</code>. It's 0.</li>
  <li>Thread 3 - 50 execute completely.</li>
  <li>Thread 2 executes until it is at the latest <code>bigSum++</code>. The latest doesn't execute.</li>
  <li>Thread 1 increases the loaded value from 0 to 1 and writes 1 back</li>
  <li>Thread 2 loads <code>bigSum</code> = 1</li>
  <li>Thread 1 executes and finishes.</li>
  <li>Thread 2 increases the loaded value from 1 to 2 and writes 2 back.</li>
</ul>

You can get all values in $[2, \text{NR}\_\text{THREADS} \cdot \text{BIG}\_\text{NR}]$!

Usually, you don't want to get different results when you give the same input to your program. How can you fix this? Take a look at <a href="http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/atomic/AtomicLong.html">AtomicLong</a> and replace the <code>long bigNr</code> by the <code>AtomicLong bigNr</code>.

<h2>Playing with BASH</h2>
If you want to execute this more often, you could save it as a executable JAR and execute the following bash script. It takes three arguments: 
<ul>
  <li>$1: The number of times you execute a the program with a fixed number of THREADS</li>
  <li>$2: The maximum number of THREADS you would like to use</li>
  <li>$3: BIG_NR</li>
</ul>

The script executes the program $$1 \cdot $2$ times. The output gets divided by the number of threads and the result is saved in raceCondition.tmp. Every line is one execution of the program. When the second number is BIG_NR, then no race conditions occured.

{% highlight bash %}
rm raceCondition.tmp
touch raceCondition.tmp

# Up to $2 threads
for (( threads=1;threads<=$2; threads++))
do
    for (( c=1; c<=$1; c++ ))
    do
        # $threads threads, count up to $3 in each thread
        thisExecutionSum=`java -jar RaceCondition.jar $threads $3`
        # Normalize: thisExecutionSum / number of threads
        normalizedSum=`awk -vsome=$thisExecutionSum -vtotal=$threads 'BEGIN { printf("%d\n", some/total); exit } '`
        echo -e $threads"\t"$normalizedSum >> raceCondition.tmp
    done
done
{% endhighlight %}
