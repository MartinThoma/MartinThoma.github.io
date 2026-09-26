#!/usr/bin/env python3
"""Check content/*.md against the rules in AGENTS.md and report problems.

Source checks (the Markdown files):

* front matter: slug format and uniqueness, no ``url:``, ``lang`` and the
  "German posts" category, tag spelling, banned tags and the tag hierarchy,
  featured image exists
* links: own articles linked absolutely or via Medium, internal links that do not
  resolve, tracking parameters
* images: file exists, ``width``/``height``, alt text, Markdown images, inline
  style, WordPress classes, hotlinks, files over 500 KB, shown wider than the file
* math: ``\\(``/``\\[`` in Markdown, whitespace before a closing ``$``, function
  names without backslash
* text: doubled words, space before punctuation, lowercase "i" in English

Output checks (``output/``, run ``make html-local`` first): Markdown that was not
rendered and ``$`` that MathJax would read as math.

Usage: ``uv run python scripts/check_articles.py [--drafts] [--only CHECK,...] [files...]``
Exit code 1 if something was found.
"""

import argparse
import html
import re
import struct
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUTPUT = ROOT / "output"
IMAGES = ROOT / "images"

MAX_IMAGE_BYTES = 500 * 1024

BANNED_TAGS = {
    "Code", "German posts", "Cyberculture", "Rating", "C++", "Clip", "Shortfilm",
    "My bits and bytes", "Machine Learning Category",
}
# old spelling -> tag to use (AGENTS.md "Merged tags" and case variants)
MERGED_TAGS = {
    "IT-Security": "Security", "IT Security": "Security", "InfoSec": "Security",
    "Cybersecurity": "Security", "CyberSecurity": "Security", "security": "Security",
    "cpp": "CPP", "A.I.": "AI", "Artificial Intelligence": "AI", "Politik": "Politics",
    "Software Development": "Software Engineering", "Development": "Software Engineering",
    "foss": "Open Source", "OpenSource": "Open Source", "Bug": "Bugs", "bug": "Bugs",
    "Reviews": "Review", "finances": "Money", "datastructure": "Data Structures",
    "data structure": "Data Structures", "mathematics": "Mathematics", "diy": "DIY",
    "do-it-yourself": "DIY", "git": "Git",
}
LOWERCASE_TAGS = {"gedit", "itertools", "scikit-learn", "pytest", "mypy", "tox", "venv", "virtualenv", "arXiv", "jq", "nox", "pip", "iPhone", "macOS", "npm", "eBay", "pandas"}
# child -> parents that must be present too (transitively, see AGENTS.md "Hierarchy")
TAG_PARENTS = {
    "Matrix": ["Linear Algebra"], "Linear Algebra": ["Mathematics"], "Analysis": ["Mathematics"],
    "Flask": ["Python"], "Neural Networks": ["Machine Learning"], "Machine Learning": ["AI"],
    "Klausur": ["University"],
}
TRACKING = re.compile(
    r"[?&](?:utm_[a-z]+|fbclid|gclid|mc_cid|mc_eid|igshid|ref_src|ref_url|si)=|amazon\.[a-z.]+/[^\s)\"']*/ref=",
    re.I,
)
MATH_FUNCTIONS = ["sin", "cos", "tan", "log", "ln", "exp", "max", "min", "det", "gcd", "lim", "arg", "rank", "sup", "inf"]
FUNC_RE = re.compile(r"(?<![\\a-zA-Z{])(" + "|".join(MATH_FUNCTIONS) + r")(?=\s*[({_^\s\\]|\s*[a-z]\b)")

# words allowed twice in a row ("that that", "had had", German "die die" ...)
DOUBLE_OK = {"that", "had", "is", "die", "das", "der", "sie", "the", "i", "a", "can", "0", "1", "ha", "bye", "no"}


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body, offset = {}, text, 0
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end:
            for line in lines[1:end]:
                m = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
                if m:
                    meta[m.group(1)] = m.group(2).strip()
            body = "\n".join(lines[end + 1:])
            offset = end + 1
    return meta, body, offset


def prose(body):
    """The body with code, comments, scripts, styles and math removed (same line count)."""
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    s = re.sub(r"(?ms)^(\s*)(```|~~~).*?^\s*\2[^\n]*$", blank, body)
    s = re.sub(r"(?s)<(pre|code|script|style|textarea)\b.*?</\1>", blank, s)
    s = re.sub(r"(?s)<!--.*?-->", blank, s)
    s = re.sub(r"`[^`\n]+`", blank, s)
    return s


