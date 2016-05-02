---
layout: post
title: Python: Check Wiki-references for citation template
author: Martin Thoma
date: 2011-09-24 11:39:40.000000000 +02:00
category: Code
tags: Python, Wikipedia, RegEx
featured_image: 2011/09/Python-Logo.png
---
Wikipedia articles are full of references. Those references should be formatted the same way. It is much easier to use a template for citations than trying to guess the right way how to cite. Unfortunately most Wikipedia users don't know the <a href="http://en.wikipedia.org/wiki/Template:Citation" title="Template:Citation">Template:Citation</a>. 

So I try to fix all manual styled citations when I edit an article. Doing this manually is quite time intensive. This is the reason why I wrote a little Python-script.

<h2>Examples</h2>

```html
<ref>[http://peter.mapledesign.co.uk/weblog/archives/python-is-slow Python is... slow?] December 21st, 2004 &mdash; Peter Bowyer&rsquo;s weblog]</ref>
```

should be 

```html
<ref>{% raw %}{{Citation |url=http://peter.mapledesign.co.uk/weblog/archives/python-is-slow |title=Python is... slow? |accessdate=September 24, 2011}}{% endraw %}</ref>
```

```html
<ref>[http://www.nongnu.org/pydbc/ Contracts for Python], PyDBC</ref>
```

should be 

```html
<ref>{% raw %}{{Citation |url=http://www.nongnu.org/pydbc/ |title=Contracts for Python |accessdate=September 24, 2011}}{% endraw %}</ref>
```

So, all that has to be done is 
<ol>
	<li>Finding all <ref>-Tags without a template in one article</li>
        <li>Trying to find the URL of this reference</li>
        <li>Filling out as much as possible for the user</li>
        <li>Asking the user for missing information</li>
        <li>Returning the new article wiki source code</li>
</ol>

<h2>Downloading wiki source code</h2>
Wikipedia offers an <a href="http://en.wikipedia.org/w/api.php" title="Wikipedia API">API</a> for accessing the needed information. I will use this API and Pythons <a href="http://docs.python.org/library/optparse.html">optparse</a>, <a href="http://www.crummy.com/software/BeautifulSoup/documentation.html">BeautifulSoup</a> and <a href="http://docs.python.org/library/htmlparser.html">HTMLParser</a> to get the raw wiki text in UTF-8 encoding:

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import urllib2
from optparse import OptionParser
from BeautifulSoup import BeautifulStoneSoup
import HTMLParser
 
parser = OptionParser()
parser.add_option("-l", "--lemma", dest="lemma",
                       default="Python", type="string",
                       help="Which lemma should be checked?")
parser.add_option("-m", "--language", dest="language",
                       default="en", type="string",
                       help="Which langauge should be used " +
                            "(english wiki, geman wiki, ... )")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="Show more information.")
(options, args) = parser.parse_args()
 
def load(lemma, language="en", format="xml"):
    """ Get the Wikipedia Source Text (not the HTML source code) 
 
        format:xml,json, ...
        language:en, de, ...
 
        Returns None if page doesn't exist
    """
    lemma     = lemma.replace(" ", "_")
    url       = 'http://' + language + '.wikipedia.org/w/api.php' + \
                '?action=query&format=' + format + \
                '&prop=revisions&rvprop=content' + \
                '&titles=' + lemma
    request   = urllib2.Request(url)
    handle    = urllib2.urlopen(request)
    text      = handle.read()
    if format == 'xml':
        soup = BeautifulStoneSoup(text)
        rev  = soup.rev
        if rev != None:
            text = unicode(rev.contents[0])
            text = HTMLParser.HTMLParser().unescape(text)
            text = text.encode( "utf-8" )
        else:
            return None
    return text
```

We are now able to access the needed information. Now we need to get the references without templates. To do so, I will use the <a href="http://docs.python.org/library/re.html">Python re module</a>:

```python
import re

def getRef(page):
    """ Get all references without templates """
    pattern = "(<ref>\[.+?</ref>)"
    prog = re.compile(pattern)
    m    = re.findall(pattern, page)
    return m
```

Now the single references have to get parsed and the user has to confirm or edit the results:

```python
{% raw %}
import readline
from datetime import date

def rlinput(prompt, prefill=''):
    """ Promt the user for input, but prefill it. """
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
      return raw_input(prompt)
    finally:
      readline.set_startup_hook()

