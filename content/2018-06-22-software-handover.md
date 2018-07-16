---
layout: post
title: Software Handover
slug: software-handover
author: Martin Thoma
date: 2018-06-22 20:00
category: My bits and bytes
tags: Code, Software Projects
featured_image: logos/code.png
---
Handing over code to another person or another team is a pretty common task.
You might simply get other tasks or even get another project.

So, what should be done for a good handover?


## Preparation

The first phase of the handover is preparation on your side. Make the project
shine in every aspect.

### Remove Outdated Code

I would think of it from the perspective of the person that gets to software.
They might have to go through all code written so far. From their perspective,
every piece of code that is not necessary just adds work. I claim that outdated
code even adds more work than the useful code as you first try to understand
why it was written which might be impossible as circumstances have changed.


### Test Coverage

The better tests you have, the more comfortable will the new developer feel
with adjusting something. You should have a 100% module coverage (any file is
touched by some test) and a high line and branch coverage.

You might want to read about [`tox`](https://tox.readthedocs.io/en/latest/),
[`unittest`](https://docs.python.org/3/library/unittest.html) and
[`pytest`](https://docs.pytest.org/en/latest/).


### Issues

Have a look at the open issues. Is it possible to understand them? Are some of
them maybe already solved? Is the priority propperly set?


### Documentation

Make sure the documentation is recent. Documentation - especially on
architecture - tends to get outdated.

Make sure your documentation answers the following questions:

* What is the purpose of the project?
* How can I install it?
* What does the overall architecture look like (including systems you interact
  with)?


## Code Walkthrough

Go with the other developer(s) through a typical program execution. Ask them
a couple of times if it is clear to them so far.


## Your first PR

Although people should read code responsible, they likely also have other
tasks. And, let's be honest, without a real task reading other peoples code is
hard and boring. So make a Pull Request (PR) and let them review it.


## Their first PR

Give them a simple task to solve. Ask them to make a PR and review it.


## Their first Bugfix

When the developer(s) who took over the project fixed the first bug that you
were not aware of on their own, then I'd say the handover is over and was
successful.
