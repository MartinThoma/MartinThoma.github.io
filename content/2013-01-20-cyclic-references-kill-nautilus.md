---
layout: post
lang: en
title: Cyclic references kill Nautilus
slug: cyclic-references-kill-nautilus
author: Martin Thoma
date: 2013-01-20 21:46:34.000000000 +01:00
category: Code
tags: OS, Operating Systems, GNOME, file manager, Bug
featured_image: 2013/01/Nautilus.png
---
I just wanted to answer an assignment and noticed that cyclic references kill Nautilus.

<h2>What I did</h2>
```bash
mkdir testFolder
cd testFolder
touch testFile.txt
ln -s testFile.txt mySoftlink
rm testFile.txt
ln -s mySoftlink testFile.txt
ls -l
total 0
lrwxrwxrwx 1 moose moose 10 2013-01-20 21:20 myfile.txt -> mySoftLink
lrwxrwxrwx 1 moose moose 10 2013-01-20 21:18 mySoftLink -> myfile.txt

```

Those two softlinks refer to each other. Now try to open this folder with Nautilus:
```bash
nautilus /home/moose/Desktop/testFolder/
```

Nautilus opens and instantly closes again.

<h2>My Nautilus</h2>
I use Ubuntu 10.04.4 LTS with Nautilus 2.30.1.

<h2>Bug report?</h2>
I know, the current version of <a href="http://en.wikipedia.org/wiki/Nautilus_(file_manager)">Nautilus</a> is 3.6.1, but how often do you find a bug which is so easy to reproduce?

The Nautilus Bugtracker is <a href="https://bugzilla.gnome.org/browse.cgi?product=nautilus">here</a>, but where would you look for the bug?
