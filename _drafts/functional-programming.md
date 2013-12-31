---
layout: post
title: Functional programming
author: Martin Thoma
date: 2012-06-05 09:26:43
categories: 
- Cyberculture
tags: []
featured_image: 
---
Some days ago I've talked to a friend who didn't know what's so special about functional programming languages and why any problem should be easier to solve with them. I couldn't give a satisfactory reply, so I'll try it now.

<h2>Definitions</h2>
Although I'd like to have an exact definition of functional programming (languages), I think the following is only a characterization:

<div class="definition"><strong>Functional programming</strong> is a programming paradigm that treats computation as the evaluation of mathematical functions and <em>avoids state and mutable data</em>. It emphasizes the application of functions.</div>

Now you have to know other paradigms to get a feeling for the differences:

<div class="definition"><strong>Imperative programming</strong> is a programming paradigm that describes computation in terms of <em>statements that change a program state</em>. In much the same way that imperative mood in natural languages expresses commands to take action, imperative programs define sequences of commands for the computer to perform.</div>

<div class="definition"><strong>Object-oriented programming</strong> is a programming paradigm using "objects" – data structures consisting of data fields and methods together with their interactions – to design applications and computer programs. Programming techniques may include features such as <em>data abstraction</em>, <em>encapsulation</em>, messaging, modularity, polymorphism, and <em>inheritance</em>.</div>

Some paradigms may be combined. C++ is called a "imperative, object-oriented (class-based), functional, generic (template metaprogramming)" programming language in Wikipedias "<a href="http://en.wikipedia.org/wiki/List_of_multi-paradigm_programming_languages">List of multi-paradigm programming languages</a>"

<h2>Some examples</h2>
<h3>Haskell</h3>
On an Ubuntu machine, you need to install the <strong>ghc6</strong> package. Then save the following as fib.hs:
[scala]fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)[/scala]



<h2>Special features of functional programming languages</h2>


<h2>See also</h2>
<ul>
  <li>Wikipedia:
  <ul>
    <li><a href="http://en.wikipedia.org/wiki/Programming_paradigm">Programming paradigm</a></li>
    <li><a href="http://en.wikipedia.org/wiki/Functional_programming">Functional programming</a>, <a href="http://en.wikipedia.org/wiki/Imperative_programming">Imperative programming</a>, <a href="http://en.wikipedia.org/wiki/Object-oriented_programming">Object-oriented programming</a></li>
  </ul>
  </li>
</ul>