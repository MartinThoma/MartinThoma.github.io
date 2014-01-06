---
layout: post
title: How can I clear gedit text search / replace history?
author: Martin Thoma
date: 2012-12-08 13:48:28.000000000 +01:00
categories:
- My bits and bytes
tags:
- gedit
- GNOME
featured_image: 2011/12/gedit.png
---
Start <code>gconf-editor</code>:
{% highlight bash %}gconf-editor{% endhighlight %}

Go to <code>/apps/gnome-settings/gedit/history-gedit2_search_for_entry</code> and <code>/apps/gnome-settings/gedit/history-gedit2_replace_entry_with</code> and remove the content there:

{% caption align="aligncenter" width="512" caption="gedit: Clear text search / replace history" url="../images/2012/12/gedit-remove-text-search-history.png" alt="gedit: Clear text search / replace history"  height="392" class="size-full wp-image-50181" %}
