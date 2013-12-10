---
layout: post
status: publish
published: true
title: Surprising C errors
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 8601
wordpress_url: http://martin-thoma.com/?p=8601
date: 2011-12-28 15:18:43.000000000 +01:00
categories:
- Code
tags:
- Programming
- learning
- C
comments:
- id: 24081
  author: Rene Pickhardt
  author_email: r.pickhardt@gmail.com
  author_url: http://www.rene-pickhardt.de
  date: !binary |-
    MjAxMS0xMi0yOCAxNjozNDowNiArMDEwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0yOCAxNDozNDowNiArMDEwMA==
  content: ! "int main()\r\n{\r\n    int x = 42;\r\n    while( x > 0 );\r\n        x--;\r\n
    \   return 0;\r\n}\r\n\r\nline 4 has a \";\" after the while. So you are running
    a loop with no statments. \r\n\r\nif you do not start a new scope with { and }
    then the next stament after a loop expression is executed. Your next statement
    is not x--; but your statement is the empty statement \";\" of course this results
    in an infinity loop. I guess it is the same in java. And in particular it has
    no connection to x=42 (-:"
- id: 24101
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMS0xMi0yOCAxNzowNzoxMSArMDEwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0yOCAxNTowNzoxMSArMDEwMA==
  content: ! "Correct. I think this is a tricky one as too much ; aren't important
    most of the time. Just like the macro-one.\r\n\r\n<blockquote>And in particular
    it has no connection to x=42 (-:</blockquote>\r\nAre you sure? I don't know
    the question, but 42 is the answer ;-)"
featured_image: 2011/12/compare-programming-languages.png
---
Those errors might be surprising and a good exercise for C beginners:

<h2>Empty printf</h2>
[c]#include <stdio.h>

int main()
{
    printf("");
    return 0;
}[/c]
{% highlight bash %}error: zero-length gnu_printf format string{% endhighlight %}

<h2>Macros</h2>
[c]#include <stdio.h>
#define MY_MACRO printf("Hello World\n");

int main()
{
    if (1)
        MY_MACRO;
    else
        printf("Crazy, huh?\n");

    return 0;
}[/c]
{% highlight bash %}macro.c: In function &lsquo;main&rsquo;:
macro.c:8: error: &lsquo;else&rsquo; without a previous &lsquo;if&rsquo;{% endhighlight %}

<h2>Single and Double quotes</h2>
[c]#include <stdio.h>

int main()
{
    printf('hello, world\n');
    return 0;
}[/c]
{% highlight bash %}macro.c:5:9: warning: character constant too long for its type
macro.c: In function &lsquo;main&rsquo;:
macro.c:5: warning: passing argument 1 of &lsquo;printf&rsquo; makes pointer from integer without a cast
/usr/include/stdio.h:339: note: expected &lsquo;const char * __restrict__&rsquo; but argument is of type &lsquo;int&rsquo;
macro.c:5: warning: format not a string literal and no format arguments
{% endhighlight %}

Thanks to <a href="http://www.drpaulcarter.com/cs/common-c-errors.php#3.1">drpaulcarter.com</a> for this example:
[c]int main()
{
    const char * myPointer = 'A';
    (void) myPointer;
    return 0;
}[/c]
{% highlight bash %}macro.c: In function &lsquo;main&rsquo;:
macro.c:3: warning: initialization makes pointer from integer without a cast
{% endhighlight %}

<h2>Pointers</h2>
[c]#include <string.h>

int main()
{
    char * myPointer;

    strcpy(myPointer, "Hello World!");
    return 0;
}[/c]
{% highlight bash %}macro.c: In function &lsquo;main&rsquo;:
macro.c:7: warning: &lsquo;myPointer&rsquo; is used uninitialized in this function
{% endhighlight %}

<h2>Loops</h2>
[c]int main()
{
    int x = 42;
    while( x > 0 );
        x--;
    return 0;
}[/c]
No compiler error, but an infinite loop.

<h2>Null terminator of Strings</h2>
[c]#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char myArray[20];
    printf("Characters: %i\n", strlen(myArray));
    strcpy(myArray, "abc");
    printf("Characters: %i\n", strlen(myArray));
    strcpy(myArray, "Hello World!"); 
    printf("Characters: %i\n", strlen(myArray));
    printf("String: -%s-\n", myArray);
    printf("Size: %i Byte\n\n", sizeof(myArray));

    char * myString = malloc(strlen(myArray));
    strcpy(myString, myArray);
    printf("String: -%s-\n", myString);
    printf("Size: %i Byte\n", sizeof(myString));
    printf("Characters: %i\n\n", strlen(myString));

    char * breakIt = malloc(strlen(myString));
    strcpy(breakIt, myString);
    printf("String: -%s-\n", breakIt);
    printf("Size: %i Byte\n", sizeof(breakIt));
    printf("Characters: %i\n", strlen(breakIt));

    return 0;
}[/c]
Again, you don't get a compiler error, but some strange results:
{% highlight bash %}Characters: 0
Characters: 3
Characters: 12
String: -Hello World!-
Size: 20 Byte

String: -Hello World!-
Size: 4 Byte
Characters: 12

String: -Hello World!-
Size: 4 Byte
Characters: 13
{% endhighlight %}

<h2>Further reading</h2>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/C_preprocessor">C Preprocessor</a> and <a href="http://en.wikipedia.org/wiki/C_preprocessor#Macro_definition_and_expansion">macros</a></li>
  <li><a href="http://www.drpaulcarter.com/cs/common-c-errors.php#2.8">Pointer initialisation</a></li>
  <li><a href="http://linux.die.net/man/3/strcpy">strcpy</a>, <a href="http://linux.die.net/man/3/strlen">strlen</a></li>
</ul>
