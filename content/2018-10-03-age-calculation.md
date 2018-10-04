---
layout: post
title: How old am I?
slug: age-calculation
author: Martin Thoma
date: 2018-10-03 20:00
category: Code
tags: Software Engineering, Datetime
featured_image: logos/dst.png
---
Calculating the age of a person in a web service is harder than one might think
to get right. Things you must be aware of are:

**Time zones**: The time zone at the client is likely not the same as on your
machine. Hence it could be that the person is under-age in their country, but
already an adult in the server time zone.

**Calendar years**: Usually we think of one year as 365 days. Hence
calculating the age of a person sounds as simple as calculating the days since
their birth, dividing by 365 and that's it. Execept that we don't think of age
like this.

I challenge you to create a program that solves the following task. I'm interested
in your solutions, so please share a link to a [gist](https://gist.github.com/), [pastebin](https://pastebin.com/)
or wherever you solved the task.


## Task

Write a program that takes the following input as a `;` separated string:

1. Birthday as `YYYY-MM-DDTHH:mm:ss`, assuming the time zone given
2. Timezone of Birth ([IANA name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g. `Europe/Berlin`)
3. Current time as `YYYY-MM-DDTHH:mm:ssZ` (UTC)

and prints the age in years (a single integer).


## Tests

```
assert get_age('1996-02-29T15:45:54;Europe/Berlin;2018-10-03T09:47:50') == 22
assert get_age('2008-04-28T15:45:54;Europe/Berlin;2018-10-03T09:47:50') == 10
assert get_age('2008-11-28T15:45:54;Europe/Berlin;2018-10-03T09:47:50') == 9
assert get_age('2006-03-01T00:00:00;Europe/Berlin;2008-02-29T23:59:59') == 1
```


## Solutions

I hope to see many solutions in different programming languages.

### Python Solution

Author: Martin Thoma

```
def get_age(input_):
    """
    Calculate the age of a person
    """
    from dateutil.parser import parse
    import pytz

    # parse input
    born, born_tz, now = input_.split(';')
    tz = pytz.timezone(born_tz)
    born = parse(born).replace(tzinfo=pytz.utc).astimezone(tz)
    now = parse(now).replace(tzinfo=pytz.utc)

    # age logic
    year_not_finished = (now.month, now.day) < (born.month, born.day)
    age = now.year - born.year - int(year_not_finished)
    return age

```
