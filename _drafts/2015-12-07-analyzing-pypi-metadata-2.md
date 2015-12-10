---
layout: post
title: Analyzing PyPI Data - 2
author: Martin Thoma
date: 2014-11-22 17:19
categories:
- Code
tags:
- Python
- Community
- SQL
featured_image: logos/python.png
---

I've recently got a request to expand my analysis of the Python Package Index
commonly known as PyPI. It is a repository of Python packages where everybody
can upload packages; pretty much without any restriction. In the article
[Analyzing PyPI Metadata](http://martin-thoma.com/analyzing-pypi-metadata/)
you can read some general stuff about the repository.

This article is going a bit more deeper. This time I don't only analyze the
metadata, but the relationship of the packages themselves. I wanted to build
a dependency graph. However, here is a downside of Pythons package structure:
The file which defines the dependencies of a Python package is a Python script
itself. This gives the package developer the highest flexibility, but it also
gives them the power to execute arbitrary code when I only want to get the
dependencies.

As I am pretty sure there are some malicious packages in the repository
(Although I've never heard of a single one there has to be one. Over
50&thinspace;000 packages by )


## Most common single dependency

One can see dependencies as being weighted by the number of times a package
imports the package.

### Non-weighted

```sql
SELECT
    `packages`.`name`,
    COUNT(`needs_package`)
FROM
    `dependencies`
JOIN
    `packages` ON `needs_package` = `packages`.`id`
GROUP BY
    `needs_package`
ORDER BY
    COUNT(`needs_package`) DESC
LIMIT 20
```

which gives

{% caption align="aligncenter" width="500" alt="This bar chart displays which Python modules get imported by most Python packages" text="This bar chart displays which Python modules get imported by most Python packages" url="../images/2015/12/pypi-imported-packages-count.png" %}

and without the system packages:

```sql
SELECT
    `packages`.`name`,
    COUNT(`needs_package`)
FROM
    `dependencies`
JOIN
    `packages` ON `needs_package` = `packages`.`id`
WHERE
    `on_pypi` = 1
GROUP BY
    `needs_package`
ORDER BY
    COUNT(`needs_package`) DESC
LIMIT 20
```

which gives

<figure style="width: 510px" class="wp-caption aligncenter">
    <img src="../images/2015/12/pypi-imported-packages-excluding-system-count.png" alt="This bar chart displays which Python modules (excluding system modules) get imported by most Python packages" />
    <figcaption>This bar chart displays which Python modules (excluding system modules) get imported by most Python packages</figcaption>
</figure>


### Weighted
How often gets a single module included over all packages?

```sql
SELECT
    `packages`.`name`,
    SUM(`times`)
FROM
    `dependencies`
JOIN
    `packages` ON `needs_package` = `packages`.`id`
GROUP BY
    `needs_package`
ORDER BY
    SUM(`times`) DESC
LIMIT 20
```

2&nbsp;seconds later I've got the result:


{% caption align="aligncenter" width="500" alt="Number of imports of Python packages" text="Number of imports of Python packages" url="../images/2015/12/pypi-imported-packages.png" %}



If I'm only interested in the packages which are on PyPI, hence not system
packages, I execute the following query:

```sql
SELECT
    `packages`.`name`,
    SUM(`times`)
FROM
    `dependencies`
JOIN
    `packages` ON `needs_package` = `packages`.`id`
WHERE
    `on_pypi` = 1
GROUP BY
    `needs_package`
ORDER BY
    SUM(`times`) DESC
LIMIT 20
```

which gives me about 2&nbsp;seconds later the following result:

{% caption align="aligncenter" width="500" alt="Number of imports of Python packages, excluding system packages" text="Number of imports of Python packages, excluding system packages" url="../images/2015/12/pypi-imported-packages-excluding-system.png" %}


## Non-functional packages

Although there are many packages for Python which are very usefull, there are
also quite a lot which are not usefull at all. One possibility to identify such
packages is by checking which packages get neither used by others nor use
other packages

```sql
SELECT
    `packages`.`id`, `name`
FROM `packages`
WHERE
    `id` in (
        SELECT DISTINCT
            `dependencies`.`package`
        FROM
            dependencies)
OR `id` in (
        SELECT DISTINCT
            `dependencies`.`needs_package`
        FROM
            `dependencies`)
```

This leads to the result that 54&thinspace;900 packages of 67&thinspace;582
packages are not obviously crap. Or to write it in another way: 11&nbsp;682
packages are crap. That is 17.5&thinspace;%. Too much, in my opinion.
However, this might also be due to my crappy script not downloading / checking
the downloaded files correctly.


## Names

One thing I was interested in while downloading all those packages was the
question if there are malicious packages (either on purpose or by accident).
One undesirable thing that could happen would be very similar names.


### Prefixes

Let's see how many packages are prefixes of other packages

### Levensthein Distance

### Non-Pythonic package names


## Graph analysis

Analyzing the dependency graph is quite a challenge. Or at least that was what
I initiallly thought. This graph has about 67&thinspace;582 nodes and
436&thinspace;980 edges. Quite a bit. Definitely much larger than what I have
previously used.

However, my friend Nilan who knows a lot about graphs send me a link to
StackOverflow: [Visualizing Undirected Graph That's Too Large for GraphViz?](http://stackoverflow.com/q/238724/562769)

This lead me to [Gephi](http://gephi.org/) and the
[OpenOrd](https://marketplace.gephi.org/plugin/openord-layout/) layout plugin.
It didn't work for the complete graph (see [issues/1207](https://github.com/gephi/gephi/issues/1207)), it worked after I removed the single nodes without edges.

Now we can ask several standard questions about graphs:

* How many connected components are there?
* Are there any circles? (That would be bad... dependency graphs should not
  have circles. Similar to family trees.)
* Which are the most central nodes?

### Gephi images

TODO: 

See also: [Features of Gephi](http://gephi.org/features/)


## What could come next

I could imagine to analyze the

* package goodness with
  [Cheesecake](https://pypi.python.org/pypi/Cheesecake),
* PEP8 conformance,
* Lines of code / documentation / whitespace
* Usage of functions
* Testing coverage
* Look for URLs in the code and which are reachable / which are not
* Look for non-Python files
