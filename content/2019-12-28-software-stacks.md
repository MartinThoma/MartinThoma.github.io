---
layout: post
lang: en
title: Software Stacks
slug: software-stacks
author: Martin Thoma
date: 2019-12-28 20:00
category: Code
tags: Development
featured_image: logos/star.png
---
Software stacks are projects of software which nicely work together.
They are sometimes also called <a href="https://en.wikipedia.org/wiki/Solution_stack">solution stacks</a>. Here are some of which I know that they are widely spread.

<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>

## LAMP

What it is good for: Simple start for creating web services.

Software:

* Linux: Operating System
* <a href="https://en.wikipedia.org/wiki/Apache_HTTP_Server">Apache</a>: Web Server
* MySQL: Database management system
* PHP: Programming language

## LNMP

What it is good for: Creating web services.

Software:

* Linux: Operating System
* Nginx: web server
* MySQL / MariaDB: Database management system
* Perl, PHP, Python: Programming language

## MEAN

What it is good for: Creating web services.

Software:

* MongoDB: Database
* Express.js: Controller layer
* Angular: Presentation layer
* Node.js: Web server

## ELK

What it is good for: Search, analyze and visualize data in real time.

Software:

* Elasticsearch: search and analytics engine
* Logstash: server‑side data processing pipeline
* Kibana: let users visualize data


## Android

Software:

* Editor: <a href="https://developer.android.com/studio/">Android Studio</a>
* Programming language: Java / <a href="https://en.wikipedia.org/wiki/Kotlin_(programming_language)">Kotlin</a>


## iOS

Software:

* Operating System: <a href="https://en.wikipedia.org/wiki/MacOS">macOS</a>
* Editor: <a href="https://en.wikipedia.org/wiki/Xcode">Xcode</a>
* Programming language: <a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift</a>


## Data Science

Although I haven't heard a catchy name, many people use similar things:

* [EDA](https://martin-thoma.com/eda/): Pandas, Jupyter notebooks and Bash (cat, jq, head, tail)
* Model Building: sklearn
    * Neural Networks: Keras / Tensorflow / (Py)Torch / CNTK
    * <a href="https://xgboost.readthedocs.io/en/latest/">XGBoost</a> / <a href="https://catboost.ai/">Catboost</a> / <a href="https://lightgbm.readthedocs.io/en/latest/">LightGBM</a>
* Images: Matplotlib and [many more visualization tools](https://martin-thoma.com/python-data-visualization/)
* Cloud:
    * AWS Stuff (S3, EC2, ECR and ECS, Cloudwatch, SSM, ...)
    * Azure (Microsoft)
    * GCP (Google Cloud)

And then there come a lot of specialized libraries into play, depending what
you want to do.
