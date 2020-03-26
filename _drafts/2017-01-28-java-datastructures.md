---
layout: post
title: Java Datastructures
author: Martin Thoma
date: 2012-03-11 05:50:43
categories:
- Code
tags:
- Java
featured_image:
---
<h2>List</h2>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/List.html">Java Lists</a>:
<blockquote>An ordered collection (also known as a sequence). The user of this interface has precise control over where in the list each element is inserted. The user can access elements by their integer index (position in the list), and search for elements in the list.</blockquote>

<h3>LinkedList</h3>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/LinkedList.html">Java LinkedList</a>:
<blockquote>Linked list implementation of the List interface. Implements all optional list operations, and permits all elements (including null).</blockquote>

<h3>ArrayList</h3>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/ArrayList.html">Java ArrayList</a>:
<blockquote>Resizable-array implementation of the List interface. Implements all optional list operations, and permits all elements, including null. In addition to implementing the List interface, this class provides methods to manipulate the size of the array that is used internally to store the list. (This class is roughly equivalent to Vector, except that it is unsynchronized.)</blockquote>

<h2>Map</h2>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/Map.html">Java Map</a>:
<blockquote>An object that maps keys to values. A map cannot contain duplicate keys; each key can map to at most one value.</blockquote>

<h3>HashMap</h3>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/HashMap.html">Java HashMap</a>:
<blockquote>Hash table based implementation of the Map interface. This implementation provides all of the optional map operations, and permits null values and the null key. (The HashMap class is roughly equivalent to Hashtable, except that it is unsynchronized and permits nulls.) This class makes no guarantees as to the order of the map; in particular, it does not guarantee that the order will remain constant over time.</blockquote>

Provides constant-time performance for the basic operations (get and put).

<h3>TreeMap</h3>
<a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/util/TreeMap.html">Java TreeMap</a>:
<blockquote>Red-Black tree based implementation of the SortedMap interface. This class guarantees that the map will be in ascending key order, sorted according to the natural order for the key's class (see Comparable), or by the comparator provided at creation time, depending on which constructor is used.</blockquote>

Provides guaranteed log(n) time cost for the containsKey, get, put and remove operations.

<h2>Set</h2>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/Set.html">Java Sets</a>:
<blockquote>A collection that contains no duplicate elements. More formally, sets contain no pair of elements e1 and e2 such that e1.equals(e2), and at most one null element. As implied by its name, this interface models the mathematical set abstraction.</blockquote>

<h3>Hash Set</h3>
<a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/HashSet.html">Java HashSet</a>:
<blockquote>This class implements the Set interface, backed by a hash table (actually a HashMap instance). It makes no guarantees as to the iteration order of the set; in particular, it does not guarantee that the order will remain constant over time. This class permits the null element.</blockquote>

Provides constant time performance for the basic operations (add, remove, contains and size).

<h3>Tree Set</h3>
<a href="http://docs.oracle.com/javase/6/docs/api/java/util/TreeSet.html">Java TreeSet</a>:
<blockquote>A NavigableSet implementation based on a TreeMap. The elements are ordered using their natural ordering, or by a Comparator provided at set creation time, depending on which constructor is used.</blockquote>

Provides guaranteed log(n) time cost for the basic operations (add, remove and contains).

<h2>Some Resources</h2>
<ul>
  <li><a href="http://stackoverflow.com/questions/322715/when-to-use-linkedlist-over-arraylist">When to use LinkedList<> over ArrayList<>?</a></li>
</ul>
