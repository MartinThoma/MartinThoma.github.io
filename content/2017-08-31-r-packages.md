---
layout: post
title: R Packages
slug: r-packages
author: Martin Thoma
status: draft
date: 2017-08-31 20:00
category: Code
tags: R, Packages
featured_image: logos/r.png
---
I am rather a Python person, but sometimes it is interesting how other
languages solve common problems in order to see what could be better in the
language of your choice.

So, lets have a look at R package managment.

<div class="alert alert-info">This post is a work in progress. I'm happy if you have interesting suggestions, though :-)</div>


## Installing packages

Start R with the command `R` (yes, a capital letter). Then enter

```
> install.packages("ggplot2")
```

choose a mirror. You've installed your first package!

You can also specify the place where it should be downloaded:

```
> install.packages("ggplot2", lib="~/Rpackages/")
```

Inspecting that folder shows the following structure:

```
.
└── ggplot2
    ├── CITATION
    ├── data
    │   ├── Rdata.rdb
    │   ├── Rdata.rds
    │   └── Rdata.rdx
    ├── DESCRIPTION
    ├── doc
    │   ├── extending-ggplot2.html
    │   ├── extending-ggplot2.R
    │   ├── extending-ggplot2.Rmd
    │   ├── ggplot2-specs.html
    │   ├── ggplot2-specs.R
    │   ├── ggplot2-specs.Rmd
    │   └── index.html
    ├── help
    │   ├── aliases.rds
    │   ├── AnIndex
    │   ├── ggplot2.rdb
    │   ├── ggplot2.rdx
    │   ├── macros
    │   │   └── aesthetics.Rd
    │   └── paths.rds
    ├── html
    │   ├── 00Index.html
    │   └── R.css
    ├── INDEX
    ├── LICENSE
    ├── Meta
    │   ├── data.rds
    │   ├── hsearch.rds
    │   ├── links.rds
    │   ├── nsInfo.rds
    │   ├── package.rds
    │   ├── Rd.rds
    │   └── vignette.rds
    ├── NAMESPACE
    ├── NEWS.md
    └── R
        ├── ggplot2
        ├── ggplot2.rdb
        └── ggplot2.rdx
```

What can we see here?

* `CITATION`: A bibtext entry
* `DESCRIPTION`: Describes the package. Looks similar to many entries of Pythons
  `setup.py`
* `INDEX`: Gives each (interesting) file a name and a description. Is part of `library(help=pkgname)`
* `/data`: See [Data in packages](https://cran.r-project.org/doc/manuals/R-exts.html#Data-in-packages)


## Minimal Example

An R package needs the following files:

* `DESCRIPTION`: Describes the file in a fixed format.
* `NAMESPACE`:
* `R/`: Directory containing all code (`.r` files)

Put all of those in a directory called just like your package.


## See also

* [Installing R packages](https://www.r-bloggers.com/installing-r-packages/)
* [Writing R Extensions](https://cran.r-project.org/doc/manuals/R-exts.html)
* [R package primer](http://kbroman.org/pkg_primer/)
* [Writing an R package from scratch](https://hilaryparker.com/2014/04/29/writing-an-r-package-from-scratch/)
* Friedrich Leisch: [Creating R Packages: A Tutorial](https://cran.r-project.org/doc/contrib/Leisch-CreatingPackages.pdf)
