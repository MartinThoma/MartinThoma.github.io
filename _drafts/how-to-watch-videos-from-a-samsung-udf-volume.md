---
layout: post
title: How to watch videos from a Samsung UDF Volume
author: Martin Thoma
date: 2012-04-12 07:14:25
categories: 
- Code
tags:
- Videos
- DVD
featured_image: 
---
I recently had a DVD which I couldn't watch directly. I think I forgot to finalize it. It got mounted as "Samsung UDF Volume":

```bash
moose@pc07:~$ mount
/dev/sda1 on / type ext4 (rw,errors=remount-ro,user_xattr)
proc on /proc type proc (rw,noexec,nosuid,nodev)
none on /sys type sysfs (rw,noexec,nosuid,nodev)
none on /sys/fs/fuse/connections type fusectl (rw)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
none on /dev type devtmpfs (rw,mode=0755)
none on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
none on /dev/shm type tmpfs (rw,nosuid,nodev)
none on /var/run type tmpfs (rw,nosuid,mode=0755)
none on /var/lock type tmpfs (rw,noexec,nosuid,nodev)
none on /lib/init/rw type tmpfs (rw,nosuid,mode=0755)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,noexec,nosuid,nodev)
gvfs-fuse-daemon on /home/moose/.gvfs type fuse.gvfs-fuse-daemon (rw,nosuid,nodev,user=moose)
```

So I umounted it:
{% highlight bash %}root@pc07:/home/moose# umount /media/Samsung\ UDF\ Volume/{% endhighlight %}

And copied the content (took quite a while):
{% highlight bash %}root@pc07:/home/moose# readom dev=/dev/cdrom f=file.iso{% endhighlight %}