def without_math(s):
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    s = re.sub(r"(?s)\$\$.*?\$\$", blank, s)
    s = re.sub(r"(?s)\\begin\{(\w+\*?)\}.*?\\end\{\1\}", blank, s)
    s = re.sub(r"(?<![\\$])\$(?!\$)[^$\n]+?(?<!\\)\$", blank, s)
    return s


def image_size(path):
    try:
        with open(path, "rb") as f:
            head = f.read(64 * 1024)
    except OSError:
        return None
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", head[16:24])
    if head[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", head[6:10])
    if head[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(head):
            if head[i] != 0xFF:
                i += 1
                continue
            marker = head[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", head[i + 5:i + 9])
                return w, h
            i += 2 + struct.unpack(">H", head[i + 2:i + 4])[0]
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP" and head[12:16] == b"VP8X":
        return int.from_bytes(head[24:27], "little") + 1, int.from_bytes(head[27:30], "little") + 1
    return None


class Report:
    def __init__(self, only):
        self.only = only
        self.items = defaultdict(list)

    def add(self, check, path, line, message):
        if self.only and check not in self.only:
            return
        self.items[check].append((str(path.relative_to(ROOT)), line, message))

    def print(self):
        total = 0
        for check in sorted(self.items):
            rows = self.items[check]
            total += len(rows)
            print(f"\n## {check} ({len(rows)})")
            for path, line, message in rows:
                print(f"{path}:{line}: {message}")
        print(f"\n{total} problems")
        return total


def lineno(body_offset, text, index):
    return body_offset + text.count("\n", 0, index) + 1


def german_share(text):
    words = re.findall(r"[a-zäöüß]+", text.lower())
    de = sum(w in {"und", "der", "die", "das", "ist", "nicht", "ich", "mit", "auf", "für", "eine", "wir", "auch", "sich", "werden"} for w in words)
    en = sum(w in {"the", "and", "is", "not", "with", "for", "this", "that", "you", "are", "can", "which", "have", "from", "it"} for w in words)
    return de / (de + en) if de + en >= 20 else None


def check_all(files, report, all_meta):
    slugs = {m.get("slug") for m in all_meta.values() if m.get("slug")}
    medium = {m["medium_url"].rstrip("/"): m.get("slug") for m in all_meta.values() if m.get("medium_url")}
    tag_counts = Counter(t.strip() for m in all_meta.values() for t in m.get("tags", "").split(",") if t.strip())
    by_lower = defaultdict(list)
    for tag in tag_counts:
        by_lower[tag.lower()].append(tag)
    categories = {m.get("category") for m in all_meta.values()}
    slug_files = defaultdict(list)
    for path, meta in all_meta.items():
        if meta.get("slug"):
            slug_files[meta["slug"]].append(path)

    for path in files:
        meta, body, off = parse(path)
        draft = meta.get("status", "").lower() == "draft"
        # ---------- front matter ----------
        for key in ("title", "date", "category"):
            if not meta.get(key):
                report.add("fm-missing", path, 1, f"no {key}")
        slug = meta.get("slug", "")
        if not slug:
            report.add("fm-missing", path, 1, "no slug")
        elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            report.add("fm-slug", path, 1, f"slug {slug!r} is not lowercase-with-hyphens")
        if slug and len(slug_files[slug]) > 1:
            others = [str(p.relative_to(ROOT)) for p in slug_files[slug] if p != path]
            report.add("fm-slug-duplicate", path, 1, f"slug {slug!r} also in {', '.join(others)}")
        for key in meta:
            if key.lower() == "url":
                report.add("fm-url", path, 1, "url: in front matter (use medium_url:)")
        lang = meta.get("lang", "en") or "en"
        if lang not in ("en", "de"):
            report.add("fm-lang", path, 1, f"lang {lang!r}")
        if (lang == "de") != (meta.get("category") == "German posts") and meta.get("category") not in ("Sell",):
            report.add("fm-lang-category", path, 1, f"lang {lang} with category {meta.get('category')!r}")
        share = german_share(without_math(prose(body)))
        if share is not None and ((lang == "en" and share > 0.7) or (lang == "de" and share < 0.3)):
            report.add("fm-lang-text", path, 1, f"lang {lang}, but the text looks {'German' if share > 0.5 else 'English'} ({share:.0%} German)")
        raw_tags = meta.get("tags", "")
        if ";" in raw_tags or re.search(r"\[|\]", raw_tags):
            report.add("fm-tags", path, 1, f"tags not a comma-separated list: {raw_tags!r}")
        tags = [t.strip() for t in raw_tags.split(",") if t.strip()]
        if len(tags) != len(set(tags)):
            report.add("fm-tags", path, 1, "duplicate tag")
        for tag in tags:
            if tag in BANNED_TAGS:
                report.add("fm-tag-banned", path, 1, f"tag {tag!r} is banned (category name or meaningless)")
            elif tag in MERGED_TAGS:
                report.add("fm-tag-merged", path, 1, f"tag {tag!r} -> {MERGED_TAGS[tag]!r}")
            else:
                variants = by_lower[tag.lower()]
                if len(variants) > 1:
                    best = max(variants, key=lambda v: tag_counts[v])
                    if tag != best:
                        report.add("fm-tag-case", path, 1, f"tag {tag!r} -> {best!r}")
                elif tag[0].islower() and tag not in LOWERCASE_TAGS:
                    report.add("fm-tag-case", path, 1, f"tag {tag!r} is not Title Case")
            todo = [tag]
            while todo:
                for parent in TAG_PARENTS.get(todo.pop(), []):
                    if parent not in tags:
                        report.add("fm-tag-parent", path, 1, f"tag {tag!r} needs parent {parent!r}")
                    todo.append(parent)
        image = meta.get("featured_image")
        if image and not (IMAGES / image).exists():
            report.add("fm-featured-image", path, 1, f"featured_image {image} does not exist")

        # ---------- links ----------
        text = prose(body)
        for m in re.finditer(r"(?:href=[\"']|\]\()\s*(https?://(?:www\.)?(?:martin-thoma\.com|martinthoma\.github\.io)/([a-z0-9-]+)/?[^\"')\s]*)", text):
            if m.group(2) != "images":
                report.add("link-own-absolute", path, lineno(off, text, m.start()), f"{m.group(1)} -> ../{m.group(2)}/")
        for m in re.finditer(r"https?://(?:[a-z-]+\.)?medium\.com/[^\s\"')<>]+|https?://(?:levelup\.gitconnected|towardsdatascience|infosecwriteups|betterprogramming\.pub|python\.plainenglish\.io)[^\s\"')<>]*", text):
            url = m.group(0).rstrip("/").split("?")[0]
            if url in medium and medium[url]:
                report.add("link-medium-own", path, lineno(off, text, m.start()), f"{url} -> ../{medium[url]}/")
        for m in re.finditer(r"(?:href=[\"']|\]\()(\.\./[^\"')#?]*)", text):
            target = m.group(1).strip().replace("%20", " ")
            rel = target[3:]
            if rel.startswith("images/"):
                if not (ROOT / rel).exists():
                    report.add("link-broken", path, lineno(off, text, m.start()), f"{target} does not exist")
            elif rel and not ((OUTPUT / rel).exists() or (OUTPUT / rel / "index.html").exists() or (ROOT / rel).exists()):
                report.add("link-broken", path, lineno(off, text, m.start()), f"{target} does not exist in output/")
        for m in re.finditer(r"https?://[^\s\"')<>\]]+", text):
            if TRACKING.search(m.group(0)):
                report.add("link-tracking", path, lineno(off, text, m.start()), m.group(0))

        # ---------- images ----------
        for m in re.finditer(r"!\[[^\]]*\](?:\([^)]+\)|\[[^\]]*\])", text):
            report.add("img-markdown", path, lineno(off, text, m.start()), m.group(0)[:80])
        for m in re.finditer(r"<img\b[^>]*>", text):
            tag = m.group(0)
            line = lineno(off, text, m.start())
            attrs = dict((k.lower(), v if v is not None else w) for k, v, w in re.findall(r"""([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')""", tag))
            src = attrs.get("src", "")
            pixel = attrs.get("width") == "1" and attrs.get("height") == "1"
            if src.startswith("http") and not pixel and "vgwort.de" not in src:
                report.add("img-hotlink", path, line, src)
            if src.startswith("http"):
                continue
            if "style" in attrs:
                report.add("img-style", path, line, f"inline style on {src}")
            if re.search(r"\b(wp-|size-|align(none|left|right|center)|img-thumbnail)", attrs.get("class", "")):
                report.add("img-wp-class", path, line, attrs.get("class"))
            if not pixel and not attrs.get("alt", "").strip():
                report.add("img-alt", path, line, f"no alt text: {src}")
            if src.startswith("../images/") or src.startswith("{static}/images/"):
                file = ROOT / src.split("/", 1)[1] if src.startswith("../") else ROOT / src[len("{static}/"):]
                if not file.exists():
                    report.add("img-missing", path, line, f"{src} does not exist")
                    continue
                if file.stat().st_size > MAX_IMAGE_BYTES and not pixel:
                    report.add("img-large", path, line, f"{src} is {file.stat().st_size // 1024} KB")
                if not pixel and not (attrs.get("width") and attrs.get("height")):
                    report.add("img-size", path, line, f"no width/height: {src}")
                size = image_size(file)
                if size and attrs.get("width", "").isdigit() and int(attrs["width"]) > size[0] and not src.endswith(".svg"):
                    report.add("img-upscaled", path, line, f"{src} shown {attrs['width']} px wide, file is {size[0]} px")
                if src.startswith("{static}"):
                    report.add("img-static", path, line, f"{src} -> ../{src[len('{static}/'):]}")

        # ---------- math ----------
        code_free = prose(body)
        for m in re.finditer(r"\\[(\[]", code_free):
            before = code_free[max(0, m.start() - 1):m.start()]
            if before != "\\":
                report.add("math-delimiter", path, lineno(off, code_free, m.start()), "\\( or \\[ in Markdown (use $...$ or $$...$$)")
        for para in re.finditer(r"(?s)(?:[^\n]|\n(?!\s*\n))+", code_free):
            chunk = para.group(0)
            chunk = re.sub(r"\\\$", "  ", chunk)
            chunk = re.sub(r"(?s)\$\$.*?\$\$", lambda x: " " * len(x.group(0)), chunk)
            for m in re.finditer(r"(?<!\$)\$(?!\$)([^$]*?)\$(?!\$)", chunk):
                inner = m.group(1)
                where = lineno(off, code_free, para.start() + m.start())
                if "\n\n" in inner:
                    continue
                if re.search(r"\s$", inner) and inner.strip():
                    report.add("math-space", path, where, f"space before closing $: ${inner[-40:]}$")
                if not re.search(r"[\\^_=+{}]", inner) and re.search(r"[A-Za-zÄÖÜäöüß]{3,} [A-Za-zÄÖÜäöüß]{3,}|\*\*|\]\(", inner):
                    report.add("math-dollar", path, where, f"looks like a price, not math: ${inner[:40]}$ (write \\$)")
                for f in FUNC_RE.finditer(re.sub(r"\\(?:text|mathrm|operatorname|textbf|mbox)\{[^}]*\}", "", inner)):
                    report.add("math-function", path, where, f"\\{f.group(1)} without backslash in ${inner[:50]}$")

        # ---------- text ----------
        words_only = without_math(code_free)
        words_only = re.sub(r"<[^>]+>", lambda m: " " * len(m.group(0)), words_only)
        words_only = re.sub(r"\]\([^)]*\)", lambda m: " " * len(m.group(0)), words_only)
        words_only = re.sub(r"https?://\S+", lambda m: " " * len(m.group(0)), words_only)
        for m in re.finditer(r"\b(\w+) \1\b", words_only, re.I):
            if m.group(1).lower() not in DOUBLE_OK and not m.group(1).isdigit() and len(m.group(1)) > 1:
                report.add("text-double-word", path, lineno(off, words_only, m.start()), m.group(0))
        for m in re.finditer(r"[a-zA-Zäöüß\)] ([,;!?]|\.(?!\.))(?=\s|$)", words_only):
            ctx = words_only[max(0, m.start() - 20):m.end() + 5].replace("\n", " ")
            report.add("text-space-punct", path, lineno(off, words_only, m.start()), ctx.strip())
        if lang == "en":
            for m in re.finditer(r"(?<![\w'./-])i(?=[ ,'’](?:am|was|have|had|think|do|don|did|will|would|can|could|use|like|want|know|m|ve|d|ll)\b)", words_only):
                report.add("text-lowercase-i", path, lineno(off, words_only, m.start()), words_only[m.start():m.start() + 20].replace("\n", " "))
        del draft


def check_output(files, report, all_meta):
    """Rendered HTML: Markdown that was not rendered, and $ outside math and code."""
    for path in files:
        meta, body, off = parse(path)
        slug = meta.get("slug")
        page = OUTPUT / slug / "index.html" if slug else None
        if not page or not page.exists():
            if meta.get("status", "").lower() != "draft" and slug:
                report.add("out-missing", path, 1, f"output/{slug}/index.html not found (run make html-local)")
            continue
        doc = page.read_text(encoding="utf-8")
        m = re.search(r'(?s)<div class="article-content"[^>]*>(.*?)<footer|<div class="article-content"[^>]*>(.*)', doc)
        content = (m.group(1) or m.group(2)) if m else doc
        content = re.sub(r"(?s)<(pre|code|script|style|textarea)\b.*?</\1>", " ", content)
        content = re.sub(r'(?s)<span class="math">.*?</span>|<div class="math">.*?</div>', " ", content)
        content = re.sub(r"(?s)<!--.*?-->", " ", content)
        text = html.unescape(re.sub(r"<[^>]+>", " ", content))
        for pattern, what in [
            (r"\*\*\S[^*\n]{0,60}\*\*", "unrendered **bold**"),
            (r"\]\((?:https?://|\.\./)", "unrendered Markdown link"),
            (r"\[\^\w+\]", "unrendered footnote"),
            (r"\{%|%\}", "Liquid/Jinja tag"),
            (r"\{(?:static|filename)\}", "unresolved {static}/{filename}"),
            (r"&(?:nbsp|amp|thinsp|rarr);", "escaped HTML entity shown as text"),
            (r"(?m)^\s*#{2,6} \w", "unrendered heading"),
        ]:
            for hit in re.finditer(pattern, text):
                ctx = text[max(0, hit.start() - 30):hit.end() + 30].replace("\n", " ")
                report.add("out-markdown", path, 1, f"{what}: …{ctx.strip()}…")
        # MathJax reads $…$ everywhere on the page. Flag pairs whose content is prose or
        # code rather than TeX: PHP/shell variables and prices need \$ in the source.
        for para in re.split(r"\n\s*\n|</?(?:p|li|td|th|h\d|div)\b[^>]*>", content):
            plain = html.unescape(re.sub(r"<[^>]+>", " ", para))
            plain = re.sub(r"\\\$", "  ", plain)
            for pair in re.finditer(r"(?<!\$)\$(?!\$)([^$]{1,300}?)\$(?!\$)", plain):
                inner = pair.group(1)
                if re.search(r"[\\^_{}=<>|]", inner):
                    continue
                if re.search(r"[A-Za-zÄÖÜäöüß]{3,}\s+[A-Za-zÄÖÜäöüß]{3,}", inner) or re.match(r"\s*\d", inner) and re.search(r"\s$", inner):
                    report.add("out-dollar", path, 1, f"MathJax would typeset this as math: ${inner.strip()[:80]}$")
        for hit in re.finditer(r'href="#?"', content):
            report.add("out-link", path, 1, f"suspicious link {hit.group(0)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--drafts", action="store_true", help="also check articles with status: draft")
    ap.add_argument("--only", help="comma-separated check names (prefixes work: fm,link,img,math,text,out)")
    ap.add_argument("files", nargs="*", type=Path)
    args = ap.parse_args()

    all_files = sorted(CONTENT.glob("*.md"))
    all_meta = {p: parse(p)[0] for p in all_files}
    files = [p.resolve() for p in args.files] if args.files else all_files
    if not args.drafts:
        files = [p for p in files if all_meta.get(p, parse(p)[0]).get("status", "").lower() != "draft"]

    only = None
    if args.only:
        prefixes = [o.strip() for o in args.only.split(",")]
        only = {c for c in KNOWN_CHECKS if any(c == p or c.startswith(p + "-") or c == p for p in prefixes)}
    report = Report(only)
    check_all(files, report, all_meta)
    if OUTPUT.exists():
        check_output(files, report, all_meta)
    sys.exit(1 if report.print() else 0)


KNOWN_CHECKS = {
    "fm-missing", "fm-slug", "fm-slug-duplicate", "fm-url", "fm-lang", "fm-lang-category", "fm-lang-text",
    "fm-tags", "fm-tag-banned", "fm-tag-merged", "fm-tag-case", "fm-tag-parent", "fm-featured-image",
    "link-own-absolute", "link-medium-own", "link-broken", "link-tracking",
    "img-markdown", "img-hotlink", "img-style", "img-wp-class", "img-alt", "img-missing", "img-large",
    "img-size", "img-upscaled", "img-static",
    "math-delimiter", "math-space", "math-dollar", "math-function",
    "text-double-word", "text-space-punct", "text-lowercase-i",
    "out-missing", "out-markdown", "out-dollar", "out-link",
}

if __name__ == "__main__":
    main()
