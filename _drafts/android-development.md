---
layout: post
title: Android Development
author: Martin Thoma
date: 2013-03-12 11:52:10
categories: 
- Code
tags: 
- Android
- Software Development
featured_image: 2013/03/android-thumb.png
---
<div class="info">The following article was tested in Linux Mint 14 Nadia (based on Ubuntu 12.10).</div>

<h2>Installation</h2>
<h3>Android Virtual Device Manager</h3>
[bash]sudo apt-get install openjdk-7-jre openjdk-7-jdk icedtea-7-plugin eclipse[/bash]

Download Android SDK:
[bash]wget http://dl.google.com/android/android-sdk_r21.1-linux.tgz[/bash]

Extract it:
[bash]tar -xvzf android-sdk_r21.1-linux.tgz[/bash]

[bash]cd android-sdk-linux/tools/
./android[/bash]

Open <code>~/.bashrc</code> for editing and add:

[text]export PATH=${PATH}:~/android-sdk-linux/tools
export PATH=${PATH}:~/android-sdk-linux/platform-tools[/text]

Now you can start Android Virtual Device Manager with this command:
[bash]android avd[/bash]

<h3>Eclipse ADT-Plugin</h3>
Here is a good explanation <a href="http://developer.android.com/sdk/installing/installing-adt.html">how to install the Eclipse ADT plugin</a>.

<h2>Start developing</h2>
Try the tutorial "<a href="http://developer.android.com/training/basics/firstapp/index.html">Building Your First App</a>". It's good and simple.