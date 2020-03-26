---
layout: post
title: Part III: Matrix multiplication on multiple cores in Python, Java and C++
slug: part-iii-matrix-multiplication-on-multiple-cores-in-python-java-and-c
author: Martin Thoma
date: 2013-10-21 16:39:35.000000000 +02:00
category: Code
tags: Python, C, Java, matrix multiplication
featured_image: 2012/03/Matrix-Inverses.png
---
<div class="info">This is Part III of my matrix multiplication series. <a href="../matrix-multiplication-python-java-cpp/">Part I</a> was about simple matrix multiplication algorithms and <a href="../strassen-algorithm-in-python-java-cpp/">Part II</a> was about the Strassen algorithm.
<a href="../part-iii-matrix-multiplication-on-multiple-cores-in-python-java-and-c/">Part III</a> is about parallel matrix multiplication.</div>
We got some pretty interesting results for matrix multiplication so far. Now, I would like to get to know in how far performance increases (or decreases) if I make use of multiple cores. I only have two cores, so I hope somebody with a better computer will also run the ikj single core algorithm form part I and the parallel version from this article and post the results as a comment.

<h2>The implementations</h2>
As last time, I&rsquo;ve added the scripts to a <a href="https://github.com/MartinThoma/matrix-multiplication">GIT repository</a>. So you can test it on your machine.

Before we start implementing code for multiple processors, we have to get an algorithm that is actually parallelisable. You could use <a href="https://en.wikipedia.org/wiki/Cannon%27s_algorithm">Cannon's algorithm</a>, a algorithm that makes use of <a href="http://en.wikipedia.org/wiki/Systolic_array">systolic arrays</a> or try to find a solution by your own. The <a href="http://www.netlib.org/lapack/lawnspdf/lawn96.pdf">Scalable Universal Matrix Multiplication Algorithm</a> (short: SUMMA) could also work. The paper that I've linked is well-written and easy to understand. You should definitively read it, if you're interested in matrix multiplication.

I will not use any advanced algorithm in this article. I will make the outer most for loop of the ikj-algorithm (see part I) execute in parallel.

More about parallel matrix multiplication:
<ul>
  <li><a href="http://www.mcs.anl.gov/~itf/dbpp/text/node45.html">Case Study: Matrix Multiplication</a></li>
  <li><a href="http://berrendorf.inf.fh-bonn-rhein-sieg.de/Parallel/index.html">berrendorf</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Matrix_multiplication#Algorithms_for_efficient_matrix_multiplication">Algorithms for efficient matrix multiplication</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Coppersmith%E2%80%93Winograd_algorithm">Coppersmith-Winograd algorith</a></li>
</ul>

<h2>Python</h2>
Because of global interpreter lock (GIL), you need to start new processes in Python (<a href="http://stackoverflow.com/a/9786225/562769">source</a>).

The ikj single core algorithm implemented in Python needs:
```bash

time python ikjMultiplication.py -i 2000.in > 2000-nonparallel.out

real	36m0.699s
user	35m53.463s
sys	0m2.356s

```

The most simple way to parallelize the ikj algorith is to use the <a href="http://docs.python.org/2/library/multiprocessing.html">multiprocessing module</a> and compute every line of the result matrix C with a new process. But for the 2000x2000-example, this would mean we started 2000 processes. The overhead is much worse than the benefit:
```bash

time python ikjMultiplication.py -i 2000.in > 2000-parallel.out

real	20m47.693s
user	40m34.460s
sys	0m2.092s

```

When we share memory, the code looks like this:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing, numpy, ctypes


def read(filename):
    lines = open(filename, "r").read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B


def printMatrix(matrix, f):
    for line in matrix:
        f.write("\t".join(map(str, line)) + "\n")


def lineMult(start):
    global A, B, mp_arr, part
    n = len(A)
    # create a new numpy array using the same memory as mp_arr
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int)
    C = arr.reshape((n, n))
    for i in range(start, start + part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]


