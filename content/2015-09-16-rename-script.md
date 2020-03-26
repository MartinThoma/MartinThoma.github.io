---
layout: post
title: Rename Script
author: Martin Thoma
date: 2015-09-16 16:15
category: Cyberculture
tags: File, Rename, Python
featured_image: logos/python.png
---
Once in a while I have to bulk rename files. For example, when I have holiday
photos. The following script helps me to do so:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Batch-Rename files in a folder according to some rules."""

import os
import math
from PIL import Image


def get_date_taken(path):
    """Get the date when the image was taken."""
    print(path)
    im = Image.open(path)
    if im is not None or im._getexif() is None:
        return im._getexif()[36867]
    else:
        print("Could not find date in EXIF data for '%s'" % path)
        return os.stat(path).st_ctime


def rename(rename, starts=None, ends=None, test=False):
    """
    Rename all files in a nice way.

    Only files which end with `ends` and start with `starts` are renamed to
    `rename-[Number]`.
    """
    files = [f for f in os.listdir(".") if os.path.isfile(f) and not f.endswith(".py")]
    # Sort files by last modification / creation
    files.sort(key=lambda x: os.stat(x).st_ctime)  # st_ctime or st_mtime
    files.sort(key=lambda x: get_date_taken(x))
    if starts is not None:
        files = [f for f in files if f.lower().startswith(starts.lower())]
    if ends is not None:
        files = [f for f in files if f.lower().endswith(ends.lower())]
    for i, f in enumerate(files, start=1):
        filename, ext = os.path.splitext(f)
        ext = ext.lower()
        digits = int(math.log10(len(files))) + 1
        number = str(i).zfill(digits)
        new_name = "%s-%s%s" % (rename, number, ext)
        if test:
            print("{0:<40}-> {1:<20}".format(f, new_name))
        else:
            os.rename(f, new_name)


def get_parser():
    """Parser for rename script."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-n", "--name", dest="name", help="new name", required=True, metavar="NAME"
    )
    parser.add_argument(
        "-s",
        "--starts",
        dest="starts",
        help="Get files which start with this string",
        default=None,
        metavar="STARTS",
    )
    parser.add_argument(
        "-e",
        "--ends",
        dest="ends",
        help="Get files which end with this string",
        default=None,
        metavar="ENDS",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        dest="test",
        default=False,
        help="don't change anything, just show what would be " "done",
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    rename(args.name, starts=args.starts, ends=args.ends, test=args.test)
```
