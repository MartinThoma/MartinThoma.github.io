---
layout: post
title: What can ArrayList / LinkedList do what List can't?
author: Martin Thoma
date: 2013-02-04 11:50:45.000000000 +01:00
category: Code
tags: Java
featured_image: 2012/07/java-thumb.png
---
I've told my students to write
```java
List<MyClass> myList = new ArrayList<MyClass>();
```
instead of
```java
ArrayList<MyClass> myList = new ArrayList<MyClass>();
```
as this allows them to switch to any Class that implements List without having to change more code.

This does always make sense, except if you need methods from ArrayList or LinkedList. But which methods does <a href="http://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html">ArrayList</a> / <a href="http://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html">LinkedList</a> offer that <a href="http://docs.oracle.com/javase/7/docs/api/java/util/List.html">List</a> doesn't have?

ArrayList has:
<ul>
  <li>Object clone()</li>
  <li>void ensureCapacity(int minCapacity)</li>
  <li>void removeRange(int fromIndex, int toIndex)</li>
  <li>void trimToSize()</li>
</ul>

LinkedList has:
<ul>
  <li>void addFirst(E e)</li>
  <li>void addLast(E e)</li>
  <li>Object clone()</li>
  <li>Iterator<E> descendingIterator()</li>
  <li>E getFirst()</li>
  <li>E getLast()</li>
  <li>boolean offer(E e)</li>
  <li>boolean offerFirst(E e)</li>
  <li>boolean offerLast(E e)</li>
  <li>E peek()</li>
  <li>E peekFirst()</li>
  <li>E peekLast()</li>
  <li>E poll()</li>
  <li>E pollFirst()</li>
  <li>E pollLast()</li>
  <li>E pop()</li>
  <li>void push(E e)</li>
  <li>E removeFirst()</li>
  <li>boolean removeFirstOccurrence(Object o)</li>
  <li>E removeLast()</li>
  <li>boolean removeLastOccurrence(Object o)</li>
</ul>
