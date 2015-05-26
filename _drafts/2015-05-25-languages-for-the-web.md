---
layout: post
title: Languages for the Web
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- Programming
- Internet
featured_image: logos/java-programming.png
---
What programming language would I use for a big, new project in a Startup which
wants to offer a Web service? Sure, on the client side there is pretty much
only JavaScript (including variants like
[CoffeeScript](http://en.wikipedia.org/wiki/CoffeeScript) and
[TypeScript](http://en.wikipedia.org/wiki/TypeScript)) in combination with HTML
and CSS. I've used [MySQL](http://en.wikipedia.org/wiki/MySQL) and
[Redis](http://en.wikipedia.org/wiki/Redis) databases and I'm quite happy with
that. So this choice is also easy. But the choice for the server side is not
that easy. I've been using PHP for quite a while now, because when I started
programming it was the cheapest and easiest choice. But things have changed
(and I have more money, so I don't have to take the super cheap hosting
services). Although my experience with web projects is very limited, I want to
share a few thoughts.


## Java

[Java](http://en.wikipedia.org/wiki/Java_(programming_language)) is an
object-orientated language which runs on the Java Virtual Machine. Java is
probably the most used language for big business websites. Why is that the
case?

* Java is old: It first appeared in 1995.
    * Java is taught at many universities and many people know at least a
      little bit of Java. So companies don't have problems finding programmers.
      At least that might be the impression of people who don't realize that
      there is a big differencee between people saying they know Java and
      developers who can actually work with it.
    * I guess the Java ecosystem is pretty mature:
      [eclipse](http://en.wikipedia.org/wiki/Eclipse_%28software%29) and
      [IntelliJ IDEA](http://en.wikipedia.org/wiki/IntelliJ_IDEA) as an IDE,
      continuous integration with
      [Jenkins](http://en.wikipedia.org/wiki/Jenkins_(software)),
      [JavaServer Pages](http://en.wikipedia.org/wiki/JavaServer_Pages),
      [GlassFish](http://en.wikipedia.org/wiki/GlassFish),
      [Apache Ant](http://en.wikipedia.org/wiki/Apache_Ant) for automatic building,
      [JUnit](http://en.wikipedia.org/wiki/JUnit) for automatic unit tests,
      [log4J](http://en.wikipedia.org/wiki/Log4j) for logging ...
* Java is developed by
  [Oracle](http://en.wikipedia.org/wiki/Oracle_Corporation). Hence you can make
  contracts with Oracle to get support when things don't work.

That was what we have on the positive side. What is not so good about Java?

* VERY clumsy syntax. This is more than just a inconvenience. You have to type
  a lot to get things done which makes you slow. Of course, you can (and need
  to) use autocompletion, but it is still a lot to read. That makes maintaining
  the code a mess.
* Tools are hard to get to work.
* Unnecessary super-abstract constructs used for eventually never happening
  future extensions (see [Geek-and-poke.com](http://geek-and-poke.com/geekandpoke/2014/1/2/games-for-the-real-geeks-part-2)).
* A bit more secure than C/C++ as you cannot access out-of-bound arrays, you
  don't have pointers. So buffer overflows are almost impossible in Java (see [SO](http://stackoverflow.com/a/479738/562769) for more details). However, you buy this security with much
  less easy syntax and you don't get as much security as would be possible with
  just a bit more effort. See rust for more details.
* Speed and memory usage: Again, Java might be better in speed than many other
  languages, but not as good as some others are. And Java seems to need A LOT
  of memory. However, I am not too sure if that is really a problem.
  (see [Surprise! Java is fastest for server-side Web apps](http://www.infoworld.com/article/2609675/java/surprise--java-is-fastest-for-server-side-web-apps.html))


See also:

* [Is Java a Compiled or an interpreted programming language?](http://stackoverflow.com/a/1326084/562769): The short answer is no. But Java guys don't like to hear that :-)
* [Why do I hear about so many Java insecurities? Are other languages more secure?](http://security.stackexchange.com/q/57646/3286): The short answer is no, thinking about C/C++.
* [Security of JVM for Server](http://security.stackexchange.com/q/32822/3286)
* [C++ performance vs. Java/C#](http://stackoverflow.com/q/145110/562769)


## JavaScript: Node.js

[Node.js](http://en.wikipedia.org/wiki/Node.js) is a runtime environment which
was initially released in 2009 and became quite popular since then. Node.js
applications are written in JavaScript and hence have all the advantages and
disadvantages of JavaScript:

* They profit from heavy development in JavaScript engines / JIT compilers like
  [V8](http://en.wikipedia.org/wiki/V8_(JavaScript_engine)).
* The syntax is flexible and light-weight.
* Just like Java, JavaScript first appeared in 1995. So the language itself is
  old and stable.
    * A lot of developers know at least a little bit of JavaScript.
    * The ecosystem is mature.

* http://java.dzone.com/articles/performance-comparison-between

## Go

## C#


## Rust

Rust is a very safe language, but seems not to be ready for productive usage.

> I am a big fan of Rust, but as it aims to be a better C++, it is probably a
> better fit for OS development, game engines, embedded systems, databases,
> complex desktop applications (Photoshop/Word/Chrome), etc. While Rust is
> quite expressive for a systems programming language, its banner features are
> the borrow checker (+ lifetimes, etc) and powerful static type system. Rust
> emphasizes zero-cost abstractions with compiler-enforced memory & thread
> safety. The popular web development languages are dynamically typed and
> interpreted, with an emphasis on rapid development, which is a very different
> niche than Rust claims to fill.

Source: [news.ycombinator.com](https://news.ycombinator.com/item?id=7809791)

Tools:

* [Iron](http://ironframework.io/): extensible web framework for rust

See:

* [arewewebyet.com](http://arewewebyet.com/)
* [Rust Web Frameworks](http://stackoverflow.com/a/23577767/562769)

## Python

* [fullstackpython.com](http://www.fullstackpython.com/)


## PHP

* [PHPCI](https://www.phptesting.org/)?

## Credits
As I don't have much experience with web development, I asked a few friends
to have a look at the different parts of the article. They looked especially
at plain wrong statements, if I named the important frameworks / tools. They
might not completely agree with the comparison to other language (after all,
I wrote the article), but they helped me a lot to get things not too wrong:

* Java: Checked by Sören. He has several years of experience with Java web
  development.
* Rust, JavaScript and Go: Johannes
* PHP: Stefan