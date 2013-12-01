---
layout: post
status: publish
published: true
title: ! 'Part I: Performance of Matrix multiplication in Python, Java and C++'
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 27371
wordpress_url: http://martin-thoma.com/?p=27371
date: 2012-06-18 21:37:46.000000000 +02:00
categories:
- Code
tags:
- Python
- C
- Java
- Linear algebra
- NumPy
- Boost
- SciPy
- matrix multiplication
comments:
- id: 168411
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNi0yMSAxMzo0NDoyNyArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNi0yMSAxMTo0NDoyNyArMDIwMA==
  content: ! "My professor for software engineering - who also inspired me to write
    this post - had some remarks:\r\n\r\n* I should use 64-Bit double matrices, as
    int-matrices aren't interesting.\r\n* I probably don't have a native JVM which
    would boost Java\r\n\r\nA student suggested, that I should give a try to pypy.
    I'll do both later"
- id: 169141
  author: Moritz
  author_email: moritz.klammler@gmail.com
  author_url: http://klammler.eu
  date: !binary |-
    MjAxMi0wNi0yMiAwNToxNzo0NyArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNi0yMiAwMzoxNzo0NyArMDIwMA==
  content: ! "Hi Martin,\r\n\r\nnice article.\r\n\r\nI think you should generally
    wrap the code that does the actual multiplication between calls to clock() to
    determine the computation time rather than measuring the overall execution time
    of the program.  For the faster solutions, the latter will effectively measure
    the I/O time, which is not interesting here.\r\n\r\nI've written a test for
    Fortran which is usually considered the gold standard in number crunching.  On
    my machine, it performs only insignificantly better than the C++ solution.  (Fortran
    has an intrinsic matrix multiplication function, matmul.  I've also tried the
    BLAS degemm subroutine but it wasn't faster.)  Eventually, I'll make a commit
    to your code later.\r\n\r\nI don't think, you did BOOST/uBLAS justice, however.
    \ First, please\r\n\r\n    #define NDEBUG 1\r\n\r\nto switch off all debugging
    normally enabled by uBLAS.  This reduced computation time by a factor of six or
    so, on my machine.  Second, you may use\r\n\r\n    #include \r\n    //
    ...\r\n    boost::numeric::ublas::matrix C(result.A.size1(), result.B.size2());\r\n
    \   boost::numeric::ublas::axpy_prod(result.A, result.B, C, true);\r\n\r\nas a
    better performing alternative.\r\n\r\nWhen I did so, the code was nothing slower
    than your implementation.  Of course, one would generally hope to improve performance
    when using a library (not just not make it worse), however, I'm not certain by
    any means that this is the end of all possible optimization.\r\n\r\nLooking forward
    to see your Blitz++ solution as I couldn't get it figured out either.\r\n\r\nEventually,
    I will also commit a makefile that compiles and runs all the different implementations
    and automatically logs the performance.\r\n\r\nRegarding the Python solutions:
    \ Most of the time in the na(t)ive solution is wasted on the n**3 type checks,
    the Python interpreter must perform during the multiplication.  I'm not sure if
    PyPy's JIT compilation could help much here.  I'm sure you know but I think it
    is worth to mention that NumPy uses external C modules which again link to the
    Fortran routines of the LAPACK / BLAS library so the additional time compared
    with the Fortran solution is basically used for caling the subroutines and passing
    around the data.  As far as I know, numpy.matrix is the same as scipy.matrix.\r\n\r\nThe
    BLAS and other high-performance libraries make use of architecture-specific optimization
    so it might matter how one installs and sets them up.  I think the manual iteration
    could be made even faster if you'd break the matrix into its memory pages so even
    less page swaps will be needed.  This will, in general, also be a non-portable
    effort, of course.\r\n\r\n\r\nBest\r\n\r\nMoritz"
- id: 169181
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wNi0yMiAwOTo0OToyMSArMDIwMA==
  date_gmt: !binary |-
    MjAxMi0wNi0yMiAwNzo0OToyMSArMDIwMA==
  content: ! "Hi Moritz,\r\n\r\nthanks for your answer! I thought about measuring
    the time after the read operation and stopping it before the program is going
    to write. I didn't do it for two reasons:\r\n* I want to get comparable results.
    This includes ...\r\n  * the resulting matrix which I want to diff with the correct
    result.\r\n  * using the same method of getting the time for every language.\r\n*
    It is also important to get to know if the I/O speed of different languages
    is significantly different. My guess is that I could speed up I/O for Python
    as well as for Java. But how can I do so?\r\n* I would like to get the time of
    matrix multiplication for many matrices. How does the time change when I use 100x100
    matrices? I'm currently working on a detailed answer. Here is the short one: I
    want to create many matrices, loop in the bash over the files, execute the program
    for each file once, store the time in a CSV-file and plot this file with LaTeX.
    This task gets much more difficult if I can't control the format of the output
    time. As matrix multiplication is in O(n^3) for the given algorithms I guess the
    results will not be very interesting, but this approach might be interesting for
    other problems, too. And I also thought that all libraries would give boring results
    which was obviously not true.\r\n\r\nSo I/O is also part of the task for every
    programming language. If I have an I/O heavy task and my preferred programming
    language is slow at I/O I can't just say \"hey, my language is very fast at
    computation, I/O isn't interesting\". I admit that the title might be misleading,
    but calling it \"Part I: Performance of Matrix reading, multiplying and writing
    in Python, Java and C++\" would be much too long.\r\n\r\nNevertheless, I am also
    interested in exact I/O-time results. As you're interested in them, you could
    time the I/O of Java and post the results.\r\n\r\nI read about the Debugging-Flags
    on Stack Overflow. According to the author of this answer, Boost is still slower
    than the ikj-algorithm. \r\nThanks for your suggestions how to increase the performance
    for the boost part, I'll include that as soon as I have some time."
- id: 1164431
  author: Jaan
  author_email: jaanvajakas@hot.ee
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0wMiAxODozMzo0MiArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0wMiAxNjozMzo0MiArMDIwMA==
  content: ! "The Java code example could certainly be improved. One, who needs to
    efficiently hold and access large collections of numbers, should use primitive
    arrays (i. e. int[][] and double[][]) instead of ArrayList/Vector of Integers
    or Doubles. (Perhaps even better performance could be achieved by using one-dimensional
    arrays int[m*n] and double[m*n] for m-by-n matrices.)\r\n\r\nIntegers and Doubles
    are slow compared to int and double because of object dereferencing overhead,
    bad memory locality (due to high memory usage overhead per element), and time
    spent on object creation/garbage collection (for two 2000*2000 matrices, 2*2000*2000=8,000,000
    Integer objects is quite a lot for the garbage collector to scan)."
- id: 1172621
  author: Kairat
  author_email: kairat_bmstu@mail.ru
  author_url: ''
  date: !binary |-
    MjAxMy0wNC0xMSAwNzozMToxNSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNC0xMSAwNTozMToxNSArMDIwMA==
  content: ! "The java code example is wrong. \r\n\r\nUsing  reference types like
    Integer, Double , Long is not good a idea for such tasks, cause they use too much
    of dynamic memory. \r\n\r\nSo u should increase the memory for jvm , or use primitive
    types like int or double. \r\n\r\nWhat parameters for JVM did you use ? \r\n\r\nDid
    you use JIT-compiler  of JVM ?"
- id: 1202341
  author: Marc Claesen
  author_email: claesenm@gmail.com
  author_url: http://www.marc-claesen.name
  date: !binary |-
    MjAxMy0wNi0wMSAxMDoyNToyOCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0wMSAwODoyNToyOCArMDIwMA==
  content: ! "I am surprised you are benchmarking matrix multiplication without using
    the BLAS and/or ATLAS. Those are the standard libraries for such kind of thing.
    In ATLAS, a 2000x2000 matrix multiplication will require far less than 15 seconds
    (probably less than 2).\r\n\r\nThe Basic Linear Algebra Software (BLAS) is a collection
    of vector/matrix computations, organized in 3 levels of increasing complexity.
    It's pretty much the standard API for any serious algebra (originally written
    in Fortran, comes with interfaces to C++, Java, Python ...). Highly optimized
    vendor-specific implementations of the BLAS exist such as Intel Math Kernel Library
    (MKL). The Automatically Tuned Linear Algebra Software (ATLAS) is a package that
    self-optimizes for your own system by running various tests prior to compiling
    (it optimizes itself for cache use and more).\r\n\r\nThe BLAS is usually installed
    by default on most Linux distributions. If not, it should at least be listed in
    your favorite package manager.\r\nFor ATLAS: http://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software\r\n\r\nFinally,
    I strongly advise to time in high priority mode (e.g. sudo nice -3 time ...).
    The measurements you have made in normal priority can be very noisy if other processes
    are interfering."
