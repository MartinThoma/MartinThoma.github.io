---
layout: post
lang: en
title: Benchmarking PHP
author: Martin Thoma
date: 2011-09-22 13:06:12.000000000 +02:00
category: Code
tags: PHP, Benchmark, Web Development
featured_image: 2011/09/PHP-logo.png
---
I used ApacheBenchmark (<a href="http://httpd.apache.org/docs/2.0/programs/ab.html" rel="nofollow">ab</a>) to make a few Benchmark tests I was interested in.

If you like to view some more, go to <a href="http://www.phpbench.com/" rel="nofollow">www.phpbench.com</a>.

The most important options are:
<ul>
	<li>-n: Number of requests to perform</li>
	<li>-c: Number of multiple requests to make</li>
</ul>


An empty file:
```bash
moose@pc07:~$ ab localhost/empty.php
This is ApacheBench, Version 2.3 &amp;lt;$Revision: 655654 $&amp;gt;
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        Apache/2.2.14
Server Hostname:        localhost
Server Port:            80

Document Path:          /empty.php
Document Length:        0 bytes

Concurrency Level:      1
Time taken for tests:   0.002 seconds
Complete requests:      1
Failed requests:        0
Write errors:           0
Total transferred:      210 bytes
HTML transferred:       0 bytes
Requests per second:    461.04 [#/sec] (mean)
Time per request:       2.169 [ms] (mean)
Time per request:       2.169 [ms] (mean, across all concurrent requests)
Transfer rate:          94.55 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     2    2   0.0      2       2
Waiting:        0    0   0.0      0       0
Total:          2    2   0.0      2       2

```

Now I make 1000 requests to this empty file:
```bash
ab -n 1000 -c 1 localhost/empty.php
```
Time per request:       1.158 [ms] (mean)

With a document of two bytes, I get 1.324 ms. A HTML-Document with 300 kB has 4.287 ms.

Now I'll begin the test I'm interested in. It is related to <a href="http://stackoverflow.com/questions/4738605/undefined-offset-with-count" rel="nofollow">this Stackoverflow Question</a>. I'll make 10000 requests per Benchmark:

```php
for($i=0; $i<5; $i++) {
    $maximum = max(
                    @count($MyArray[$i*7]),
                    @count($MyArray[$i*7+1]),
                    @count($MyArray[$i*7+2]),
                    @count($MyArray[$i*7+3]),
                    @count($MyArray[$i*7+4]),
                    @count($MyArray[$i*7+5]),
                    @count($MyArray[$i*7+6])
                   );
    echo $maximum.' ';
}
```

1.817 ms

```php
for($i=0; $i<5; $i++) {
    $chunk = array_intersect_key($MyArray, array($i*7=>1, $i*7+1=>2, $i*7+2=>3, $i*7+3=>4, $i*7+4=>5, $i*7+5=>6));
    if(count($chunk) > 0){$maximum = max(array_map('count', $chunk));}
    else {$maximum = 0;}
    echo $maximum.' ';
}
```

1.801 ms

```php
for($i=0;$i<5;$i++){
    $arr = array();
    for ($j=0;$j<=6;$j++) {
        if (isset($MyArray[$i*7+$j])) $arr[] = count($MyArray[$i*7+$j]);
        else {$arr[] = 0;}
    }
    $maximum = max($arr);
    echo $maximum.' ';
}
```

1.742 ms
