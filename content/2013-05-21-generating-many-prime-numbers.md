---
layout: post
lang: en
title: Generating many prime numbers
slug: generating-many-prime-numbers
author: Martin Thoma
date: 2013-05-21 22:50:10.000000000 +02:00
category: Cyberculture
tags: mathematics, Project Euler, CPP, prime number
featured_image: 2012/04/leonhard-euler.jpg
---
Today, a fellow student claimed that it would take much time to check the first 1,000,000 numbers for primes. I claimed that it would be a matter of seconds to do so for the first 1,000,000,000 numbers.

So, lets prove my claim.

<h2>Trivial approach</h2>
```cpp

#include <iostream> // cin, cout
#include <cmath> // sqrt
#include <vector>

using namespace std;
vector<unsigned long> primeList;

bool isPrime(unsigned long n) {
    vector<unsigned long>::iterator myIt;
    unsigned long root = (unsigned long) sqrt(n);
    for(myIt=primeList.begin(); myIt != primeList.end(); myIt++){
        if(n%(*myIt) == 0) {
            return false;
        } else if ((*myIt) > root) {
            return true;
        }
    }
    return true;
}

int main(int argc, char* argv[]) {
    primeList.push_back(2);
    cout << 2 << endl;

    unsigned long long max = (unsigned long long) atoi(argv[1]);
    for (unsigned long i=3; i<max; i+=2) {
        if(isPrime(i)) {
            primeList.push_back(i);
            cout << i << endl;
        }
    }

    return 0;
}

```

Execute it for 100,000,000:

```bash
time ./generate-prime-list.out 100000000 > primes.txt

real	0m57.274s
user	0m41.855s
sys	0m15.229s

```

So 41 seconds for all primes not bigger than 100,000,000.

Now, lets test it for 1,000,000,000:
```bash
time ./generate-prime-list.out 1000000000 > primes.txt

real	18m18.205s
user	15m56.904s
sys	2m12.500s

```

16 minutes ... not exactly "seconds". But please keep in mind that I also wrote the result to a txt-file. This txt file is 502.0 MB big. It takes quite a lot of time to write such an amount of data from memory to disk.

<h2>Sieve of Eratosthenes</h2>
<h3>A first try</h3>
```cpp

#include <iostream> // cin, cout
#include <vector>

using namespace std;

void sieveOfEratosthenes(unsigned long n) {
    vector<bool> primesEratosthenes (n+1, true);
    cout << 2 << endl;
    for (unsigned long i=3; i<n; i+=2) {
        if (primesEratosthenes[i] == true) {
            cout << i << endl;
            for (unsigned long j=2; j*i<=n; j++) {
                primesEratosthenes[j*i] = false;
            }
        }
    }
}

int main(int argc, char* argv[]) {
    unsigned long long n = (unsigned long long) atoi(argv[1]);
    sieveOfEratosthenes(n);
    return 0;
}

```

This one takes 1 minute 5 seconds:
```bash

make;time ./generate-prime-list.out 1000000000 > testPrimes.txt
g++ -std=c++0x -Wall -pedantic -O3 -D NDEBUG generate-prime-list.cpp -o generate-prime-list.out

real	3m20.436s
user	1m4.908s
sys	2m11.748s

```

I'm getting closer to "seconds". ☺

<h3>ofstream, endl, \n and buffers</h3>
Writing 502.0 MB takes some time. It's not getting better when I pipe this through bash. So lets write it directly:

```cpp
#include <fstream> // ofstream
#include <vector>

using namespace std;

void sieveOfEratosthenes(unsigned long n) {
    ofstream myfile;
    myfile.open ("huge-prime-list.txt");
    vector<bool> primesEratosthenes (n+1, true);
    myfile << 2 << endl;
    for (unsigned long i=3; i<n; i+=2) {
        if (primesEratosthenes[i] == true) {
            myfile << i << endl;
            for (unsigned long j=2; j*i<=n; j++) {
                primesEratosthenes[j*i] = false;
            }
        }
    }
    myfile.close();
}

int main(int argc, char* argv[]) {
    unsigned long long n = (unsigned long long) atoi(argv[1]);
    sieveOfEratosthenes(n);
    return 0;
}
```

```bash
time ./generate-prime-list.out 1000000000

real	3m21.249s
user	1m4.016s
sys	2m12.332s

```

Ok, no real change :-/

Another idea is to replace <code>endl</code> by <code>\n</code> (see <a href="http://stackoverflow.com/a/5192299/562769">explanation</a>)

