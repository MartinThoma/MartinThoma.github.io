---
layout: post
title: Bug Reporting - A users perspective
author: Martin Thoma
date: 2015-01-21 14:54
categories:
- Cyberculture
tags:
- Bugs
- Issues
- Software Quality
- User Experience
- Caja
- Chrome
featured_image: logos/bug.png
---
Bug reporting is extremely important. It helps developers to get aware of
problems and hence get the possibility to do something against it. It is
impossible to guarantee for any real, non-trivial software that it has no bugs.
Even when you formally prove that it is correct, the prove might be wrong.
However, when users report bugs one can get confident that the remaining bugs
are appearing very rarely or causing not so much harm.

Reporting bugs is also important from a User Experience point of view. For me,
it already helps to be able to report a bug / see that a bug was already
reported. However, this is a pain in the ass for most software from a users
perspective.

I've just had that experience for Caja (the file explorer of MATE).

## Caja example

### Get information

Caja crashed. I just wanted to create a new text file. Then it froze for
about two seconds and closed. After another one or two seconds I got a crash
report window. (I forgot to make a screenshot of that, but it looks like
in the Google Chrome example)

I clicked on something like "examine locally" - whatever that means. This is
the first point I have to critize. The user should always know or at least be
able to get the information what such messages mean.

I was curious, so I clicked on it. Then this appeared:

{% caption align="aligncenter" width="500" alt="Apport 'examine locally' window" text="Apport 'examine locally' window" url="../images/2015/01/apport-examine-locally.png" %}

> This will launch apport-retrace in a terminal window to examine the crash.

That is fine.

> - Run gdb session
> - Run gdb session without downloading debug symbols
> - Update /var/crash/_usr_bin_caja.1000.crash with fully symbolic stack trace

That is not ok. This might be good information for developers, but for normal
users it is useless. There should be information when to use which one.
For example:

* Which option takes most time (if there is a significant difference)?
* Is one option a superset of the other?
* Might one option contain private / secret information which I should not share?

Lets try 'Run gdb session'. By the way, 'gdb' is the GNU project debugger.

{% caption align="aligncenter" width="500" alt="Error creating child process" text="Error creating child process" url="../images/2015/01/run-gdb-session.png" %}

Hrmpf. Seems as if I found a bug while trying to report a bug...
This happens for every option.

Ok. Let's see if I can report the bug. As the automatic tools did not help,
I check for a program version via *Help > About*:

{% caption align="aligncenter" width="500" alt="Caja About window" text="Caja About window" url="../images/2015/01/caja-about.png" %}

Nice! It is obvious which version I use and how the program is called
(Caja 1.8.2). There is even a link to a website where I could eventually report
the bug. It links to [www.mate-desktop.org](http://www.mate-desktop.org/).


### Report bug
When I search for 'bug' on [www.mate-desktop.org](http://www.mate-desktop.org/)
I get to
[Reporting Bugs](http://www.mate-desktop.org/tr/blog/2012-01-18-reporting-bugs/).
That seems to be a blog article which explains they are moving to GitHub with a
link to [github.com/mate-desktop](https://github.com/mate-desktop). There are
many repositories, so I have to search. Hrmpf. Then I get:

{% caption align="aligncenter" width="500" alt="Caja Repositories" text="Caja Repositories" url="../images/2015/01/caja-github.png" %}

5 repositories. Hrmpf. I guess it is simply 'caja'. When I click on this
repository, I have to click on 'issues'.

Now I am stuck. I don't know how to find a better description than
"it crashed". There is certainly more information on my system, but I don't
know how to get to it and I don't see any instructions how to do so. I also
don't want to waste my time searching for information how to get information
about the crash.


## Google Chrome example

Just a few images...

{% gallery columns="3" size="medium" %}
    ../images/2015/01/bug-chrome-ubuntu-closed-unexpectedly.png    "Step 1"
    ../images/2015/01/bug-chrome-details-1.png    "Details 1"
    ../images/2015/01/bug-chrome-details-2-dependencies.png    "Details 2"
    ../images/2015/01/bug-chrome-details-3.png    "Details 3"
    ../images/2015/01/bug-chrome-details-4.png    "Details 4"
{% endgallery %}


## What's wrong and how to fix it

Did you notice how complicated this is for a user? This should be easier. In
fact, I think if the bug reporting process is done right it could enhance the
trust a user has in software, speed the fixing process up and help develpers
to proritize what is important. Some basic steps could be:

* The automatic reporting tool should be created for non-developers.
* It should automatically store crash information in a place where the user
  can easily find it (e.g. /home/myaccount/.bugreports/caja/yyyy-mm-dd-hh-mm.xml)
* It should be stored in a format which the user can read (e.g. an xml file)
* The bug reporting website should be hosted by somebody else.

Now the last one is important in my opinion. It makes sure that users know
their bugs are not deleted / removed from the public just because it makes
the software look bad. One could add metrics how confident users are, e.g.
if you let users tell which software they use. In this case you can add graphs
of how many users use the software and how many bugs / issues are reported.
(The classification bugs and issues might also not be easy for users!)

## Existing Issue Trackers

All of the following bug trackers seem to be developed for developers, not
for users:

* Open Source Projects:
  * [Trac](https://en.wikipedia.org/wiki/Trac): Python
  * [Bugzilla](https://en.wikipedia.org/wiki/Bugzilla): Perl
  * [Mantis Bug Tracker](https://en.wikipedia.org/wiki/Mantis_Bug_Tracker): PHP
  * [Redmine](https://en.wikipedia.org/wiki/Redmine): Ruby on Rails
* Hosted Services:
  * GitHub issues (e.g. for [numpy](https://github.com/numpy/numpy/issues))
  * Google Code (e.g. for [chromium](https://code.google.com/p/chromium/issues/list))
  * SourceForge (e.g. for [dvdstyler](http://sourceforge.net/p/dvdstyler/bugs/?source=navbar))
  * Launchpad (e.g. for [ubuntu](https://bugs.launchpad.net/ubuntu))
  * GNU Savannah (e.g. for [lordsawar](http://savannah.nongnu.org/bugs/?group=lordsawar))

See also:

* [Comparison of source code software hosting facilities](https://en.wikipedia.org/wiki/Comparison_of_source_code_software_hosting_facilities)