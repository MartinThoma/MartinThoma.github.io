#!/usr/bin/env python3
"""Normalize image markup in content/*.md to the blog's figure convention.

Target markup (see "Images" in AGENTS.md)::

    <figure class="figure-right ai-generated">
        <a href="../images/2024/01/x.png"><img src="../images/2024/01/x.png" alt="..." width="512" height="300" loading="lazy"></a>
        <figcaption>Caption</figcaption>
    </figure>

What it does:

* rewrites ``<figure>`` blocks, standalone ``<img>``/``<a><img></a>`` lines,
  single images wrapped in ``<p>``/``<div>``/``<center>`` (Blogger's
  ``<div class="separator">``) and standalone Markdown images (``![alt](src)``)
  into that form,
* turns MediaWiki galleries (``<ul class="gallery">``), runs of consecutive
  image lines and runs of three or more figures with only blank lines between them
  into ``<div class="gallery">`` holding one figure per image; figures next to a
  gallery join it,
* strips WordPress and Bootstrap leftovers (``wp-*``, ``size-*``, ``align*``,
  ``img-thumbnail``, ``border-0``, ``text-center`` on captions, inline ``style``),
* turns ``style="width:512px"`` / ``max-width``/``max-height`` into
  ``width``/``height`` attributes (from the real image size),
* links every local image to its full-size file (no JavaScript needed).

Usage: ``python scripts/normalize_images.py [--dry-run] [files...]``
"""

import argparse
import html
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

ATTR_RE = re.compile(r"""([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""")
IMG_ATTRS = r"""(?:[^>"']|"[^"]*"|'[^']*')*"""
IMG_RE = re.compile(r"<img\b" + IMG_ATTRS + ">", re.I | re.S)
FIGURE_RE = re.compile(r"<figure\b([^>]*)>(.*?)</figure>", re.I | re.S)
FIGCAP_RE = re.compile(r"<figcaption\b[^>]*>(.*?)</figcaption>", re.I | re.S)
A_OPEN_RE = re.compile(r"<a\b([^>]*)>", re.I | re.S)
PROTECT_RE = re.compile(
    r"^(```|~~~).*?^\1[^\n]*$|<pre\b.*?</pre>|<!--.*?-->|`[^`\n]*`",
    re.S | re.M | re.I,
)
MD_IMG_RE = re.compile(
    r"^(?P<alt>.*?)\]\((?P<src>[^)\s]+)(?:\s+\"[^\"]*\")?\)(?:\*(?P<cap>.+)\*)?\s*$"
)
# a <p>, <div> or <center> at the start of a line whose only content is one (linked) image
WRAPPER_RE = re.compile(
    r"^[ \t]*<(p|div|center)\b[^>]*>\s*((?:<a\b[^>]*>\s*)?<img\b" + IMG_ATTRS + r">(?:\s*</a>)?)\s*</\1>",
    re.I | re.M,
)
MW_GALLERY_RE = re.compile(r'<ul class="gallery\b[^"]*"[^>]*>(.*?)</ul>', re.S)
MW_GALLERY_ITEM_RE = re.compile(r'<li class="gallerybox"[^>]*>(.*?)</li>', re.S)
MW_GALLERY_TEXT_RE = re.compile(r'<div class="gallerytext">(.*?)</div>', re.S)
STANDALONE_RE = re.compile(
    r"^ {0,3}(?:<a\b[^>]*>\s*)?<img\b" + IMG_ATTRS + r">(?:\s*</a>)?\s*$", re.I
)
# characters of text above the first image that still fit on the first screen
EAGER_TEXT_LIMIT = 1500
DROP_IMG_CLASS_RE = re.compile(r"^(wp-|size-|align|img-|text-center$|border-0$)")
# a figure or gallery at the start of a line, i.e. not indented inside another block
TOP_BLOCK_RE = re.compile(
    r'^<figure\b[^>]*>.*?</figure>|^<div class="gallery">\n.*?\n</div>', re.I | re.S | re.M
)
BLOCK_TAG_RE = re.compile(r"<(/?)(?:div|details|table|ul|ol|blockquote|section|aside)\b", re.I)
# this many figures in a row, without text between them, become a gallery
MIN_GALLERY_RUN = 3

