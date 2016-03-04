---
layout: post
title: Disable Caps Lock
author: Martin Thoma
date: 2016-03-04 10:59
category: Cyberculture
tags:
- Ubuntu
featured_image: logos/caps-lock.png
---
I've just hit caps lock accidentially. This key is so useless; I never ever
wanted to hit it.

So I deactivated it:

```bash
$ setxkbmap -option caps:none
```

To run this every time at startup, I've added it to `/etc/rc.local`.
However, it did not work. I guess it is executed to soon.

An alternative which worked is adding a file `~/.config/shift.deskop` with the
following content:

```
[Desktop Entry]
Type=Application
Name=shift
Exec=setxkbmap -option caps:none
X-GNOME-Autostart-enabled=true
```


No more issues with caps lock ♡.
