---
layout: post
title: What is a forward/reverse proxy?
slug: what-is-a-forward-reverse-proxy
lang: en
author: Martin Thoma
date: 2024-08-18 08:58
category: The Web
tags: Web Development, Internet
featured_image: logos/web.png
summary: A proxy forwards requests. They can filter or change requests.
medium_url: https://medium.com/@martinthoma/what-is-a-forward-reverse-proxy-4e798c178ee5
---
<figure>
    <a href="../images/2024/08/what-is-a-forward-reverse-proxy-1.png"><img src="../images/2024/08/what-is-a-forward-reverse-proxy-1.png" alt="Diagram: a client in its internal network talks to a forward proxy, which connects over the internet to a proxy in front of the server in another internal network" width="800" height="211"></a>
    <figcaption>Image created by Martin Thoma.</figcaption>
</figure>

A **proxy** forwards requests. They can filter or change requests.

A **forward proxy** takes a request for the user and forwards it to a website. Examples are:

* [Privoxy](https://en.wikipedia.org/wiki/Privoxy): A forward proxy which helps to protect privacy ([German Talk](https://media.ccc.de/v/froscon2016-1808-das_privoxy-okosystem) from 2016). You can also block advertisement with it.
* [Charles Proxy](https://www.charlesproxy.com/): Allows you to monitor and manipulate traffic. [Charles Proxy can be used for testing](https://medium.com/@jagjeetjohal/mastering-api-testing-with-charles-proxy-how-to-monitor-and-manipulate-http-traffic-like-a-pro-4e48689a52e1).

A **reverse proxy** takes a request for a website and forwards it to a server. They can be used for caching and load balancing. Examples for reverse proxies are [nginx](https://nginx.org/en/) or the Apache HTTP Server with [mod\_proxy](https://httpd.apache.org/docs/current/mod/mod_proxy.html).