- id: 1202351
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMy0wNi0wMSAxMTowMDo1MSArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0wMSAwOTowMDo1MSArMDIwMA==
  content: ! "Hi Marc,\r\n\r\nthanks for your comment. Could you please make a minimal
    example how to use BLAS and/or ATLAS?\r\n\r\nWhat's the difference between
    BLAS and uBlas (which I've used, see \"Boost\")?"
- id: 1203201
  author: Marc Claesen
  author_email: claesenm@gmail.com
  author_url: http://www.marc-claesen.name
  date: !binary |-
    MjAxMy0wNi0wMiAxMjo1NTo0OCArMDIwMA==
  date_gmt: !binary |-
    MjAxMy0wNi0wMiAxMDo1NTo0OCArMDIwMA==
  content: ! "Hi Martin,\r\n\r\nInterfacing to BLAS and ATLAS is easy if you use their
    C interfaces. For example, for single precision matrix-matrix multiplication you
    need to interface with sgemm (dgemm for double precision). \r\n\r\nIn C++, this
    is done by declaring the API function as extern:\r\n\r\nenum CBLAS_ORDER {CblasRowMajor=101,
    CblasColMajor=102};\r\nenum CBLAS_TRANSPOSE {CblasNoTrans=111, CblasTrans=112,\r\n
    \   CblasConjTrans=113, AtlasConj=114};\r\n\r\nextern \"C\"{\r\nvoid cblas_sgemm(const
    enum CBLAS_ORDER Order, const enum CBLAS_TRANSPOSE\r\n   TransA, const enum CBLAS_TRANSPOSE
    TransB, const int M, const int N,\r\n   const int K, const float alpha, const
    float *A, const int lda, \r\n   const loat *B, const int ldb, const float beta,
    float *C, const int ldc);\r\n}\r\n\r\nYou can google these functions to find their
    documentation and how to use them. You'll need to link to BLAS/ATLAS libraries
    during compilation to use the functions (-lblas or -latlas).\r\n\r\nI am not familiar
    with uBlas, so I can't say what the difference are. The reference implementation
    of the BLAS is the netlib version (this is not optimized). If you want to use
    ATLAS, you can download it for free and tune/compile it yourself. ATLAS offers
    the xgemm routines in its API, so you don't have to make any changes in your code.\r\n\r\nTo
    give you some idea with regards to performance, I recently timed a medium-scale
    matrix-matrix multiplication (2.000x37.000 times 37.000x2.000) with the following
    results (relative):\r\n- optimal loop order + SIMD instructions: 1\r\n- default
    BLAS on debian wheezy: 1/45\r\n- ATLAS: 1/110\r\n\r\nHopefully this is
    useful for you!\r\n\r\nMarc"
