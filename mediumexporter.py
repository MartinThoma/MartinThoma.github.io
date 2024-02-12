#!/usr/bin/env python

import argparse
from datetime import datetime
import json
from typing import Any
import sys
import requests
from pydantic import BaseModel

MEDIUM_IMG_CDN = "https://medium2.global.ssl.fastly.net/max/"


class MediumPost(BaseModel):
    id: str
    versionId: str
    creatorId: str
    title: str
    detectedLanguage: str  # e.g. "en"
    latestVersion: str
    latestPublishedVersion: str
    hasUnpublishedEdits: bool
    latestRev: int
    createdAt: datetime
    updatedAt: datetime
    acceptedAt: datetime
    firstPublishedAt: datetime
    latestPublishedAt: datetime
    content: dict[str, Any]
    slug: str
    canonicalUrl: str


class MediumPayload(BaseModel):
    value: MediumPost


class MediumResponse(BaseModel):
    success: bool
    payload: MediumPayload


def load_medium_post(medium_url: str) -> dict[str, Any]:
    if medium_url.startswith("http"):
        if "?" in medium_url:
            url = medium_url + "&format=json"
        else:
            url = medium_url + "?format=json"
        response = requests.get(url)
        response.raise_for_status()
        json_string = response.text[response.text.index("{") :]
        return json.loads(json_string)
    else:
        with open(medium_url, "r") as file:
            return json.load(file)


def process_section(s):
    section = ""
    if "backgroundImage" in s:
        img_width = int(s["backgroundImage"]["originalWidth"])
        img_src = (
            f"{MEDIUM_IMG_CDN}{max(img_width * 2, 2000)}/{s['backgroundImage']['id']}"
        )
        section = f"\n![]({img_src})"
    return section


def process_paragraph(p):
    markups_array = create_markups_array(p.get("markups", []))

    if markups_array:
        previous_index = 0
        text = p["text"]
        tokens = []
        for j, markup in enumerate(markups_array):
            if markup:
                token = text[previous_index:j]
                previous_index = j
                tokens.extend([token, markup])
        tokens.append(text[j - 1 :])
        print("#" * 80)
        print(tokens)
        p["text"] = "".join([str(t) for t in tokens])

    markup = ""
    p_type = p.get("type", 0)
    if p_type == 1:
        markup = "\n"
    elif p_type == 2:
        p["text"] = "\n# " + p["text"].replace("\n", "\n# ")
    elif p_type == 3:
        p["text"] = "\n## " + p["text"].replace("\n", "\n## ")
    elif p_type == 4:  # image & caption
        img_width = int(p["metadata"]["originalWidth"])
        img_src = f"{MEDIUM_IMG_CDN}{max(img_width * 2, 2000)}/{p['metadata']['id']}"
        p["text"] = f"\n![{p['text']}]({img_src})*{p['text']}*"
    elif p_type == 6:
        markup = "> "
    elif p_type == 7:  # quote
        p["text"] = "> # " + p["text"].replace("\n", "\n> # ")
    elif p_type == 8:
        p["text"] = "\n    " + p["text"].replace("\n", "\n    ")
    elif p_type == 9:
        markup = "\n* "
    elif p_type == 10:
        markup = "\n1. "
    elif p_type == 11:
        p[
            "text"
        ] = f'\n<iframe src="https://medium.com/media/{p["iframe"]["mediaResourceId"]}" frameborder=0></iframe>'
    elif p_type == 13:
        markup = "\n### "
    elif p_type == 15:  # caption for section image
        p["text"] = f"*{p['text']}*"
    else:
        print(f"Unknown paragraph type {p_type}", p, file=sys.stderr)

    p["text"] = markup + p["text"]

    if p.get("alignment") == 2 and p_type not in {6, 7}:
        p["text"] = f"<center>{p['text']}</center>"

    return p["text"]


def add_markup(markups_array, open_tag, close_tag, start, end):
    markups_array[start] = markups_array.get(start, "") + open_tag
    markups_array[end] = markups_array.get(end, "") + close_tag
    return markups_array


def create_markups_array(markups):
    markups_array = {}
    for m in markups:
        m_type = m["type"]
        if m_type == 1:  # bold
            markups_array = add_markup(markups_array, "**", "**", m["start"], m["end"])
        elif m_type == 2:  # italic
            markups_array = add_markup(markups_array, "*", "*", m["start"], m["end"])
        elif m_type == 3:  # anchor tag
            markups_array = add_markup(
                markups_array, f"[", f"]({m['href']})", m["start"], m["end"]
            )
        else:
            print(f"Unknown markup type {m_type}", m, file=sys.stderr)
    return markups_array


def main():
    parser = argparse.ArgumentParser(
        description="Export Medium posts to markdown format"
    )
    parser.add_argument("medium_post_url", help="Medium post URL")
    parser.add_argument(
        "-H",
        "--headers",
        action="store_true",
        help="Add headers at the beginning of the markdown file with metadata",
    )
    parser.add_argument(
        "-S", "--separator", default="", help="Separator between headers and body"
    )
    parser.add_argument(
        "-I",
        "--info",
        action="store_true",
        help="Show information about the medium post",
    )
    args = parser.parse_args()

    medium_url = args.medium_post_url

    try:
        medium_post_json = load_medium_post(medium_url)
    except Exception as e:
        print(f"Failed to fetch Medium post: {e}", file=sys.stderr)
        sys.exit(1)

    story = {}
    resp = MediumResponse.model_validate(medium_post_json)
    medium_post: MediumPost = resp.payload.value
    story["title"] = medium_post.title
    story["subtitle"] = medium_post.content["subtitle"]
    story["date"] = medium_post.firstPublishedAt
    story["url"] = medium_post.canonicalUrl
    story["language"] = medium_post.detectedLanguage

    if args.info:
        print("args.info:")
        print(json.dumps(story, indent=4))
        sys.exit(0)

    sections = medium_post.content["bodyModel"]["sections"]
    paragraphs = medium_post.content["bodyModel"]["paragraphs"]

    markdown = []
    markdown.append("\n# " + story["title"].replace("\n", "\n# "))
    markdown.append("\n## " + story["subtitle"].replace("\n", "\n## "))
    for i, paragraph in enumerate(paragraphs):
        if i in sections:
            markdown.append(process_section(sections[i]))

        markdown.append(process_paragraph(paragraph))

    if args.headers:
        print("url: " + story["url"])
        print("date: " + str(story["date"]))
        print(args.separator)

    print("\n".join(markdown))


if __name__ == "__main__":
    main()
