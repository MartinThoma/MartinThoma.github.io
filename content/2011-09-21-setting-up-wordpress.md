---
layout: post
lang: en
title: Setting up WordPress
author: Martin Thoma
date: 2011-09-21 19:36:18.000000000 +02:00
category: The Web
tags: WordPress
featured_image: 2011/09/WordPress-Logo.png
---
This article is about creating a new WordPress blog. This includes installing and basic customization.

You need to know how how to upload files and how your MySQL database credentials.

I used almost the same setup and I will update this post if I make some bad experiences with it.

<h2>Requirements</h2>
<h3>Minimum</h3>
Webserver with:
<ul>
	<li>MySQL 5.0 or higher</li>
	<li>PHP 5.2.4 or higher</li>
	<li>10 MB free space</li>
	<li>Any possibility to upload files</li>
</ul>
<h3>Recommended</h3>
<ul>
	<li>The <a href="http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html">mod_rewrite</a> Apache module.</li>
	<li>An FTP-Client (e.g. FileZilla)</li>
</ul>
<h2>Installation</h2>
<ol>
	<li>Download the latest version from <a href="http://wordpress.org/download/">wordpress.org</a></li>
	<li>Decompress it and submit it to your Webserver. It should be directly in your working directory.
<small>Example: Use www.martin-thoma.com, not www.martin-thoma.com/wordpress/</small></li>
	<li>Run the installation setup
<ol>
	<li>Fill in your database information
<small>(database name, host, database user, database password)</small></li>
	<li>Store <span class="inline-file">wp-config.php</span> in your WordPress-Folder.</li>
	<li>Make the most basic configuration of your blog
<small>(give it a title, create the admin account)</small></li>
</ol>
</li>
</ol>
<h2>Plugins</h2>
<ol>
<ul>
	<li><a href="http://akismet.com/">Akismet</a>: Protect your blog from spam. Don't forget to add your API Key.</li>
	<li><a href="http://wordpress.org/extend/plugins/sociable">Sociable</a>: A little, customizable link bar with icons to share the post on social networks. I miss Google+ ☹</li>
	<li><a href="http://wordpress.org/extend/plugins/syntaxhighlighter/">SyntaxHighlighter Evolved</a>: A syntax highlighter. Absolutely necessary, if you want to write about code. If you don't write about code, you don't need it.</li>
	<li><a href="http://wordpress.org/extend/plugins/twitter-tools/">Twitter Tools</a>: a plugin that creates a complete integration between your WordPress blog and your Twitter account.</li>
	<li><a href="http://wordpress.org/extend/plugins/wordpress-seo/">WordPress SEO by Yoast</a>: XML-Sitemap, binding for Google/Bing Webmaster Tools</li>
	<li><a href="http://wordpress.org/extend/plugins/wp-piwik/">WP-Piwik</a>: Piwik is an OpenSource alternative to Google Analytics. You can get some information about your readers.
Download the latest Piwik-Version <a href="http://piwik.org/">here</a> and install it on your Website. Don't forget to add your Auth token.</li>
</ul>
</ol>
<h2>Configuration</h2>
<ol>
<ol>
	<li>Add the categories you want.
<small>Go to Posts &rarr; Categories</small></li>
	<li>Set your default category.
<small>Go to Settings &rarr; Writing</small></li>
	<li>Delete the "Hello World!" post.</li>
	<li>Delete "Sample" page.</li>
	<li>Set a default category in Settings &rarr; Writing. Then delete the category "Uncategorized".</li>
	<li>Set up a custom theme. You can find free ones on <a href="http://wordpress.org/extend/themes">wordpress.org/extend/themes</a>.</li>
	<li>Use <a href="http://codex.wordpress.org/Using_Permalinks">Permalinks</a>. I use <span class="inline-code">/%postname%/</span> as I want short URLs. Another plus of this URL is that the URL never changes.</li>
</ol>
</ol>
<h2>Finetuning</h2>
<strong>www or non-www-URL</strong>: decide if you want www.martin-thoma.com or martin-thoma.com as your standard URL. Both should work, but one should redirect the user to the other. I choose to take martin-thoma.com as I like short URLs. Add this to your .htaccess if you want www.martin-thoma.com:

```bash
RewriteEngine on
RewriteCond %{HTTP_HOST} !^www.martin-thoma.com$
RewriteRule ^(.*)$ http://www.martin-thoma.com/$1 [R=301]
```


<strong>Imprint</strong>: In Germany, you have to create an imprint. Even if you don't have to create one, I strongly recommend giving your readers the possibility to get to know who writes the posts. It gives you more credibility.

<h2>Piwik</h2>
<ul>
  <li><a href="http://piwik.org/">Piwik</a></li>
  <li>Login &rarr; Geolocation tab &rarr; follow the instructions</li>
</ul>

<h2>Sources and further reading</h2>
<ul>
	<li><a href="http://codex.wordpress.org/Using_Permalinks#Structure_Tags">Using Permalinks - Structure Tags.</a> Retrieved 17 September 2011.</li>
	<li><a href="http://www.jimwestergren.com/seo-for-wordpress-blogs/">SEO for WordPress &ndash; The Complete Guide.</a> Retrieved 17 September 2011.</li>
</ul>
