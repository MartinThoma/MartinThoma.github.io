---
layout: post
lang: en
title: 5 Web Technologies which should be used more often
slug: 5-web-technologies-which-should-be-used-more-often
author: Martin Thoma
date: 2011-10-08 06:21:25.000000000 +02:00
category: The Web
tags: Web Development, OpenID, RSS
featured_image: 2011/10/OpenID.png
---
<figure class="alignright">
            <a href="../images/2011/10/RSS-Feeds.png"><img src="../images/2011/10/RSS-Feeds.png" alt="RSS-Feeds" style="max-width:100px;max-height:100px;" class="size-full wp-image-4411"/></a>
            <figcaption class="text-center">RSS-Feeds</figcaption>
        </figure>


## RSS-Feeds
Everyone who wants to get informed about updates on websites has to use RSS Feeds. Every time any website you have in your Feed Reader makes an update, you can get instantly a little notice. Its a bit like e-mail, but you have the possibility to stop this service. You can't get spam, as the Feed owner doesn't get an identifier for you.

<figure class="alignright">
            <a href="../images/2011/10/OpenID.png"><img src="../images/2011/10/OpenID.png" alt="OpenID" style="max-width:100px;max-height:100px;" class="size-full wp-image-4431"/></a>
            <figcaption class="text-center">OpenID</figcaption>
        </figure>


## OpenID
It is really annoying to register on every single page you use. The idea behind OpenID is having one account for registering on many domains. If you want to log-in in Blogger, you are sent to Google. You type in your username and password and Google sends you back to Blogger.

Here is another explanation:
<iframe title="YouTube video player" class="youtube-player" type="text/html" width="512" height="414" src="//www.youtube.com/embed/xcmY8Pk-qEk" frameborder="0" allowFullScreen></iframe>

The process seems to be too complex for many users, so Google developed the <a href="http://code.google.com/intl/de-DE/apis/identitytoolkit/index.html">Google Identity Toolkit</a> (GIT). The technique is really nice, but I don't like the idea that I have to force my users to use Google (or a service of them). Though I use Google for almost everything.


## Ajax
<a href="http://en.wikipedia.org/wiki/Ajax_(programming)" rel="nofollow">Ajax</a> is a programming style. If you like to view another page or get some information which isn't already loaded, you don't have to reload the whole page. The Pages simply display the new content as soon as it has loaded the content. GMail makes heavy use of Ajax.

<h2>Hierarchical Labels</h2>
Well, I guess this is less a technology than an idea. I think it would be great if labels were used more often. I'd like to sort my personal files with labels, not with folders. The advantage of labels in comparison with folders is that you can add any number of labels to one object (file, e-mail, ...). But you can have a file only in one path if you don't copy the file. So you have to know how the person is thinking, if you want to find the file you are searching for.

Example: You search for a file about you favorite books. Unfortunately, you don't remember if it was an Excel-file or a Word-file. Now you have this tree structure:

<ul>
<li>Excel</li>
<li>Documents
<ul>
<li>School</li>
<li>E-mails</li>
<li>eBooks</li>
<li>Math</li>
</ul>
</li>
<li>School
<ul>
<li>Biology</li>
<li>Chemistry</li>
<li>English</li>
<li>Math</li>
</ul>
</li>
<li>Word</li>
</ul>

The document you a re searching for could be in Word; in School/English, in Documents/eBooks or in Excel. You you had labels for your files, you could just select the files with a "Books"-label.

I wrote "Hierarchical Labels", because sometimes you have one label, that comes always with another one, but not the other way round. As I am not very interested in chemistry, all files about chemistry were for school. So if I tagged a file with "chemistry" it should automatically get the "school"-tag.

<figure class="alignright">
            <a href="../images/2011/10/Gravatar-Logo.png"><img src="../images/2011/10/Gravatar-Logo.png" alt="Gravatar-Logo" style="max-width:63px;max-height:63px;" class="size-full wp-image-4441"/></a>
            <figcaption class="text-center">Gravatar-Logo</figcaption>
        </figure>
<h2>Gravatar</h2>
Have you ever noticed <a href="http://www.sembeo.com/ninja/comment-page-2/" rel="nofollow">blogs</a> or <a href="http://stackoverflow.com/questions/4880891/javascript-settimeout-and-changes-to-system-time-cause-problems" rel="nofollow">other</a> sites where some people have avatars and others don't? Sometimes, if a possibility to login is provided this is not really amazing. But where does the website get the pictures from if there is no possibility to log in?

<a href="http://en.wikipedia.org/wiki/Gravatar" rel="nofollow">Gravatar</a> (an abbreviation for globally recognized avatar) is a service for providing globally-unique avatars. This is good for any website, where you don't have the possibility to store large amounts of data or you don't want to be annoyed with different file types, resizing and users who can't manage to use your software.

<a href="http://lea.verou.me/demos/gravatar.php?email=info%40martin-thoma.de">Here</a> is a web service, that allows you to quickly see the Gravatars of one e-mail address.

<h2>
Links for developers</h2>
<ul>
<li><a href="http://openid.net/developers/libraries/" rel="nofollow">OpenID libraries</a></li>
<li><a href="http://de.gravatar.com/site/implement/hash/" rel="nofollow">Working with Gravatar</a></li>
<li><a href="http://www.petefreitag.com/item/465.cfm" rel="nofollow">Howto Create an RSS 2.0 Feed</a></li>
</ul>
