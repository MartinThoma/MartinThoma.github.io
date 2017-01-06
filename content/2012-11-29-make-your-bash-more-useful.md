---
layout: post
title: Make your Bash more useful
author: Martin Thoma
date: 2012-11-29 11:15:56.000000000 +01:00
category: Code
tags: Linux, Bash
featured_image: 2011/09/Gnome-Terminal.png
---
I just had the problem, that the bash prompt of my universities 
computer I've connected to via SSH looked like this:
`bash-4.0$`

<h2>Change the prompt</h2>
I think it's much more useful to see the path you're currently using.
To get the current path in your bash promt, you have to add the 
following snippet to your `.bashrc`:

```bash
# This will limit the path to 30 characters.
PROMPT_COMMAND='if [ ${#PWD} -gt 30 ]; then 
myPWD=${PWD:0:12}...
${PWD:${#PWD}-15}; else myPWD=$PWD; fi'
PS1="\u@\h \$myPWD$ "
```

(Source: <a href="http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html">cyberciti.biz</a>)

Reload your bash config with `source .bashrc` and you should 
instantly see the changes.

<h2>Aliases</h2>

```bash
# Add color to ls
alias ls="ls --color"
```

```bash
# simply update an svn-repository
alias swt='svn up /home/moose/Studium/SWT'
```
