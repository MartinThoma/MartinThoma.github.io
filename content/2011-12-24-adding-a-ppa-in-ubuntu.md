---
layout: post
lang: en
title: Adding a ppa in Ubuntu
slug: adding-a-ppa-in-ubuntu
author: Martin Thoma
date: 2011-12-24 15:30:06.000000000 +01:00
category: Cyberculture
tags: Ubuntu, PPA
featured_image: 2011/09/Ubuntu-Logo.png
---
PPAs (<a href="http://en.wikipedia.org/wiki/Personal_Package_Archive">Personal Package Archive</a>) provide additional resources. They are small repositories you can add to get some special content.

You can add them with Bash:
```bash
sudo add-apt-repository ppa:<repository-name>
```

Lets make an example:

If you want to install <a href="http://clipgrab.de/en">Clipgrab</a>, you add the repository first:
```bash
sudo add-apt-repository ppa:clipgrab
```

Then you have to update your sources:
```bash
sudo apt-get update
```

Now you can install clipgrab the usual way:
```bash
sudo apt-get install clipgrab
```

<h2>Further Reading</h2>
<ul>
  <li><a href="https://help.ubuntu.com/community/Repositories/CommandLine">Repositories and the CommandLine</a></li>
  <li><a href="http://wiki.ubuntuusers.de/Clipgrab">Clipgrab</a> (German)</li>
</ul>
