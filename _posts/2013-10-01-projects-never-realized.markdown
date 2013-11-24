---
layout: post
status: publish
published: true
title: Projects I never realized
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 76376
wordpress_url: http://martin-thoma.com/?p=76376
date: 2013-10-01 23:41:37.000000000 +02:00
categories:
- Cyberculture
tags:
- Idea
comments:
- id: 1237910
  author: addy
  author_email: tru5@hotmail.de
  author_url: ''
  date: !binary |-
    MjAxMy0xMC0wNyAyMDoxNTowMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0xMC0wNyAxODoxNTowMiArMDIwMA==
  content: ! "Actually, there are modern \"Not so smart phones\"\r\nhttp://www.amazon.de/Samsung-E1050-Handy-Branding-black/dp/B004LR5PRQ/ref=sr_1_1?s=ce-de&amp;ie=UTF8&amp;qid=1381169455&amp;sr=1-1&amp;keywords=handy\r\n\r\nThis
    device was realeased in 2011, I don't know if Samsung offers newer models. Be
    aware, the market for \"simple\" mobile phones is extremely declining in the US
    and Europe."
- id: 1237913
  author: bob
  author_email: bob@bob.com
  author_url: ''
  date: !binary |-
    MjAxMy0xMC0wOCAxODowNjowOCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0xMC0wOCAxNjowNjowOCArMDIwMA==
  content: for "work computers" Google have the Chromebooks https://www.google.co.uk/intl/en/chrome/devices/
- id: 1237917
  author: Magnus
  author_email: magnus@coderoots.org
  author_url: ''
  date: !binary |-
    MjAxMy0xMC0wOSAxNDoxOTo0OCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0xMC0wOSAxMjoxOTo0OCArMDIwMA==
  content: Hey, the complete (or nearly) Office Suite by Microsoft can be used online,
    with only a LIVE account. Also usefull for poeple who don't have a license!
---
The following is a collection of ideas for projects I had, but never realized. I would really love to do them, but they seem to be a little bit too time consuming to do them in my free time. Please send me an Email if you would like to realize them!

<h2>Book portal</h2>
I really miss a book recommendation portal. It should allow you to mark books you've read or started to read, let you rate and tag books. The tags should be created by users, similar to the system StackExchange uses. Tags might be funny", "zombie", "magic", "romance", "love", ... and users should rate for tags for books. 
In some general settings you define language(s) you know. Every book, which should be administrated by ISBN number if possible, should have information about the language. The portal should also see when books are only released with a new cover / collectors edition and notice that its the same story.

With this information, it should recommend books and allow you to search books.

Eventually you could connect to friends and let their ratings influence what you get.

And, very important, it should let you follow series and/or authors. So you should be able to say "When there is a new book of the 'Harry Potter' series, send me an email!" or "When there is a new book of the 'Harry Potter' series translated to 'German', send me an email!".

<h2>Science and Education Platform</h2>
Sometimes, scientists get new insights that are able to influence millions. But until such a great invention or discovery is made, hundreds or thousands of people might have thought about the same problem. Today, with <abbr title="Massive open online courses"><a href="https://en.wikipedia.org/wiki/Massive_open_online_course">MOOCs</a></abbr> education in some fields is quite open to a lot of people. <a href="https://www.khanacademy.org/">Khan academy</a> offers many very basic courses, <a href="https://www.coursera.org/">Coursea</a> and <a href="https://www.udacity.com">Udacity</a> a few advanced ones. But the process of creating new content seems to be quite closed. <a href="https://en.wikiversity.org">Wikiversity</a> is more open, but very limited. For example, I think it is not possible to include <a href="http://martin-thoma.com/html5/graphic-filters/graphic-filters.htm">my graphic filter examples</a>. And it is not possible to track progress of students.

I think it is necessary to gamify this. Both, students and educators, should get rewards. They might be only digital, but a student who can see the progress he makes might be much more interested in continuing a course. A teacher who can see the influence he has, who can see how students learn and where problems are might be much better able to improve his content and be motivated to do so. 

Also, scientists should not have to worry about presenting their studies. A lot of people know how to create graphics, some people know better about (the English) language and others are experts in LaTeX. If people were able to create requests online, get rewards for helping others and provide rewards to show that they really need help, I guess much better research could be made. Of course, this should be open.

