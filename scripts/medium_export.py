#!/usr/bin/env python
"""Export Medium articles into this blog.

Writes content/YYYY-MM-DD-<slug>.md (with ``status: draft``) and downloads the images
to images/YYYY/MM/<slug>-<n>.<ext>, following the rules in AGENTS.md (front matter with
``medium_url``, <figure> markup, relative links to articles that are already on the blog).

Two sources for the posts:

* Medium's data export (recommended, no credentials):
  Medium → Settings → Security and apps → Download your information. Pass the ZIP file
  (or the unpacked folder) with ``--from-export``.
* Online, with the session cookies of your browser. Put them into
  scripts/medium_credentials.py (see medium_credentials.example.py).

Usage:

    uv run python scripts/medium_export.py list --from-export medium-export.zip
    uv run python scripts/medium_export.py list            # online, needs credentials
    uv run python scripts/medium_export.py export --missing --from-export medium-export.zip
    uv run python scripts/medium_export.py export https://martinthoma.medium.com/some-post-0123456789ab

``list`` prints the posts that are not on the blog yet and rewrites MEDIUM_EXPORT_TODO.md.
``export`` never overwrites an existing article.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import io
import json
import os
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
IMAGES = ROOT / "images"
TODO_FILE = ROOT / "MEDIUM_EXPORT_TODO.md"
TZ = ZoneInfo("Europe/Berlin")
MAX_DISPLAY_WIDTH = 800  # px; images are never shown wider than their pixel width
IMG_URL = "https://miro.medium.com/v2/resize:fit:{width}/{image_id}"
POST_ID_RE = re.compile(r"(?:-|/p/)([0-9a-f]{10,12})(?:[/?#]|$)")
TRACKING_PARAMS = {"source", "sk", "gi", "fbclid", "gclid", "ref", "ref_src"}

# Medium tags → blog tags (AGENTS.md: Title Case, merged spellings).
TAG_MAP = {
    "python": "Python",
    "python3": "Python",
    "programming": "Programming",
    "software-development": "Software Engineering",
    "software-engineering": "Software Engineering",
    "machine-learning": "Machine Learning",
    "data-science": "Data Science",
    "artificial-intelligence": "AI",
    "ai": "AI",
    "security": "Security",
    "cybersecurity": "Security",
    "infosec": "Security",
    "appsec": "AppSec",
    "testing": "Testing",
    "unit-testing": "Unit Testing",
    "pytest": "pytest",
    "javascript": "JavaScript",
    "web-development": "Web Development",
    "devops": "DevOps",
    "energy": "Energy",
    "climate-change": "Climate Change",
    "politics": "Politics",
    "chatgpt": "ChatGPT",
    "open-source": "Open Source",
}


# --------------------------------------------------------------------------- model


@dataclass
class Block:
    """One paragraph-level element, independent of the source format."""

    kind: str  # h2, h3, p, ul, ol, quote, code, img, card, embed, hr
    text: str = ""  # Markdown (already escaped) for text blocks; code for "code"
    items: list[str] = field(default_factory=list)  # list items (Markdown)
    lang: str = ""  # code block language
    image_id: str = ""  # Medium image id
    image_url: str = ""  # full URL (export) if no id is known
    width: int = 0
    height: int = 0
    href: str = ""  # card / embed target


@dataclass
class Post:
    post_id: str
    title: str
    url: str  # canonical URL without query
    published: dt.datetime | None
    subtitle: str = ""
    lang: str = ""
    tags: list[str] = field(default_factory=list)
    blocks: list[Block] = field(default_factory=list)
    is_draft: bool = False


# --------------------------------------------------------------------------- helpers


def rel(path: Path) -> Path:
    """Path relative to the repository, if possible (for messages)."""
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def card_text(markdown: str) -> str:
    """Text of a link card: no inner links, no trailing domain name (AGENTS.md)."""
    markdown = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    markdown = re.sub(r"\s+", " ", markdown).strip()
    return re.sub(r"\s*\b[\w-]+(\\?\.[\w-]+)*\\?\.(com|pub|org|io|net|de|dev|co)$", "", markdown)


def post_id_from_url(url: str) -> str | None:
    match = POST_ID_RE.search(url.split("?")[0] + "?")
    return match.group(1) if match else None


def clean_url(url: str) -> str:
    """Drop tracking parameters (AGENTS.md) and Medium's ?source=… suffixes."""
    parts = urlsplit(url)
    query = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.startswith("utm_") and k not in TRACKING_PARAMS
    ]
    return urlunsplit(parts._replace(query=urlencode(query)))


