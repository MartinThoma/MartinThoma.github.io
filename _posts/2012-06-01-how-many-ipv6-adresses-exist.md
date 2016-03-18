---
layout: post
title: How many IPv6 adresses exist?
author: Martin Thoma
date: 2012-06-01 18:43:22.000000000 +02:00
categories:
- The Web
tags:
- Numbers
---
<h2>Some general information</h2>
<iframe width="512" height="288" src="http://www.youtube.com/embed/-Uwjt32NvVA" frameborder="0" allowfullscreen></iframe>

A typical IPv4 address in a local network looks like this:
<code>192.168.0.1</code>
This is <code>11000000 10101000 00000000 00000001</code> in binary octets. You can easily see that it has 32 bits. 
As one bit may have two values - 0 or 1 - there are $2^{32} = 4,294,967,296 \approx 4.3 \cdot 10^9$ possible addresses.
The internet needs IP-addresses to know which information should be sent to whom. So only 4.3 billion devices can be connected to the internet. Devices are home computers (your PCs), servers (of big companies like Google or Facebook), Smartphones. So we are currently getting out of addresses. To solve this problem, IPv6 was introduced.

<h2>Pure Numbers</h2>
IPv6 has 128 bit. This means there are the number of addresses is:
$2^{128} = 340282366920938463463374607431768211456 \approx 3.4 \cdot 10^{38}$

Quite a lot.

<h2>Playing with numbers</h2>
Imagine the world had 10 billion people ($10,000,000 = 10 \cdot 10^9 = 10^{10}$). Imagine everyone bought 6 smartphones, 5 computers, 1 car, 4 tablet, 4 car radios in every year. That would be 20 internet devices for every person every year. Now you could give every device a unique address for much, much more than billion billion years! The sun is going to get a <a href="http://en.wikipedia.org/wiki/Red_giant">red giant</a> in about 4 billion years, so this is nothing we have to worry about.
Calculation: $\frac{2^{128}}{10^{10} \cdot 20} \approx 1.7 \cdot 10^{34}$

<h2>See also</h2>
<ul>
  <li>Wikipedia: <a href="http://en.wikipedia.org/wiki/Internet_Protocol">Internet Protocol</a></li>
  <li>UbuntuUsers: <a href="http://ikhaya.ubuntuusers.de/2012/06/01/ipv6-ueberblick/">IPv6</a> (German)</li>
</ul>
