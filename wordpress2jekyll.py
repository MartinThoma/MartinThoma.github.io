#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys

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
    
    with open(filename, 'w') as f:
        f.write(content)

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
    
