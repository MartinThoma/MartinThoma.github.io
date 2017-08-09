---
layout: post
title: Ways to store Data
status: draft
slug: ways-to-store-data
author: Martin Thoma
date: 2017-05-16 20:00
category: Code
tags: Machine Learning, Data
featured_image: logos/ml.png
---
Data is one core element of machine learning. Hence it is worth to think about
ways to store it. This post is inspired by some news of really big datasets being published ([source](https://www.reddit.com/r/MachineLearning/comments/6a97pt/n_new_massive_medical_image_dataset_coming_from/)).


## Hardware

This post is not about hardware. Well, not mainly. The only thing I would
like to mention are some rough scales:

<table class="table">
    <tr>
        <th>Size</th>
        <th>Hardware</th>
        <th>Backup</th>
    </tr>
    <tr>
        <td>&lt; 250GB</td>
        <td>SSD</td>
        <td>Easy</td>
    </tr>
    <tr>
        <td>250 GB - 10 TB</td>
        <td>HDD</td>
        <td>Ok</td>
    </tr>
    <tr>
        <td>10 TB - 32 TB</td>
        <td>HDD + RAID</td>
        <td>Difficult</td>
    </tr>
    <tr>
        <td>more than 32 TB</td>
        <td>Tapes? SANs?</td>
        <td>Extremely difficult</td>
    </tr>
</table>

A short overview of some RAID levels:

<table class="table">
    <tr>
        <th>RAID</th>
        <th>Stripes</th>
        <th>Mirror</th>
        <th>Parity</th>
        <th>Comment</th>
    </tr>
    <tr>
        <td>0</td>
        <td>Blocks</td>
        <td>No</td>
        <td>No</td>
        <td>Just chaining the disks. You can easily loose data</td>
    </tr>
    <tr>
        <td>1</td>
        <td>No</td>
        <td>Blocks</td>
        <td>No</td>
        <td>You can only use half the storage</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Blocks</td>
        <td>No</td>
        <td>Yes</td>
        <td>(1/n)th of the storage is used for parity, where n is the number of disks</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Blocks</td>
        <td>Blocks</td>
        <td>No</td>
        <td>Raid 1 and 0 combined</td>
    </tr>
</table>


You might be interested in

* [Unboxing a PETABYTE of Storage - HOLY $H!T Ep. 16](https://www.youtube.com/watch?v=uykMPICGeqw).
* [RAID levels](http://www.dell.com/support/article/us/en/4/SLN129581/understanding-hard-drive-types--raid-and-raid-controllers-on-dell-poweredge-and-blade-chassis-servers?lang=EN)
* [Why is ext4 only recommended up to 16 TB?](https://unix.stackexchange.com/q/365355/4784)
* [What limits the number of drives in RAID?](https://superuser.com/q/1209642/64857)

I've heard you can store much more on <a href="https://en.wikipedia.org/wiki/Tape_drive">tape drives</a>.
It might be necessary to physically go there and put a tape in / out.


## File formats

Having talked about limitations on the upper scale of the amount of data, I
would like to go down several levels. Let's talk about file formats.


### Structured Data

TODO: See data serialization


### Unstructured data

There are too many file formats for unstructured data to name them all. Here
are a few examples:

* Text files: e-mails
* Images: JPG, PNG, GIF, BMP, ...
* Documents: PDF, PS, ...
* Video, Audio, ...


## Databases

Databases are a nice way to store data. Types of databases are:

* SQL-based: MySQL / MariaDB, PostgreSQL, ...
* [Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database): CouchDB, MongoDB, Elasticsearch
* Graph databases: Neo4j, ...
* Key-Value databases: Reddis, ...


## Data Warehouse

Classical usecases of data warehouses are operational and financial reporting.

See also:

* Wikipedia
    * [Data Warehouse](https://en.wikipedia.org/wiki/Data_warehouse)
    * [FACT table](https://en.wikipedia.org/wiki/Fact_table)

## Data Lake

The idea of a *data lake* is that it is a large container. Several sources add
data to the lake. The type of data might be structured or unstructured, machine
generated or log files.

Data lakes have 5 core principles according to <a href="https://www.youtube.com/watch?v=zlBZrG8dDMM">Evan Shelley</a>:

* Ingest: Ability to collect all data you care about
* Store: Getting data in one place (e.g. with file system like Hadoop)
* Analyze: Find relations you care about
* Surface: Display results found in data
* Act: Help the customer to make more money

Hadoop is a key tool for data lakes.


## TODO

* Hadoop
* Spark
* http://cassandra.apache.org/