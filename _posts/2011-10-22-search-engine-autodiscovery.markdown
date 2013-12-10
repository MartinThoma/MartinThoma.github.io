---
layout: post
status: publish
published: true
title: Search Engine Autodiscovery
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 6771
wordpress_url: http://martin-thoma.com/?p=6771
date: 2011-10-22 11:12:07.000000000 +02:00
categories:
- Code
tags:
- Chrome
- Firefox
- Web Development
- HTML5
comments:
- id: 122891
  author: Phil Oertel
  author_email: phillipao@gmail.com
  author_url: http://philoertel.com
  date: !binary |-
    MjAxMi0wNS0wMiAwMTozNTozMiArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNS0wMSAyMzozNTozMiArMDIwMA==
  content: ! "Thanks Martin, this is the only writing I was able to find on Chrome's
    search engine discovery feature. Would you mind sharing how you were able to figure
    out Chrome's behavior? A pointer to the source maybe? Or was this through trial
    and error?\r\n\r\nI was surprised to see the limited conditions for Chrome discovery:
    type=\"search\" or name=\"s\". I checked one of the search engines added to my
    preferences and saw an . Might this pattern also trigger an add?\r\n\r\nOf course,
    this is an open source browser and it's not worth speculating too much, but this
    gets me close enough that it doesn't seem worth it to go spelunking in the Chromium
    source. Thank you!"
