---
layout: post
title: Analyzing PyPI Metadata
author: Martin Thoma
date: 2015-01-18 20:19
categories:
- Code
tags:
- Python
- Community
- SQL
featured_image: logos/python.png
---

<div class="info">This is part one of a series. See <a href="http://martin-thoma.com/analyzing-pypi-metadata-2/">Analyzing PyPI Data - 2</a> for part two.</div>

PyPI, the Python Package Index, gives a very crappy but simple interface to
query metadata about its packages. I scrapped all of the packages metadata.
53,533 packages were scrapped (date: 2015-01-18), because I wanted to
see if there is malware on PyPI (related to
[this question on security.SE](http://security.stackexchange.com/q/79326/3286)).

The database looks like this:

{% caption align="aligncenter" width="500" alt="PyPI metadata database schema" text="PyPI metadata" url="../images/2015/01/pypi-metadata-db.png" %}


## Exploring the data

When I scapped the data from PyPI, I made all database fields "varchar 255" as
there seems to be no information about the possible values. Then I explored
the data

* `name`: The longest package name is 80 characters long (`Aaaaaaaaaaa...`), the shortest packages have only one
character.
* `author`: 911× "UNKOWN", 741× empty, 195× "None", 151× "Zope Foundation and
  Contributors". There are about 22,000 different authors. There are 595
  authors who wrote more than 10 packages.
* `author_email`: 2059× "UNKOWN", 932× empty, 323× "zope-dev@zope.org", 216×
  "None" and 204× "TODO".
* `maintainer`: 46879× "None", 5507× empty, 17× [Paul Boddie](http://www.boddie.org.uk/paul/CV.html).
* `requires_python`: 53467× "None", 3× "UNKNOWN", 2× ">=2.7,!=3.0,!=3.1", 2×
  ">=2.5", 1× "2.6", 1× ">= 3.3", 1× ">=2.4", 1× ">= 2.7" - that's it. No other
  values. Seems as if this is pretty much useless.
* `docs_url`: Either begins with `http://pythonhosted.org` or is empty.


### Most active authors

```sql
SELECT
    `author`, COUNT(`id`) as `created_packages`
FROM
    `packages`
GROUP BY
    `author`
ORDER BY
    COUNT(`id`) DESC, `author` ASC
LIMIT
    50
```

gives

|                                   | 1485 |
| --------------------------------- | ---- |
| UNKNOWN                           | 1150 |
| None                              | 196  |
| OpenStack                         | 188  |
| Zope Foundation and Contributors  | 146  |
| MicroPython Developers            | 139  |
| OpenERP SA                        | 137  |
| Zope Corporation and Contributors | 128  |
| RedTurtle Technology              | 127  |
| Praekelt Foundation               | 126  |
| Fanstatic Developers              | 98   |
| Tryton                            | 98   |
| Raptus AG                         | 97   |
| russianidiot                      | 93   |
| hfpython                          | 92   |
| LOGILAB S.A. (Paris, FRANCE)      | 88   |
| BlueDynamics Alliance             | 87   |
| Ralph Bean                        | 83   |
| JeanMichel FRANCOIS aka toutpt    | 69   |
| Bart Thate                        | 68   |


The total number of authors is 28&thinsp;183 (06.12.2015):

```sql
SELECT COUNT(DISTINCT `author`) AS `total_authors` FROM `packages`
```

### Maximum Length

I guess many values are stored on PyPI as `Varchar(255)`. To check if I might
have missed some values, I checked which entry was the longest one for all
columns. I did this with

```sql
SELECT `name`, LENGTH(`name`) FROM `packages` ORDER BY LENGTH(`name`) DESC
```

<table>
    <tr>
        <th>Column</th>
        <th>Maximum Length</th>
        <th>Entry</th>
    </tr>
    <tr>
        <td>name</td>
        <td>80</td>
        <td>Aaaaaaaaaaaaaaaaaaa-aaaaaaaaa-aaaaaaasa-aaaaaaasa-aaaaasaa-aaaaaaasa-bbbbbbbbbbb</td>
    </tr>
    <tr>
        <td>author</td>
        <td>248</td>
        <td>Michael R. Crusoe, Greg Edvenson, Jordan Fish, Adina Howe, Luiz Irber, Eric McDonald, Joshua Nahum, Kaben Nanlohy, Humberto Ortiz-Zuazaga, Jason Pell, Jared Simpson, Camille Scott, Ramakrishnan Rajaram Srinivasan, Qingpeng Zhang, and C. Titus Brown</td>
    </tr>
    <tr>
        <td>author_email</td>
        <td>215</td>
        <td>ongsp@ucsd.edu, anubhavj@mit.edu, mpkocher@lbnl.gov, geoffroy.hautier@uclouvain.be, wrichard@mit.edu, sdacek@mit.edu, dkgunter@lbl.gov, scholia@lbl.gov, gmatteo@gmail.com, vincentchevrier@gmail.com, armiento@mit.edu</td>
    </tr>
    <tr>
        <td>maintainer</td>
        <td>63</td>
        <td>Panagiotis Liakos, Katia Papakonstantinopoulou, Michael Sioutis</td>
    </tr>
    <tr>
        <td>maintainer_email</td>
        <td>67</td>
        <td>maxistedeams@gmail.com, p_riendeau@live.ca, rheault.etccy@gmail.com</td>
    </tr>
    <tr>
        <td>requires_python</td>
        <td>17</td>
        <td>&gt;=2.7,!=3.0,!=3.1</td>
    </tr>
    <tr>
        <td>platform</td>
        <td>231</td>
        <td>Natural Language :: English<br/>License :: OSI Approved :: Apache Software License<br/>Environment :: Console<br/>Development Status :: 2 - Pre-Alpha<br/>Intended Audience :: Developers<br/>Programming Language :: Python :: 2.7<br/>Topic :: Database</td>
    </tr>
    <tr>
        <td>version</td>
        <td>73</td>
        <td>[In Progress] Python middle layer for interacting with Redis data easily.</td>
    </tr>
    <tr>
        <td>license</td>
        <td>466</td>
        <td>Copyright &copy; 2014 &#1047;&#1040;&#1054; &ldquo;&#1041;&#1040;&#1056;&#1057; &#1043;&#1088;&#1091;&#1087;&rdquo;<br/><br/>&#1044;&#1072;&#1085;&#1085;&#1072;&#1103; &#1083;&#1080;&#1094;&#1077;&#1085;&#1079;&#1080;&#1103; &#1088;&#1072;&#1079;&#1088;&#1077;&#1096;&#1072;&#1077;&#1090; &#1083;&#1080;&#1094;&#1072;&#1084;, &#1087;&#1086;&#1083;&#1091;&#1095;&#1080;&#1074;&#1096;&#1080;&#1084; &#1082;&#1086;&#1087;&#1080;&#1102; &#1076;&#1072;&#1085;&#1085;&#1086;&#1075;&#1086; &#1087;&#1088;&#1086;&#1075;&#1088;&#1072;&#1084;&#1084;&#1085;&#1086;&#1075;&#1086; &#1086;&#1073;&#1077;&#1089;&#1087;&#1077;&#1095;&#1077;&#1085;&#1080;&#1103; &#1080; &#1089;&#1086;&#1087;&#1091;&#1090;&#1089;&#1090;&#1074;&#1091;&#1102;&#1097;&#1077;&#1081; &#1076;&#1086;&#1082;&#1091;&#1084;&#1077;&#1085;&#1090;&#1072;&#1094;&#1080;&#1080; (&#1074; &#1076;&#1072;&#1083;&#1100;&#1085;&#1077;&#1081;&#1096;&#1077;&#1084;<br/>&#1080;&#1084;&#1077;&#1085;&#1091;&#1077;&#1084;&#1099;&#1084;&#1080; &laquo;&#1055;&#1088;&#1086;&#1075;&#1088;&#1072;&#1084;&#1084;&#1085;&#1086;&#1077; &#1054;&#1073;&#1077;&#1089;&#1087;&#1077;&#1095;&#1077;&#1085;&#1080;&#1077;&raquo;), &#1073;&#1077;&#1079;&#1074;&#1086;&#1079;&#1084;&#1077;&#1079;&#1076;&#1085;&#1086; &#1080;&#1089;&#1087;&#1086;&#1083;&#1100;&#1079;&#1086;&#1074;&#1072;&#1090;&#1100; &#1055;&#1088;&#1086;&#1075;&#1088;&#1072;&#1084;&#1084;&#1085;&#1086;&#1077; &#1054;&#1073;&#1077;&#1089;&#1087;&#1077;&#1095;&#1077;&#1085;&#1080;&#1077; &#1073;&#1077;&#1079; &#1086;&#1075;</td>
    </tr>
    <tr>
        <td>keywords</td>
        <td>655</td>
        <td>ArcLink,array,array analysis,ASC,beachball,beamforming,cross correlation,database,dataless,Dataless SEED,datamark,earthquakes,Earthworm,EIDA,envelope,events,FDSN,features,filter,focal mechanism,GSE1,GSE2,hob,iapsei-tau,imaging,instrument correction,instrument simulation,IRIS,magnitude,MiniSEED,misfit,mopad,MSEED,NERA,NERIES,observatory,ORFEUS,picker,processing,PQLX,Q,real time,realtime,RESP,response file,RT,SAC,SEED,SeedLink,SEG-2,SEG Y,SEISAN,SeisHub,Seismic Handler,seismology,seismogram,seismograms,signal,slink,spectrogram,StationXML,taper,taup,travel time,trigger,VERCE,WAV,waveform,WaveServer,WaveServerV,WebDC,web service,Winston,XML-SEED,XSEED</td>
    </tr>
    <tr>
        <td>description</td>
        <td>65535</td>
        <td>[id don't want to put that here - there were 22 with this length]</td>
    </tr>
    <tr>
        <td>summary</td>
        <td>278</td>
        <td>Splits one vcard file (*.vcf) to many vcard files &nbsp; &nbsp; &nbsp; &nbsp;with one vcard per file. Useful for import contacts to phones, &nbsp; &nbsp; &nbsp; &nbsp; thats do not support multiple vcard in one file. &nbsp; &nbsp; &nbsp; &nbsp; Supprt unicode cyrillic characters. &nbsp; &nbsp; &nbsp; &nbsp; &#1050;&#1086;&#1085;&#1089;&#1086;&#1083;&#1100;&#1085;&#1072;&#1103; &#1087;&#1088;&#1086;&#1075;&#1088;&#1072;&#1084;&#1084;&#1072; &#1076;&#1083;&#1103; &#1088;</td>
    </tr>
    <tr>
        <td>stable_version</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>home_page</td>
        <td>134</td>
        <td>http://127.0.0.1:8888/USK@9X7bw5HD2ufYvJuL3qAVsYZb3KbI9~FyRu68zsw5HVg,lhHkYYluqHi7BcW1UHoVAMcRX7E5FaZjWCOruTspwQQ,AQACAAE/pyfcp-api/0/</td>
    </tr>
    <tr>
        <td>release_url</td>
        <td>130</td>
        <td>http://pypi.python.org/pypi/softwarefabrica.django.appserver/1.0dev-BZR-r10-panta-elasticworld.org-20091023132843-vitk6k7e5qlvhej5</td>
    </tr>
    <tr>
        <td>bugtrack_url</td>
        <td>104</td>
        <td>https://bugzilla.redhat.com/buglist.cgi?submit&amp;component=python-nss&amp;product=Fedora&amp;classification=Fedora</td>
    </tr>
    <tr>
        <td>download_url</td>
        <td>183</td>
        <td>http://pypi.python.org/packages/source/s/softwarefabrica.django.appserver/softwarefabrica.django.appserver-1.0dev-BZR-r10-panta-elasticworld.org-20091023132843-vitk6k7e5qlvhej5.tar.gz</td>
    </tr>
    <tr>
        <td>package_url</td>
        <td>108</td>
        <td>http://pypi.python.org/pypi/Aaaaaaaaaaaaaaaaaaa-aaaaaaaaa-aaaaaaasa-aaaaaaasa-aaaaasaa-aaaaaaasa-bbbbbbbbbbb</td>
    </tr>
    <tr>
        <td>_pypi_hidden</td>
        <td>-</td>
        <td>True or False</td>
    </tr>
    <tr>
        <td>_pypi_ordering</td>
        <td>-</td>
        <td>Integers from 0 to 464</td>
    </tr>
    <tr>
        <td>cheesecake_code_kwalitee_id</td>
        <td>-</td>
        <td>Integers from 183 to 6513 and None values</td>
    </tr>
    <tr>
        <td>cheesecake_documentation_id</td>
        <td>-</td>
        <td>Integers from 182 to 6512 and None values</td>
    </tr>
    <tr>
        <td>cheesecake_installability_id</td>
        <td>-</td>
        <td>Integers from 181 to 6511 and None values</td>
    </tr>
</table>

We can see multiple problems here:

* URLs: localhost / 127.0.0.1 is almost certainly not desired
* `cheesecake_installability_id`, `cheesecake_documentation_id`, `cheesecake_code_kwalitee_id`
  should have NULL and None should be casted to NULL. The data type is likely
  to be numeric.
* `_pypi_ordering` should be numeric
* `_pypi_hidden` should be boolean

So I changed the types in the database. Let's continue.


## What people don't use

All metadata is provided by the authors of the packages. Some fields, like the
package name or the description, are used very often, but some fields are only
rarely used:


### Maintainer

`maintainer` and `maintainer_email` is interesting for people who want to send
bug reports. If this is empty, I would guess the package is dead.


### Platform

```sql
SELECT
    `platform`, COUNT(`id`)
FROM
    `packages`
GROUP BY
    `platform`
ORDER BY
    COUNT(`id`) DESC
```

gives 759 different results. The TOP-10 were

| Platform                | Count |
| ----------------------- | ----- |
| UNKNOWN                 | 43539 |
| any                     | 3515  |
|                         | 1986  |
| Any                     | 635   |
| OS Independent          | 542   |
| None                    | 265   |
| Linux                   | 225   |
| linux                   | 167   |
| Posix; MacOS X; Windows | 157   |
| POSIX                   | 156   |

You can see that there are alternative ways to express the same thing.
Also, the ";" should not be here as the manual states it should be a list.

[The manual](https://docs.python.org/2/distutils/setupscript.html) is also too
short for this entry. It only says "a list of platforms" which seems to be
pretty much useless.

[docstore.mik.ua](http://docstore.mik.ua/orelly/other/python/0596001886_pythonian-chp-26-sect-1.html)
gives a little bit more information

> A list of platforms on which this distribution is known to work. You should provide this information if you have reasons to believe this distribution may not work everywhere. This information should be reasonably concise, so this field may refer for details to a file in the distribution or to a URL.


### Bugtracker

This one is very important. Users should have an easy possibility to report
bugs. So please help them by added your bug tracker URL wherever it makes
sense. Here is how you add it on PyPI:

{% caption align="aligncenter" width="500" alt="Go to your packages PyPI page" text="Go to your packages PyPI page" url="../images/2015/01/pypi-bugtrack-url.png" %}

{% caption align="aligncenter" width="500" alt="Add your bugtracker / issue tracker url" text="Add your bugtracker / issue tracker url" url="../images/2015/01/pypi-add-bugtrack-url.png" %}

{% caption align="aligncenter" width="500" alt="Check if you really added it" text="Check if you really added it" url="../images/2015/01/pypi-added-bugtracker.png" %}


### License

Another important one. Add a license to your software!

```sql
SELECT
    `license`, COUNT(`id`)
FROM
    packages
GROUP BY
    `license`
ORDER BY
    COUNT(`id`) DESC
```

gives

| License                     | Count |
| --------------------------- | ----- |
| UNKNOWN                     | 11444 |
| MIT                         | 8098  |
| BSD                         | 7224  |
| GPL                         | 4202  |
| MIT License                 | 1410  |
| (empty)                     | 1398  |
| LICENSE.txt                 | 1201  |
| GPLv3                       | 1083  |
| LGPL                        | 833   |
| ZPL 2.1                     | 829   |
| BSD License                 | 811   |
| Apache License 2.0          | 482   |
| Apache License, Version 2.0 | 443   |
| Apache 2.0                  | 437   |
| GPLv2                       | 370   |
| None                        | 363   |
| ZPL                         | 288   |
| GPL-3                       | 272   |
| GPLv3+                      | 258   |
| LICENSE                     | 249   |

and about 6500 other licenses. Most might be variants in writing, e.g.

* Apache License 2.0
* Apache License, Version 2.0
* Apache 2.0

are all the same license. Some packages have no licence (`Unknown` and empty).
Many are invalid values, like

* LICENSE.txt
* None
* LICENSE
* Python

These indicate that people have no idea what to input there.
[tldrlegal.com](https://tldrlegal.com/) might help in that case. I think the
Python community should try to eliminate variants in writing license names as
it makes finding, filtering and analyzing packages more difficult.


## Classifiers

Python makes use of so called trove classifiers. They are defined in
[PEP 301](https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification)
and listed [here](https://pypi.python.org/pypi?%3Aaction=list_classifiers).

The following table gives the TOP-10 most commonly used classifiers:

| Classifier                                            | Percentage |
| ----------------------------------------------------- | ---------- |
| Programming Language :: Python                        | 0.4615     |
| Intended Audience :: Developers                       | 0.4412     |
| Operating System :: OS Independent                    | 0.3229     |
| Programming Language :: Python :: 2.7                 | 0.2183     |
| Topic :: Software Development :: Libraries :: Pyth... | 0.2038     |
| Development Status :: 4 - Beta                        | 0.2038     |
| License :: OSI Approved :: BSD License                | 0.1632     |
| License :: OSI Approved :: MIT License                | 0.1529     |
| Environment :: Web Environment                        | 0.1487     |
| Programming Language :: Python :: 2.6                 | 0.1306     |

When you analyze the licenses with the trove classifiers you get a different
image:

```sql
SELECT
    `classifier`, COUNT(`id`) / 53533
FROM
    `package_classifiers`
WHERE
    `classifier` LIKE "License%"
GROUP BY
    `classifier`
ORDER BY
    COUNT(`id`) DESC
```

| License                                                                        | Percentage |
| ------------------------------------------------------------------------------ | ---------- |
| License :: OSI Approved :: BSD License                                         | 0.1632     |
| License :: OSI Approved :: MIT License                                         | 0.1529     |
| License :: OSI Approved :: GNU General Public License (GPL)                    | 0.0625     |
| License :: OSI Approved :: Apache Software License                             | 0.0460     |
| License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL) | 0.0188     |

There are 94 trove classifiers with five or less packages which use this
classifier. I guess many of them are not in the official list of classifiers.


## Package type

```sql
SELECT
    `packagetype`, COUNT(`id`)
FROM
    `urls`
GROUP BY
    packagetype
ORDER BY
    COUNT(`id`) DESC
```

gives

| Package type   | Count |
| -------------- | ----- |
| sdist          | 47649 |
| bdist_egg      | 4933  |
| bdist_wheel    | 3098  |
| bdist_wininst  | 1512  |
| bdist_dumb     | 577   |
| bdist_msi      | 45    |
| bdist_rpm      | 35    |
| bdist_dmg      | 4     |

Can anybody explain what this means?


## Downloads

```sql
SELECT
    `name`, `url`, `downloads`
FROM
    `urls`
JOIN
    `packages` ON `urls`.`package_id` = `packages`.`id`
ORDER BY
    `urls`.`downloads`  DESC
LIMIT 10
```

gives

| Package type                                              | Count    |
| --------------------------------------------------------- | -------- |
| [wincertstore](https://pypi.python.org/pypi/wincertstore) | 10026403 |
| [ssl](https://pypi.python.org/pypi/ssl)                   | 8987455  |
| [pyasn1](https://pypi.python.org/pypi/pyasn1)             | 8655361  |
| [Paste](https://pypi.python.org/pypi/Paste)               | 8401111  |
| [PyYAML](https://pypi.python.org/pypi/PyYAML)             | 7180547  |
| [distribute](https://pypi.python.org/pypi/distribute)     | 6276421  |
| [MarkupSafe](https://pypi.python.org/pypi/MarkupSafe)     | 6215382  |
| [ecdsa](https://pypi.python.org/pypi/ecdsa)               | 6030395  |
| [meld3](https://pypi.python.org/pypi/meld3)               | 5715687  |
| [pika](https://pypi.python.org/pypi/pika)                 | 5567400  |


and

```sql
SELECT
    `name`, SUM(`downloads`)
FROM
    `releases`
JOIN
    `packages` ON `releases`.`package_id` = `packages`.`id`
GROUP BY
    `name`
ORDER BY
    SUM(`downloads`)  DESC
LIMIT 10
```

| Package type                                              | Count    |
| --------------------------------------------------------- | -------- |
| [setuptools](https://pypi.python.org/pypi/setuptools)     | 45485205 |
| [requests](https://pypi.python.org/pypi/requests)         | 35446321 |
| [virtualenv](https://pypi.python.org/pypi/virtualenv)     | 35039299 |
| [distribute](https://pypi.python.org/pypi/distribute)     | 34779943 |
| [boto](https://pypi.python.org/pypi/boto)                 | 29678066 |
| [six](https://pypi.python.org/pypi/six)                   | 28253705 |
| [certifi](https://pypi.python.org/pypi/certifi)           | 27381407 |
| [pip](https://pypi.python.org/pypi/pip)                   | 26266325 |
| [wincertstore](https://pypi.python.org/pypi/wincertstore) | 24831145 |
| [lxml](https://pypi.python.org/pypi/lxml)                 | 20901298 |


## Size

What is the biggest Python package?

```sql
SELECT
    `name`, `release_number`, `size`
FROM
    `releases`
JOIN
    `packages` ON `releases`.`package_id` = `packages`.`id`
ORDER BY
    `releases`.`size` DESC
LIMIT 30
```

| Package                                               | Version       | Size      |
| ----------------------------------------------------- | ------------- | --------- |
| [de422](https://pypi.python.org/pypi/de422)           | 2009.1        | 545298406 |
| de406                                                 | 1997.1        | 178260546 |
| [scipy](https://pypi.python.org/pypi/scipy)           | 0.13.3        | 62517637  |
| appdynamics-bindeps-linux-x86                         | 5913-master   | 57861536  |
| appdynamics-bindeps-linux-x64                         | 5913-master   | 56366211  |
| python-qt5                                            | 0.1.5         | 56259023  |
| python-qt5                                            | 0.1.8         | 56237972  |
| [pycalculix](https://pypi.python.org/pypi/pycalculix) | 0.92          | 56039839  |
| [wltp](https://pypi.python.org/pypi/wltp)             | 0.0.9-alpha.3 | 55414544  |
| [cefpython3](https://pypi.python.org/pypi/cefpython3) | 31.2          | 55163815

## Code

See [github.com/MartinThoma/algorithms](https://github.com/MartinThoma/algorithms/tree/master/PyPI).


## Related

* [Why are some packages on pypi.python.org/simple, but have no page?](http://stackoverflow.com/q/28010799/562769)
* [How can I find out when the last interaction on PyPI happened for a given package?](http://www.quora.com/How-can-I-find-out-when-the-last-interaction-on-PyPI-happened-for-a-given-package)
* [What is cheesecake_code_kwalitee_id on PyPI good for?](http://www.quora.com/What-is-cheesecake_code_kwalitee_id-on-PyPI-good-for)


## Further Ideas

* **Build a dependency graph**: Some of the code was already written. However,
  one has to download about 25&nbsp;GB of data, extract it and run over those
  files. This is quite a bit of work.
* Analyze package quality
    * Missing requirements
    * Missing metadata / description
    * Missing documentation
    * PEP8
    * Code duplication
* Malicious package search:
   * Check which package names are prefixes of other package names.
   * Find packages which upload data (dropbox?)
   * Find pacakges which remove data from your file system
