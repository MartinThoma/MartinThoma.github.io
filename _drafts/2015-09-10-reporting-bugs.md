---
layout: post
title: Bug reporting for developers
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Cyberculture
tags:
- Rating
featured_image: logos/bug.png
---

Reporting bugs seems to be a problem for a lot of users and some developers.
Most people seem only to be able to say "it is not working" (example [1](http://stackoverflow.com/q/32494981/562769), but I've seen this VERY often on StackOverflow).

There are dozens of ways something can "not work":

* Nothing happens at all (e.g. because the code doesn't get executed)
* Something happens, but not what you expected (e.g. because you're / the
  developer is doing it wrong)
* The machine crashes (always / sometimes / often / rarely)
* The program crashes (always / sometimes / often / rarely)

A good bug report should answer the following questions:

1. What did you want to achieve?
2. What did you do (e.g. which input did you give / what did you click in which order)?
3. What happened (e.g. which output did you get)?
4. What did you expect to happen (e.g. which output did you expect to get)?

## Common mistakes

### I've tried everything

Probably not. If the problem is solvable, you haven't tried the correct way.
And you should give a list of what you tried and what happened.

Examples for this mistake:

* http://stackoverflow.com/q/32665520/562769

### Not giving minimal examples

Try to make the piece of code which is not working as short as possible.

1. Can you make it a single file?
2. Can you make it a single function?
3. Can you make the function have less parameters?
4. Can you reduce the code of the function?
5. Can you make the input which gives unexpected results shorter?

When you made the example minimal, give your peers the following information

* Example input
* Expected output
* Actual output

## See also

* My articles
    * [Bug Reporting - A users perspective](http://martin-thoma.com/bug-reporting/)
    * [Debugging a C program](http://martin-thoma.com/debugging-a-c-program/)
    * [Profiling C programs](http://martin-thoma.com/profiling-c-programs/)
* StackOverflow
    * [How to debug Rust programs?](http://stackoverflow.com/q/15871885/562769)
    * [How to debug Node.js applications](http://stackoverflow.com/q/1911015/562769)
    * [How do you debug PHP scripts?](http://stackoverflow.com/q/888/562769)
    * [How to create a Minimal, Complete, and Verifiable example](http://stackoverflow.com/help/mcve)