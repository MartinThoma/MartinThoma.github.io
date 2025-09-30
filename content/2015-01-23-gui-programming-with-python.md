---
layout: post
lang: en
title: GUI programming with Python
slug: gui-programming-with-python
author: Martin Thoma
date: 2015-01-23 14:39
category: Code
tags: Python, GTK, Qt, tkinter
featured_image: logos/gui-programming.png
---
A graphical user interface (GUI) is essential for applications which should be
used by standard computer users (non-developers, not computer scientists, ...).
However, I have almost no experience with GUI development outside of the web.

Multiple GUI toolkits exist and the only one I have ever used is
[Tk](https://en.wikipedia.org/wiki/Tk_(software)) for a very, very simple GUI.

In this article, I want to share some of my thoughts about GUI development with
Python as a beginner. I might update this in future.


## GUI toolkits

> A widget toolkit, widget library, GUI toolkit, or UX library is a library or
> a collection of libraries containing a set of graphical control elements
> (called widgets) used to construct the graphical user interface (GUI) of
> programs.

Source: [Widget toolkit](https://en.wikipedia.org/wiki/Widget_toolkit)


## Comparison

I am only interested in GUI toolkits

* which work on Ubuntu 12.04+,
* which have a Python binding,
* which are OpenSource and have a good license,
* which are used by others (and hence have enough documentation and examples)

It seems to me that only the following four toolkits fulfill these requirements:
GTK, Qt, Tk, wxWidgets. Some of these have multiple Python bindings and all
have multiple GUI builders / designers. I tried to find the most commonly used
one. Please let me know if I should add something, replace something:

<style>
    .data-table {
        border-collapse: collapse;
    }
    .border-bottom {
        border-bottom: 1px solid #000;
    }
    .border-right {
        border-right: 1px solid #000;
    }
</style>

<table class="data-table">
    <tr>
        <th class="border-bottom border-right">Name</th>
        <th class="border-bottom"><a href="https://en.wikipedia.org/wiki/GTK%2B">GTK+</a></th>
        <th class="border-bottom"><a href="https://en.wikipedia.org/wiki/Qt_(software)">Qt</a></th>
        <th class="border-bottom"><a href="https://en.wikipedia.org/wiki/Tk_(software)">Tk</a></th>
        <th class="border-bottom"><a href="https://en.wikipedia.org/wiki/WxWidgets">wxWidgets</a></th>
    </tr>
    <tr>
        <th class="border-right">Latest version (23.01.2015)</th>
        <td>3.14.1</td>
        <td>5.4.0</td>
        <td>8.6.3</td>
        <td>3.0.2</td>
    </tr>
    <tr>
        <th class="border-right">Official Website</th>
        <td><a href="http://www.gtk.org/">gtk.org</a></td>
        <td><a href="https://qt-project.org/">qt-project.org</a></td>
        <td><a href="http://www.tcl.tk/">tcl.tk</a></td>
        <td><a href="http://wxwidgets.org/">wxwidgets.org</a></td>
    </tr>
    <tr>
        <th class="border-right">Initial release</th>
        <td>1998</td>
        <td>1995</td>
        <td>1991</td>
        <td>1992</td>
    </tr>
    <tr>
        <th class="border-right">Written in</th>
        <td>C</td>
        <td>C++</td>
        <td>C</td>
        <td>C++</td>
    </tr>
    <tr>
        <th class="border-right">Documentation</th>
        <td><a href="http://www.gtk.org/documentation.php">gtk.org/documentation.php</a></td>
        <td><a href="http://doc.qt.io/">doc.qt.io</a></td>
        <td><a href="http://www.tkdocs.com/">tkdocs.com</a></td>
        <td><a href="http://wxwidgets.org/docs/">wxwidgets.org/docs</a></td>
    </tr>
    <tr>
        <th class="border-right">Tutorial</th>
        <td><a href="https://developer.gnome.org/gtk-tutorial/stable/">developer.gnome.org/gtk-tutorial/stable</a></td>
        <td><a href="http://qt-project.org/doc/qt-4.8/tutorials.html">qt-project.org/doc/qt-4.8/tutorials.html</a></td>
        <td><a href="http://www.tkdocs.com/tutorial/index.html">tkdocs.com/tutorial</a></td>
        <td><a href="https://www.wxwidgets.org/docs/tutorials/">wxwidgets.org/docs/tutorials</a></td>
    </tr>
    <tr>
        <th class="border-right">StackOverflow questions</th>
        <td>4,715</td>
        <td>37,626</td>
        <td>929</td>
        <td>1,918</td>
    </tr>
    <tr>
        <td class="border-right">StackOverflow unanswered</td>
        <td>1,159</td>
        <td>9,704</td>
        <td>208</td>
        <td>429</td>
    </tr>
    <tr>
        <th class="border-right">License</th>
        <td>LGPL 2.1&nbsp;</td>
        <td>LGLP 3.0 (mutliple</td>
        <td>BSD-style</td>
        <td>wxWindows License</td>
    </tr>
    <tr>
        <th class="border-right">Python binding</th>
        <td>PyGTK (<a href="http://www.pygtk.org/pygtk2reference/">docs</a>)</td>
        <td>PySide (<a href="http://qt-project.org/wiki/PySide">docs</a>), PyQt</td>
        <td>Tkinter (<a href="https://docs.python.org/3/library/tkinter.html">docs</a>)</td>
        <td>wxPython (<a href="http://www.wxpython.org/">docs</a>)</td>
    </tr>
    <tr>
        <th class="border-right">Python 3 support</th>
        <td>yes</td>
        <td>yes</td>
        <td>yes?</td>
        <td>yes</td>
    </tr>
    <tr>
        <th class="border-right">Designer</th>
        <td>Glade Interface Designer</td>
        <td>QtDesigner, QtCreator, QDevelop, Edyuk</td>
        <td>SpecTcl</td>
        <td>wxGlade</td>
    </tr>
    <tr>
        <th class="border-right">Famous applications</th>
        <td>Gnome applications like Inkscape, <a href="https://github.com/elbersb/otr-verwaltung">OTR-Verwaltung</a></td><!-- GTK-->
        <td>vlc, Virtual Box, KDE applications like K3B, <a href="https://github.com/dae/anki">Anki</a></td><!-- Qt-->
        <td>I could not find any</td><!-- Tk-->
        <td>Code::Blocks<br/>FileZilla<br/>0 A.D.</td><!-- wxwidgets-->
    </tr>
</table>

There are also some applications which use custom UI toolkits:

* [Sublime Text](https://news.ycombinator.com/item?id=2822114)
* [Firefox](https://en.wikipedia.org/wiki/Firefox)
* [LibreOffice](http://ask.libreoffice.org/en/question/81/which-gui-toolkit-is-used-by-lo/)


## See also

* [List of widget toolkits](https://en.wikipedia.org/wiki/List_of_widget_toolkits)
* [Graphical user interface builder](https://en.wikipedia.org/wiki/Graphical_user_interface_builder)
* [The Python GTK+ 3 Tutorial](https://python-gtk-3-tutorial.readthedocs.org/en/latest/)
* [Why are Tk GUI's considered ugly?](http://stackoverflow.com/q/349409/562769)
* [wxPython vs PyQt vs PyGTK: when and what to use?](http://stackoverflow.com/q/19584076/562769)
* [What's the difference between GTK and QT?](http://askubuntu.com/q/85144)

Qt-specific

* [Differences Between PySide and PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt)
* [Should I use PyQt or PySide for a new Qt project?](http://askubuntu.com/q/140740/10425)
* [PyQt or PySide - which one to use](http://stackoverflow.com/q/6888750/562769)
* [Developing Cross Platform Application using Qt, PyQt and PySide : Introduction - Part 1 of 5](http://pythonthusiast.pythonblogs.com/230_pythonthusiast/archive/1348_developing_cross_platform_application_using_qt_pyqt_and_pyside__introduction-part_1_of_5.html)
