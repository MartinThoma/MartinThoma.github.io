---
layout: post
title: Languages for Back Ends
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- Programming
- Internet
featured_image: logos/java-programming.png
---
What programming language would I use for the back end of a big, new project in
a Startup which wants to offer a Web service? Sure, on the client side there is
pretty much only JavaScript (including variants like
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

Just for clarification: I am only talking about the back end. A back end is the
data access layer which manages requests comming to the server. It needs to
server many requests (> 100 requests/second) fast (< 300 ms in average). It
should not execute computationally heavy jobs which can be pre-computed. This
can be done by another system which does not need to be programmed in the same
language. The back end does also not deal with presentation to the user. This
is what the front end does. However, you should have more than a good idea in
which form the front end gets the data. The cleanest approach I've seen so far
is a pure RESTful API for all interactions between front end and back end .


## Java

[Java](http://en.wikipedia.org/wiki/Java_(programming_language)) is an
object-oriented language which runs on the Java Virtual Machine. Java is
probably the most used language for big business websites. Why is that the
case?

* Java is old: It first appeared in 1995.
    * Java is taught at many universities and many people know at least a
      little bit of Java. So companies don't have problems finding developers.
      At least that might be the impression of people who don't realize that
      there is a big differencee between people saying they know Java and
      developers who can actually work with it.
    * I guess the Java ecosystem is pretty mature:
        * [eclipse](http://en.wikipedia.org/wiki/Eclipse_%28software%29),
          [IntelliJ IDEA](http://en.wikipedia.org/wiki/IntelliJ_IDEA) and
          [Netbeans](https://en.wikipedia.org/wiki/NetBeans) as IDEs,
        * [Jenkins](http://en.wikipedia.org/wiki/Jenkins_(software)) for
          continuous integration,
        * [GlassFish](http://en.wikipedia.org/wiki/GlassFish),
        * [Apache Ant](http://en.wikipedia.org/wiki/Apache_Ant)/[Apache Maven](https://en.wikipedia.org/wiki/Apache_Maven) or [Gradle](https://gradle.org/) for automatic building,
        * [JUnit](http://en.wikipedia.org/wiki/JUnit),
          [Mockito](https://en.wikipedia.org/wiki/Mockito), Powermock for automatic unit tests,
        * [log4J](http://en.wikipedia.org/wiki/Log4j) and [log4J 2](http://logging.apache.org/log4j/2.x/) for logging,
        * [Apache JMeter](https://en.wikipedia.org/wiki/Apache_JMeter) for load
          testing
        * [Jersey](https://jersey.java.net/) for RESTful Web services,
        * [Grizzly](https://grizzly.java.net/)
        * [FindBugs](http://findbugs.sourceforge.net/),
          [SonarQube](https://en.wikipedia.org/wiki/SonarQube) for code quality
          / static code analysis
        * [Hibernate](https://en.wikipedia.org/wiki/Hibernate_(Java)) for ORM,
        * Frameworks like [Spring](https://en.wikipedia.org/wiki/Spring_Framework),
          [JSF](https://en.wikipedia.org/wiki/JavaServer_Faces),
          [JSP](http://en.wikipedia.org/wiki/JavaServer_Pages),
          [Apache Struts 2](https://en.wikipedia.org/wiki/Apache_Struts_2),
          [Apache Wicket](https://en.wikipedia.org/wiki/Apache_Wicket)
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
was initially released in 2009 and became quite popular since then. Node.js is
asynchronous, event-driven and scalable. Node.js applications are written in
JavaScript and hence have all the advantages of JavaScript:

* They profit from heavy development in JavaScript engines / JIT compilers like
  [V8](http://en.wikipedia.org/wiki/V8_(JavaScript_engine)).
* The syntax is flexible and light-weight.
* Just like Java, JavaScript first appeared in 1995. So the language itself is
  old and stable.
    * A lot of developers know at least a little bit of JavaScript.
    * The ecosystem is mature.
        * [npm](http://en.wikipedia.org/wiki/Npm_(software)) and [bower](http://en.wikipedia.org/wiki/Bower_(software)) for package management
        * [AngularJS](http://en.wikipedia.org/wiki/AngularJS) and [Underscore.js](http://en.wikipedia.org/wiki/Underscore.js) as big frameworks
        * [Backbone.js](http://en.wikipedia.org/wiki/Backbone.js) for MVP.
        * [Unit.js](http://en.wikipedia.org/wiki/Unit.js) for unit testing.
        * [Grunt](http://gruntjs.com/) as a task runner.
        * [Sequelize](http://docs.sequelizejs.com/en/latest/) as an ORM.
* [Lots of easy tutorials](http://stackoverflow.com/q/2353818/562769)
* Nice community:
    * [nodeschool.io](http://nodeschool.io/), [nodesummit.com](http://nodesummit.com/)

What is still to say?

* Node is FAST and scalable! (see [Performance Comparison Between Node.js and Java EE](http://java.dzone.com/articles/performance-comparison-between))
* JavaScript is very insecure. Even simple syntax error will only get revealed
  when they are actually executed. So Unit testing is very important.
* Node.js is used by LinkedIn, Yahoo!, Uber, PayPal ([source](https://nodejs.org/industry/))

See also:

* [How to decide when to use Node.js?](http://stackoverflow.com/q/5062614/562769)
* [How to debug Node.js applications](http://stackoverflow.com/q/1911015/562769)
* [node.js tutorial](https://www.airpair.com/javascript/node-js-tutorial)


## Go

[Go](https://en.wikipedia.org/wiki/Go_(programming_language)) is a
statically-typed, compiled language developed by Google. It first appeared in
2009, so it is very young.

* Go offers the basic tools you need for web development:
    * [martini](http://martini.codegangsta.io/)/[Gin Gonic](https://gin-gonic.github.io/gin/): A web development framework
    * [mustache](https://github.com/hoisie/mustache) for templates
* [Good tutorial](https://tour.golang.org/) and also some [material for web development](https://golang.org/doc/articles/wiki/)

See also:

* [Gin Gonic May Be 40x Faster Than Martini, But It Is Not Better](https://www.dougcodes.com/go-lang/gin-gonic-may-be-40x-faster-than-martini-but-it-is-not-better)

## C&#35;

* [nuget.org](http://www.nuget.org/)


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

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is one of
the oldest programming languages which are still in use. It first appeared in
1991. Python is dynamically typed, interpreted, object-oriented and includes
functional programming features.

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))/[Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) as frameworks

* [pypi.python.org](https://pypi.python.org/pypi)
* [fullstackpython.com](http://www.fullstackpython.com/)


## PHP

[PHP](https://en.wikipedia.org/wiki/PHP) is a server-side scripting language
which appeared first in 1995. It is dynamically typed.

* [Language inconsistencies](http://martin-thoma.com/php-a-strange-language/)
* The ecosystem is ok:
    * [PHPCI](https://www.phptesting.org/) for continuus integration.
    * [Zend Framework](https://en.wikipedia.org/wiki/Zend_Framework) / [Drupal](https://en.wikipedia.org/wiki/Drupal) / [Joomla](https://en.wikipedia.org/wiki/Joomla) / [TYPO3](https://en.wikipedia.org/wiki/TYPO3) / [Symfony](https://en.wikipedia.org/wiki/Symfony) / [WordPress](https://en.wikipedia.org/wiki/WordPress)
    * [PHPUnit](https://en.wikipedia.org/wiki/PHPUnit) for unit testing,
    * [Composer](https://en.wikipedia.org/wiki/Composer_(software)) for package management and [packagist.org](https://packagist.org/) to find packages,

## Others

* [Ruby](http://en.wikipedia.org/wiki/Ruby_(programming_language)) with [Rails](http://en.wikipedia.org/wiki/Ruby_on_Rails): I know it is quite well-known and used by many people. But
  I don't know Ruby enough to write anything meaningful. The Ruby syntax is
  similar to Python.

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
* Python: Me?
* C#: ?