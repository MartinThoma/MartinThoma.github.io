---
layout: post
status: publish
published: true
title: Zero Mean Normalized Cross-Correlation
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 71801
wordpress_url: http://martin-thoma.com/?p=71801
date: 2013-06-28 22:15:45.000000000 +02:00
categories:
- Code
- The Web
tags:
- KogSys
comments: []
featured_image: 2013/06/image-correlation.png
---
{% caption align="alignright" width="128" caption="An image from Tsukuba University. This is one of hundreds of images that you can use to test your algorithms. Link is below." url="../images/2013/06/image-correlation.png" alt="Image correlation test image" title="" height="128" class="size-full wp-image-71931" %}

Zero Mean Normalized Cross-Correlation or shorter ZNCC is an integer you can get when you compare two grayscale images.

Lets say you have a webcam at a fixed position for security. It takes images all the time, but most of the time the room is empty. So quite a lot of images will not be interesting. They only waste space. So you want to get rid of those redundant images.

BUT those images are not identical! Even if the scenery didn't change, your sensor will produce slightly different results. A human will not notice them, but you can't simply compare images bit by bit. Even if you could, the images will be different because the sun moved (and so do shadows) and perhaps you have a clock in the image.

Now you can solve this problem with various techniques.

I want to describe those techniques in a very general way. As the images in other scenarios might have different sizes and you probably don't want to compare whole images, I'll assume you have a part of both image of size $(2n+1) \times (2n+1)$. The pixel in the center has coordinates $(u_1, v_1)$ for the part of the first image and $(u_2, v_2)$ for the second image.

<h2>Sum of squared differences</h2>
Go through all pixels, get the difference of both and add up the squares:

$\displaystyle SSD(Img_1, Img_2, u_1, v_1, u_2, v_2, n) := \sum_{i=-n}^n \sum_{j=-n}^n \left ( Img_1(u_1+i, v_1+j) - Img_2(u_2 + i, v_2 + j) \right )^2$

When SSD is small, both images are very similar. Wehn SSD is 0, the images are identical.

<h2>Zero Mean Normalized Cross-Correlation</h2>
The average gray value is:
$\displaystyle \overline{Img}(u, v, n) := \frac{1}{(2n+1)^2} \sum_{i=-n}^n \sum_{j=-n}^n Img(u+i, v+j)$

The standard deviation is:
$\displaystyle \sigma(u, v, n) := \sqrt{\frac{1}{(2n+1)^2} \left (\sum_{i=-n} \sum_{j=-n}^n (Img(u +i, v+j)-\overline{Img}(u, v, n))^2 \right )}$

The ZNCC is defined as:

$\displaystyle ZNCC(Img_1, Img_2, u_1, v_1, u_2, v_2, n) := \frac{\frac{1}{(2n+1)^2}\sum_{i=-n}^n \sum_{j=-n}^n \prod_{t=1}^2 \left (Img_t (u_t+i,v_t+j) - \overline{Img}(u_t, v_t, n) \right )}{\sigma_1(u_1, v_1, n) \cdot \sigma_2(u_2, v_2, n)}$

The higher the ZNCC gets, the more are those two images correlated.
(I think the value is always in [0, 1])

Here is some Python code:

{% highlight python %}
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getAverage(img, u, v, n):
    """img as a square matrix of numbers"""
    s = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            s += img[u+i][v+j]
    return float(s)/(2*n+1)**2

def getStandardDeviation(img, u, v, n):
    s = 0
    avg = getAverage(img, u, v, n)
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            s += (img[u+i][v+j] - avg)**2
    return (s**0.5)/(2*n+1)

def zncc(img1, img2, u1, v1, u2, v2, n):
    stdDeviation1 = getStandardDeviation(img1, u1, v1, n)
    stdDeviation2 = getStandardDeviation(img2, u2, v2, n)
    avg1 = getAverage(img1, u1, v1, n)
    avg2 = getAverage(img2, u2, v2, n)

    s = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            s += (img1[u1+i][v1+j] - avg1)*(img2[u2+i][v2+j] - avg2)
    return float(s)/((2*n+1)**2 * stdDeviation1 * stdDeviation2)

if __name__ == "__main__":
    A  = [[1,2,3],[4,5,6],[7,8,9]]
    B1 = [[1,2,3],[4,5,6],[7,8,9]]
    B2 = [[1,2,3],[4,5,6],[7,8,7]]
    print(zncc(A, B1, 1,1,1,1, 1))
    print(zncc(A, B2, 1,1,1,1, 1))
{% endhighlight %}

<h2>See also</h2>
<ul>
  <li><a href="http://www.site.uottawa.ca/research/viva/projects/imagepairs/">Feature point image matching</a></li>
  <li><a href="http://www.cvlab.cs.tsukuba.ac.jp/index.php?CVLAB%20Home%20Page">Tsukuba University stereo images</a>: Just in case you want to try those algorithms</li>
  <li><a href="http://siddhantahuja.wordpress.com/tag/normalized-cross-correlation/">Correlation based similarity measures-Summary</a></li>
  <li><a href="http://www.ti.uni-bielefeld.de/downloads/publications/diploma_theses/ba11_bboettcher_illuminationchange.pdf">Bachelorarbeit</a>: Bildvorverarbeitung und Bild&auml;hnlichkeitsfunktionen f&uuml;r beleuchtungstolerante visuelle Navigation (German)</li>
</ul>
