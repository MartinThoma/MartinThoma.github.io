---
layout: post
status: publish
published: true
title: DNS-Services
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 62231
wordpress_url: http://martin-thoma.com/?p=62231
date: 2013-07-20 14:46:34.000000000 +02:00
categories:
- The Web
tags:
- DNS
comments: []
---
I've just read (ok, now it's over 3 months ago) that <a href="http://en.wikipedia.org/wiki/Google_Public_DNS">Google Public DNS</a> now supports DNSSEC (<a href="http://googleonlinesecurity.blogspot.de/2013/03/google-public-dns-now-supports-dnssec.html">source</a>).

I was curious what I currently use on my Linux Mint 14 machine. The relevant file is <strong>/etc/resolv.conf</strong>:
[text]nameserver 127.0.1.1

# OpenDNS Fallback (configured by Linux Mint in /etc/resolvconf/resolv.conf.d/tail).
nameserver 208.67.222.222
nameserver 208.67.220.220
[/text]


<h2>namebench</h2>
A programm called <a href="https://code.google.com/p/namebench">namebench</a>  checks how fast several DNS configurations would be for you.

[caption id="attachment_62241" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/namebench.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/namebench-300x222.png" alt="namebench" width="300" height="222" class="size-medium wp-image-62241" /></a> namebench[/caption]

<h2>Further reading</h2>
<ul>
  <li><a href="http://wiki.ubuntuusers.de/Dnsmasq">Dnsmasq</a> (German)</li>
  <li><a href="http://www.debian.org/doc/manuals/debian-reference/ch05.en.html#_the_hostname_resolution">Debian manual - The hostname resolution</a>: explains where 127.0.1.1 comes from</li>
</ul>