- id: 122991
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNS0wMiAwNjozNzoyNSArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNS0wMiAwNDozNzoyNSArMDIwMA==
  content: ! "Hi Phil,\r\n\r\ndie original source was (as I wrote in my post) Jan
    Phillip. He wrote his post in German and I thought this might be interesting for
    more people, so I've translated it. He found got to know this behaviour by trial
    and error.\r\n\r\nIf you really want to find out more, you can check the source
    (as you mentioned):\r\n\r\nCheckout of the Chromium repository:\r\n<source>svn
    checkout http://chromium.googlecode.com/svn/trunk/ chromium-read-only</source>\r\nAfter
    that you can grep through the source. Or you could use the <a href=\"http://code.google.com/p/chromium/source/search?q=search+engine+discovery&origq=search+engine+discovery&btnG=Search+Trunk\"
    rel=\"nofollow\">online interface</a>.\r\n\r\nI was interested if I could
    find the relevant pages in a couple of minutes (it worked :D). Here you are:\r\n*
    <a href=\"http://code.google.com/searchframe#OAMlx_jo-ck/src/chrome/test/pyautolib/pyauto.py&exact_package=chromium&q=GetSearchEngineInfo&ct=rc&cd=1&sq=\"
    rel=\"nofollow\">pyauto.py</a>: Take a look at GetSearchEngineInfo, AddSearchEngine\r\n*
    <a href=\"http://code.google.com/searchframe#OAMlx_jo-ck/src/chrome/test/functional/search_engines.py&exact_package=chromium\"
    rel=\"nofollow\">Testing</a>: This is probably not interesting for you, but
    I would like to take a look at it later (now I have to get ready for University).
    I got interested in automatic testing. (By the way: Thanks for pointing to PHPUnit
    on your website. I'll definitely take a look at it. Do you know some good pages
    with tutorials how to use it?)\r\n\r\nI've just read that you work at Google.
    Its a little bit funny that I can tell you something about a Google product (I
    know that Google is big and nobody can know all details of all projects of Google.
    Nevertheless, it's funny :-) )"
featured_image: 2011/10/firefox-add-search-engine-thumb.png
---
Recently I read a very good post about search engine autodiscovery <a href="http://www.knallisworld.de/blog/2011/04/14/autodiscovery-der-searchengine-in-google-chrome-opensearch/">by Jan Phillip</a>. Did you know that many browsers can detect an internal search engine automatically? 
Firefox gives you the possibility to add such a search engine to your browser:
{% caption align="aligncenter" width="294" caption="Firefox: Add search engine detected via autodiscovery" url="../images/2011/10/firefox-add-search-engine.png" alt="Firefox: Add search engine detected via autodiscovery" title="Firefox: Add search engine detected via autodiscovery" height="236" class="size-full wp-image-6921" %}

<h2>OpenSearch</h2>
<a href="http://en.wikipedia.org/wiki/OpenSearch">OpenSearch</a> is a collection of technologies. This project aims to create a standard for publishing the metadata which describes a search engine: name, description, URL-pattern, language, ...

A <abbr title="OpenSearch Description Document">OSSD</abbr> looks like this:
[xml]<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
    <ShortName>Example</ShortName>
    <Description>My example search engine</Description>
    <InputEncoding>UTF-8</InputEncoding>
    <Image height="16" width="16" type="image/x-icon">
        http://example.org/favicon.ico
    </Image>
    <Url type="text/html" 
         template="http://example.org/index.html#search={searchTerms}"/>
</OpenSearchDescription>[/xml]

The browser needs a hint where it can find the OSSD. So you have to add the following tag to your website:
[xml]<link title = "Example" 
      type  = "application/opensearchdescription+xml" 
      rel   = "search" 
      href  = "http://example.org/opensearch.xml">[/xml]

Now you can add the websites internal search engine automatically to Chrome and easily to Firefox and Internet Explorer 8+. 

Additionally, you can add this little piece of JavaScript to tell Firefox 2+ and Internet Explorer 7+ that your site supports OpenSearch:
{% highlight javascript %}window.external.AddSearchProvider("http://exampl.org/opensearch.xml");{% endhighlight %}

<h2>Google Chrome Autodiscovery</h2>
Google doesn't provide a <abbr title="user interface">UI</abbr> for adding an internal search engine. Instead, you can add it via Settings:

{% caption align="aligncenter" width="300" caption="Add Search Engines via Settings in Google Chrome" url="../images/2011/10/google-chrome-add-search-300x206.png" alt="Add Search Engines via Settings in Google Chrome" title="Add Search Engines via Settings in Google Chrome" height="206" class="size-medium wp-image-6891" %}

Chrome also adds the sites internal search engine automatically. Did you ever notice this? Here are some screenshots:

{% caption align="aligncenter" width="659" caption="Google Chrome Search - Hit tab to search this site" url="../images/2011/10/google-chrome-search-1.png" alt="Google Chrome Search - Hit tab to search this site" title="Google Chrome Search - Hit tab to search this site" height="31" class="size-full wp-image-6841" %}

{% caption align="aligncenter" width="656" caption="Google Chrome Search - Search with the websites internal search engine" url="../images/2011/10/google-chrome-search-2.png" alt="Google Chrome Search - Search with the websites internal search engine" title="Google Chrome Search - Search with the websites internal search engine" height="30" class="size-full wp-image-6851" %}

Interestingly the auto discovery only works if the search engine is at the homepage. You have to have either an input field of the type "search" or of the type "text" with the name "s":
[html]<form>
  <input type="search" name="s" />
</form>[/html]

or

[html]<form>
  <input type="text" name="s" />
</form>[/html]

<h2>Drawbacks</h2>
<ul>
  <li>It seems as if Safari didn't support OSSD natively. (14.04.2011)</li>
  <li>Internet Explorer 9 seems not to support OSSD.</li>
  <li>No support by Opera.</li>
</ul>

<h2>This article in a nutshell</h2>
<ul>
  <li>opensearch.xml gives meta information about your websites internal search engine</li>
  <li>For Chromes autodiscovery you will need to add an input fild with "type=search" or "name=s"</li>
  <li>It is not necessary for Chrome that the user can see the form (display:none with CSS) nor that it the site start page is loaded long (meta redirect after 0 seconds).</li>
  <li>Adding the search engine manually is possible in almost all browsers</li>
  <li>With OSSD you can manage more than one internal search engine.</li>
</ul>

<h2>Further reading</h2>
<ul>
  <li>OpenSearch.org:
    <ul>
      <li><a href="http://www.opensearch.org/Community/OpenSearch_search_clients">OpenSearch search clients</a></li>
  <li><a href="http://www.opensearch.org/Documentation/Developer_best_practices_guide">Developer best practices guide</a></li>
    </ul>
  </li>
  <li>David Walsh: <a href="http://davidwalsh.name/open-search">Add Your Website to Firefox&rsquo;s Search Bar Using OpenSearch XML</a>.</li>
</ul>
