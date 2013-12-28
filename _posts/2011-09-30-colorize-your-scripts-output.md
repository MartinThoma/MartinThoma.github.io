---
layout: post
title: Colorize your scripts output
author: Martin Thoma
date: 2011-09-30 08:59:59.000000000 +02:00
categories:
- Code
tags:
- Command Line
- Bash
- Scripting
- C
featured_image: 2011/09/Gnome-Terminal.png
---
The bash is very nice if you want to know exactly what your scripts are doing. Unfortunately, its almost always white colored text on a black background, without any accentuation. No bold text, nothing underlined and no colors are used.

You can change this standard behaviour. You can add color to your output.

This is the way you do it:

The mini-program tput can initialize a terminal or query terminfo database. If you want to know more about it, you can take a look at the <a href="http://linux.die.net/man/1/tput">tput manpage</a>.

<h2>A quick example</h2>
{% highlight bash %}# Text color variables
txtred=$(tput setaf 1)    # Red
txtreset=$(tput sgr0)     # Reset your text
echo "Roses are ${txtred}red${txtreset}."{% endhighlight %}

Simply copy this example line by line and then you'll see the expected example.

A shorter way would be
{% highlight bash %}echo "Roses are `tput setaf 1`red`tput sgr0`."{% endhighlight %}

<h2>The sgr attribuge</h2>
{% highlight bash %}tput sgr 0 1     turn off standout; turn on underline
tput sgr 0 0     turn off standout; turn off underline
tput sgr 1 1     turn on standout; turn on underline
tput sgr 1 0     turn on standout; turn off underline
tput sgr0        short for sgr 0 0{% endhighlight %}

<h2>The setaf attribute</h2>
{% highlight bash %}setaf 1 Red
setaf 2 Green
setaf 3 Yellow
setaf 4 Blue
setaf 5 Purple
setaf 6 Cyan
setaf 7 Gray{% endhighlight %}

<h2>Misc</h2>
Make your text bold:
{% highlight bash %}tput bold{% endhighlight %}

Reset your style:
{% highlight bash %}tput sgr0{% endhighlight %}

<h2>Advanced Example</h2>
Imagine you had a script which generated much output. All messages are important for you, but some are more important than others. You definitely want to see all "[ERROR]" output. So you want to apply a red and bold modification to the stream.

This is the way how "[ERROR]" gets red and bold:
{% highlight bash %}`tput setaf 1``tput bold`[ERROR]`tput sgr0`{% endhighlight %}
You can test it with
{% highlight bash %}echo "`tput setaf 1``tput bold`[ERROR]`tput sgr0`"{% endhighlight %}

I've created a little python script called output.py for testing purposes. It simply outputs a quite long <a href="http://en.wikipedia.org/wiki/Lorem_ipsum">Lorem ipsum</a> text with some random [ERROR] messages.

The next task is to replace the [ERROR] messages. The tool of my choice is sed. See the <a href="http://linux.die.net/man/1/sed">sed man page</a> for more information. The basic usage is 
{% highlight bash %}sed 's/search/replace/'{% endhighlight %}

So we pipe the output to sed:
{% highlight bash %}python output.py | sed 's/\[ERROR\]/MYLOOOOOOOOOOOOOOOOOONGTEST/'{% endhighlight %}

And now we bring it all together:
{% highlight bash %}python output.py | sed 's/[ERROR]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/'{% endhighlight %}

Doesn't work? Well, lets analyse it. Instead of replacing `tput setaf 1` it gets printed directly. This means, something we did prevented the bash of replacing our command. If you look carefully at the command, you might see that I used ' instead of ". If you change this, everything is fine:

{% highlight bash %}python output.py | sed "s/\[ERROR\]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/"{% endhighlight %}

<h2>Colorize C / C++ output</h2>
You need <a href="http://en.wikipedia.org/wiki/ANSI_escape_code">ANSI color codes</a>:
{% highlight c %}#include <stdio.h>

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
}{% endhighlight %}

\033 is the ASCII 27 ESC character. It has to be followed by "[". After that you can write one or two numbers separated by ";". Then you have to write "m". You can get back to standard output with "\033[0m".
The numbers 30&ndash;37 change the color, 4 is a single underline.

I guess these will also work for Java, but I didn't test it.

Do you know what setaf or sgr stand for? Do you know further "terminal enhancement" tricks? Just leave a post!
