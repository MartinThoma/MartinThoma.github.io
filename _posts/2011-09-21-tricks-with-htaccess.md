---
layout: post
title: ! 'Tricks with .htaccess '
author: Martin Thoma
date: 2011-09-21 22:02:59.000000000 +02:00
category: Code
tags: htaccess, Apache
featured_image: 2011/09/Apache-Logo.png
---
If your Website is running on an Apache2 Webserver, you can change the behavior of this server with .htaccess-files. 

Here are some examples:

<h2>
Enable htaccess-files</h2>
Set <a href="http://httpd.apache.org/docs/2.0/mod/core.html#allowoverride" rel="nofollow">AllowOverride</a> to "All":
```bash
sudo gedit /etc/apache2/sites-available/default
```

Restart Apache:
```bash
sudo /etc/init.d/apache2 reload
```

<h2>
Enable ExpiresOn / mod_rewrite</h2>
This is for Ubuntu:
```bash
sudo a2enmod
rewrite expires
sudo /etc/init.d/apache2 restart

```

<h2>
Prevent or allow directory listing</h2>
Add the following line to your .htaccess-file to allow directory listing:
```bash
Options +Indexes
```
Add the following line to your .htaccess-file to prevent directory listing:
```bash
Options -Indexes
```

<h2>
Prevent Hot Linking</h2>
```bash
RewriteEngine on
RewriteCond %{HTTP_REFERER} !^$
RewriteCond %{HTTP_REFERER} !^http://(www.)?your-domain.com/.*$ [NC]
RewriteRule \.(gif|jpe?g|png)$ - [F]

```

<h2>
Prevent Direct Access</h2>
If you include some files with PHP, you might want that others can't access this file directly. So add the following to your .htaccess-file:
```bash
<FilesMatch "\.(inc)\.(php)$">
    Order deny,allow
    Deny from all
</FilesMatch>
<FilesMatch "\.(tpl)$">
    Order deny,allow
    Deny from all
</FilesMatch>

```
