---
layout: post
status: publish
published: true
title: Add a new font to ImageMagick
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 59671
wordpress_url: http://martin-thoma.com/?p=59671
date: 2013-03-06 23:15:26.000000000 +01:00
categories:
- Cyberculture
tags:
- ImageMagick
comments: []
featured_image: 2013/03/Imagemagick-logo.png
---
You can list all fonts that are known to ImageMagick by <code>identify -list font</code>. When your font isn't there, but it is installed, you might want to try these steps:

<ul>
  <li><code>sudo updatedb</code></li>
  <li>Download <a href="http://www.imagemagick.org/Usage/scripts/imagick_type_gen">imagick_type_gen</a></li>
  <li>Execute it: <code>perl imagick_type_gen > types.xml</code></li>
  <li>Copy the result to the folder where it should be
  <ul>
    <li><code>locate type.xml</code>. That was <em>/usr/lib/ImageMagick-6.5.7/config/type.xml</em> for me</li>
    <li><code>sudo cp type.xml /usr/lib/ImageMagick-6.5.7/config/type.xml</code></li>
  </ul>
  </li>
</ul>

You can find some nice fonts <a href="http://www.losttype.com/browse/">here</a>.
