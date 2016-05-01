#!/usr/bin/env python
# encoding: utf-8

"""Convert Markdown pages from Jekyll format to the Pelican format."""

import os


def categories_and_tags(filename):
    """
    Parse all Markdown files and overwrite them in the desired format.

    This script assumes your header looks like this (same order):

    ---
    layout: post
    title: Migrate from Jekyll to Pelican
    author: Martin Thoma
    date: 2014-11-22 17:19
    categories:
    - Cyberculture
    tags:
    - Jekyll
    - Blogging
    featured_image: logos/star.png
    ---
    """
    with open(filename) as f:
        lines = f.read().split("\n")
    tags_i = None
    category_i = None
    last_tag_i = None
    tags = []
    categories = []
    seen_dashes = 0
    categories_ended = False
    for i, line in enumerate(lines):
        line_ = line.strip()
        if line_ == '---':
            seen_dashes += 1
        if seen_dashes == 2:
            break
        if line_ == "category:" or line_ == "categories:":
            category_i = i
        elif line_.startswith("category:"):
            category_i = i
            categories = [line_[len("category:"):].strip()]
        if category_i and line_.startswith("-") and not categories_ended:
            categories.append(line_[1:].strip())  # Get right of leading '- '
        if line_ == "tags:":
            categories_ended = True
            tags_i = i
        elif line_.startswith("tags:"):
            tags = [line_[len("tags:"):].strip()]
        if tags_i and line_.startswith("-"):
            tags.append(line_[1:].strip())
            last_tag_i = i
    print(filename)

    tags_ = tags

    if len(categories) == 1:
        category = categories[0]
    else:
        print("WARNING: '%s' has categories %i (%s)" %
              (filename, len(categories), categories))

    txt = ""
    txt += "\n".join(lines[:category_i]) + "\n"
    txt += "category: %s\n" % category
    txt += "tags: %s\n" % ", ".join(tags_)

    if last_tag_i:
        txt += "\n".join(lines[last_tag_i+1:])
    else:
        txt += "\n".join(lines[category_i + len(categories) + 1:])

    with open(filename, "w") as o:
        o.write(txt)


def math(filename):
    """
    Convert math mode indicators.

    \(...\) to $...$
    \[...\] to $$...$$$
    """
    import re
    with open(filename) as f:
        content = f.read()

    single_math = re.compile("\((.+?)\)")
    content = single_math.sub(lambda m: "${math}$".format(math=m.group(1)),
                              content)

    with open(filename, "w") as o:
        o.write(content)

if __name__ == '__main__':
    filenames = filter(lambda x: x.endswith(".md"), os.listdir("."))
    for filename in sorted(filenames):
        categories_and_tags(filename)
