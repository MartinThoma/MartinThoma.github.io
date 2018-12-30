---
layout: post
title: Expert Systems
slug: expert-systems
author: Martin Thoma
date: 2018-12-30 20:00
category: Machine Learning
tags: Machine Learning, Expert Systems
featured_image: logos/ml.png
---
<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>
Science fiction movies are full of advanced systems for medical analysis and
treatment:

* Stargate SG1: The [Goa'uld healing device](http://stargate.wikia.com/wiki/Goa%27uld_healing_device)
  is a box in which you lay, it scans yourself and after a few hours you are
  just healed. From basically anything, <abbr title="if I remember correctly">IIRC</abbr>.
* Elysium: A [healing pod](https://www.youtube.com/watch?v=RyMoJHf7rCQ) which
  looks a bit like a CT scan.
* Prometheus: A medical robot pod performing a surgery (WARNING: The [clip](https://www.youtube.com/watch?v=6-DOeEkqOZg) is from a horror movie)
* Star Trek: A hand-held medical scanner (Tricoder?) which scans you for diseases ([clip](https://www.youtube.com/watch?v=IHd9bYGJtoI))

I can imagine parts of those really well. Especially I think there is much room
for improvement in the analysis by using machine learning.

The answer to "what's wrong with me" has many possible answers and depending on
this many different treatments. As it is such a complex problem, I think an
expert system is the right approach for it.

In the following, I try to structure some thoughts around it.


## Problem overview

What we have:

* The patient: Age, sex, job, social background, ethnicity might be some of the
               important features everybody has.
* Patient record: A list of tuples
    * Tests: (date time, test, test outcome)
    * Treatement: (date time, treatment) - I would include pills, surgeries, excercise, ...
* Diseases: Possible answers to "what's wrong with me". Examples of this category
  are:
    * [Genetic ones](https://en.wikipedia.org/wiki/Genetic_disorder): Sickle cell anaemia, Huntington's disease, ...
    * Viruses: HIV, Hepatitis D, Polio, Cowpox, Measles
    * Bacteria: Yersinia pestis (black death), Haverhill fever


<!-- ## Other stuff

You might have expected something about logical inference,  -->

## Expert Systems

Expert Systems typically consist of 3 parts:

* knowledge base: logical rules
* inference engine
* interface to human


## See also

* [How to get Data for ML systems](https://martin-thoma.com/ml-get-data/)
* [Informationsfusion](https://martin-thoma.com/informationsfusion/)
* Stack Overflow:
    * [Rules Engine vs Expert System](https://stackoverflow.com/q/1687734/562769)