featured_image: 2011/09/Python-Logo.png
---
<div class="info">This is Part I of my matrix multiplication series. <a href="http://martin-thoma.com/matrix-multiplication-python-java-cpp/">Part I</a> was about simple matrix multiplication algorithms and <a href="http://martin-thoma.com/strassen-algorithm-in-python-java-cpp/">Part II</a> was about the Strassen algorithm.
<a href="part-iii-matrix-multiplication-on-multiple-cores-in-python-java-and-c">Part III</a> is about parallel matrix multiplication.</div>

This post is about simple implementations of matrix multiplications. The goal of this post is to find out how easy it is to implement a matrix multiplication in Python, Java and C++. Additionally, I want to get to know how good these solutions are.

The second post will be an implementation of the Strassen algorithm for matrix multiplication. <a href="http://en.wikipedia.org/wiki/Strassen_algorithm">Strassen algorithm</a> does matrix multiplication in $\cal O(n^{log_2(7)+o(1)}) \approx \cal O(n^{2.807})$ instead of $\cal O(n^3)$. I am quite sure this will outperform almost every other change. See Part II: <a href="http://martin-thoma.com/strassen-algorithm-in-python-java-cpp/">The Strassen algorithm in Python, Java and C++</a>.

The third post will be about parallel programming. I have two cores and I want to see if it will be significantly faster if I use both of them.

