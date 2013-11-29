---
layout: post
status: publish
published: true
title: Check Computer / Hardware for Linux-compatibility
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 12691
wordpress_url: http://martin-thoma.com/?p=12691
date: 2012-01-27 20:42:21.000000000 +01:00
categories:
- Cyberculture
tags:
- Linux
- Hardware
comments: []
---
Linux users who are not very skilled have a big problem: If they want to buy a new computer or new hardware, it is very difficult for them to find out if something works or not. I'll give you some hints how you could find it out:

<h2>Debian device driver check & report</h2>
<a href="http://kmuto.jp/debian/hcl/">This site</a> checks your whole system. You only need to boot a Linux system (e.g. via <a href="http://en.wikipedia.org/wiki/Live_CD">LiveCD</a>) and execute:
{% highlight bash %}lspci -n{% endhighlight %} in the terminal (which pops up if you type Ctrl + Alt + T). Copy it, paste it into the provided form and you will get a list of your hardware and simply "Yes" if this component works with Debian.

<h2>Linux HCL</h2>
The <a href="http://linuxhcl.com/">Linux HCL</a> provides a lot of hand-written reviews of users. Here is my <a href="http://linuxhcl.com/browse/product?id=7719">review of my notebook</a>.

<h2>UbuntuUsers</h2>
German users might want to take a look at the wiki-article "<a href="http://wiki.ubuntuusers.de/Hardwaredatenbanken">Hardwaredatenbanken</a>".
