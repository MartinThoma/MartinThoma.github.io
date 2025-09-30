---
layout: post
lang: en
title: How can I clear gedit text search / replace history?
slug: how-can-i-clear-gedit-text-search-replace-history
author: Martin Thoma
date: 2012-12-08 13:48:28.000000000 +01:00
category: My bits and bytes
tags: gedit, GNOME
featured_image: 2011/12/gedit.png
---
Start <code>gconf-editor</code>:
```bash
gconf-editor
```

Go to <code>/apps/gnome-settings/gedit/history-gedit2_search_for_entry</code> and <code>/apps/gnome-settings/gedit/history-gedit2_replace_entry_with</code> and remove the content there:

<figure class="aligncenter">
            <a href="../images/2012/12/gedit-remove-text-search-history.png"><img src="../images/2012/12/gedit-remove-text-search-history.png" alt="gedit: Clear text search / replace history" style="max-width:512px;max-height:392px" class="size-full wp-image-50181"/></a>
            <figcaption class="text-center">gedit: Clear text search / replace history</figcaption>
        </figure>