def improve(references, page):
    """ Try to guess the right formatation for each reference and ask 
        the user to confirm or edit the formatation of the reference. """

    urlPattern = "http.+? "
    urlPatternCompiled = re.compile(urlPattern)

    today = date.today()
    accessdate = str(today.strftime("%B %d, %Y"))


    for refOld in references:
        url = re.findall(urlPatternCompiled, refOld)
        refNew = "<ref>{{Citation " + \
                 "|url=" + str(url[0]) + \
                 "|title= " + \
                 "|accessdate="  + accessdate + \
                 "}}</ref>"

        refNew = rlinput(refOld + " (old):\n", refNew)
        page = page.replace(refOld, refNew)
        print ""

    return page
{% endraw %}
```

Here is the full script:

```python
{% raw %}
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import urllib2
from optparse import OptionParser
from BeautifulSoup import BeautifulStoneSoup
import HTMLParser

import re

import readline
from datetime import date
 
parser = OptionParser()
parser.add_option("-l", "--lemma", dest="lemma",
                       default="Python", type="string",
                       help="Which lemma should be checked?")
parser.add_option("-f", "--file", dest="filename",
                  help="write corrected wiki source code to FILE", 
                  metavar="FILE", default="wikioutput.txt")
parser.add_option("-m", "--language", dest="language",
                       default="en", type="string",
                       help="Which langauge should be used " +
                            "(english wiki, geman wiki, ... )")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="Show more information.")
(options, args) = parser.parse_args()
 
def load(lemma, language="en", format="xml"):
    """ Get the Wikipedia Source Text (not the HTML source code) 
 
        format:xml,json, ...
        language:en, de, ...
 
        Returns None if page doesn't exist
    """
    lemma     = lemma.replace(" ", "_")
    url       = 'http://' + language + '.wikipedia.org/w/api.php' + \
                '?action=query&format=' + format + \
                '&prop=revisions&rvprop=content' + \
                '&titles=' + lemma
    request   = urllib2.Request(url)
    handle    = urllib2.urlopen(request)
    text      = handle.read()
    if format == 'xml':
        soup = BeautifulStoneSoup(text)
        rev  = soup.rev
        if rev != None:
            text = unicode(rev.contents[0])
            text = HTMLParser.HTMLParser().unescape(text)
            text = text.encode( "utf-8" )
        else:
            return None
    return text

def getRef(page):
    """ Get all references without templates """
    pattern = "(<ref>\[.+?</ref>)"
    prog = re.compile(pattern)
    m    = re.findall(prog, page)
    return m

def rlinput(prompt, prefill=''):
    """ Promt the user for input, but prefill it. """
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
      return raw_input(prompt)
    finally:
      readline.set_startup_hook()

def improve(references, page):
    """ Try to guess the right formatation for each reference and ask 
        the user to confirm or edit the formatation of the reference. """

    urlPattern = "http.+? "
    urlPatternCompiled = re.compile(urlPattern)

    today = date.today()
    accessdate = str(today.strftime("%B %d, %Y"))


    for refOld in references:
        url = re.findall(urlPatternCompiled, refOld)
        refNew = "<ref>{{Citation " + \
                 "|url=" + str(url[0]) + \
                 "|title= " + \
                 "|accessdate="  + accessdate + \
                 "}}</ref>"

        refNew = rlinput(refOld + " (old):\n", refNew)
        page = page.replace(refOld, refNew)
        print ""

    return page

if __name__ == '__main__':
    print("If you need more parameters like 'date': " + \
          "http://en.wikipedia.org/wiki/Template:Citation#" + \
          "Full_citation_parameters")
    page = load(options.lemma)
    references = getRef(page)
    page = improve(references, page)
    f = open(options.filename, 'w')
    f.write(page)
    f.close()
    print("Page has been written to %s." % options.filename)
{% endraw %}
```

This can be improved in several ways:
<ul>
    <li>Checking automatically the title / dead links</li>
    <li>Trying to find the publication date automatically</li>
    <li>Skip links with <a href="http://en.wikipedia.org/wiki/Template:Dead_link" title="Template:Dead link">Templade:Dead link</a></li>
    <li>Search also for <ref name="xyz">Text</ref></li>
</ul>

Here is the <a href="http://en.wikipedia.org/w/index.php?title=Python_%28programming_language%29&action=historysubmit&diff=452167384&oldid=452164712">Wikipedia diff page</a>. My little script seems to work.
