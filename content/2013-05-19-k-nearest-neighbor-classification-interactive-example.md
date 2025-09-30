---
layout: post
lang: en
title: k-nearest-neighbor classification and k-means - an interactive example
slug: k-nearest-neighbor-classification-interactive-example
author: Martin Thoma
date: 2013-05-19 15:23:11.000000000 +02:00
category: Code
tags: HTML5, KogSys, k-means, JavaScript, canvas, Clustering
featured_image: 2013/05/k-means-interesting-setting-thumb.png
---
<iframe src="../html5/clustering/clustering.htm" width="98%" height="700px"></iframe>

When the circle has exactly the same number of blue / green dots in it, it will
be green.

When you move the mouse over the box, everything will be calculated and drawn
again. This leads to flickering with k-means, as k-means includes a random
choice of cluster centers.

<h2>Changelog</h2>
<table>
  <tr>
    <th>Version</th>
    <th>Change</th>
  </tr>
  <tr>
    <td><span class="hint" title="974b52110126bfd7169622c7041506f56beae1cf">2.2</span></td>
    <td>Cluster centers have the same color as the clustered points; when one cluster has no points (and there are at least as many points as clusters) everything gets recalculated</td>
  </tr>
  <tr>
    <td><span class="hint" title="1c37b0a860a419668e54c3c6c6189148485d3ea5">2.1</span></td>
    <td>users can now specify an arbitrary number of classes; ctrl-key change of class was removed; added hints to configuration options</td>
  </tr>
  <tr>
    <td><span class="hint" title="4ed5997089...">2.0</span></td>
    <td>k-means implemented</td>
  </tr>
  <tr>
    <td>1.0</td>
    <td>k-nearest neighbor implemented</td>
  </tr>
</table>

Code is <a href="https://github.com/MartinThoma/algorithms/tree/master/k-nearest-neighbor">on GitHub</a>.
You may use it for free, but you should add a link to this article.

<h2>See also</h2>

<figure class="aligncenter">
            <a href="../images/2013/05/k-nearest-neighbor-interesting-setting.png"><img src="../images/2013/05/k-nearest-neighbor-interesting-setting.png" alt="One interesting setting for k=2" style="max-width:401px;max-height:401px" class="size-full wp-image-66811"/></a>
            <figcaption class="text-center">One interesting setting for k=2</figcaption>
        </figure>

<figure class="aligncenter">
            <a href="../images/2013/05/k-means-good-vs-bad.png"><img src="../images/2013/05/k-means-good-vs-bad.png" alt="k-means: Good vs. Bad" style="max-width:800px;max-height:379px" class="size-full wp-image-67701"/></a>
            <figcaption class="text-center">k-means: Good vs. Bad</figcaption>
        </figure>

<ul>
  <li><a href="http://en.wikipedia.org/wiki/Voronoi_diagram">Voronoi diagram</a></li>
  <li><a href="http://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">K-nearset neighbor</a></li>
  <li><a href="http://en.wikipedia.org/wiki/K-means_clustering">k-means clustering</a></li>
  <li>Udacity: Introduction to A.I: <a href="https://www.youtube.com/watch?v=zaKjh2N8jN4">k-means</a></li>
</ul>