stats = {"figures": 0, "standalone": 0, "imgs": 0, "galleries": 0, "warnings": []}


def parse_attrs(tag):
    return {m[1].lower(): html.unescape(m[2] if m[2] is not None else m[3]) for m in ATTR_RE.finditer(tag)}


def q(value):
    return html.escape(value, quote=True).replace("&#x27;", "'")


CURRENT_DIR = [CONTENT]


def local_path(src):
    if not is_local(src):
        return None
    src = src.split("?")[0].split("#")[0]
    m = re.match(r"\{(?:static|filename)\}/?(.*)", src)
    path = (CONTENT / m[1]) if m else (CURRENT_DIR[0] / src)
    return path.resolve() if path.is_file() else None


def svg_size(path):
    root = re.search(r"<svg\b[^>]*>", path.read_text(encoding="utf-8", errors="replace"), re.S)
    if not root:
        return None
    attrs = parse_attrs(root.group(0))
    w, h = (re.fullmatch(r"(\d+(?:\.\d+)?)(?:px)?", attrs.get(k, "")) for k in ("width", "height"))
    if w and h:
        return round(float(w[1])), round(float(h[1]))
    box = attrs.get("viewbox", "").replace(",", " ").split()
    return (round(float(box[2])), round(float(box[3]))) if len(box) == 4 else None


def natural_size(src):
    """(width, height) of a local image, or None."""
    path = local_path(src)
    if not path:
        return None
    if path.suffix.lower() == ".svg":
        return svg_size(path)
    try:
        from PIL import Image

        with Image.open(path) as im:
            w, h = im.size
            if im.getexif().get(0x0112, 1) in (5, 6, 7, 8):  # browsers apply EXIF rotation
                w, h = h, w
            return w, h
    except Exception:
        head = path.read_bytes()[:24]  # some PNGs Pillow rejects still have a valid header
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", head[16:24])
        return None


def px(style, prop):
    m = re.search(rf"(?<![\w-]){prop}\s*:\s*(\d+(?:\.\d+)?)px", style)
    return float(m[1]) if m else None


def target_size(attrs, nat, vector=False):
    """Displayed (width, height) or (width, None); None values if unknown."""
    style = attrs.get("style", "")
    w, h = px(style, "width"), px(style, "height")
    mw, mh = px(style, "max-width"), px(style, "max-height")
    if w is None and attrs.get("width", "").isdigit():
        w = float(attrs["width"])
        h = float(attrs["height"]) if attrs.get("height", "").isdigit() else h
    if w is None and (mw or mh):
        if nat:
            scale = min(1.0, (mw or 1e9) / nat[0], (mh or 1e9) / nat[1])
            w = nat[0] * scale
        elif mw:
            w = mw
    if w is None and nat:
        w = nat[0]
    if w is None:
        return (None, None)
    if nat:
        if not vector:
            w = min(w, nat[0])  # never upscale raster images: they turn blurry
        h = w * nat[1] / nat[0]
    return (round(w), round(h) if h else None)


def build_img(tag):
    attrs = parse_attrs(tag)
    src = attrs.get("src", "")
    nat = natural_size(src)
    w, h = target_size(attrs, nat, src.lower().endswith(".svg"))
    if is_pixel(attrs):
        # tracking pixels (VG Wort) must load eagerly and must not be styled
        return f'<img src="{q(src)}" alt="" width="1" height="1">', src, 1
    if not attrs.get("alt", "").strip():
        stats["warnings"].append(f"empty alt: {src}")
    out = [f'src="{q(src)}"', f'alt="{q(attrs.get("alt", ""))}"']
    if attrs.get("title") and attrs["title"] != attrs.get("alt"):
        out.append(f'title="{q(attrs["title"])}"')
    if w:
        out.append(f'width="{w}"')
        if h:
            out.append(f'height="{h}"')
    classes = [c for c in attrs.get("class", "").split() if not DROP_IMG_CLASS_RE.match(c)]
    if classes:
        out.append(f'class="{q(" ".join(classes))}"')
    out.append('loading="lazy"')
    stats["imgs"] += 1
    return "<img " + " ".join(out) + ">", src, w


