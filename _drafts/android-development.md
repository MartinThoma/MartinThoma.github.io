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
{% highlight bash %}sudo apt-get install openjdk-7-jre openjdk-7-jdk icedtea-7-plugin eclipse{% endhighlight %}

Download Android SDK:
{% highlight bash %}wget http://dl.google.com/android/android-sdk_r21.1-linux.tgz{% endhighlight %}

Extract it:
{% highlight bash %}tar -xvzf android-sdk_r21.1-linux.tgz{% endhighlight %}

{% highlight bash %}cd android-sdk-linux/tools/
./android{% endhighlight %}

Open <code>~/.bashrc</code> for editing and add:

{% highlight text %}export PATH=${PATH}:~/android-sdk-linux/tools
export PATH=${PATH}:~/android-sdk-linux/platform-tools{% endhighlight %}

Now you can start Android Virtual Device Manager with this command:
{% highlight bash %}android avd{% endhighlight %}

<h3>Eclipse ADT-Plugin</h3>
Here is a good explanation <a href="http://developer.android.com/sdk/installing/installing-adt.html">how to install the Eclipse ADT plugin</a>.

<h2>Start developing</h2>
Try the tutorial "<a href="http://developer.android.com/training/basics/firstapp/index.html">Building Your First App</a>". It's good and simple.