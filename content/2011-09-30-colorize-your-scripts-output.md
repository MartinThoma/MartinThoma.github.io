---
layout: post
lang: en
title: Colorize your scripts output
slug: colorize-your-scripts-output
author: Martin Thoma
date: 2011-09-30 08:59:59.000000000 +02:00
category: Code
tags: Command Line, Bash, Scripting, C
featured_image: 2011/09/Gnome-Terminal.png
---
The bash is very nice if you want to know exactly what your scripts are doing. Unfortunately, its almost always white colored text on a black background, without any accentuation. No bold text, nothing underlined and no colors are used.

You can change this standard behaviour. You can add color to your output.

This is the way you do it:

The mini-program tput can initialize a terminal or query terminfo database. If you want to know more about it, you can take a look at the <a href="http://linux.die.net/man/1/tput">tput manpage</a>.

<h2>A quick example</h2>
```bash
# Text color variables
txtred=$(tput setaf 1)    # Red
txtreset=$(tput sgr0)     # Reset your text
echo "Roses are ${txtred}red${txtreset}."
```

Simply copy this example line by line and then you'll see the expected example.

A shorter way would be
```bash
echo "Roses are `tput setaf 1`red`tput sgr0`."
```

<h2>The sgr attribuge</h2>
```bash
tput sgr 0 1     turn off standout; turn on underline
tput sgr 0 0     turn off standout; turn off underline
tput sgr 1 1     turn on standout; turn on underline
tput sgr 1 0     turn on standout; turn off underline
tput sgr0        short for sgr 0 0
```

<h2>The setaf attribute</h2>
```bash
setaf 1 Red
setaf 2 Green
setaf 3 Yellow
setaf 4 Blue
setaf 5 Purple
setaf 6 Cyan
setaf 7 Gray
```

<h2>Misc</h2>
Make your text bold:
```bash
tput bold
```

Reset your style:
```bash
tput sgr0
```

<h2>Advanced Example</h2>
Imagine you had a script which generated much output. All messages are important for you, but some are more important than others. You definitely want to see all "[ERROR]" output. So you want to apply a red and bold modification to the stream.

This is the way how "[ERROR]" gets red and bold:
```bash
`tput setaf 1``tput bold`[ERROR]`tput sgr0`
```
You can test it with
```bash
echo "`tput setaf 1``tput bold`[ERROR]`tput sgr0`"
```

I've created a little python script called output.py for testing purposes. It simply outputs a quite long <a href="http://en.wikipedia.org/wiki/Lorem_ipsum">Lorem ipsum</a> text with some random [ERROR] messages.

The next task is to replace the [ERROR] messages. The tool of my choice is sed. See the <a href="http://linux.die.net/man/1/sed">sed man page</a> for more information. The basic usage is
```bash
sed 's/search/replace/'
```

So we pipe the output to sed:
```bash
python output.py | sed 's/$$ERROR$$/MYLOOOOOOOOOOOOOOOOOONGTEST/'
```

And now we bring it all together:
```bash
python output.py | sed 's/[ERROR]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/'
```

Doesn't work? Well, lets analyse it. Instead of replacing `tput setaf 1` it gets printed directly. This means, something we did prevented the bash of replacing our command. If you look carefully at the command, you might see that I used ' instead of ". If you change this, everything is fine:

```bash
python output.py | sed "s/$$ERROR$$/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/"
```

<h2>Colorize C / C++ output</h2>
You need <a href="http://en.wikipedia.org/wiki/ANSI_escape_code">ANSI color codes</a>:
```c
#include <stdio.h>

int main()
{
    printf("\\033[30m%s\\033[0m\n", "black?");
    printf("\\033[31m%s\\033[0m\n", "red");
    printf("\\033[32m%s\\033[0m\n", "lime");
    printf("\\033[33m%s\\033[0m\n", "yellow");
    printf("\\033[34m%s\\033[0m\n", "blue");
    printf("\\033[35m%s\\033[0m\n", "gray");
    printf("\\033[36m%s\\033[0m\n", "blue");
    printf("\\033[37m%s\\033[0m\n", "light gray");
    printf("\\033[38m%s\\033[0m\n", "black?");
    printf("\\033[39m%s\\033[0m\n", "black?");
    printf("\\033[41m%s\\033[0m\n", "red background");
    printf("\\033[1;34m%s\\033[0m\n", "bold and blue");
    printf("\\033[4m%s\\033[0m\n", "underlined");
    printf("\\033[9m%s\\033[0m\n", "strike");
    return 0;
}
```

\033 is the ASCII 27 ESC character. It has to be followed by "[". After that you can write one or two numbers separated by ";". Then you have to write "m". You can get back to standard output with "\033[0m".
The numbers 30&ndash;37 change the color, 4 is a single underline.

I guess these will also work for Java, but I didn't test it.

Do you know what setaf or sgr stand for? Do you know further "terminal enhancement" tricks? Just leave a post!
