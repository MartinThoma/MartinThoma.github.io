---
layout: post
status: publish
published: true
title: How to analyze Mailman archives
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 76293
wordpress_url: http://martin-thoma.com/?p=76293
date: 2013-08-18 21:23:49.000000000 +02:00
categories:
- Cyberculture
tags:
- Bash
- Mailman
- discussion
comments: []
---
All mailing lists I use are <a href="http://en.wikipedia.org/wiki/GNU_Mailman">GNU Mailman</a> lists. This software provides archives of all Emails that were send over the list. 

They look like this:
[caption id="attachment_76298" align="aligncenter" width="300"]<a href="http://martin-thoma.com/wp-content/uploads/2013/08/mailman-list-archive.png"><img src="http://martin-thoma.com/wp-content/uploads/2013/08/mailman-list-archive-300x277.png" alt="GNU Mailman list archive" width="300" height="277" class="size-medium wp-image-76298" /></a> GNU Mailman list archive[/caption]

Once in a while, I would like to search if a topic was already discussed. Here is how you can do it:

<h2>Download archives</h2>
{% highlight bash %}wget --save-cookies cookie.txt --post-data 'username=user&amp;password=pass' -A gz -m -p -E -k -K -np https://lists.abc.org/mailman/blub/{% endhighlight %}

<h2>Rename archives</h2>
{% highlight bash %}for file in *.txt.gz; do mv "$file" "${file%.txt.gz}.txt"; done{% endhighlight %}

To make them sortable:
{% highlight bash %}
for file in *January.txt; do mv "$file" "${file%January.txt}01.txt"; done
for file in *February.txt; do mv "$file" "${file%February.txt}02.txt"; done
for file in *March.txt; do mv "$file" "${file%March.txt}03.txt"; done
for file in *April.txt; do mv "$file" "${file%January.txt}04.txt"; done
for file in *May.txt; do mv "$file" "${file%May.txt}05.txt"; done
for file in *June.txt; do mv "$file" "${file%June.txt}06.txt"; done
for file in *July.txt; do mv "$file" "${file%July.txt}07.txt"; done
for file in *August.txt; do mv "$file" "${file%August.txt}08.txt"; done
for file in *September.txt; do mv "$file" "${file%September.txt}09.txt"; done
for file in *October.txt; do mv "$file" "${file%October.txt}10.txt"; done
for file in *November.txt; do mv "$file" "${file%November.txt}11.txt"; done
for file in *December.txt; do mv "$file" "${file%December.txt}12.txt"; done
{% endhighlight %}

<h2>Analyze them</h2>
To analyze the archives properly, you should perhaps first import all emails in a relational database. But with <code>grep</code> you could also do simple keyword searches.
