---
layout: post
status: publish
published: true
title: How can I clear gedit text search / replace history?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 50171
wordpress_url: http://martin-thoma.com/?p=50171
date: 2012-12-08 13:48:28.000000000 +01:00
categories:
- My bits and bytes
tags:
- gedit
- GNOME
comments:
- id: 1138951
  author: Vlad
  author_email: vladv@vladv.umail.net
  author_url: ''
  date: !binary |-
    MjAxMy0wMi0xOCAwMzowNzo1NyArMDEwMA==
  date_gmt: !binary |-
    MjAxMy0wMi0xOCAwMjowNzo1NyArMDEwMA==
  content: ! "In a recent versions the history was moved to dconf.\r\nUse dconf-editor
    to edit the setting, its path is /org/gnome/gedit/state/history-entry."
featured_image: 2011/12/gedit.png
---
Start <code>gconf-editor</code>:
{% highlight bash %}gconf-editor{% endhighlight %}

Go to <code>/apps/gnome-settings/gedit/history-gedit2_search_for_entry</code> and <code>/apps/gnome-settings/gedit/history-gedit2_replace_entry_with</code> and remove the content there:

[caption id="attachment_50181" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/12/gedit-remove-text-search-history.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/12/gedit-remove-text-search-history.png" alt="gedit: Clear text search / replace history" title="gedit: Clear text search / replace history" width="512" height="392" class="size-full wp-image-50181" /></a> gedit: Clear text search / replace history[/caption]
