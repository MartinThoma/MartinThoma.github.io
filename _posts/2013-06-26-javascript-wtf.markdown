---
layout: post
status: publish
published: true
title: ! 'JavaScript: WTF?!?'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 71601
wordpress_url: http://martin-thoma.com/?p=71601
date: 2013-06-26 22:51:52.000000000 +02:00
categories:
- Code
tags:
- JavaScript
comments:
- id: 1237724
  author: Leo
  author_email: neuman.il@gmail.com
  author_url: ''
  date: !binary |-
    MjAxMy0wOC0yOCAxMDozODoxOSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wOC0yOCAwODozODoxOSArMDIwMA==
  content: ! "Thanks for the post!\r\n\r\nIf you haven't seen it already, check out
    Gary Bernhardt's short talk (starts with Ruby but gets to JS):\r\n\r\nhttps://www.destroyallsoftware.com/talks/wat\r\n\r\nL."
- id: 1237740
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wOC0yOSAxNzoxMTozNiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wOC0yOSAxNToxMTozNiArMDIwMA==
  content: Haha, hilarious! Thank you for sharing!
featured_image: 2013/06/javascript-thumb.png
---
JavaScript is THE web programming language. It gets interpreted by your browser and web applications like Google Mail, Google Maps and Facebook make heavy use of them. Almost always, when you see something working smoothly / interactive, you see JavaScript in action.

But JavaScript has a lot of "features" which are ... well, I don't have words for those. Just continue reading.

Most of the following content is from a StackOverflow question <a href="http://stackoverflow.com/q/1995113/562769">Strangest language feature</a>

<h2>Weak typing</h2>
<strong>Example</strong>
{% highlight javascript %}console.log(3..toString());{% endhighlight %}

<strong>Output</strong>
{% highlight bash %}'3'{% endhighlight %}

<strong>Explanation</strong>
<strong>3.</strong> is a floating point and can get converted to a string. But <code>3.toString()</code> gives 
{% highlight bash %}SyntaxError: Unexpected token ILLEGAL {% endhighlight %}

<h2>Weak typing and string concatenation</h2>
<strong>Example</strong>
{% highlight javascript %}
console.log('5' + 3);
console.log('5' - 3);
{% endhighlight %}

<strong>Output</strong>
{% highlight bash %}'53'
2{% endhighlight %}

<strong>Explanation</strong>
JavaScript automatically converts datatypes and <code>+</code> is used for string concatenation and for addition. 

In the first case, as the first datatype is a string and <code>+</code> is defined for strings as concatenation, JS converts <code>3</code> to <code>'3'</code> which results in the string <code>'53'</code>.

In the second case, <code>-</code> is only defined for subtraction so <code>'5'</code> gets converted to a number (int? float? I don't know. I guess int.)

<h2>Automatic semicolons</h2>
<strong>Example 1</strong>

{% highlight javascript %}
function test() {
    return
    {
        id : 1338,
        title : 'This is a test'
    };
}

console.log(test());
{% endhighlight %}

<strong>Example 2</strong>
{% highlight javascript %}
function test() {
    return
        2 + 2;
}

console.log(test());
{% endhighlight %}

<strong>Output 1</strong>
{% highlight bash %}Uncaught SyntaxError: Unexpected token :{% endhighlight %}

<strong>Output 2</strong>
{% highlight bash %}undefined{% endhighlight %}

<strong>Explanation</strong>
JS adds a <code>;</code> at every line end. Automatically. You can't prevent it.

Please note that the second output is no error! It has a (valid) return value of <code>undefined</code>.

<h2>Truth table</h2>
<strong>Example</strong>
{% highlight javascript %}
console.log("