For every unit / paper, there should be definitions what is necessary to know. The topics should automatically be linked to content that provides the knowledge.

It is very complex to plan such a system, because education in different languages / nations might be very different and ideas how to educate vary a lot. Even subtasks (creating a LaTeX editor, a graph that shows influence of papers / books by citation, creating an image editor, creating a reward system) are very difficult. And everything has to scale for millions of users. This means you would have to plan quite a lot before you could even think about implementation. For this project, you would need:
<ul>
  <li>Somebody, who has experience with online courses.</li>
  <li>A teacher for children.</li>
  <li>A teacher for teenagers.</li>
  <li>A teacher for students.</li>
  <li>Somebody, who has experience with gamification.</li>
  <li>Somebody, who has contacts to politics and knows how to advertise.</li>
</ul>

<h2>Wikipedia KI</h2>
Try to categorize images in <a href="https://en.wikipedia.org/wiki/Category:Uncategorized_images">Category:Uncategorized images</a> or find images that have the wrong category / missing categories.

<h2>Translations</h2>
I did some translation work some years ago for <a href="http://www.nongnu.org/lordsawar/">LordsAWar</a>. From a software point of view, this was a pain in the ass. Rosetta (part of Launchpad, for Ubuntu) is much better.

Another idea that is much better is <a href="http://www.duolingo.com/">Duolingo</a>.

<h2>Distributed, Universal Tagging System</h2>
<h3>Tagging</h3>
Most information can be displayed rather simple. A string that describes the kind of information and a bool / int / float / string / BLOB for the information itself and an identifier.

For example, you can describe a product with the following labels:
<ul>
  <li>Identifier: "898a4c822ffc456fa7a417e500b2c05a"</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "ISBN-10": "0141439513" (string)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "ISBN-13": "978-0141439518" (string)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "Pages": 480 (int)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "Publisher": "Penguin Classics" (string)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "Category": "Book" (string)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "Category": "Literature" (string)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "Category": ed054753e4b240a8aa1322ad348bf728 (identifier)</li>
  <li>"898a4c822ffc456fa7a417e500b2c05a", "VIEW": 0839c5beac414fb19c400b6ca0372388 (identifier)</li>
  <li>Identifier: "ed054753e4b240a8aa1322ad348bf728"</li>
  <li>"ed054753e4b240a8aa1322ad348bf728", "Name": "Literature"</li>
  <li>"ed054753e4b240a8aa1322ad348bf728", "Category": "Books"</li>
</ul>

As you can see, it is possible to create nested categories with this structure. You an also create lists this way.

Now clients should store information like this and share it. 

<h3>Views</h3>
When information is presented like this, it is quite useless. But what about this kind of presentation:

[caption id="attachment_76576" align="aligncenter" width="267"]<a href="http://martin-thoma.com/wp-content/uploads/2013/10/pride-and-prejudice-infobox.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/10/pride-and-prejudice-infobox.png" alt="Pride and prejudice infobox" width="267" height="549" class="size-full wp-image-76576" /></a> Pride and prejudice infobox (defined <a href="https://en.wikipedia.org/wiki/Template:Infobox_book">here</a>)[/caption]

Or, for example <a href="http://ark.intel.com/compare/75133,50176">ark.intel.com</a>:

[caption id="attachment_76577" align="aligncenter" width="643"]<a href="http://martin-thoma.com/wp-content/uploads/2013/10/intel-ark-compare.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/10/intel-ark-compare.png" alt="Intel Arc compare processors" width="643" height="591" class="size-full wp-image-76577" /></a> Intel Arc compare processors[/caption]

So another required feature of such a client are "views". A view is defined by an identifier (so that you can tag views just like any other object) and an HTML template. Objects could have labels called "VIEW" with type identifier that tell the client which view should be added.

<h3>Distribution</h3>
There are plenty of cool tools out there (Amazon recommendations, <a href="http://ark.intel.com/">ark.intel.com</a> to compare Intel processors, <a href="http://de.blackberry.com/smartphones/compare.html">blackberry</a> allows you to compare their phones, Wikipedia info boxes, ...). But most of them are very ristricted. For example, the way I compare smartphones is not fundamentally different from the way I compare processors. Yes, the attributes differ. But basically it is creating a table with all the information. Also, Intel does not provide information about AMD processors.

