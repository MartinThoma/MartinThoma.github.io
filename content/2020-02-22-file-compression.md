---
layout: post
title: File Compression
slug: file-compression
author: Martin Thoma
date: 2020-02-22 20:00
category: My bits and bytes
tags: compression, gzip, bz2, 7z, zip, backup, speed
featured_image: logos/star.png
---
I'm currently creating a backup of my domain <a href="http://www.martin-thoma.de/">martin-thoma.de</a>.
It is pretty small, but the MySQL database behind it grew extremely as I stored
every drawing from <a href="http://write-math.com/">write-math.com</a> in there.
For this reason, I want to store that specific table in a compressed way. But
which compression format is the best for which use case?

This article is only about loss-less compression. There are many more things
to say about lossy compression.

## My System

<table class="table">
    <thead>
        <tr style="background-color:#cdcdcd">
            <th>&nbsp;</th>
            <th>Thinkpad T460p</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="background-color:#efefef">CPU (<a href="https://ark.intel.com/content/www/de/de/ark/compare.html?productIds=42925,88967">comparison on ark.inten.com</a>)</td>
            <td>8x Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">RAM</td>
            <td>8 GB</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">Video Card</td>
            <td>Nvidia GeForce 940MX</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">System</td>
            <td>Ubuntu 18.04.3 LTS</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">Disk</td>
            <td>SAMSUNG MZ7LN512HCHP (<a href="https://www.notebookcheck.com/Test-Lenovo-ThinkPad-T460p-Core-i7-GeForce-940MX-Notebook.163310.0.html#c2263026">PM871 series</a>)</td>
        </tr>
    </tbody>
</table>


## Usage

<table class="table">
    <thead>
        <tr>
            <th>Format</th>
            <th>(Un)compress</th>
            <th>Command</th>
            <th>Time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ZIP</td>
            <td>compress</td>
            <td><code>zip output.zip input.sql</code></td>
            <td>92s</td>
        </tr>
        <tr>
            <td>ZIP</td>
            <td>extract</td>
            <td><code><a href="https://linux.die.net/man/1/unzip">unzip</a> output.zip -d outputdir</code></td>
            <td>29s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code><a href="https://linux.die.net/man/1/gzip">gzip</a> -1 -k backup.sql</code></td>
            <td>51s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -2 -k backup.sql</code></td>
            <td style="background-color: #b1fcb1;">50s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -3 -k backup.sql</code></td>
            <td>54s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -4 -k backup.sql</code></td>
            <td>58s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -5 -k backup.sql</code></td>
            <td>65s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -6 -k backup.sql</code></td>
            <td>89s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -7 -k backup.sql</code></td>
            <td style="background-color: #ffbebe;">110s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -8 -k backup.sql</code></td>
            <td style="background-color: #ffbebe;">319s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>compress</td>
            <td><code>gzip -9 -k backup.sql</code></td>
            <td style="background-color: #ffbebe;">372s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>extract</td>
            <td><code>gzip -d backup.sql.gz</code> (-1 to -6)</td>
            <td>58s to 62s</td>
        </tr>
        <tr>
            <td>gzip</td>
            <td>extract</td>
            <td><code>gzip -d backup.sql.gz</code> (-7 to -9)</td>
            <td>49s to 50s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code><a href="https://linux.die.net/man/1/bzip2">bzip2</a> -1 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">287s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -2 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">285s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -3 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">294s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -4 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">301s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -5 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">363s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -6 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">356s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -7 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">364s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -8 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">407s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>compress</td>
            <td><code>bzip2 -9 -k -z backup.sql</code></td>
            <td style="background-color: #ffbebe;">369s</td>
        </tr>
        <tr>
            <td>bz2</td>
            <td>extract</td>
            <td><code>bzip2 -d backup.sql.bz2</code> (-1 to -9)</td>
            <td style="background-color: #ffbebe;">102s to 109s</td>
        </tr>
        <tr>
            <td>7z</td>
            <td>compress</td>
            <td><code>7z a backup.sql.7z backup.sql</code></td>
            <td style="background-color: #ffbebe;">466s</td>
        </tr>
        <tr>
            <td>7z</td>
            <td>extract</td>
            <td><code>7z e backup.sql.7z</code></td>
            <td>49s</td>
        </tr>
        <tr>
            <td>7z (ultra)</td>
            <td>compress</td>
            <td><code>7z a out.7z -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on backup.sql</code></td>
            <td style="background-color: red;">1562s</td>
        </tr>
    </tbody>
