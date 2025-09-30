---
layout: post
lang: en
title: How to get Data for ML systems
slug: ml-get-data
author: Martin Thoma
date: 2017-06-15 20:00
category: Machine Learning
tags: Machine Learning, data
featured_image: logos/ml.png
---
Machine Learning is only possible with data. The more data, the better. For
many services this is a self-improving system. The more data the system gets,
the better it becomes. The better the system is, the more users use it. The
more users use the system, the more data the system gets.

This is an awesome property, but what do you do if you don't have any / enough
data to create a useful system? How do you bootstrap a machine learning system?

I will take write-math.com (handwritten symbol recognition) and Amazon book
recommendations as examples.


## Generate Data yourself

Sometimes, it is possible to generate data yourself. This is what I did for
write-math.com. It could be expected that users are not too different - after
all, single symbols should look somewhat similar, no matter who wrote them.

This is not possible for Amazon recommendations as they are mainly dependant on
the user.


## Ask friends

You can ask friends / collegues to use your system and feed it with data. I did
this with write-math.com, too.


## Gamification

Sometimes, you can make a game which is interesting enough to attract users to
use your system and feed it with data. For example, Google did this with
[Quickdraw](https://quickdraw.withgoogle.com/).


## Side-steping

Some tasks can be re-formulated so that they are intersting for other problems.
Examples are [Asirra](https://www.microsoft.com/en-us/research/publication/asirra-a-captcha-that-exploits-interest-aligned-manual-image-categorization/) and
reCaptcha:

You are given 12 images. Your task is to identify all images which contain
dogs. The developer knows the content of 11 images. If you get those 11 right,
some trust is put into your classification of the 12th image.

Similar, for reCaptcha you are given two words. The developer knows one of
them. It is placed randomly on the left or the right. If you get that one
right, some trust is put into your classification of the other one.

Another example is Duolingo.


## Alternative Algorithms

You could use other algorithms with do not need data. [Expert systems](https://en.wikipedia.org/wiki/Expert_system) are
examples for this kind of algorithm. Just let an expert hand-craft rules. This
could work for Amazon recommendations:

* Get besteller lists to rank books initially.
* As soon as the user liked one book of one author, add a little bit to the
  score of all other books of that author.
* Users who bought one edition of a book usually don't buy the same book in
  another edition. Hence reduce the score for them.
* ...


## Sparse matrix completion

For recommendation systems, you can define user "prototypes" ("the nerd", "the
artist", "the gamer", ...). Define their properties. Find one person for each
prototype. Let them rank the books. Not necessarily every book, but many. You
could add rules to infer the ranking of missing books.

As soon as a new user arrives, ask them about some distinguishing books. Try to
see in which prototypes (or mixture of prototypes) they fit best. Recommend new
books according to that mixture.
