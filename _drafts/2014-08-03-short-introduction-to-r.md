---
layout: post
title: A short introduction to R
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Code
tags:
- R
- data visualization
- statistics
featured_image: logos/R.png
---

## Installation

On Ubuntu:

```bash
$ sudo apt-get install r-base
$ sudo apt-get install r-cran-ggplot2
```

## Start it

Simply type `R` in the terminal. It is important that it is uppercase!

## Loading data from external sources

```rconsole
> mydata = read.csv("myfile.csv")
```

You can also load data from Excel files (see [r-tutor.com](http://www.r-tutor.com/r-introduction/data-frame/data-import)).

## Visualizations

```rconsole
> boxplot(mydata)
> title("Your title")
```

## See also

* [UbuntuUsers](http://wiki.ubuntuusers.de/R) (German)
