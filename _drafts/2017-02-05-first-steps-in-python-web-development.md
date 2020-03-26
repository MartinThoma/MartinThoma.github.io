---
layout: post
title: First steps in Python Web Development
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- Python
- Web Development
featured_image: logos/python.png
---

The following article will take you through the first steps in web development
with Python. You have to have an Apache 2 webserver running. I am using
Linux Mint (an Ubuntu derivate), so if you don't have that <abbr title="operating system">OS</abbr>
things might be different for you.

## Very first script
First, install the necessary Python module for Apache:

```bash
sudo apt-get install libapache2-mod-python
sudo service apache2 restart
```

Then modify `/etc/apache2/apache2.conf`:

```
<Directory /var/www/>
    Options Indexes FollowSymLinks Indexes
    AllowOverride All
    Require all granted
    AddHandler mod_python .py
    PythonHandler mod_python.publisher
    PythonDebug On
</Directory>
```

You can now create `/var/www/index.py` with the following content:

```
def index(req):
  return "Test successful"
```

If you see `Test successful` the test was successful. If you see `def ...` it
was not successful.

## Fix restart-error
This one is not so important and might not affect you. Some people get

```bash
sudo service apache2 restart
 * Restarting web server apache2
   AH00558: apache2: Could not reliably determine the server's fully
   qualified domain name, using 127.0.1.1. Set the 'ServerName' directive
   globally to suppress this message
```

To help apache to determine the server's fully quallified domain name, edit
`/etc/apache2/apache2.conf` and add `ServerName localhost`.


## DirectoryHandler

You might want to set up a `DirectoryHandler` so that `index.py` gets executed
when it's folder is called. To do so, add `index.py` to `/etc/apache2/mods-available/dir.conf`
and restart Apache with `sudo service apache2 restart`.

## Frameworks

There are a lot of frameworks for web development in Python:

* [Django](https://docs.djangoproject.com/) ([Wiki](https://en.wikipedia.org/wiki/Django_(web_framework))):
  High-level Python web development framework
  * [django-workshop.de](http://www.django-workshop.de/): A German Django tutorial.
* [Flask](http://flask.pocoo.org/) ([Wiki](https://en.wikipedia.org/wiki/Flask_(web_framework))):
  micro web framework based on Werkzeug, Jinja2 and good intentions
* [Pyramid](http://www.pylonsproject.org/) ([Wiki](https://en.wikipedia.org/wiki/Pylons_project#Pyramid)):
  Python web framework emphasizing flexibility and rapid development
  * [pylonsbook.com](http://pylonsbook.com/en/1.1/introducing-pylons.html)

Comparisons:
* [Django vs. Flask](http://www.reddit.com/r/Python/comments/1yr8v5/django_vs_flask/):
    Flask seem to have a bigger "fanbase", but Django is used more often in
    industry.
* [Django vs. Pylons (Pyramid)](http://stackoverflow.com/q/48681/562769)
*

I've found a great short answer on [stacktrace.ch](http://blog.stacktrace.ch/post/49178654214)
to the question when you should use which framework:

> Flask: One page app
> Django: CRUD app
> Pyramid: Unique app
> Plone: CMS

## Pyramid
### MWE
```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response("Hello %(name)s!" % request.matchdict)


if __name__ == "__main__":
    config = Configurator()
    config.add_route("hello", "/hello/{name}")
    config.add_view(hello_world, route_name="hello")
    app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 8080, app)
    server.serve_forever()
```

Source: [docs.pylonsproject.org](http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/firstapp.html)

## Flask

You might want to read [mod_wsgi (Apache)](http://flask.pocoo.org/docs/deploying/mod_wsgi/)
or [How To Deploy a Flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/articles/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
as soon as you want to deploy.
