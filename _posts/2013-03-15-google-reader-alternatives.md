---
layout: post
title: Google Reader Alternatives
author: Martin Thoma
date: 2013-03-15 23:09:04.000000000 +01:00
categories:
- The Web
tags:
- Google
- RSS
featured_image: 2013/03/google-reader-logo.png
---
On July 1, 2013, Google will retire Google Reader (<a href="http://googleblog.blogspot.de/2013/03/a-second-spring-of-cleaning.html">source</a>). A first step should be to save your data (especially your subscriptions). You can do that with <a href="https://www.google.com/takeout">Google Takeout</a>. You could also sign a <a href="https://www.change.org/petitions/google-keep-google-reader-running">petition against closing Google Reader</a>, but I doubt that this will have any effect. Currently, 106,712 people support this petition, though.

<h2>How I used Google Reader</h2>
Most important for me was the Chrome plugin:

[gallery columns="2" size="medium" ids="61401,61391"]

The website offered a nice, clean way to administrate my 109 Feeds. Last (and least) the Android App. I don't have my smartphone long enough to really use this app, but it is one of 10 Apps I've currently installed.

[gallery columns="2" size="medium" ids="61421,61411"]

Now, I am interested in alternatives. They should
<ul>
  <li>allow me to import my subscriptions,</li>
  <li>have a Google Chrome Extension (in <a href="https://chrome.google.com/webstore?utm_source=chrome-ntp-icon">Chrome Web Store</a>)</li>
  <li>have an Android App (in <a href="https://play.google.com/store">Android Market</a>)</li>
  <li>have export options</li>
  <li>sync my feeds, as I would like to read my feeds on several computers and my smartphone</li>
  <li>allow me to login via Google OpenID</li>
</ul>

<h2>Web Services</h2>
<h3>The Old Reader</h3>
<a href="http://theoldreader.com/">The Old Reader</a> is a web service that wants to provide the same service as Google did before.

{% caption align="aligncenter" width="300" caption="The Old Reader" url="../images/2013/03/theoldreader.com-feeds-import-300x175.png" alt="The Old Reader"  height="175" class="size-medium wp-image-61231" %}

Looks pretty good, doesn't it? But it currently displays the message "There are 27283 users in the import queue ahead of you."

<h3>BazQux Reader</h3>
<a href="http://bazqux.com/">BazQux Reader</a> seemed to be a real alternative. It allowed me to sign in with Google, import my subscriptions and it looked familiar:

{% caption align="aligncenter" width="300" caption="BazQux Reader" url="../images/2013/03/bazqux.com_-300x222.png" alt="BazQux Reader"  height="222" class="size-medium wp-image-61261" %}

Another point for BazQux: It supports OPML-Export (Click on the icon at the top right corner &rarr; Subscriptions &rarr; Export OPML)

But now the drawbacks:
<ul>
  <li>9 $/year</li>
  <li>no Chrome plugin</li>
  <li>no Android App</li>
</ul>

<h3>Bloglovin'</h3>
<div class="warning">Bloglovin sends you emails with your feeds. Those emails don't have an unsubscribe link.</div>

<a href="http://www.bloglovin.com/">Bloglovin'</a> is another WebService that looks very nice and is free, seems to be a real alternative. While importing my subscriptions, I got a 504 Gateway Time-out, but it imported my feeds anyway.

{% caption align="aligncenter" width="300" caption="bloglovin" url="../images/2013/03/bloglovin-300x210.png" alt="bloglovin"  height="210" class="size-medium wp-image-61271" %}

The service seems to be free, they have an <a href="https://play.google.com/store/apps/details?id=se.yo.android.bloglovin">Android App</a> and an <a href="https://itunes.apple.com/app/bloglovin/id421818340?mt=8">iPhone App</a>, but no Google Chrome App and I can't sign in with Google.

Bloglovin' does not provide an export function.