So we need a way to get and share information. XML is the way-to-go for centralized computer systems. Maybe they can also be used to realize what I'm thinking about. But I think a problem that has to be solved is that we don't have a single source for all information that we trust in. We have networks of trust. When Intel says A and a friend says B about an Intel processor, I guess I will rather believe A. But when Intel does not provide some information about a processor and a friend says B, but a person I don't know says C, I'll believe B. But when thousands of people say C and my friend says B, I might rather believe C.

It's getting complicated, right? Maybe the processor example is not good, as there is much information and information is either right or wrong. But lets say we talk about genre of movies. This might be much more difficult as there is no "definitely right" or "definitely wrong". Multiple answers might be right. 

So every information has also have to carry information about who thinks it is right. And you have to be able to define networks you trust in. Perhaps you could create "people objects" that can also be labeled. "Your" object had to be protected so that only you could add "friend of" labels or "I trust" labels or something like this.

<h2>Chrome</h2>
I had some <a href="http://martin-thoma.com/how-chrome-could-be-improved-2nd-post/">ideas how to improve Chrome</a>.

<h2>MATE</h2>
After the changes in desktop environments, <a href="https://en.wikipedia.org/wiki/MATE_(software)">MATE</a> got my favorite desktop environment. Although I was more happy with GNOME 2.6.

<ul>
  <li>Adding the drag-and-drop effect that creates a new window from an tab, known from Chrome, to Terminal and Pluma (gEdit).</li>
  <li>Creating a LaTeX plugin for Pluma that auto-completes the environments.</li>
</ul>

<h2>LaTeX Tools</h2>
I would like to create online tools (pure HTML/CSS/JavaScript) that make the following tasks simpler.
<ul>
  <li>A table editor. I know <a href="http://truben.no/latex/table/">Trubens table tool</a>, but this tool does not allow to combine cells. Also, the site is down quite often.</li>
  <li>A Ti<em>k</em>Z editor.</li>
  <li>An editor for bibliography.</li>
  <li>A LaTeX source code beautifier.</li>
  <li>A LaTeX-aware spell checker. This spell checker could probably use aspell, but it would have to filter LaTeX code.</li>
</ul>

Also, I would like to create an app that helps users to create formulas. This app should run on smartphones and on tablets. I don't think that this can be done with pure JavaScript.

<h2>Open Hardware</h2>
I'm fascinated by the idea of open hardware. That means that you publish plans of something and maybe also how to create it. Although I don't have any experience in this field, I can think of some interesting projects. One way to support open hardware would be to create an education and science platform, like the one I've described above.

<h3>Open Internet</h3>
I guess most smartphone users know this situation: You go to a friend / on vacation and you don't have WLAN. This means you have to use mobile internet, which is expensive. If you're in an area where not many people live, it is ok. If you're in a big city, it is not. There are so many people who have an internet connection and a router which already establishes a WLAN. You can see them, but not use the connection! What a shame!

