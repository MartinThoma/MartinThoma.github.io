#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://martin-thoma.com"
RELATIVE_URLS = True

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Drafts are only for local previews (pelicanconf-local.py); an empty SAVE_AS
# keeps them out of the published site.
DRAFT_SAVE_AS = ""
DRAFT_PAGE_SAVE_AS = ""
DRAFT_LANG_SAVE_AS = ""
DRAFT_PAGE_LANG_SAVE_AS = ""

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
