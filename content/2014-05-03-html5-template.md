---
layout: post
title: HTML5 Template
author: Martin Thoma
date: 2014-05-03 20:43
category: Code
tags: HTML5, Sublime
featured_image: logos/html.png
---

Once in a while I need to create simple HTML pages. This is the template
I use:

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>TODO</title>
</head>
<body>
    <h1>TODO</h1>
</body>
</html>
```

and as a sublime snippet:

```xml
<snippet>
    <content><![CDATA[
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>${1:Title}</title>
</head>
<body>
    <h1>${2:Header}</h1>
    ${3:Content}
</body>
</html>
]]></content>
    <tabTrigger>html5</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
    <!-- <scope>source.python</scope> -->
</snippet>
```