def is_pixel(attrs):
    return attrs.get("width") == "1" and attrs.get("height") == "1"


def is_local(src):
    return not re.match(r"[a-z]+://|//|data:", src)


def figure_classes(attrs_str):
    classes = attrs_str and parse_attrs("<x " + attrs_str + ">").get("class", "") or ""
    out = []
    for c in classes.split():
        if c == "alignright":
            out.append("figure-right")
        elif c == "alignleft":
            out.append("figure-left")
        elif c in ("figure-left", "figure-right", "ai-generated", "ai-modified"):
            out.append(c)
    return out


def caption_html(text):
    return re.sub(r"\s+", " ", text).strip()


def render_figure(indent, classes, a_open, img_html, caption):
    cls = f' class="{" ".join(classes)}"' if classes else ""
    inner = f"{a_open}{img_html}</a>" if a_open else img_html
    lines = [f"<figure{cls}>", f"    {inner}"]
    if caption:
        lines.append(f"    <figcaption>{caption}</figcaption>")
    lines.append("</figure>")
    return ("\n" + indent).join(lines)


def link_open(a_match, src, w):
    """Return the <a ...> opening tag to use, or '' if none should wrap the image."""
    if a_match:
        attrs = parse_attrs(a_match.group(0))
        href = attrs.get("href")
        if href:
            return f'<a href="{q(href)}">'
    if is_local(src) and not (w and w < 64):
        return f'<a href="{q(src)}">'
    return ""


def rebuild_figure(match, before):
    body = match.group(2)
    imgs = IMG_RE.findall(body)
    if len(imgs) != 1 or "<table" in body.lower():
        stats["warnings"].append(f"figure with {len(imgs)} images left as is")
        return IMG_RE.sub(lambda m: build_img(m.group(0))[0], match.group(0))
    img_html, src, w = build_img(imgs[0])
    if w == 1:
        return img_html
    a_match = A_OPEN_RE.search(body[: body.index(imgs[0])])
    outer_a = re.search(r"<a\b[^>]*>\s*$", before)
    a_open = "" if outer_a else link_open(a_match, src, w)
    cap = FIGCAP_RE.search(body)
    line_start = before.rfind("\n") + 1
    indent = re.match(r"[ \t]*", before[line_start:]).group(0) if not before[line_start:].strip() else ""
    stats["figures"] += 1
    return render_figure(indent, figure_classes(match.group(1)), a_open, img_html, caption_html(cap.group(1)) if cap else "")


def md_links_to_html(text):
    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)


def strip_md_links(text):
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)


def standalone_to_figure(line):
    m = re.match(r"\s*(<a\b[^>]*>)?\s*(<img\b" + IMG_ATTRS + ">)", line, re.I)
    img_html, src, w = build_img(m.group(2))
    if w == 1:
        return img_html
    a_open = link_open(re.match(r"<a\b[^>]*>", m.group(1) or ""), src, w)
    classes = figure_classes(f'class="{parse_attrs(m.group(2)).get("class", "")}"')
    stats["standalone"] += 1
    return render_figure("", classes, a_open, img_html, "")


def markdown_image_to_figure(line):
    text = line.strip()
    if not text.startswith("!["):
        return None
    m = MD_IMG_RE.match(text[2:])
    if not m:
        return None
    alt, src, cap = m.group("alt"), m.group("src"), m.group("cap")
    has_link = bool(re.search(r"\[[^\]]*\]\([^)]*\)", alt))
    caption = md_links_to_html(cap) if cap else (md_links_to_html(alt) if has_link else "")
    alt_plain = strip_md_links(alt)
    if not alt_plain.strip():
        stats["warnings"].append(f"empty alt: {src}")
    tag = f'<img src="{q(src)}" alt="{q(alt_plain)}">'
    img_html, _, w = build_img(tag)
    a_open = link_open(None, src, w)
    stats["standalone"] += 1
    return render_figure("", [], a_open, img_html, caption)


