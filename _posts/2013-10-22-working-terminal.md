---
layout: post
title: Working with Terminal
author: Martin Thoma
date: 2013-10-22 10:40:46.000000000 +02:00
categories:
- Code
tags:
- Linux
- Command Line
- Bash
- ZSH
- Terminal
- Shell
featured_image: 2011/09/Gnome-Terminal.png
alias: [/working-terminal/bash-vs-zsh-spelling-correction/index.html,/working-terminal/bash-vs-zsh-time/]
---
I've just switched from <a href="https://en.wikipedia.org/wiki/Bash_(Unix_shell)">Bash</a> to <a href="https://en.wikipedia.org/wiki/Z_shell">ZSH</a> because of <a href="https://github.com/robbyrussell/oh-my-zsh">oh-my-ZSH</a>. I think this is just the right time to explain the words Shell, command line, Terminal, Bash and ZSH.

<a href="https://en.wikipedia.org/wiki/GNOME_Terminal">Terminal</a> is an terminal emulator, sometimes also called a "terminal window". I work in a window environment (MATE) and I want to use command line tools within that environment. So I need a "terminal window":
{% caption align="aligncenter" width="300" caption="Terminal Window with ZSH and Bash" url="../images/2013/10/teriminal-window-300x168.png" alt="Terminal Window with ZSH and Bash" height="168" class="size-medium wp-image-76644" %}

ZSH and Bash are both Unix shells. A shell is a command line interpreter that provides a text-based user interface.

Command line describes the textual way you interact with the computer. When you're in a graphical user interface situation you interact by manipulating windows with your keyboard/mouse. When you're in a text-based user interface situation, you interact by entering commands in a line (hence command line).

## Oh-my-ZSH Installation ##
Oh-my-ZSH is a plugin for ZSH. I think this plugin is very good and makes a big difference to Bash. So when you look at the screenshots below, keep in mind that this is not a "plain vanilla" zsh.

<ul>
  <li>Install "<a href="https://github.com/robbyrussell/oh-my-zsh">Oh-my-ZSH</a>"</li>
  <li>Install "<a href="https://github.com/Lokaltog/powerline-fonts">powerline fonts</a>" and change your Terminal font to one of them</li>
  <li>Change your Terminal theme to "agnoster" by setting <code>ZSH_THEME="agnoster"</code> in <strong>~/.zshrc</strong>
</li>
  <li>Set your terminal theme to "Solarized Dark" (<a href="http://www.mintmate.org/?p=13">description</a>)</li>
  <li>Make ZSH your default Shell in MATE Terminal (<a href="http://askubuntu.com/a/342342/10425">description</a>) and eventually <code>sudo chsh -s /usr/bin/zsh username</code></li>
</ul>

## ZSH and Bash ##
Here are some differences. On the left side is zsh, on the right is bash:
{% gallery columns="2" %}
    ../images/2013/10/bash-vs-zsh-cd.png    "Bash vs zsh: cd command completion"
    ../images/2013/10/bash-vs-zsh-git.png   "Bash vs zsh: Git prompt indicator"
    ../images/2013/10/bash-vs-zsh-spelling-correction.png   "Bash vs zsh: Spelling correction"
    ../images/2013/10/bash-vs-zsh-time.png  "Bash vs zsh: time command"
{% endgallery %}

I like the time command of bash more, but that's it. All other interactions are either almost the same or better in zsh. I especially like that zsh doesn't print everything again when you autocomplete with tab. And it also autocompletes when you make an capitalization error.

I also begin to like the Git-specific prompt indicators:
{% caption align="aligncenter" width="236" caption="ZSH 'git add' indicator" url="../images/2013/10/oh-my-zsh-git-added.png" alt="ZSH 'git add' indicator" height="42" class="size-full wp-image-76671" %}

## Some usefull tools ##
### ack ###
You might already know `grep`. And if you've worked with it, you 
might already have typed something like the following:

```bash
grep --exclude-dir=".svn" "searchterm" *
grep -rI "onlytextSearchterm" .
```

An alternative to `grep` is `ack` (for Ubuntu users: `ack-grep`).
See [beyondgrep.com](http://beyondgrep.com/).

## Windows

It seems to be possible to get something similar (the same?) for Windows. See
[OH MY CYGWIN](https://github.com/haithembelhaj/oh-my-cygwin/blob/master/README.md).