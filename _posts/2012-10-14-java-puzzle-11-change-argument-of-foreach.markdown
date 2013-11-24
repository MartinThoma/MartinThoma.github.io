---
layout: post
status: publish
published: true
title: ! 'Java Puzzle #11: Change argument of foreach'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 46901
wordpress_url: http://martin-thoma.com/?p=46901
date: 2012-10-14 21:15:43.000000000 +02:00
categories:
- Code
tags:
- Programming
- Java
- puzzle
comments: []
---
What is the output of the following HelloWorld.java?

[java]import java.util.LinkedList;

public class HelloWorld {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        list.add(1);
        list.add(2);
        list.add(3);
        int i = 0;
        for (Integer el : list) {
            System.out.println(el);
            list.add(el);
            i++;
            if (i > 20) {
                break;
            }
        }
    }
}[/java]


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
.

<h2>Answer</h2>
[java]1
Exception in thread "main" java.util.ConcurrentModificationException
	at java.util.LinkedList$ListItr.checkForComodification(LinkedList.java:761)
	at java.util.LinkedList$ListItr.next(LinkedList.java:696)
	at HelloWorld.main(HelloWorld.java:10)[/java]