def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    pool = multiprocessing.Pool(threadNumber)

    pool.map(lineMult, range(0, n, part))
    # mp_arr and arr share the same memory
    arr = numpy.frombuffer(mp_arr.get_obj(), dtype=ctypes.c_int)
    C = arr.reshape((n, n))
    return C


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not isfile(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x


if __name__ == "__main__":
    import argparse, sys
    from os.path import isfile
    from argparse import ArgumentParser

    parser = ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument(
        "-i",
        "--input",
        dest="filename",
        required=True,
        type=extant_file,
        help="input file with two matrices",
        metavar="FILE",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType(mode="w"),
        default=sys.stdout,
        dest="output",
        help="file to write output to (default=stdout)",
    )
    args = parser.parse_args()

    A, B = read(args.filename)
    n, m, p = len(A), len(A[0]), len(B[0])

    threadNumber = 2
    part = len(A) / threadNumber
    if part < 1:
        part = 1

    # shared, can be used from multiple processes
    mp_arr = multiprocessing.Array(ctypes.c_int, n * p)
    C = ikjMatrixProduct(A, B, threadNumber)
    printMatrix(C, args.output)
```

and it needs MUCH more time:
```bash

time python ikjMultiplication-shared.py -i 2000.in > 2000-parallel-2threads.out

real	131m35.433s
user	250m36.820s
sys	0m9.533s

```

When we don't use shared memory, things run faster:

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing, numpy, ctypes


def read(filename):
    lines = open(filename, "r").read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B


def printMatrix(matrix, f):
    for line in matrix:
        f.write("\t".join(map(str, line)) + "\n")


def lineMult(start):
    global A, B, C, part
    n = len(A)
    for i in range(start, start + part):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]


def ikjMatrixProduct(A, B, threadNumber):
    n = len(A)
    pool = multiprocessing.Pool(threadNumber)

    pool.map(lineMult, range(0, n, part))
    return C


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not isfile(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x


if __name__ == "__main__":
    import argparse, sys
    from os.path import isfile
    from argparse import ArgumentParser

    parser = ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument(
        "-i",
        "--input",
        dest="filename",
        required=True,
        type=extant_file,
        help="input file with two matrices",
        metavar="FILE",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=argparse.FileType(mode="w"),
        default=sys.stdout,
        dest="output",
        help="file to write output to (default=stdout)",
    )
    args = parser.parse_args()

    A, B = read(args.filename)
    n, m, p = len(A), len(A[0]), len(B[0])

    threadNumber = 2
    part = len(A) / threadNumber
    if part < 1:
        part = 1

    C = [[0 for i in range(n)] for j in range(n)]
    C = ikjMatrixProduct(A, B, threadNumber)
    printMatrix(C, args.output)
```

```bash

time python ikjMultiplication.py -i 2000.in > 2000-parallel-4threads.out

real	22m46.066s
user	41m42.396s
sys	0m2.324s


```

<h2>Java</h2>
Shell.java:
```java

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Shell {
	static List<ArrayList<ArrayList<Integer>>> read(String filename) {
		ArrayList<ArrayList<Integer>> A = new ArrayList<ArrayList<Integer>>();
		ArrayList<ArrayList<Integer>> B = new ArrayList<ArrayList<Integer>>();

		String thisLine;

		try {
			BufferedReader br = new BufferedReader(new FileReader(filename));
			// Begin reading A
			while ((thisLine = br.readLine()) != null) {
				if (thisLine.trim().equals("")) {
					break;
				} else {
					ArrayList<Integer> line = new ArrayList<Integer>();
					String[] lineArray = thisLine.split("\t");
					for (String number : lineArray) {
						line.add(Integer.parseInt(number));
					}
					A.add(line);
				}
			}

			// Begin reading B
			while ((thisLine = br.readLine()) != null) {
				ArrayList<Integer> line = new ArrayList<Integer>();
				String[] lineArray = thisLine.split("\t");
				for (String number : lineArray) {
					line.add(Integer.parseInt(number));
				}
				B.add(line);
			}
			br.close();
		} catch (IOException e) {
			System.err.println("Error: " + e);
		}

		List<ArrayList<ArrayList<Integer>>> res = new LinkedList<ArrayList<ArrayList<Integer>>>();
		res.add(A);
		res.add(B);
		return res;
	}

	static void printMatrix(int[][] matrix) {
		for (int[] line : matrix) {
			int i = 0;
			StringBuilder sb = new StringBuilder(matrix.length);
			for (int number : line) {
				if (i != 0) {
					sb.append("\t");
				} else {
					i++;
				}
				sb.append(number);
			}
			System.out.println(sb.toString());
		}
	}

	public static int[][] parallelMult(ArrayList<ArrayList<Integer>> A,
			ArrayList<ArrayList<Integer>> B, int threadNumber) {
		int[][] C = new int[A.size()][B.get(0).size()];
		ExecutorService executor = Executors.newFixedThreadPool(threadNumber);
		List<Future<int[][]>> list = new ArrayList<Future<int[][]>>();

		int part = A.size() / threadNumber;
		if (part < 1) {
			part = 1;
		}
		for (int i = 0; i < A.size(); i += part) {
			System.err.println(i);
			Callable<int[][]> worker = new LineMultiplier(A, B, i, i+part);
			Future<int[][]> submit = executor.submit(worker);
			list.add(submit);
		}

		// now retrieve the result
		int start = 0;
		int CF[][];
		for (Future<int[][]> future : list) {
			try {
				CF = future.get();
				for (int i=start; i < start+part; i += 1) {
					C[i] = CF[i];
				}
			} catch (InterruptedException e) {
				e.printStackTrace();
			} catch (ExecutionException e) {
				e.printStackTrace();
			}
			start+=part;
		}
		executor.shutdown();

		return C;
	}

	public static void main(String[] args) {
		String filename;
		int cores = Runtime.getRuntime().availableProcessors();
		System.err.println("Number of cores:\t" + cores);
		
		int threads;
		if (args.length < 3) {
			filename = "3.in";
			threads = cores;
		} else {
			filename = args[1];
			threads = Integer.parseInt(args[2]);
		}

		List<ArrayList<ArrayList<Integer>>> matrices = read(filename);
		ArrayList<ArrayList<Integer>> A = matrices.get(0);
		ArrayList<ArrayList<Integer>> B = matrices.get(1);
		int[][] C = parallelMult(A, B, threads);
		printMatrix(C);
	}
}

```

LineMultiplier.java:
```java

import java.util.ArrayList;
import java.util.concurrent.Callable;

public class LineMultiplier implements Callable<int[][]> {
	ArrayList<ArrayList<Integer>> A;
	ArrayList<ArrayList<Integer>> B;
	int start;
	int end;
	public int[][] C;

	public LineMultiplier(ArrayList<ArrayList<Integer>> a,
			ArrayList<ArrayList<Integer>> b, int s, int e) {
		A = a;
		B = b;
		C = new int[a.size()][b.get(0).size()];
		start = s;
		end = e;
	}

	@Override
	public int[][] call() {
		for (int i = start; i < end; i++) {
			for (int k = 0; k < B.size(); k++) {
				for (int j = 0; j < B.get(0).size(); j++) {
					C[i][j] += A.get(i).get(k) * B.get(k).get(j);
				}
			}
		}
		return C;
	}
}

```

Execute it with only one thread:
```bash

time java Shell -i 2000.in 1 > 2000-paralllel.out
Number of cores:	2
0

real	0m40.571s
user	0m42.259s
sys	0m0.388s

```

Execute it with two threads:
```bash

time java Shell -i 2000.in 2 > 2000-paralllel.out
Number of cores:	2
0
1000

real	0m30.188s
user	0m54.999s
sys	0m0.512s

```

Note that real time is lower than user time. The reason is simply that the execution time on each processor is added. So user time might be double as high as real time!

We got from 40.571s down to 0m30.188s!

<h3>Information for parallelism</h3>
<ul>
<li><a href="http://docs.oracle.com/javase/tutorial/essential/concurrency/pools.html">Thread pools</a></li>
<li><a href="http://www.ibm.com/developerworks/library/j-jtp0730/index.html">Java theory and practice: Thread pools and work queues</a></li>
<li><a href="http://stackoverflow.com/questions/tagged/java+parallel-processing">StackOverflow</a></li>
</ul>

<h2>C++</h2>
Making the ikj-algorithm parallel is trivial with C++. You only need to add <code>#pragma omp parallel for</code> before the outer most for loop and add <code>-fopenmp</code> as a compile flag!
(If you really want to see the code, go to <a href="https://github.com/MartinThoma/matrix-multiplication/tree/master/C%2B%2B/Parallel">my Git repository</a>.)

```bash

$ time ./ikj-algorithm.out 2 2000.in > 2000-parallel.out

real	0m12.563s
user	0m20.569s
sys	0m0.156s

```

So we got from 20.407 seconds down to 12.563 seconds by adding only one line!

<h3>More Information</h3>
<ul>
  <li><a href="http://bisqwit.iki.fi/story/howto/openmp/">Guide into OpenMP: Easy multithreading programming for C++</a></li>
</ul>
