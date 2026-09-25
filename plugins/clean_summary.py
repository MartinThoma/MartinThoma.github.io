"""Pelican plugin: build the article summary from the article text only.

Pelican truncates the article HTML to ``SUMMARY_MAX_LENGTH`` words and the templates
strip the tags. The text of figure captions, ``<style>`` and ``<script>`` blocks
stays, so previews showed "Mit Claude AI generierte Illustration: …" or
".good { background-color: #ccffcc; }". This plugin removes those elements before
truncating. An explicit ``summary`` in the front matter is left alone.
"""

import re

from pelican import signals
from pelican.contents import Article, Page
from pelican.utils import truncate_html_paragraphs, truncate_html_words

NOT_TEXT = re.compile(r"<(figure|figcaption|style|script)\b[^>]*>.*?</\1\s*>", re.S | re.I)


def clean_summary(content):
    if not isinstance(content, (Article, Page)) or "summary" in content.metadata:
        return
    settings = content.settings
    summary = NOT_TEXT.sub("", content._content or "")
    if settings.get("SUMMARY_MAX_PARAGRAPHS") is not None:
        summary = truncate_html_paragraphs(summary, settings["SUMMARY_MAX_PARAGRAPHS"])
    if settings["SUMMARY_MAX_LENGTH"] is not None:
        summary = truncate_html_words(
            summary, settings["SUMMARY_MAX_LENGTH"], settings["SUMMARY_END_SUFFIX"]
        )
    content.metadata["summary"] = summary
    content._summary = summary


def register():
    signals.content_object_init.connect(clean_summary)
