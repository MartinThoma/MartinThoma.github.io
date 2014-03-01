---
layout: post
title: Sublime Text
author: Martin Thoma
date: 2014-03-01
categories:
- Code
tags:
- Editor
- Sublime Text
featured_image: /home/moose/Downloads/MartinThoma.github.io/images/logos/sublime-text.png
---
Sublime Text is the coolest editor I have ever used.

## Configuration
Sublime Text offers plenty of configuration options. You can apply them to projects, users or system wide. Most of the time, I change my preferences for me via Preferences > Settings - User:

{% caption align="aligncenter" width="500" alt="Preferences > Settings - User" text="Preferences > Settings - User" url="../images/2014/03/sublime-user-preferences.png" %}

Here is what I have changed:

```text
// Adds two vertical rulers: one at line 80 and one at line 120
"rulers": [80, 120],
```

## Plugins
### Package Control
The [`Package Control`](https://sublime.wbond.net/) plugin should definitely be installed. It makes installation of other packages so much easier. After you have installed it, you can press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>
to get this dialog:

{% caption align="aligncenter" width="500" alt="Sublime Tabs" text="Sublime Tabs" url="../images/2014/03/sublime-package-control-install.png" %}

### LaTeXTools
The [LaTeXTools](https://github.com/SublimeText/LaTeXTools) package adds support
for LaTeX. It adds shortcuts, a pulldown menu when you enter `\cref{` and much 
more.

## Themes
First of all, make sure you have installed the `Colorsublime` package.
After you have it, you can press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
and enter "Install Theme". Then it contacts the server and provides you a list
of many good themes. You can go through them with the arrow keys and they will
instantly be applied!

I really like the "Textmate" theme, but the "Chrome_DevTools" theme is also good.

## Shortcuts

<kbd>Ctrl</kbd> + <kbd>r</kbd>

{% caption align="aligncenter" width="500" alt="Ctrl+R in Sublime Text" text="Ctrl+R in Sublime Text (LaTeX)" url="../images/2014/03/sublime-latextools-jump-ctrl-r.png" %}
{% caption align="aligncenter" width="500" alt="Ctrl+R in Sublime Text" text="Ctrl+R in Sublime Text (Markdown)" url="../images/2014/03/sublime-jump-markdown-ctrl-r.png" %}

## What could be better
### Chrome-like Tabs
Look at this:

{% caption align="aligncenter" width="500" alt="Sublime Tabs" text="Sublime Tabs" url="../images/2014/03/sublime-text-tabs.png" %}

Now compare it to this:

{% caption align="aligncenter" width="500" alt="Chrome Tabs" text="Chrome Tabs" url="../images/2014/03/chrome-tabs.png" %}

Chrome tabs look much cleaner, don't they? Many others seem to think that, too ([source](http://sublimetext.userecho.com/topic/19361-move-tabs-to-the-title-bar-like-in-google-chrome/)).

## More
* [colorsublime.com](http://colorsublime.com/): Lots of themes
* [tmtheme-editor.herokuapp.com](http://tmtheme-editor.herokuapp.com/#/theme/Chrome%20DevTools): Adjust your theme online