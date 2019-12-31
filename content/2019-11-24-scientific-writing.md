---
layout: post
title: Scientific Writing
slug: scientific-writing
author: Martin Thoma
date: 2019-11-24 20:00
category: My bits and bytes
tags: Academia, University
featured_image: logos/mathematics.png
---
Writing a paper or a thesis in Computer Science is in some ways very different
from writing an essay or a blog post. I figured those out by accident and would
like to help my readers to be directly aware of them. If you want to get a
better introduction, I recommend reading "The Elements of Style".

While writing this article, I noticed the difference between scientific writing
and a blog post quite well. Weasel words, for example, make a lot of sense in
a blog post.


## General Structure

Most papers I read have the following structure:

```
   Abstract
1. Introduction
2. Related Work
3. The idea
   ...
4. The idea
5. Experiments
6. Discussion / Conclusion / Future Work
   References
```

### Abstract

It should be short. Mabye 700 - 1500 characters.


### Introduction

What is the problem that was investigated? Why is it relevant?

### Related Work

What are other key papers related to yours? This section is a small Literature
Review that puts your paper into context.

### The Idea

How did you come up with this? Independent of the experiments, why do you think
it is a good idea?


### Experiments

What was the experimental setup? What do readers need to know to make
experiments themselves?

### Discussion

Which conclusions do you draw from the experiments? What further work needs to
be done?


## Types of Publications

* **Research Paper**: You had a new idea, conducted and reported experiments.
  This paper presents the original, new idea and the insights you got through
  experiments about the idea.
* **Survey Paper**: You provide a detailed overview over a domain. You put the
  relevant work into context, show how it developed. This is a starting point
  for new researchers and something that can be cited for "common knowledge".
* **Review Paper**: You critically analize previously published work.


If you publish the paper to a journal, you could call it an article.


## Weasel Words

Academic writing is about precision. For this reason, the following words should
rarely be used:

* **Amount**: almost, many, various, very, fairly, several, extremely,
  exceedingly, few, mostly, largely, huge, tiny,relatively, ((are|is) a
  number), vast, completely, quite
* **Certainty**: might, appears to be, theoretically, actual
* **Personal judgement**: it is easy to see, interestingly, remarkably,
  surprisingly, excellent, clearly
* significantly, substantially

If you want to give an amount, cite stuff:

* many: Have at least 5 references
* several: Have at least 3 references
* few: Have at least 1 reference

The personal judgement should in many cases be removed without replacement. It
depends a bit on the part of the publication. For example, in an introduction
or the outlook it might be completely fine and even desirable to have some
ideas what implications an observation might have. This also depends very much
on the community for which you publish.


## Numbers

When you evaluate a system, you might denote things like the accuracy. Be aware
that you also communicate something with the number of digits you denote. The
more digits, the more certain you are that this is relevant. So if you say a
classifier has an accuracy of 96.123%, then your test data should better have
at least 100,000 data points. Otherwise, it does not make any sense at all to
denote that many.


## Tables and Images

They should be able to stand on their own. Each table and each image needs a
small text below / above it, that gives enough context for a reader who is
knowledgabe in the area to understand what it says. It is ok to repeat
yourself.

Each table and each image should be referenced in the text. Which means that
each table and each image needs a number.

## See also

* [Strunk & White: The Elements of Style](https://en.wikipedia.org/wiki/The_Elements_of_Style) ([pdf](https://faculty.washington.edu/heagerty/Courses/b572/public/StrunkWhite.pdf))
* [Academic Writing Check](https://github.com/devd/Academic-Writing-Check): A
  tool which can detect many flaws in academic writing.
* [Difference between Paper and Article for scientific writings](https://english.stackexchange.com/a/263206/9880)
* [Literature Review versus Literature Survey. What is the difference?](https://academia.stackexchange.com/q/15080/4092)
