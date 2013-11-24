---
layout: post
status: publish
published: true
title: Entwurfsmuster-Beispiele
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 37691
wordpress_url: http://martin-thoma.com/?p=37691
date: 2012-08-11 17:00:03.000000000 +02:00
categories:
- German posts
tags:
- SWT I
- Design Pattern
comments: []
---
<h2>Singleton</h2>
<strong>Zweck</strong>: Stelle sicher, dass es nur eine Instanz dieser Klasse gibt.
<strong>Beispiel</strong>: <a href="http://docs.oracle.com/javase/6/docs/api/java/lang/Runtime.html#getRuntime%28%29">java.lang.Runtime.getRuntime()</a>
[java]public class Singleton {
    // an instance of a singleton
    private static Singleton instance = null;

    // private default constructor to prevent the external creation
    // of more instances
    private Singleton() {
    }

    // static method which returns the instance
    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}[/java]

<h2>Bequemlichkeitsklasse</h2>
<strong>Zweck</strong>: Faulheit - mache Methodenaufrufe durch &auml;nderbare default-Parameter einfacher.
Das Bequemlichkeitsmuster ist einfach das &Uuml;berladen einer Methode:
[java]public class Bequemlichkeitsklasse {
    // convenience class
    int v1, v2, v3;

    int anfrage(int p1, int p2, int p3) {
        return p1 * p2 * p3;
    }

    int anfrage(int p1) {
        return anfrage(p1, v2, v3);
    }

    int anfrage() {
        return anfrage(v1, v2, v3);
    }

    void setzeZustand(int p1, int p2, int p3) {
        v1 = p1;
        v2 = p2;
        v3 = p3;
    }
}[/java]

<h2>Schablonenmethode</h2>
Siehe <a href="http://martin-thoma.com/java-puzzle-9-template-method-pattern">Java Puzzle #9: Template method pattern</a>.

<h2>Siehe auch</h2>
<ul>
  <li><a href="http://stackoverflow.com/a/2707195/562769">Examples of GoF Design Patterns in Java</a></li>
</ul>