That was a good try. Now it needs only 46 seconds:

```bash
time ./generate-prime-list.out 1000000000

real	0m49.539s
user	0m46.619s
sys	0m0.920s

```

Another reason why this might be slow could be too many system calls. So I could buffer some and write them in blocks. I could also just write blocks of unsigned long numbers instead of a string representation. This might lead to a much smaller file size which in consequence is faster to write:

```cpp

#include <stdio.h> // fopen
#include <iostream> // atoi
#include <vector>

using namespace std;

void sieveOfEratosthenes(unsigned long n) {
    FILE* pFile;
    pFile = fopen("huge-prime-list.txt", "wb");
    vector<bool> primesEratosthenes (n+1, true);

    unsigned long tmp = 2;
    fwrite(&tmp, sizeof(unsigned long),1, pFile);
    for (unsigned long i=3; i<n; i+=2) {
        if (primesEratosthenes[i] == true) {
            fwrite(&i, sizeof(unsigned long),1, pFile);

            for (unsigned long j=2; j*i<=n; j++) {
                primesEratosthenes[j*i] = false;
            }
        }
    }

    fclose(pFile);
}

int main(int argc, char* argv[]) {
    unsigned long long n = (unsigned long long) atoi(argv[1]);
    sieveOfEratosthenes(n);
    return 0;
}

```

And execute it:
```bash

time ./generate-prime-list.out 1000000000

real	0m39.700s
user	0m38.546s
sys	0m0.640s

```

38 seconds for all primes from 2 to 1,000,000,000. The file size is now only 203.4 MB.

By the way, simply setting this with <code>setbuf(pFile, NULL);</code> to unbuffered resulted in 50 seconds execution time.

You can get the list with this snippet:

```cpp

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "You have to specify a file name" << endl;
    } else {
        FILE* pFile;
        pFile = fopen(argv[1], "rb");

        long long x;
        size_t read;
        while (!feof(pFile)) {
            read = fread(&x, sizeof(long long), 1, pFile);
            (void) read;
            if (feof(pFile)){
                break; // otherwise it duplicates the last entry
            }
            cout << x << endl;
        }
        fclose(pFile);
    }
}

```

<h3>Improve sieving</h3>
The following change was suggested by <em>Niklas B.</em>. Thanks!

Take a look at the inner for loop. This one does the sieving, so it gets executed very often. In this loop, you have to calculate <code>j*i</code> for checking the condition of the loop and again for setting it to false. You can get rid of one of those operations. Additionally, you don't have to start sieving at <code>2*p</code>, but you can start at <code>p*p</code> as you already sieved out all multiples of the first, second, ..., current-1-th prime.

```cpp

#include <stdio.h> // fopen
#include <iostream> // atoi
#include <vector>

using namespace std;

void sieveOfEratosthenes(long long n) {
    FILE* pFile;
    pFile = fopen("huge-prime-list.bin", "wb");
    vector<bool> primesEratosthenes (n+1, true);

    long long tmp = 2;
    fwrite(&tmp, sizeof(long long),1, pFile);
    for (long long i=3; i<n; i+=2) {
        if (primesEratosthenes[i]) {
            fwrite(&i, sizeof(long long), 1, pFile);

            for (long long j=i*i; j<=n; j+=i) {
                primesEratosthenes[j] = false;
            }
        }
    }

    fclose(pFile);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "You have to specify n" << endl;
    } else {
        long long  n = (long long) atoi(argv[1]);
        sieveOfEratosthenes(n);
    }
    return 0;
}

```

Execute:
```bash

time ./generate-prime-list.out 1000000000

real	0m24.222s
user	0m23.485s
sys	0m0.436s

```

<h3>primesieve</h3>
<a href="https://code.google.com/p/primesieve/">Primesieve</a> is a free software program and C++ library that generates prime numbers and prime k-tuplets (twin primes, prime triplets, ...) $< 2^{64}$ using a highly optimized implementation of the sieve of Eratosthenes.

According to the GUI, it finds all 50,847,534 primes below 1,000,000,000 in 0.16 seconds. But write them to a file...

<h2>Sieve of Atkin</h2>
Arthur Oliver Lonsdale Atkin (July 31, 1925 &ndash; December 28, 2008) was a British mathematician who invented this sieve. I've implemented it according to the <a href="http://en.wikipedia.org/wiki/Sieve_of_Atkin#Pseudocode">pseudocode provided in Wikipedia</a>. A <a href="http://stackoverflow.com/a/12066272/562769">very long explanation of Atkins sieve</a> is on StackOverflow

