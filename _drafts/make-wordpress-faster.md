---
layout: post
title: Make WordPress faster
author: Martin Thoma
date: 2011-09-22 07:13:22
categories: 
- The Web
tags: 
- SEO
- Web Development
- WordPress
featured_image: 2011/09/WordPress-Logo.png
---
Speed is important. On the one hand Google uses site speed for its page ranking. On the other hand your visitors will skip your page quite fast if your site isn't fast.

So, how do you make your Blog faster? Many plugins are available, but I guess its not a good idea to add all of them. I want to test the speed of my blog and get some data. I will decide which plugins I will install on basis of this data.
<h2>Testing environement</h2>
I don't want to get trouble with this blog, so I will <a title="Setting up WordPress" href="http://martin-thoma.com/setting-up-wordpress/">set up WordPress</a> with the same configuration on my local machine. This is also a good idea, as I will not have different results just because of a variable speed of my internet connection.

I will set up wordpress three times with exactly the same setup to assure that every plugin get the same chance.
<h2>Benchmarking</h2>
The first tool of my choice are the built-in Chrome developer tools. They are very simmilar to Firefox' Firebug with YSlow.

The second is <a title="Benchmarking PHP" href="http://martin-thoma.com/benchmarking-php/">ApacheBench</a>, a program which is available for Linux as "ab".
<h2>How do these Plugins work?</h2>
Several possibilites exists with which you can make WordPress faster:
<ul>
	<li><strong>Caching</strong>: WordPress builds the whole page dynamically for each user. Imagine a big set of toy blocks. You have decided how your building (website) should look like. You have chosen which toy blocks to use and in which order you would like them to appear. Without caching, WordPress re-builds always the whole building for each user. This isn't necessary. You can store the website and show the same page to many users.</li>
	<li><strong>Combining resources</strong>: Most WordPress Blogs have a lot of JavaScript, CSS and graphic files which need to be loaded and requested. If you combine some scripts, you don't need to request that many files.</li>
	<li><strong>Compression</strong>: You can compress your files with GZip.</li>
	<li><strong>Minification</strong>: It is very usefull to have comments in source code and HTML / CSS. But those comments are not needed by the user. So they could be stripped. Also the structuring with newlines / whitespaces is not needed by your reader.</li>
</ul>
<h2>Results before installing any speed plugin</h2>
I had
<ul>
	<li>7 CSS files,</li>
	<li>6 local JavaScript files,</li>
	<li>3 JavaScript files from s.ytimg.com,</li>
	<li>3 JavaScript files from b.scorecardresearch.com,</li>
	<li>16 files which could be gzipped,</li>
	<li>88 files which could be cached by the browser and</li>
	<li>3660 CSS rules which were not used.</li>
</ul>
[caption id="attachment_1231" align="alignnone" width="630" caption="Benchmark Before adding a Plugin: Audit"]<a href="http://martin-thoma.com/wp-content/uploads/2011/09/Benchmark-Before-Audit.png"><img class="size-full wp-image-1231" title="Benchmark Before: Audit" src="http://martin-thoma.com/wp-content/uploads/2011/09/Benchmark-Before-Audit.png" alt="Benchmark Before: Audit" width="630" height="385" /></a>[/caption]

The page took about 17 seconds to load (rendering + downloading):

[caption id="attachment_1251" align="alignnone" width="604" caption="Benchmark Before adding a Plugin: Timeline"]<a href="http://martin-thoma.com/wp-content/uploads/2011/09/Benchmark-Before-Timeline.png"><img class="size-large wp-image-1251 " title="Benchmark Before: Timeline" src="http://martin-thoma.com/wp-content/uploads/2011/09/Benchmark-Before-Timeline-1024x408.png" alt="Benchmark Before adding a Plugin: Timeline" width="604" height="240" /></a>[/caption]

[bash]moose@pc08:~$ ab -n 1000 -c 1 localhost/wordpress-wpsupercache
This is ApacheBench, Version 2.3 &lt;$Revision: 655654 $&gt;
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Apache/2.2.14
Server Hostname:        localhost
Server Port:            80

Document Path:          /wordpress-before
Document Length:        323 bytes