<h3>Good Noows</h3>
It seems to get better. <a href="http://goodnoows.com/">Good Noows</a> lets me sign in with Google, offers an import function and has a <a href="https://chrome.google.com/webstore/detail/good-noows/deegloljmdbfbjhlimieancmcfombgjj?utm_source=chrome-ntp-icon">Chrome App</a>. I seems to be free.

{% caption align="aligncenter" width="300" caption="Good Noows" url="../images/2013/03/goodnoows-300x183.png" alt="Good Noows"  height="183" class="size-medium wp-image-61291" %}

However, it has no Android App and seems not to support export.

<h3>Bloglines</h3>
<a href="http://www.bloglines.com/index.html">Bloglines</a> offers an export function! I can't login with Google, but I can import my 109 Feeds. 

It looks like this:
<a href="../images/2013/03/bloglines.png"><img src="../images/2013/03/bloglines-300x184.png" alt="bloglines" width="300" height="184" class="aligncenter size-medium wp-image-61351" /></a>

It has no Chrome App and the <a href="https://play.google.com/store/apps/details?id=org.nyquil.rss2bloglines&feature=search_result#?t=W251bGwsMSwyLDEsIm9yZy5ueXF1aWwucnNzMmJsb2dsaW5lcyJd">Android App</a> is possibly not official.

<h2>Host yourself</h2>
<h3>Selfoss</h3>
<a href="http://selfoss.aditu.de/">Selfoss</a> gives you the possibility to host your RSS-Aggregator by yourself. It looks quite good, requires only PHP 5.3 and MySQL and mobiles are supported.

{% caption align="aligncenter" width="300" caption="Screenshot of selfoss" url="../images/2013/03/selfoss-300x203.png" alt="Screenshot of selfoss"  height="203" class="size-medium wp-image-68361" %}

<ul>
  <li>Selfoss: <a href="https://github.com/SSilence/selfoss">GitHub</a>, <a href="http://selfoss.aditu.de/">Download</a></li>
</ul>

<h3>Tiny Tiny RSS</h3>
<a href="http://tt-rss.org/redmine/projects/tt-rss/wiki">TT-RSS</a> allows you to host a service similar to Google Reader. This could be an interesting alternative, but currently the demo page is disabled. I'm waiting for reviews of this one.

<ul>
  <li>Tiny Tiny RSS: <a href="https://github.com/gothfox/Tiny-Tiny-RSS">GitHub</a>, <a href="http://tt-rss.org/redmine/projects/tt-rss-android/issues">Issue Tracker</a>, <a href="http://tt-rss.org/redmine/projects/tt-rss/wiki#Download">Download</a>, <a href="https://www.softaculous.com/demos/Tiny_Tiny_RSS">Demo</a></li>
  <li>Android Client: <a href="https://play.google.com/store/apps/details?id=org.fox.ttrss&feature=search_result">Market</a></li>
</ul>

<h2>Tried, but no alternative</h2>
<ul>
  <li><a href="https://www.pulse.me/">Pulse</a>: Where can I add RSS-Feeds in this service?</li>
  <li><a href="http://www.feedafever.com/#account">FeedAFever</a>: Why should I pay for this, when there are free services?</li>
  <li><a href="http://blog.feedly.com/2013/03/14/google-reader/">Feedly</a>: What is this? Is it a Web service? Is it a standalone software? Do I have to host it myself?</li>
  <li><a href="http://hivemined.org/#wut">Hivemined</a>: Not ready yet</li>
  <li><a href="http://www.newsblur.com/">NewsBlur</a>: I could not sign in.</li>
  <li><a href="https://www.rolio.com/">Rolio.com</a>: No import</li>
</ul>

<h2>More alternatives</h2>
Here is <a href="http://www.anoxa.de/blog2/?p=16012">an article</a> that lists lots of alternatives.

<h2>A short survey</h2>
I'm interested in your experiences. Would you please participate in this five minute survey?

<iframe src="https://docs.google.com/forms/d/1m7-dKZkKGKQrn3fhejKAxMAw-rWjTR8t1hdE3-zZr-8/viewform?embedded=true" width="512" height="500" frameborder="0" marginheight="0" marginwidth="0">Wird geladen...</iframe>
