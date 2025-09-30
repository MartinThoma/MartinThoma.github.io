---
layout: post
lang: en
title: Current Python Versions
slug: current-python-versions
author: Martin Thoma
date: 2020-02-12 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
Which Python versions should my library support?

For which version should I develop my web service / application?

For the second question, I like to never take a x.y.0 version. Let them get
the patches out first.


## Lifecycle of cPython

I've asked which CPython versions get support right now on SO, and <a href="https://stackoverflow.com/q/60126561/562769">it got heavily downvoted</a>.
But I got <a href="https://devguide.python.org/#status-of-python-branches">the answer</a>:

<table class="table">
    <tr>
        <th>Python Version</th>
        <th>PEP</th>
        <th>First Release</th>
        <th>End-of-life</th>
    </tr>
    <tr>
        <td>3.8</td>
        <td><a href="https://www.python.org/dev/peps/pep-0569/">PEP 569</a></td>
        <td>2019-10-14</td>
        <td>2024-10</td>
    </tr>
    <tr>
        <td>3.7</td>
        <td><a href="https://www.python.org/dev/peps/pep-0537/">PEP 537</a></td>
        <td>2018-06-27</td>
        <td>2023-06-27</td>
    </tr>
    <tr>
        <td>3.6</td>
        <td><a href="https://www.python.org/dev/peps/pep-0494/">PEP 494</a></td>
        <td>2016-12-23</td>
        <td>2021-12-23</td>
    </tr>
    <tr>
        <td>3.5</td>
        <td><a href="https://www.python.org/dev/peps/pep-0478/">PEP 478</a></td>
        <td>2015-09-13</td>
        <td>2020-09-13</td>
    </tr>
</table>


## Python Interpreters

CPython is by far the most commonly used interpreter, but there are others.
PyPy for example. And currently only supports Python 3.6, although development
of Python 3.9 has already started (see [pypy.org](https://www.pypy.org/download.html) for the latest state).

So if you want to allow the usage of other interpreters, you might need to use
older Python versions.


## AWS Lambda

<a href="https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html">Documentation</a> states:

<table class="table">
    <thead>
        <tr>
            <th>Python Version</th>
            <th>boto3</th>
            <th>botocore</th>
            <th>Operating System</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Python 3.8</td>
            <td>boto3-1.10.34</td>
            <td>botocore-1.13.34</td>
            <td>Amazon Linux 2</td>
        </tr>
        <tr>
            <td>Python 3.8</td>
            <td>boto3-1.10.34</td>
            <td>botocore-1.13.34</td>
            <td>Amazon Linux</td>
        </tr>
        <tr>
            <td>Python 3.8</td>
            <td>boto3-1.10.34</td>
            <td>botocore-1.13.34</td>
            <td>Amazon Linux</td>
        </tr>
        <tr>
            <td>Python 2.7</td>
            <td>boto3-1.10.34</td>
            <td>botocore-1.13.34</td>
            <td>Amazon Linux</td>
        </tr>
    </tbody>
</table>

## Distribution Defaults

Linux distributions ship with Python. The default of those influences a lot
what is used. I've used the <a href="https://packages.debian.org/search?suite=default&section=all&arch=any&lang=de&searchon=names&keywords=python3">debian package search</a> and the <a href="https://packages.ubuntu.com/search?suite=disco&searchon=names&keywords=python">Ubuntu package search</a> to get the numbers:

<table class="table">
    <thead>
        <tr>
            <th>Operating System</th>
            <th>Package "python"</th>
            <th>Package "python3"</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ubuntu 18.04 LTS</td>
            <td>2.7.x</td>
            <td>3.6.x</td>
        </tr>
        <tr>
            <td>Ubuntu 19.04</td>
            <td>2.7.x</td>
            <td>3.7.x</td>
        </tr>
        <tr>
            <td>Ubuntu 19.10</td>
            <td>2.7.x</td>
            <td>3.7.x</td>
        </tr>
        <tr>
            <td>Debian (jessie)</td>
            <td>2.7.x</td>
            <td>3.4.x</td>
        </tr>
        <tr>
            <td>Debian (stretch)</td>
            <td>2.7.x</td>
            <td>3.5.x</td>
        </tr>
        <tr>
            <td>Debian (buster)</td>
            <td>2.7.x</td>
            <td>3.7.x</td>
        </tr>
        <tr>
            <td>Debian (bullseye)</td>
            <td>2.7.x</td>
            <td>3.7.x</td>
        </tr>
        <tr>
            <td>Debian (sid)</td>
            <td>2.7.x</td>
            <td>3.7.x</td>
        </tr>
    </tbody>
</table>

## Python Download Statistics

I'm <a href="each x.y Python version">trying to get more recent data</a>,
but here you see subtotals for some time before May 2019:

<table class="table">
    <thead>
        <tr>
            <th>Python Version</th>
            <th>Sum of Hits</th>
            <th>% of Hits</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>3.7.x</td>
            <td>15,519,728</td>
            <td>58.36%</td>
        </tr>
        <tr>
            <td>3.6.x</td>
            <td>5,616,969</td>
            <td>21.12%</td>
        </tr>
        <tr>
            <td>2.7.x</td>
            <td>4,112,428</td>
            <td>15.46%</td>
        </tr>
        <tr>
            <td>3.5.x</td>
            <td>1,187,840</td>
            <td>4.47%</td>
        </tr>
        <tr>
            <td>3.8.x</td>
            <td>156,111</td>
            <td>0.59%</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>Grand Total</td>
            <td>26,593,076</td>
            <td>100%</td>
        </tr>
    </tfoot>
</table>


## pipenv download statistics

I'm still trying to get those.


## Google Trends

<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/2051_RC11/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"python 2.7","geo":"","time":"today 12-m"},{"keyword":"python 3.5","geo":"","time":"today 12-m"},{"keyword":"python 3.6","geo":"","time":"today 12-m"},{"keyword":"python 3.7","geo":"","time":"today 12-m"},{"keyword":"python 3.8","geo":"","time":"today 12-m"}],"category":0,"property":""}, {"exploreQuery":"q=python%202.7,python%203.5,python%203.6,python%203.7,python%203.8&date=today 12-m,today 12-m,today 12-m,today 12-m,today 12-m","guestPath":"https://trends.google.de:443/trends/embed/"}); </script>

## See also

* Jetbrains: [Python](https://www.jetbrains.com/de-de/lp/devecosystem-2019/python/), 2019.
* w3techs.com: [Usage statistics of Python Version 3 for websites](https://w3techs.com/technologies/details/pl-python/3)
* Stackoverflow: [python runtime version statistics](https://stackoverflow.com/q/38747864/562769), 2016.
