---
layout: post
status: publish
published: true
title: Adding a ppa in Ubuntu
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 9931
wordpress_url: http://martin-thoma.com/?p=9931
date: 2011-12-24 15:30:06.000000000 +01:00
categories:
- Cyberculture
tags:
- Ubuntu
- PPA
comments: []
---
PPAs (<a href="http://en.wikipedia.org/wiki/Personal_Package_Archive">Personal Package Archive</a>) provide additional resources. They are small repositories you can add to get some special content.

You can add them with Bash:
[bash]sudo add-apt-repository ppa:<repository-name>[/bash]

Lets make an example:

If you want to install <a href="http://clipgrab.de/en">Clipgrab</a>, you add the repository first:
[bash]sudo add-apt-repository ppa:clipgrab[/bash]

Then you have to update your sources:
[bash]sudo apt-get update[/bash]

Now you can install clipgrab the usual way:
[bash]sudo apt-get install clipgrab[/bash]

<h2>Further Reading</h2>
<ul>
  <li><a href="https://help.ubuntu.com/community/Repositories/CommandLine">Repositories and the CommandLine</a></li>
  <li><a href="http://wiki.ubuntuusers.de/Clipgrab">Clipgrab</a> (German)</li>
</ul>
