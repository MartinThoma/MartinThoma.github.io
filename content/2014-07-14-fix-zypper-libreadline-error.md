---
layout: post
title: Fix zypper readline error
author: Martin Thoma
date: 2014-07-14 11:34
category: Code
tags: openSUSE
featured_image: logos/open-suse.png
---

In case you work on a openSUSE system and you get the following error

```bash
$ zypper
zypper: symbol lookup error: /usr/lib/libreadline.so.6: undefined symbol: PC
```

you can probably "fix" it by setting the 64 Bit `LD_LIBRARY` like this:

```bash
$ export LD_LIBRARY_PATH=/lib64:$LD_LIBRARY_PATH
```

It worked for me on openSUSE 12.1 "Asparagus".

## Credits

Thanks to [JRSETI's Blog](http://jrseti.blogspot.com/2011/09/zypper-does-not-work-on-opensuse-fixed.html)
