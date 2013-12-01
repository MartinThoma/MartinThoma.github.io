---
layout: post
status: publish
published: true
title: MD5 cracking
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 3711
wordpress_url: http://martin-thoma.com/?p=3711
date: 2011-10-17 07:36:15.000000000 +02:00
categories:
- The Web
tags:
- MD5
- Internet Security
- hash
comments: []
---
MD5 is a cryptographic hash function. This means, you can give the MD5 algorithm a string and it will return another 32-character long alphanumeric string. The returned string looks quite random, but it isn't. If you use the same input, you always get the same 32 character output.

What is it good for?

Well, imagine you had a web application. Now an attacker found a security whole and can read the password-column in the database. If it was plain text, he could use the passwords to log into the users accounts. As it is hashed and the hash function can't be simply reverted. So the attacker can't take any advantage of the passwords he just read.

It is much more realistic that the attacker can read the whole database. So he can access sensitive user data. As it is very likely that you have some Email-Adresses in there, he could quite probably log into the Email-accounts of the users with the same password. If the password is hashed, it's not that simple. He has to try to crack the MD5 hashed passwords. 

I'll describe and test in the following how easy this is and how it could be done.

<h2>Tested Hashes</h2>
MD5 is a widely used cryptographic hash function. I wanted to know how easy it is to crack them, so I tested it. I used those passwords:
<ul>
<li>"computer": df53ca268240ca76670c8566ee54568a</li>
<li>"establishment": f469410e5ec7594a9c41603e06ccf6a3</li>
<li>"My Birthday": ce9dbd008dac54422b90b3f82f58dd40</li>
<li>"I'm born in 1990.": 834649b6298642a7576b10c6705842d8</li>
<li>"r4Nd0m9": cc11c3de28e4425eff27b2fb5f216903</li>
</ul>

<h2>Online Crackers</h2>
If you search for "md5 cracker" you find <a href="http://md5cracker.org/" rel="nofollow">some md5 crackers</a>. 
This website could crack <em>computer</em>, <em>establishment</em> and <em>My Birthday</em>. 
The other two hashes weren't cracked.

<h2>John the Ripper</h2>
Ubuntu-Users can easily install John the Ripper (sudo apt-get install john) and use it for cracking hashes. To do so, the have to create a file in their working directory (let's call it md5.txt) and execute the following command: 
{% highlight bash %}john --format=raw-MD5 md5.txt{% endhighlight %}

Here is the time, john needed to crack the hashes:
<ul>
<li>"computer": 0.521 seconds</li>
<li>"establishment": after 1 h it wasn't cracked</li>
<li>"My Birthday": after 5 min it wasn't cracked</li>
<li>"I'm born in 1990.": after 5 min it wasn't cracked</li>
<li>"r4Nd0m9": after 38 min it wasn't cracked</li>
</ul>

Okay, these results aren't good. But you can also use a wordlist (e.g. the 15 MB list from http://www.bright-shadows.net/download/downloads.php) and the command 
john --wordlist:tbswordlist1.txt --format=raw-MD5 md5.txt
<ul>
<li>"computer": df53ca268240ca76670c8566ee54568a</li>
<li>"establishment": 0.568 seconds</li>
<li>"My Birthday": not cracked</li>
<li>"I'm born in 1990.": not cracked</li>
<li>"r4Nd0m9": not cracked</li>
</ul>
