---
layout: post
status: publish
published: true
title: What does volatile mean?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 62281
wordpress_url: http://martin-thoma.com/?p=62281
date: 2013-03-20 22:19:41.000000000 +01:00
categories:
- Code
tags:
- C
- Java
comments: []
---
You might have read the variable modifier <code>volatile</code> in C, C++ or in Java. But do you know what it means?

<h2>C Programming Language</h2>
The C Programming language by Kerninghan and Ritchie (second edition) contains this keyword only 13 times. Here are the most important ones:
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

<h2>When do you need it volatile?</h2>
<div class="warning">I'm not sure if it is correct what I write here. It makes sense, but please leave a note in comments when I'm wrong.</div>

<h3>Thermometer</h3>
Imagine you want to build your own thermometer. So you have to access hardware. Now you only want to print the temperature periodically. Something like this:

[c]
#include <stdio.h>
#include <unistd.h>

int getTemperature() {
	// accessing the hardware device register happens here
	return 42;
}

int main() {
	for (int i=0; i<60; i++) {
                int temperature = getTemperature();
		printf("Temperature: %i &deg;C\n", temperature);
		sleep(2);
	}

	return 0;
}[/c]

Now, as you always access the same register and you don't change it, the CPU could cache the result. That would be bad, because another source (the hardware) changes the value. So you don't want to cache it. This is - if I understand it correctly - what volatile is good for. It makes sure that you really access memory and not some registers, because it got optimized or cached.

<h3>I / O</h3>
Imagine you write an application that want to transfer data from a disk to another disk. You might have one producer and one consumer. The producer tries to get data from the disk. Lets say the disk has a buffer and a register that indicates how many blocks are in the buffer. So your producer might poll at some point:

<code>int register = 0;
while(register == 0);</code>

Now the register can get changed by the device, but it seems to be an obvious that you can optimize this to

<code>while(TRUE);</code>

Now, with this "optimization" that the compiler might make, you will never notice when you can read from the disk. So you would mark register as volatile to tell the compiler that he should not optimize it.

Do you know some better examples? Perhaps short C examples with real code where you can actually see the difference?

<h2>Further reading</h2>
<ul>
  <li><a href="http://stackoverflow.com/q/3488703/562769">When exactly do you use the volatile keyword in Java?</a></li>
  <li><a href="http://stackoverflow.com/a/3430809/562769">Different meaning in Java and C#</a></li>
</ul>