def gallery_block(figures):
    lines = [f"    {line}" for figure in figures for line in figure.split("\n")]
    return "\n".join(['<div class="gallery">', *lines, "</div>"])


def group_figure_runs(body):
    """Turn figures that follow each other into a gallery.

    Only blank lines may separate them. A run of at least MIN_GALLERY_RUN figures becomes
    a gallery; figures next to a gallery join it. Galleries next to each other stay
    separate (they can be intended rows). Blocks nested in other elements (lists,
    tables, info boxes) are left alone.
    """
    saved = []

    def stash(match):
        saved.append(match.group(0))
        return f"\x00c{len(saved) - 1}\x00"

    text = PROTECT_RE.sub(stash, body)

    def nesting(pos):
        return sum(-1 if m.group(1) else 1 for m in BLOCK_TAG_RE.finditer(text, 0, pos))

    def canonical(figure):
        # floats make no sense inside the grid; inner lines get one level of indentation
        figure = re.sub(r"\s*\bfigure-(?:left|right)\b", "", figure, count=1)
        figure = re.sub(r'\s*class="\s*"', "", figure, count=1)
        lines = [line.strip() for line in figure.strip().split("\n") if line.strip()]
        return "\n".join(line if line.startswith(("<figure", "</figure")) else "    " + line for line in lines)

    items = []  # (match, figures, is_gallery)
    for m in TOP_BLOCK_RE.finditer(text):
        block = m.group(0)
        if nesting(m.start()) > 0:
            continue
        if block.startswith("<div"):
            figures = [f.group(0) for f in FIGURE_RE.finditer(block)]
            items.append((m, figures, True))
        elif "<img" in block and not re.search(r"<(?:iframe|video|audio)\b", block):
            items.append((m, [block], False))

    runs = []
    for item in items:
        if runs and not text[runs[-1][-1][0].end() : item[0].start()].strip():
            runs[-1].append(item)
        else:
            runs.append([item])
    for run in reversed(runs):
        figures = [f for _, figs, _ in run for f in figs]
        has_gallery = any(is_gallery for _, _, is_gallery in run)
        loose = sum(not is_gallery for _, _, is_gallery in run)
        if not loose or (not has_gallery and len(figures) < MIN_GALLERY_RUN):
            continue  # galleries next to each other stay separate: rows can be intended
        block = gallery_block([canonical(f) for f in figures])
        text = text[: run[0][0].start()] + block + text[run[-1][0].end() :]
        stats["galleries"] += 1
    return re.sub(r"\x00c(\d+)\x00", lambda m: saved[int(m.group(1))], text)


def convert_mw_gallery(match):
    figures = []
    for item in MW_GALLERY_ITEM_RE.finditer(match.group(1)):
        item = item.group(1)
        img = IMG_RE.search(item)
        a = A_OPEN_RE.search(item[: img.start()])
        cap = MW_GALLERY_TEXT_RE.search(item)
        inner = f"{a.group(0)}{img.group(0)}</a>" if a else img.group(0)
        caption = f"<figcaption>{cap.group(1)}</figcaption>" if cap and cap.group(1).strip() else ""
        figures.append(f"<figure>{inner}{caption}</figure>")
    return gallery_block(figures)


def convert_wrapper(match):
    figure = standalone_to_figure(match.group(2))
    followed_by_text = re.match(r"\n[^\n]", match.string[match.end() :])
    return figure + ("\n" if followed_by_text else "")


def line_to_figure(line):
    if STANDALONE_RE.match(line):
        return standalone_to_figure(line)
    return markdown_image_to_figure(line)


