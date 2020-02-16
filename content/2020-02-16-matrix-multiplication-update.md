---
layout: post
title: Matrix Multiplication: 2020 Update
slug: matrix-multiplication-2020
author: Martin Thoma
date: 2020-02-16 20:00
category: Code
tags: Python, C++, pypy
featured_image: logos/python.png
---
In 2012 I wrote a series of articles about matrix
multiplication. Now I'm preparing a course about speeding up Python. For this
reason I need an example of code that is fairly simple to understand and can be
optimized. So let's update the results of my old articles :-)

The code can be found in a git repository on GitHub ([github.com/MartinThoma/matrix-multiplication](https://github.com/MartinThoma/matrix-multiplication)) and you can have a look at the [old article](https://martin-thoma.com/matrix-multiplication-python-java-cpp/) as well, if you want.

All scripts are tested on my new Thinkpad T460p. For comparision, I've also
added the laptop I had before when I wrote the 2012 matrix multiplication article:

<table class="table">
    <thead>
        <tr style="background-color:#cdcdcd">
            <th>&nbsp;</th>
            <th>Acer TravelMate 5735Z</th>
            <th>Thinkpad T460p</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="background-color:#efefef">CPU (<a href="https://ark.intel.com/content/www/de/de/ark/compare.html?productIds=42925,88967">comparison on ark.inten.com</a>)</td>
            <td>2x Pentium(R) Dual-Core CPU T4500 @2.30GHz</td>
            <td>8x Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">RAM</td>
            <td>4 GB</td>
            <td>8 GB</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">Video Card</td>
            <td>Intel GMA 4500MHD</td>
            <td>Nvidia GeForce 940MX</td>
        </tr>
        <tr>
            <td style="background-color:#efefef">System</td>
            <td>Ubuntu 10.10.04 LTS</td>
            <td>Ubuntu 18.04.3 LTS</td>
        </tr>
    </tbody>
</table>


## Python

In the following table you can see the execution times for the different
algorithms and different Python versions. As input, I took the
<code>2000.in</code> test set. To switch Python versions, I used <code>pyenv</code>

For Python 2.7, you can see the speedup compared to my 2012 machine. A speedup
of 2.6x means that you could run the code on the new machine 2.6x in the time
the old machine needed.

<table class="table">
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Python 2.7.16</th>
            <th>Python 3.8.1</th>
            <th>pypy3.6-7.3.0</th>
            <th>pypy-c-jit-latest</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>ijk</th>
            <td>1253 (<span style="color: green;">2.6x</span>)</td>
            <td>1884</td>
            <td>158</td>
            <td>147</td>
        </tr>
        <tr>
            <th>ikj</th>
            <td>901s (<span style="color: green;">2.9x</span>)</td>
            <td>1735</td>
            <td>52</td>
            <td>50</td>
        </tr>
        <tr>
            <th><a href="https://en.wikipedia.org/wiki/NumPy">NumPy</a></th>
            <td>20 (<span style="color: green;">~6x</span>)<br/>version: 1.14.4</td>
            <td>20<br/>version: 1.18.1</td>
            <td>42</td>
            <td>36</td>
        </tr>
        <tr>
            <th><a href="https://en.wikipedia.org/wiki/SciPy">SciPy</a></th>
            <td>45 (<span style="color: green;">2.6x</span>)<br/>version: 1.1.0</td>
            <td>20<br/>version: 1.4.1</td>
            <td colspan="2"><a href="https://stackoverflow.com/q/60248443/562769">Installation problems</a></td>
        </tr>
        <tr>
            <th><a href="https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/">Strassen (LEAF_SIZE=8)</a></th>
            <td>1709 (<span style="color: green;">1.7x</span>)</td>
            <td>1780</td>
            <td>190</td>
            <td>125</td>
        </tr>
        <tr>
            <th><a href="https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/">Strassen (LEAF_SIZE=64)</a></th>
            <td>855 (<span style="color: green;">3.4x</span>)</td>
            <td>1022</td>
            <td>44</td>
            <td>41</td>
        </tr>
        <tr>
            <th>ikj (2 threads)</th>
            <td>953</td>
            <td>1611</td>
            <td>37</td>
            <td>32</td>
        </tr>
        <tr>
            <th>ikj (4 threads)</th>
            <td>459</td>
            <td>762</td>
            <td>19</td>
            <td>17</td>
        </tr>
    </tbody>
</table>

Things to note:

* pypy is crazy fast compared to CPython - up to a speedup of 34x 😲 So JIT is
  worth a try. I actually wanted to try
  [Pyston](https://github.com/dropbox/pyston)
  ([comparison](https://pybenchmarks.org/u64q/benchmark.php?test=all&lang=pypy&lang2=pyston&data=u64q))
  as well, but the built failed with pyenv.
* Python 2.7 is faster than 3.8 for this benchmark 😢
* Ways to improve; speedups are always compared to the naive ijk algorithm:
    * Cache optimization: The ikj algorithm gave a 1.08x speedup
    * Algorithmic: The Strassen algorithm gave a 1.84x speedup
    * Parallelization: Using 4 threads instead of 1 with a super simple algorithm gave a 2.47x speedup
    * Time:
        * New Hardware which is 8 years newer gave a 2.6x speedup on the naive
          solution
        * Running the old code with updated libraries on my new machine gave a
          6x speedup compared to running the older version of numpy on the old
          machine.
    * Libraries: Using numpy gave a **94.2x speedup**!
* Numpy and scipy are the way to go, just as expected 🤷‍♂️

You might also be interested in [pybenchmarks.org](https://pybenchmarks.org/)
which seems to be similar to [The Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html).

### pypy

Quoting from the [PyPy 1.2 Release notes](https://opensource.googleblog.com/2010/04/pypy-12-released.html):

> PyPy is a reimplementation of Python in Python [...]. [PyPy] speed results
> often beat CPython, ranging from being slightly slower, to speedups of up to
> 2x on real application code, to speedups of up to 10x on small benchmarks.

Another resource which states that PyPy is faster than CPython is [pybenchmarks.org](https://pybenchmarks.org/u64q/pypy.php) (also [PyPy 3](https://pybenchmarks.org/u64q/pypy3.php)).

PyPy uses [Just-in-time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation) (JIT)
to get those speedups.

Go to [PyPy — How can it possibly beat CPython?](https://stackoverflow.com/q/2591879/562769)
for more information why PyPy is that fast.


## C++

<table class="table">
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>g++-O0 -D _DEBUG -g</th>
            <th>-O3 -D NDEBUG -DBOOST_UBLAS_NDEBUG</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>ijk</th>
            <td>168.06</td>
            <td>45.05</td>
        </tr>
        <tr>
            <th>ikj</th>
            <td>89.67</td>
            <td>5.24</td>
        </tr>
        <tr>
            <th>library-boost</th>
            <td>1002.36</td>
            <td>4.56</td>
        </tr>
    </tbody>
</table>

Things to note:

* Debug flags / Optimization settings while compiling make a huge difference
* It's way faster than Python


## Using C++ from Python

Obviously, C++ is way faster than pure Python. Astonishingly, C++ is also
faster than Numpy for this simple number crunching task. So the idea is to
combine both: Have the nice interface of Python with the raw computing power
of C++.

However, there are many ways to combine the two:

* [subprocess](https://docs.python.org/3/library/subprocess.html) 🙄
* ctypes: [beginner tutorial](https://stackoverflow.com/a/5082294/562769)
* [cffi](https://cffi.readthedocs.io/en/release-0.6/)
* cython
* c extensions: [examples](https://github.com/jiffyclub/cext23)
* [pybind11](https://pybind11.readthedocs.io/en/stable/)
* [Py++](https://pyplusplus.readthedocs.io/en/latest/)

[Cython versus CFFI](https://eev.ee/blog/2013/09/13/cython-versus-cffi/)
helped me to wrap my head around this topic a bit.


## See also

* [Matti Picus](https://bids.berkeley.edu/resources/videos/cffi-ctypes-cython-good-bad-and-ugly): [CFFI, Ctypes, Cython: the Good, the Bad and the Ugly](https://www.youtube.com/watch?v=EABNkHRtMLo) at EuroSciPy, 2018. (first presented at <a href="https://pyvideo.org/pycon-israel-2017/cffi-ctypes-cython-the-good-the-bad-and-the-ugly.html">PyCon Israel 2017</a>)
    * 2:10 Begins
    * 4:05 Matti Picus introduces himself
    * 5:02 He will use Mandelbrot as an example
    * 15:00 C implementation
    * 18:00 C done: 130ms (Python 3057ms)
    * 18:15 ctypes is writing python in c
        * Take a shared object (*.so) or ddl
        * 20:48 ctypes.Structure
        * 24:00 Memory managment / free-ing memory
        * 36:00 Create *.so
        * 38:40 Load dll / *.so
        * 44:24 Timing - 1554ms
    * 45:10 cffi - cffi came out as a replacement for ctypes. cffi is writing c in python. Use c as directly as possible.
        * 46:20 Load C header in Python; header needs to be in very specific format. IT CAN'T HANDLE MACROS!
        * 50:20 cffi memory management
        * 52:37 Call function
        * 53:33 Timing - 640ms
        * 53:50 Q/A
    * 55:36 Cython - can be used from jupyter notebook
        * Cython has a own language; like a mix between C and Python
        * 56:58 Cython creates a shared object
        * 1:00:07 cpdef - a mixture between c and python
        * 1:02:12 Timing - 594ms
    * 1:02:49 [cppyy](https://cppyy.readthedocs.io/en/latest/) - C++!
        * 1:03:30 LLVM
    * 1:09 Final thoughts
* Armin Rigo: [CFFI: calling C from Python](https://www.youtube.com/watch?v=ejUzVcvTLgI) at EuroPython, 2016.
* [Comparing Python, Numpy, Numba and C++ for matrix multiplication](https://stackoverflow.com/q/36526708/562769)
* [Nuitka](https://en.wikipedia.org/wiki/Nuitka) (<a href="https://pybenchmarks.org/u64q/nuitka.php">Benchmark</a>)