def escape_md(text: str) -> str:
    """Escape characters that Markdown or MathJax would interpret."""
    text = text.replace("\\", "\\\\")
    for char in "*_`[]":
        text = text.replace(char, "\\" + char)
    text = text.replace("$", "\\$")  # AGENTS.md: a literal dollar sign is \$
    return text.replace("<", "&lt;").replace(">", "&gt;")


def slugify(text: str) -> str:
    text = text.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "medium-post"


def guess_lang(text: str) -> str:
    words = re.findall(r"[a-zäöüß]+", text.lower())
    de = sum(w in {"und", "der", "die", "das", "ist", "nicht", "ich", "mit", "für"} for w in words)
    en = sum(w in {"the", "and", "is", "not", "with", "for", "you", "that", "this"} for w in words)
    return "de" if de > en else "en"


def plain(markdown: str) -> str:
    """Markdown → plain text (for alt texts)."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    text = re.sub(r"\\(.)", r"\1", text)
    return re.sub(r"[*`]", "", text).strip()


# --------------------------------------------------------------------------- blog index


@dataclass
class BlogIndex:
    by_post_id: dict[str, str]  # Medium post id → blog slug
    slugs: set[str]

    @classmethod
    def load(cls) -> BlogIndex:
        by_post_id: dict[str, str] = {}
        slugs: set[str] = set()
        for path in CONTENT.glob("*.md"):
            front = path.read_text(encoding="utf-8").split("---", 2)[1]
            slug = re.search(r"^slug:\s*(\S+)", front, re.M)
            if slug:
                slugs.add(slug.group(1))
            medium = re.search(r"^medium_url:\s*(\S+)", front, re.M)
            if medium and slug:
                post_id = post_id_from_url(medium.group(1))
                if post_id:
                    by_post_id[post_id] = slug.group(1)
        return cls(by_post_id, slugs)

    def rewrite_link(self, href: str) -> str:
        """Links to Medium posts that are already on the blog become ../slug/."""
        href = clean_url(href)
        host = urlsplit(href).netloc
        if "medium" in host or host.endswith((".pub", "gitconnected.com", "towardsdatascience.com")):
            post_id = post_id_from_url(href)
            if post_id in self.by_post_id:
                return f"../{self.by_post_id[post_id]}/"
        return href


# --------------------------------------------------------------------------- online source


class MediumClient:
    def __init__(self) -> None:
        creds = load_credentials()
        self.username = creds["username"]
        self.session = requests.Session()
        self.session.headers["User-Agent"] = creds["user_agent"] or "Mozilla/5.0"
        self.session.headers["Accept"] = "application/json"
        for name, value in creds["cookies"].items():
            if value:
                self.session.cookies.set(name, value, domain=".medium.com")

    def get_json(self, url: str) -> dict:
        response = self.session.get(url, timeout=30)
        if response.status_code == 403:
            sys.exit(
                f"403 from {url}\nCloudflare blocked the request. Update cf_clearance and "
                "USER_AGENT in scripts/medium_credentials.py (same browser), or use "
                "--from-export with Medium's data export."
            )
        response.raise_for_status()
        text = response.text
        return json.loads(text[text.index("{") :])  # strips the ])}while(1);</x> prefix

    def list_posts(self) -> list[Post]:
        """All published posts of the user, via Medium's GraphQL endpoint."""
        query = """
        query UserPosts($username: ID!, $from: String) {
          user(username: $username) {
            homepagePostsConnection(paging: {limit: 25, from: $from}) {
              posts { id title mediumUrl firstPublishedAt }
              pagingInfo { next { from } }
            }
          }
        }"""
        posts: list[Post] = []
        cursor = None
        while True:
            response = self.session.post(
                "https://medium.com/_/graphql",
                json={"query": query, "variables": {"username": self.username, "from": cursor}},
                timeout=30,
            )
            if response.status_code == 403:
                sys.exit("403 from medium.com/_/graphql: update the cookies or use --from-export.")
            response.raise_for_status()
            data = response.json()
            if "errors" in data:
                sys.exit(f"Medium's GraphQL API changed: {data['errors']}\nUse --from-export.")
            connection = data["data"]["user"]["homepagePostsConnection"]
            for item in connection["posts"]:
                published = item.get("firstPublishedAt")
                posts.append(
                    Post(
                        post_id=item["id"],
                        title=item["title"],
                        url=clean_url(item["mediumUrl"]),
                        published=dt.datetime.fromtimestamp(published / 1000, TZ) if published else None,
                    )
                )
            next_page = (connection.get("pagingInfo") or {}).get("next")
            if not next_page or not next_page.get("from"):
                return posts
            cursor = next_page["from"]

    def fetch_post(self, url: str, index: BlogIndex | None = None) -> Post:
        url = clean_url(url)
        data = self.get_json(url + ("&" if "?" in url else "?") + "format=json")
        return post_from_json(data, index)


