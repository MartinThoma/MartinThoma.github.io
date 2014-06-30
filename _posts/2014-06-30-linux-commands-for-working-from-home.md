---
layout: post
title: Linux Commands for Working from home
author: Martin Thoma
date: 2014-06-30 13:41
categories:
- Code
tags:
- SSH
- Shell
featured_image: logos/shell.png
---

This article is just a collection of commands and shortcuts I need quite often.

## Creating a single archive file from a complete folder

```bash
$ tar -zcvf ~/[target file].tar.gz [folder you want to copy]
```

## Getting a file from a remote host to localhost

```bash
$ scp [username]@[host]:[path/to/remote/file] [path/to/local/folder]
```

## Shell Shortcuts

Copy a selected text:

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>

Paste a text from clipboard to the command line:

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>

Copy a selected text from the command line and paste it:

<kbd>Mouse wheel click</kbd>

Search through the history of commands you have typed before:

<kbd>Ctrl</kbd> + <kbd>R</kbd>

## Web stuff
### Watching the Apache error log

```bash
$ tail -f  /var/log/apache2/error.log
```

### Truncating the Apache error log

```bash
$ sudo truncate -s 0 /var/log/apache2/error.log
```

### Finding php.ini

```bash
$ php -i | grep "Loaded Configuration File"
```

### Importing data to MySQL

```bash
$ mysql --host localhost -u root -p write-math < wm_raw_draw_data.sql
```