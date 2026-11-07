"""Generate the "More in this series" section from one data file per series.

An article contains the marker ``<!-- series: appsec -->`` (on its own line,
where the section should appear). The plugin replaces it with the section
defined in ``series/appsec.yaml`` (next to the content directory):

* parts with a ``slug`` of a published article are numbered and linked,
* the current article is bold instead of a link,
* parts without a published article (drafts, ideas) are listed under the
  outlook text, without a link.

So every part shows the same list, and no published page links to a draft.
"""

import html
import logging
import re
from pathlib import Path

import yaml
from pelican import signals

logger = logging.getLogger(__name__)

MARKER = re.compile(r"(?:<p>)?<!--\s*series:\s*([\w-]+)\s*-->(?:</p>)?")

_series = {}  # name -> parsed yaml
_published = set()  # slugs of published articles


def _front_matter(path):
    meta = {}
    with open(path, encoding="utf-8") as fh:
        first = fh.readline()
        if first.strip() != "---":
            return meta
        for line in fh:
            if line.strip() == "---":
                break
            key, sep, value = line.partition(":")
            if sep:
                meta[key.strip().lower()] = value.strip()
    return meta


def load(pelican):
    content = Path(pelican.settings["PATH"])
    series_dir = Path(pelican.settings.get("SERIES_PATH", content.parent / "series"))
    _series.clear()
    for path in sorted(series_dir.glob("*.yaml")):
        _series[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
    _published.clear()
    for path in content.rglob("*.md"):
        meta = _front_matter(path)
        if meta.get("slug") and meta.get("status", "published") == "published":
            _published.add(meta["slug"])


def _part(part, current_slug, number=None):
    title = html.escape(part["title"])
    slug = part.get("slug")
    if slug == current_slug:
        label = f"<strong>{title}</strong>"
    elif number is not None:
        label = f'<a href="../{slug}/">{title}</a>'
    elif part.get("url"):  # planned topic with an external explanation
        label = f'<a href="{html.escape(part["url"])}">{title}</a>'
    else:
        label = title
    prefix = f"Part {number}: " if number is not None else ""
    note = f" {html.escape(part['note'])}" if part.get("note") else ""
    icons = f" {part['icons']}" if part.get("icons") else ""
    return f"<li>{prefix}{label}{note}{icons}</li>"


def render(name, current_slug):
    data = _series[name]
    done, upcoming = [], []
    number = 0
    for part in data["parts"]:
        slug = part.get("slug")
        if slug and (slug in _published or slug == current_slug):
            number += 1
            done.append(_part(part, current_slug, number))
        else:
            upcoming.append(_part(part, current_slug))
    out = [f'<h2 id="more-in-this-series">{html.escape(data["title"])}</h2>']
    out.append(f"<p>{html.escape(data['intro'])}</p>")
    out.append("<ul>\n" + "\n".join(done) + "\n</ul>")
    if upcoming and data.get("outlook"):
        out.append(f"<p>{html.escape(data['outlook'])}</p>")
        out.append("<ul>\n" + "\n".join(upcoming) + "\n</ul>")
    return "\n".join(out)


def replace_marker(instance):
    content = getattr(instance, "_content", None)
    if not content or "series:" not in content:
        return

    def sub(match):
        name = match.group(1)
        if name not in _series:
            logger.warning("Unknown series '%s' in %s", name, instance.source_path)
            return match.group(0)
        return render(name, getattr(instance, "slug", None))

    instance._content = MARKER.sub(sub, content)


def register():
    signals.initialized.connect(load)
    signals.content_object_init.connect(replace_marker)
