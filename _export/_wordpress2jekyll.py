#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys, re

def re_sub(pattern, replacement, string):
	def _r(m):
		# Now this is ugly.
		# Python has a "feature" where unmatched groups return None
		# then re.sub chokes on this.
		# see http://bugs.python.org/issue1519638
		
		# this works around and hooks into the internal of the re module...

		# the match object is replaced with a wrapper that
		# returns "" instead of None for unmatched groups

		class _m():
			def __init__(self, m):
				self.m=m
				self.string=m.string
			def group(self, n):
				return m.group(n) or ""

		return re._expand(pattern, _m(m), replacement)
	
	return re.sub(pattern, _r, string)

def parseCaptions(content):
    """
    [caption id="attachment_76716" align="aligncenter" width="500"]<a href="http://martin-thoma.com/wp-content/uploads/2013/11/WER-calculation.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full wp-image-76716" /></a> WER calculation[/caption]

    to

    {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="../images/2013/11/WER-calculation.png" %}
    """
    import re

    pattern = '\[caption(.*?)align="(?P<align>.*?)"(.*?)(caption="(?P<caption>.*?)")?(.*?)\]' + \
        '<a(.*?)href=\"(?P<url>.*?)\"(?P<asonst>.*?)>' + \
        '<img(.*?)' + \
            'class=\"(?P<imgclass>.*?)\"\s*' + \
            'src=\"(?P<imgurl>http://martin-thoma.com/wp-content/uploads/(?P<innerurl>.*?))\" ' + \
            'alt=\"(?P<alt>.*?)\"\s*' + \
            '(title=\"(?P<title>.*?)\")?\s*' + \
            'width=\"(?P<width>.*?)\"\s*' + \
            'height=\"(?P<height>.*?)\"\s*' + \
            '(?P<isonst>.*?)/>' + \
        '</a>\s*' + \
        '(?P<text>.*?)\[/caption\]'
    pattern = re.compile(pattern)
    results = [m.groupdict() for m in pattern.finditer(content)]
    for result in results:
        for key, value in result.items():
            print("%s:\t%s" % (key, value))

    content = re_sub(pattern, '{% caption align="\g<align>" width="\g<width>" caption="\g<caption>\g<text>" url="../images/\g<innerurl>" alt="\g<alt>" title="\g<title>" height="\g<height>" class="\g<imgclass>" %}', content)

    return content

def pageCodeConversion(page):
    yaml, content = getYaml(page)

    content = content.replace("[latex]", "$")
    content = content.replace("[/latex]", "$")

    # Syntax highlighter: also '[python collapse="true"]'
    # [c] is dangerous. Use it with caution!
    for language in ['python', 'cpp', 'text', 'bash', 'java', 'javascript']:
        content = content.replace("["+language+"]", "{% highlight "+language+" %}")
        content = content.replace("[/"+language+"]", "{% endhighlight %}")
    content = parseCaptions(content)
    return "---" + yaml + "---" + content

def getYaml(content):
    tmp, yaml, *content = content.split("---") #here you need python3
    content = "---".join(content)
    return (yaml, content)

def featuredImage(website, content):
    post2image = {}
    # Get all featured image urls connected to posts
    import urllib2
    from bs4 import BeautifulSoup

    # Parse Website for images
    while website:
        response = urllib2.urlopen(website)
        html = response.read()
        soup = BeautifulSoup(html)
        for entry in soup.find_all("div", "entry"):
            img = entry.find("img")
            if img is not None:
                imgsrc = img['src'].split("uploads/")[1]

                a = entry.find("a", "readmore")
                post = a['href'][len(website):-1]

                post2image[post] = imgsrc

        nav = soup.find("div", "alignleft")
        if nav is not None:
            website = nav.find("a")
            if website is not None:
                website = website['href']
        else:
            website = None
        print(website)

    yaml, content = getYaml(content)
    hasFeaturedImage = False

    for i, line in enumerate(yaml.split("\n")):
        if ":" in line:
            if line.startswith("featured_image"):
                hasFeaturedImage = True
                break
            if line.startswith("comment"):
                commentline = i

    if not hasFeaturedImage:
        mdfilename = filename[len("./_posts/2013-11-18-"):-len(".markdown")]
        if mdfilename not in post2image:
            print("w warning: %s might not have a featured image." % mdfilename)
        else:
            print("# success: %s" % mdfilename)
            imgsrc = post2image[mdfilename]
            newsrc = "---" + yamml + "featured_image: "+imgsrc+"\n" + "---" + content
            with open(filename, 'w') as f:
                f.write(newsrc)
    else:
        print("x info: %s has already a featured image" % filename)

def changeYaml(content):
    tmp, yaml, *contentArray = content.split("---")
    newContent = "---\n"
    isComment = False
    isTagOrCat = False
    for line in yaml.split("\n"):
        if line.startswith("layout:") or \
            line.startswith("title:") or \
            line.startswith("author:") or \
            line.startswith("date:") or \
            line.startswith("context:") or \
            line.startswith("featured_image:"):
            newContent += line + "\n"
            isComment = False
            isTagOrCat = False
        elif line.startswith("status:") or \
            line.startswith("published:") or \
            line.startswith("author_login:") or \
            line.startswith("author_email:") or \
            line.startswith("author_url:") or \
            line.startswith("wordpress_id:") or \
            line.startswith("wordpress_url:") or \
            line.startswith("published:"):
            isComment = False
            isTagOrCat = False
            pass#ignore those lines (that means: delete them!)
        elif line.startswith("comments:"):
            isComment = True
        elif line.startswith("tags:"):
            newContent += line + "\n"
            isTagOrCat = True
        elif line.startswith("categories:"):
            newContent += line + "\n"
            isTagOrCat = True
        elif line.startswith("-") and isComment:
            pass
        elif line.startswith("-") and isTagOrCat:
            newContent += line + "\n"
        else:
            print(line)
    newContent += "---"
    newContent += "---".join(contentArray)
    return newContent

def forEveryPost(website, operation, development=True):
    from os import listdir
    directory = "./_posts/"
    files = sorted(listdir(directory))
    for f in files:
        filename = directory+f

        with open(filename) as f:
            content = f.read()
        newContent = operation(content)

        print(filename)
        if not development:
            with open(filename, 'w') as f:
                f.write(newContent)
        else:
            #print(newContent)
            print("#"*80)

def captionRemoveDeprecated(page):
    yaml, content = getYaml(page)

    pattern = re.compile("{% caption(?P<before>.*?)caption=\"(?P<caption>.*?)\"(?P<between>.*?)title=\"\"(?P<after>.*?)%}")
    content = re.sub(pattern, '{% caption\g<before>caption=\"\g<caption>\"\g<between>\g<after>%}', content)
    return "---" + yaml + "---" + content

if __name__ == "__main__":
    """
    from argparse import ArgumentParser
    parser = ArgumentParser()
    # Add more options if you like
    parser.add_argument("-f", "--file", dest="filename", required="True",
                      help="convert file FILE", metavar="FILE")
     
    args = parser.parse_args()
     
    pageCodeConversion(args.filename)
    """

    # improve things
    forEveryPost("http://martin-thoma.com/", captionRemoveDeprecated, False)
    
