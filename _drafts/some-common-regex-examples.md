---
layout: post
title: Some common RegEx examples
author: Martin Thoma
date: 2012-03-23 03:41:52
categories: 
- Code
- The Web
tags: 
- RegEx
featured_image: 
---
<h2>Numbers</h2>
<h3>non-negative even numbers</h3>
<strong>RegEx</strong>: [xml]^\d*[02468]$[/xml]
<strong>Description</strong>: All even numbers end with either 0, 2, 4, 6 or 8.
<strong>Matches</strong>: 12 | 2 | 012 | 4 | 44
<strong>Non-Matches</strong>: -12 | 3 | 13

<h3>Percentage</h3>
<strong>RegEx</strong>: [xml]^\d{0,2}(\.[0-9]{1,2})?$|^(100)(\.[0]{1,2})?$[/xml]
<strong>Description</strong>: All percentages with 0, 1 or 2 decimal places without the percent sign.
<strong>Matches</strong>: 0 | 0.0 | 0.00 | 12.42 | 100 | 100.0 | 100.00
<strong>Non-Matches</strong>: -12.42 | +12.42 | 112.42

<h2>Email</h2>
<strong>RegEx</strong>: [xml]^((?:(?:(?:\w[\.\-\+]?)*)\w)+)\@((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$[/xml]
Description: Not a 100% email validation. It doesn't work with IP-Adresses, but it's good for most common cases. At least I hope so.
<strong>Matches</strong>: a-b-c@d-e-f.com | a@b.ce | Me@my.museum
<strong>Non-Matches</strong>: abc@def.g | a--b@c--d.fe | -abc@-def-.def
<strong>Source</strong>: <a href="http://regexlib.com/REDetails.aspx?regexp_id=600">Sebastian Hiller</a>

<h2>See also</h2>
<ul>
  <li>docs.oracle.com: <a href="http://docs.oracle.com/javase/1.4.2/docs/api/java/util/regex/Pattern.html">Java Pattern Class</a></li>
  <li>php.net: <a href="http://php.net/manual/en/reference.pcre.pattern.syntax.php">PCRE Pattern Syntax</a></li>
</ul>