def load_credentials() -> dict:
    creds = {"username": "martinthoma", "cookies": {}, "user_agent": ""}
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        import medium_credentials as module  # type: ignore[import-not-found]

        creds["username"] = getattr(module, "MEDIUM_USERNAME", creds["username"])
        creds["cookies"] = dict(getattr(module, "COOKIES", {}))
        creds["user_agent"] = getattr(module, "USER_AGENT", "")
    except ImportError:
        pass
    for name in ("sid", "uid", "cf_clearance"):
        env = os.environ.get(f"MEDIUM_{name.upper()}")
        if env:
            creds["cookies"][name] = env
    creds["user_agent"] = os.environ.get("MEDIUM_USER_AGENT", creds["user_agent"])
    if not creds["cookies"].get("sid"):
        sys.exit(
            "No Medium credentials. Copy scripts/medium_credentials.example.py to "
            "scripts/medium_credentials.py and fill it in, or use --from-export."
        )
    return creds


# Paragraph types in Medium's JSON (content.bodyModel.paragraphs[].type)
P, H2, H3, IMG, BQ, PQ, PRE, ULI, OLI, IFRAME, H4, MIXTAPE = 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14


def apply_markups(text: str, markups: list[dict], index: BlogIndex | None) -> str:
    """Insert Markdown for Medium's inline markups (strong, em, link, code)."""
    opens: dict[int, list[tuple[int, str]]] = {}
    closes: dict[int, list[tuple[int, str]]] = {}
    code_ranges: list[tuple[int, int]] = []
    for markup in markups:
        start, end = markup["start"], markup["end"]
        if start >= end:
            continue
        kind = markup["type"]
        if kind == 1:
            pair = ("**", "**")
        elif kind == 2:
            pair = ("*", "*")
        elif kind == 3 and markup.get("href"):
            href = index.rewrite_link(markup["href"]) if index else clean_url(markup["href"])
            pair = ("[", f"]({href})")
        elif kind == 10:
            pair = ("`", "`")
            code_ranges.append((start, end))
        else:
            continue
        # longer spans open first and close last, so the result nests
        opens.setdefault(start, []).append((end - start, pair[0]))
        closes.setdefault(end, []).append((end - start, pair[1]))
    out = []
    for i in range(len(text) + 1):
        for _, tag in sorted(closes.get(i, []), key=lambda x: x[0]):
            out.append(tag)
        for _, tag in sorted(opens.get(i, []), key=lambda x: -x[0]):
            out.append(tag)
        if i < len(text):
            in_code = any(s <= i < e for s, e in code_ranges)
            out.append(text[i] if in_code else escape_md(text[i]))
    return "".join(out)


