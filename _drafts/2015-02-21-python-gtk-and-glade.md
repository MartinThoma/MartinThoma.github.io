---
layout: post
title: Python, GTK and Glade
author: Martin Thoma
date: 2014-11-22 17:19
categories: 
- Code
tags: 
- Python
- GTK
- Glade
- GUI
featured_image: logos/Python.png
---
GUI development is a completely new skill, independent of other programming
skills. You have to know how the GUI library (GTK) works, know the tools to
create graphical user interfaces (Glade) and, of course, know how to use it
with your programming language (Python). In this article, I want to give some
hints how to start.

You should try the [Python GTK3 Tutorial](http://python-gtk-3-tutorial.readthedocs.org/en/latest/index.html). But please note that it is written for Python 3!

## Installation

For Debian systems, the following should work:

```bash
$ sudo apt-get install python3 gobject-introspection glade libgtk-3-dev
```

Try to execute the following:

```python
#!/usr/bin/env python3
from gi.repository import Gtk

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
```

If this works, the installation went fine. If not, you should ask for help
(and paste the error to the person you ask for help!).



## See also

* [GTK+ 3 Reference Manual](https://developer.gnome.org/gtk3/stable/)
* [Sublime Text 3 with Python 3](https://coderwall.com/p/nhq2gg/setting-up-sublimerepl-with-python3)
* [Python GI API Reference](http://lazka.github.io/pgi-docs/index.html#Gtk-3.0)

http://www.pygtk.org/articles/pygtk-glade-gui/Creating_a_GUI_using_PyGTK_and_Glade.htm

