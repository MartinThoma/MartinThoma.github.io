---
layout: post
lang: en
title: Java Puzzle #8: Interfaces and Visibility
slug: java-puzzle-8-interfaces-and-visibility
author: Martin Thoma
date: 2012-08-09 17:00:42.000000000 +02:00
category: Code
tags: Programming, Java, puzzle
featured_image: 2012/07/java-thumb.png
---
What is the output of the following snippets:

<strong>Shape.java</strong>:
```java
public interface Shape {
    public void draw();
    private void calculateArea();
    public void printArea();
}
```

<strong>Rectangle.java</strong>
```java
public class Rectangle implements Shape {

    private final int x1, x2, y1, y2;
    private int area;

    public Rectangle(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }

    @Override
    public void calculateArea() {
        area = Math.abs((x1 - x2) * (y1 - y2));
    }

    @Override
    public void draw() {
        // TODO Auto-generated method stub
    }

    @Override
    public void printArea() {
        calculateArea();
        System.out.println("My area is " + area + ".");
    }

}
```

<strong>test.java</strong>:
```java
public class test {
    public static void main(String[] args) {
        Shape s = new Rectangle(0, 0, 1, 1);
        s.printArea();
    }
}
```

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
```bash
My area is 1.
```

<h2>Explanation</h2>
Interfaces may not implement anything. So it makes no sense to define private methods. Nevertheless it seems to be valid Java code.
