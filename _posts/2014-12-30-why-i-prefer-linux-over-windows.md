---
layout: post
title: Why I prefer Linux over Windows
author: Martin Thoma
date: 2014-12-30 21:25
categories:
- The Web
tags:
- Linux
- Windows 7
featured_image: 2012/12/tux-vs-windows.png
---

<div class="info">This is a quick article I had for quite a while as a draft.It might not be finished or have other problems, but I still want to share it.</div>

Some friends wondered why I prefer Linux over Windows. As I am currently using
only Linux, I can make some examples.

Here is an open list, why I prefer Linux over Windows:

## No marketing strategies
Windows 7 comes in may flavours: Windows 7 Home, Windows 7 Home Premium,
Windows 7 Ultimate, Windows 7 Enterprise, Windows 7 Professional, ... (see <a
href="../microsoft-product-flavor-hell/">Microsoft product flavor hell</a>)

I have to admit that the choice of Linux can be difficult, too. You can choose
from different distributions like Ubuntu, Suse, Fedora, ... (see <a
href="http://distrowatch.com/dwres.php?resource=major">distrowatch.com</a>) and
some distributions offer different <a
href="http://en.wikipedia.org/wiki/Comparison_of_X_Window_System_desktop_environments">desktop
environments</a> like GNOME and KDE. The important difference is that Linux
flavors depend on your needs, but Windows flavors depend on your money.

## User-friendly system
As a Ubuntu 10.04 LTS user, I think that Ubuntu is much more user friendly than
Windows 7. You have much more control about your system than you have on
Windows (see <a href="../why-are-microsoft-products-so-user-unfriendly/">Why
are Microsoft products so User unfriendly?</a>)

Here are some everyday examples:
<ul>
  <li>Chaning the sound volume on a Notebook: You will see an indicator in Ubuntu <a href="http://www.markshuttleworth.com/wp-content/uploads/2009/02/notify-osd-screenshot.png">like this</a>. On Windows, you have to guess or wait until your movie starts</li>
  <li>Taking a screenshot: In Ubuntu, you only have to press "Print Screen". On Windows, you have to know Snipping tool or install some additional software. Additionally, it seems not to be possible to get a the key "Print Screen" as a shortcut for taking screenshots (<a href="http://superuser.com/q/524357/64857">source</a>).</li>
  <li>Different workspaces, pinning a window to "always in foreground" is definitely missing in Windows.</li>
  <li><a href="../pdf-printing-on-windows-7/">PDF-Printers</a>: oh my god. This is really sad.</li>
</ul>

## Better community
When I have questions for my system, I can ask them on <a
href="http://askubuntu.com/users/10425/moose?tab=questions">askubuntu.com</a>,
<a
href="http://unix.stackexchange.com/users/4784/moose?tab=questions">unix.stackexchange.com</a>
or on <a href="http://forum.ubuntuusers.de/">ubuntuusers.de</a>. I usually get
friendly answers that help me to fix my problem within a few minutes.

Where do I find answers to Windows questions? I have tried <a href="http://superuser.com/users/64857/moose?tab=questions">superuser.com</a>, but is there anything else?

## Repositories
When I want to install <code>something</code> on my Ubuntu machine, I simply
type:

```bash
sudo apt-get install something
```

When I want to install something on Windows, I have to Google for it. When I
find a tool which seems to fit, I have to find out if it is for free or if it's
only a trial version. Then I need to find a way to download it and make sure
that it's not malware.

When I want to update all software I have on my linux machine, I type:

```bash
sudo apt-get update
sudo apt-get upgrade
```

After this command, my system and every single piece of software I have
installed is updated. The updates are automatically installed in the
background. A restart might be necessary, but until the restart is done the old
software is used.

On Windows, I have to:
<ol>
  <li>Click on the start button</li>
  <li>Type "update" in the search bar</li>
  <li>Click on "Search for updates"</li>
  <li>Install all updates</li>
</ol>

A restart might be required. But I can't simply make the restart when I want
to. No, on Windows you will get reminded. You can choose the delay (max. 4
hours) of the reminder, but you can't disable it. And this is only an update
for the operating system. You have to look for updates of your software by
yourself. For every single piece of software! This is not so easy. How do you
find a reliable source of Updates e.g. for Unreal Tournament 2004?

## Terminal

You can do everything with terminal. When the system is slowing down, I press
<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F4</kbd>, log into the shell,
call `top` and `kill` the process which slows my system down.

And I really like [ZSH and Oh-My-ZSH](//martin-thoma.com/working-terminal/).

## Linux is gratis

You don't have to pay for it. In comparison, Windows 7 costs now (31.12.2014)
about 50 Euro on Amazon. Although it is already outdated.

## Simple stuff

There are some simple, little things which I like when I use Linux. I can't
name them all, but some that come to my mind are:

### LiveCD

Isn't it great to have the possibility to use the OS from a CD / DVD only?
This gives you the possibility to check if your system runs (or to diagnose
what's going wrong) without chaning anything.

### Installation setup

The installation setup is great. It detects at the beginning if everything is
ok (disk space, internet connection, battery) and tells you in simple words
what is wrong. To chose your time zone you are shown a very simple graphic
and by now the default was always correct for me. It continues with keyboard
detection. Although the default was always wrong for me by now, it has an
awesome auto-detection tool. You simply have to type some letters and it
returns your layout. Great!

## Reasons to stay with Windows
Although I don't like Windows 7 for many reasons, I can see some reasons to
stay with Windows:

* Linux doesn't support your hardware (see <a href="../check-computer-hardware-for-linux-compatibility/">Check Computer / Hardware for Linux-compatibility</a>)
* Linux doesn't support your software AND no free alternative exists (e.g. Photoshop for professionals)

## Pseudo reasons for Linux

A pseudo-reason is an argument which might be true, but is not important at
all for the person who wrote it.

### Security
I often hear that people like Linux because of higher security. I don't think
that this is a real reason, as I have never heared of any end user having
switched because of security reasons. I also don't think that there is a
significant difference of the bare systems in security.

### Freedom to change code
Some people argue, that you can change the code of Linux / OpenSource programs
according to your needs. This is only an argument, if you have done it at least
once.

## Pseudo reasons against Linux

### Linux is only for geeks

This is obviously not true. I know at least some non-geeks who are able to use
it.

### Linux supports NO games!

Not true either. Steam gives A LOT of high quality games to Linux and you
also have the possibility to use wine.

However, if you want a specific game that might be a different story.