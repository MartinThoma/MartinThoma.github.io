---
layout: post
status: publish
published: true
title: ! 'What does #!/usr/bin/python mean?'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 63591
wordpress_url: http://martin-thoma.com/?p=63591
date: 2013-04-16 18:23:17.000000000 +02:00
categories:
- Code
tags:
- Python
comments: []
featured_image: 2011/09/Python-Logo.png
---
You've probably already seen one of the following lines:

{% highlight text %}
#!/bin/sh
#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/perl
#!/usr/bin/php
#!/usr/bin/ruby
{% endhighlight %}

This is a <a href="http://en.wikipedia.org/wiki/Shebang_%28Unix%29">shebang</a>. It's a directive for your command line interpreter how it should execute a script.

For example, you have a file with this content:

{% highlight python %}
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
print(sys.version_info)
{% endhighlight %}

Now you can execute it via <code>python3 yourFile.py</code>. But alternatively, you can make it executable and simply type <code>./yourFile.py</code>

By the way, you should use <code>#!/usr/bin/env python</code> <a href="http://stackoverflow.com/q/1352922/562769">for some reasons</a>.