</table>


## 7z Benchmark

```
$ 7z b

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (506E3),ASM,AES-NI)

Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (506E3)
CPU Freq:  1737  2731  3166  3349  3271  3108  3181  3202  3157

RAM size:    7404 MB,  # CPU hardware threads:   8
RAM usage:   1765 MB,  # Benchmark threads:      8

                       Compressing  |                  Decompressing
Dict     Speed Usage    R/U Rating  |      Speed Usage    R/U Rating
         KiB/s     %   MIPS   MIPS  |      KiB/s     %   MIPS   MIPS

22:      15592   618   2455  15168  |     175880   731   2053  15002
23:      12156   632   1958  12386  |     171362   738   2008  14829
24:      13697   643   2289  14727  |     164813   754   1918  14465
25:      13105   654   2287  14964  |     151047   742   1812  13443
----------------------------------  | ------------------------------
Avr:             637   2247  14311  |              741   1948  14435
Tot:             689   2098  14373
```

and

```
$ 7z b -mm=\* -mmt=\*

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (506E3),ASM,AES-NI)

Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (506E3)
CPU Freq:  2661  2917  3208  3272  3177  3302  3269  3246  3188

RAM size:    7404 MB,  # CPU hardware threads:   8
RAM usage:    225 MB,  # Benchmark threads:      1


Method           Speed Usage    R/U Rating   E/U Effec
                 KiB/s     %   MIPS   MIPS     %     %

CPU                      100   3186   3186
CPU                      100   3180   3180
CPU                      100   3129   3129   100   100

LZMA:x1          11260   100   4121   4116   132   132
                 33725   100   2750   2746    88    88
LZMA:x5:mt1       2596   100   3245   3244   104   104
                 32537   100   2745   2744    88    88
LZMA:x5:mt2       5446   180   3780   6804   121   217
                 34839   100   2939   2939    94    94
Deflate:x1       38939   100   4944   4944   158   158
                112657   100   3500   3500   112   112
Deflate:x5        8530   100   3285   3284   105   105
                102640   100   3189   3186   102   102
Deflate:x7        5016   100   5558   5558   178   178
                121815   100   3780   3780   121   121
Deflate64:x5     11477   100   4961   4960   159   159
                118711   100   3713   3713   119   119
BZip2:x1          6447   100   3895   3895   125   125
                 30463   100   3303   3302   106   106
BZip2:x5          5066   100   4228   4228   135   135
                 15084   100   2961   2961    95    95
BZip2:x5:mt2      9708   194   4167   8103   133   259
                 42347   160   5185   8311   166   266
BZip2:x7          1648   100   4271   4271   137   137
                 27652   100   5423   5423   173   173
PPMD:x1           4516   100   4672   4671   149   149
                  4234   100   4987   4987   159   159
PPMD:x5           3289   100   5575   5574   178   178
                  3070   100   5753   5753   184   184
Delta:4         863808   100   5309   5307   170   170
                953462   100   5858   5858   187   187
BCJ            1672730   100   6852   6852   219   219
               1654731   100   6778   6778   217   217
AES256CBC:1     201192   100   4946   4945   158   158
                189151   100   4650   4649   149   149
AES256CBC:2     854545   100   7002   7000   224   224
               3411324   100   6986   6986   223   223
CRC32:1         398309   100   2901   2900    93    93
CRC32:4        1302032   100   2907   2906    93    93
CRC32:8        2657729   100   3604   3604   115   115
CRC64          1196491   100   2451   2450    78    78
SHA256          201949   100   4121   4120   132   132
SHA1            553725   100   5190   5183   166   166
BLAKE2sp        325681   100   7167   7165   229   229

CPU                      100   3364   3363
------------------------------------------------------
Tot:                     111   3690   4120   119   132


RAM usage:    901 MB,  # Benchmark threads:      4


Method           Speed Usage    R/U Rating   E/U Effec
                 KiB/s     %   MIPS   MIPS     %     %

CPU                      399   3084  12318
CPU                      400   3090  12353
CPU                      400   3090  12354   100   400

LZMA:x1          49593   397   4571  18130   148   587
                127780   399   2607  10406    84   337
LZMA:x5:mt1      11043   396   3482  13796   113   447
                123224   399   2602  10391    84   336
LZMA:x5:mt2      15408   694   2774  19250    90   623
                115385   394   2472   9730    80   315
Deflate:x1      127310   396   4079  16165   132   523
                377145   399   2934  11718    95   379
Deflate:x5       39249   399   3791  15112   123   489
                371312   399   2892  11527    94   373
Deflate:x7       15420   398   4291  17085   139   553
                370053   399   2880  11483    93   372
Deflate64:x5     32242   388   3596  13933   116   451
                364650   399   2855  11407    92   369
BZip2:x1         19452   399   2949  11753    95   381
                101048   399   2743  10955    89   355
BZip2:x5         15092   400   3150  12595   102   408
                 61031   400   2996  11979    97   388
BZip2:x5:mt2     16446   783   1754  13726    57   444
                 93754   727   2530  18402    82   596
BZip2:x7          4855   397   3166  12578   102   407
                 62094   400   3046  12177    99   394
PPMD:x1          14300   400   3701  14790   120   479
                 13009   399   3836  15320   124   496
PPMD:x5           9590   399   4075  16253   132   526
                  8516   394   4050  15960   131   517
Delta:4        2229140   399   3429  13696   111   443
               2407149   397   3727  14790   121   479
BCJ            4218363   398   4344  17278   141   559
               4682966   393   4880  19181   158   621
AES256CBC:1     516685   391   3250  12698   105   411
                488100   397   3018  11996    98   388
AES256CBC:2    2548047   399   5228  20874   169   676
               9436324   397   4874  19326   158   626
CRC32:1        1304042   400   2375   9493    77   307
CRC32:4        4019189   399   2246   8971    73   290
CRC32:8        7320978   400   2484   9927    80   321
CRC64          3549391   399   1824   7269    59   235
SHA256          505381   395   2607  10310    84   334
SHA1           1255910   380   3093  11755   100   381
BLAKE2sp        451934   377   2638   9943    85   322

CPU                      360   2275   8188
------------------------------------------------------
Tot:                     440   3063  13276    98   430


RAM usage:   1802 MB,  # Benchmark threads:      8


Method           Speed Usage    R/U Rating   E/U Effec
                 KiB/s     %   MIPS   MIPS     %     %

CPU                      596   2352  14024
CPU                      759   2489  18901
CPU                      727   2477  18016   110   800

LZMA:x1          20619   590   1277   7538    57   335
                110780   616   1466   9023    65   401
LZMA:x5:mt1       9602   633   1895  11997    84   533
                135560   734   1557  11432    69   508
LZMA:x5:mt2      10958   696   1968  13690    87   608
                114711   686   1411   9674    63   430
Deflate:x1      120232   707   2158  15267    96   678
                368073   728   1572  11437    70   508
Deflate:x5       39116   707   2131  15061    95   669
                391901   708   1719  12168    76   540
Deflate:x7       15543   736   2339  17222   104   765
                416000   756   1707  12910    76   573
Deflate64:x5     33348   703   2050  14411    91   640
                381221   742   1607  11926    71   530
BZip2:x1         19466   743   1583  11761    70   522
                107349   705   1650  11637    73   517
BZip2:x5         14640   757   1614  12219    72   543
                 77475   738   2061  15207    92   675
BZip2:x5:mt2     15561   731   1776  12987    79   577
                 80522   758   2085  15805    93   702
BZip2:x7          5127   775   1714  13284    76   590
                 69233   782   1737  13577    77   603
PPMD:x1          13343   739   1867  13800    83   613
                 11466   720   1876  13503    83   600
PPMD:x5           9060   740   2074  15355    92   682
                  5011   648   1449   9392    64   417
Delta:4        1425436   592   1478   8758    66   389
               1668622   575   1783  10252    79   455
BCJ            1763558   544   1328   7224    59   321
               2872698   569   2070  11767    92   522
AES256CBC:1     473162   723   1609  11628    71   516
                482136   744   1592  11849    71   526
AES256CBC:2    3391242   638   4356  27781   193  1234
               7308622   649   2307  14968   102   665
CRC32:1        2005570   744   1961  14601    87   648
CRC32:4        5340310   769   1550  11920    69   529
CRC32:8        8750400   749   1585  11866    70   527
CRC64          4884587   707   1416  10004    63   444
SHA256          469742   751   1277   9583    57   426
SHA1           1292792   725   1669  12101    74   537
BLAKE2sp        810867   764   2335  17839   104   792

CPU                      775   2390  18537
------------------------------------------------------
Tot:                     696   1710  11921    76   529
```


