---
layout: post
title: File Sizes
slug: file-sizes
author: Martin Thoma
date: 2018-12-30 20:00
category: Cyberculture
tags: file, size, storage, format, image, jpg
featured_image: logos/star.png
---
<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>
I was just wondering how long a camera which takes images in 5s intervalls and
has 256 GB of storage could take photos. This is quite easy to answer as soon
as you know the average file size. For that, however, I could not find a good
answer in the first 3 Google results. Let's fix that.


## Images

### JPG

Don't forget that JPEG supports different compression levels!

<table>
    <tr>
        <th>Resolution (in px x px)</th>
        <th>Pixel</th>
        <th>MP</th>
        <th>Average file size<br/>(1% - 99% percentile)</th>
    </tr>
    <tr>
        <td>32 x 32</td>
        <td>1024</td>
        <td></td>
        <td>1.0kB (0.5kB - 1.6kB)</td>
    </tr>
    <tr>
        <td>96 x 128</td>
        <td>12288</td>
        <td></td>
        <td>3.8kB (1.0kB - 7.9kB)</td>
    </tr>
    <tr>
        <td>192 x 256</td>
        <td>49152</td>
        <td></td>
        <td>8.3kB (2.2kB - 18.8kB)</td>
    </tr>
    <tr>
        <td>384 x 512</td>
        <td>196608</td>
        <td>0.2</td>
        <td>18.0kB (5.4kB - 41.8kB)</td>
    </tr>
    <tr>
        <td>512 x 512</td>
        <td>262144</td>
        <td>0.3</td>
        <td>21.0 kB (6.5 kB - 47.8kB)</td>
    </tr>
    <tr>
        <td>768 x 1024</td>
        <td>786432</td>
        <td>0.8</td>
        <td></td>
    </tr>
    <tr>
        <td>3072 x 4096</td>
        <td>12582912</td>
        <td>13</td>
        <td></td>
    </tr>
    <tr>
        <td>6144 x 8192</td>
        <td>50331648</td>
        <td>50</td>
        <td></td>
    </tr>
</table>


### PNG

<table>
    <tr>
        <th>Resolution (in px x px)</th>
        <th>Pixel</th>
        <th>MP</th>
        <th>Average file size<br/>(1% - 99% percentile)</th>
    </tr>
    <tr>
        <td>32 x 32</td>
        <td>1024</td>
        <td></td>
        <td>1.3kB (0.4kB - 2.5kB)</td>
    </tr>
    <tr>
        <td>96 x 128</td>
        <td>12288</td>
        <td></td>
        <td>3.7kB (0.5kB - 9.6kB)</td>
    </tr>
    <tr>
        <td>192 x 256</td>
        <td>49152</td>
        <td></td>
        <td>7.2kB (0.5kB - 20.0kB)</td>
    </tr>
    <tr>
        <td>384 x 512</td>
        <td>196608</td>
        <td>0.2</td>
        <td>15.0kB (0.8kB - 42.9kB)</td>
    </tr>
    <tr>
        <td>512 x 512</td>
        <td>262144</td>
        <td>0.3</td>
        <td>9.3 kB (0.5 kB - 25.5kB)</td>
    </tr>
    <tr>
        <td>768 x 1024</td>
        <td>786432</td>
        <td>0.8</td>
        <td></td>
    </tr>
    <tr>
        <td>3072 x 4096</td>
        <td>12582912</td>
        <td>13</td>
        <td></td>
    </tr>
    <tr>
        <td>6144 x 8192</td>
        <td>50331648</td>
        <td>50</td>
        <td></td>
    </tr>
</table>


The average file sizes were calculated like this:

* 512 x 512: Downloaded [380 essential icons](https://www.flaticon.com/packs/essential-collection) of Smashicons

If necessary, the size / file format was adjusted with `convert` (ImageMagick).


## See also

* [Converting Files with Linux](https://martin-thoma.com/converting-files-with-linux/)
