---
layout: post
title: A classical, system-independant theme management
author: Martin Thoma
date: 2012-12-19 12:49:47
categories: 
- Cyberculture
tags: 
- Linux
- Windows
- XML
featured_image: 
---
I just had the problem, that I wanted to customize my theme in Windows, but I didn't know how to do it in Windows. I stumbled over <a href="http://www.addictivetips.com/windows-tips/on-screen-volume-control-indicator-for-windows/">3RVX</a>.

My idea is to create an open format that can be read by any system so that a theme reader can be implemented on every system.

It could be included into a zip-archive:

myTheme.zip
<ul>
  <li>/theme.xml</li>
  <li>/icons/ - A 16x16, 32x32 of
    <ul>
      <li>Folders</li>
      <li>Text files</li>
      <li>Archives</li>
      <li>Temporary files</li>
      <li>PDF documents</li>
      <li>Executable binaries</li>
      <li>Python files</li>
      <li>HTML files</li>
      <li>C source files</li>
      <li>C header files</li>
    </ul>
  </li>
  <li>/wallpapers/ a 1366x768 version should be there</li>
  <li>/misc/</li>
</ul>

A complete theme has