---
layout: post
title: Converting Files with Linux
author: Martin Thoma
date: 2011-09-21 22:10:08.000000000 +02:00
categories:
- Code
tags:
- cheat sheet
- conversion
- Linux
- Ubuntu
- Command Line
- PDF
featured_image: 2011/09/Gnome-Terminal.png
---
The following tipps work under a Linux terminal and were tested with Ubuntu 10.04 LTS.

I guess they will also work with other systems, as the programs are available for them.

If you know some further file conversions, please let me know.

I am also very interested in Web based conversions.


## PDF

Convert a folder of PDF slides into text files of the same name. This is nice
for using `grep`:

```bash
$ for file in *.pdf;do pdftotext "$file"; done
```


## Image Files

If you want to change image files via terminal, <a href="http://en.wikipedia.org/wiki/ImageMagick" rel="nofollow">ImageMagick</a> is a good choice.

**Resize Images to a maximum resolution**

```bash
convert "OldPicture.jpg" -resize 1600x1600 "NewPicture.jpg"
```

You can also do this for a whole folder. Just go into that folder and:

```bash
for i in *.jpg; do convert $i -resize 1600x1600 $i; done
```

In case you have just taken many photos of a document and you want to send it
as a single PDF via email. Thats the way to go:

```bash
for i in *.JPG; do convert $i -resize 1200x1200 $i; done; convert *.JPG merged.pdf
```

**Create a Black-and-white picture and compress it**
{% highlight bash %}djpeg "OldPicture.jpg" | ppmtopgm | cjpeg -qual 70 >"NewPicture.jpg"{% endhighlight %}

<b>Rename Pictures</b>:
{% highlight bash %}rename -n &rsquo;s/\.jpg$/\.JPG/&rsquo; *.jpg{% endhighlight %}


## Audio Files
<b>Give all mp3 songs the same sound level</b> (it's called <a href="http://en.wikipedia.org/wiki/Audio_normalization" rel="nofollow">Audio normalization</a>):
{% highlight bash %}mp3gain -a *.mp3{% endhighlight %}

<b>Merge many audio files to one</b>:
{% highlight bash %}mp3wrap merged.mp3 one.mp3 two.mp3{% endhighlight %}

<b>Convert all *.wav-files in one folder two *.mp3-files and remove the *.wav-files</b>:
{% highlight bash %}for i in *.wav;do lame "$i" "${i%wav}mp3"; rm "$i"; done{% endhighlight %}


## Video Files

For quite a lot purposes is the command line tool <a href="http://en.wikipedia.org/wiki/FFmpeg" rel="nofollow">FFmpeg</a> with its <a href="http://www.ffmpeg.org/ffmpeg-doc.html">lots of options</a> a good choice. For others might <a href="http://en.wikipedia.org/wiki/MEncoder" rel="nofollow">MEncoder</a> be better.
You might also want to install some codecs first:
{% highlight bash %}sudo apt-get install libavcodec-extra-52 libavdevice-extra-52 libavformat-extra-52 libavutil-extra-50 libpostproc-extra-51 libswscale-extra-0 libavcodec-unstripped-52 ubuntu-restricted-extras{% endhighlight %}

<b>Merge many video files to one</b>:
{% highlight bash %}cat One.mpg Two.mpg Three.mpg | ffmpeg -f mpeg -i - -vcodec copy -acodec copy "Merged.mpg"{% endhighlight %}

<b>avi2mpg</b>:
{% highlight bash %}ffmpeg -i "Original.avi" "New.mpg"{% endhighlight %}

<b>mp42mpg</b>:
{% highlight bash %}ffmpeg -i "Original.mp4" -target ntsc-vcd "New.mpg"{% endhighlight %}

<b>mod2avi</b>:
?

<b>vcd2avi</b>:
{% highlight bash %}mencoder vcd://2 -o "New.avi" -oac copy -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=2000{% endhighlight %}

<b>ogv2avi</b>:
{% highlight bash %}mencoder "Original.ogv" -ovc xvid -oac mp3lame -xvidencopts pass=1 -o "New.avi"{% endhighlight %}

<b>wmv2mpg</b>:
aspect=16/9 should eventually be changed to 4/3 or other aspects
{% highlight bash %}mencoder -of avi -ofps 25 \
  -oac mp3lame -lameopts cbr:br=112:aq=3:mode=0:vol=0 \
  -vf hqdn3d,softskip,harddup \
  -ovc xvid \
  -xvidencopts bitrate=501:max_key_interval=37:aspect=16/9:turbo:nochroma_me:notrellis:max_bframes=0:vhq=0 \
  Original.wmv \
  -o New.avi
{% endhighlight %}

<b>mkv2avi</b>:
{% highlight bash %}mencoder "Original.mkv" -ovc lavc -lavcopts vcodec=mpeg4:vhq:vbitrate=6000 -oac mp3lame -lameopts vbr=3 -o "New.avi"{% endhighlight %}

<h3>Converting Flash Videos flv to mpg</h3>
You might want to get the information of the video first:
{% highlight bash %}ffmpeg -i inputVideo.flv{% endhighlight %}

This is how you convert it:
{% highlight bash %}ffmpeg -i inputVideo.flv -acodec libmp3lame -ab 64k -s 320x240 -r 24 outputVideo.mpg{% endhighlight %}
<strong>-i</strong> input file
<strong>-acodec</strong> audio codec
<strong>-ab</strong> audio bitrate
<strong>-s</strong> size
<strong>-r</strong> fps where fps is the frame rate in Hz. The default value is 25Hz.


## Converting Flash Videos flv to avi
{% highlight bash %}ffmpeg -i inputVideo.flv -sameq -ab 128k outputVideo.avi{% endhighlight %}


## Shortcuts for Linux Console
I convert svg2png or pdf2png quite often for my articles. So I've created a command.

You can create a command in Linux very easy:
<ol>
  <li>Enter <code>echo $PATH</code> in your console</li>
  <li>Go to <code>/usr/bin</code> or any other path in your PATH</li>
  <li>Create a file with the name of your command (e.g. svg2png)</li>
  <li>Fill the fill (see below for some examples).</li>
  <li>Make it executable: <code>chmod +x svg2png</code></li>
</ol>

My <code>svg2png</code> looks like this:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description="convert a svg file to png")
parser.add_argument("-i", "--input", dest="input",
                  help="read svg file", metavar="FILE")
parser.add_argument("-o", "--output", dest="output",
                  help="output png file", metavar="FILE")
parser.add_argument("-w", "--width", dest="width", default=512, type=int,
                  help="width of output png")

args = parser.parse_args()

import os
command = "inkscape " + args.input + \
          " -w " + str(args.width) + " --export-png=" + args.output
os.system(command)
print("Executed command: " + command)
```

My pdf2png looks like this:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description="convert a svg file to png")
parser.add_argument("-i", "--input", dest="input",
                  help="read svg file", metavar="FILE")
parser.add_argument("-o", "--output", dest="output",
                  help="output png file", metavar="FILE")
parser.add_argument("-w", "--width", dest="width", default=512, type=int,
                  help="width of output png")

args = parser.parse_args()

import os
commands=[]
commands.append("pdf2svg "+args.input+" ~"+args.input+".svg")
commands.append("inkscape ~"+args.input+".svg --export-plain-svg=~"+args.input+".svg")
commands.append("svg2png -i ~"+args.input+".svg -o "+args.output+" -w " + str(args.width))
commands.append("rm ~"+args.input+".svg")
for command in commands:
	os.system(command)
	print("Executed command: " + command)

args = parser.parse_args()
```
