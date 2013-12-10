---
layout: post
status: publish
published: true
title: How to use magic rescue
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 9981
wordpress_url: http://martin-thoma.com/?p=9981
date: 2011-12-17 13:02:47.000000000 +01:00
categories:
- Code
tags:
- Data Recovery
comments: []
featured_image: 2011/12/PartitionManager.png
---
I've just searched an image I have created some time ago. I knew that I've put it on one of my USB-Sticks, but it seems as if I had deleted it. So how could I get the image back? Magic rescue is a program for recovering deleted files. It doesn't simply open your trash can, but it searches files which were deleted, but not overwritten.

<h2>Installation</h2>
{% highlight bash %}sudo apt-get install magicrescue{% endhighlight %}

<h2>Basic usage</h2>
{% highlight bash %}$ magicrescue
Usage: magicrescue [-I FILE] [-M MODE] [-O [+-=][0x]OFFSET] [-b BLOCKSIZE]
	-d OUTPUT_DIR -r RECIPE1 [-r RECIPE2 [...]] DEVICE1 [DEVICE2 [...]]

  -b  Only consider files starting at a multiple of BLOCKSIZE.
  -d  Mandatory.  Output directory for found files.
  -r  Mandatory.  Recipe name, file or directory.
  -I  Read input file names from this file ("-" for stdin)
  -M  Produce machine-readable output to stdout.
  -O  Resume from specified offset (hex or decimal) in the first device.{% endhighlight %}

You need recipes to use Magic Rescue. These are the basic ones:
{% highlight bash %}moose@pc07:/usr/share/magicrescue/recipes$ ls
avi        flac      gzip       mp3-id3v1  nikon-raw  ppm
canon-cr2  gimp-xcf  jpeg-exif  mp3-id3v2  perl       zip
elf        gpl       jpeg-jfif  msoffice   png{% endhighlight %}

<h2>Where is my USB-Stick?</h2>
{% highlight bash %}$ sudo fdisk -l
[sudo] password for moose: 

Disk /dev/sda: 320.1 GB, 320072933376 bytes
255 heads, 63 sectors/track, 38913 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00065e10

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *           1       37810   303704064   83  Linux
/dev/sda2           37810       38914     8864769    5  Extended
/dev/sda5           37810       38914     8864768   82  Linux swap / Solaris

Disk /dev/sdc: 2067 MB, 2067267584 bytes
2 heads, 63 sectors/track, 32044 cylinders
Units = cylinders of 126 * 512 = 64512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x005f4d47

   Device Boot      Start         End      Blocks   Id  System
/dev/sdc1   *           1       32045     2018800    b  W95 FAT32{% endhighlight %}

<h2>Usage</h2>
{% highlight bash %}sudo magicrescue -r png -r jpeg-jfif -r gimp-xcf \
-r jpeg-exif -d /home/moose/output/ /dev/sdc1{% endhighlight %}

Just got the image back :-) 
