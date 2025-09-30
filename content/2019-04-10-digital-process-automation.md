---
layout: post
lang: en
title: Digital Process Automation
slug: digital-process-automation
author: Martin Thoma
date: 2019-04-10 20:00
category: Cyberculture
tags: Automation, Shell, Productivity, Software Development
featured_image: logos/star.png
---
Many people work a significant amount of their time in front of a computer
today. And for many there are repetitive tasks. If the task is shared by many
people, this is a chance to develop dedicated software for it. Tabular
calculations (excel), writing documents (word), communicating (e-mail / chat
software) are some examples.

But there are other tasks which are not so common. Which are too specialized so
that it's not worth to pay a developer for designing, programming, testing,
maintenance; to pay for marketing, support, legal fees, and infrastructure.

This is the part where it becomes interesting to learn to use some tools.


## Text Editors

My favorite editor is [Sublime Text](https://martin-thoma.com/sublime-text/) hence
the links / names in the following are for it. But there are a couple of other
editors like [Atom](https://atom.io/) or [Visual Studio Code](https://code.visualstudio.com/)
that might have the same features.

Suppose you have a long list of names, phone numbers and e-mail addresses which
was provided by your "contacts" export:

```text
Martin Thoma; +49 123 456; foo@martin-thoma.de
Adam Aaron;+1 23 456 789; aaron@gmx.net
Berta Booth;002 345678; bb@googlemail.com
...
```

You want to insert the e-mail addresses in another system. But for that you
need to have only the e-mail addresses in double quotes `"`. How do you get that?

You could, of course, just manually copy all of the e-mail addresses to another
file. Assuming you have maybe 80 of those and it takes you 5 seconds for each
entry in average, you would need less than 7 minutes. That is ok. But it is
boring. And this kind of task will come more than once in your live.

So, instead, you can learn a tiny bit about **regular expressions**. They are a
way to define patterns in text. For example, `.` matches any single character
except a newline. With `+` you say that you want at least one of the things you
defined before the `+`. If you have the combination `.+`, it means that you
want to match any single character and as many of them as possible. By adding a
`?` you say you want to match as few as possible. Hence the search `.+?;.+?;`
means that you want to find any characters, then a `;`, then again any
caracters until the next `;` comes. In my editor it looks like this:

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2019/04/regex-matches.png"><img src="../images/2019/04/regex-matches.png" alt="3 matches for the RegEx .+?;.+?;" style="width: 512px;"/></a>
    <figcaption class="text-center">3 matches for the RegEx .+?;.+?;</figcaption>
</figure>

Then, I press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> to get **multiple cursors**.
From this point on everything I enter will be applied to all matches. First, you can
delete the name and phone number. Then you enter `"` to make the opening double
quote, then you press <kbd>End</kbd> to get to each end of the line. You press
<kbd>"</kbd> again to get the closing double quote. Task solved.

For 80 entries, this would have reduced the time from 7 minutes of an annoying
repetitive task to about 15 seconds.

For more about regex, you might want to look at a [cheat sheet](https://www.debuggex.com/cheatsheet/regex/python)
or go through a tutorial. Another cool thing is to enter different things with
multiple cursors, e.g. a sequence of numbers. Have a look at [Text Pastry](https://github.com/duydao/Text-Pastry/wiki/Number-Range) for that.

## Shortcuts

All operating systems and most programs define some keyboard shortcuts. If the
programs are really nice (like Sublime Text), you can re-define the shortcuts
yourself. This can save so much time. Some shortcuts I use all the time:


Operating System

<dl>
    <dt>Switch Windows</dt>
    <dd><kbd>Alt</kbd>+<kbd>Tab</kbd></dd>
    <dt>Switch Workspaces</dt>
    <dd><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>[arrow]</kbd></dd>
    <dt>Close Window</dt>
    <dd><kbd>Alt</kbd>+<kbd>F4</kbd></dd>
    <dt>Lock Screen</dt>
    <dd><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>L</kbd></dd>
</dl>

Programs

<dl>
    <dt>Save</dt>
    <dd><kbd>Ctrl</kbd>+<kbd>S</kbd></dd>
    <dt>Open</dt>
    <dd><kbd>Ctrl</kbd>+<kbd>O</kbd></dd>
    <dt>Switch Tabs</dt>
    <dd><kbd>Alt</kbd>+<kbd>[number]</kbd></dd>
    <dt>Execute (Sublime)</dt>
    <dd><kbd>F5</kbd></dd>
</dl>

## Shell and Scripting

A little bit of knowledge of a shell is helpful. For Linux, the most common
shell is called bash. Knowing some command line tools and how to execute them
in simple shell scripts is pretty powerful.

Here are some of the basic commands, roughly in the order how often I need them:

<dl>
    <dt>Change Directory</dt>
    <dd><code>cd [relative or absolute path]</code></dd>
    <dt>Find within a file</dt>
    <dd><code>grep</code></dd>
    <dt>Look up what you execute in the past</dt>
    <dd><code>history</code></dd>
    <dt>List files/directories</dt>
    <dd><code>ls</code></dd>
    <dt>Open a file</dt>
    <dd><code>xdg-open</code></dd>
    <dt>Move a file</dt>
    <dd><code>mv origin destination</code></dd>
    <dt>Copy a file</dt>
    <dd><code>cp origin destination</code></dd>
    <dt>Delete a file</dt>
    <dd><code>rm filepath</code></dd>
    <dt>Disk usage</dt>
    <dd><code>df -h</code> and <code>ncdu</code> (<a href="https://dev.yorhel.nl/ncdu">website</a>)</dd>
    <dt>Running processes</dt>
    <dd><code>top</code> and <code>htop</code></dd>
    <dt>Repetedly execute something</dt>
    <dd><code>watch</code></dd>
    <dt>Show content of a text file</dt>
    <dd><code>cat</code>, <code>head</code>, <code>tail</code></dd>
    <dt>Word / line / character counts</dt>
    <dd><code>wc</code></dd>
    <dt>Locating files</dt>
    <dd><code>locate</code>, <code>find</code></dd>
    <dt>Read the manual</dt>
    <dd><code>man</code></dd>
    <dt>Print working Directory</dt>
    <dd><code>pwd</code></dd>
</dl>

And some things you have to install

<dl>
    <dt>Show differences between text files</dt>
    <dd><code>meld file1 file2</code> (<a href="http://meldmerge.org/">website</a>)</dd>
    <dt>Download a webpage</dt>
    <dd><code>curl</code> or <code>wget</code> or <code>httpie</code> (<a href="https://httpie.org/">website</a>)</dd>
    <dt>Manipulate JSON files</dt>
    <dd><code>jq</code> (<a href="https://stedolan.github.io/jq/">website</a>)</dd>
    <dt>Environment Variable Loading / Unloading</dt>
    <dd><a href="https://direnv.net/">direnv</a></dd>
</dl>

`vim` and its various plugins like NERDTree and Powerline are a completely
seperate topic.

See also:

* [ZSH and Oh-My-ZSH](https://martin-thoma.com/working-terminal/)
* [Linux Commands for Working from home](https://martin-thoma.com/linux-commands-for-working-from-home/)

## Screen automation

Some times tools don't come with the necessary interfaces to automate things.
The simplest example are IDLE games like [Cookie Clicker](http://orteil.dashnet.org/cookieclicker/).
In this case you just have to click. Fast. All the time.

So what you can use is [`xdotool`](https://www.semicomplete.com/projects/xdotool/).

First, navigate to where you want to click. Leave your cursor there and execute
`xdotool getmouselocation`. Once you know the location, you can move there with
`xdotool mousemove 100 200` and execute a left click with `xdotool click 1`.

So a script for this could be:

```bash
#!/bin/bash
for i in {1..500}; do
  xdotool click 1 &
  sleep 0.001
  echo $i
done
```