def post_from_json(data: dict, index: BlogIndex | None = None) -> Post:
    value = data["payload"]["value"]
    references = data["payload"].get("references", {})
    paragraphs = value["content"]["bodyModel"]["paragraphs"]
    title = value["title"]
    subtitle = value["content"].get("subtitle", "")
    published = value.get("firstPublishedAt")
    post = Post(
        post_id=value["id"],
        title=title,
        url=clean_url(value.get("mediumUrl") or value.get("canonicalUrl") or ""),
        published=dt.datetime.fromtimestamp(published / 1000, TZ) if published else None,
        subtitle=subtitle,
        lang=value.get("detectedLanguage", "") or "",
        tags=[t["slug"] for t in value.get("virtuals", {}).get("tags", [])],
    )
    for number, para in enumerate(paragraphs):
        kind, text = para["type"], para.get("text", "")
        # the first paragraphs usually repeat title and subtitle
        if number < 2 and text.strip() in {title.strip(), subtitle.strip()} and kind in {H3, H4, H2, PQ}:
            continue
        markdown = apply_markups(text, para.get("markups", []), index)
        if kind in {H2, H3}:
            post.blocks.append(Block("h2", markdown))
        elif kind == H4:
            post.blocks.append(Block("h3", markdown))
        elif kind == P:
            post.blocks.append(Block("p", markdown))
        elif kind in {BQ, PQ}:
            post.blocks.append(Block("quote", markdown))
        elif kind == PRE:
            lang = (para.get("codeBlockMetadata") or {}).get("lang", "") or ""
            post.blocks.append(Block("code", text, lang=lang))
        elif kind in {ULI, OLI}:
            list_kind = "ul" if kind == ULI else "ol"
            if post.blocks and post.blocks[-1].kind == list_kind:
                post.blocks[-1].items.append(markdown)
            else:
                post.blocks.append(Block(list_kind, items=[markdown]))
        elif kind == IMG:
            meta = para.get("metadata", {})
            post.blocks.append(
                Block(
                    "img",
                    markdown,
                    image_id=meta.get("id", ""),
                    width=int(meta.get("originalWidth") or 0),
                    height=int(meta.get("originalHeight") or 0),
                )
            )
        elif kind == MIXTAPE:
            href = (para.get("mixtapeMetadata") or {}).get("href", "")
            href = index.rewrite_link(href) if index else clean_url(href)
            post.blocks.append(Block("card", card_text(apply_markups(text, [m for m in para.get("markups", []) if m["type"] != 3], None)), href=href))
        elif kind == IFRAME:
            resource_id = (para.get("iframe") or {}).get("mediaResourceId", "")
            resource = references.get("MediaResource", {}).get(resource_id, {})
            post.blocks.append(Block("embed", href=resource.get("href") or resource.get("iframeSrc", "")))
        else:
            print(f"warning: unknown paragraph type {kind} in {post.url}", file=sys.stderr)
            post.blocks.append(Block("p", markdown))
    if not post.lang:
        post.lang = guess_lang(" ".join(b.text for b in post.blocks))
    return post


# --------------------------------------------------------------------------- export source


def read_export(path: Path) -> list[tuple[str, str]]:
    """(file name, HTML) for every post in Medium's data export (ZIP or folder)."""
    files = []
    if path.is_dir():
        for file in sorted((path / "posts").glob("*.html")):
            files.append((file.name, file.read_text(encoding="utf-8")))
    else:
        with zipfile.ZipFile(path) as archive:
            for name in sorted(archive.namelist()):
                if re.match(r"(.*/)?posts/[^/]+\.html$", name):
                    files.append((Path(name).name, archive.read(name).decode("utf-8")))
    if not files:
        sys.exit(f"No posts/*.html found in {path}")
    return files


def inline_md(node: Tag | NavigableString, index: BlogIndex | None) -> str:
    if isinstance(node, NavigableString):
        return escape_md(str(node))
    name = node.name
    inner = "".join(inline_md(child, index) for child in node.children)
    if name in {"strong", "b"}:
        return f"**{inner}**" if inner.strip() else inner
    if name in {"em", "i"}:
        return f"*{inner}*" if inner.strip() else inner
    if name == "code":
        code = node.get_text()
        fence = "``" if "`" in code else "`"
        return f"{fence}{code}{fence}"
    if name == "a" and node.get("href"):
        href = index.rewrite_link(node["href"]) if index else clean_url(node["href"])
        return f"[{inner}]({href})"
    if name == "br":
        return "  \n"
    return inner


