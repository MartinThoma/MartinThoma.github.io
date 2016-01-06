---
layout: post
title: Languages for Back Ends
author: Martin Thoma
date: 2015-06-24 12:43
categories:
- Code
tags:
- Programming
- Internet
- Java
- JavaScript
- Go
- Rust
- Python
- PHP
- Hack
featured_image: logos/java-programming.png
---
What programming language would I use for the back end of a big, new project in
a startup which wants to offer a web service? Sure, on the client side there is
pretty much only JavaScript (including variants like
[CoffeeScript](http://en.wikipedia.org/wiki/CoffeeScript) and
[TypeScript](http://en.wikipedia.org/wiki/TypeScript)) in combination with HTML
and CSS. I've used [MySQL](http://en.wikipedia.org/wiki/MySQL) and
[Redis](http://en.wikipedia.org/wiki/Redis) databases and I'm quite happy with
that. But the choice for the server side is not that easy. I've been using PHP
for quite a while now, because it was the cheapest and easiest choice when I
started programming. But things have changed (and I have more money, so I
don't have to take the super cheap hosting services). Although my experience
with web projects is very limited, I want to share a few thoughts.


## Definitions: Back End and Security

Just for clarification: I am only talking about the back end. A back end is the
data access layer which manages requests comming to the server. It needs to
server **many requests** (&gt; 100 requests/second) **fast** (&lt; 300 ms in
average). It should not execute computationally heavy jobs which can be
pre-computed or do not need to be displayed instantly to the client. This can
be done by another system which does not need to be programmed in the same
language. The back end does also not deal with presentation to the user. This
is what the front end does. However, you should have more than a good idea in
which form the front end gets the data. The cleanest approach I've seen so far
is a pure RESTful API for all interactions between front end and back end.

The backend language should also make it easy to validate / sanitize input
data, connect with databases, store/get stuff on/from the file system.

In the following, I will write that some languages are "secure" or "not
secure". This does not mean that you can / cannot write code which is secure.
It means that the compiler (or other widespread tools) give you guarantees
about bugs in your code. For example, C is a very insecure language as the
compiler does no
[bounds checking](https://en.wikipedia.org/wiki/Bounds_checking). The types
of errors which can be detected by automatic tools (without further testing)
are:

* Syntax errors,
* Out of bounds (reading),
* [buffer overflow](https://en.wikipedia.org/wiki/Buffer_overflow) (not checked in C/C++, but not possible in Java ([source](http://stackoverflow.com/q/479701/562769))),
* unused variables (which might indicate other problems; at least code smell),
* type problems: This is a bit fuzzy, as you can write stringly typed code (see
  [New Programming Jargon](http://blog.codinghorror.com/new-programming-jargon/))
  in probably every language, but in some languages it is more common than in
  others. Some languages also make it easier to use the type system to detect
  errors. For example, PHP is very insecure in this sense as `123 == "123ab"`,
  Python is a bit more secure, but you can return whatever you want, Java is
  much more secure. Haskell is even more secure in this sense, as it has
  real functions (without side effects, checked by the compiler). See
  [What can Haskell's type system do that Java's can't and vice versa?](http://programmers.stackexchange.com/q/167975/25699) for more.

There are also some errors which can be detected at runtime. The handling of
those runtime errors differs from language to language. For example, C and C++
fails silently (e.g. [this question](http://stackoverflow.com/q/671703/562769)).
This is bad. For example, there are some silent out-of-bounds errors in C / C++
where Rust would fail loud (I think Heartbleed is one example; see
[Would Rust have prevented Heartbleed? Another look](http://tonyarcieri.com/would-rust-have-prevented-heartbleed-another-look) if you're interested in that specific example).

Of course, all of those problems can be detected with good testing. But the
more is done automatically, the less can go wrong when you don't write (good)
tests.


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
        * [Apache Tomcat](https://en.wikipedia.org/wiki/Apache_Tomcat) / [WildFly](https://en.wikipedia.org/wiki/WildFly) (former JBoss): application server / web server / servlet container
        * [Grizzly](https://grizzly.java.net/) / [Jetty](https://en.wikipedia.org/wiki/Jetty_(web_server)): Web server
        * [FindBugs](http://findbugs.sourceforge.net/),
          [SonarQube](https://en.wikipedia.org/wiki/SonarQube) for code quality
          / static code analysis
        * [Hibernate](https://en.wikipedia.org/wiki/Hibernate_(Java)) for ORM,
        * [OSGi](https://en.wikipedia.org/wiki/OSGi#Architecture):
          [Apache Felix](https://en.wikipedia.org/wiki/Apache_Felix) /
          [Equinox](https://en.wikipedia.org/wiki/Equinox_(OSGi)) - see [10min clip](https://www.youtube.com/watch?v=3Ut_3u4aVZQ) for a high-level explanation of OSGi,
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
        * [Backbone.js](http://en.wikipedia.org/wiki/Backbone.js) / [AngularJS](http://en.wikipedia.org/wiki/AngularJS) for MVP / MVC.
        * [Unit.js](http://en.wikipedia.org/wiki/Unit.js) for unit testing.
        * [Grunt](http://gruntjs.com/) as a task runner.
        * [Sequelize](http://docs.sequelizejs.com/en/latest/) as an ORM.
        * [Karma](http://karma-runner.github.io/0.12/index.html): Test runner
        * [expressjs](http://expressjs.com/): web application framework
* [Lots of easy tutorials](http://stackoverflow.com/q/2353818/562769)

What is still to say?

* Node is FAST and scalable! (see [Performance Comparison Between Node.js and Java EE](http://java.dzone.com/articles/performance-comparison-between))
* JavaScript is very insecure. Even simple syntax error will only get revealed
  when they are actually executed. So Unit testing is very important.
* Node.js is used by LinkedIn, Yahoo!, Uber, PayPal ([source](https://nodejs.org/industry/))
* There are quite a few people moving from Node.js to Go ([1](http://thenewstack.io/from-node-js-to-go-why-one-startup-made-the-switch/), [2](http://bowery.io/posts/Nodejs-to-Golang-Bowery/), [3](http://zef.me/blog/6191/the-march-towards-go), [4](https://medium.com/code-adventures/farewell-node-js-4ba9e7f3e52b))

See also:

* [How to decide when to use Node.js?](http://stackoverflow.com/q/5062614/562769)
* [How to debug Node.js applications](http://stackoverflow.com/q/1911015/562769)
* [node.js tutorial](https://www.airpair.com/javascript/node-js-tutorial)


## Go

[Go](https://en.wikipedia.org/wiki/Go_(programming_language)) is a
statically-typed, compiled language developed by Google. It first appeared in
2009, so it is very young.

* Go offers the basic tools you need for web development:
    * [martini](http://martini.codegangsta.io/)/
      [Gin Gonic](https://gin-gonic.github.io/gin/): A web development framework
    * [mustache](https://github.com/hoisie/mustache) for templates
    * [gorm](https://github.com/jinzhu/gorm): ORM
* [Good tutorial](https://tour.golang.org/) and also some [material for web development](https://golang.org/doc/articles/wiki/)
* Some tasks are much more complicated than they should be. Sorting, to name one example (see [SO](http://stackoverflow.com/q/28999735/562769)).
* Go is different from some other languages, e.g. if you want a method to be
  public, the first character of the method name has to be capitalized. Or
  unused variables result in a compiler error.

See also:

* [Gin Gonic May Be 40x Faster Than Martini, But It Is Not Better](https://www.dougcodes.com/go-lang/gin-gonic-may-be-40x-faster-than-martini-but-it-is-not-better)
* [Go vs Node.js for servers](https://www.reddit.com/r/golang/comments/1ye3z6/go_vs_nodejs_for_servers/)


## C&#35;

[C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) is a
compiled, statically typed language (with dynamic features, see [Understanding the Dynamic Keyword in C# 4](https://visualstudiomagazine.com/articles/2011/02/01/understanding-the-dynamic-keyword-in-c4.aspx)) developed by Microsoft. It was publically
announced in 2000. The initial release of its web appliction framework
[ASP.NET](https://en.wikipedia.org/wiki/ASP.NET) was in 2002.

The ecosystem seems to include:

* [nuget.org](http://www.nuget.org/)
* [IIS](https://en.wikipedia.org/wiki/Internet_Information_Services): Web server
* [Entity Framework](http://www.asp.net/entity-framework): ORM
* [LINQ](https://en.wikipedia.org/wiki/Language_Integrated_Query): SQL queries
* [Visual Studio](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio): IDE
* [ASP.NET MVC Framework](https://en.wikipedia.org/wiki/ASP.NET_MVC_Framework)

But I don't know enough about C&#35; / ASP.NET to write something meaningful
about it.

Coding Horror described why they use ASP.NET for StackOverflow and why he
doesn't recommend it for OpenSource projects
([source](http://blog.codinghorror.com/why-ruby/)). StackExchange also
describes what they use
([1](http://blog.stackoverflow.com/2008/09/what-was-stack-overflow-built-with/),
[2](http://meta.stackexchange.com/a/10370/158075)).

I see a big problem in the Microsoft-centric technology stack. <strike>You have to use
everything from them. (Almost) everything is closed source. If they discontinue
the development or if they don't fix stuff which might be relevant for you,
you're fucked.</strike>

This seems to change. Microsoft moved some important parts of their stack to
GitHub (see [dotnet.github.io](http://dotnet.github.io/)). Most important seems
to be that the compiler Roslyn is licensed under an Apache License. But there
is also ASP.NET, the Entity Framework, and the .NET runtime. The
[Visual Studio Community Edition](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx) is not available for free (but only for Windows).


## Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is one of
the oldest programming languages which are still in use. It first appeared in
1991. Python is dynamically typed, interpreted, object-oriented and includes
functional programming features.

Although I use Python for many projects, I didn't use it by now for a web
project. So I might not know the important tools / frameworks. Please keep that
in mind.

* Ecosystem:
    * [pypi.python.org](https://pypi.python.org/pypi) and `pip`: Package
      hosting and package management
    * [Sphinx](http://sphinx-doc.org/): (Semi) automatic code documentation,
      e.g. the [scipy docs](http://docs.scipy.org/doc/scipy/reference/optimize.html)
      are generated with Sphinx from Python code. This is one of the best
      documentations I have ever seen.
    * [Django](https://en.wikipedia.org/wiki/Django_(web_framework))/
      [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) as frameworks
    * [pytest](http://pytest.org/latest/)/[nose](https://nose.readthedocs.org/en/latest/) for testing
    * [gevent](http://www.gevent.org/): a coroutine-based Python networking library
    * [Tornado](http://www.tornadoweb.org/en/stable/): Web server
* Some Python people switch to Go ([1](https://lincolnloop.com/blog/djangonaut-building-webapp-go-gorilla/), [2](http://blog.disqus.com/post/51155103801/trying-out-this-go-thing))
* Many tutorials and often very good documentation:
    * [Flask](http://flask.pocoo.org/)
    * [djangobook.com](http://www.djangobook.com/en/2.0/index.html) and [docs.djangoproject.com](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
    * [fullstackpython.com](http://www.fullstackpython.com/)
* Flask and Django work with PyPy ([source](http://pypy.org/compat.html)). That
  might make them much faster.
* Used by big players:
    * Quora ([source](http://www.quora.com/Why-did-Quora-choose-Python-for-its-development))
    * Prezi, Pinterest, Instagram ([source](https://wakatime.com/blog/25-pirates-use-flask-the-navy-uses-django))
    * Bitbucket, The Onion ([source](http://codecondo.com/popular-websites-django/))

I think one of the main advantages of Python is that it is really easy to write
code which is easy to read (because of docstrings, Pythons weird intendation
semantics and very nice syntax) and quite hard to write unreadable code. I am
sure I have a biased view regarding Python, but I am also sure a lot of people
share this subjective impression.


## PHP

[PHP](https://en.wikipedia.org/wiki/PHP) is a server-side scripting language
which appeared first in 1995. It is dynamically typed.

* [Language inconsistencies](//martin-thoma.com/php-a-strange-language/)
  are really bad with PHP - see also
  [PHP: a fractal of bad design](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/)
* The ecosystem is ok:
    * [PHPCI](https://www.phptesting.org/) for continuus integration.
    * [Zend Framework](https://en.wikipedia.org/wiki/Zend_Framework) / [Symfony](https://en.wikipedia.org/wiki/Symfony)
    * Smaller Frameworks like [CakePHP](http://cakephp.org/) and [Code Igniter](http://www.codeigniter.com/)
    * [Drupal](https://en.wikipedia.org/wiki/Drupal) / [Joomla](https://en.wikipedia.org/wiki/Joomla) / [TYPO3](https://en.wikipedia.org/wiki/TYPO3) / [WordPress](https://en.wikipedia.org/wiki/WordPress)
    * [PHPUnit](https://en.wikipedia.org/wiki/PHPUnit) for unit testing,
    * [Composer](https://en.wikipedia.org/wiki/Composer_(software)) for package management and [packagist.org](https://packagist.org/) to find packages
    * [cruisecontrol](http://cruisecontrol.sourceforge.net/) for Continuus
      Integration

A big advantage of PHP is that it is easy to learn. You can run PHP everywhere
and hosting is cheap. Wikipedia makes use of PHP, so it is obviously possible
to create systems which have HUGE numbers of requests and still work fine.

{% caption align="aligncenter" width="500" alt="The right tool for the right job" text="The right tool for the right job - by <a href='http://www.commitstrip.com/en/2015/01/12/the-right-tool-for-the-right-job/'>commitstrip.com</a>" url="../images/2015/05/Strip-PHP-doute650-Webenglsih.jpg" %}


## Hack

[Hack](https://en.wikipedia.org/wiki/Hack_(programming_language)) is a
programming language introduced in 2014 by Facebook. It is a PHP dialect. Key
differences to PHP are:

* Function arguments and return values can be annotated with types.
* Hack does not support some language features which are supported by PHP
  ([source](http://docs.hhvm.com/manual/en/hack.unsupported.php)). Which is
  good. For example, goto, variable variables, string incrementing, ...


See also:

* [hacklang.org](http://hacklang.org/)


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

See:

* [arewewebyet.com](http://arewewebyet.com/)
* [Rust Web Frameworks](http://stackoverflow.com/a/23577767/562769)


## Others

* [Ruby](http://en.wikipedia.org/wiki/Ruby_(programming_language)) with [Rails](http://en.wikipedia.org/wiki/Ruby_on_Rails): I know it is quite well-known and used by many people. But
  I don't know Ruby enough to write anything meaningful. The Ruby syntax is
  similar to Python.
* [Scala](https://en.wikipedia.org/wiki/Scala_(programming_language)) [seems to be noteworthy](http://readwrite.com/2011/06/06/cpp-go-java-scala-performance-benchmark)


## See also

* [Web Framework Benchmarks](http://www.techempower.com/benchmarks/#section=data-r9&hw=i7&test=json)
* [Usage of server-side programming languages for websites](http://w3techs.com/technologies/overview/programming_language/all)
* [todobackend.com](http://www.todobackend.com/): A lot of different back end technology stacks
* [bento.io](https://www.bento.io/): Seems to offer many tutorials
* [The RedMonk Programming Language Rankings: January 2015](http://redmonk.com/sogrady/2015/01/14/language-rankings-1-15/)
* [Comparison of programming languages](https://en.wikipedia.org/wiki/Comparison_of_programming_languages)


## Conclusion

Thinking about it that carefully, I see three languages which seem to be
suitable for back ends for me:

* Go: Fast and compiled
* node.js: Good scalability
* Python: It is the language I know best and of which I like the syntax best.
  Besides that, it has a very nice and clear syntax, good community-developed
  coding style standards and is very easy to read and well-documented.

Not suitable seem to be:

* PHP: Because of the language inconsistencies which seem to make it pretty
  hard to make a reliable back end
* C#: The technology stack is too Microsoft centered.
* Java: Too clumsy syntax, too hard to get it work.

The other programming languages could be very good choices. I simply don't know
it. I am very curious if rust will be used for back ends. Hack is very young,
let's see if it will spread in a few years.


## Credits
As I don't have much experience with web development, I asked a few friends to
have a look at the different parts of the article. They looked especially at
plain wrong statements, if I named "all" the important frameworks / tools. They
might not completely agree with the comparison to other language (after all, I
wrote the article), but they helped me a lot to get things not too wrong:

* [Sören Liebich](https://www.linkedin.com/pub/s%C3%B6ren-liebich/31/b2a/252)
  ([@liebsoer](https://twitter.com/liebsoer)) has several years of
  experience with Java web development and helped me to name the important
  tools / technologies used in the Java stack.
* Henning Dieterichs helped me to fix some of the mistakes in the C# part and
  reminded me of Hack and the positive sides of PHP.
* Stefan had a look at the PHP section.

Thank you!