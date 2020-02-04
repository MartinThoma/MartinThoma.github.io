---
layout: post
title: Git Contribution Statistics
slug: git-contribution-statistics
author: Martin Thoma
date: 2019-12-31 20:00
category: Code
tags: git
featured_image: logos/git.png
---
I've just received a letter that the Scipy community will write a "scipy 1.0"
paper and is wondering who should be mentioned as an author. So they want to
figure out who "really" contributed something. While I think this should be a
manual process (and maybe just anybody who added a line of code / documentation
/ gave valuable feedback should be in the author list), I wondered how to do
this automatically. So here are a few ways. To keep it short, I will crop the
first ten.

<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>


## Commit Count

```
$ git shortlog -s -n --all --no-merges
  2183  Pauli Virtanen
  1565  Ralf Gommers
   976  Travis Oliphant
   893  David Cournapeau
   708  Evgeni Burovski
   705  Warren Weckesser
   506  Pearu Peterson
   484  Alex Griffing
   376  Nathan Bell
   363  @endolith
   ...
```

Add `-e` for e-mails.

851 people in total. 13 people made more than 50% of the commits.

It would be really nice to have a waffle chart showing those numbers. so maybe
to top 10 with name / initials, everybody with more than 100 commits in one
group, everybody with more than 50 commits in another, just one commit in one
group and the rest in another group.


## Git Stats

Install it via `apt-get install gitstats` and execute `gitstats . out`. Then
open `out/index.html` in a browser.

General:

```
Project name: scipy
Generated: 2019-06-19 19:00:08 (in 89 seconds)
Generator: GitStats (version 2015.10.03), git version 2.17.1, gnuplot 5.2 patchlevel 2
Report Period: 2001-02-01 09:32:30 to 2019-06-19 08:15:31
Age: 6713 days, 4227 active days (62.97%)
Total Files: 2545
Total Lines of Code: 778151 (3208814 added, 2430663 removed)
Total Commits: 21178 (average 5.0 commits per active day, 3.2 per all days)
Authors: 850 (average 24.9 commits per author)
```

## Git Fame

```
$ sudo apt-get install python-pip python-dev build-essential
$ pip install --user git-fame
$ git fame
```

gives

```
Total commits: 21178
Total ctimes: 22524
Total files: 9415
Total loc: 277469
| Author                            |   loc |   coms |   fils |  distribution   |
|:----------------------------------|------:|-------:|-------:|:----------------|
| Pauli Virtanen                    | 74162 |   2897 |   1236 | 26.7/13.7/13.1  |
| Abraham Escalante                 | 61316 |     94 |     27 | 22.1/ 0.4/ 0.3  |
| Travis Oliphant                   | 36595 |    977 |    665 | 13.2/ 4.6/ 7.1  |
| Andreas Kloeckner                 | 10942 |     12 |     48 | 3.9/ 0.1/ 0.5   |
| nmarais                           |  9974 |      4 |     87 | 3.6/ 0.0/ 0.9   |
| Ralf Gommers                      |  8543 |   2506 |    473 | 3.1/11.8/ 5.0   |
| Eric Moore                        |  8146 |    157 |     66 | 2.9/ 0.7/ 0.7   |
| Ian Henriksen                     |  4831 |     77 |     64 | 1.7/ 0.4/ 0.7   |
| Warren Weckesser                  |  4665 |    760 |    383 | 1.7/ 3.6/ 4.1   |
| Josh Wilson                       |  4568 |    302 |    155 | 1.6/ 1.4/ 1.6   |
```
