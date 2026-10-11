"""Pelican plugin: pick the preview image (og:image) of an article from its text.

Most articles only have a generic logo as ``featured_image``, although the text
has a real picture. This plugin sets ``article.og_image`` to the first suitable
local image of the article: a JPG, PNG or WebP below ``images/`` that is at least
``MIN_WIDTH`` x ``MIN_HEIGHT`` pixels and has no transparency (it would be
rendered on black by some services). An explicit ``featured_image`` that is not
a logo wins; the template falls back to the logo if no image is found.

``og_image`` is a path relative to the site root, e.g. ``images/2024/01/x.png``.
"""

import re
from functools import lru_cache
from pathlib import Path

from PIL import Image
from pelican import signals
from pelican.contents import Article

IMG_SRC = re.compile(r"<img\b[^>]*?\bsrc=\"([^\"]+)\"", re.I)
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MIN_WIDTH = 400
MIN_HEIGHT = 200


@lru_cache(maxsize=None)
def usable_size(path):
    """Return (width, height) of an opaque image that is big enough, else None."""
    try:
        with Image.open(path) as img:
            if img.mode in ("RGBA", "LA") or "transparency" in img.info:
                return None
            width, height = img.size
    except (OSError, ValueError):
        return None
    if width < MIN_WIDTH or height < MIN_HEIGHT:
        return None
    return width, height


def first_image(content, root):
    for src in IMG_SRC.findall(content):
        rel = src.replace("{static}", "").lstrip("/")
        while rel.startswith("../"):
            rel = rel[3:]
        if not rel.startswith("images/") or Path(rel).suffix.lower() not in EXTENSIONS:
            continue
        size = usable_size(str(root / rel))
        if size:
            return rel, size
    return None


def social_image(content):
    if not isinstance(content, Article):
        return
    featured = content.metadata.get("featured_image", "")
    if featured and not featured.startswith("logos/"):
        return
    root = Path(content.settings["PATH"])
    found = first_image(content._content or "", root)
    if found:
        content.og_image, (content.og_image_width, content.og_image_height) = found


def register():
    signals.content_object_init.connect(social_image)
