---
layout: post
title: Python and CSV
slug: python-csv
author: Martin Thoma
date: 2015-02-08 12:48
category: Code
tags: Python, CSV
featured_image: logos/python.png
---
Python has a very nice module called
[`csv`](https://docs.python.org/3/library/csv.html)
which makes working with <abbr title="comma seperated values">CSV</abbr> very
easy. This mini article is only a reminder for me so that I can easily find
how to use it when I forget once again how it is used exactly.

## Reading CSV files

```python
try:
    from future.builtins import open
except:
    pass

import csv

with open("eggs.csv", "rt", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";", quotechar='"')
    next(csvreader, None)  # skip the headers
    for row in csvreader:
        print(", ".join(row))
```


## Writing CSV files

```python
try:
    from future.builtins import open
except:
    pass

import csv

with open("eggs.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(
        csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    csvwriter.writerow(["Spam"] * 5 + ["Baked Beans"])  # Write header
    for row in container:
        csvwriter.writerow(row)  # Write data
```

## See also

* [Open files in 'rt' and 'wt' modes](http://stackoverflow.com/q/23051062/562769)
* [Python+CSV on StackOverflow](http://stackoverflow.com/questions/tagged/python+csv?sort=votes&pageSize=50)