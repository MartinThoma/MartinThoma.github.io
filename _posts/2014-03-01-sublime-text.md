---
layout: post
title: Sublime Text
author: Martin Thoma
date: 2014-03-01 17:01
categories:
- Code
tags:
- Editor
- Sublime Text
featured_image: logos/sublime-text.png
---
Sublime Text is the coolest editor I have ever used. It has a lot of features,
is blazingly fast as I expect it from every editor and has a convenient configuration.
It is available for Linux, Windows and Mac. You can use it for free without any
restrictions as long as you want. But keep in mind that somebody had to develop
this nice software.

## Installation
You can get a free version from [sublimetext.com](http://www.sublimetext.com/)
or you could install it on Linux Mint via

```bash
sudo apt-get install sublime-text
```

I've added a symlink to make it easier to call it from command line:

```bash
sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/sublime
```

The editor is usable right after the installation, but you might want to make 
some fine-tuning.

## Configuration
Sublime Text offers plenty of configuration options. You can apply them to projects, users or system wide. Most of the time, I change my preferences for me via Preferences > Settings - User:

{% caption align="aligncenter" width="500" alt="Preferences > Settings - User" text="Preferences > Settings - User" url="../images/2014/03/sublime-user-preferences.png" %}

Here is what I have changed:

```text
{
	"color_scheme": "Packages/User/textmate (SL).tmTheme",
	"draw_white_space": "all",
	"fold_buttons": true,
	"font_face": "Ubuntu Mono",
	"font_size": 13,
	"highlight_line": true,
	"ignored_packages":
	[
		"Vintage"
	],
	"rulers":
	[
		80,
		120
	],
	"tab_size": 4,
	"translate_tabs_to_spaces": false,
	"use_tab_stops": false
}
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

### Bracket Highlighter
[BracketHighlighter](https://github.com/facelessuser/BracketHighlighter) adds
brackets on the left side. It looks like this:

{% caption align="aligncenter" width="500" alt="Highlight braces" text="Highlight braces" url="../images/2014/03/sublime-braces.png" %}

### Alignment
[Sublime Alignment](http://wbond.net/sublime_packages/alignment) gives you the
possibility to mark text, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>a</kbd> to
align:

{% caption align="aligncenter" width="500" alt="automatical alignment" text="automatical alignment" url="../images/2014/03/sublime-align.gif" %}

## Themes
First of all, make sure you have installed the `Colorsublime` package.
After you have it, you can press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
and enter "Install Theme". Then it contacts the server and provides you a list
of many good themes. You can go through them with the arrow keys and they will
instantly be applied!

I really like the "Textmate" theme, but the "Chrome_DevTools" theme is also good.

## Custom Keybindings

You can create custom keybindings via *Preferences Key Bindings (User)*

I have these:

```text
[
{ "keys": ["ctrl+shift+r"], "command": "reindent", "args": { "single_line": false } },
{ "keys": ["shift+tab"], "command": "unindent", "args": {"single_line":true} },
{ "keys": ["ctrl+7"], "command": "toggle_comment", "args": { "block": false } },
{ "keys": ["ctrl+shift+7"], "command": "toggle_comment", "args": { "block": true } }
]
```

## Buildin Keybindings

<kbd>Ctrl</kbd> + <kbd>p</kbd>: Goto file

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>: Goto anything


<kbd>Ctrl</kbd> + <kbd>r</kbd>: Goto section

{% caption align="aligncenter" width="500" alt="Ctrl+R in Sublime Text" text="Ctrl+R in Sublime Text (LaTeX)" url="../images/2014/03/sublime-latextools-jump-ctrl-r.png" %}
{% caption align="aligncenter" width="500" alt="Ctrl+R in Sublime Text" text="Ctrl+R in Sublime Text (Markdown)" url="../images/2014/03/sublime-jump-markdown-ctrl-r.png" %}

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Up / Down</kbd>: Move the current line one line up / down

<kbd>Shift</kbd> + <kbd>F11</kbd>: Distraction free mode

{% caption align="aligncenter" width="500" alt="Distraction free mode" text="Distraction free mode" url="../images/2014/03/sublime-text-distraction-free.png" %}

<kbd>Ctrl</kbd> + <kbd>D</kbd>: Multi-Select



## What could be better
### Chrome-like Tabs
Look at this:

{% caption align="aligncenter" width="500" alt="Sublime Tabs" text="Sublime Tabs" url="../images/2014/03/sublime-text-tabs.png" %}

Now compare it to this:

{% caption align="aligncenter" width="500" alt="Chrome Tabs" text="Chrome Tabs" url="../images/2014/03/chrome-tabs.png" %}

Chrome tabs look much cleaner, don't they? Many others seem to think that, too ([source](http://sublimetext.userecho.com/topic/19361-move-tabs-to-the-title-bar-like-in-google-chrome/)).

### Line Wrapping
Sublime Text 3 does wrap points and commas to the next line:

{% caption align="aligncenter" width="500" alt="line wrapping" text="line wrapping" url="../images/2014/03/sublime-word-wrapping.png" %}

This behaviour is bad and not liked by the community ([source](http://www.sublimetext.com/forum/viewtopic.php?f=3&t=5214)).


## More
* [Documentation](https://www.sublimetext.com/docs/3/)
* [colorsublime.com](http://colorsublime.com/): Lots of themes
* [tmtheme-editor.herokuapp.com](http://tmtheme-editor.herokuapp.com/#/theme/Chrome%20DevTools): Adjust your theme online