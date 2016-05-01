---
layout: post
title: MediaViewer and Superprotect
author: Martin Thoma
date: 2014-08-15 14:35
category: Cyberculture
tags: Wikipedia, Community, WMF, superprotect, MediaViewer
featured_image: logos/wikipedia.png
---

Recently, a heated discussion started on the German Wikipedia about Superprotect.
This article should give a very short summary how it came to this discussion.

## Timeline

* **25. July 2014**: Straw poll in the German Wiki began ([link](https://de.wikipedia.org/wiki/Wikipedia:Meinungsbilder/Medienbetrachter))
* **08. August 2014**: Straw poll in the German Wiki ended. 72.5% voted for a
  default deactivation of the MediaViewer
* **09. /10. August 2014**: The Admins [DaB.](https://de.wikipedia.org/wiki/Benutzer:DaB.),
  [Raymond](https://de.wikipedia.org/wiki/Benutzer:Raymond) and [JEissfeldt (WMF)](https://de.wikipedia.org/wiki/Benutzer:JEissfeldt_(WMF)) repeatedly change [MediaWiki:Common.js](https://de.wikipedia.org/wiki/MediaWiki:Common.js) to activate / deactivate the MediaViewer
  for the German wiki
* **10. August 2014**: Superprotect got introduced and Erik Möller ([User:Eloquence](https://de.wikipedia.org/wiki/Benutzer:Eloquence)) protected MediaWiki:Common.js.

## The MediaViewer

You can [try the MediaViewer](https://en.wikipedia.org/wiki/Wikipedia:Media_Viewer)
to get a feeling what this is all about.

You can view some images of the MediaViewer here:

{% gallery size="medium" columns="2" %}
    ../images/2014/08/wikipedia-first-view.png "Article"
    ../images/2014/08/media-viewer-first-click.png "First click on image with MediaViewer"
    ../images/2014/08/without-media-viewer-first-click.png "First click on image without MediaViewer"
    ../images/2014/08/media-viewer-first-click-notes.png "notes to the MediaViewer interface"
    ../images/2014/08/media-viewer-more-information.png "MediaViewer Bottom 'Tab'"
    ../images/2014/08/media-viewer-use-this-file.png "MediaViewer 'Use this file'"
{% endgallery %}

There has been a survey that suggests that 60% of all users like the MediaViewer ([source](https://www.mediawiki.org/wiki/Multimedia/Media_Viewer/Survey)).
However, there are concerns that the survey was biased ([source](https://en.wikipedia.org/wiki/Wikipedia:Media_Viewer/June_2014_RfC#Biased_survey_wording)).

You should know that you can easily disable the MediaViewer if you have an
account:

> Preferences → Appearance → Files = uncheck 'Enable Media Viewer'


The question is: Should the MediaViewer be activated per default?

### Pro

* Average users want to see the image in a higher resolution. The MediaViewer
  looks more professional than the old view.

#### Wrong arguments

* The copyright notice doesn't get in my way.<br/>
  It is a legal obligation to show the copyright notice.

### Contra

* The MediaViewer doesn't give new functionality: One could see high-resolution
  images before by simply clicking a second time on the image.
* The MediaViewer makes it more difficult for new users to edit file
  descriptions.
* The MediaViewer hides information like the copyright status.
  * Charts and maps that are color-coded and change/are edited over time and have a legend/key in multiple languages simply do not work with this interface. See [this example](https://en.wikipedia.org/wiki/Same-sex_marriage_in_the_United_States#mediaviewer/File:Samesex_marriage_in_USA.svg).
* The MediaViewer makes browsing difficult on touch-screen devices that use pinch-to-zoom.
* It becomes almost unusably slow on slower machines or machines on a slow connection.
* MediaViewer makes it more difficult to find the image in the highest resolution.

#### Wrong arguments

* It's in the way of long-term wikipedia editors.<br/>
  This argument is wrong, because long-term wikipedia editors can simply disable
  it. They should know how to do it.
* Logged in in users don't need this feature.<br/>
  Again, they can disable it.

### Good comments

* The default setting for logged-in users should be the same as for unregistered users, so that new users have fewer surprises to deal with. 

### Alternatives to default-enable MediaViewer

* Change from opt-out to opt-in
* Disabled for current users and enabled for newly registered users

## Superprotect

The German Wikipedia community decided to disable MediaViewer per default.
As the MediaViewer got rolled out, some admins in the German Wikipedia enabled / disabled
it (see [version history of Common.js](https://de.wikipedia.org/wiki/MediaWiki:Common.js)). This was the reason to create
superprotect:

> Add a new protection level called "superprotect"
> <br/>
> Assigned to nobody by default. Requested by Erik Möller for the purposes
of protecting pages such that sysop permissions are not sufficient to
edit them.
>Change-Id: Idfa211257dbacc7623d42393257de1525ff01e9e

Source: [gerrit.wikimedia.org](https://gerrit.wikimedia.org/r/#/c/153302/)

That started another community poll in the German wiki:

[Wikipedia:Umfragen/Superschutz](https://de.wikipedia.org/wiki/Wikipedia:Umfragen/Superschutz)

and

[Wikipedia:Meinungsbilder/Gruppenrecht Superschutz](https://de.wikipedia.org/wiki/Wikipedia:Meinungsbilder/Benutzerrecht_Superprotect)

Now the question is: Should the new group right 'super protect' be kept?

### Pro

* Super protect is a necessary tool to temporarily prevent abuse of admin powers
  in heated discussions.
* The WMF has the legal right to do what they want on wikipedia.org.
* The WMF controls the technical details of the Wikipedia platform, whereas the
  community only controls the content.

#### Wrong arguments
* The super protect right was necessary as one admin was abusing his power.<br/>
  If the problem is only one admin, there already is the possibility to remove
  the admin status of this user.
* The WMF has the legal right to do what they want and they need superprotect
  to have legal security.<br/>
  That is simply wrong. There is (currently) no case where an admin tried to
  put something illegal on Wikipedia.org and abused his admin rights to keep
  it there.

### Contra

* There is no need for such a tool, as the community is able to solve 'wheel wars'.
* In case of the abuse of powers by admins, these powers can be removed (see [Review and removal of adminship](https://en.wikipedia.org/wiki/Wikipedia:Administrators#Review_and_removal_of_adminship))
* The community wants to organize Wikipedia by themselves without intervention
  from the WMF. The problem for many users seems to be that the WMF is not
  elected, whereas admins are (see [Wikipedia:Administrators#Becoming_an_administrator](https://en.wikipedia.org/wiki/Wikipedia:Administrators#Becoming_an_administrator) - there seem to be differences in the English / German Wiki).
* The new concept of 'super protection' was introduced too fast without a concept which was discussed within the community.
* The risk of misuse of power is too high as there is no mutual control.

### Comments

I think super protect might be a good solution to temporarily freeze pages
when more than two admins have a wheel war. In that case it could be implemented
so that it can only freeze a page for 7 days and after those 7 days the page
cannot be frozen for at least 14 days (one would have to discuss the numbers).

This way, it can be a tool for de-escalation and the abuse can be limited.

Also, sites that get frozen must have at least two back-and-forth edits by two
admins and the community must have voted for freezing.

## Terms

**[Wikipedia](https://en.wikipedia.org/wiki/Wikipedia)** is the free Internet encyclopedia at wikipedia.org.

**[MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)** is the software that Wikipedia uses. It is also free and it gets developed by the Wikimedia Foundation and others. You
can [download MediaWiki here](https://www.mediawiki.org/wiki/MediaWiki) and find the source code via `https://gerrit.wikimedia.org/r/p/mediawiki/core.git`.

**[Wikimedia Foundation](https://en.wikipedia.org/wiki/Wikimedia_Foundation)** (short: WMF) is an American non-profit and charitable organization headquartered in San Francisco, California, that operates wikipedia.org.

**[MediaViewer](https://en.wikipedia.org/wiki/Wikipedia:Media_Viewer)** is a JavaScript that gives the possibility to browse through all images of an article by using a diashow.

**Wheel war** is happening when two or more admins repeatedly revert their changes.

## Sources

* [Wikipedia:Superschutz](https://de.wikipedia.org/wiki/Wikipedia:Superschutz) (German)
* [Multimedia/Media Viewer/Survey](https://www.mediawiki.org/wiki/Multimedia/Media_Viewer/Survey)
* [Wikipedia:Media Viewer/June 2014 RfC](https://en.wikipedia.org/wiki/Wikipedia:Media_Viewer/June_2014_RfC)
* [Wikipedia:Meinungsbilder/Medienbetrachter](https://de.wikipedia.org/wiki/Wikipedia:Meinungsbilder/Medienbetrachter)