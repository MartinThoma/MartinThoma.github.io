---
layout: post
title: JavaScript - A strange language
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- JavaScript
- Programming
featured_image: logos/star.png
---

Just like I did before for [PHP](http://martin-thoma.com/php-a-strange-language/),
I would like to show some strange features of JavaScript. Quite a lot comes
from [JS WAT Talk reup](https://www.youtube.com/watch?v=FqhZZNUyVFM).

## Plus operations

```javascript
> [] + []
""
```

```javascript
> [] + {}
"[object Object]"
```

```javascript
> {} + []
0
```

```javascript
> {} + {}
NaN
```

## Arrays

```javascript
> Array(16)
[undefined × 16]
> Array(16).join("wat")
"watwatwatwatwatwatwatwatwatwatwatwatwatwatwatwat"
> Array(16).join("wat" + 1)
"wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1wat1"
> Array(16).join("wat" - 1)
"NaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaNNaN"
```