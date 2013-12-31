---
layout: post
title: Coordinates of regular polygons
author: Martin Thoma
date: 2013-03-07 05:19:43
categories: 
- Cyberculture
tags: []
featured_image: 
---
I've just wondered if there is any way to get nice coordinates for regular polygons. Now, what does nice mean?

I define:

<ul>
    <li>natural numbers [latex]\mathbb{N}[/latex] are best</li>
    <li>decimal fractions that are not periodical for decimal and binary (a subset of [latex]\mathbb{Q}[/latex])</li>
    <li>the closer you come with a double to the real coordinates, the better</li>
    <li>ugly are irrational numbers ([latex]\mathbb{R} \setminus \mathbb{Q}[/latex])</li>
</ul>

I think the first two are actually the same. When I have a fraction, I can scale my polygon up and get natural numbers.

<h2>Triangle</h2>
First try:

[caption id="attachment_59981" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/triangle-regular.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/triangle-regular-300x290.png" alt="A regular triangle with ugly coordinates" width="300" height="290" class="size-medium wp-image-59981" /></a> A regular triangle with ugly coordinates[/caption]

Actually, it is not possible to get integer coordinates (<a href="http://math.stackexchange.com/a/105387/6876">source</a>).

<h2>Sqrare</h2>
That one is easy:

{(0|0), (1,0), (1,1), (0,1)}

<h2>Pentagon</h2>