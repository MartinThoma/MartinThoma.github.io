---
layout: post
status: publish
published: true
title: Make your Bash more useful
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 49561
wordpress_url: http://martin-thoma.com/?p=49561
date: 2012-11-29 11:15:56.000000000 +01:00
categories:
- Code
tags:
- Linux
- Bash
comments: []
---
I just had the problem, that the bash prompt of my universities computer I've connected to via SSH looked like this:
<code>bash-4.0$</code>

<h2>Change the prompt</h2>
I think it's much more useful to see the path you're currently using. To get the current path in your bash promt, you have to add the following snippet to your <code>.bashrc</code>:

[text]# This will limit the path to 30 characters.
PROMPT_COMMAND='if [ ${#PWD} -gt 30 ]; then 
myPWD=${PWD:0:12}...
${PWD:${#PWD}-15}; else myPWD=$PWD; fi'
PS1="\u@\h \$myPWD$ "[/text]

(Source: <a href="http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html">cyberciti.biz</a>)

Reload your bash config with <code>source .bashrc</code> and you should instantly see the changes.

<h2>Aliases</h2>

[text]# Add color to ls
alias ls="ls --color"[/text]

[text]# simply update an svn-repository
alias swt='svn up /home/moose/Studium/SWT'[/text]
