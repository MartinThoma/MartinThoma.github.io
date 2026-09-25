"""Pelican plugin: write ``search.json``, the index for the search page.

One entry per published article (translations included) with what a result row
shows: title, URL, date, category, tags, featured image and the plain text. Figures,
styles and scripts are removed from the text, so excerpts do not start with image
credits or CSS. ``pelican-thoma/static/js/search.js`` reads the file.
"""

import html
import json
import os
import re

from bs4 import BeautifulSoup
from pelican import signals

NOT_TEXT = ["figure", "figcaption", "style", "script"]
# a space after these; inline elements (links, code) join their neighbours, so "619</a>."
# stays "619." and does not become "619 ."
BLOCKS = ["blockquote", "br", "dd", "div", "dt", "h1", "h2", "h3", "h4", "h5", "h6", "hr",
          "li", "p", "pre", "table", "td", "th", "tr"]


def plain_text(markup):
    soup = BeautifulSoup(markup, "html.parser")
    for element in soup(NOT_TEXT):
        element.decompose()
    for element in soup(BLOCKS):
        element.insert_after(" ")
    return " ".join(soup.get_text().replace("¶", " ").split())


def entry(article):
    return {
        "title": html.unescape(re.sub(r"<[^>]+>", "", article.title)).strip(),
        "url": article.url,
        "date": article.locale_date,
        "datetime": article.date.isoformat(),
        "category": article.category.name,
        "tags": [tag.name for tag in getattr(article, "tags", [])],
        "image": getattr(article, "featured_image", "") or "",
        "lang": article.lang,
        "text": plain_text(article.content),
    }


def write_index(generators):
    for generator in generators:
        if type(generator).__name__ != "ArticlesGenerator":
            continue
        articles = list(generator.articles)
        for article in generator.articles:
            articles.extend(article.translations)
        pages = [entry(a) for a in articles if a.status == "published"]
        path = os.path.join(generator.output_path, "search.json")
        os.makedirs(generator.output_path, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fd:
            json.dump({"pages": pages}, fd, ensure_ascii=False, separators=(",", ":"))


def register():
    signals.all_generators_finalized.connect(write_index)
