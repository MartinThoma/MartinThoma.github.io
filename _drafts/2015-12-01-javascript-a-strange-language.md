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

Just like I did before for [PHP](//martin-thoma.com/php-a-strange-language/),
I would like to show some strange features of JavaScript. Quite a lot comes
from [JS WAT Talk reup](https://www.youtube.com/watch?v=FqhZZNUyVFM).



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

## Unreasonable Difficult

Things which are difficult in JS, but easy in other (similar) languages.

TODO


## Unreasonable Specs

If you really want to read the specs, here you are: [Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm) (6th edition from June 2015).
However, I'll link the mozilla resources now as the specs are only available as
PDF (which is a shame :-/).

### Number.MIN_VALUE

```javascript
Number.MAX_VALUE > 0;  // true
Number.MIN_VALUE < 0;  // false
```

> The Number.MIN_VALUE property represents the smallest positive numeric value representable in JavaScript.

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE)


### Coercion

```javascript
1 < 2 < 3;  // true
3 > 2 > 1;  // false
```

See [Why does “alert(3>2>1)” alert “false”](http://stackoverflow.com/a/5852071/562769)
and [What exactly is Type Coercion in Javascript?](http://stackoverflow.com/q/19915688/562769)

### Plus operations

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


### Mind the spaces

```javascript
42.toFixed(2);  // Syntax Error
42. toFixed(2);  // Syntax Error
42 .toFixed(2);  // "42.00"
42 . toFixed(2);  // "42.00"
42.0.toFixed(2);  // "42.00"
42..toFixed(2);  // "42.00"
```

### Stringification

```javascript
JSON.stringify(-0);  // "0"
String(-0);          // "0"
-0 + "";             // "0"
```


### New Octal notation

```javascript
Number("0O0");  // "0"
Number("0X0");  // "0"
```

### Number conversion

```javascript
Number({});  // NaN
Number([]);  // "0"
```


## Cross-browser Quircks

TODO

## Resources

* Kyle Simspon: [What the... JavaScript?](https://www.youtube.com/watch?v=2pL28CcEijU). On YouTube (38:16 min).


## See also

* [wtfjs.com](http://wtfjs.com/)
* [youdontknowjs.com](http://youdontknowjs.com)
