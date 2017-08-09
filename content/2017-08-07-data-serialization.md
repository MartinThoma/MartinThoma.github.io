---
layout: post
title: Data Serialization
slug: data-serialization
author: Martin Thoma
date: 2017-08-07 20:00
category: Code
tags: Data formats, Machine Learning
featured_image: logos/ml.png
---
Transforming objects you have in memory into a structure which can be stored in
a file is called serialization. Serializing data is important for several
reasons:

* **Checkpoints**: Especially in machine learning, it happens often that the
  preprocessing takes long. The longest setup I had so far was something like
  20 hours. I don't want my computer to run when I sleep. And I want it to be
  usable when I sit in front of it. Hence I want to be able to abort and resume
  the preprocessing. This means I have to store the current state on the disk.
* **Memory limitations**: My laptop has 8&nbsp;GB of RAM. For some datasets,
  this is not enough. Hence I want to be able to preprocess some part of my
  data, store the results to a file, remove it from memory and continue. This
  way, I can handle arbitrary large datasets. Formats with random access are
  nice in such a case, otherwise you can always create multiple files.
* **Sharing data**

Properties that are interesting are:

* **Library support**: How easy is it to read / write data? Is it only for
  one programming language / environment or is the format open and wide-spread?
* **Read speed**
* **Write speed**

## Overview

<table class="table">
    <tr>
        <th>Format</th>
        <th>Pro</th>
        <th>Con</th>
        <th>Binary</th>
        <th>Comment</th>
    </tr>
    <tr>
        <td><a href="http://stackoverflow.com/questions/41585078/how-do-i-read-and-write-csv-files-with-python/41585079#41585079">CSV</a></td>
        <td>Simple to use, not much overhead, can be imported into EXCEL</td>
        <td>No data types</td>
        <td>No</td>
        <td></td>
    </tr>
    <tr>
        <td><a href="http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python/37795053#37795053">JSON</a></td>
        <td>Simple to use, data types, supported by all programming languages</td>
        <td>some overhead</td>
        <td>No</td>
        <td>Use this if possible</td>
    </tr>
    <tr>
        <td><a href="http://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python/42054860#42054860">YAML</a></td>
        <td>Simple to use, data types, supported by Python</td>
        <td>some overhead, not so simple to write it correctly</td>
        <td>No</td>
        <td>Don't use this for storing data. Nice for configuration, though.</td>
    </tr>
    <tr>
        <td>XML</td>
        <td>Data formats</td>
        <td>A pain in the *** to use</td>
        <td>No</td>
        <td>Might be worth a shot if you're using a strictly typed programming language</td>
    </tr>
    <tr>
        <td><a href="http://stackoverflow.com/questions/34660090/how-do-i-decode-a-msgpack-file-in-python/34660959#34660959">MessagePack</a></td>
        <td>Data types, relatively small</td>
        <td></td>
        <td>Yes</td>
        <td></td>
    </tr>
</table>


## See also

* [Speed comparison](https://gist.github.com/justinfx/3174062)
