---
layout: post
title: What does volatile mean?
slug: what-does-volatile-mean
lang: en
author: Martin Thoma
date: 2013-03-20 22:19:41.000000000 +01:00
category: Code
tags: C, Java
featured_image: 2012/05/C.png
---
You might have read the variable modifier <code>volatile</code> in C, C++ or in Java. But do you know what it means?

<h2>C Programming Language</h2>
The C Programming language by Kernighan and Ritchie (second edition) contains this keyword only 13 times. Here are the most important ones:
<blockquote>[...] declaring it volatile announces that it has special properties relevant to optimization. Neither qualifier affects the range of values or arithmetic properties of the object. Qualifiers are discussed in Par.A.8.2.</blockquote>
Page 158

<blockquote>The purpose of volatile is to force an implementation to suppress optimization that could otherwise occur. For example, for a machine with memory-mapped input/output, a pointer to a device register might be declared as a pointer to volatile, in order to prevent the compiler from removing apparently redundant references through the pointer. Except that it should diagnose explicit attempts to change const objects, a compiler may ignore these qualifiers.</blockquote>
Page 172

<h2>Java</h2>
Java Language Specification actually covers this quite good:

<blockquote>The Java programming language allows threads to access shared variables (&sect;17.1).
As a rule, to ensure that shared variables are consistently and reliably updated, a thread should ensure that it has exclusive use of such variables by obtaining a lock that, conventionally, enforces mutual exclusion for those shared variables.

The Java programming language provides a second mechanism, volatile fields, that is more convenient than locking for some purposes.

A field may be declared volatile, in which case the Java Memory Model ensures that all threads see a consistent value for the variable (&sect;17.4).</blockquote>

Ok, so in Java it is important for multithreading. The example 8.3.1.4-1 of the <a href="http://docs.oracle.com/javase/specs/">JLS 7.0</a> is also very interesting.

<blockquote>A write to a volatile field (&sect;8.3.1.4) happens-before every subsequent read of
that field.</blockquote>

<blockquote>For the purposes of the Java programming language memory model, a single write to a non-volatile long or double value is treated as two separate writes: one to each 32-bit half. This can result in a situation where a thread sees the first 32 bits of a 64-bit value from one write, and the second 32 bits from another write. Writes and reads of volatile long and double values are always atomic.</blockquote>

<h2>When do you need volatile?</h2>
In C and C++, `volatile` tells the compiler that a variable can change, or is read,
in ways it cannot see in the code. So the compiler must do every read and every
write exactly as written: it may not keep the value in a CPU register, merge
accesses or drop them. That is all `volatile` does. It does not bypass the CPU
cache, and it does not make an access atomic.

<h3>Thermometer</h3>
Imagine you want to build your own thermometer. The sensor puts the current
temperature into a device register that is mapped to a memory address. You want
to print the temperature periodically:

```c
#include <stdint.h>
#include <stdio.h>
#include <unistd.h>

/* The address of the sensor's register depends on the hardware. */
#define TEMPERATURE_REGISTER ((volatile int32_t *)0x40001000)

int main(void) {
    for (int i = 0; i < 60; i++) {
        int32_t temperature = *TEMPERATURE_REGISTER;
        printf("Temperature: %d °C\n", (int)temperature);
        sleep(2);
    }
    return 0;
}
```

Your program never writes to this address; the hardware does. Without `volatile`,
the compiler may assume that memory only changes when the program writes to it,
and reuse a value it has already read instead of reading the register again.
`volatile` forbids that: every `*TEMPERATURE_REGISTER` really reads the register.

<h3>I / O</h3>
Imagine you write an application that wants to transfer data from a disk to another disk. You might have one producer and one consumer. The producer tries to get data from the disk. Lets say the disk has a buffer and a register that indicates how many blocks are in the buffer. So your producer might poll at some point:

```c
volatile uint32_t *blocks_ready = (volatile uint32_t *)0x40002000;

while (*blocks_ready == 0) {
    /* wait until the device has data */
}
```

Nothing in the loop changes `*blocks_ready`. Without `volatile`, the compiler may
read it once and turn the loop into `while (1);` if the value was 0. Then you
would never notice when you can read from the disk.

<h3>Signal handlers: an example you can run</h3>
A variable that a signal handler changes is a case you can try on any Linux
machine:

```c
#include <signal.h>
#include <stdio.h>

static volatile sig_atomic_t stop = 0;

static void handle_sigint(int sig) {
    (void)sig;
    stop = 1;
}

int main(void) {
    signal(SIGINT, handle_sigint);
    unsigned long n = 0;
    while (!stop) {
        n++;
    }
    printf("Stopped after %lu iterations\n", n);
    return 0;
}
```

Compile it with `gcc -O2 stop.c` and press Ctrl+C: the handler sets `stop` and the
loop ends. Now remove `volatile` and compile again: the program no longer stops
on Ctrl+C. GCC reads `stop` once before the loop and then jumps in an endless loop,
because nothing inside the loop changes `stop` (tested with GCC 13.3). A variable
that a signal handler writes should have the type `volatile sig_atomic_t`.

The C standard names one more case: a local variable that is changed between
`setjmp` and `longjmp` only has a defined value after the `longjmp` if it is
`volatile`.

<h3>Not for threads in C and C++</h3>
Here C and C++ differ from Java. In Java, `volatile` makes a write visible to
other threads and orders it (happens-before, see above). In C and C++, `volatile`
gives no such guarantee: accesses are neither atomic nor ordered between threads.
For data that threads share, use atomics (`<stdatomic.h>` in C11,
`std::atomic` in C++11) or a mutex.

<h2>Further reading</h2>
<ul>
  <li><a href="http://stackoverflow.com/q/3488703/562769">When exactly do you use the volatile keyword in Java?</a></li>
  <li><a href="http://stackoverflow.com/a/3430809/562769">Different meaning in Java and C#</a></li>
</ul>
