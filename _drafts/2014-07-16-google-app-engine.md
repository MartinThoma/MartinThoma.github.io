---
layout: post
title: Google App Engine
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
- Google
- App Engine
featured_image: logos/app-engine.png
---

While developing [write-math.com](http://write-math.com) with [knallhart.de](https://www.knallhart.de/) webhosting for only 2.40 Euro / month I stumbled over some limitations:

* I can execute only PHP, not Python
* I am limited to 30 seconds of execution time with PHP
* The MySQL database I am using cannot be exported, as it grew too big and I cannot use mysqldump but only phpMyAdmin.

So I decided to switch the MySQL server from Knallhart to Googles App Engine
service. Google App Engine is a <abbr title="Platfrom as a Service">PaaS</abbr>

## First steps

Download the [Google App Engine SDK](https://developers.google.com/appengine/downloads).

Install docker for Python:

```bash
$ sudo pip install docker-py
$ sudo pip install rpc
```

Then go to the extracted folder and execute the `run_tests.py`.

https://appengine.google.com/start

## PHP

<iframe width="512" height="288" src="//www.youtube.com/embed/Qt1_atU_Qsg" frameborder="0" allowfullscreen></iframe>

## Python

### Advanced
<iframe width="512" height="288" src="//www.youtube.com/embed/VPHHlnyoGfk" frameborder="0" allowfullscreen></iframe>

## Google Cloud SQL

<iframe width="512" height="384" src="//www.youtube.com/embed/_kQXgjIfLgo" frameborder="0" allowfullscreen></iframe>

## See also
* [Importing and Exporting Data](https://developers.google.com/cloud-sql/docs/import-export)
* [Google Cloud SQL: Relational Databases in Google's Cloud](https://developers.google.com/cloud-sql/)
* [Using Google Cloud SQL with App Engine](https://developers.google.com/appengine/docs/php/cloud-sql/)
* [Python Service APIs](https://developers.google.com/appengine/docs/python/apis)
* [Tips and Tricks for PHP on Google App Engine](https://gae-php-tips.appspot.com/2013/05/26/setting-up-phpmyadmin-on-app-engine/): Explains how to get phpMyAdmin for Google Cloud SQL

The book "Using Google App Engine" might also be good. I found an excerpt that