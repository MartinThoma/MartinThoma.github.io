---
layout: post
title: Linux access rights and attributes
author: Martin Thoma
date: 2013-03-04 22:29:42.000000000 +01:00
category: Cyberculture
tags: Linux, IT-Security, gedit, Bug
---
<h2>RWX</h2>
<h3>Files</h3>
Linux files have three important access rights for files:
<ul>
  <li><strong>R</strong>ead</li>
  <li><strong>W</strong>rite</li>
  <li>E<strong>x</strong>ecute</li>
</ul>

If you want to mark a file as executable, you can add the x-right:

```bash
chmod +x
```


When you want to mark a file as readable, you can dd the r-right:

```bash
chmod +r
```


You can remove rights in a similar way:

```bash
chmod -x testfile
```


Now, often this is expressed numerically. Three bits determine if the file is readable (4), writable (2) or executable (1). Did you notice that all of them are powers of two?

<h3>Folders</h3>
rwx has a meaning for folders, too:
<ul>
  <li><strong>R</strong>ead: if that is missing, you can't use <code>ls</code> in the directory.</li>
  <li><strong>W</strong>rite: you need this to create new files / folders in the direcotry</li>
  <li><strong>x</strong> ... like "enter"?: if that is missing, you can't enter the directory.</li>
</ul>

<h2>User, Group, Others</h2>
The rights above can be set for the user who created the file (sometimes also called the owner). Then the group that owns the file and all others. This is the reason why you have three times the rights from above:

```bash
moose@pc07:~/Downloads$ ls -l
total 29624
drwxr-xr-x  8 moose moose     4096 2013-02-22 14:18 algorithms
-rw-r--r--  1 moose moose    60058 2013-02-11 08:00 args4j-2.0.21.jar
drwxr-xr-x  6 moose moose     4096 2013-02-25 20:07 bwinf
-rw-r--r--  1 moose moose 22160041 2013-02-05 16:45 DT2012.zip
drwxr-xr-x  8 moose moose     4096 2013-02-28 19:23 graphentheorie
-rw-r--r--  1 moose moose  2164878 2013-02-22 12:38 guava-14.0-rc1.jar
-rw-r--r--  1 moose moose  2705344 2013-03-01 21:07 HardVacuum.zip
drwxr-xr-x  8 moose moose     4096 2013-02-05 16:38 informatik-2011
-rw-r--r--  1 moose moose   111926 2013-02-24 19:09 Jim_Keener_resume.pdf
drwxr-xr-x  2 moose moose     4096 2011-11-08 11:50 juniper_linux
-rw-r--r--  1 moose moose   288666 2012-12-04 11:38 junit-4.11.jar
drwxr-xr-x 13 moose moose     4096 2013-02-01 23:33 LaTeX-examples
drwxr-xr-x  2 moose moose     4096 2009-08-11 17:04 otrdecoder
-rw-r--r--  1 moose moose   728292 2013-03-01 19:33 PlanetCute PNG.zip
drwxr-xr-x  2 moose moose     4096 2012-11-13 10:49 ProjectEuler
drwxr-xr-x  2 moose moose     4096 2013-03-04 20:28 Screenshots Matlab
-rw-r--r--  1 moose moose   764196 2013-03-04 20:28 Screenshots Matlab.zip
-rw-r--r--  1 moose moose   534614 2013-03-01 19:48 spritelib_gpl.zip
drwxr-xr-x  8 moose moose     4096 2013-02-27 18:36 Team
drwxr-xr-x  5 moose moose     4096 2013-02-27 19:17 ViMuDat
```

You might wonder what happens when you execute <code>chmod +x filename</code>. Does it set the execute-flag only for the user? Or for all three - user, group, others? Try and find out. You might want to remove all rights with <code>chmod 000 filename</code> before you start.

Did you know that you can search for file permissions with <code>find /home/ -perm 777</code>?

<h2>SUID, SGID, Sticky Bit</h2>
<h3>Files</h3>
Sometimes, you want to execute programs as root, although the user who started the execution isn't root. Take passwd, the program that allows users to change passwords, for example:

```bash
moose@pc07:/usr/bin$ ls -l | grep passwd$
-rwsr-xr-x 1 root   root       53812 2011-02-14 23:11 gpasswd
-rwxr-xr-x 1 root   root       13612 2012-11-06 21:41 htpasswd
-rwsr-xr-x 1 root   lpadmin    13540 2012-12-04 16:24 lppasswd
-rwsr-xr-x 1 root   root       37140 2011-02-14 23:11 passwd
-rwxr-xr-x 1 root   root     5070304 2012-04-24 23:38 smbpasswd
-rwxr-xr-x 1 root   root        9688 2013-01-18 17:59 vino-passwd
```

Instead of "x" in the user-execution-row, it states "s". That means, you can execute it and it has the SUID-bit set. If "x" wasn't set, the "S" would be in a capital letter. When you change your password, you need to edit <code>/etc/shadow</code>. This file has very limited access rights: <code>-rw-r-----</code> and is owned by "root" and group "shadow":

```bash
moose@pc07:/etc$ ls -l | grep shadow$
-rw-r-----  1 root    shadow     813 2013-01-24 06:21 gshadow
-rw-r-----  1 root    shadow    1274 2013-01-24 06:21 shadow
```

Here is <a href="http://www.cyberciti.biz/faq/understanding-etcshadow-file/">more about shadow file</a>.

The SGID (set group id) bit works similar to the SUID (set user id) bit. When you want to execute something with as the group of the file, you set the SGID bit.

The sticky bit seems to be used for programs to stick in memory after it was finished.

