---
layout: post
title: Migrate from Jekyll to Pelican
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Jekyll
- Blogging
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
\{% highlight (.*?) %\}([\s\S]*?)\{% endhighlight %\}
```

and replace it with

```text
\n```\1\n\2\n```\n
```


## MathJax and Markdown

The problem with MathJax and Markdown (e.g. [CommonMark](http://commonmark.org/))
is that it uses the `\` for escaping. Especially for multi-line math tags this
is a real issue. However, CommonMark gets deactivated when
it's inside of an block-level HTML tag. This means inside of an HTML-Tag I have to write
`\(\mathbb{R}\)` and outside of and HTML tag I have to write `\\(\mathbb{R}\\)`.

The problem of using `$` for triggering MathJax is that PHP makes use of it and
that it is the US-Dollar currency symbol.

### Inline Math

Search for

```text
\$([\s\S]*?)\$
```

and replace it by the following if it is inside a HTML tag

```text
\\(\1\\)
```

or with the following if it is not

```text
\\\\(\1\\\\)
```

### Block Math


## See also

* https://jawher.me/2012/10/19/moving-from-jekyll-to-pelican/