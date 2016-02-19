---
layout: post
title: Scan the LAN
author: Martin Thoma
date: 2014-11-22 17:19
category: Cyberculture
tags:
- Rating
- Linux
featured_image: logos/star.png
---

## Requirements

```bash
$ sudo apt-get install nmap
```


## Host discovery

```bash
$ nmap -sP 192.168.2.1/24
```


## See also

* [How to find live hosts on my network?](http://security.stackexchange.com/q/36198/3286)