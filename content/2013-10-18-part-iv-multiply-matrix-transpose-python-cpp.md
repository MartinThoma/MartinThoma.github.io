---
layout: post
lang: en
title: Part IV: How to multiply matrix with its transpose in Python and C++
slug: part-iv-multiply-matrix-transpose-python-cpp
author: Martin Thoma
date: 2013-10-18 17:41:13.000000000 +02:00
category: Code
tags: Python, C
featured_image: 2012/03/Matrix-Inverses.png
---
<div class="info">This is Part IV of my matrix multiplication series. Part I was about simple implementations and libraries: <a href="../matrix-multiplication-python-java-cpp/">Performance of Matrix multiplication in Python, Java and C++</a>, Part II was about multiplication with the <a href="../strassen-algorithm-in-python-java-cpp/" title="Part II: The Strassen algorithm in Python, Java and C++">Strassen algorithm</a> and Part III will be about parallel matrix multiplication (I didn't write it yet).</div>

You can always multiply a matrix $J \in \mathbb{R}^{n \times m}$ with its transpose $J^T$, because $J^T \in \mathbb{R}^{m \times n}$. You will get a matrix $C \in \mathbb{R}^{n \times n}$.

Standard matrix multiplication of square matrices $\in \mathbb{R}^{n \times n}$ is in $\mathcal{O}(n^3)$. With the Strassen algorithm you can multiply in $\approx \cal O(n^{2.807})$. But this is for general matrix multiplication. When we do $J \cdot J^T$ we have more structure, so it might be possible to do this multiplication faster.

One important property of the result matrix $R = J \cdot J^T$ is symmetry. So $R_{i,j} = R_{j,i}$.
If we used the ikj-algorithm for this multiplication, we needed $n^2 \cdot m$ operations. This way, we only need $\frac{n^2 +n}{2} \cdot m$ operations. Yes, I know, asymptotically it is irrelevant. But skipping almost half of the operations is still quite good.

<h2>Python</h2>
<h3>NumPy</h3>
I guess doing this with NumPy is the best option:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-i",
    dest="filename",
    default="2000.in",
    help="input file with two matrices",
    metavar="FILE",
)
(options, args) = parser.parse_args()


def read(filename):
    lines = open(filename, "r").read().splitlines()
    J = []
    for line in lines:
        J.append(map(int, line.split("\t")))
    return numpy.matrix(J)


def printMatrix(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print("\t".join(map(str, line)))


J = read(options.filename)
R = J * J.T
printMatrix(R)
```

Time:
```bash

real	7m19.223s
user	7m12.147s
sys	0m2.388s

```

When you want to do this in an application, you might want to use <a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html">numpy.load</a>.

<h2>C++</h2>
<h3>First try</h3>
```cpp

#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getMatrixN(string filename) {
    std::ifstream inFile(filename.c_str());
    return std::count(std::istreambuf_iterator<char>(inFile),
             std::istreambuf_iterator<char>(), '\n');
}

int getMatrixM(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

void read(string filename, vector< vector<double> > &A) {
	string line;
	FILE* matrixfile = freopen(filename.c_str(), "r", stdin);

	int i = 0, j;
    double a;
	while (getline(cin, line) && !line.empty()) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			A[i][j] = a;
			j++;
		}
		i++;
	}

	fclose (matrixfile);
}

vector< vector<double> > ikjalgorithmTranspose(
                                   vector< vector<double> > &J,
								   vector< vector<double> > &T,
								   vector< vector<double> > &R,
                                   int n, int m) {
	for (register int i = 0; i < n; i++) {
		for (register int k = 0; k < m; k++) {
			for (register int j = i; j < n; j++) {
				R[i][j] += J[i][k] * T[k][j];
			}
		}
	}

	for (register int i = 0; i < n; i++) {
		for (register int j = 0; j < i; j++) {
			R[i][j] += R[j][i];
		}
	}

	return R;
}

void transpose(vector< vector<double> > &A,
               vector< vector<double> > &B, int n, int m) {
    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            B[j][i] = A[i][j];
        }
    }
}

void printMatrix(vector< vector<double> > &matrix, int n) {
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			if (j != 0) {
				cout << "\t";
			}
			cout << matrix[i][j];
		}
		cout << endl;
	}
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "../Testing/5161x7058.in";
	} else {
		filename = argv[2];
	}

	int n = getMatrixN(filename);
    int m = getMatrixM(filename);
	vector<double> inner (m);
	vector<double> inner2 (n);
	vector< vector<double> > J(n, inner), T(m, inner2), R(n, inner);
	read (filename, J);
    transpose(J, T, n, m);
	ikjalgorithmTranspose(J, T, R, n, m);
	printMatrix(R, n);
	return 0;
}

```

Time:
```bash

real	5m31.488s
user	5m27.560s
sys	0m1.812s

```

<h3>Direct multiplication</h3>
One might think that transposing first is a bad idea, because you can do this:
```cpp

vector< vector<double> > ikjDirect(vector< vector<double> > &J,
								   vector< vector<double> > &R,
                                   int n, int m) {
	for (register int i = 0; i < n; i++) {
		for (register int k = 0; k < m; k++) {
			for (register int j = 0; j < n; j++) {
				R[i][j] += J[i][k] * J[j][k];
			}
		}
	}
	return R;
}

```

I stopped execution after 15 minutes.
