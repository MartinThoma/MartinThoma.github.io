---
layout: post
title: How can I sketch an application?
author: Martin Thoma
date: 2012-12-20 01:54:57.000000000 +01:00
categories:
- Code
- The Web
tags:
- Web Development
- Software Development
- Balsamiq
- mockup
- sketch
featured_image: 2012/12/balsamiq-mockup.png
---
I've recently participated in a medium size software project. This project is rather fixed for a web project, so we don't suffer from rapid changes ("rapid" in terms of other web applications), but nether the less they change. The task seemed to be clear at the beginning, but bit for bit my team of developers discovered details that were not so clear. In this project I have learned that a GUI / prototype driven development can be of great benefit. I assumed this beforehand, but I didn't expect how much it helped.

So, I had the idea to create a good GUI to have something to talk about. How do you create a GUI for a web project? 

<h2>HTML</h2>
<ul>
  <li>is quite simple</li>
  <li>I know it very well</li>
  <li>everything I write is obviously possible to realize</li>
</ul>

but 

<ul>
  <li>the result looks too much like the resulting product. The customer might think that we already have some functional prototype
  <li>it is also unsatisfying to print HTML pages or screenshots of rendered browser views</li>
  <li>although HTML is easy, arranging items on a screen might take a while</li> 
</ul>

<h2>GIMP</h2> 
GIMP was the next option I tried, but its disadvantage is too severe to think seriously about using it for rapid GUI prototyping: It takes ages!

A friend of mine helped me out of my misery. He told me of a product called "<a href="http://www.balsamiq.com/">Balsamiq</a>". 

<h2>Balsamiq</h2>
Balsamiq is easy to use, has a lot of very intuitive features and is able to generate a linked PDF. This means, you can add links to some parts of the interface and simulate interactivity. The user should have opened the slides in full screen, so that on slide fills the screen. Then you might even think it was an web application.

Here is <a href='../images/2012/12/Scientific-publishing.pdf'>an example PDF created with Balsamiq</a>

<h3>What's great about Balsamiq</h3>
Balsamiq was carefully designed, is available (and working!) on Windows 7 and Ubuntu 10.04 and via browser. The learning curve is very well. I keep finding new features as I need them. So I first intuitively found the most important ones and recognized advanced ones later.

Here are two screenshots of the GUI of the Balsamiq web service:

{% caption align="aligncenter" width="300" caption="Balsamiq GUI overview" url="../images/2012/12/balsamiq-tabs-bar-300x137.png" alt="Balsamiq GUI overview" title="Balsamiq GUI overview" height="137" class="size-medium wp-image-51021" %}

Do you see the arrow-symbol? This looks very cool in drafts. Why doesn't GIMP provide anything similar?

{% caption align="aligncenter" width="300" caption="Edit an element with Balsamiq" url="../images/2012/12/balsamiq-edit-300x138.png" alt="Edit an element with Balsamiq" title="Edit an element with Balsamiq" height="138" class="size-medium wp-image-51031" %}

<h3>What I've missed</h3>
No application is perfect, so I also found some specials that Balsamiq didn't offer:
<ul>
  <li>Form elements in tables</li>
  <li>Adjusting table column width</li>
</ul>

I've found workarounds for both problems, but I guess there could be a better way to solve it. Nevertheless, Balsamiq is a great application that might help a lot to develop great software!
