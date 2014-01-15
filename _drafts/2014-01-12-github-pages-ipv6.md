---
layout: post
title: GitHub pages and IPv6
author: Martin Thoma
categories:
- The Web
tags:
- GitHub
- IPv6
featured_image: 2014/01/github-logo.png
description: GitHub pages do currently not support IPv6.
---

After my switch from WordPress to Jekyll which included a switch
from my former provider to GitHub, I was very surprised that I could
no longer access my site from university. After some investigation a
fellow student suggested that IPv6 might be the reason.

So I've [checked my public IP address](http://canhazip.com/),
pinged my site

```bash
moose@pc08$ ping martin-thoma.com
PING martin-thoma.com (204.232.175.78) 56(84) bytes of data.
64 bytes from pages.github.com (204.232.175.78): icmp_req=1 ttl=47 time=100 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=2 ttl=47 time=101 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=3 ttl=50 time=101 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=4 ttl=47 time=95.5 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=5 ttl=47 time=99.1 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=7 ttl=50 time=101 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=8 ttl=47 time=99.7 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=9 ttl=47 time=95.5 ms
64 bytes from pages.github.com (204.232.175.78): icmp_req=10 ttl=47 time=95.8 ms
^C
--- martin-thoma.com ping statistics ---
10 packets transmitted, 9 received, 10% packet loss, time 9020ms
rtt min/avg/max/mdev = 95.547/98.869/101.445/2.395 ms
```

and tried tracerout

```bash
moose@pc08$ traceroute martin-thoma.com
traceroute to martin-thoma.com (204.232.175.78), 30 hops max, 60 byte packets
 1  defgw-kit-intra-1x.scc.kit.edu (141.3.208.1)  104.971 ms  104.945 ms  104.921 ms
 2  tr-v1311-rircs1.scc.kit.edu (129.13.73.9)  104.901 ms  104.888 ms  104.871 ms
 3  tr-v825-fwinetkit.scc.kit.edu (141.52.249.149)  3.210 ms  3.398 ms  3.356 ms
 4  tr-v824-rircn1.scc.kit.edu (141.52.249.138)  104.783 ms  104.768 ms  104.750 ms
 5  xr-fzk1-te1-3-906.x-win.dfn.de (188.1.38.221)  104.676 ms  104.658 ms  104.630 ms
 6  cr-fra1-te0-7-0-3.x-win.dfn.de (188.1.144.121)  8.077 ms  6.895 ms  58.975 ms
 7  xe-1-2-0.mpr1.fra4.de.above.net (80.81.194.26)  58.956 ms  54.090 ms  52.243 ms
 8  ae1.mpr1.cdg11.fr.above.net (64.125.32.78)  14.592 ms  14.580 ms  14.566 ms
 9  xe-0-0-0.mpr2.cdg12.fr.above.net (64.125.26.74)  14.553 ms  14.750 ms  14.688 ms
10  ae3.mpr2.lhr2.uk.above.net (64.125.32.98)  20.846 ms  20.789 ms  20.778 ms
11  ae4.cr1.dca2.us.above.net (64.125.20.73)  95.859 ms  94.280 ms  96.384 ms
12  ae1.cr2.dca2.us.above.net (64.125.28.242)  95.036 ms  94.971 ms  94.985 ms
13  xe-1-1-0.er2.dca2.us.above.net (64.125.26.178)  96.828 ms  94.926 ms  128.439 ms
14  208.185.125.154.IPYX-076520-921-ZYO.above.net (208.185.125.154)  95.583 ms  95.575 ms  95.564 ms
15  corea-edge6.iad2.rackspace.net (69.20.2.56)  102.147 ms  102.090 ms coreb-edge6.iad3.rackspace.net (69.20.2.58)  95.452 ms
16  corea-czi1.iad2.rackspace.net (69.20.2.137)  96.972 ms  96.934 ms  96.869 ms
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
```

After that, I've contacted GitHub and got. They gave me pretty fast
an answer:

> I am afraid we generally don't support IPv6 currently. It might be 
worth the trouble to try the normal A record and see if that fixes 
the problem.
