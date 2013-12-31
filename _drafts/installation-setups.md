---
layout: post
title: Installation setups
author: Martin Thoma
date: 2011-11-16 11:59:37
categories: 
- Cyberculture
tags: 
- Administration
featured_image: 2011/11/computer-fix-it-guy.jpg
---
I am currently reinstalling my operating system. As I am quite often reinstalling it, I have written a little shell script which helps me doing it.

This is the procedure I use when I want to reinstall a new (Ubuntu) Linux system:

<h2>Save old data</h2>
I am copying every file I want to have manually to my external hard disk. 

Alternatives are:
<ul>
  <li><strong>Cloud Storage</strong>: e.g. Ubuntu One</li>
  <li><strong>Partitions</strong>: As soon as Ubuntu works out of the box with my notebook I'll use a seperate /home partition. This means I can remove the old system partitions without loosing my configuration / data.</li>
  <li>Auto</li>
</ul>

<h2>Install the new System</h2>
I am always deleting every kind of data of my old partition.

<h2>Configuring the new system</h2>
<h3>Update</h3>
and restart

<h3>Installing everything</h3>
{% highlight bash %}dpkg -s mysql-server{% endhighlight %}