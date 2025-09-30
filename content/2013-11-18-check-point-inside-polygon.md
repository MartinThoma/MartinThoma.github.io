---
layout: post
lang: en
title: How to check if a point is inside of a polygon?
slug: check-point-inside-polygon
author: Martin Thoma
date: 2013-11-18 21:36:09.000000000 +01:00
category: Code
tags: Python, algorithms, Geometry
featured_image: 2013/11/polygon-is-point-inside-thumb.png
---
Suppose you have a with $n$ sides. This is called a $n$-glon.


<h2>Basics about polygones</h2>
A $n$-glon can be defined by a list of $n$ points.

Note that the order is important:

<figure class="aligncenter">
            <a href="../images/2013/11/polygon-order.png"><img src="../images/2013/11/polygon-order.png" alt="The order of points is important for the definition of a polygon" style="max-width:512" height="233px;" class=""/></a>
            <figcaption class="text-center">[A, B, C, D, E, F, G] != [A, B, C, D, F, E, G]</figcaption>
        </figure>


I will not consider self-intersecting polygones for the following statements. I'm aware of them, but whenever you have a self-intersecting polygon you can create multiple polygones that cover the same area and don't intersect each other (some pairs might have a finite number of points in common, but not an infinite number).

<h2>Is a point in a triangle / a rectangle</h2>
It is quite easy to check weather a point is inside of a triangle or inside of a rectangle. I have already written an article about <a href="../how-to-check-if-a-point-is-inside-a-rectangle/">how to check if a point is inside of a rectangle</a>.

<h2>Is a point inside of a n-glon?</h2>
Let $P$ be a point and $N = [P_1, P_2, \dots, P_n]$ be a $n$-glon. It is now much more difficult to check if $P$ is inside of $N$. The area-approach works for convex $n$-glons, but that's it.


<h3>Count Crossing Line Segments</h3>
However, you can try another approach which I have visualized in the following image:

<figure class="aligncenter">
    <img src="../images/2013/11/polygon-is-point-inside.png" style="max-width: 512px; max-height: 481px;" class="size-full" alt="Check if P is inside of N"/>
    <figcaption>Check if P is inside of N</figcaption>
</figure>

When $P$ is inside of $N$, every line $P_{1}P, P_{2}P, \dots, P_{n}P$ will cross the polygon lines $P_{1}P_2,P_{2}P_3, \dots, P_{n}P_1$ an even number of times. If P is outside, at least one of the lines $P_{i}P$ will cross a polygon line $P_{j}P_{j+1}$ once.

This means, for every check you have to check $n^2$ pairs of line segments for crossings. How you can do that is explained in my article <a href="../how-to-check-if-two-line-segments-intersect/" title="How to check if two line segments intersect">How to check if two line segments intersect</a>.

This algorithm is in $\mathcal{O}(n^2)$ time complexity (it does need a constant amount of additional space).

<h3>Triangularization</h3>
When you have a lot of querys, you might want to divide your polygon into convex polygones. The easiest way to do this might be dividing $N$ into triangles.

That way, you can check for every triangle if $P$ is inside of it. I assume that the number of triangles is not bigger than $n$. As the check is in constant time for one triangle, you would have an algorithm that needs $\mathcal{O}(n)$ time and space for its checks (+ some preprocessing which is done only once).