<h2>The implementations</h2>
I will post all scripts for this test and I've added a <a href="https://github.com/MartinThoma/matrix-multiplication">GIT repository</a>, so feel free to test it on your machine. I am also happy if you post some of your solutions with running times :-) I am quite sure that my Java and C++ code can be written much better. If you know how, please leave a comment.
If you know other languages, you could create a script for these. I focus on Python, Java and C++ as they are very often used.

I have implemented these three types of algorithms for this post:
<ul>
    <li><strong>ijk-algorithm</strong>: This is a simple, straight forward implementation of a matrix multiplication. I've used the definition of matrix multiplication. I didn't use multiple threads.</li>
    <li><strong>ikj-algorithm</strong>: just like the ijk-algorithm, but I've switched two of the three the for-loops.</li>
    <li><strong>Library-functions</strong>: I always prefer libraries over self-implemented solutions. I think they are faster than anything I could come up with in a reasonable amount of time.</li>
</ul>

If you post a solution, please consider these restrictions:
<ul>
    <li><strong>Input</strong>: The input file should get passed with the parameter <code>-i</code>, e.g.: 
    <code>python -i 2000.in</code> or <code>java Shell -i 2000.in</code></li>
    <li>The standard value for the command line parameter -i should be "2000.in" (a $2000 \times 2000$ matrix)</li>
    <li>The user should <em>not</em> have to give the size of the matrix!</li>
    <li>The two square-matrices that should get multiplied are ...
    <ul>
    <li>... read from a text-file.</li>
    <li>... represented like this:
        <ul>
        <li>Every line of one matrix is one line in the text-file.</li>
        <li>Newlines are only "\n".</li>
        <li>Every number is separated by "\t".</li>
        <li>The both matrices are separated by one newline.</li>
        </ul>
    </li>
    </ul>
    </li>
    <li><strong>Output</strong>: The result has to get printed to standard output.</li>
    <li>The result has to be formatted like the input (tabs for separation of number, \n for marks a new line)</li>
</ul>

<h2>The Tests</h2>
I will check the speed of a multiplication of two big matrices following for Python, Java and C++ for all algorithms like this:

{% highlight bash %}time python scriptABC.py -i ../2000.in > result.txt
diff result.txt bigMatrix.out{% endhighlight %}

The <code>bigMatrix.out</code> was produced by the Python ijk-implementation. I make the diff to test if the result is correct.

<h2>The Setting</h2>
I created two "random" matrices $A, B \in \mathbb{N}^{2000 \times 2000}$ with this script. The file that was created needs about 29.7 MB and is also in the GIT-Hub repository. But you can also create the matrices with this script:
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
random.seed(1234)

def createRandomMatrix(n):
	maxVal = 1000 # I don't want to get Java / C++ into trouble
	matrix = []
	for i in xrange(n):
		matrix.append([random.randint(0,maxVal) for el in xrange(n)])
	return matrix

def saveMatrix(matrixA, matrixB, filename):
	f = open(filename, 'w')
	for i, matrix in enumerate([matrixA, matrixB]):
		if i != 0:
			f.write("\n")
		for line in matrix:
			f.write("\t".join(map(str, line)) + "\n")
n = 3
matrixA = createRandomMatrix(n)
matrixB = createRandomMatrix(n)
saveMatrix(matrixA, matrixB, "2000.in"){% endhighlight %}

All scripts are tested on my computer:
<table>
<tr>
<td colspan="2" style="background-color:#cdcdcd">Acer TravelMate 5735Z</td>
</tr>
<tr>
<td style="background-color:#efefef">CPU</td>
<td>2x Pentium(R) Dual-Core CPU T4500 @2.30GHz</td>
</tr>
<tr>
<td style="background-color:#efefef">RAM</td>
<td>4 GB</td>
</tr>
<tr>
<td style="background-color:#efefef">Video Card</td>
<td>Intel GMA 4500MHD</td>
</tr>
<tr>
<td style="background-color:#efefef">System</td>
<td>Ubuntu 10.10.04 LTS</td>
</tr>
</table>

<h2>Python</h2>
I've used Python 2.6.5.

