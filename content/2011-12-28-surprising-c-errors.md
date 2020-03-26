---
layout: post
title: Surprising C errors
author: Martin Thoma
date: 2011-12-28 15:18:43.000000000 +01:00
category: Code
tags: Programming, learning, C
featured_image: 2011/12/compare-programming-languages.png
---
Those errors might be surprising and a good exercise for C beginners:

<h2>Empty printf</h2>

```c
#include <stdio.h>

int main()
{
    printf("");
    return 0;
}
```

```bash
error: zero-length gnu_printf format string
```

<h2>Macros</h2>

```c
#include <stdio.h>
#define MY_MACRO printf("Hello World\n");

int main()
{
    if (1)
        MY_MACRO;
    else
        printf("Crazy, huh?\n");

    return 0;
}
```

```bash
macro.c: In function &lsquo;main&rsquo;:
macro.c:8: error: &lsquo;else&rsquo; without a previous &lsquo;if&rsquo;
```

<h2>Single and Double quotes</h2>

```c
#include <stdio.h>

int main()
{
    printf('hello, world\n');
    return 0;
}
```

```bash
macro.c:5:9: warning: character constant too long for its type
macro.c: In function &lsquo;main&rsquo;:
macro.c:5: warning: passing argument 1 of &lsquo;printf&rsquo; makes pointer from integer without a cast
/usr/include/stdio.h:339: note: expected &lsquo;const char * __restrict__&rsquo; but argument is of type &lsquo;int&rsquo;
macro.c:5: warning: format not a string literal and no format arguments

```

Thanks to <a href="http://www.drpaulcarter.com/cs/common-c-errors.php#3.1">drpaulcarter.com</a> for this example:

```c
int main()
{
    const char * myPointer = 'A';
    (void) myPointer;
    return 0;
}
```

```bash
macro.c: In function &lsquo;main&rsquo;:
macro.c:3: warning: initialization makes pointer from integer without a cast

```

<h2>Pointers</h2>

```c
#include <string.h>

int main()
{
    char * myPointer;

    strcpy(myPointer, "Hello World!");
    return 0;
}
```

```bash
macro.c: In function &lsquo;main&rsquo;:
macro.c:7: warning: &lsquo;myPointer&rsquo; is used uninitialized in this function

```

<h2>Loops</h2>

```c
int main()
{
    int x = 42;
    while( x > 0 );
        x--;
    return 0;
}
```

No compiler error, but an infinite loop.

<h2>Null terminator of Strings</h2>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char myArray[20];
    printf("Characters: %i\n", strlen(myArray));
    strcpy(myArray, "abc");
    printf("Characters: %i\n", strlen(myArray));
    strcpy(myArray, "Hello World!");
    printf("Characters: %i\n", strlen(myArray));
    printf("String: -%s-\n", myArray);
    printf("Size: %i Byte\n\n", sizeof(myArray));

    char * myString = malloc(strlen(myArray));
    strcpy(myString, myArray);
    printf("String: -%s-\n", myString);
    printf("Size: %i Byte\n", sizeof(myString));
    printf("Characters: %i\n\n", strlen(myString));

    char * breakIt = malloc(strlen(myString));
    strcpy(breakIt, myString);
    printf("String: -%s-\n", breakIt);
    printf("Size: %i Byte\n", sizeof(breakIt));
    printf("Characters: %i\n", strlen(breakIt));

    return 0;
}
```

Again, you don't get a compiler error, but some strange results:

```bash
Characters: 0
Characters: 3
Characters: 12
String: -Hello World!-
Size: 20 Byte

String: -Hello World!-
Size: 4 Byte
Characters: 12

String: -Hello World!-
Size: 4 Byte
Characters: 13
```

<h2>Further reading</h2>
<ul>
  <li><a href="http://en.wikipedia.org/wiki/C_preprocessor">C Preprocessor</a> and <a href="http://en.wikipedia.org/wiki/C_preprocessor#Macro_definition_and_expansion">macros</a></li>
  <li><a href="http://www.drpaulcarter.com/cs/common-c-errors.php#2.8">Pointer initialisation</a></li>
  <li><a href="http://linux.die.net/man/3/strcpy">strcpy</a>, <a href="http://linux.die.net/man/3/strlen">strlen</a></li>
</ul>
