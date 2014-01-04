---
layout: post
title: ! 'Python: Check Wiki-references for citation template'
author: Martin Thoma
date: 2011-09-24 11:39:40.000000000 +02:00
categories:
- Code
tags:
- Python
- Wikipedia
- RegEx
featured_image: 2011/09/Python-Logo.png
---
Wikipedia articles are full of references. Those references should be formatted the same way. It is much easier to use a template for citations than trying to guess the right way how to cite. Unfortunately most wikipedia users don't know the <a href="http://en.wikipedia.org/wiki/Template:Citation" title="Template:Citation">Template:Citation</a>. 

So I try to fix all manual styled citations when I edit an article. Doing this manually is quite time intensive. This is the reason why I wrote a little Python-script.

<h2>Examples</h2>

```html
<ref>[http://peter.mapledesign.co.uk/weblog/archives/python-is-slow Python is... slow?] December 21st, 2004 &mdash; Peter Bowyer&rsquo;s weblog]</ref>
```

should be 

```html
<ref>{{Citation |url=http://peter.mapledesign.co.uk/weblog/archives/python-is-slow |title=Python is... slow? |accessdate=September 24, 2011}}</ref>
```

```html
<ref>[http://www.nongnu.org/pydbc/ Contracts for Python], PyDBC</ref>
```

should be 

```html
{{Citation |url=http://www.nongnu.org/pydbc/ |title=Contracts for Python |accessdate=September 24, 2011}}
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

{% gist 5555251 %}

We are now able to access the needed information. Now we need to get the references without templates. To do so, I will use the <a href="http://docs.python.org/library/re.html">Python re module</a>:

{% gist 5555251 %}

Here is the full script:
{% gist 5555251 %}

This can be improved in several ways:
<ul>
    <li>Checking automatically the title / dead links</li>
    <li>Trying to find the publication date automatically</li>
    <li>Skip links with <a href="http://en.wikipedia.org/wiki/Template:Dead_link" title="Template:Dead link">Templade:Dead link</a></li>
    <li>Search also for <ref name="xyz">Text</ref></li>
</ul>

Here is the <a href="http://en.wikipedia.org/w/index.php?title=Python_%28programming_language%29&action=historysubmit&diff=452167384&oldid=452164712">Wikipedia diff page</a>. My little script seems to work.
