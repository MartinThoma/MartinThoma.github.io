---
layout: post
title: Graphic filters
author: Martin Thoma
date: 2013-07-04 18:21:19.000000000 +02:00
category: Code
tags: HTML5, JavaScript, canvas
featured_image: 2013/07/laplace-filter-example-thumbnail.png
---
I begin to fall in love with JavaScript and HTML5. You can access your Webcam with JS! As an example, I've implemented some graphic filters.

<h2>Basics</h2>
<h3>HTML5</h3>
You need:
<ul>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas"><code>&lt;canvas&gt;</code></a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video"><code>&lt;video&gt;</code></a></li>
</ul>

This is the bare minimum HTML code you need for valid HTML:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Some title</title>
    </head>
    <body>
		<video autoplay id="vid" style="display:none;"></video>
		<canvas id="canvas" width="640" height="480"></canvas>
		<script type="text/javascript" src="graphic-filter.js">
		</script>
	</body>
</html>
```

<h3>JavaScript</h3>
Important functions / datastructures are:
<ul>
  <li><a href="https://developer.mozilla.org/en-US/docs/WebRTC/navigator.getUserMedia">getUserMedia</a>: see <a href="http://caniuse.com/stream">support by browsers</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/API/ImageData">ImageData</a>: WTF? The image is a ONE dimensional array of integers in 0, ..., 255. So the first 4 array elements describe the pixel (0|0) with its RGBA value</li>
</ul>

A starting point for your code might be:

```javascript
'use strict';

var video = document.querySelector("#vid");
var canvas = document.querySelector('#canvas');
var context = canvas.getContext('2d');
var localMediaStream = null;

var onCameraFail = function (e) {
    console.log('Camera did not work.', e);
};

setInterval(function snapshot() {
    if (localMediaStream) {
        context.drawImage(video, 0, 0);
        var width = 640;
        var height = 480;
        var imgDataNormal = context.getImageData(0, 0, width, height);
        var imgData = context.createImageData(width, height);

        // convert image to grayscale
        for (var i = 0; i < imgData.width*imgData.height*4; i += 4) {
            var r = imgDataNormal.data[i + 0];
            var g = imgDataNormal.data[i + 1];
            var b = imgDataNormal.data[i + 2];
            var brightness = (3*r+4*g+b)>>>3;
            imgData.data[i] = brightness;
            imgData.data[i+1] = brightness;
            imgData.data[i+2] = brightness;
        }

        context.putImageData(imgData, 0, 0);
    }
}, 500);

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL;
navigator.getUserMedia({video:true}, function (stream) {
    video.src = window.URL.createObjectURL(stream);
    localMediaStream = stream;
}, onCameraFail);
console.log(localMediaStream);
```

<h2>Interactive example</h2>
<div class="info">
You need a webcam for this:
<a href="../html5/graphic-filters/graphic-filters.htm" target="_blank">Open demonstration in new window</a>
</div>

This is what it should look like:
{% caption align="aligncenter" width="664" caption="Webcam example" url="../images/2013/07/graphic-webcam-html5-js-example.png" alt="Webcam example"  height="395" class="size-full wp-image-72801" %}

And it gives these results:
{% gallery %}
    ../images/2013/07/prewitt-x-filter-example.png  "Prewitt x-filter example"
    ../images/2013/07/prewitt-y-filter-example.png  "Prewitt y-filter example"
    ../images/2013/07/laplace-filter-example.png    "Laplace filter example"
{% endgallery %}

By the way, you can check if a website is currently accessing your webcam (with Google Chrome):

{% caption align="aligncenter" width="370" caption="Webcam indicator on tab in Google Chrome" url="../images/2013/07/webcam-red-dot.png" alt="Webcam indicator on tab in Google Chrome"  height="125" class="size-full wp-image-72811" %}

If you want to use these examples from your Android phone, you might have to enable getUserMedia. To do this, enable "Web RTC" in "chrome://flags":
{% caption align="aligncenter" width="180" caption="Enamble Web-RTC in Chrome for Android" url="../images/2013/07/enable-webrtc-180x300.png" alt="Enamble Web-RTC in Chrome for Android"  height="300" class="size-medium wp-image-73191" %}
