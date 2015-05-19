---
layout: post
title: PID-Controller
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Controller
featured_image: logos/star.png
---
PID controllers have three parts:

* Proportional part: Tries to ge to the required output
* Integral part: Tries to fix long-term errors
* Derivative part: Tries to react to change

So for a PID controller you are given a current state, a target state, some
value $\alpha$ you can adjust to get to the target state as well as some rule
how adjustments to $\alpha$ will change your current state. Sadly, there is
the environment. Nothing is perfect, so the value your rule gives will not be
completely accurate. You have an error. The PID controller should keep that
error as small as possible

## Steering

## Water temperature

## Acceleration of a car


## See also

* [PID Control - A brief introduction](https://www.youtube.com/watch?v=UR0hOmjaHp0) 7:43 min + [Simple Examples of PID Control](https://www.youtube.com/watch?v=XfAt6hNV8XM) 13:09 min
* http://www.frustfrei-lernen.de/thermodynamik/waermeenergie.html