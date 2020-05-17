---
layout: post
title: Start long running processes via SSH
author: Martin Thoma
date: 2014-08-11 14:51
category: Code
tags: SSH, screen, nohup, Software Development
featured_image: logos/shell.png
---

## Screen

[`screen`](https://en.wikipedia.org/wiki/GNU_Screen) is a nice tool that can be
used to detach long running processes from the current SSH session - and be able
to get it again!


### Basic usage
You start it with

```shell
$ screen
```

You detach it with <kbd>Ctrl</kbd> + <kbd>a</kbd> and then <kbd>d</kbd>. After
you pressed this key combination, you will see

```shell
[detached]
```

You get it back again with:

```shell
$ screen -r
```

### Named sessions

You can start a named session with

```shell
$ screen -S foo
```

and get it back with

```shell
$ screen -r foo
```

## nohup

```shell
$ nohup command &
```

## See also

* [10 Screen Command Examples to Manage Linux Terminals](http://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/)
* [Matt Cutts: A quick tutorial on screen](http://www.mattcutts.com/blog/a-quick-tutorial-on-screen/)
* [Screen User's Manual](http://www.gnu.org/software/screen/manual/screen.html)
