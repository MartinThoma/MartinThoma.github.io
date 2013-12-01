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
    url = "(.*?)"
    pattern = re.compile('\[caption[\w\s=\d"]*align="(?P<alignment>.*?)"[\w\s=\d"]*\]' + \
        '<a href=\"(?P<url>' + url + ')\"(?P<asonst>.*?)>' + \
        '<img src=\"(?P<imgurl>http://martin-thoma.com/wp-content/uploads/(?P<innerurl>' + url + '))\" ' + \
            'alt=\"(?P<alt>.*?)\"\s*' + \
            'width=\"(?P<width>.*?)\"\s*' + \
            'height=\"(?P<height>.*?)\"\s*' + \
            'class=\"(?P<imgclass>.*?)\"\s*' + \
            '(?P<isonst>.*?)/>' + \
        '</a>\s*' + \
        '(?P<text>.*?)\[/caption\]')
    results = [m.groupdict() for m in pattern.finditer(content)]
    for result in results:
        for key, value in result.items():
            print("%s:\t%s" % (key, value))

    return re.sub(pattern, '{% caption class="\g<imgclass>" width="\g<width>" height="\g<height>" alt="\g<alt>" text="\g<text>" url="../images/\g<innerurl>" %}', content)

def pageCodeConversion(filename):
    with open(filename) as f:
        content = f.read()

    content = content.replace("&#47;", "/")

    # Create MathJax:
    #if "$" in content:
    #    print("Error: contained a $. It might already have been processed. Replace [latex]-tags manually", file=sys.stderr)
    #else:
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
        

    from os import listdir
    directory = "./_posts/"
    files = listdir(directory)
    for f in files:
        filename = directory+f

        with open(filename) as f:
            content = f.read()

        yamml = getYamml(content)
        if len(yamml) != 3:
            print("There seems to be --- inside of the post. Please fix it!")
            exit

        yamml = yamml[1]
        hasFeaturedImage = False
        for line in yamml.split("\n"):
            if ":" in line:
                if line.startswith("featured_image"):
                    hasFeaturedImage = True
                    break

        if not hasFeaturedImage:
            mdfilename = filename[len("./_posts/2013-11-18-"):-len(".markdown")]
            if mdfilename not in post2image:
                print("%s might not have a featured image." % mdfilename)
            else:
                print("# %s # success" % mdfilename)
        else:
            print("xx %s has already a featured image" % filename)



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
    findFeaturedImage("http://martin-thoma.com")
    
