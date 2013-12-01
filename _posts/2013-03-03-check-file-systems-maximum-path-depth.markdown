---
layout: post
status: publish
published: true
title: Check File Systems maximum path depth
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 58821
wordpress_url: http://martin-thoma.com/?p=58821
date: 2013-03-03 20:51:24.000000000 +01:00
categories:
- Code
tags:
- C
- OS
- Nautilus
comments: []
featured_image: 2013/03/long-path-thumb.png
---
Today, I've wondered how deep a path could be at maximum. I've guessed the file system may be limiting that, but perhaps also some tools that I use for basic operations like listing a folders contents would fail before. So I've created the following C-Snippet to test it:

[c]#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int i = 0;
int returnCode;
char *pathname;

void giveInformation() {
    printf("return code\t\t: %i\n", returnCode);
    printf("Created sub-directories\t: %i\n", i);
    printf("length of pathname\t: %i\n", strlen(pathname));
    if (strlen(pathname) <= 80) {
        printf("Path\t\t\t: %s\n", pathname);
    }
}

int main () {
    pathname = "/home/moose/Desktop/Test";
    char *ext = "/one";
    returnCode = 0;
    int maxDir = 1000000;

    while(i < maxDir &amp;&amp; returnCode == 0) {
        char *newName = malloc(strlen(pathname)+strlen(ext)+1);
        strcpy(newName, pathname);
        strcat(newName, ext);
        returnCode = mkdir(newName, 0777);
        if (i != 0) {
            // if you remove this line, your system gets very slow:
            free(pathname);
        }
        pathname = newName;
        i++;
    }

    giveInformation();
    return 0;
}[/c]

Now run it:
{% highlight bash %}
$ time ./createDirectories 

return code		: -1
Created sub-directories	: 1018
length of pathname	: 4096

real	0m0.281s
user	0m0.004s
sys	0m0.180s
{% endhighlight %}

Ok, something went wrong at the end. Lets see what crashes when I enter this path in Gnome terminal

{% highlight bash %}
$ cd one/one/one .... one/
$ mkdir two
$ cd two
cd: error retrieving current directory: getcwd: cannot access 
    parent directories: File name too long
{% endhighlight %}

Strangely, it showed me a path <code>/home/moose/.../one/one/one/one/tw$</code>. No, this is not a typo. It showed tw, not two. So, maybe the path can get only that long?
Now I created a folder called "three" and one called "this". I entered both of them with cd, both showed <code>/home/moose/.../one/one/th</code>. So I guess this is a problem of Gnome Terminal and not a limitation of the file system.

Let's see what Nautilus does. I <a href="http://martin-thoma.com/cyclic-references-kill-nautilus/" title="Cyclic references kill Nautilus">once got Nautilus to crash</a>, I think I get it another time:

Contents, according to nautilus: <code>1,016 items, totalling 4.0 MB</code>

Then I've opened the folder "one" and double clicked as fast as I could. CPU utilization: 100%, but no crash. And 995 items are left :-) Now a single double click causes 100% CPU utilization for about 25 seconds.

When I use a single character for sub-directories, I get:
{% highlight bash %}
moose@pc07:~/Desktop/Test$ ./createDirectories 
return code		: -1
Created sub-directories	: 2036
length of pathname	: 4096
{% endhighlight %}

<h2>Number of directories in one directory</h2>
Do you know how many folders can fit into one folder? Well, lets find out:

[c]
#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int i = 0;
int returnCode;
char *pathname;

/** http://stackoverflow.com/a/440240/562769 */
void gen_random(char *s, const int len) {
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < len; ++i) {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
}

void giveInformation() {
    printf("return code\t\t: %i\n", returnCode);
    printf("Created sub-directories\t: %i\n", i);
    printf("length of pathname\t: %i\n", strlen(pathname));
    if (strlen(pathname) <= 80) {
        printf("Path\t\t\t: %s\n", pathname);
    }
}

int main () {
    pathname = "/home/moose/Desktop/Test/test/";
    returnCode = 0;
    int maxDir = 1000000;

    while(i < maxDir &amp;&amp; returnCode == 0) {
        // get unique name
        char *foldername = malloc(50+1);
        gen_random(foldername, 50);
        char *completePath = malloc(strlen(pathname)
                             +strlen(foldername)+1);
        strcpy(completePath, pathname);
        strcat(completePath, foldername);
        returnCode = mkdir(completePath, 0777);
        free(foldername);
        free(completePath);
        i++;
    }

    giveInformation();
    return 0;
}
[/c]

I've executed it and after eight minutes I canceled the execution.

{% highlight bash %}$ ls | wc -l
378463{% endhighlight %}

Ok, not a million folders, but 378.463 is also quite a lot. When I try to open this folder with Nautilus, I get 140% CPU utilization by Nautilus. Quite impressive, for only showing some folders.

You should probably not execute the script above, as <a href="http://unix.stackexchange.com/q/66806/4784">deleting the folder isn't that easy</a>.

By the way, I got a new error message that I didn't know before:

[caption id="attachment_58951" align="aligncenter" width="498"]<a href="http://martin-thoma.com/wp-content/uploads/2013/03/cannot-move-to-trash-filename.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/03/cannot-move-to-trash-filename.png" alt="Cannot move file to trash - Filename too long!" width="498" height="269" class="size-full wp-image-58951" /></a> Cannot move file to trash - Filename too long![/caption]
