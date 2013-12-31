---
layout: post
title: WordPress Comment Spam
author: Martin Thoma
date: 2013-03-20 10:10:15
categories: 
- The Web
tags: 
- CAPTCHA
- Spam
- WordPress
featured_image: 2011/09/WordPress-Logo.png
---
At the moment, I use <a href="http://wordpress.org/extend/plugins/wp-recaptcha/">WP-reCAPTCHA</a> to prevent spam comments and <a href="http://wordpress.org/extend/plugins/akismet/">Akismet</a> to detect spam comments.

TODO: Akismet stats

<h2>Disqus</h2>
One alternative would be to completely pass my comment administration to <a href="http://wordpress.org/extend/plugins/disqus-comment-system/">Disqus</a>. 

<h2>Require login with OpenID</h2>
Another alternative is to force people to login. Yes, this only solves half of the problem as spammers will also create accounts. So I hope that if I only offer login via OpenID (and possibly Facebook) they might not get through that.

I could use <a href="http://wordpress.org/extend/plugins/openid/">WordPress OpenID plugin</a> to get OpenID support.