<h3>ijk-algorithm</h3>
{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", dest="filename", default="2000.in",
     help="input file with two matrices", metavar="FILE")
(options, args) = parser.parse_args()

def read(filename):
	lines = open(filename, 'r').read().splitlines()
	A = []
	B = []
	matrix = A
	for line in lines:
		if line != "":
			matrix.append(map(int, line.split("\t")))
		else:
			matrix = B
	return A, B

def printMatrix(matrix):
	for line in matrix:
		print "\t".join(map(str,line))

def standardMatrixProduct(A, B):
	n = len(A)
	C = [[0 for i in xrange(n)] for j in xrange(n)]
	for i in xrange(n):
		for j in xrange(n):
			for k in xrange(n):
				C[i][j] += A[i][k] * B[k][j]
	return C

A, B = read(options.filename)
C = standardMatrixProduct(A, B)
printMatrix(C){% endhighlight %}

{% highlight bash %}real	56m49.266s
user	56m30.524s
sys	0m2.980s{% endhighlight %}

<h3>ikj-algorithm</h3>
{% highlight python %}def ikjMatrixProduct(A, B):
	n = len(A)
	C = [[0 for i in xrange(n)] for j in xrange(n)]
	for i in xrange(n):
		for k in xrange(n):
			for j in xrange(n):
				C[i][j] += A[i][k] * B[k][j]
	return C{% endhighlight %}

{% highlight bash %}real	44m36.507s
user	44m13.458s
sys	0m2.000s{% endhighlight %}

<h3>Psyco ikj-algorithm</h3>
<a href="http://en.wikipedia.org/wiki/Psyco">Psyco</a> is a just in time compiler, which makes my scripts MUCH faster. It is very simple to use. Add these two lines at the top of the ikj-script:
{% highlight python %}import psyco
psyco.full(){% endhighlight %}

{% highlight bash %}real	6m14.820s
user	6m12.959s
sys	0m0.620s{% endhighlight %}

Amazing, isn't it?

<h3>Libraries</h3>
<h4>NumPy</h4>
NumPy-Version: 1.3.0 (Current version is 1.6.2, see <a href="http://en.wikipedia.org/wiki/NumPy">Wiki</a>)

{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", dest="filename", default="2000.in",
     help="input file with two matrices", metavar="FILE")
(options, args) = parser.parse_args()

def read(filename):
	lines = open(filename, 'r').read().splitlines()
	A = []
	B = []
	matrix = A
	for line in lines:
		if line != "":
			matrix.append(map(int, line.split("\t")))
		else:
			matrix = B
	return A, B

def printMatrix(matrix):
	matrix = numpy.array(matrix)
	for line in matrix:
		print "\t".join(map(str,line))

A, B = read(options.filename)
A = numpy.matrix(A)
B = numpy.matrix(B)
C = A * B # easy and intuitive, isn't it?
printMatrix(C){% endhighlight %}

{% highlight bash %}real	1m38.425s
user	1m36.066s
sys	0m0.520s{% endhighlight %}

<h4>SciPy</h4>
You might need to install <code>python-scitools</code>.

{% highlight python %}#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import scipy

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", dest="filename", default="2000.in",
     help="input file with two matrices", metavar="FILE")
(options, args) = parser.parse_args()

def read(filename):
	lines = open(filename, 'r').read().splitlines()
	A = []
	B = []
	matrix = A
	for line in lines:
		if line != "":
			matrix.append(map(int, line.split("\t")))
		else:
			matrix = B
	return A, B

def printMatrix(matrix):
	matrix = numpy.array(matrix)
	for line in matrix:
		print "\t".join(map(str,line))

A, B = read(options.filename)
A = scipy.matrix(A)
B = scipy.matrix(B)
C = A * B # easy and intuitive, isn't it?
printMatrix(C){% endhighlight %}

{% highlight bash %}real	1m35.795s
user	1m33.438s
sys	0m0.488s{% endhighlight %}

