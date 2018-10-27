---
layout: post
title: Command Line
slug: command-line
author: Martin Thoma
date: 2018-10-09 20:00
category: Code
tags: Development, Command line
featured_image: logos/code.png
---
As a software developer, I work daily many hours on the command line. This
article summarizes some tools and tricks to speed up this work.


## The basics

[Bash](http://tiswww.case.edu/php/chet/bash/bashtop.html), [ZSH](http://www.zsh.org/), [Fish](https://fishshell.com/) are Linux shells.

[Oh-my-ZSH](https://ohmyz.sh/) is a plugin for ZSH which is AWESOME!


## Commands


### Basics
* `cd`: Change directory, e.g. `cd ..`, `cd /home`, `cd foo/bar/baz`
* `pwd`: Print the working directory
* `ls`: List the contents of the current directory
* `man`: show manual / help page
* `history`: Show the last commands executed in the shell
* `rm filename.ext` removes `filename.ext`
* `mv filename.ext newname.jpg`: Rename a file

### Advanced

* `grep`: Pattern search
* `cat filename`: print the contents of `filename` to the output
* [`watch`](http://www.linfo.org/watch.html): run any designated command at regular intervals
* `free`: Memory consumption
* `top` and `htop`: display Linux processes
* [`find`](https://martin-thoma.com/wandering-through-the-depths-of-find/) and `locate`
* `tree`: Print a directory tree
* `cloc`: count lines of code
* `wc` : word count (or lines or characters)


### Professional

* `tmux` - terminal multiplexer
* [`direnv`](https://github.com/direnv/direnv)

### Internet

* `ping martin-thoma.com`: Check if you can reach a domain
* `ssh 123.168.0.1`: Connect to the IP `123.168.0.1`.
* `screen`: Create a new terminal session that can be detached / re-attached
* `ifconfig` - configure a network interface


### Hardware Analysis

* `lsusb`, `lspci`


## Alias

```
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'
```


## The Bang

There are various commands with the "bang" `!`:

* `!!`: Execute the last executed command in the bash history
* `!*`: Execute the command with all the arguments passed to the previous command
* `!ˆ`: Get the first argument of the last executed command in the bash history
* `!$`: Get the last argument of the last executed command in the bash history


## The Dash

`cd -` jumps back to the directory in which you were before:

```
/home/moose$ cd foobar
/home/moose/foobar$ cd -
/home/moose$
```

`git checkout -` jumps back to the branch in which you were before.


## .dotfiles git repository

Dotfiles a files which start with a `.`. Those files are hidden in Linux and
often contain configuration files. Here is [mine](https://github.com/MartinThoma/dotfiles).


## Tools

* [`ncdu`](https://dev.yorhel.nl/ncdu): Find what is eating your disk space and delete it on the fly.
* [`httpie`](https://httpie.org/): Command line HTTP client
* [`jq`](https://stedolan.github.io/jq/): JSON query tool
* [`ranger`](https://ranger.github.io/): console file manager
* [`tmux`](https://gist.github.com/MohamedAlaa/2961058)


## See also

* [Working with Terminal](https://martin-thoma.com/working-terminal/)
* [Working at FZI](https://martin-thoma.com/working-at-fzi/)
* [Converting Files with Linux](https://martin-thoma.com/converting-files-with-linux/)
