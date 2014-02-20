---
layout: post
title: Drawing on Canvas
author: Martin Thoma
date: 2014-02-18
categories:
- Code
tags:
- HTML
- JavaScript
featured_image:
---
Did you know that you can draw with HTML5 and JavaScript?

The following draws a U-Shape

## MWE

```html
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <canvas id="myCanvas" width="800" height="600"></canvas>
    <script>
      var canvas = document.getElementById('myCanvas');
      var context = canvas.getContext('2d');

      context.moveTo(100, 150);
      context.lineTo(450, 50);
      context.lineTo(10, 50);
      context.lineTo(450, 100);
      context.stroke();
      context.closePath();
    </script>
  </body>
</html>
```

## Specification
I think "W3C - HTML Canvas 2D Context" is the right place to look at. But I'm confused. According to Wikipedia ([source][https://en.wikipedia.org/wiki/World_Wide_Web_Consortium#Specification_Maturation]), "[Editors Drafts][http://www.w3.org/html/wg/drafts/2dcontext/html5_canvas_CR/]" (from 18 February 2014) are before "[Candidate Recommendations][http://www.w3.org/TR/2dcontext]" (from 6 August 2013). And there is even a "Nightly" Version ([link][http://www.w3.org/html/wg/drafts/2dcontext/html5_canvas/]).

I'll go with the "Candidate Recommendation" from 6th of August in the following.

* Each object implementing the CanvasPathMethods interface has a path. A path has a list of zero or more subpaths.
* `context.moveTo(x, y)`: Creates a new subpath with the given point.
* `context.closePath()`: Marks the current subpath as closed, and starts a new subpath with a point the same as the start and end of the newly closed subpath.
* `context.lineTo(x, y)`: Adds the given point to the current subpath, connected to the previous one by a straight line.

So when I understand this correctly, then `canvas` has a path object. Always.
