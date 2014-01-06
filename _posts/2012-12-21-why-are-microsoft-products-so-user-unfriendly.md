---
layout: post
title: Why are Microsoft products so User unfriendly?
author: Martin Thoma
date: 2012-12-21 17:00:31.000000000 +01:00
categories:
- Code
tags:
- eclipse
- windowsrage
- Microsoft
- Visual Studio
- Windows 7
featured_image: 2012/12/loading-times.png
---
Another rage-post ... 

<h2>Loading times</h2>
Did you ever work with eclipse? Then you might know the feeling, that it takes an eternity until Eclipse has started. I've just stopped it. 

Eclipse takes 30 seconds to start:
{% caption align="aligncenter" width="300" caption="Eclipse Juno loading screen" url="../images/2012/12/eclipse-juno-loading-300x200.png" alt="Eclipse Juno loading screen"  height="200" class="size-medium wp-image-51161" %}

Visual Studio 2012 takes 1 minute and 15 seconds to start:
{% caption align="aligncenter" width="229" caption="Visual Studio Ultimate - Loading screen" url="../images/2012/12/visual-studio-2012-loading-229x300.png" alt="Visual Studio Ultimate - Loading screen"  height="300" class="size-medium wp-image-51171" %}

But that's not the worst. It's okay if it takes long to start, if it's later a swift. But it's not. I get those loading screens from time to time without having done anything:

{% caption align="aligncenter" width="300" caption="Visual Studio 2012 - loading something without any action from my side" url="../images/2012/12/visual-studio-2012-loading-times-300x202.png" alt="Visual Studio 2012 - loading something without any action from my side"  height="202" class="size-medium wp-image-51181" %}

Why is it loading something from time to time without interaction? What does Visual Studio load?

<h2>Control</h2>
The next big problem I have with Microsoft products is the lack of control. I would like to know what are the effects of a command I use before I use it - no matter if it is a command line command or a GUI or key-press-combination command. As it is very difficult to make GUI commands unambiguous, I really like the command line for some tasks. Why doesn't Windows offer a default command line that is usable? I mean, yes, you have the PowerShell ... but why isn't it the default shell? Why does the user have to know that there are other (better?) shells? Is there any reason not to use the PowerShell in Windows 7?
And even the PowerShell misses some really basic tools. I mean, did you try the path autocompletion (with tab) on bash (the Linux shell)? It completes the path / command, if there is only one possibility. If there are more possibilities, the user gets displayed all options (if there are too many, he will get asked before all are displayed). The Windows-shells go through each possibility. 

Here are some screenshots of the shells displaying the content of the current folder:
{% caption align="aligncenter" width="300" caption="Windows32 cmd" url="../images/2012/12/CWindowssystem32cmd-300x204.png" alt="Windows32 cmd"  height="204" class="size-medium wp-image-51251" %}

{% caption align="aligncenter" width="300" caption="Windows PowerShell v1.0" url="../images/2012/12/WindowsPowerShellv1.0-300x231.png" alt="Windows PowerShell v1.0"  height="231" class="size-medium wp-image-51261" %}

Now compare this to Linux:

{% caption align="aligncenter" width="300" caption="Gnome shell (bash)" url="../images/2012/12/gnome-shell-300x117.png" alt="Gnome shell (bash)"  height="117" class="size-medium wp-image-51271" %}

Where do you find easier what you need? And why do they have a black background with white font color? Try to work with this for some hours and than compare it to a shell with black font size and white background...

<h3>Missing (command line) tools</h3>
I like using git / svn from command line. But the default way to use SVN (and eventually GIT) seems to be by GUI. Why results in a crappy, overblown right click menu:

{% caption align="aligncenter" width="287" caption="Windows right click menu" url="../images/2012/12/windows-right-click-287x300.png" alt="Windows right click menu"  height="300" class="size-medium wp-image-51291" %}

Now compare this to Linux 10.04 with GNOME:
{% caption align="aligncenter" width="300" caption="Right click menu on GNOME 2" url="../images/2012/12/gnome-2-right-click-300x292.png" alt="Right click menu on GNOME 2"  height="292" class="size-medium wp-image-51311" %}

And I should also mention that I didn't clean up my Linux system for over one year. I use it every day, install new software, remove software, forget to remove software. I have git and svn on my Linux machine as well as Apache, Python, some games, ...

The Windows 7 machine is a fresh install. It has better hardware and I only use it for work (so it basically only has TurtoiseSVN, Visual Studio and IIS). I guess this would be even worse if I used it every day.

