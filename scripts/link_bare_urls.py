#!/usr/bin/env python3
"""Turn bare URLs in article text into links (see "Links" in AGENTS.md).

A URL that is shown as plain text is not clickable. This script makes every such URL
a link whose text is the URL without scheme, ``www.`` and trailing slash, shortened
when long (the style of ``[logotournament.com](http://logotournament.com/)``):

* ``[text](url)`` in Markdown text,
* ``<a href="url">text</a>`` inside raw HTML blocks (``<ul>``, ``<div>``, ``<table>``,
  ...), where Markdown is not processed,
* links to martin-thoma.com become relative (``../slug/``).

It leaves alone: code (fenced, indented, inline, ``<pre>``, ``<code>``), math, HTML
comments and attributes, existing links and autolinks (``<https://...>``). A URL that
is the subject of the text rather than a reference (an example domain, an API
endpoint) belongs in a code span; mark those by hand before running this.

Usage: ``python scripts/link_bare_urls.py [--dry-run] [files...]``
"""

import argparse
import html
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
MAX_LABEL = 50

# everything in which a URL is not shown as plain text
PROTECT_RE = re.compile(
    r"^(```|~~~).*?^\1[^\n]*$"                      # fenced code
    r"|<!--.*?-->"
    r"|<(pre|code|script|style|a)\b.*?</\2>"          # code, scripts, existing links
    r"|`[^`\n]*`"
    r"|\$\$.*?\$\$|(?<![\\$])\$[^$\n]+\$"             # math
    r"|!?\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)\s]*(?:\([^)\s]*\)[^)\s]*)*(?:\s+\"[^\"]*\")?\)"  # [..](..)
    r"|^ {0,3}\[(?!\^)[^\]]+\]:[ \t]*\S+.*$"          # reference definitions (not footnotes)
    r"|<(?:https?|ftp|mailto):[^>\s]+>"               # autolinks
    r"|<[^>]+>",                                      # tags with their attributes
    re.S | re.M | re.I,
)
CODE_RE = re.compile(
    r"^(```|~~~).*?^\1[^\n]*$|<!--.*?-->|<(pre|code|script|style)\b.*?</\2>|`[^`\n]*`", re.S | re.M | re.I
)
# an indented code block: 4+ spaces or a tab, after a blank line
INDENTED_RE = re.compile(r"(?:\A|(?<=\n\n))((?:(?: {4}|\t).*(?:\n|\Z))+)")
LIST_ITEM_RE = re.compile(r"(?m)^\s*(?:[*+-]|\d+\.)\s")
URL_RE = re.compile(r"(?<![\w/@.\-])(?:https?://|www\.)[^\s<>\"`\]\x00]+", re.I)
TRAILING = ".,:;!?*_'"
# query parameters that only track the click (see "Links" in AGENTS.md)
TRACKING_RE = re.compile(r"^(?:utm_\w+|fbclid|gclid|CMP|cfem|ref_src|si)$")
# blocks whose content Python-Markdown passes through as raw HTML
BLOCK_TAG_RE = re.compile(
    r"<(/?)(div|ul|ol|li|dl|dd|dt|table|thead|tbody|tr|td|th|p|blockquote|details|summary"
    r"|figure|figcaption|center|section|aside|h[1-6])\b[^>]*?(/?)>",
    re.I,
)


def clean(url):
    """Cut trailing punctuation and unbalanced closing parentheses off a match."""
    while url:
        if url[-1] in TRAILING:
            url = url[:-1]
        elif url[-1] == ")" and url.count(")") > url.count("("):
            url = url[:-1]
        else:
            break
    return url


def label(url):
    """Readable link text: host and path, with a short query (``?v=...``) kept."""
    parts = urlsplit(url if "://" in url else "https://" + url)
    host = parts.netloc.lower().removeprefix("www.")
    path = unquote(parts.path).rstrip("/")
    query = unquote(parts.query)
    text = host + path + (f"?{query}" if query and len(query) <= 20 else "")
    if len(text) <= MAX_LABEL:
        return text
    segments = path.strip("/").split("/")
    for shorter in (f"{host}/{segments[0]}/…/{'/'.join(segments[-2:])}", f"{host}/…/{segments[-1]}"):
        if len(segments) > 2 and len(shorter) <= MAX_LABEL:
            return shorter
    text = f"{host}/…/{segments[-1]}" if len(segments) > 1 else text
    return text if len(text) <= MAX_LABEL else text[: MAX_LABEL - 1] + "…"


def href(url):
    url = html.unescape(url)
    if not re.match(r"https?://", url, re.I):
        url = "https://" + url
    self_link = re.match(r"https?://(?:www\.)?martin-thoma\.com/(.*)", url, re.I)
    if self_link:
        url = "../" + self_link.group(1)
    base, _, query = url.partition("?")
    if query:
        query, _, fragment = query.partition("#")
        kept = [p for p in query.split("&") if p and not TRACKING_RE.match(p.split("=")[0])]
        url = base + ("?" + "&".join(kept) if kept else "") + (f"#{fragment}" if fragment else "")
    # parentheses would end a Markdown link target early
    return quote(url, safe=":/?#[]@!$&'*+,;=%~-._")


def in_raw_html(before):
    """True if the text ``before`` a position leaves a block-level HTML element open."""
    depth = 0
    for m in BLOCK_TAG_RE.finditer(CODE_RE.sub("", before)):
        if not m.group(3):  # not self-closing
            depth += -1 if m.group(1) else 1
    return depth > 0


def process(text):
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    head, body = (text[: m.end()], text[m.end() :]) if m else ("", text)
    saved = []

    def stash(value):
        saved.append(value)
        return f"\x00{len(saved) - 1}\x00"

    def restore(value):
        while "\x00" in value:
            value = re.sub(r"\x00(\d+)\x00", lambda mm: saved[int(mm.group(1))], value)
        return value

    def indented(mm):
        previous_block = mm.string[: mm.start()].rstrip("\n").rsplit("\n\n", 1)[-1]
        if LIST_ITEM_RE.search(previous_block):  # continuation of a list item, not code
            return mm.group(0)
        return stash(mm.group(0))

    # fenced code first: an indented block inside it must not swallow the closing fence
    masked = PROTECT_RE.sub(lambda mm: stash(mm.group(0)), body)
    masked = INDENTED_RE.sub(indented, masked)
    out, last, count = [], 0, 0
    for m in URL_RE.finditer(masked):
        url = clean(m.group(0))
        if "." not in url.split("//")[-1]:
            continue
        start = m.start()
        if in_raw_html(restore(masked[:start])):
            link = f'<a href="{html.escape(href(url))}">{html.escape(label(html.unescape(url)))}</a>'
        else:
            shown = re.sub(r"([\[\]_*\\])", r"\\\1", label(html.unescape(url)))
            link = f"[{shown}]({href(url)})"
        out.append(masked[last:start] + link)
        last = start + len(url)
        count += 1
    return head + restore("".join(out) + masked[last:]), count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    files = [Path(f) for f in args.files] or sorted((ROOT / "content").glob("*.md"))
    total = changed = 0
    for f in files:
        old = f.read_text(encoding="utf-8")
        new, n = process(old)
        if n:
            total += n
            changed += 1
            print(f"{n:3}  {f}")
            if not args.dry_run:
                f.write_text(new, encoding="utf-8")
    print(f"{total} bare URLs linked in {changed} files")


if __name__ == "__main__":
    main()