What we would need is a device with the following attributes:
<ul>
  <li>Simplicity
    <ul>
      <li>It has to be a <a href="https://en.wikipedia.org/wiki/DSL_modem">DSL modem</a> and a <a href="https://en.wikipedia.org/wiki/Router_(computing)">router</a> combined, eventually also a <a href="https://en.wikipedia.org/wiki/DSL_filter">DSL filter</a>.</li>
      <li>Everything has to be configurable via web interface. This interface has to be VERY GOOD.</li>
      <li>You should be able to get a backup file via web interface that contains every single configuration. This file should be an good documented XML file. The documentation should contain example data.</li>
      <li>Every setting should have its own url, just like in Google Chrome.</li>
      <li>As many self-tests that give meaningful messages as possible:
        <ul>
          <li>A LED that indicates if the device has power.</li>
          <li>Ethernet jack should glow if a device is connected and blink if data is send.</li>
          <li>A software test via web interface that checks if internet connection is available.</li>
          <li>Direct feedback when you enter wrong / malformed credentials.</li>
        </ul>
      </li>
      <li>A reset button that restores the software completely from non-erasable memory.</li>
      <li>Small memory and rechargeable battery that allows you to download router software updates when the battery is full.</li>
      <li>A user manual with pictures that explains what to do to get internet.</li>
    </ul>
  </li>
  <li>Functionality and requirements
    <ul>
      <li>It has to be able to create a WLAN.</li>
      <li>It has to be fast. I think currently 802.11n is with 450 Mbit/s the best you can get for WLAN and 1000 Mbit/s for Ethernet</li>
      <li>At least one Ethernet jack.</li>
      <li>It should be secure (WPA2, eventually don't support WEP and WPA).</li>
      <li>Reasonable energy consumption and no active fans.</li>
      <li>A standardized power supply unit that can be bought without buying a new device.</li>
    </ul>
  </li>
  <li>Box - how it looks
    <ul>
      <li>The case should be robust.</li>
      <li>You should be able to mount it to a wall or to lay it on the floor.</li>
    </ul>
  </li>
</ul>

I don't think it is necessary to support VoIP, ISDN and Surf Sticks.

Now the special part: It should allow you to create a WLAN that others can use by registering in a service. The device should guarantee that you get the bandwidth, in case you need it. But if you have free bandwidth, others should be able to use it.
Of course, this function should also protect you from legal trouble. An essential problem is keeping you from legal trouble while making sure that nobody uses the system to betray external users. But when you solve this problem, I guess it would be quite easy to establish free WLAN in all bigger cities. A great chance for tourism and a backup-option for you when your internet connection breaks.

The service should also allow the user to register the free WLAN online. An app should download these locations and be 
able to navigate a user to the next free WLAN.

Ah and of course everything in there should be free. This piece of hardware is critical for your internet access. If you want to be sure that you don't get under surveillance by an attack on this piece of hardware, it would be good to know that some smart people had the possibility to check if everything is fine with this hardware.

<h3>Work computers</h3>
Today, we have a lot of computers that are used for very, very simple work. The most computing intensive part might be large Excel sheets. So basically, they don't need any improvements in hardware for years. But the few things they do, need to be done well. Security is important. It is also important that things are stable and don't change a lot. And what they do should be fast. Loading times are almost not acceptable.

I guess many tasks could be done within a browser. So work that needs heavy computation can be done on a stronger machine (the cloud - not necessarily outside of the company).

Why hasn't any big company like <a href="https://en.wikipedia.org/wiki/General_motors">General Motors</a>, <a href="https://en.wikipedia.org/wiki/General_Electric">General Electric</a>, <a href="https://en.wikipedia.org/wiki/Walmart">Wallmart</a> or even countries that have thousands of schools and government employees tried to create such a computer that is really reliable, robust and cheap (energy and because it can be produced it can be produced in very big numbers)?

Here is what I think should be ok:
<ul>
  <li>processor with low power consumption (700 MHz or more)</li>
  <li>2 GB of RAM (I guess you might now think of this <a href="https://en.wikiquote.org/wiki/Bill_Gates#Misattributed">missatributed Bill Gates quote</a> ... but with <code>cat /proc/meminfo</code> you can see how much you currently use).</li>
  <li>30 GB SSD: Important information should be stored on a computer that is protected very well against data loss. A SSD is silent and can read content very fast. Ideally, only the <abbr title="operating system">OS</abbr> is stored on the employees computer.</li>
  <li>VERY silent fan, if possible non at all.</li>
  <li>Big monitor with high resolution, because those people have to work all day with the computer and low quality speakers.</li>
  <li>Good and silent keyboards (like the <a href="http://codekeyboards.com/">CODE keyboard</a>).</li>
  <li>Network card.</li>
  <li>Graphic card that allows the high resolution display.</li>
</ul>

This is just a quick thought. I think such a system should contain some reference software that has to run fluidly. The software should also be open, of course.
I think the following should be enough:

<ul>
  <li>Linux based OS (e.g. <a href="https://en.wikipedia.org/wiki/Debian">Debian</a>)</li>
  <li>Basic command line tools (bash, grep, find, cat, vim)</li>
  <li>Desktop manager with classic desktop metaphor (e.g. <a href="https://en.wikipedia.org/wiki/MATE_(desktop_environment)">MATE</a>)</li>
  <li>File manager with access to a network drive (e.g. Caja or Nautilus)</li>
  <li>Modern Browser (Firefox or Chrome)</li>
</ul>

Tasks that can (and should) be done via browser are:
<ul>
  <li>Emails: e.g. <a href="https://en.wikipedia.org/wiki/Roundcube">Roundcube</a></li>
  <li>Excel: Hmmm ... I know that <a href="https://drive.google.com">Google Docs</a> offers some similar stuff. Bug I guess it can't replace Microsoft Excel by now. I don't know if there are any self-hosted services</li>
  <li>Word: e.g. <a href="http://etherpad.org/">Etherpad</a></li>
  <li>Outlook: e.g. <a href="http://owncloud.org/">OwnCloud</a></li>
  <li>LaTeX: e.g. <a href="https://github.com/alabid/flylatex">FlyLaTeX</a></li>
  <li>Geographic information systems: I don't know if there is software online. But I guess with OpenStreetMaps it should not be too difficult to create it. <a href="http://www.esri.com/software/arcgis/arcgisonline">ArcGis</a> seems to be one solution.</li>
</ul>

Basically, you can do almost everything with a web application. So the client can get quite slim. But although you could probably do everything with a self hosted client/server solution, those solutions don't always exist yet.

Tasks that should not be done via browser might be:
<ul>
  <li>Professional video/audio editing: I guess you need more than one monitor to display all relevant information.</li>
  <li>Programming: Although I have seen <a href="https://c9.io/">Cloud9</a>, I doubt that programming in the cloud can be convenient in the next years. How does bug fixing work? How about manual testing? Whats with parallel execution?</li>
  <li>Messaging: If you want to use encrypted communication (e.g. Email with PGP) you should probably do the encryption on your machine.</li>
</ul>

Hmmm ... astonishingly, I can currently not think of more tasks.

<h3>Not so smart phone</h3>
Do you remember the good old days when your cell phone wasn't essentially a small PC?
I've bought a smartphone a while ago (<a href="http://martin-thoma.com/nexus-4/">article</a>), but I still see reasons to have a cell phone:
<ul>
  <li>Battery life: My Motorola W156 had a battery with only 940 mAh, but 465 hours stand-by time. If it had 3100 mAh as the <a href="https://en.wikipedia.org/wiki/Samsung_Galaxy_Note_II">Samsung Galaxy Note II</a>, it would have a standby time of 1534 hours! That are about 64 days!</li>
  <li>Security: Have you ever heard of somebody hacking a device that can only phone and send SMS?</li>
  <li>Cost: The Motorola W156 costs 25 Euro on Amazon.</li>
  <li>Robustness: A friend of mine put her <a href="https://en.wikipedia.org/wiki/Nokia_3310">Nokia 3310</a> accidentally in the washing machine. After that, she removed the battery, let it dry for a week, put the battery back. It worked. What the hell!?! (See also: <a href="http://weknowmemes.com/2012/02/our-love-is-forever-so-here-is-a-nokia/">Nokia is forever</a> and <a href="http://knowyourmeme.com/memes/indestructible-nokia-3310">Indestructible Nokia 3310 meme</a>)</li>
  <li>Size: Modern smartphones are a little bit uncomfortable to phone with. They are too big, although they are very thin. A size of 114 x 43 x 14 mm is fine, maybe a little bigger is also ok.</li>
</ul>

The needed functionality is:
<ul>
  <li>Phone with good quality</li>
  <li>Send SMS (and repetedly try to do so if no net is available)</li>
  <li>Store about 100 contacts</li>
  <li>Save about 100 SMS</li>
  <li>Load battery via micro USB (<a href="https://en.wikipedia.org/wiki/Common_External_Power_Supply">Common External Power Supply</a>)</li>
  <li>If not too complicated: Let me back up all data on the phone via this micro-USB slot and let me also restore such a backup</li>
  <li>3.5mm phone jack for using a headset</li>
</ul>

What is not needed:
<ul>
  <li>Camera, Flashlight</li>
  <li>Internet access, Bluethooth, NFC, ...</li>
  <li>Multi-colored display: B/W screen is just ok</li>
  <li>Fingerprint scanner</li>
</ul>
