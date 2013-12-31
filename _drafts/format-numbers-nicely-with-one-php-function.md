---
layout: post
title: Format numbers nicely with one PHP function
author: Martin Thoma
date: 2011-10-09 02:29:51
categories: 
- Code
tags: 
- PHP
- Web Development
featured_image: 2011/10/PHP-logo.png
---
I am currently writing a little web application to generate random passwords. I would also like to output some data about the password, e.g. how many possible passwords exist. Those numbers can get quite fast very big. They are not readable if you have an output like 1034013247894313498143981434. So we have to format them.

PHP has such a function built-in:
string <strong><a href="http://www.php.net/manual/en/function.number-format.php">number_format</a></strong> ( float <em>$number</em>, int <em>$decimals = 0</em>, string <em>$dec_point = '.'</em>, string <em>$thousands_sep = ','</em>)
As soon as you try it with some other numbers, you may encounter some problems:
[php]&lt;?php

echo number_format(123).&quot;&lt;br/&gt;&quot;;
echo number_format(-123).&quot;&lt;br/&gt;&quot;;
echo &quot;&lt;br/&gt;&quot;;
echo number_format(1234567890).&quot;&lt;br/&gt;&quot;;
echo number_format(-1234567890).&quot;&lt;br/&gt;&quot;;
echo &quot;&lt;br/&gt;&quot;;
echo number_format(0000000000123).&quot;&lt;br/&gt;&quot;;
echo number_format(-0000000000123).&quot;&lt;br/&gt;&quot;;
echo &quot;&lt;br/&gt;&quot;;
echo number_format(123.123235345).&quot;&lt;br/&gt;&quot;;
echo number_format(-123.123235345).&quot;&lt;br/&gt;&quot;;
echo &quot;&lt;br/&gt;&quot;;
echo number_format(pow(8,64)).&quot;&lt;br/&gt;&quot;;

?&gt;[/php]
{% highlight text %}123
-123

1,234,567,890
-1,234,567,890

83
-83

123
-123

6,277,101,735,386,680,763,835,789,423,207,666,416,102,355,444,464,034,512,896{% endhighlight %}

The first problem I see is the conversion into Octal (0000000000123 get 83), the second is the missing scientific notation (6.27 &middot; 10<pow>57</pow> instead of 6,277,101,735,386,680,763,835,789,423,207,666,416,102,355,444,464,034,512,896)


http://stackoverflow.com/search?q=php+number_format
WordPress MathJax - Latex - two plugins tested