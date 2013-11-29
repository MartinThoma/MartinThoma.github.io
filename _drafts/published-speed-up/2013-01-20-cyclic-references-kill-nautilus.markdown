---
layout: post
status: publish
published: true
title: Cyclic references kill Nautilus
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 54541
wordpress_url: http://martin-thoma.com/?p=54541
date: 2013-01-20 21:46:34.000000000 +01:00
categories:
- Code
- Cyberculture
tags:
- OS
- Operating Systems
- GNOME
- file manager
- Bug
comments:
- id: 1122751
  author: Stefan Koch
  author_email: blog@stefan-koch.name
  author_url: http://stefan-koch.name/
  date: !binary |-
    MjAxMy0wMS0yMSAwODowNDoyMiArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0yMSAwNzowNDoyMiArMDEwMA==
  content: ! "Actually, you don&rsquo;t have to create a temp-file to create a symlink.
    ln -s does not check for the existance of a file.\r\n\r\nbrati ~ $ ln -s foo3
    foo2\r\nbrati ~ $ ln -s foo2 foo3\r\n\r\nis totally fine.\r\n\r\nBut what I actually
    wanted to say, in PCManFM it works quite fine :)"
- id: 1122801
  author: Keba
  author_email: mariofuest@aol.com
  author_url: ''
  date: !binary |-
    MjAxMy0wMS0yMSAyMDo1NjoxNyArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMS0yMSAxOTo1NjoxNyArMDEwMA==
  content: ! "> I know, the current version of Nautilus is 3.6.1,\r\n\r\nIt&lsquo;s
    3.6.3 on my Arch Linux system here and I cannot reproduce the bug. Semms to be
    fixed by now."
---
I just wanted to answer an assignment and noticed that cyclic references kill Nautilus.

<h2>What I did</h2>
{% highlight bash %}mkdir testFolder
cd testFolder
touch testFile.txt
ln -s testFile.txt mySoftlink
rm testFile.txt
ln -s mySoftlink testFile.txt
ls -l
total 0
lrwxrwxrwx 1 moose moose 10 2013-01-20 21:20 myfile.txt -> mySoftLink
lrwxrwxrwx 1 moose moose 10 2013-01-20 21:18 mySoftLink -> myfile.txt
{% endhighlight %}

Those two softlinks refer to each other. Now try to open this folder with Nautilus:
{% highlight bash %}nautilus /home/moose/Desktop/testFolder/{% endhighlight %}

Nautilus opens and instantly closes again.

<h2>My Nautilus</h2>
I use Ubuntu 10.04.4 LTS with Nautilus 2.30.1. 

<h2>Bug report?</h2>
I know, the current version of <a href="http://en.wikipedia.org/wiki/Nautilus_(file_manager)">Nautilus</a> is 3.6.1, but how often do you find a bug which is so easy to reproduce?

The Nautilus Bugtracker is <a href="https://bugzilla.gnome.org/browse.cgi?product=nautilus">here</a>, but where would you look for the bug?