<h3>My first implementation</h3>
```cpp

#include <stdio.h> // fopen
#include <iostream> // atoi
#include <vector>
#include <cmath> // sqrt, ceil,

using namespace std;

void sieveOfAtkin(long long limit) {
    FILE* pFile;
    pFile = fopen("huge-prime-list.bin", "wb");

	long long root = ceil(sqrt(limit));

    // initialize the sieve
	vector<bool> is_prime(limit, false);

    // put in candidate primes:
    // integers which have an odd number of
    // representations by certain quadratic forms
	for (long long x = 1; x <= root; x++) {
        long long xSquare = x*x;
		for (long long y = 1; y <= root; y++) {
			long long n = (4*xSquare)+(y*y);
			if (n <= limit && (n % 12 == 1 || n % 12 == 5)) {
                is_prime[n] = !is_prime[n];
            }

			n = (3*xSquare)+(y*y);
			if (n <= limit && n % 12 == 7) {
                is_prime[n] = !is_prime[n];
            }

			n = (3*xSquare)-(y*y);
			if (x > y && n <= limit && n % 12 == 11) {
                is_prime[n] = !is_prime[n];
            }
		}
	}

    // eliminate composites by sieving
	for (long long n = 5; n <= root; n++) {
        if (is_prime[n]) {
            long long add = n*n;
            for (long long k = add; k < limit; k += add) {
                // n is prime, omit multiples of its square; this is
                // sufficient because composites which managed to get
                // on the list cannot be square-free
                is_prime[k] = false;
            }
        }
    }

    // Output primes
    long long primTmp = 2;
    fwrite(&primTmp, sizeof(long long), 1, pFile);
    primTmp = 3;
    fwrite(&primTmp, sizeof(long long), 1, pFile);

	for (long long n = 5; n < limit; n++) {
		if (is_prime[n]) {
            fwrite(&n, sizeof(long long), 1, pFile);
		}
	}

    fclose(pFile);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "You have to specify n" << endl;
    } else {
        long long  n = (long long) atoi(argv[1]);
        sieveOfAtkin(n);
    }
    return 0;
}

```

Atkins sieve has a much worse performance than Sieve of Eratosthenes:

```bash

time ./generate-prime-list.out 1000000000

real	1m6.001s
user	1m4.724s
sys	0m0.604s

```

<h3>Primegen</h3>
<a href="http://cr.yp.to/primegen.html">Primegen</a> is an implementation by <a href="http://en.wikipedia.org/wiki/Daniel_J._Bernstein">Daniel J. Bernstein</a>. It's a little bit cluttered with 80 files and 3854 LOC in total.

When I have some time, I'll update this article and create a new version of my sieve with ideas from Primegen.

Primegen is fast:
```bash

time ./primes > primes.txt

real	0m11.677s
user	0m10.649s
sys	0m0.708s

```
About 11 seconds for writing all primes between 2 and 1,000,000,000 to a txt file.

<h2>See also</h2>
You might want to try the following Project Euler problem sets:
<ul>
<li>Project Euler
  <ul>
    <li><a href="http://projecteuler.net/problem=3">Problem 3</a>: What is the largest prime factor of the number 600851475143 ?</li>
    <li><a href="http://projecteuler.net/problem=7">Problem 7</a>: What is the 10 001st prime number?</li>
    <li><a href="http://projecteuler.net/problem=60">Problem 60</a></li>
  </ul>
</li>
<li>SPOJ
  <ul>
    <li><a href="http://www.spoj.com/problems/PRIME1/">PRIME1</a></li>
    <li><a href="http://www.spoj.com/problems/PRIME2/">PRIME2</a></li>
    <li><a href="http://www.spoj.com/problems/KPRIMES2/">KPRIMES2</a></li>
  </ul>
</li>
<li><a href="http://sweet.ua.pt/tos/software/prime_sieve.html">Segmented sieve of Eratosthenes</a></li>
<li><a href="http://www.troubleshooters.com/codecorn/primenumbers/primenumbers.htm">Fun with prime numbers</a>: This looks almost like my article. It might be interesting, because the author thought about finding primes above $10^9$ which I didn't.</li>
</ul>

<h2>Finally</h2>
The last script that took 23 seconds for calculating and writing all primes in 2 to 1,000,000,000 seems to be the best one. Do you know anything else that could get improved? Please provide a working example (e.g. as a <a href="https://gist.github.com/">gist</a>)
