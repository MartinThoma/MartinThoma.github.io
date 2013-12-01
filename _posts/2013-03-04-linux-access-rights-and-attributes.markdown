---
layout: post
status: publish
published: true
title: Linux access rights and attributes
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 59161
wordpress_url: http://martin-thoma.com/?p=59161
date: 2013-03-04 22:29:42.000000000 +01:00
categories:
- Cyberculture
tags:
- Linux
- IT-Security
- gedit
- Bug
comments: []
featured_image: 2011/09/Tux.png
---
<h2>RWX</h2>
<h3>Files</h3>
Linux files have three important access rights for files:
<ul>
  <li><strong>R</strong>ead</li>
  <li><strong>W</strong>rite</li>
  <li>E<strong>x</strong>ecute</li>
</ul>

If you want to mark a file as executable, you can add the x-right:
{% highlight bash %}chmod +x{% endhighlight %}

When you want to mark a file as readable, you can dd the r-right:
{% highlight bash %}chmod +r{% endhighlight %}

You can remove rights in a similar way:
{% highlight bash %}chmod -x testfile{% endhighlight %}

Now, often this is expressed numerically. Three bits determine if the file is readable (4), writable (2) or executable (1). Did you notice that all of them are powers of two? 

<h3>Folders</h3>
rwx has a meaning for folders, too:
<ul>
  <li><strong>R</strong>ead: if that is missing, you can't use <code>ls</code> in the directory.</li>
  <li><strong>W</strong>rite: you need this to create new files / folders in the direcotry</li>
  <li><strong>x</strong> ... like "enter"?: if that is missing, you can't enter the directory.</li>
</ul>

<h2>User, Group, Others</h2>
The rights above can be set for the user who created the file (sometimes also called the owner). Then the group that owns the file and all others. This is the reason why you have three times the rights from above:

{% highlight bash %}
moose@pc07:~/Downloads$ ls -l
total 29624
drwxr-xr-x  8 moose moose     4096 2013-02-22 14:18 algorithms
-rw-r--r--  1 moose moose    60058 2013-02-11 08:00 args4j-2.0.21.jar
drwxr-xr-x  6 moose moose     4096 2013-02-25 20:07 bwinf
-rw-r--r--  1 moose moose 22160041 2013-02-05 16:45 DT2012.zip
drwxr-xr-x  8 moose moose     4096 2013-02-28 19:23 graphentheorie
-rw-r--r--  1 moose moose  2164878 2013-02-22 12:38 guava-14.0-rc1.jar
-rw-r--r--  1 moose moose  2705344 2013-03-01 21:07 HardVacuum.zip
drwxr-xr-x  8 moose moose     4096 2013-02-05 16:38 informatik-2011
-rw-r--r--  1 moose moose   111926 2013-02-24 19:09 Jim_Keener_resume.pdf
drwxr-xr-x  2 moose moose     4096 2011-11-08 11:50 juniper_linux
-rw-r--r--  1 moose moose   288666 2012-12-04 11:38 junit-4.11.jar
drwxr-xr-x 13 moose moose     4096 2013-02-01 23:33 LaTeX-examples
drwxr-xr-x  2 moose moose     4096 2009-08-11 17:04 otrdecoder
-rw-r--r--  1 moose moose   728292 2013-03-01 19:33 PlanetCute PNG.zip
drwxr-xr-x  2 moose moose     4096 2012-11-13 10:49 ProjectEuler
drwxr-xr-x  2 moose moose     4096 2013-03-04 20:28 Screenshots Matlab
-rw-r--r--  1 moose moose   764196 2013-03-04 20:28 Screenshots Matlab.zip
-rw-r--r--  1 moose moose   534614 2013-03-01 19:48 spritelib_gpl.zip
drwxr-xr-x  8 moose moose     4096 2013-02-27 18:36 Team
drwxr-xr-x  5 moose moose     4096 2013-02-27 19:17 ViMuDat
{% endhighlight %}

You might wonder what happens when you execute <code>chmod +x filename</code>. Does it set the execute-flag only for the user? Or for all three - user, group, others? Try and find out. You might want to remove all rights with <code>chmod 000 filename</code> before you start.

Did you know that you can search for file permissions with <code>find /home/ -perm 777</code>?

<h2>SUID, SGID, Sticky Bit</h2>
<h3>Files</h3>
Sometimes, you want to execute programs as root, although the user who started the execution isn't root. Take passwd, the program that allows users to change passwords, for example:

{% highlight bash %}moose@pc07:/usr/bin$ ls -l | grep passwd$
-rwsr-xr-x 1 root   root       53812 2011-02-14 23:11 gpasswd
-rwxr-xr-x 1 root   root       13612 2012-11-06 21:41 htpasswd
-rwsr-xr-x 1 root   lpadmin    13540 2012-12-04 16:24 lppasswd
-rwsr-xr-x 1 root   root       37140 2011-02-14 23:11 passwd
-rwxr-xr-x 1 root   root     5070304 2012-04-24 23:38 smbpasswd
-rwxr-xr-x 1 root   root        9688 2013-01-18 17:59 vino-passwd
{% endhighlight %}

Instead of "x" in the user-execution-row, it states "s". That means, you can execute it and it has the SUID-bit set. If "x" wasn't set, the "S" would be in a capital letter. When you change your password, you need to edit <code>/etc/shadow</code>. This file has very limited access rights: <code>-rw-r