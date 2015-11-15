---
layout: post
title: Migrate from Jekyll to Pelican
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Rating
featured_image: logos/star.png
---

## Highlight blocks

Get rid of blocks like

```text
{% highlight whatever-lang %}
bla bla code
bla
{% endhighlight %}
```

and use instead:

```text
```bash
```
```

In sublime text, you can use the following search regex:

```text
\{% highlight (.*?) %\}(.*?)\{% endhighlight %\}
```

and replace it with

```text
\n```\1\n\2\n```\n
```

## See also

* https://jawher.me/2012/10/19/moving-from-jekyll-to-pelican/