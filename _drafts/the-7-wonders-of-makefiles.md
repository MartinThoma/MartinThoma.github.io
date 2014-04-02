---
layout: post
title: The 7 Wonders of Makefiles
author: Martin Thoma
date: 2012-05-07 06:56:24
categories: 
- Code
tags: 
- Makefile
- Programming
featured_image: 
---
Makefiles are great. They provide a very simple tool for executing some folder-specific tasks.

A Makefile usually looks like this:

```bash
CC=     gcc
LD=     ld
CFLAGS= -W -Wall -Werror -std=c99
TARGET= processes
SRC=    $(TARGET).c main.c
OBJ=    $(SRC:%.c=%.o)

$(TARGET): $(OBJ)
	$(CC) -o $@ $(OBJ)

.PHONY: $(TARGET)-solution.o
$(TARGET)-sol: $(subst $(TARGET),$(TARGET)-solution,$(OBJ))
	$(CC) -o $@ $^

$(TARGET)-solution.o:
	@test -f $(TARGET)-solution.c \
	|| { echo "Download solution tarball." >&amp;2; false; }
	$(CC) $(CFLAGS) -c $(TARGET)-solution.c

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -rf $(TARGET) $(TARGET)-sol *.o
```

Here is some useful information about these files.

## Remember the TAB
Makefiles use TABS in front of the commands, not spaces.

## Two Dollars are better than one
If you want to use Bash Variables, you have to use $$varname instead of $varname.

## Variables: Recursive expansion
You can create variables in Bash like this:

```bash
variable = value
```

And you access them like this:

```bash
echo $(variable)
```

But it gets really strange if you assign variable to other variables:

```bash
first  = $(second)
second = $(third)
third  = Huh?

all:;echo $(first)
```

This prints "Huh?".

More about variables <a href="http://www.gnu.org/software/make/manual/make.html#Flavors">here</a>.

## Useful Examples
```bash
make:
	# Check files
	checkstyle -c /home/moose/Downloads/Progr_WS11_Checkstyle1.xml -r .
	# Create zip for upload
	find . -name "*.java" -type f -print | zip ~/blatt3.zip -@
clean:
	rm -rf  *.class
	rm -rf  *.o
```

## Further reading
<ul>
	<li><a href="http://en.wikipedia.org/wiki/Make_(software)">Wikipedia</a></li>
    <li>Freies Magazin, Mai 2012: <a href="http://www.freiesmagazin.de/freiesMagazin-2012-05">Selbstgebacken 3: make</a></li>
</ul>