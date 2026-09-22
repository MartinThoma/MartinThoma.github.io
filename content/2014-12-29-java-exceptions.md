---
layout: post
title: Java Exceptions
slug: java-exceptions
lang: en
author: Martin Thoma
date: 2014-12-29 20:39
category: Code
tags: Java
featured_image: logos/java-programming.png
---
<div class="info">This is a quick article I have had as a draft for quite a while. It might not be finished or have other problems, but I still want to share it.</div>

<h2>When to use Errors and Exceptions</h2>
<blockquote>An Error is a subclass of Throwable that indicates serious problems that a reasonable application should not try to catch. Most such errors are abnormal conditions.</blockquote> (Source: <a href="http://docs.oracle.com/javase/6/docs/api/java/lang/Error.html">Javadoc</a>)



<h2>How to throw an exception</h2>
```java

public void myMethod( String s ) {
  if (!isStringValid(s)) {
    throw new IllegalArgumentException("This string is not valid!");
  }
}

```

<h2>Common Exceptions</h2>
* IllegalArgumentException: One argument of the current method doesn't have the form it should have.
* IllegalStateException: The current object is in the wrong state.
* NullPointerException: A null pointer was given, but it should have been an object.

A long list of exceptions is on <a href="http://wuhrr.wordpress.com/2007/11/22/java-exceptions-list/">Hai's Blog</a>.

<h2>See also</h2>
<ul>
  <li>http://docs.oracle.com/:
    <ul>
      <li><a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/lang/Exception.html">Class Exception</a></li>
    </ul>
  </li>
</ul>
