---
layout: page
title: About Me
author: Martin Thoma
date: 2011-09-21 18:35:30.000000000 +02:00
categories: []
tags: []
context: about
gplus: https://plus.google.com/+MartinThoma/about
twitter: https://twitter.com/#!/themoosemind
stackoverflow: http://stackoverflow.com/users/562769/moose
alias: /author/moose/index.html
---
<div class="vcard">
{% caption align="alignright" width="134" height="200" alt="Martin Thoma" caption="Martin Thoma" url="../../images/2011/09/Martin_Thoma_web_thumb.jpg" class="size-full photo" %}

<p>My name is <span class="fn">Martin Thoma</span>. I am a <time class="dt-bday" datetime="1990-04-28">24 year</time> old student from <span class="locality">Karlsruhe, Germany</span>.</p>

<p>Do you want to know more about me? I've created a <a href="../../pdf/cv-curriculum-vitae.pdf">short English CV</a> and <a href="http://www.martin-thoma.de/about.htm" rel="me">a longer German CV</a>.</p>

<p><small>(This page was last updated on <time class="updated" datetime="{{ page.path | file_date | date_to_xmlschema }}">{% assign d = page.path | file_date | date: "%d" | plus:'0' %}
                                {{ page.path | file_date | date: "%B" }} 
                                {% case d %}
                                  {% when 1 or 21 or 31 %}{{ d }}st,
                                  {% when 2 or 22 %}{{ d }}nd,
                                  {% when 3 or 23 %}{{ d }}rd,
                                  {% else %}{{ d }}th,
                                  {% endcase %}
                                {{ page.path | file_date | date: "%Y" }}</time>).</small></p>

<h2>Other Profiles</h2>
<ul>
	<li><a href="{{ page.gplus }}" rel="me">Google+</a></li>
	<li><a href="{{ page.twitter }}" rel="me">Twitter</a></li>
    <li><a href="{{ page.stackoverflow }}" rel="me">StackOverflow</a></li>
</ul>
</div>