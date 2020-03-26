---
layout: post
title: Google Code Jam Templates
author: Martin Thoma
date: 2013-04-26 11:17:35.000000000 +02:00
category: Code
tags: Python, PHP, C, Java, Google Code Jam
featured_image: 2012/04/code-jam-logo.png
---
Here are some templates that are a good start for Google Code Jam.

<h2>C++</h2>
```cpp

#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
    /* number of test cases */
    unsigned short int testcases;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
        for (int zeile=0; zeile<4; zeile++) {
            for (int spalte=0; spalte<4; spalte++) {
                cin >> game[zeile][spalte];
            }
        }
        cout << "Case #" << i << ": " << solve() << endl;
    }

    return 0;
}

```

Compile
```bash
g++ A.cpp
```

Execute
```bash
./a.out < A-small-practice.in > result.txt
```

<h2>Python</h2>
<ul>
  <li>Input: <a href="http://docs.python.org/2/library/functions.html#input">input</a>, <a href="http://docs.python.org/2/library/functions.html#raw_input">raw_input()</a></li>
  <li>String parsing: <a href="http://docs.python.org/2/library/stdtypes.html#str.strip">strip()</a>, <a href="http://docs.python.org/2/library/stdtypes.html#str.split">split()</a></li>
</ul>

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()

    for caseNr in range(1, testcases + 1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
```

Execute
```bash
python A.py < A-small-practice.in > result.txt
```

<h2>Java</h2>
This is an ajusted version of mystics solution for "Dancing with Googlers". You might want to take a look at <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html">Scanner</a> and <a href="http://docs.oracle.com/javase/7/docs/api/java/io/PrintWriter.html">PrintWriter</a>.
```java

import java.util.*;
import java.io.*;

public class DancingWithGoogle {
	final static String PROBLEM_NAME = "dance";
	final static String WORK_DIR = "/home/moose/Desktop/" + PROBLEM_NAME + "/";
	final static String INPUT_FILE_NAME = "input.txt";
	final static String OUTPUT_FILE_NAME = "output.txt";

	static int[][] maxBest = new int[31][2];

	static void preprocess() {
		for (int i = 0; i <= 30; i++)
			Arrays.fill(maxBest[i], -1);

		for (int A = 0; A <= 10; A++)
			for (int B = A; B <= 10 && B <= A + 2; B++)
				for (int C = B; C <= 10 && C <= A + 2; C++) {
					int tot = A + B + C, sur = (C - A == 2 ? 1 : 0);
					maxBest[tot][sur] = Math.max(maxBest[tot][sur], C);
				}
	}

	void solve(Scanner sc, PrintWriter pw) {
		int N = sc.nextInt();
		int S = sc.nextInt();
		int p = sc.nextInt();
		int[] tot = new int[N];
		for (int i = 0; i < N; i++)
			tot[i] = sc.nextInt();

		int[][] dp = new int[N + 1][N + 1];
		for (int i = 0; i <= N; i++)
			Arrays.fill(dp[i], -100000);
		dp[0][0] = 0;

		for (int pos = 0; pos < N; pos++)
			for (int sur = 0; sur <= pos; sur++)
				for (int nSur = 0; nSur < 2; nSur++)
					if (maxBest[tot[pos]][nSur] >= 0)
						dp[pos + 1][sur + nSur] = Math.max(dp[pos + 1][sur
								+ nSur], dp[pos][sur]
								+ (maxBest[tot[pos]][nSur] >= p ? 1 : 0));

		pw.println(dp[N][S]);
	}

	public static void main(String[] args) throws Exception {
		preprocess();

		Scanner sc = new Scanner(new FileReader(WORK_DIR + INPUT_FILE_NAME));
		PrintWriter pw = new PrintWriter(new FileWriter(WORK_DIR
				+ OUTPUT_FILE_NAME));
		int caseCnt = sc.nextInt();
		for (int caseNum = 0; caseNum < caseCnt; caseNum++) {
			System.out.println("Processing test case " + (caseNum + 1));
			pw.print("Case #" + (caseNum + 1) + ": ");
			new DancingWithGoogle().solve(sc, pw);
		}
		pw.flush();
		pw.close();
		sc.close();
	}
}

```

Adjust the path and execute it within Eclipse.

<h2>PHP</h2>
Input / output:
<ul>
  <li>\$fp = <a href="http://php.net/manual/en/function.fopen.php">fopen</a> (<a href="http://php.net/manual/en/reserved.variables.argv.php">$argv[1]</a>, 'r'): Open file pointer to file in first command line argument</li>
  <li>string <a href="http://php.net/manual/en/function.fgets.php">fgets</a> (\$fp): Read one line</li>
</ul>

Execute:
```bash
php A.php input.txt > output.txt
```

<h2>JavaScript</h2>
Did you know that you can also solve those tasks with JavaScript? I've explained <a href="http://stackoverflow.com/a/16242806/562769">how to install v8</a>.

Here is a <a href="http://www.go-hero.net/jam/13/name/aditsu">solution from aditsu</a>:
```javascript

// run with v8: d8 file.js < file.in

var m, res, dot

function check(x0, y0, dx, dy) {
	var x = 0
	var o = 0
	var t = 0
	for (var i = 0; i < 4; ++i) {
		switch (m[x0 + i * dx][y0 + i * dy]) {
		case 'X':x++;break
		case 'O':o++;break
		case 'T':t++;break
		case '.':dot=1;break
		}
	}
	if (x + t == 4) res = 'X'
	if (o + t == 4) res = 'O'
}

var t = readline()
for (var i = 1; i <= t; ++i) {
	m = []
	for (var j = 0; j < 4; ++j) {
		m[j] = readline()
	}
	readline()
	res = null
	dot = 0
	for (var j = 0; j < 4; ++j) {
		check(j, 0, 0, 1)
		check(0, j, 1, 0)
	}
	check(0, 0, 1, 1)
	check(3, 0, -1, 1)
	res = res ? res + ' won' : dot ? 'Game has not completed' : 'Draw'
	print('Case #' + i + ': ' + res)
}

```
