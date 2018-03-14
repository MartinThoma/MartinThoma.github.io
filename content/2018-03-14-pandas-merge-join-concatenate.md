---
layout: post
title: Pandas: Merge, join, concatenate
slug: pandas-merge-join-concatenate
author: Martin Thoma
date: 2018-03-14 20:00
category: Code
tags: Pandas
featured_image: logos/pandas.png
---
I always get confused about the different methods how to join Pandas
dataframes. So here are some examples that should make it crystal clear.

First, we create two dataframes:

```
#!/usr/bin/env python

import pandas as pd

countries = ['Germany', 'France', 'Indonesia']
inhabitants = [82.5 * 10**6, 66.9 * 10**6, 255.5 * 10**6]
capitals = ['Berlin', 'Paris', 'Jakarta']

df1 = pd.DataFrame({'country': countries,
                    'inhabitant': inhabitants,
                    'capital': capitals})
df1 = df1[['country', 'capital', 'inhabitant']]
print(df1)

countries = ['Germany', 'Italy', 'Spain', 'Austria']
capitals = ['Berlin', 'Rome', 'Madrid', 'Vienna']
hdis = [0.926, 0.897, 0.844, 0.893]
df2 = pd.DataFrame({'country': countries,
                    'capital': capitals,
                    'HDI': hdis})
df2 = df2[['country', 'capital', 'HDI']]
print(df2)
```

So `df1` is:

```
     country  capital   inhabitant
0    Germany   Berlin   82500000.0
1     France    Paris   66900000.0
2  Indonesia  Jakarta  255500000.0
```

and `df2` is

```
   country capital    HDI
0  Germany  Berlin  0.926
1    Italy    Rome  0.897
2    Spain  Madrid  0.844
3  Austria  Vienna  0.893
```

## Merge

The [pandas docs](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html)
tell you that it has the syntax:

```
>>> df1.merge(df2, on='country', how='inner')
   country capital_x  inhabitant capital_y    HDI
0  Germany    Berlin  82500000.0    Berlin  0.926
```

Please note that the column `capital` was duplicated as it is in both tables

Then you can do all of the usual operations we know from SQL JOINs, e.g. a LEFT JOIN:

```
>>> df1.merge(df2, on='country', how='left')
     country capital_x   inhabitant capital_y    HDI
0    Germany    Berlin   82500000.0    Berlin  0.926
1     France     Paris   66900000.0       NaN    NaN
2  Indonesia   Jakarta  255500000.0       NaN    NaN
```

A RIGHT JOIN:

```
>>> df1.merge(df2, on='country', how='right')
   country capital_x  inhabitant capital_y    HDI
0  Germany    Berlin  82500000.0    Berlin  0.926
1    Italy       NaN         NaN      Rome  0.897
2    Spain       NaN         NaN    Madrid  0.844
3  Austria       NaN         NaN    Vienna  0.893
```

OUTER JOIN:

```
>>> df1.merge(df2, on='country', how='outer')
     country capital_x   inhabitant capital_y    HDI
0    Germany    Berlin   82500000.0    Berlin  0.926
1     France     Paris   66900000.0       NaN    NaN
2  Indonesia   Jakarta  255500000.0       NaN    NaN
3      Italy       NaN          NaN      Rome  0.897
4      Spain       NaN          NaN    Madrid  0.844
5    Austria       NaN          NaN    Vienna  0.893
```


## Join

Join is just a convenience method, which uses merge and should be used if you
want to merge on the index:

> The related DataFrame.join method, uses merge internally for the
> index-on-index and index-on-column(s) joins, but joins on indexes by default
> rather than trying to join on common columns (the default behavior for
> merge). If you are joining on index, you may wish to use DataFrame.join to
> save yourself some typing.

The [pandas join operation](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html)
states:

> DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
>
> Join columns with other DataFrame either on index or on a key column.
> Efficiently Join multiple DataFrame objects by index at once by passing a
> list.

Having a look at the following example:

```
>>> df1.join(df2, on='country', how='outer', lsuffix='_df1')
  country_df1 capital_df1   inhabitant country capital    HDI
0     Germany      Berlin   82500000.0     NaN     NaN    NaN
1      France       Paris   66900000.0     NaN     NaN    NaN
2   Indonesia     Jakarta  255500000.0     NaN     NaN    NaN
2         NaN         NaN          NaN       0  Berlin  0.926
2         NaN         NaN          NaN       1    Rome  0.897
2         NaN         NaN          NaN       2  Madrid  0.844
2         NaN         NaN          NaN       3  Vienna  0.893
```

I would say join and merge look extremely similar. You can notice differences
in the function signature when you look at the help, but the difference in the
output is more subtile. It's the index: For merge, you still have the typical
index where each element is unique. For join, if you merge on a column, you
don't have that anymore.


## Concatenate

[Pandas Documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)
and the example

```
>>> pd.concat([df1, df2])
     HDI  capital    country   inhabitant
0    NaN   Berlin    Germany   82500000.0
1    NaN    Paris     France   66900000.0
2    NaN  Jakarta  Indonesia  255500000.0
0  0.926   Berlin    Germany          NaN
1  0.897     Rome      Italy          NaN
2  0.844   Madrid      Spain          NaN
3  0.893   Vienna    Austria          NaN
```


## See also

* [Merge, join, and concatenate](https://pandas.pydata.org/pandas-docs/stable/merging.html)
* [What is the difference between join and merge in Pandas?](https://stackoverflow.com/a/37891437/562769)
