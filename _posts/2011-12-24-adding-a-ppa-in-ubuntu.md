---
layout: post
title: Adding a ppa in Ubuntu
author: Martin Thoma
date: 2011-12-24 15:30:06.000000000 +01:00
categories:
- Cyberculture
tags:
- Ubuntu
- PPA
featured_image: 2011/09/Ubuntu-Logo.png
---
PPAs (<a href="http://en.wikipedia.org/wiki/Personal_Package_Archive">Personal Package Archive</a>) provide additional resources. They are small repositories you can add to get some special content.

You can add them with Bash:
{% highlight bash %}sudo add-apt-repository ppa:<repository-name>{% endhighlight %}

Lets make an example:

If you want to install <a href="http://clipgrab.de/en">Clipgrab</a>, you add the repository first:
{% highlight bash %}sudo add-apt-repository ppa:clipgrab{% endhighlight %}

Then you have to update your sources:
{% highlight bash %}sudo apt-get update{% endhighlight %}

Now you can install clipgrab the usual way:
{% highlight bash %}sudo apt-get install clipgrab{% endhighlight %}

<h2>Further Reading</h2>
<ul>
  <li><a href="https://help.ubuntu.com/community/Repositories/CommandLine">Repositories and the CommandLine</a></li>
  <li><a href="http://wiki.ubuntuusers.de/Clipgrab">Clipgrab</a> (German)</li>
</ul>