<h3>Conclusion for Python</h3>
[caption id="attachment_28301" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/06/python-execution-times.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/06/python-execution-times.png" alt="Python execution times for matrix multiplication" title="Python execution times for matrix multiplication" width="512" height="315" class="size-full wp-image-28301" /></a> Python execution times for matrix multiplication[/caption]
Using NumPy is by far the easiest and fastest option. I've needed about five minutes for each of the non-library scripts and about 10 minutes for the NumPy/SciPy scripts.

By the way, it is useless to combine Psyco and NumPy. It gets a little bit faster (1 minute and 28 seconds), but this could also be a random effect. If you execute it many times, you will see that the execution time is never the same.

<h2>Java</h2>
I am using this Java version:
{% highlight bash %}$ java -version
java version "1.6.0_20"
OpenJDK Runtime Environment (IcedTea6 1.9.13) (6b20-1.9.13-0ubuntu1~10.04.1)
OpenJDK Server VM (build 19.0-b09, mixed mode){% endhighlight %}
<h3>ijk-algorithm</h3>
{% highlight java %}import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

public class Shell {
    static List<ArrayList<ArrayList<Integer>>> read(String filename) {
        ArrayList<ArrayList<Integer>> A = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> B = new ArrayList<ArrayList<Integer>>();

        String thisLine;

        try {
            BufferedReader br = new BufferedReader(
                    new FileReader(filename));

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

    static int[][] ijkAlgorithm(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
        int n = A.size();

        // initialise C
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A.get(i).get(k) * B.get(k).get(j);
                }
            }
        }
        return C;
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

    public static void main(String[] args) {
		String filename;
		if (args.length < 2) {
			filename = "2000.in";
		} else {
			filename = args[1];
		}
        List<ArrayList<ArrayList<Integer>>> matrices = read(filename);
        ArrayList<ArrayList<Integer>> A = matrices.get(0);
        ArrayList<ArrayList<Integer>> B = matrices.get(1);
        int[][] C = ijkAlgorithm(A, B);
        printMatrix(C);
    }

}{% endhighlight %}

{% highlight bash %}real	27m21.295s
user	26m53.877s
sys	0m4.368s{% endhighlight %}

Note: Java is not C++! If you use <a href="http://docs.oracle.com/javase/6/docs/api/java/util/Vector.html">Vector</a> instead of <a href="http://docs.oracle.com/javase/6/docs/api/java/util/ArrayList.html">ArrayList</a>, you get these results:
{% highlight bash %}real	82m26.754s
user	80m42.003s
sys	0m24.598s{% endhighlight %}
One reason might be that Vector is synchronized.

<h3>ikj-algoirthm</h3>
I've only switched line 60 and line 61.
{% highlight bash %}real	2m9.478s
user	1m26.369s
sys	0m39.162s{% endhighlight %}

<h3>Library: JAMA</h3>
I've searched in Google for "java matrix multiplication". The first 10 results were only implementations of the ijk-algorithm. Although the ijk-algorithm is very easy, most of the results were only questions where people tried to implement it.

After some search (20 minutes minimum) I've found <a href="http://math.nist.gov/javanumerics/jama/">JAMA</a>. They also have a <a href="http://math.nist.gov/javanumerics/jama/doc/">documentation</a>. You might need to install this for the following code:
{% highlight bash %}sudo apt-get install libjama-*{% endhighlight %}

{% highlight java %}import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import Jama.Matrix;

public class Shell {
    static List<ArrayList<ArrayList<Double>>> read(String filename) {
        ArrayList<ArrayList<Double>> A = new ArrayList<ArrayList<Double>>();
        ArrayList<ArrayList<Double>> B = new ArrayList<ArrayList<Double>>();

        String thisLine;

        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));

            // Begin reading A
            while ((thisLine = br.readLine()) != null) {
                if (thisLine.trim().equals("")) {
                    break;
                } else {
                    ArrayList<Double> line = new ArrayList<Double>();
                    String[] lineArray = thisLine.split("\t");
                    for (String number : lineArray) {
                        line.add((double) Integer.parseInt(number));
                    }
                    A.add(line);
                }
            }

            // Begin reading B
            while ((thisLine = br.readLine()) != null) {
                ArrayList<Double> line = new ArrayList<Double>();
                String[] lineArray = thisLine.split("\t");
                for (String number : lineArray) {
                    line.add((double) Integer.parseInt(number));
                }
                B.add(line);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e);
        }

        List<ArrayList<ArrayList<Double>>> res = new LinkedList<ArrayList<ArrayList<Double>>>();
        res.add(A);
        res.add(B);
        return res;
    }

    static int[][] ijkAlgorithm(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
        int n = A.size();

        // initialise C
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A.get(i).get(k) * B.get(k).get(j);
                }
            }
        }
        return C;
    }

    static void printMatrix(Matrix matrix, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j != 0) {
                    System.out.print("\t");
                }
                System.out.printf("%.0f", matrix.get(i, j));
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        String filename;
        if (args.length < 2) {
            filename = "2000.in";
        } else {
            filename = args[1];
        }
        List<ArrayList<ArrayList<Double>>> matrices = read(filename);
        ArrayList<ArrayList<Double>> A = matrices.get(0);
        ArrayList<ArrayList<Double>> B = matrices.get(1);
        int n = A.size();
        double[][] Aarray = new double[n][n];
        double[][] Barray = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Aarray[i][j] = A.get(i).get(j);
                Barray[i][j] = B.get(i).get(j);
            }
        }
        Matrix AM = new Matrix(Aarray);
        Matrix BM = new Matrix(Aarray);
        Matrix CM = AM.times(BM);

        printMatrix(CM, n);
    }

}{% endhighlight %}

