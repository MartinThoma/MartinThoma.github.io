---
layout: post
lang: en
title: Web Frameworks
slug: web-frameworks
author: Martin Thoma
status: draft
date: 2019-02-16 20:00
category: My bits and bytes
tags: Machine Learning
featured_image: logos/star.png
---
I have the idea to build a website for education and certification for quite a
while. I notice that this is a relevant topic for millions of people and I
think I have a good idea how to improve it. But I need to get started. It is a
web project and web development is not my main area of expertise. So I wonder
for quite a while what a good language / framework for starting a bigger web
project would be. In 2015 I wrote [Languages for Back Ends](https://martin-thoma.com/languages-for-back-ends/),
but I think I got it wrong. The language is a bit important, but way more important is the eco system. And a big part of the eco system is the framework you use. Now I try to figure out which
frameworks I want to work with.

There are <a href="https://en.wikipedia.org/wiki/Comparison_of_web_frameworks">tons of web frameworks</a>.
I will focus on the following languages:

* Python: My all-time favorite
* JavaScript and Ruby: Jep, even I am aware of node.js and Rails
* Scala: Just curious

I will not include C#, Java, PHP, Perl and many more. I don't like the
languages and their eco systems. I will also not include Go and Rust, because I
have the impression it is hard to find developers.

I will look at a couple of things for each framework:

* **Famous Examples**: Big Websites / Services that use the framework
* **StackOverflow**: Number of questions over time - not sure if many questions are good, tough
* **Google Trends**: What do people look for?
* **Google ngrams**: What do people write?

## Enthusiasm



<table>
    <tr>
        <th>Framework</th>
        <th>Github Stars</th>
        <th>stackshare Votes</th>
        <th>stackshare Fans</th>
    </tr>
    <tr>
        <td>Laravel (PHP)</td>
        <td>49.8K</td>
        <td>2.53K</td>
        <td>3.9K</td>
    </tr>
    <tr>
        <td>Rails (Ruby)</td>
        <td>42.2K</td>
        <td>5.18K</td>
        <td>5.01K</td>
    </tr>
    <tr>
        <td>Flask (Python)</td>
        <td>42K</td>
        <td>1.05K</td>
        <td>2.65K</td>
    </tr>
    <tr>
        <td>Django (Python)</td>
        <td>39.5K</td>
        <td>2.69K</td>
        <td>4.58K</td>
    </tr>
    <tr>
        <td>Node.js</td>
        <td>35.6K</td>
        <td>7.73K</td>
        <td>17.9K</td>
    </tr>
    <tr>
        <td>Spring Boot</td>
        <td>34.2K</td>
        <td>369</td>
        <td>2.58K</td>
    </tr>
    <tr>
        <td>Rocket (Rust)</td>
        <td>6.46K</td>
        <td>7</td>
        <td>49</td>
    </tr>
</table>


## Jobs

The picture here is clear: Node.js and Spring are by far the best option if you
want to have an easy time getting a job.

<table>
    <tr>
        <th>Framework</th>
        <th>SO.com/jobs</th>
        <th>Indeed Results</th>
        <th>stackshare Stacks</th>
        <th>stackshare Jobs</th>
    </tr>
    <tr>
        <td>Node.js</td>
        <td>31</td>
        <td>278</td>
        <td>20.8K</td>
        <td>5.65K</td>
    </tr>
    <tr>
        <td>Spring (Boot)</td>
        <td>29 (11)</td>
        <td>576 (188)</td>
        <td>2.78K</td>
        <td>76</td>
    </tr>
    <tr>
        <td>Django</td>
        <td>3</td>
        <td>42</td>
        <td>5.11K</td>
        <td>1.6K</td>
    </tr>
    <tr>
        <td>Rails (Ruby)</td>
        <td>1</td>
        <td>62</td>
        <td>6.92K</td>
        <td>3.91K</td>
    </tr>
    <tr>
        <td>Laravel (PHP)</td>
        <td>1</td>
        <td>54</td>
        <td>4.35K</td>
        <td>344</td>
    </tr>
    <tr>
        <td>Flask</td>
        <td>1</td>
        <td>19</td>
        <td>2.88K</td>
        <td>629</td>
    </tr>
    <tr>
        <td>Rocket (Rust)</td>
        <td>0</td>
        <td>11</td>
        <td>43</td>
        <td>0</td>
    </tr>
</table>

Methodology:

* The Indeed Results were counted on 2019-02-16 for Munich.
* Stackoverflow was searched for 50km around Munich.

## Learning curve

* Stackoverflow questions
* unanswered

<table>
    <tr>
        <th>Framework</th>
        <th>StackOverflow Questions</th>
        <th>StackOverflow Unanswered</th>
    </tr>
    <tr>
        <td>Django</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Flask</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Node.js</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Spring Boot</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Rocket (Rust)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Rails (Ruby)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Laravel (PHP)</td>
        <td></td>
        <td></td>
    </tr>
</table>


## Node.js

Famous users are:

* Netflix ([source](https://www.youtube.com/watch?time_continue=307&v=QcNqfvMeWow), [source](http://netflix.github.io/))
* Uber
* Twitter
* ebay
* Disqus
* DuckDuckGo
* Flipboard

## Django

<a href="https://www.djangoproject.com/">Django</a> (<a href="https://github.com/django/django">GitHub</a>) is around since 2005 (<a href="https://en.wikipedia.org/wiki/Django_(web_framework)">source</a>).

Famous users are:

* Instagram
* Pinterest
* Udemy
* Coursera
* Bitbucket
* Sentry
* Disqus
* Quora

Small examples:

* https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks

## Flask

Famous users are:

* Reddit
* Netflix
* Lyft
* Zillow
* Mailgun

## React

Jep, I know, I compare apples and pears.

Famous users:

* Netflix ([source](http://netflix.github.io/))


## Major Websites

### Wikipedia

Wikipedia uses [Mediawiki](https://en.wikipedia.org/wiki/MediaWiki), which is
written in **PHP** ([HHVM](https://en.wikipedia.org/wiki/HipHop_for_PHP)).
They use Apache and Nginx.


### Facebook

Facebook uses (used?) a version of PHP called <a
href="https://hacklang.org/">hack</a>. As a database some claim they use MySQL
(<a href="https://royal.pingdom.com/the-software-behind-facebook/">source</a> / <a href="https://www.quora.com/What-is-Facebooks-architecture-6">source</a>).
It is also claimed on that page that Facebook uses <a
href="http://memcached.org/">memcached</a>. The main point to learn from that
post is that development on this scale is difficult and requires more than one
tool.

According to <a href="https://stackshare.io/facebook/facebook">stackshare.io</a>:

* PHP (HHVM)
* Cassandra
* React
* GraphQL
* Memcached

### YouTube

I couldn't find reliable information on what YouTube is using. Some say <a href="https://softwareengineering.stackexchange.com/a/219435/25699">Python for the front end</a> (generating the HTML).

### Amazon

According to <a href="https://stackshare.io/amazon/amazon">stackshare.io</a>:

* Java
* MySQL
* AngularJS

### Netflix

According to <a href="https://stackshare.io/netflix/netflix">stackshare.io</a>

* Node.js
* Java, Python
* MySQL
* React
* Flask
* Cassandra
* PostgreSQL


## See also

* https://hotframeworks.com/
* https://en.wikipedia.org/wiki/Comparison_of_web_frameworks
