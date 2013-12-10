#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys

def parseCaptions(content):
    """
    [caption id="attachment_76716" align="aligncenter" width="500"]<a href="http://martin-thoma.com/wp-content/uploads/2013/11/WER-calculation.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full wp-image-76716" /></a> WER calculation[/caption]

    to


    <div style="width: 510px" class="wp-caption aligncenter">
        <a href="../images/2013/11/WER-calculation.png">
            <img src="../images/2013/11/WER-calculation.png" alt="WER calculation" width="500" height="494" class="size-full">
        </a>
        <p class="wp-caption-text">WER calculation</p>
    </div>

    or

    {% caption align="aligncenter" width="500" alt="WER calculation" text="WER calculation" url="../images/2013/11/WER-calculation.png" %}
    """
    import re

    # first with caption inside caption tag
    pattern = '\[caption(.*?)align="(?P<align>.*?)"(.*?)caption="(?P<caption>.*?)"(.*?)\]' + \
        '<a(.*?)href=\"(?P<url>(.*?))\"(?P<asonst>.*?)>' + \
        '<img(.*?)src=\"(?P<imgurl>http://martin-thoma.com/wp-content/uploads/(?P<innerurl>(.*?)))\" ' + \
            'alt=\"(?P<alt>.*?)\"\s*' + \
            'title=\"(?P<title>.*?)\"\s*' + \
            'width=\"(?P<width>.*?)\"\s*' + \
            'height=\"(?P<height>.*?)\"\s*' + \
            'class=\"(?P<imgclass>.*?)\"\s*' + \
            '(?P<isonst>.*?)/>' + \
        '</a>\s*' + \
        '(?P<text>.*?)\[/caption\]'
    pattern = re.compile(pattern)
    results = [m.groupdict() for m in pattern.finditer(content)]
    for result in results:
        for key, value in result.items():
            print("%s:\t%s" % (key, value))

    content = re.sub(pattern, '{% caption align="\g<align>" width="\g<width>" caption="\g<caption>" url="../images/\g<innerurl>" alt="\g<alt>" title="\g<title>" height="\g<height>" class="\g<imgclass>" %}', content)

    return content

def pageCodeConversion(filename):
    with open(filename) as f:
        content = f.read()

    content = content.replace("[latex]", "$")
    content = content.replace("[/latex]", "$")

    # Syntax highlighter: also '[python collapse="true"]'
    for language in ['python', 'cpp', 'text', 'bash', 'java', 'javascript']:
        content = content.replace("["+language+"]", "{% highlight "+language+" %}")
        content = content.replace("[/"+language+"]", "{% endhighlight %}")
    content = parseCaptions(content)
    with open(filename, 'w') as f:
        f.write(content)

def getYamml(content):
    return content.split("---")

def findFeaturedImage(website):
    post2image = {}
    # Get all featured image urls connected to posts
    import urllib2
    from bs4 import BeautifulSoup

    """
    while website:
        response = urllib2.urlopen(website)
        html = response.read()
        soup = BeautifulSoup(html)
        for entry in soup.find_all("div", "entry"):
            img = entry.find("img")
            if img is not None:
                imgsrc = img['src'].split("uploads/")[1]

                a = entry.find("a", "readmore")
                post = a['href'][len("http://martin-thoma.com/"):-1]

                post2image[post] = imgsrc

        nav = soup.find("div", "alignleft")
        if nav is not None:
            website = nav.find("a")
            if website is not None:
                website = website['href']
        else:
            website = None
        print(website)
    """

    from os import listdir
    directory = "./_posts/"
    files = listdir(directory)
    for f in files:
        filename = directory+f

        #with open(filename) as f:
        #    content = f.read()

        #yamml = getYamml(content)
        #if len(yamml) != 3:
        #    print("There seems to be --- inside of post '%s'. Please fix it!" % filename)
        #    continue

        #yamml, content = yamml[1], yamml[2]
        #hasFeaturedImage = False
        """
        for i, line in enumerate(yamml.split("\n")):
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
        """

        pageCodeConversion(filename)



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
    findFeaturedImage("http://martin-thoma.com/")
    