{% highlight bash %}real	1m36.506s
user	0m51.367s
sys	0m45.043s{% endhighlight %}

It took me about two hours to get it work. I had to add the JAMA-JAR to eclipse, export my project as a JAR and run it with
{% highlight bash %}time java -jar jama-shell.jar -i ../2000.in > jama-result.out{% endhighlight %}

I still have no idea how to compile it with bash only.

<h3>Conclusion for Java</h3>

[caption id="attachment_28331" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/06/java-execution-time.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/06/java-execution-time.png" alt="Java execution times for matrix multiplication" title="Java execution times for matrix multiplication" width="512" height="287" class="size-full wp-image-28331" /></a> Java execution times for matrix multiplication[/caption]

You should definitely know if some Java-datastructures are synchronised or not. And you should know how the computer / caches work.

<h2>C++</h2>
I have gcc 4.4.3 and compiled everything with these options:
{% highlight bash %}g++ -std=c++98 -Wall -O3 -g myScript.cpp -o $(PROBLEM).out -pedantic{% endhighlight %}

<h3>ijk-algorithm</h3>
{% highlight cpp %}#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

struct Result {
	vector< vector<int> > A;
	vector< vector<int> > B;
};

Result read(string filename) {
	vector< vector<int> > A, B;
	Result ab;
	string line;
	ifstream infile;
	infile.open (filename.c_str());

	int i = 0;
	while (getline(infile, line) &amp;&amp; !line.empty()) {
		istringstream iss(line);
		A.resize(A.size() + 1);
		int a, j = 0;
		while (iss >> a) {
			A[i].push_back(a);
			j++;
		}
		i++;
	}

	i = 0;
	while (getline(infile, line)) {
		istringstream iss(line);
		B.resize(B.size() + 1);
		int a;
		int j = 0;
		while (iss >> a) {
			B[i].push_back(a);
			j++;
		}
		i++;
	}

	infile.close();
	ab.A = A;
	ab.B = B;
	return ab;
}

vector< vector<int> > ijkalgorithm(vector< vector<int> > A, 
									vector< vector<int> > B) {
	int n = A.size();

	// initialise C with 0s
	vector<int> tmp(n, 0);
	vector< vector<int> > C(n, tmp);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}
	return C;
}

void printMatrix(vector< vector<int> > matrix) {
	vector< vector<int> >::iterator it;
	vector<int>::iterator inner;
	for (it=matrix.begin(); it != matrix.end(); it++) {
		for (inner = it->begin(); inner != it->end(); inner++) {
			cout << *inner;
			if(inner+1 != it->end()) {
				cout << "\t";
			}
		}
		cout << endl;
	}
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "2000.in";
	} else {
		filename = argv[2];
	}
	Result result = read (filename);
	vector< vector<int> > C = ijkalgorithm(result.A, result.B);
	printMatrix(C);
	return 0;
}{% endhighlight %}
{% highlight bash %}real	1m40.439s
user	1m38.642s
sys	0m0.280s{% endhighlight %}

<h3>ikj-algorithm</h3>
Again, I've only switched line 61 and 62.

{% highlight bash %}real	0m15.172s
user	0m14.877s
sys	0m0.248s{% endhighlight %}

