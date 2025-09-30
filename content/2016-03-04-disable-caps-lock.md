---
layout: post
lang: en
title: Disable Caps Lock
slug: disable-caps-lock
author: Martin Thoma
date: 2016-03-04 10:59
category: Cyberculture
tags: Ubuntu
featured_image: logos/caps-lock.png
---
I've just hit caps lock accidentally. This key is so useless; I never ever
wanted to hit it.

So I deactivated it:

```bash
$ setxkbmap -option caps:none
```

To run this every time at startup, I've added it to `/etc/rc.local`.
However, it did not work. I guess it is executed to soon.

An alternative which worked is adding a file `~/.config/shift.deskop` with the
following content:

```ini
[Desktop Entry]
Type=Application
Name=shift
Exec=setxkbmap -option caps:none
X-GNOME-Autostart-enabled=true
```


No more issues with caps lock ♡.


## More functionality

I've just received a remark by [Micha](http://plasisent.org/) that one could
add useful functionality. For example with
[Xmodmap](https://github.com/rosetree/tildeslash/blob/master/.Xmodmap) or
within the [Ubuntu settings](https://help.ubuntu.com/stable/ubuntu-help/keyboar
d-shortcuts-set.html) one can make this a [compose
key](https://en.wikipedia.org/wiki/Compose_key) for special characters such as
·×⋄.
