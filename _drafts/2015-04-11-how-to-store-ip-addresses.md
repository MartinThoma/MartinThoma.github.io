---
layout: post
title: How to store IP addresses
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- database
- MySQL
- IPv4
- IPv6
featured_image: logos/maria-db.png
---
You hava a couple of possibilities when you want to store IP addresses. But
first take a look at some examples:

```text
192.168.0.1
255.255.255.255
2001:0db8:0000:0000:0000:ff00:0042:8329
2001:db8:0:0:0:ff00:42:8329
```

You might know that IPv4 has 4 blocks from 0-255 (hence 32 bit) and IPv6 has
128 bit.

You might also be interested in [How to convert an address from IPv4 to IPv6](http://stackoverflow.com/a/1555659/562769) and [6to4](https://en.wikipedia.org/wiki/6to4).

## PHP


## Python

IPy


## See also

* [Storing IP Address in Mysql Database](http://blog.chatwee.com/2014/02/storing-ip-address-in-mysql-database/)
* [How to convert IPv6 from binary for storage in MySQL](http://stackoverflow.com/a/1619332/562769)