You can set the sticky bit like this:

```bash
chmod +t testfile
```

or like that:

```bash
chmod 1777 testfile
```


<h3>Folders</h3>
<ul>
  <li>suid: is ignored on UNIX and Linux systems</li>
  <li>sgid: new files and subdirectories created within this folder inherit the folders group ID</li>
  <li>t: when the sticky bit is set, only owners may change the filename or delete files</li>
</ul>


<h2>Type</h2>
The first column of <code>ls -l</code> tells you the type of the item:

<ul>
  <li>-: a file</li>
  <li>b: a block device</li>
  <li>c: a character device</li>
  <li>d: a directory</li>
  <li>l: a symbolic link</li>
  <li>p: pipe</li>
  <li>s: a socket</li>
</ul>

```bash
moose@pc07:/dev$ ls -l
total 0
crw-------  1 root video    10, 175 2013-03-04 10:01 agpgart
crw-rw----+ 1 root audio    14,   4 2013-03-04 10:01 audio
drwxr-xr-x  2 root root         640 2013-03-04 12:59 block
drwxr-xr-x  2 root root         100 2013-03-04 12:59 bsg
drwxr-xr-x  3 root root          60 2013-03-04 10:01 bus
lrwxrwxrwx  1 root root           3 2013-03-04 10:01 cdrom -> sr0
lrwxrwxrwx  1 root root           3 2013-03-04 10:01 cdrw -> sr0
crw-rw----+ 1 root audio    14,   3 2013-03-04 10:01 dsp
lrwxrwxrwx  1 root root           3 2013-03-04 10:01 dvd -> sr0
lrwxrwxrwx  1 root root           3 2013-03-04 10:01 dvdrw -> sr0
crw-rw----  1 root root     10,  61 2013-03-04 10:01 ecryptfs
crw-rw----  1 root video    29,   0 2013-03-04 10:01 fb0
lrwxrwxrwx  1 root root          13 2013-03-04 10:01 fd -> /proc/...
crw-rw-rw-  1 root root      1,   7 2013-03-04 10:01 full
crw-rw-rw-  1 root fuse     10, 229 2013-03-04 10:01 fuse
crw-rw----  1 root root    251,   0 2013-03-04 18:14 hidraw0
crw-rw----  1 root root     10, 228 2013-03-04 10:01 hpet
drwxr-xr-x  4 root root         380 2013-03-04 18:14 input
crw-rw----  1 root root      1,  11 2013-03-04 10:01 kmsg
srw-rw-rw-  1 root root           0 2013-03-04 10:01 log
brw-rw----  1 root disk      7,   0 2013-03-04 10:01 loop0
[...]
```



<h2>stat</h2>
You can display quite a lot of information of a file with stat:

```bash
moose@pc07:~/Desktop/Test$ stat testfile
  File: `testfile'
  Size: 13        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 923339      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: ( 1000/   moose)   Gid: ( 1000/moose)
Access: 2013-03-04 21:31:52.154187243 +0100
Modify: 2013-03-04 21:31:51.154184098 +0100
Change: 2013-03-04 21:31:51.154184098 +0100
```

The content of the file is "Hello World." (12 characters)

<h2>Attributes</h2>
According to the manpage of chattr:

<blockquote>The `c', 's',  and `u' attributes are not honored by the ext2 and ext3 filesystems as implemented in the current mainline Linux kernels. These attributes may be implemented in future versions of the ext2 and ext3 filesystems.</blockquote>

<h3>Version</h3>
I've just learned that you can give files version-attributes:

```bash
moose@pc07:~/Desktop/Test$ lsattr -v
 1338 -----------------e- ./testfile
```

You can set the version like this:

```bash
chattr -v 1339 testfile
```


<h3>Append only</h3>
This one is weird. Theoretically, it should allow me to append to a file, but not to change / delete anything in the file.

First of all, I had to use sudo to add this attribute:


```bash
sudo chattr +a testfile
```


Then, I had all permissions:

```bash
moose@pc07:~/Desktop/Test$ stat testfile
  File: `testfile'
  Size: 13        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 923339      Links: 1
Access: (0777/-rwxrwxrwx)  Uid: ( 1000/   moose)   Gid: ( 1000/moose)
Access: 2013-03-04 21:31:52.154187243 +0100
Modify: 2013-03-04 21:31:51.154184098 +0100
Change: 2013-03-04 21:33:55.154184312 +0100
moose@pc07:~/Desktop/Test$ lsattr
-----a-----------e- ./testfile
```

But I couldn't append to the file with gedit. With bash, it worked fine:

```bash
moose@pc07:~/Desktop/Test$ echo "One more line " >> testfile
moose@pc07:~/Desktop/Test$ cat testfile
Hello World.
One more line
```

So I guess I found another bug in gEdit.

<h3>Immutable</h3>
You can mark a file as immutable with <code>sudo chattr +i testfile</code>. It's funny, you can't see that with <code>ls -l</code>, you have to use <code>lsattr</code>. I guess if you manage to get root privileges and want to troll somebody, you could set this bit. I think this might take quite a while until you recognize it.

<h3>Secure deletion and undeletable</h3>
When secure deletion is set with <code>chattr +s testfile</code> the operating system overwrites the file with random data when it is deleted.

<code>chattr +u testfile</code> makes your file undeletable. This is strange. You can still delete the file with <code>rm</code>, but the system will not overwrite it. I've just <a href="http://unix.stackexchange.com/q/66870/4784">asked a question on SE</a>.

<h3>Synchronous update</h3>
when you set <code>chattr +S testfile</code> the file gets directly written to the HDD and not buffered by the kernel cache.
