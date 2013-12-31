---
layout: post
title: Install PyPy on Ubuntu
author: Martin Thoma
date: 2012-07-16 10:22:48
categories: 
- Code
tags: 
- Python
- Ubuntu
featured_image: 2011/09/Ubuntu-Logo.png
---
If you want to install a package on a Ubuntu machine, you should check the following (in this order):
<ul>
  <li>Is the package in the repository? - <code>apt-cache search pypy</code></li>
  <li>Does a PPA exist? - just <a href="google.com/?q=ppa+pypy">Google it</a> - yes, <a href="https://launchpad.net/~pypy/+archive/ppa">they have a PPA</a>.</li>
  <li><a href="http://pypy.org/download.html#building-from-source">Compile it yourself</a>.</li>
</ul>

If the version in the repository is to old (that's too often the case :-( ) and the project has no PPA, you might have to compile it yourself. Most of the time, this is very simple. Just <code>./configure</code>, then <code>make</code> and <code>make install</code>. I will not explain this as I want to focus on installing a PPA.

First, you need the name. It is on the page of the PPA in this box:
[caption id="attachment_32781" align="alignnone" width="510"]<a href="http://martin-thoma.com/wp-content/uploads/2012/07/Adding-this-PPA.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/07/Adding-this-PPA.png" alt="Adding-this-PPA" title="Adding-this-PPA" width="510" height="147" class="size-full wp-image-32781" /></a> ppa:pypy/ppa is what you need[/caption]

Then you have to go to the terminal and enter:
[bash]sudo add-apt-repository ppa:pypy/ppa[/bash]

You might see something like:
[bash]Executing: gpg --ignore-time-conflict --no-options --no-default-keyring --secret-keyring /etc/apt/secring.gpg --trustdb-name /etc/apt/trustdb.gpg --keyring /etc/apt/trusted.gpg --primary-keyring /etc/apt/trusted.gpg --keyserver keyserver.ubuntu.com --recv 2862D0785AFACD8C65B23DB0251104D968854915
gpg: requesting key 68854915 from hkp server keyserver.ubuntu.com
gpg: key 68854915: public key &quot;Launchpad pypy-1.2&quot; imported
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)[/bash]

Then you execute these commands:
[bash]sudo apt-get update
sudo apt-get install pypy[/bash]

That's it. Easy, isn't it? (Easy as Py :D )

The version seems to be quite old. The current one is 1.9 (see <a href="http://en.wikipedia.org/wiki/PyPy">Wiki</a>).
[bash]moose@pc07:~$ pypy --version
Python 2.5.2 (75347, Jul 02 2010, 01:38:39)
[PyPy 1.3.0][/bash]


<h2>See also</h2>
<ul>
  <li><a href="http://wiki.ubuntuusers.de/Launchpad/PPA">How to make your own PPA</a> (German)</li>
  <li><a href="http://wiki.ubuntuusers.de/Paketquellen_freischalten/PPA">Paketquellen freischalten</a> (German)</li>
</ul>

iron python ubuntu