def post_from_export_html(file_name: str, page: str, index: BlogIndex | None = None) -> Post:
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find(class_="p-name")
    canonical = soup.find("a", class_="p-canonical")
    published = soup.find("time", class_="dt-published")
    subtitle = soup.find(class_="p-summary")
    url = clean_url(canonical["href"]) if canonical else ""
    post = Post(
        post_id=post_id_from_url(url) or post_id_from_url(file_name.replace(".html", "")) or file_name,
        title=title.get_text(strip=True) if title else file_name,
        url=url,
        published=dt.datetime.fromisoformat(published["datetime"].replace("Z", "+00:00")).astimezone(TZ)
        if published
        else None,
        subtitle=subtitle.get_text(" ", strip=True) if subtitle else "",
        is_draft=file_name.startswith("draft_"),
    )
    body = soup.find("section", attrs={"data-field": "body"}) or soup
    for graf in body.find_all(class_=re.compile(r"^(graf|section-divider)$")):
        classes = graf.get("class", [])
        if "section-divider" in classes:
            post.blocks.append(Block("hr"))
            continue
        if any(c in classes for c in ("graf--title", "graf--subtitle")):
            continue
        text = inline_md(graf, index).strip()
        if "graf--h3" in classes:
            post.blocks.append(Block("h2", text))
        elif "graf--h4" in classes:
            post.blocks.append(Block("h3", text))
        elif "graf--p" in classes:
            post.blocks.append(Block("p", text))
        elif "graf--blockquote" in classes or "graf--pullquote" in classes:
            post.blocks.append(Block("quote", text))
        elif "graf--pre" in classes:
            for br in graf.find_all("br"):
                br.replace_with("\n")
            post.blocks.append(Block("code", graf.get_text(), lang=graf.get("data-code-block-lang", "")))
        elif "graf--li" in classes:
            list_kind = "ol" if graf.parent and graf.parent.name == "ol" else "ul"
            if post.blocks and post.blocks[-1].kind == list_kind:
                post.blocks[-1].items.append(text)
            else:
                post.blocks.append(Block(list_kind, items=[text]))
        elif "graf--figure" in classes and graf.find("img"):
            img = graf.find("img")
            caption = graf.find("figcaption")
            post.blocks.append(
                Block(
                    "img",
                    inline_md(caption, index).strip() if caption else "",
                    image_id=img.get("data-image-id", ""),
                    image_url=img.get("src", ""),
                    width=int(img.get("data-width") or 0),
                    height=int(img.get("data-height") or 0),
                )
            )
        elif "graf--mixtapeEmbed" in classes:
            anchor = graf.find("a", class_=re.compile("mixtapeEmbed-anchor")) or graf.find("a")
            href = anchor["href"] if anchor and anchor.get("href") else ""
            href = index.rewrite_link(href) if index else clean_url(href)
            post.blocks.append(Block("card", card_text(inline_md(anchor, None) if anchor else escape_md(graf.get_text(" ", strip=True))), href=href))
        elif "graf--iframe" in classes or graf.find("iframe"):
            iframe = graf.find("iframe")
            post.blocks.append(Block("embed", href=(iframe.get("src") or iframe.get("data-src", "")) if iframe else ""))
    post.lang = guess_lang(" ".join(b.text for b in post.blocks))
    return post


# --------------------------------------------------------------------------- rendering


def download_image(block: Block, target_stem: Path) -> tuple[str, int, int]:
    """Download one image; returns (file name, width, height)."""
    width = block.width or 2000
    url = IMG_URL.format(width=min(width, 2000), image_id=block.image_id) if block.image_id else block.image_url
    response = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    content_type = response.headers.get("content-type", "")
    ext = {"image/png": ".png", "image/gif": ".gif", "image/webp": ".webp", "image/svg+xml": ".svg"}.get(
        content_type.split(";")[0], ".jpg"
    )
    path = target_stem.with_suffix(ext)
    path.write_bytes(response.content)
    if ext != ".svg":
        try:
            from PIL import Image

            with Image.open(io.BytesIO(response.content)) as image:
                block.width, block.height = image.size
        except Exception:  # noqa: BLE001 - keep the metadata from Medium
            pass
    if len(response.content) > 500_000:
        print(f"warning: {rel(path)} is larger than 500 KB (AGENTS.md)", file=sys.stderr)
    return path.name, block.width, block.height