## Compression Rates

<table class="table">
    <thead>
        <tr>
            <th>File</th>
            <th>File Size</th>
            <th>.zip</th>
            <th>.gz</th>
            <th>.bz2</th>
            <th>.7z</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>MySQL DB dump</td>
            <td>3.5 GB</td>
            <td><span style="color: orange">634 MB</span></td>
            <td>1: 737 MB<br/>2: 729 MB<br/>3: 722 MB<br/>4: 654 MB<br/>5: 638 MB<br/><span style="color: orange">6: 634 MB</span><br/>7: 610 MB<br/>8: 606 MB<br/>9: 606 MB</td>
            <td>1: 534 MB<br/>2: 525 MB<br/>3: 521 MB<br/>4: 519 MB<br/>5: 518 MB<br/>6: 518 MB<br/>7: 518 MB<br/>8: 518 MB<br/>9: 518 MB</td>
            <td>default: 471 MB<br/>ultra: 398 MB</td>
        </tr>
    </tbody>
</table>

## Features

<table class="table">
    <thead>
        <tr>
            <th>Format</th>
            <th>Archiving</th>
            <th>Compression</th>
            <th>Integrity Check</th>
            <th>Partial Extraction</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://sevenzip.osdn.jp/chm/cmdline/">7z</a> (<a href="https://linux.die.net/man/1/7z">man</a>)</td>
            <td style="color: green;">✔</td>
            <td style="color: green;">✔</td>
            <td style="color: green;">✔</td>
            <td style="color: green;"><a href="https://unix.stackexchange.com/q/460615/4784">✔</a></td>
        </tr>
        <tr>
            <td>zip (<a href="https://linux.die.net/man/1/zip">man</a>)</td>
            <td style="color: green;">✔</td>
            <td style="color: green;">✔</td>
            <td style="color: green;"><a href="https://unix.stackexchange.com/a/197136/4784">✔</a></td>
            <td style="color: green;">✔</td>
        </tr>
        <tr>
            <td>tar (<a href="https://linux.die.net/man/1/tar">man</a>)</td>
            <td style="color: green;">✔</td>
            <td style="color: red;">✗</td>
            <td></td>
            <td style="color: green;"><a href="https://unix.stackexchange.com/a/35315/4784"></a></td>
        </tr>
        <tr>
            <td>gzip (<a href="https://linux.die.net/man/1/gzip">man</a>)</td>
            <td style="color: red;">✗</td>
            <td style="color: green;">✔</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>bzip2 (<a href="https://linux.die.net/man/1/bzip2">man</a>)</td>
            <td style="color: red;">✗</td>
            <td style="color: green;">✔</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

