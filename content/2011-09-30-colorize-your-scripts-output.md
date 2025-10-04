---
layout: post
title: Colorize Your Script Output
slug: colorize-your-scripts-output
lang: en
author: Martin Thoma
date: 2011-09-30 08:59:59.000000000 +02:00
category: Code
tags: Command Line, Bash, Scripting, C
featured_image: 2011/09/Gnome-Terminal.png
---
Bash is very useful when you want to know exactly what your scripts are doing.
Unfortunately, it's almost always white text on a black background, without any
emphasis. No bold text, nothing underlined, and no colors are used.

You can change this standard behavior by adding color to your output.

Here's how you do it:

The `tput` utility can initialize a terminal or query the terminfo database. If
you want to know more about it, you can check the [tput manual page](http://linux.die.net/man/1/tput).

## A Quick Example
```bash
# Text color variables
txtred=$(tput setaf 1)    # Red
txtreset=$(tput sgr0)     # Reset your text
echo "Roses are ${txtred}red${txtreset}."
```

Simply copy this example line by line and you'll see the expected result.

A shorter way would be:

```bash
echo "Roses are `tput setaf 1`red`tput sgr0`."
```

## The sgr Attribute

```bash
tput sgr 0 1     # turn off standout; turn on underline
tput sgr 0 0     # turn off standout; turn off underline
tput sgr 1 1     # turn on standout; turn on underline
tput sgr 1 0     # turn on standout; turn off underline
tput sgr0        # short for sgr 0 0
```

## The setaf Attribute

```bash
setaf 1   # Red
setaf 2   # Green
setaf 3   # Yellow
setaf 4   # Blue
setaf 5   # Purple
setaf 6   # Cyan
setaf 7   # Gray
```

## Miscellaneous Commands

Make your text bold:
```bash
tput bold
```

Reset your style:
```bash
tput sgr0
```

## Advanced Example

Imagine you have a script that generates a lot of output. All messages are important, but some are more important than others. You definitely want to see all "[ERROR]" output, so you want to apply red and bold formatting to make it stand out.

Here's how to make "[ERROR]" red and bold:
```bash
`tput setaf 1``tput bold`[ERROR]`tput sgr0`
```

You can test it with:
```bash
echo "`tput setaf 1``tput bold`[ERROR]`tput sgr0`"
```

I've created a little Python script called `output.py` for testing purposes. It simply outputs a long [Lorem ipsum](http://en.wikipedia.org/wiki/Lorem_ipsum) text with some random [ERROR] messages.

The next task is to replace the [ERROR] messages. The tool of choice is `sed`. See the [sed manual page](http://linux.die.net/man/1/sed) for more information. The basic usage is:

```bash
sed 's/search/replace/'
```

So we pipe the output to sed:
```bash
python output.py | sed 's/$$ERROR$$/MYLOOOOOOOOOOOOOOOOOONGTEST/'
```

Now let's put it all together:
```bash
python output.py | sed 's/[ERROR]/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/'
```

Doesn't work? Let's analyze it. Instead of executing `tput setaf 1`, it gets
printed directly. This means something we did prevented bash from executing our
command. If you look carefully at the command, you might notice that I used
single quotes (`'`) instead of double quotes (`"`). If you change this,
everything works fine:

```bash
python output.py | sed "s/$$ERROR$$/`tput setaf 1``tput bold`[ERROR]`tput sgr0`/"
```

## Colorize C/C++ Output

You need [ANSI color codes](http://en.wikipedia.org/wiki/ANSI_escape_code):

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

`\033` is the ASCII 27 ESC character. It must be followed by `[`. After that,
you can write one or two numbers separated by `;`. Then you must write `m`. You
can return to standard output with `\033[0m`.

The numbers 30–37 change the color, and 4 provides a single underline.

I believe these will also work for Java, but I haven't tested it.
