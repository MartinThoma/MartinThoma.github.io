---
layout: post
status: publish
published: true
title: Colorize your scripts output
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 3021
wordpress_url: http://martin-thoma.com/?p=3021
date: 2011-09-30 08:59:59.000000000 +02:00
categories:
- Code
tags:
- Command Line
- Bash
- Scripting
- C
comments:
- id: 1431
  author: Peter
  author_email: steffek@k-tc.de
  author_url: ''
  date: !binary |-
    MjAxMS0xMC0wMSAwNzowODowMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMS0xMC0wMSAwNTowODowMiArMDIwMA==
  content: ! "Hello Thomas,\r\ngood job we will youse this for our log output in our
    company. \r\nPeter"
- id: 21731
  author: snip
  author_email: webmaster@leprimepagine.com
  author_url: http://brainstretching.blogspot.com/
  date: !binary |-
    MjAxMS0xMi0yMCAxODoyMzo1NyArMDEwMA==
  date_gmt: !binary |-
    MjAxMS0xMi0yMCAxNjoyMzo1NyArMDEwMA==
  content: Interesting, really.
---
The bash is very nice if you want to know exactly what your scripts are doing. Unfortunately, its almost always white colored text on a black background, without any accentuation. No bold text, nothing underlined and no colors are used.

You can change this standard behaviour. You can add color to your output.

This is the way you do it:

The mini-program tput can initialize a terminal or query terminfo database. If you want to know more about it, you can take a look at the <a href="http://linux.die.net/man/1/tput">tput manpage</a>.

<h2>A quick example</h2>
[bash]# Text color variables
txtred=$(tput setaf 1)    # Red
txtreset=$(tput sgr0)     # Reset your text
echo "Roses are ${txtred}red${txtreset}."[/bash]

Simply copy this example line by line and then you'll see the expected example.

A shorter way would be
[bash]echo "Roses are `tput setaf 1`red`tput sgr0`."[/bash]

<h2>The sgr attribuge</h2>
[bash]tput sgr 0 1     turn off standout; turn on underline
tput sgr 0 0     turn off standout; turn off underline
tput sgr 1 1     turn on standout; turn on underline
tput sgr 1 0     turn on standout; turn off underline
tput sgr0        short for sgr 0 0[/bash]

<h2>The setaf attribute</h2>
[bash]setaf 1 Red
setaf 2 Green
setaf 3 Yellow
setaf 4 Blue
setaf 5 Purple
setaf 6 Cyan
setaf 7 Gray[/bash]

<h2>Misc</h2>
Make your text bold:
[bash]tput bold[/bash]

Reset your style:
[bash]tput sgr0[/bash]

<h2>Advanced Example</h2>
Imagine you had a script which generated much output. All messages are important for you, but some are more important than others. You definitely want to see all "[ERROR]" output. So you want to apply a red and bold modification to the stream.

This is the way how "[ERROR]" gets red and bold:
[bash]`tput setaf 1``tput bold`[ERROR]`tput sgr0`[/bash]
You can test it with
[bash]echo "`tput setaf 1``tput bold`[ERROR]`tput sgr0`"[/bash]

I've created a little python script called output.py for testing purposes. It simply outputs a quite long <a href="http://en.wikipedia.org/wiki/Lorem_ipsum">Lorem ipsum</a> text with some random [ERROR] messages.

The next task is to replace the [ERROR] messages. The tool of my choice is sed. See the <a href="http://linux.die.net/man/1/sed">sed man page</a> for more information. The basic usage is 
[bash]sed 's/search/replace/'[/bash]

So we pipe the output to sed:
[bash]python output.py | sed 's/\[ERROR\]/MYLOOOOOOOOOOOOOOOOOONGTEST/'[/bash]

And now we bring it all together:
[bash]python output.py | sed 's/[ERROR]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/'[/bash]

Doesn't work? Well, lets analyse it. Instead of replacing `tput setaf 1` it gets printed directly. This means, something we did prevented the bash of replacing our command. If you look carefully at the command, you might see that I used ' instead of ". If you change this, everything is fine:

[bash]python output.py | sed "s/\[ERROR\]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/"[/bash]

<h2>Colorize C / C++ output</h2>
You need <a href="http://en.wikipedia.org/wiki/ANSI_escape_code">ANSI color codes</a>:
[c]#include <stdio.h>

int main()
{
    printf("&#92;&#48;33[30m%s&#92;&#48;33[0m\n", "black?");
    printf("&#92;&#48;33[31m%s&#92;&#48;33[0m\n", "red");
    printf("&#92;&#48;33[32m%s&#92;&#48;33[0m\n", "lime");
    printf("&#92;&#48;33[33m%s&#92;&#48;33[0m\n", "yellow");
    printf("&#92;&#48;33[34m%s&#92;&#48;33[0m\n", "blue");
    printf("&#92;&#48;33[35m%s&#92;&#48;33[0m\n", "gray");
    printf("&#92;&#48;33[36m%s&#92;&#48;33[0m\n", "blue");
    printf("&#92;&#48;33[37m%s&#92;&#48;33[0m\n", "light gray");
    printf("&#92;&#48;33[38m%s&#92;&#48;33[0m\n", "black?");
    printf("&#92;&#48;33[39m%s&#92;&#48;33[0m\n", "black?");
    printf("&#92;&#48;33[41m%s&#92;&#48;33[0m\n", "red background");
    printf("&#92;&#48;33[1;34m%s&#92;&#48;33[0m\n", "bold and blue");
    printf("&#92;&#48;33[4m%s&#92;&#48;33[0m\n", "underlined");
    printf("&#92;&#48;33[9m%s&#92;&#48;33[0m\n", "strike");
    return 0;
}[/c]

\033 is the ASCII 27 ESC character. It has to be followed by "[". After that you can write one or two numbers separated by ";". Then you have to write "m". You can get back to standard output with "\033[0m".
The numbers 30&ndash;37 change the color, 4 is a single underline.

I guess these will also work for Java, but I didn't test it.

Do you know what setaf or sgr stand for? Do you know further "terminal enhancement" tricks? Just leave a post!
