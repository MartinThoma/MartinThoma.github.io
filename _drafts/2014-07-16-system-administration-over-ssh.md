---
layout: post
title: System Administration over SSH
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Linux
featured_image: logos/linux.png
---

I'm just making my first steps in system administration over SSH. I bought a
VPS at [Knallhart.de](http://knallhart.de/) (a great German provider).

As soon as I've figured out that the username is `root` I could begin:

```bash
# apt-get update
# apt-get upgrade
# apt-get install vim
# useradd -s /bin/bashh -m -d /home/moose moose
# apt-get install apache2
# apt-get install libapache2-mod-php5 php5 php5-mysql
# apt-get install mysql
```

## phpMyAdmin

For phpMyAdmin you have to add some repositories:

```bash
# vim cat /etc/apt/sources.list
```

add

```text
deb http://archive.ubuntu.com/ubuntu trusty main
deb http://archive.ubuntu.com/ubuntu trusty universe
```

Now you can install phpMyAdmin:

```
# apt-get install phpmyadmin
```

## FTP-Server

[ProFTPD](http://wiki.ubuntuusers.de/ProFTPD):

```bash
# apt-get install inetutils-inetd
# apt-get install proftpd-basic
# /etc/init.d/proftpd restart
```

## User configuration

Then I've added `/home/moose/.bashrc` and inserted:

```text
alias ls='ls --color=auto'
PS1="${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \$\[\033[00m\]"
```
