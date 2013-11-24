---
layout: post
status: publish
published: true
title: Wandering through the depths of find
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 2621
wordpress_url: http://martin-thoma.com/?p=2621
date: 2011-12-28 16:01:18.000000000 +01:00
categories:
- Code
tags:
- Linux
- Command Line
- Bash
comments: []
---
find is a very mighty tool. It allows you to apply a very detailed search syntax. Every Linux user should know how to use it.

<h2>Very basic usage</h2>
<a href="http://martin-thoma.com/wp-content/uploads/2011/09/find-basic1.png"><img src="http://martin-thoma.com/wp-content/uploads/2011/09/find-basic1.png" alt="$ find  /home -iname &#039;Tux*&#039;" title="$ find  /home -iname &#039;Tux*&#039;" width="500" height="100" class="alignnone size-full wp-image-2671" /></a>

I told you I would start with the very basics, didn't I? So, you can need the option -iname if you want to do basic matching against the filename. The * can be used as a placeholder.

<h2>Redirecting errors</h2>
You might get some "Permission denied" errors. They are very bothersome if you combine commands in the bash. So you redirect them to /dev/null, a special file which discards everything it gets:

<a href="http://martin-thoma.com/wp-content/uploads/2011/09/find-error-redirection.png"><img src="http://martin-thoma.com/wp-content/uploads/2011/09/find-error-redirection.png" alt="find /home -iname &#039;Tux*&#039; 2>/dev/null" title="find /home -iname &#039;Tux*&#039; 2>/dev/null" width="500" height="100" class="alignnone size-full wp-image-2691" /></a>

<h2>Real life example</h2>
I am also a developer who likes to have good names for constants, database tables and variables. Sometimes, like today, I think it's time to change a database table a bit. It got a lot more rows and the old name doesn't really fit any longer. I used a constant for the table name in all scripts. This constant was SOFTWARE_USER_TABLE and should now be USER_INFO_TABLE. So I have to search recursively and case-sensitive in my project and replace all occurences in all strings by the new string. Except for .svn-directories, of course.
The easiest way to achieve this is via find, xargs and sed:
{% highlight bash %}find . -path '*/.svn' -prune -o -type f -print0 | xargs -0 sed -i 's/SOFTWARE_USER_TABLE/USER_INFO_TABLE/g'{% endhighlight %}

Now the explanation of the different commands:
<strong>find:</strong>
<ul>
    <li>.: search in the current working directory</li>
    <li>-path '*/.svn' -prune': If a directory starting with .svn is in the path to the file, skip it</li>
    <li>-o: atlernative (OR)</li>
    <li>-type f: only search for files</li>
    <li>-print0: print  the  full  file name on the standard output, followed by a null character (instead of the newline character that -print uses).  This allows file names that contain newlines or other types of white space  to  be  correctly  interpreted by programs that process the find output.  This option corresponds to the -0 option of xargs.</li>
</ul>
<strong>xargs</strong> -0: exchanges the arguments. -0 means that input items are terminated by a null character instead of by whitespace, and the quotes and backslash are not special (every character is taken lit erally).  Disables the end of file string, which is treated like any other argument.  Useful when input  items  might  contain  white  space,  quote marks, or backslashes.  The GNU find -print0 option produces input suitable for this mode.
<strong>sed:</strong>
<ul>
    <li>-i: edit the given file in-place. If you would not use -i, it would just print everything in standard output</li>
    <li>/g: edit the file globaly. If you would not use g, sed would only replace the first occurence of SOFTWARE_USER_TABLE</li>
</ul>

<h2>Snippets</h2>
move all files in subdirectories to a single directory:
{% highlight bash %}find -type f -exec mv {} collection/ \;{% endhighlight %}

find all files which are bigger than 20MB and print their location and size. Maybe you could use du for this one, but I don't know how:
{% highlight bash %}find / -type f -size +20000k -exec ls -lh {} \; 2>/dev/null | awk '{ print $5 ":\t" $8 }'{% endhighlight %}

find files in the home folder owned by alice:
{% highlight bash %}find /home -user alice{% endhighlight %}

<h2>Further reading</h2>
Note that you should use grep if you want to search for patterns in single files.

<ul>
  <li><a href="http://linux.die.net/man/1/find">man page</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Find">Wikipedia</a></li>
</ul>
