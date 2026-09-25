---
layout: post
title: Amazing Speed of C++
slug: amazing-speed-of-cpp
lang: en
author: Martin Thoma
date: 2012-05-04 07:58:58
category: Code
tags: CPP
featured_image:
---
C++ is amazingly fast. I took part in Google Code Jam - <a href="../google-code-jam-2012-round-1a-2012/" title="Google Code Jam 2012 – Round 1A 2012">Round 1A 2012</a> and solved one problem with Python. It took 30 mintues and 4.479 seconds for the large input set!

The same algorithm took only 33 seconds with C++! I compile C++ with O3 compiler optimization:
```bash
g++ -Wall -O3 Passwords.cpp -o Passwords.out
```

If I compile the same program with O0 it takes 1 minutes and 15 seconds.