Concurrency Level:      1
Time taken for tests:   0.438 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Non-2xx responses:      1000
Total transferred:      586000 bytes
HTML transferred:       323000 bytes
Requests per second:    2282.66 [#/sec] (mean)
Time per request:       0.438 [ms] (mean)
Time per request:       0.438 [ms] (mean, across all concurrent requests)
Transfer rate:          1306.29 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.4      0       5
Waiting:        0    0   0.4      0       5
Total:          0    0   0.4      0       6

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      1
  98%      2
  99%      2
 100%      6 (longest request)[/bash]

<h2>Results after installing WP Super Cache</h2>
<a title="WP Super Cache" href="http://wordpress.org/extend/plugins/wp-super-cache/">WP Super Cache</a> has 2.5 million downloads and 1028 ratings gave in average 4 stars. Quite good.

However, this plugin neither supports minification nor 

I had to enable mod_headers and mod_expires via 
[bash]sudo a2enmod headers
sudo a2enmod expires
sudo /etc/init.d/apache2 restart[/bash]

I've installed it and used those settings:
<ul>
    <li>Easy &rarr; Caching On</li>
    <li>Advanced:
	<ul>
	    <li>Use mod_rewrite to serve cache files.</li>
	    <li>Compress pages so they’re served more quickly to visitors.</li>
            <li>304 Not Modified browser caching. Indicate when a page has not been modified since last requested.</li>
            <li>Don’t cache pages for known users.</li>
            <li>Cache rebuild. Serve a supercache file to anonymous users while a new file is being generated.</li>
	</ul>
     </li>
</ul>

This plugin recommends some other plugins:
<ul>
  <li><a href="http://wordpress.org/extend/plugins/wp-minify/" title="WP Minify">WP Minify</a>: reduces the number of files served by your web server by joining Javascript and CSS files together.</li>
  <li><a href="http://wordpress.org/extend/plugins/use-google-libraries/" title="Use Google Libraries">Use Google Libraries</a>: allows you to load some commonly used Javascript libraries from Google webservers.</li>
</ul>

The result of the audit was even worse: 1 more CSS file, 2 more local JS-files, 4 JS-files from a.vimeocdn.com.

The reason for this might be, that I hadn't been able to log out.

The timeline showed that loading the page was much faster: Only about 15 seconds to load and render the page. The page could be viewed after a second or two, of course.

[bash]moose@pc08:~$ ab -n 1000 -c 1 localhost/wordpress-wpsupercache
This is ApacheBench, Version 2.3 &lt;$Revision: 655654 $&gt;
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Apache/2.2.14
Server Hostname:        localhost
Server Port:            80

Document Path:          /wordpress-wpsupercache
Document Length:        323 bytes

Concurrency Level:      1
Time taken for tests:   0.651 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Non-2xx responses:      1000
Total transferred:      586000 bytes
HTML transferred:       323000 bytes
Requests per second:    1535.03 [#/sec] (mean)
Time per request:       0.651 [ms] (mean)
Time per request:       0.651 [ms] (mean, across all concurrent requests)
Transfer rate:          878.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     0    1   0.3      0       4
Waiting:        0    0   0.3      0       4
Total:          0    1   0.3      1       4
ERROR: The median and mean for the processing time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      2
 100%      4 (longest request)[/bash]



<h2>Results after installing W3 Total Cache</h2>
<a title="W3 Total Cache" href="http://wordpress.org/extend/plugins/w3-total-cache/">W3 Total Cache</a> has over 750,000 downloads and 1780 ratings with 4.5 stars in average. Thats amazing.

This plugin support minification, caching and using CDN. Lets see the results:
<ul>
  <li>Now I've got 5 CSS files (it were 7 before),</li>
  <li>10 JS-files (12 before) and</li>
  <li>3 local JS-files (6 before).</li>
</ul>

The page is now downloaded and rendered after 15 seconds.
[bash]moose@pc08:~$ ab -n 1000 -c 1 localhost/wordpress-wpsupercache
This is ApacheBench, Version 2.3 &lt;$Revision: 655654 $&gt;
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Apache/2.2.14
Server Hostname:        localhost
Server Port:            80

Document Path:          /wordpress-wpsupercache
Document Length:        323 bytes

Concurrency Level:      1
Time taken for tests:   0.651 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Non-2xx responses:      1000
Total transferred:      586000 bytes
HTML transferred:       323000 bytes
Requests per second:    1535.03 [#/sec] (mean)
Time per request:       0.651 [ms] (mean)
Time per request:       0.651 [ms] (mean, across all concurrent requests)
Transfer rate:          878.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     0    1   0.3      0       4
Waiting:        0    0   0.3      0       4
Total:          0    1   0.3      1       4
ERROR: The median and mean for the processing time are more than twice the standard
       deviation apart. These results are NOT reliable.

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      2
 100%      4 (longest request)
moose@pc08:~$ chmod 755 /var/www/wordpress-W3TotalCache/wp-content
moose@pc08:~$ chmod 777 /var/www/wordpress-W3TotalCache/wp-content
moose@pc08:~$ ab -n 1000 -c 1 localhost/wordpress-W3TotalCache
This is ApacheBench, Version 2.3 &lt;$Revision: 655654 $&gt;
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Apache/2.2.14
Server Hostname:        localhost
Server Port:            80

Document Path:          /wordpress-W3TotalCache
Document Length:        323 bytes

Concurrency Level:      1
Time taken for tests:   0.750 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Non-2xx responses:      1000
Total transferred:      586000 bytes
HTML transferred:       323000 bytes
Requests per second:    1332.78 [#/sec] (mean)
Time per request:       0.750 [ms] (mean)
Time per request:       0.750 [ms] (mean, across all concurrent requests)
Transfer rate:          762.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     1    1   0.5      1       8
Waiting:        0    1   0.4      1       8
Total:          1    1   0.5      1       8

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      2
  99%      3
 100%      8 (longest request)[/bash]


<h2>Results after Quick Cache</h2>
&nbsp;
<h2>Conclusion</h2>
<h2>Sources</h2>
<ul>
	<li><a title="Using site speed in web search ranking" href="http://googlewebmastercentral.blogspot.com/2010/04/using-site-speed-in-web-search-ranking.html">Using site speed in web search ranking.</a> 9 April 2010. Retrieved 22 September 2011.</li>
</ul>