<h3>Library: Boost</h3>
If you want to compile these scripts, you might have to install the boost libraries first. On Ubuntu you can enter:
{% highlight bash %}sudo apt-get install libboost-math*{% endhighlight %}

{% highlight cpp %}#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;

struct Result {
	boost::numeric::ublas::matrix<int> A;
	boost::numeric::ublas::matrix<int> B;
};

int getMatrixSize(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

void printMatrix(boost::numeric::ublas::matrix<int> matrix) {
	for (unsigned int i=0; i < matrix.size1(); i++) {
		for (unsigned int j=0; j < matrix.size2(); j++) {
			cout << matrix(i, j);
			if(j+1 != matrix.size2()) {
				cout << "\t";
			}	
		}
		cout << endl;
	}
}

Result read(string filename) {
	Result ab;
	string line;
	ifstream infile;
	infile.open (filename.c_str());

	// get dimension
	getline(infile, line);
	int n = getMatrixSize(filename);

	boost::numeric::ublas::matrix<int> A(n,n), B(n,n);

	// process first line
	istringstream iss(line);
	int a, i = 0, j = 0;
	while (iss >> a) {
		A(i,j) = a;
		j++;
	}
	i++;

	while (getline(infile, line) &amp;&amp; !line.empty()) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			A(i,j) = a;
			j++;
		}
		i++;
	}

	i = 0;
	while (getline(infile, line)) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			B(i,j) = a;
			j++;
		}
		i++;
	}

	infile.close();
	ab.A = A;
	ab.B = B;
	return ab;
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "2000.in";
	} else {
		filename = argv[2];
	}
	Result result = read (filename);

	boost::numeric::ublas::matrix<int> C;
	C = boost::numeric::ublas::prod(result.A, result.B);
	printMatrix(C);

	return 0;
}{% endhighlight %}

{% highlight bash %}real	4m15.388s
user	4m10.272s
sys	0m0.588s{% endhighlight %}

<h3>Library: Blitz</h3>
This is a great example of useless library. I've installed the library:
{% highlight bash %}sudo apt-get install libblitz*{% endhighlight %}
Then I wanted to use it. Well, I have no clue how I could exactly use it! See my StackOverflow Question: <a href="http://stackoverflow.com/questions/11113993/is-a-documentation-of-blitz-matrices-available">Is a documentation of Blitz++ matrices available?</a>

<h3>Conclusion for C++</h3>
[caption id="attachment_28351" align="aligncenter" width="512"]<a href="http://martin-thoma.com/wp-content/uploads/2012/06/cpp-execution-time.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/06/cpp-execution-time.png" alt="C++ execution times for matrix multiplication" title="C++ execution times for matrix multiplication" width="512" height="249" class="size-full wp-image-28351" /></a> C++ execution times for matrix multiplication[/caption]

Again, it brings a performance boost if you know how your CPU works. I was very astonished, that the library Boost is slower (actually MUCH slower) than my simplest approach was.

<h2>Conclusion</h2>
If I want to create a working piece of code in a minimum amount of time, I will always take Python. It has been very easy to solve this task with the given restrictions. But C++ is amazing when speed is important.

It was astonishingly difficult to find working code examples for this task for Java and C++. I was searching for libraries and found some, but the search results were not satisfying.

<h2>See also</h2>
<ul>
  <li><a href="http://www.boost.org/doc/libs/1_49_0/libs/numeric/ublas/doc/matrix.htm">Boost Matrix multiplication</a></li>
  <li><a href="http://rosettacode.org/wiki/Matrix_multiplication">Rosetta Code: Matrix multiplication</a> (Implementations in 63 programming languages!)</li>
  <li><a href="http://stackoverflow.com/questions/10442365/why-is-matrix-multiplication-faster-with-numpy-than-with-ctypes-in-python">Why is matrix multiplication faster with numpy than with ctypes in Python?</a></li>
  <li><a href="http://stackoverflow.com/questions/11110604/why-is-boosts-matrix-multiplication-slower-than-mine">Why is boosts matrix multiplication slower than mine?</a></li>
</ul>

<div class="info">Continue reading with Part II: <a href="http://martin-thoma.com/strassen-algorithm-in-python-java-cpp/">The Strassen algorithm in Python, Java and C++</a></div>
