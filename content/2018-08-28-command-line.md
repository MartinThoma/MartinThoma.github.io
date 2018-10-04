---
layout: post
title: Command Line
slug: command-line
author: Martin Thoma
status: draft
date: 2018-08-28 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/star.png
---
As a software developer, I work daily many hours on the command line. This
article summarizes some tools and tricks to speed up this work.


## The basics

[Bash](http://tiswww.case.edu/php/chet/bash/bashtop.html), [ZSH](http://www.zsh.org/), [Fish](https://fishshell.com/) are Linux shells.

[Oh-my-ZSH](https://ohmyz.sh/) is a plugin for ZSH which is AWESOME!


## Commands

* `cd`: Change directory, e.g. `cd ..`, `cd /home`, `cd foo/bar/baz`
* `pwd`: Print the working directory
* `ls`: List the contents of the current directory
* `history`: Show the last commands executed in the shell
* `grep`: Pattern search
* `cat filename`: print the contents of `filename` to the output
* `man`: show manual / help page

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
often contain configuration files.


## Tools

* `ncdu`: Find what is eating your disk space and delete it on the fly.
* [`httpie`](https://httpie.org/): Command line HTTP client
* [`jq`](https://stedolan.github.io/jq/): JSON query tool
* [`ranger`](https://ranger.github.io/)
* [`tmux`](https://gist.github.com/MohamedAlaa/2961058)
