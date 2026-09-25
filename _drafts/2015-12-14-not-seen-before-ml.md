---
layout: post
title: Things I haven't seen before ML
slug: things-i-havent-seen-before-ml
lang: en
author: Martin Thoma
date: 2014-11-22 17:19
category: Cyberculture
tags: Machine Learning
featured_image: logos/star.png
status: draft
---


## ZSH: arg list too long

<figure>
    <a href="../images/2015/12/ml-not-seen-before-zsh-arg-list-too-long.png"><img src="../images/2015/12/ml-not-seen-before-zsh-arg-list-too-long.png" alt="ZSH complaining that the argument list is too long" width="500" height="19"></a>
    <figcaption>ZSH complaining that the argument list is too long</figcaption>
</figure>


## File busy

<figure>
    <a href="../images/2015/12/ml-not-seen-before-file-busy.png"><img src="../images/2015/12/ml-not-seen-before-file-busy.png" alt="A small text files of about 200 lines with no more than 80 characters per line taking so much time that I'm faster starting it than it is with writing (heavy IO in the background)" width="500" height="25" loading="lazy"></a>
    <figcaption>A small text files of about 200 lines with no more than 80 characters per line taking so much time that I'm faster starting it than it is with writing (heavy IO in the background)</figcaption>
</figure>


## Crashes / Slow response times

My system responded always, no matter what I did. Now I had multiple crashes /
waiting times:

* Opening images of 24&nbsp;MB (some with about 50&nbsp;MB) &rightarrow; Eye of
  Mate crashes
* Opening a folder with about 60&thinsp;000 files &rightarrow; Caja gets
  *really* slow
* Opening a file with a single line which is very long &rightarrow; Sublime
  Text gets really slow

<figure>
    <a href="../images/2015/12/ml-not-seen-before-renaming-time.png"><img src="../images/2015/12/ml-not-seen-before-renaming-time.png" alt="Renaming becomes really slow" width="537" height="184" loading="lazy"></a>
    <figcaption>Renaming becomes really slow</figcaption>
</figure>


## Swapping

When your system starts to swap, it becomes unusably slow. You should stop
(kill) whatever you were doing and empty the swap:

```bash
# swapoff -a
# swapon -a
```

This takes several minutes.


## Long saving times

<figure>
    <a href="../images/2015/12/ml-not-seen-before-saving.png"><img src="../images/2015/12/ml-not-seen-before-saving.png" alt="Saving your data suddenly takes a long time" width="528" height="137" loading="lazy"></a>
    <figcaption>Saving your data suddenly takes a long time</figcaption>
</figure>