def render(post: Post, slug: str, download: bool = True) -> str:
    while post.blocks and post.blocks[-1].kind == "hr":
        post.blocks.pop()
    while post.blocks and post.blocks[0].kind == "hr":
        post.blocks.pop(0)
    published = post.published or dt.datetime.now(TZ)
    year, month = f"{published:%Y}", f"{published:%m}"
    image_dir = IMAGES / year / month
    lines: list[str] = []
    image_number = 0
    for position, block in enumerate(post.blocks):
        if block.kind == "h2":
            lines += [f"## {block.text}", ""]
        elif block.kind == "h3":
            lines += [f"### {block.text}", ""]
        elif block.kind == "p" and block.text:
            lines += [block.text, ""]
        elif block.kind == "quote":
            lines += ["> " + block.text.replace("\n", "\n> "), ""]
        elif block.kind == "code":
            lines += [f"```{block.lang}", block.text.rstrip("\n"), "```", ""]
        elif block.kind in {"ul", "ol"}:
            marker = "*" if block.kind == "ul" else "1."
            lines += [f"{marker} {item}" for item in block.items] + [""]
        elif block.kind == "hr":
            lines += ["---" if lines else "", ""]
        elif block.kind == "card":
            lines += [f"[{block.text}]({block.href})", ""]
        elif block.kind == "embed":
            href = block.href
            youtube = re.search(r"(?:youtube\.com/(?:embed/|watch\?v=)|youtu\.be/)([\w-]{11})", href)
            if youtube:
                lines += [
                    f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{youtube.group(1)}" '
                    'title="YouTube video player" frameborder="0" allowfullscreen></iframe>',
                    "",
                ]
            else:
                lines += [f"TODO: Embedded content from Medium: <{href}>", ""]
        elif block.kind == "img":
            image_number += 1
            name = f"{slug}-{image_number}"
            if download and (block.image_id or block.image_url):
                image_dir.mkdir(parents=True, exist_ok=True)
                file_name, width, height = download_image(block, image_dir / name)
            else:
                file_name, width, height = f"{name}.jpg", block.width, block.height
            src = f"../images/{year}/{month}/{file_name}"
            shown_width = min(width or MAX_DISPLAY_WIDTH, MAX_DISPLAY_WIDTH)
            shown_height = round(height * shown_width / width) if width and height else 0
            alt = html.escape(plain(block.text), quote=True) or "TODO: alt text"
            size = f' width="{shown_width}" height="{shown_height}"' if shown_height else ""
            lazy = "" if position < 3 and image_number == 1 else ' loading="lazy"'
            figure = [
                "<figure>",
                f'    <a href="{src}"><img src="{src}" alt="{alt}"{size}{lazy}></a>',
            ]
            if block.text:
                figure.append(f"    <figcaption>{block.text}</figcaption>")
            lines += figure + ["</figure>", ""]
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"

    tags = []
    for tag in post.tags:
        mapped = TAG_MAP.get(tag, tag.replace("-", " ").title())
        if mapped not in tags:
            tags.append(mapped)
    category = "German posts" if post.lang == "de" else "Code"
    front = [
        "---",
        "layout: post",
        f"title: {post.title}",
        f"slug: {slug}",
        f"lang: {post.lang or 'en'}",
        "author: Martin Thoma",
        f"date: {published:%Y-%m-%d %H:%M}",
        f"category: {category}",
    ]
    if tags:
        front.append("tags: " + ", ".join(tags))
    if post.subtitle:
        front.append(f"summary: {post.subtitle}")
    front += [f"medium_url: {post.url}", "status: draft", "---"]
    return "\n".join(front) + "\n" + body


