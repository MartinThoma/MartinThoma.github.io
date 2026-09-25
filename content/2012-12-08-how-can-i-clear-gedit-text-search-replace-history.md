---
layout: post
title: How can I clear gedit text search / replace history?
slug: how-can-i-clear-gedit-text-search-replace-history
lang: en
author: Martin Thoma
date: 2012-12-08 13:48:28.000000000 +01:00
category: My bits and bytes
tags: gedit, GNOME, Linux
featured_image: 2011/12/gedit.png
---
Start <code>gconf-editor</code>:
```bash
gconf-editor
```

Go to <code>/apps/gnome-settings/gedit/history-gedit2_search_for_entry</code> and <code>/apps/gnome-settings/gedit/history-gedit2_replace_entry_with</code> and remove the content there:

<figure>
    <a href="../images/2012/12/gedit-remove-text-search-history.png"><img src="../images/2012/12/gedit-remove-text-search-history.png" alt="gedit: Clear text search / replace history" width="512" height="392"></a>
    <figcaption>gedit: Clear text search / replace history</figcaption>
</figure>
