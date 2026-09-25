---
layout: post
title: Configurig gEdit for developers
slug: configurig-gedit-for-developers
lang: en
author: Martin Thoma
date: 2011-12-08 23:10:19.000000000 +01:00
category: Cyberculture
tags: gedit, Editor, Linux
featured_image: 2011/12/gedit.png
---
<a href="http://en.wikipedia.org/wiki/Gedit">gedit</a> is a very lightweight text editor. It supports syntax highlighting for every programming language I can think of and is highly customizable.

It belongs to GNOME, but it is also available for Windows. This is how it looks like:

<figure>
    <a href="../images/2011/12/gedit-screenshot-300x208.png"><img src="../images/2011/12/gedit-screenshot-300x208.png" alt="gedit screenshot" width="300" height="208"></a>
    <figcaption>gedit screenshot</figcaption>
</figure>

You might want to install gedit-plugins:
```bash
sudo apt-get install gedit-plugins
```

<h2>External Tools</h2>
gedit allows you to run external command line tools by pressing shortcuts. You can find the external tools plugins in your preferences:
<figure>
    <a href="../images/2011/12/gedit-external-tools1-300x209.png"><img src="../images/2011/12/gedit-external-tools1-300x209.png" alt="gedit external tools" width="300" height="209" loading="lazy"></a>
    <figcaption>gedit external tools</figcaption>
</figure>

You can assign shortcuts by clicking into an input field and simply using the shortcut once:
<figure>
    <a href="../images/2011/12/external-tool-java-300x209.png"><img src="../images/2011/12/external-tool-java-300x209.png" alt="external tools java" width="300" height="209" loading="lazy"></a>
    <figcaption>external tools java</figcaption>
</figure>

<h3>Java</h3>
```bash
#!/bin/sh
cd $GEDIT_CURRENT_DOCUMENT_DIR
if javac $GEDIT_CURRENT_DOCUMENT_NAME;
then
java ${GEDIT_CURRENT_DOCUMENT_NAME%\.java}
else
echo "Failed to compile"
fi
```

<h2>Code Comment</h2>
This neat little plugin detects which programming language you are using. If you select a code block and press ctrl+m it gets marked as a comment. If you press ctrl+shift+m a block of comments gets "decommented" to a block of code. It uses # for Python and // for Java.

<h2>Bracket Completion</h2>
Well, I guess the name is meaningful, isn't it? As soon as you type a bracket - (, [ or { it gets completed with }, ] or ).

<h2>Better Python Console</h2>
The <a href="http://live.gnome.org/Gedit/Plugins/BetterPythonConsole">Better Python Console Plugin</a> allows you to press F5 and execute the current code in an interactive Python console. This means, you can access the current variables!

You install it by extracting and copying the whole folder (with plugins!) to ~/gnome2/gedit.

<h2>What could be better</h2>
The design could be similar to Chrome ☺ So they could have some nicer tabs. Nothing really important.

I really miss comment folding since I have to write Java code with a lot of Doc comments

<h2>Further reading and resources</h2>
<ul>
    <li><a href="http://projects.gnome.org/gedit/">Official Website</a>: You can find the Windows Binary here.</li>
    <li><a href="http://live.gnome.org/Gedit/ExternalToolsPluginCommands">External Tools</a></li>
    <li><a href="http://www.makeuseof.com/tag/top-plugins-to-extend-and-make-gedit-a-more-useful-text-editor-linux/">13 Gedit Plugins to Make It a More Useful Text Editor</a>: Seems as if you could also have a class browser in gedit</li>
</ul>
