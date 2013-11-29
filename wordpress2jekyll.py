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
    pattern = re.compile('\[caption[\w\s=\d"]*\]' + \
        '<a href=\"(?P<url>' + url + ')\"(?P<asonst>.*?)>' + \
        '<img src=\"(?P<imgurl>' + url + ')\" ' + \
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

    return re.sub(pattern, '{% caption class="\g<imgclass>" width="\g<width>" height="\g<height>" alt="\g<alt>" text="\g<text>" url="\g<imgurl>" %}', content)

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
    #with open(filename, 'w') as f:
    #    f.write(content)
    print(filename)
    print(content)
    print("#"*80)

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
    from os import listdir
    directory = "./_posts/"
    files = listdir(directory)
    for f in files:
        pageCodeConversion(directory+f)
    
