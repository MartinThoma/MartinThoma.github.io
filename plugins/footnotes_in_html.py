"""Pelican plugin: footnote references ``[^label]`` everywhere, in reading order.

Python-Markdown does not parse raw HTML blocks (``<table>``, ``<ul>``, ``<figure>``),
so a ``[^1]`` in a table cell stayed literal text, and hand-written footnote links
there had no back link.

Before the inline patterns run, this walks the document in reading order and turns
every ``[^label]``, in Markdown text and in raw HTML blocks alike, into the markup
the footnotes extension creates. Each citation is registered with the extension:
the numbers follow the order of the first citations (with
``USE_DEFINITION_ORDER: False``), and a footnote cited several times gets one ↩ per
citation, the first ↩ pointing to the first citation.
"""

import re

from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import HTML_PLACEHOLDER_RE
from pelican import signals

FOOTNOTE_REF = re.compile(r"(?<!\\)\[\^([^\]]+)\]")
# In Markdown text: code spans are skipped, raw HTML blocks are rewritten.
TOKEN = re.compile(
    r"(?P<code>(?P<ticks>`+).+?(?P=ticks))"
    r"|(?<!\\)\[\^(?P<label>[^\]]+)\]"
    r"|" + HTML_PLACEHOLDER_RE.pattern.replace("([0-9]+)", "(?P<stash>[0-9]+)"),
    re.DOTALL,
)
CODE_BLOCK = re.compile(r'\s*<(pre|div class="(highlight|codehilite)")')


class FootnoteReferenceProcessor(Treeprocessor):
    def run(self, root):
        # `extra` bundles the footnotes extension, so there may be several instances;
        # the one whose inline pattern is registered holds the footnotes.
        if "footnote" not in self.md.inlinePatterns:
            return
        self.footnotes = self.md.inlinePatterns["footnote"].footnotes
        if not self.footnotes.footnotes:
            return
        self.stash = self.md.htmlStash.rawHtmlBlocks
        self.walk(root)

    def walk(self, element):
        """Rewrite the text of the tree in reading order."""
        if element.tag in ("pre", "code") or element.get("class") == "footnote":
            return
        if element.text:
            element.text = TOKEN.sub(self.markdown_token, element.text)
        for child in element:
            self.walk(child)
            if child.tail:
                child.tail = TOKEN.sub(self.markdown_token, child.tail)

    def markdown_token(self, m):
        if m.group("label"):
            html = self.reference(m.group("label"))
            return self.md.htmlStash.store(html) if html else m.group(0)
        if m.group("stash"):
            index = int(m.group("stash"))
            block = self.stash[index] if index < len(self.stash) else None
            if isinstance(block, str) and not CODE_BLOCK.match(block):
                self.stash[index] = FOOTNOTE_REF.sub(
                    lambda r: self.reference(r.group(1)) or r.group(0), block
                )
        return m.group(0)

    def reference(self, label):
        fn = self.footnotes
        if label not in fn.footnotes:
            return None
        fn.addFootnoteRef(label)
        if fn.getConfig("USE_DEFINITION_ORDER"):
            number = list(fn.footnotes).index(label) + 1
        else:
            number = fn.footnote_order.index(label) + 1
        return '<sup id="{}"><a class="footnote-ref" href="#{}">{}</a></sup>'.format(
            fn.makeFootnoteRefId(label, found=True),
            fn.makeFootnoteId(label),
            fn.getConfig("SUPERSCRIPT_TEXT").format(number),
        )


class FootnotesInHtmlExtension(Extension):
    def extendMarkdown(self, md):
        # after the footnotes div is built (50), before the inline patterns (20)
        md.treeprocessors.register(FootnoteReferenceProcessor(md), "footnotes_in_html", 25)


def add_extension(pelican):
    pelican.settings["MARKDOWN"].setdefault("extensions", []).append(FootnotesInHtmlExtension())


def register():
    signals.initialized.connect(add_extension)
