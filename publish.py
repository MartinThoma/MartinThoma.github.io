#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, datetime, sys

def change_yaml_date(content):
    def getYaml(content):
        tmp, yaml, *content = content.split("---") #here you need python3
        content = "---".join(content)
        return (yaml, content)
    yaml, content = getYaml(content)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    pattern = re.compile("^date: (.*)$", re.MULTILINE)
    yaml = re.sub(pattern, "date: "+now, yaml)
    return "---" + yaml + "---" + content

def get_filename(draft):
    """Return new filename from old draft filename."""
    filename = '_posts/'
    if not draft.startswith("_drafts/"):
        print("Why doesn't your filename begin with '_drafts/'?")
        sys.exit(-1)
    else:
        draft = draft[len("_drafts/"):]
    pattern = re.compile('^(\d{4})-(\d{2})-(\d{2})')
    m=re.match(pattern, draft)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    if m is None:
        #No date at beginning of string
        if not draft.startswith("-"):
            draft = "-" + draft
        filename += today + draft
    else:
        draft = draft[len("yyyy-mm-dd"):]
        if not draft.startswith("-"):
            draft = "-" + draft
        filename += today + draft

    while os.path.isfile(filename):
        #Oh noes! File does already exist.
        filename = filename.split(".")
        filename[-2] += "-dup"
        filename = ".".join(filename)
    return filename

def publish(draft):
    try:
        with open(draft) as f:
           content = f.read()
        content = change_yaml_date(content)
        
        filename = get_filename(draft)
        print("New filename will be '%s'." % filename)
        with open(filename,'w') as f:
            f.write(content)
        os.remove(draft)
    except IOError:
       print('The draft %s does not exist.' % os.path.abspath(draft))

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    # Add more options if you like
    parser.add_argument("-f", "--file", dest="draft",required=True,
                      help="publish FILE", metavar="FILE")
    args = parser.parse_args()
    publish(args.draft)
