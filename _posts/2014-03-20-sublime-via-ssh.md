---
layout: post
title: How to use Sublime Text via SSH
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Sublime Text
- SSH
featured_image: logos/sublime-text.png
---

Sublime Text is the best editor I have ever used. One argument for vim and against
SSH could be that you can't simply use Sublime Text when you're accessing a
computer via SSH. But there is a way!

In the following, I will expain the simplest way how to remote edit files with
Sublime Text.

## Preparation on your computer

<ol>
    <li>Install and start Sublime Text.</li>
    <li>Install the <code>rsub</code> package via Package Controll.</li>
    <li>Open <code>~/.ssh/config</code>. Create it if id does not exist yet. Add this:

{% highlight text %}
Host myname
  Hostname pc123.your.network.com
  User mthoma
  RemoteForward 52698 127.0.0.1:52698
{% endhighlight %}

You can add more information like `User yourusername`.</li>
    <li>Start SSH with <code>ssh myname</code>.</li>
</ol>

## Server-Side steps

<ol start="5">
    <li>Download the <code>rmate</code> script:
{% highlight bash %}
curl https://raw.github.com/aurora/rmate/master/rmate > rmate
{% endhighlight %}
    </li>
    <li>Execute `./rmate yourfile`. It will open in your local Sublime Text!</li>
</ol>

## Improvements

It's not so nice to open files with `~/rmate filename` all the time. You can
use `rmate filename` after executing this command:

`sudo ln -s ~/rmate /usr/local/bin/rmate`