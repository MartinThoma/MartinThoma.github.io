---
layout: post
status: publish
published: true
title: Software Versioning Cheat Sheet
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 22591
wordpress_url: http://martin-thoma.com/?p=22591
date: 2012-04-18 07:00:59.000000000 +02:00
categories:
- Code
tags:
- cheat sheet
- software versioning
- svn
- git
comments: []
---
This <a href='http://martin-thoma.com/wp-content/uploads/2012/04/versioning-cheat-sheet.pdf'>Software Versioning Cheat Sheet</a> has very basic information aboout the installation and usage of Subversion and Git. (The <a href='http://martin-thoma.com/wp-content/uploads/2012/04/versioning-cheat-sheet.zip'>LaTeX Source Code</a> is here.)

If you're at the KIT and you have SWT, then you'll probably need this command:

[bash]svn checkout https://svn.ipd.kit.edu/lehre/vorlesung/SWT1/SS12/stud/ SWT/ --username swt1[/bash]
You will be asked for a password. I hope you remember it.

<h2>SVN</h2>
[bash]svn co URL LocalTarget --username yourUserName[/bash]
Source: <a href="http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html">svn checkout</a>

[bash]svn up[/bash]
Source: <a href="http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.update.html">svn update</a>

[bash]svn log -l 4[/bash]
Source: <a href="http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html">svn log</a>

<h3>Updating the repository</h3>
You can update a SVN repository with this command:
[bash]svn up [path][/bash]

If you need to execute the command often, you might want to define an alias. aliases are shorthands for long commands in the bash. To create a permanent one, add the following line to your ~/.bashrc file:
[bash]alias swt='svn up /home/moose/Studium/SWT'[/bash]
Now you only have to enter "swt" to execute "svn up /home/moose/Studium/SWT".

<h3>Nice diffs</h3>
You can modify your config file:
[bash]gedit ~/.subversion/config[/bash]

and change <code>diff-cmd</code> to <code>meld</code>.

<h3>Compare revisions</h3>
[bash]svn diff -r 63:64[/bash]

compares revision number 63 with revision number 64 with the tool you defined (see Nice diffs).

<h2>Git</h2>
<h3>Nice diffs</h3>
If you want a GUI for <code>git diff</code>, then you should do the following:

Install meld:
[bash]sudo apt-get install meld[/bash]

Got to <code>/bin</code> and create a Shell-Script called <strong>git-meld</strong> with the following content:
[bash]#!/bin/bash
meld "$2" "$5"[/bash]

Make it executable:
[bash]chmod +x git-meld[/bash]

Add it to your git configuration:
[bash]git config --global diff.external git-meld[/bash]

Enjoy this experience when entering <code>git diff</code>:
[caption id="attachment_35541" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2012/04/git-meld.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/04/git-meld-300x129.png" alt="Using Meld with GIT" title="Using Meld with GIT" width="300" height="129" class="size-medium wp-image-35541" /></a> Using Meld with GIT[/caption]

See also <a href="http://jeetworks.org/node/90">jeetworks.org</a> for some other solutions.

<h3>GitHub</h3>
<h4>Preparation</h4>
Read the guide "<a href="https://help.github.com/articles/generating-ssh-keys">Generating SSH keys</a>" for more information on SSH and "<a href="http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup">Getting Started - First-Time Git Setup</a>" for Git-specific questions.

[bash]cd ~/.ssh
ssh-keygen -t rsa -C "info@martin-thoma.de"
git config --global user.name "Martin Thoma"
git config --global user.email info@martin-thoma.de[/bash]

<h4>Clone</h4>
Clone a GITHub repository:
[bash]git clone git@github.com:MartinThoma/matrix-multiplication.git[/bash]

<h3>Snippets</h3>
Reset a single file to the latest revision on the server:
[bash]git checkout HEAD file/to/restore[/bash]

Get the latest diff:
[bash]git diff HEAD @{1}[/bash]

<h2>Resources</h2>
<ul>
  <li><a href="http://svnbook.red-bean.com/en/1.6/">Version Control with Subversion</a>: a great explanation how to use subversion, e.g. <a href="http://svnbook.red-bean.com/en/1.6/svn.ref.svn.c.export.html">svn export</a></li>
  <li>StackOverflow: <a href="http://stackoverflow.com/questions/3233059/basic-subversion-question">Which files should be put under version controll?</a></li>
  <li>GitHub:  <a href="http://help.github.com/remotes/">Remotes</a></li>
</ul>
