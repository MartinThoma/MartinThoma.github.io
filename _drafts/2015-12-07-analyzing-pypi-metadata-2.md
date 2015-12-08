---
layout: post
title: Analyzing PyPI Metadata - 2
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

## Most common single dependency

Including modules not on PyPI:

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

On PyPI:

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
