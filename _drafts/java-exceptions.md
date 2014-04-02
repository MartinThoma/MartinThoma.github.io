---
layout: post
title: Java Exceptions
author: Martin Thoma
date: 2012-01-21 10:50:11
categories: 
- Code
tags: 
- Exception
- Java
featured_image: 2011/11/java-programming.png
---
<h2>When to use Errors and Exceptions</h2>
<blockquote>An Error is a subclass of Throwable that indicates serious problems that a reasonable application should not try to catch. Most such errors are abnormal conditions.</blockquote> (Source: <a href="http://docs.oracle.com/javase/6/docs/api/java/lang/Error.html">Javadoc</a>)



<h2>How to throw an exception</h2>
{% highlight java %}
public void myMethod( String s ) {
  if (!isStringValid(s)) {
    throw new IllegalArgumentException("This string is not valid!");
  }
}
{% endhighlight %}

<h2>Common Exceptions</h2>
IllegalArgumentException: One argument of the current method hasn't the form it should have.
IllegalStateException: The current object is in the wrong state.
NullPointerException: A Null-Pointer was given, but it should have been an object.
A long list of Exceptions is on <a href="http://wuhrr.wordpress.com/2007/11/22/java-exceptions-list/">Hai's Blog</a>.

<h2>See also</h2>
<ul>
  <li>http://docs.oracle.com/:
    <ul>
      <li><a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/lang/Exception.html">Class Exception</a></li>
    </ul>
  </li>
</ul>
