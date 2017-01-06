---
layout: post
title: Get Information about Files
author: Martin Thoma
date: 2014-11-22 17:19
category: Cyberculture
tags:
- Linux
- Command Line
featured_image: logos/shell.png
---
This article shows you a few tricks how to get basic information about a file
without opening it and without programming. It is adressed at Linux people.


## file

The command `file` already gives you quite a bit:

```bash
$ file robot.png
robot.png: PNG image data, 128 x 128, 8-bit/color RGB, non-interlaced
```

You can see the dimensions of the image (`128 x 128`, it is `width x height`),
the type of the file and the color space.

Here you can see an example for an audio file:

```
$ file music.mp3
music.mp3: Audio file with ID3 version 2.4.0, extended header, contains: MPEG ADTS, layer III, v1, 128 kbps, 44.1 kHz, Stereo
```

and a video file

```
$ file Emily\ Howell\ fugue.mp4
Emily Howell fugue.mp4: ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]
```


## mp3info

**Duration**

```bash
$ mp3info -p "%m:%s\n" music.mp3
2:54
```


## ImageMagick

**Image size** ([source](http://stackoverflow.com/a/32824749/562769)):

```bash
identify -ping -format '%w %h\n' python.png
128 128
```
