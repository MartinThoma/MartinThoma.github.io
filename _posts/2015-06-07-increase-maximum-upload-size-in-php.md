---
layout: post
title: Increase the maximum file upload size in PHP
author: Martin Thoma
date: 2015-06-07 09:13
categories:
- Cyberculture
tags:
- PHP
- apache
featured_image: logos/php.png
---

Create a `test.php` with the following content to check your current maximum
upload size.

```php
<?php phpinfo(); ?>
```

Search your `php.ini` in the Apache folder:

```bash
$ find /etc -name 'php.ini'
/etc/php5/cli/php.ini
/etc/php5/apache2/php.ini
```

Edit it. Set `upload_max_filesize` and `post_max_size` to whatever you want.

Restart the server with

```bash
$ sudo service apache2 restart
```