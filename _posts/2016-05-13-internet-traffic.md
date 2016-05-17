---
layout: post
title: Internet Traffic
slug: internet-traffic
author: Martin Thoma
status: draft
date: 2016-05-13 20:00
category: Cyberculture
tags: Internet, Traffic, Volume, DSL
featured_image: logos/internet.png
---
Do you have any idea how much internet traffic (volume) you need? How much do
you download / upload on a usual day?

I didn't have any idea, so I started recording it. In this article I will show
you the results.

For the context: I am a computer science student from Karlsruhe, Germany.


## How to measure

Install `vnstat` and `vnstati`:

```bash
$ sudo apt-get install vnstat vnstati
```

Then execute

```bash
$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000
    link/ether 98:76:54:32:10:45 brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DORMANT group default qlen 1000
    link/ether 12:34:56:78:90:ab brd ff:ff:ff:ff:ff:ff
```

to find your network interface. In my case, it is `wlp3s0`. In most cases, it
will be `wlan0` or `eth0` if you use a cable.

To get the nice images, you have to execute the following code (with your
network interface). It will create a `summary.png` image:

```bash
$ vnstati -vs -i wlp3s0 -o ~/summary.png
```


## Results

To interpret the following, you should know that `rx` is the received traffic
and `tx` is the transferred traffic.

### Watching News

Watching the German 20 o'clock news (15 minutes on tagesschau.de) is about
200&thinsp;MiB rx and about 3&thinsp;MiB tx.


### Publishing Blog articles

For [ml-ka.de](https://ml-ka.de/) it is less than 10&thinsp;KiB.