<h3>Updates</h3>
Windows makes its updates at very bad times. Sometimes it just makes an update and you have to wait for quarter of an hour to finish it, before you can shut down. Why? Can't you just ask the user before you make an update? A friend of mine had a tutorial after which she wanted to go to a Christmas party. Guess what happened: Before she could shut down the computer, Windows decided to make automatically an update. Took about 15 - 20 minutes. No Christmas parties for Windows users.

{% caption align="aligncenter" width="426" caption="Automatic shutdown of Windows" url="../images/2012/12/shutdown-windows.png" alt="Automatic shutdown of Windows"  height="362" class="size-full wp-image-54251" %}

{% caption align="aligncenter" width="300" caption="Windows 7: Automatic update installation" url="../images/2012/12/windows-7-automatic-update-installation-300x225.jpg" alt="Windows 7: Automatic update installation"  height="225" class="size-medium wp-image-54261" %}

Windows really shut down my computer automatically and blocked it for about 15 minutes. What if I had to hold a presentation? What if I downloaded something?

<h2>Nice features, crappy realization</h2>
Windows has a very nice feature: You an search at the "start". But why doesn't it work for every program? I've searched for "winver.exe", a program shipped per default from Microsoft. Why can't you find this in start?
{% caption align="aligncenter" width="240" caption="Windows Start search" url="../images/2012/12/windows-start-search-240x300.png" alt="Windows Start search"  height="300" class="size-medium wp-image-51281" %}

If I have to type the whole name, this feature is essentially useless...

<a href="http://en.wikipedia.org/wiki/Outlook_Web_App">Microsoft OWA</a> is an online email service. A friend showed me this usability desaster:
{% caption align="aligncenter" width="300" caption="Microsoft OWA" url="../images/2012/12/microsoft-owa-300x157.png" alt="Microsoft OWA"  height="157" class="size-medium wp-image-54791" %}

<h2>No structure for programs</h2>
Where do programs get installed? 
<ul>
  <li>C:\</li>
  <li>C:\Program Files</li>
  <li>C:\Program Files (x86)</li>
</ul>

If you have a German system, the explorer will show a German path although the underlying path is English. What the hell? And <a href="../microsoft-product-flavor-hell/" title="Microsoft product flavor hell">switching languages isn't easy on Microsofts Systems</a>.

<h2>Drivers</h2>
<h3>Installation CD</h3>
Although many drivers exist for Windows, you have to install them almost always by CD.

<h3>Mouse drivers</h3>
You have to INSTALL mouse drivers! WTF! I expect an USB mouse to work immediately and not to get something like that:
{% caption align="aligncenter" width="300" caption="Installing USB mouse in Windows 7" url="../images/2012/12/usb-mouse-windows-7-300x101.png" alt="Installing USB mouse in Windows 7"  height="101" class="size-medium wp-image-52321" %}

<h2>Windows Explorer</h2>
<h3>No tabs</h3>
Clover tries to fix that, but I don't want to install a third party tool for such a basic tool.

<h3>Structure</h3>
{% caption align="aligncenter" width="300" caption="Windows 7 Explorer" url="../images/2012/12/windows-7-explorer-300x220.png" alt="Windows 7 Explorer"  height="220" class="size-medium wp-image-52481" %}

<h2>Shell</h2>
There is so much wrong with the Windows Shells:
<ul>
  <li>You can't maximize it (see <a href="http://superuser.com/a/80098/64857">explantation</a>)</li>
  <li>Crappy autocomplete: In Linux, if you have multiple ways to autocomplete, you get a list of the options. Windows 7 only pics the first.</li>
  <li>PowerShell: Its soooo slow! I don't want to wait for my shell to start!</li>
</ul>

{% caption align="aligncenter" width="300" caption="Windows Terminal in 'Full Screen'" url="../images/2012/12/full-screen-terminal-300x169.png" alt="Windows Terminal in 'Full Screen'"  height="169" class="size-medium wp-image-54771" %}

<h2>A wrap-up for Windows 8</h2>
<iframe width="512" height="288" src="http://www.youtube.com/embed/WTYet-qf1jo" frameborder="0" allowfullscreen></iframe>

<h2>Microsoft Bob</h2>
Have you ever heard of <a href="http://en.wikipedia.org/wiki/Microsoft_Bob">Microsoft Bob</a>? I guess we should not complain about Windows 8 desktop, if you have seen this desktop environment interface...

<iframe width="512" height="384" src="http://www.youtube.com/embed/ZegWedG-jk4" frameborder="0" allowfullscreen></iframe>
