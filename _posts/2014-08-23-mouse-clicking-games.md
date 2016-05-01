---
layout: post
title: Mouse clicking games
author: Martin Thoma
date: 2014-08-23 14:15
category: Cyberculture
tags: Python, Games, Cheat
featured_image: logos/cookie-clicker.png
---

Do you know games like [cookie clicker](http://orteil.dashnet.org/cookieclicker/)
where you only have to click a lot?

{% caption align="aligncenter" width="500" alt="Cookie Clicker" text="Cookie Clicker" url="../images/2014/08/cookie-cliker.png" %}

You can do that automatically with the following Python script.

Just execute `xdotool getmouselocation --shell` before that to find the
position of your mouse.

```python
#!/usr/bin/env python

"""Tool to make automatic clicks VERY fast (useful for idle games)."""

import os
import time
import random


def main(clicks, twiggle, x, y, delay):
    for i in range(clicks):
        xrand = random.randint(-twiggle, twiggle)
        yrand = random.randint(-twiggle, twiggle)
        xpos, ypos = x+xrand, y+yrand
        os.system("xdotool mousemove %i %i click 1" % (xpos, ypos))
        if delay > 0:
            time.sleep(delay)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()

    # Add more options if you like
    parser.add_argument("-c", "--clicks", dest="clicks",
                        help="number of clicks that will be done",
                        default=500,
                        type=int)
    parser.add_argument("-t", "--twiggle", dest="twiggle",
                        help="how much should the cursor move randomly",
                        default=50,
                        type=int)
    parser.add_argument("-x", dest="x",
                        help="x coordinate where to click",
                        default=711,
                        type=int)
    parser.add_argument("-y", dest="y",
                        help="y coordinate where to click",
                        default=467,
                        type=int)
    parser.add_argument("--delay", dest="delay",
                        help="delay between clicks",
                        default=0.01,
                        type=float)
    args = parser.parse_args()
    main(args.clicks, args.twiggle, args.x, args.y, args.delay)

```

{% caption align="aligncenter" width="500" alt="Cookie Clicker after 5 minutes with a script" text="Cookie Clicker after 5 minutes with a script" url="../images/2014/08/cookie-clicker-5min.png" %}

Have fun playing those games now!