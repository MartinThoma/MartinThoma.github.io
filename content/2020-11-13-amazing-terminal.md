---
layout: post
title: How to get an amazing Terminal
subtitle: In Windows and Linux; including prompts, fonts, and colors
slug: amazing-terminal
URL: https://towardsdatascience.com/how-to-get-an-amazing-terminal-91619a0beeb7
author: Martin Thoma
date: 2020-11-13 20:00
category: Code
tags: Code, Linux, Windows
featured_image: logos/star.png
---
As a developer with 10+ years of experience, I love using the shell. The commands never change, I can create custom shortcuts, it’s reliable and fast. The defaults are not great, though. After reading this article, you will know how to get an awesome shell + terminal on your system.

## Terminology

The **shell** is what actually executes the command. The **terminal** is a
wrapper that runs the shell.

The **terminal** is where you set the font face, font size, color schemes, support for multiple tabs. Examples for terminal emulators are [GNOME terminal](https://en.wikipedia.org/wiki/GNOME_Terminal), [Konsole](https://en.wikipedia.org/wiki/Konsole) on KDE, [Terminator](https://en.wikipedia.org/wiki/Terminator_(terminal_emulator)), and [XTerm](https://en.wikipedia.org/wiki/Xterm). On Linux, I recommend keeping the default. On Windows, the [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) is awesome. On Mac, I’ve heard good things about [iTerm 2](https://www.iterm2.com/).

![Four terminal emulators on Linux (Gnome Terminal, Konsole, XTerm, Terminator). XTerm does not directly support tabs. The others have 2 tabs open. All of them run the Bash shell. The image was created by Martin Thoma.](https://cdn-images-1.medium.com/max/2754/1*OhItafIJ3T--kdh9F716VA.png)*Four terminal emulators on Linux (Gnome Terminal, Konsole, XTerm, Terminator). XTerm does not directly support tabs. The others have 2 tabs open. All of them run the Bash shell. The image was created by Martin Thoma.*

The **shell** stores the history of entered commands, defines how you set
environment variables, how you switch the current directory. Examples for
shells on Linux are [ZSH](https://en.wikipedia.org/wiki/Z_shell),
[Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)),
[fish](https://en.wikipedia.org/wiki/Fish_(Unix_shell)). On Windows, the
typical shells are [PowerShell](https://en.wikipedia.org/wiki/PowerShell). You
can see which shell you are running by executing echo $0 . On Linux, it’s most
likely Bash.

![Three Linux shells (ZSH, Bash, fish) within the Gnome Terminal. I’ve heavily customized the ZSH shell; Bash and fish show the default. You can see that fish has an in-line autosuggestion feature that the two other shells lack. Image by Martin Thoma.](https://cdn-images-1.medium.com/max/2692/1*FYSzehDiGtZNHjowCZxUXg.png)*Three Linux shells (ZSH, Bash, fish) within the Gnome Terminal. I’ve heavily customized the ZSH shell; Bash and fish show the default. You can see that fish has an in-line autosuggestion feature that the two other shells lack. Image by Martin Thoma.*

Every shell has a **prompt**. The prompt is what is written before your cursor.
It signalizes that you can enter a command and gives useful context
information. In the example above, the prompt contains the user name `moose`,
the current computer `pc08`, the current working directory
`~/GitHub/MartinThoma/flake8-simplify`, the active git branch `feature/19` and
the fact that there are modifications `±`.

## Fonts

No matter what you take, the font matters. You might want to have a monospace
font. And you for sure want a [powerline
font](https://github.com/powerline/fonts); trust me with that one. The
powerline font gives your shell the possibility to use characters that look
like images. It can make the prompt way nicer.

I like [Ubuntu Mono](https://github.com/powerline/fonts/tree/master/UbuntuMono) and [Droid Sans Mono](https://github.com/powerline/fonts/tree/master/DroidSansMono):

![The top line is Ubuntu Mono, the bottom example is written in Droid Sans Mono. I like Ubuntu Mono a bit better, but both are reasonable fonts. Image by Martin Thoma](https://cdn-images-1.medium.com/max/2236/1*TrxyQTnHKZA7DPuLZT4sfg.png)*The top line is Ubuntu Mono, the bottom example is written in Droid Sans Mono. I like Ubuntu Mono a bit better, but both are reasonable fonts. Image by Martin Thoma*

There are also “programming fonts” like [Fira Code](https://github.com/tonsky/FiraCode) or [Jetbrains Mono](https://www.jetbrains.com/lp/mono/?ref=betterwebtype). I don’t like them, because they make it harder for me to really know what is written. They look nice, though.

## Windows Terminal

First, make sure you have the [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?source=lp&activetab=pivot:overviewtab) installed:
[**Get Windows Terminal — Microsoft Store**
*The Windows Terminal is a modern, fast, efficient, powerful, and productive terminal application for users of…*www.microsoft.com](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?source=lp&activetab=pivot:overviewtab)

Launch a terminal and navigate to the settings. It’s this small downwards pointing “arrow”:

![Click on “Settings”. The screenshot was taken by Martin Thoma](https://cdn-images-1.medium.com/max/2000/0*FSlD8BQx1mNP532h.png)*Click on “Settings”. The screenshot was taken by Martin Thoma*

You should see a JSON file which you can change to fit your taste. I have the following:

<iframe src="https://medium.com/media/db0a1b7a8b8d0eccc2a75276eec241da" frameborder=0></iframe>

Download and install all 4 “[DejaVu Sans Mono Powerline](https://github.com/powerline/fonts/tree/master/DejaVuSansMono)” fonts. On all systems I know, installing a font is done by double-clicking it. Then a window opens which has an “Install” button.

## Linux and Windows Terminal: Aminal

[Aminal](https://github.com/liamg/aminal) is a Terminal Emulator written in Go. It can be used on Linux, Windows, and Mac. It allows configuration via a configuration file and includes the color and keyboard shortcuts in it.

First, you need to install and configure Go on your system. On Ubuntu, it works like this:

```bash
$ sudo apt-get install golang libgl1-mesa-dev xorg-dev
$ export GOPATH="$HOME/go"
$ export GOBIN=$(go env GOPATH)/bin
```

Then you can install and run aminal:

```bash
$ go get -u github.com/liamg/aminal
$ aminal
```

## Linux: Gnome Terminal

The Gnome terminal can be customized by editing the profile. Here I set the [Ubuntu Mono derivate Powerline Regular](https://github.com/powerline/fonts/tree/master/UbuntuMono) with a font size of 12.

![Image by Martin Thoma](https://cdn-images-1.medium.com/max/2000/1*DTs5EGYqnJvLIN16WMhwBA.png)*Image by Martin Thoma*

The command is set to zsh as this is my favorite shell.

![Image by Martin Thoma](https://cdn-images-1.medium.com/max/2000/1*JNf0sfN047bN3AqDfVfRSw.png)*Image by Martin Thoma*

The colors are set to [solarized dark](https://ethanschoonover.com/solarized/) (left-to-right, top-line / bottom-line)

* Background: #2e3436 / #555753
* Dark Red: #cc0000 / Light Red: ef2929
* Dark Green: #4e9a06 / Light Green: #8ae234
* Dark Yellow: #c4a000 / Light Yellow: #fce94f
* Dark Blue: #3465a4 / Light Blue: #729fcf
* Dark Purple: #75507b / Light Purple: #ad7fa8
* Dark Teal: #06989a / Light Teal: #34e2e2
* Dark Gray: #d3d7cf / Light Gray: #eeeeec

![](https://cdn-images-1.medium.com/max/2000/1*P4xCOjogPGb3SdquyLiC2Q.png)

## Linux Shell: fish

Install the **fish** shell:

```bash
sudo apt-get install fish
```

Change the default shell in your terminal emulator to fish . Within Gnome
terminal, it is called “custom command”.

Then install “[**Oh My Fish**](https://github.com/oh-my-fish/oh-my-fish)”:

```bash
curl -L https://get.oh-my.fish | fish
```

And set the theme to **agnoster**:

```bash
omf install agnoster
omf theme agnoster
```

For cool features of the fish shell, read [Why I Use Fish Shell Over Bash and Zsh](https://medium.com/better-programming/why-i-use-fish-shell-over-bash-and-zsh-407d23293839) by [Alec Brunelle](undefined).

## Aliases

A core part of making the terminal awesome is making common commands short. To do so, you create an alias for a command — a shorter version of the original command. The most common example is changing a directory to go one level up. For example, if you are in /home/user/foo/bar , you want to get to /home/user/foo . In most shells, you have to enter cd .. . I like to abbreviate that to .. . So I have the alias alias ..='cd ..' . The syntax may vary, depending on your shell. For Bash, ZSH, and fish it is

```bash
alias short='long'
```

For bash, you insert them in ~/.bashrc , for ZSH in ~/.zshrc . In fish, [it is different](https://stackoverflow.com/a/2763014/562769).

Here are some aliases I like:

```bash
# Shorten things
alias ..='cd ..'
alias ...='cd ../../'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias c='clear'

# If your terminal supports colors, use them!
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias diff='colordiff'

# Works only if you have notify-send
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
```

## Summary

* Make sure you have a reasonable **terminal emulator**. I suggest [Gnome Terminal](https://en.wikipedia.org/wiki/GNOME_Terminal) for Linux, [iTerm 2](https://www.iterm2.com/) for Mac, and [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) for Windows.
* Install a good powerline font like [**Ubuntu Mono Powerline](https://github.com/powerline/fonts/tree/master/UbuntuMono)**.
* Adjust the **font face**, **font size**, and **color scheme** of your terminal emulator to your preferences.
* Install a good **shell**. I suggest [fish](https://en.wikipedia.org/wiki/Fish_(Unix_shell)) for Linux and [PowerShell](https://en.wikipedia.org/wiki/PowerShell) for Windows.
* Adjust the **prompt** of your shell to your needs. I like the **agnoster theme**.