## See also

* Wikipedia:
    * [List of archive formats](https://en.wikipedia.org/wiki/List_of_archive_formats)
    * [Comparison of file archivers](https://en.wikipedia.org/wiki/Comparison_of_file_archivers)
    * [Hutter Prize](https://en.wikipedia.org/wiki/Hutter_Prize)
* Martin Thoma: [Data Backup Strategies](https://martin-thoma.com/data-backup-strategies/), 2013.
* Jeff Atwood:
    * [File Compression in the Multi-Core Era](https://blog.codinghorror.com/file-compression-in-the-multi-core-era/), 2009.
    * [Don't Use ZIP, Use RAR](https://blog.codinghorror.com/dont-use-zip-use-rar/), 2007.
    * [Compression and Cliffs](https://blog.codinghorror.com/compression-and-cliffs/), 2005.
* Lossy compression:
    * Jeff Atwood: [A Comparison of JPEG Compression Levels and Recompression](https://blog.codinghorror.com/a-comparison-of-jpeg-compression-levels-and-recompression/)
    * Jeff Atwood: [Getting the Most Out of PNG](https://blog.codinghorror.com/getting-the-most-out-of-png/), 2007.
* [What is the maximum size of a zip file on Windows 10 Pro 64-Bit?](https://superuser.com/q/1305867/64857), 2018