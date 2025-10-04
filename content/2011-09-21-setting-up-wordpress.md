---
layout: post
title: Setting up WordPress
slug: setting-up-wordpress
lang: en
author: Martin Thoma
date: 2011-09-21 19:36:18.000000000 +02:00
category: The Web
tags: WordPress
featured_image: 2011/09/WordPress-Logo.png
---
This article is about creating a new WordPress blog, including installation and basic customization.

You need to know how to upload files and have your MySQL database credentials available.

I used a similar setup and will update this post if I encounter any issues.

## Requirements

### Minimum

Webserver with:

- MySQL 5.0 or higher
- PHP 5.2.4 or higher
- 10 MB free space
- Any possibility to upload files

### Recommended

- The [mod_rewrite](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html) Apache module
- An FTP client (e.g., FileZilla)
## Installation

1. Download the latest version from [wordpress.org](http://wordpress.org/download/)
2. Decompress it and upload it to your web server. It should be directly in your root directory.

   *Example: Use www.martin-thoma.com, not www.martin-thoma.com/wordpress/*

3. Run the installation setup:
   1. Fill in your database information (database name, host, database user, database password)
   2. Store `wp-config.php` in your WordPress folder
   3. Make the most basic configuration of your blog (give it a title, create the admin account)

## Plugins

**Note: This list is from 2011 and very likely outdated. Please check for current alternatives.**

- [Akismet](http://akismet.com/): Protect your blog from spam. Don't forget to add your API key.
- [Sociable](http://wordpress.org/extend/plugins/sociable): A customizable link bar with icons to share posts on social networks.
- [SyntaxHighlighter Evolved](http://wordpress.org/extend/plugins/syntaxhighlighter/): A syntax highlighter. Essential if you write about code.
- [Twitter Tools](http://wordpress.org/extend/plugins/twitter-tools/): Creates complete integration between your WordPress blog and your Twitter account.
- [WordPress SEO by Yoast](http://wordpress.org/extend/plugins/wordpress-seo/): XML sitemap, Google/Bing Webmaster Tools integration.
- [WP-Piwik](http://wordpress.org/extend/plugins/wp-piwik/): Piwik is an open-source alternative to Google Analytics. Download the latest Piwik version [here](http://piwik.org/) and install it on your website. Don't forget to add your auth token.
## Configuration

1. Add the categories you want (Go to Posts → Categories)
2. Set your default category (Go to Settings → Writing)
3. Delete the "Hello World!" post
4. Delete the "Sample" page
5. Set a default category in Settings → Writing, then delete the "Uncategorized" category
6. Set up a custom theme. You can find free ones on [wordpress.org/extend/themes](http://wordpress.org/extend/themes)
7. Use [Permalinks](http://codex.wordpress.org/Using_Permalinks). I use `/%postname%/` for short URLs. This URL structure never changes.
## Fine-tuning

**www or non-www URL**: Decide whether you want www.martin-thoma.com or martin-thoma.com as your standard URL. Both should work, but one should redirect to the other. I chose martin-thoma.com because I prefer short URLs. Add this to your `.htaccess` if you want www.martin-thoma.com:

```apache
RewriteEngine on
RewriteCond %{HTTP_HOST} !^www.martin-thoma.com$
RewriteRule ^(.*)$ http://www.martin-thoma.com/$1 [R=301]
```

**Imprint**: In Germany, you must create an imprint. Even if you don't have to create one, I strongly recommend giving your readers the possibility to know who writes the posts. It gives you more credibility.

## Piwik

- [Piwik](http://piwik.org/)
- Login → Geolocation tab → follow the instructions

## Sources and Further Reading

- [Using Permalinks - Structure Tags](http://codex.wordpress.org/Using_Permalinks#Structure_Tags). Retrieved 17 September 2011.
- [SEO for WordPress – The Complete Guide](http://www.jimwestergren.com/seo-for-wordpress-blogs/). Retrieved 17 September 2011.
