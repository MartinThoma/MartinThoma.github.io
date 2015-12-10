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



### Weighted
How often gets a single module included over all packages?

```sql
SELECT
    `packages`.`name`,
    SUM(`packages`)
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

Three minutes later I've got the result:


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

{% caption align="aligncenter" width="500" alt="This bar chart displays which Python modules (excluding system modules) get imported by most Python packages" text="This bar chart displays which Python modules (excluding system modules) get imported by most Python packages" url="../images/2015/12/pypi-imported-packages-excluding-system-count.png" %}