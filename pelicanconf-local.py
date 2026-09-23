#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Martin Thoma"
SITENAME = "Martin Thoma"
SITESUBTITLE = "A blog about Code, the Web and Cyberculture"
SITEURL = "http://127.0.0.1:8000"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_RSS = "feeds/index.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
FEED_USE_SUMMARY = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
READERS = {"html": None, "htm": None}

# Blogroll
LINKS = (("Pelican", "https://blog.getpelican.com/"),)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/_martinthoma"),
    ("Email", "mailto:info@martin-thoma.de"),
    ("Github", "https://github.com/MartinThoma"),
    ("Stackoverflow", "http://stackoverflow.com/users/562769/martin-thoma"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "./pelican-thoma"
PYGMENTS_STYLE = "tango"  # Syntax highlighting theme
CUSTOM_CSS = "static/custom.css"


ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
ARTICLE_LANG_URL = "{slug}/"
ARTICLE_LANG_SAVE_AS = "{slug}/index.html"
AUTHOR_URL = "author/{slug}/"
# The author page is content/author/martin-thoma/index.md. A generated author
# listing would be written to author/martin-thoma.html and shadow it on
# servers that prefer "<path>.html" over "<path>/index.html" (pelican --listen).
AUTHOR_SAVE_AS = ""
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"
SEARCH_URL = "search/"
SEARCH_SAVE_AS = "search/index.html"

PLUGIN_PATHS = [
    "./pelican_plugin-render_math",
    "./pelican-tipue_search",
    "./pelican-toc",
    "./pelican-sitemap",
    # './pelican-bootstrapify',
    # './simple_footnotes',
]
PLUGINS = [
    "pelican_plugin-render_math",
    "tipue_search",
    "toc",
    "sitemap",
    "pelican_alias",
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.footnotes": {},
    },
    "output_format": "html5",
}
MATH_JAX = {"auto_insert": False}

SITEMAP = {
    "exclude": ["tag/", "category/", "tags/", "archives/", "categories/", "search/"],
    "format": "xml",
}

TOC = {"TOC_HEADERS": "^h[2-3]", "TOC_RUN": "true", "TOC_INCLUDE_TITLE": False}

DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")

ARTICLE_EXCLUDES = ["html5", "js", "python", "pdf"]
PAGE_EXCLUDES = ["html5", "js", "python", "pdf"]

STATIC_PATHS = [
    "images",
    "extra/CNAME",
    "extra/custom.css",
    "extra/print.css",
    "extra/favicon.ico",
    "extra/opensearch.xml",
    "pdf",
    "anki",
    "audio",
    "html5",
    "js",
    "python",
]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/print.css": {"path": "static/print.css"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/opensearch.xml": {"path": "opensearch.xml"},
}
OUTPUT_PATH = "/var/www/blog/"
# SUMMARY_MAX_LENGTH = 0