def process_lines(text):
    lines = text.split("\n")
    out = []
    depth = 0  # inside table / ul / ol
    n = len(lines)

    def is_imgline(i):
        return 0 <= i < n and (
            bool(STANDALONE_RE.match(lines[i])) or lines[i].startswith("![")
        )

    i = 0
    while i < n:
        line = lines[i]
        low = line.lower()
        end = i + 1
        new = None
        if depth == 0 and is_imgline(i):
            while is_imgline(end):
                end += 1
            figures = [line_to_figure(lines[k]) for k in range(i, end)]
            if None in figures:
                end = i + 1
            elif len(figures) == 1:
                new = figures[0]
            else:
                new = gallery_block(figures)
        if new is not None:
            if out and out[-1].strip():
                out.append("")
            out.append(new)
            if end < n and lines[end].strip():
                out.append("")
        else:
            out.extend(lines[i:end])
        depth += len(re.findall(r"<(?:table|ul|ol)\b", low)) - len(re.findall(r"</(?:table|ul|ol)>", low))
        depth = max(depth, 0)
        i = end
    return "\n".join(out)


def process(text):
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    head, body = (text[: m.end()], text[m.end() :]) if m else ("", text)

    saved = []

    def stash(prefix):
        def inner(match):
            saved.append(match.group(0))
            return f"\x00{prefix}{len(saved) - 1}\x00"

        return inner

    body = PROTECT_RE.sub(stash("c"), body)
    body = MW_GALLERY_RE.sub(convert_mw_gallery, body)
    body = WRAPPER_RE.sub(convert_wrapper, body)

    # figures first; each result is stashed so later passes leave it alone
    def fig_repl(match):
        result = rebuild_figure(match, match.string[: match.start()])
        saved.append(result)
        return f"\x00f{len(saved) - 1}\x00"

    body = FIGURE_RE.sub(fig_repl, body)
    body = process_lines(body)

    def stash_new_figures(text_):
        return FIGURE_RE.sub(lambda mm: (saved.append(mm.group(0)), f"\x00f{len(saved) - 1}\x00")[1], text_)

    body = stash_new_figures(body)

    def img_repl(match):
        img_html, src, w = build_img(match.group(0))
        before = match.string[: match.start()]
        if re.search(r"<a\b[^>]*>\s*$", before) or not is_local(src) or (w and w < 64):
            return img_html
        return f'<a href="{q(src)}">{img_html}</a>'

    body = IMG_RE.sub(img_repl, body)

    while "\x00" in body:
        new = re.sub(r"\x00[cf](\d+)\x00", lambda mm: saved[int(mm.group(1))], body)
        if new == body:
            break
        body = new
    return head + eager_first_image(group_figure_runs(body))


def eager_first_image(body):
    """Drop loading="lazy" from the first image if it is likely on the first screen.

    That image is usually the Largest Contentful Paint; lazy-loading it delays it.
    """
    code = [m.span() for m in PROTECT_RE.finditer(body)]
    for m in IMG_RE.finditer(body):
        if any(a <= m.start() < b for a, b in code) or 'loading="lazy"' not in m.group(0):
            continue
        text = re.sub(r"<[^>]+>|\]\([^)]*\)", "", body[: m.start()])
        if len(re.sub(r"\s+", " ", text).strip()) > EAGER_TEXT_LIMIT:
            return body
        return body[: m.start()] + m.group(0).replace(' loading="lazy"', "") + body[m.end() :]
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    files = [Path(f) for f in args.files] or sorted(CONTENT.rglob("*.md"))
    changed = 0
    for f in files:
        CURRENT_DIR[0] = f.resolve().parent
        old = f.read_text(encoding="utf-8")
        if "<img" not in old and "![" not in old:
            continue
        new = process(old)
        if new != old:
            changed += 1
            if not args.dry_run:
                f.write_text(new, encoding="utf-8")
    print(f"changed {changed} files; {stats['figures']} figures rebuilt, "
          f"{stats['standalone']} standalone images wrapped, {stats['imgs']} <img> tags written, "
          f"{stats['galleries']} figure runs grouped into galleries")
    for w in sorted(set(stats["warnings"])):
        print("WARN", w, file=sys.stderr)


if __name__ == "__main__":
    main()