def export_post(post: Post, index: BlogIndex, download: bool = True) -> Path | None:
    if post.post_id in index.by_post_id:
        print(f"skip (already on the blog as {index.by_post_id[post.post_id]}): {post.title}")
        return None
    base = re.sub(r"-[0-9a-f]{10,12}$", "", urlsplit(post.url).path.rstrip("/").split("/")[-1])
    slug = slugify(base or post.title)
    if slug in index.slugs:
        slug = f"{slug}-medium"
    published = post.published or dt.datetime.now(TZ)
    path = CONTENT / f"{published:%Y-%m-%d}-{slug}.md"
    if path.exists():
        print(f"skip (file exists): {rel(path)}")
        return None
    path.write_text(render(post, slug, download), encoding="utf-8")
    index.slugs.add(slug)
    index.by_post_id[post.post_id] = slug
    print(f"wrote {rel(path)}")
    return path


# --------------------------------------------------------------------------- commands


def write_todo(missing: list[Post], source: str) -> None:
    lines = [
        "# Medium articles that are not on the blog yet",
        "",
        f"Generated by `scripts/medium_export.py list` from {source} on "
        f"{dt.date.today():%Y-%m-%d}. Export them with",
        "`uv run python scripts/medium_export.py export --missing …` (they are written as drafts),",
        "then review them (AGENTS.md: tags, links, images) and remove them from this list.",
        "",
        f"{len(missing)} articles:",
        "",
    ]
    for post in sorted(missing, key=lambda p: p.published or dt.datetime.min.replace(tzinfo=TZ)):
        date = f"{post.published:%Y-%m-%d}" if post.published else "????-??-??"
        lines.append(f"- [ ] {date} — [{post.title}]({post.url})")
    TODO_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {rel(TODO_FILE)}")


def load_posts(args: argparse.Namespace, index: BlogIndex) -> list[Post]:
    if args.from_export:
        posts = [post_from_export_html(name, page, index) for name, page in read_export(Path(args.from_export))]
        return [p for p in posts if not p.is_draft and p.url]
    return MediumClient().list_posts()


def cmd_list(args: argparse.Namespace) -> None:
    index = BlogIndex.load()
    posts = load_posts(args, index)
    missing = [p for p in posts if p.post_id not in index.by_post_id]
    print(f"{len(posts)} posts on Medium, {len(posts) - len(missing)} on the blog, {len(missing)} missing")
    for post in missing:
        print(f"  {post.published:%Y-%m-%d}  {post.title}  {post.url}" if post.published else f"  {post.title}")
    if not args.no_write:
        write_todo(missing, "Medium's data export" if args.from_export else f"medium.com/@{load_credentials()['username']}")


def cmd_export(args: argparse.Namespace) -> None:
    index = BlogIndex.load()
    if args.from_export:
        posts = {p.post_id: p for p in load_posts(args, index)}
        wanted = (
            [p for p in posts.values() if p.post_id not in index.by_post_id]
            if args.missing
            else [posts[i] for i in (post_id_from_url(u) for u in args.urls) if i in posts]
        )
        for post in wanted:
            export_post(post, index, download=not args.no_images)
        return
    client = MediumClient()
    urls = args.urls
    if args.missing:
        urls = [p.url for p in client.list_posts() if p.post_id not in index.by_post_id]
    for url in urls:
        export_post(client.fetch_post(url, index), index, download=not args.no_images)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("list", "export"):
        p = sub.add_parser(name)
        p.add_argument("--from-export", metavar="ZIP_OR_DIR", help="Medium's data export instead of the website")
    sub.choices["list"].add_argument("--no-write", action="store_true", help="don't rewrite MEDIUM_EXPORT_TODO.md")
    export = sub.choices["export"]
    export.add_argument("urls", nargs="*", help="Medium post URLs")
    export.add_argument("--missing", action="store_true", help="export all posts that are not on the blog yet")
    export.add_argument("--no-images", action="store_true", help="don't download images")
    args = parser.parse_args()
    if args.command == "export" and not args.urls and not args.missing:
        parser.error("export needs URLs or --missing")
    {"list": cmd_list, "export": cmd_export}[args.command](args)


if __name__ == "__main__":
    main()
