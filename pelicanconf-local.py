#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Martin Thoma'
SITENAME = u'Martin Thoma'
SITESUBTITLE = u'A blog about Code, the Web and Cyberculture'
SITEURL = '//127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'), )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/themoosemind'),
          ('Github', 'https://github.com/MartinThoma'),
          ('Stackoverflow',
           'http://stackoverflow.com/users/562769/martin-thoma'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '/home/moose/GitHub/pelican-themes/elegant'

DISQUS_SITENAME = "martinthoma"


ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

PLUGIN_PATHS = ['./pelican_plugin-render_math'
                # './pelican-bootstrapify',
                #                 './simple_footnotes',
                #                 './pelican-toc'
                ]
PLUGINS = ['pelican_plugin-render_math'
           # 'bootstrapify',
           #            'simple_footnotes',
           #            'toc'
           ]

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
# SUMMARY_MAX_LENGTH = 0
