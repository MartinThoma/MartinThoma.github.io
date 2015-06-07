---
layout: post
title: Execute Python on Apache2
author: Martin Thoma
date: 2015-02-01 15:11
categories:
- Code
tags:
- Python
- Apache
featured_image: logos/python.png
---

I have to run a very simple Python script on an Apache2 web server. These were
the steps with which I made it work:

## Find the Apache2 config

```bash
$ /usr/sbin/apache2 -V
```

It is in `/etc/apache2/apache2.conf`


## Add CGI

Somewhere in the `/etc/apache2/apache2.conf` there is a `<Directory ...>` part.
I've added `Options ExecCGI` and `AddHandler cgi-script .py`. Now this part
looks like this:

```text
<Directory /var/www/>
    Options Indexes FollowSymLinks ExecCGI
    AddHandler cgi-script .py
    AllowOverride None
    Require all granted
</Directory>
```


## Test it

Create the following `test.py` file:

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print("Content-Type: text/html\n")
print("Hello World! The answer to live, the universe and everything is %i." %
      (2*21))

```

Now call `http://localhost/test.py`.

If that doesn't work, take a look at the apache log files:

```bash
$ tail -f /var/log/apache2/error.log
```