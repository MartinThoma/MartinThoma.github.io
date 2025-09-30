---
layout: post
lang: en
title: Customer Segmentation
slug: customer-segmentation
author: Martin Thoma
status: draft
date: 2019-01-02 20:00
category: My bits and bytes
tags: Machine Learning, Clustering
featured_image: logos/ml.png
---
Customer segmentation is one form of clustering. It's a set of techniques that
group customers in segments that have something in common.

It's important to note that not every customer has to belong to one segment.
There might be outliers who don't belong to any group and you might model the
problem such that people can partially belong to multiple segments.

It is helpful to give the segments names. For example, if you cluster by age
and income, then the low-income+low-age group might be called "students".


## How it helps

* Taylor advertisement and products more specifically to the customer
* Optimizing sales-channel mix

An example where it was likely applied is Obamas election campaign (see "Brand Obama: How Barack Obama Revolutionized Political Campaign Marketing in the 2008 Presidential Election")


## Typical Features

Demographic information

* Age
* Income
* Gender
* Marital Status

Transactional information

* Products purchased
* $ volume purchased
* # items purchased
* Time of purchase

Geographic information

* Country
* Region
* City size
* Climate


## Technologies

* Pandas: Exploratory data analysis
