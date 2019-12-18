---
layout: post
title: Bucketing in A/B-Testing
slug: bucketing-in-ab-testing
author: Martin Thoma
date: 2019-11-28 20:00
category: Code
tags: Data Science, A/B-Testing, Random Number Generator
featured_image: logos/data-science.png
---
Bucketing users in two groups is a key part in A/B testing. We need to randomly
assign users to a bucket. And in practice, we need to make sure a user is
assigned to the same bucket consistently.

First, we need a user identifier.


## Database Solution

We want to store a variation per user in a database. Hence we have [key-value store](https://martin-thoma.com/key-value-stores/) with the user-identifier as key and
the variation as value.

The code then is as follows:

```python
import random
from typing import Dict


def get_variation(user_id: int) -> str:
    # Some initialization / connection with a key_value_store
    variation = key_value_store.get(user_id)
    if variation is None:
        # The user_id was not in the key_value_store
        variation = assign_user_to_variant(user_id, {"A": 0.6, "B": 0.4})
    return variation


def assign_user_to_variant(user_id: int, distribution: Dict[str, float]) -> str:
    """
    Assign the user_id to a variant.

    Parameters
    ----------
    user_id : int
    distribution : Dict[str, float]
        Maps the name of a variant to a float. The sum of all should be 1.

    Returns
    -------
    variant : str
    """
    assert sum(distribution.values()) == 1.0
    user_number = random.random()  # in the interval [0, 1]
    prob_sum = 0.0
    for variant, prob in sorted(distribution.items()):
        if prob_sum <= user_number < prob_sum + prob:
            return variant
        prob_sum += prob
    return variant
```

In case the `user_id` is not an integer, you have two ways to assign one:

1. Have another table mapping the strings to the numbers, counting up from 0.
2. Use a hash (e.g. MD5) and convert the hexstring to a number (base 16 conversion).
   Optimizely uses a <a href="https://en.wikipedia.org/wiki/MurmurHash">MurmurHash</a> (Python: <a href="https://pypi.org/project/mmh3/">mmh3</a>)


## Seeding Solution

The above solution is nice, because it is absolutely clear how it works. It is
not so nice that you need to access a database.

Instead, you can play around with the seed of the random number generator. This
makes the database call obsolete. By seeding we can guarantee the output of
the random number generator while still having (pseudo) random numbers.

```python
import random
from typing import Dict


def assign_user_to_variant(user_id: int, distribution: Dict[str, float]) -> str:
    """
    Assign the user_id to a variant.

    Parameters
    ----------
    user_id : int
    distribution : Dict[str, float]
        Maps the name of a variant to a float. The sum of all should be 1.

    Returns
    -------
    variant : str
    """
    assert sum(distribution.values()) == 1.0
    random.seed(user_id)
    user_number = random.random()  # in the interval [0, 1]
    prob_sum = 0.0
    for variant, prob in sorted(distribution.items()):
        if prob_sum <= user_number < prob_sum + prob:
            return variant
        prob_sum += prob
    return variant
```

Please note that this has another nice property: If you change the distribution
slightly, then as many users as possible keep what they have.

A potential problematic property: Always the same users get to be in the "A"
variant. So if you always choose the names "current" vs. "new", then some users
will always end up in A/B&nbsp;tests. This is not good as the new variant might be
brittle or have flaws.

Instead, we can give the test an unique name and thus do:

```python
import random
from typing import Dict

import mmh3

def assign_user_to_variant(user_id: str, test_name: str, distribution: Dict[str, float]) -> str:
    """
    Assign the user_id to a variant.

    Parameters
    ----------
    user_id : str
    test_name : str
    distribution : Dict[str, float]
        Maps the name of a variant to a float. The sum of all should be 1.

    Returns
    -------
    variant : str
    """
    assert sum(distribution.values()) == 1.0
    seed = mmh3.hash(user_id + test_name)
    random.seed(user_id)
    user_number = random.random()  # in the interval [0, 1]
    prob_sum = 0.0
    for variant, prob in sorted(distribution.items()):
        if prob_sum <= user_number < prob_sum + prob:
            return variant
        prob_sum += prob
    return variant
```


## Random Number Generators

We might want to generate the variations across multiple systems. Most of the
code above is trivial to execute in any programming language. However, the
output of `random.seed(0); random.random()` might differ between programming
languages or even versions of a programming language. The reason are
differences in the random number generators.

A Pseudo-Random Number Generator (RNG) is a key component for the described
solution. In the following is a list of the components:

<table class="table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Seed</th>
            <th>Neighboring Seeds</th>
            <th>Used By</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Mersenne_Twister">Mersenne Twister</a></td>
            <td style="background-color: #ccffcc" class="text-center"><span style="color:green;" title="Yes">✔️</span></td>
            <td style="background-color: #ccffcc">Different results</td>
            <td><a href="https://docs.python.org/3/library/random.html">Python 2.3 to 3.8</a>, <a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/Random.html">R</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Linear_congruential_generator">Linear congruential generator</a></td>
            <td style="background-color: #ccffcc" class="text-center"><span style="color:green;" title="Yes">✔️</span></td>
            <td style="background-color: #ffd3d3">Similar results</td>
            <td><a href="https://docs.oracle.com/javase/8/docs/api/java/util/Random.html">Java 8</a>, <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/n4713.pdf">C++</a>, <a href="https://www.php.net/manual/en/function.rand.php">PHP?</a>, <a href="https://www.nu42.com/2014/05/perl-5200-brings-better-prng-to-windows.html">Perl</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Permuted_congruential_generator">Permuted Congruential Generator</a> <sup id="fnref-2"><a class="footnote-ref" href="#fn-2">2</a></sup></td>
            <td style="background-color: #ccffcc" class="text-center"><span style="color:green;" title="Yes">✔️</span></td>
            <td class="text-center">?</td>
            <td><a href="https://docs.scipy.org/doc/numpy/reference/random/bit_generators/pcg64.html">Numpy</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Salsa20#ChaCha20_adoption">ChaCha20</a></td>
            <td class="text-center">?</td>
            <td class="text-center">?</td>
            <td><a href="https://rust-random.github.io/rand/rand/rngs/struct.StdRng.html">Rust</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Xorshift">xorshift128+</a></td>
            <td class="text-center">?</td>
            <td class="text-center">?</td>
            <td><a href="https://v8.dev/blog/math-random">JavaScript (V8)</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Xoroshiro128%2B">Xoroshiro128+</a></td>
            <td style="background-color: #ccffcc" class="text-center"><span style="color:green;" title="Yes">✔️</span></td>
            <td style="background-color: #ccffcc">Different results</td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Counter-based_random_number_generator_(CBRNG)">Threefry / Philox</a></td>
            <td style="background-color: #ccffcc" class="text-center"><span style="color:green;" title="Yes">✔️</span></td>
            <td style="background-color: #ccffcc">Different results</td>
            <td></td>
        </tr>
    </tbody>
</table>

I cannot properly judge the statistical quality of those, but I recommend
reading [^1] and [^2].

However, I tried [`java-random`](https://pypi.org/project/java-random/) and
visualized the results ([code](https://github.com/MartinThoma/algorithms/blob/master/Python/random/generate_number_image.py)).
What you see is 1000 random numbers generated. The colum is the seed, the row
are 1000 consecutive random numbers. Clearly, the numpy and the Python version
look better:

<table class="table">
    <thead>
    <tr>
        <th>Java</th>
        <th>Python</th>
        <th>Numpy (PCG64)</th>
    </tr>
    </thead>
    <tr>
        <td><a href="../images/2019/11/1000-random-numbers-java.png"><img src="../images/2019/11/1000-random-numbers-java.png" alt="Java Pseudo-Random Number Generator" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-python.png"><img src="../images/2019/11/1000-random-numbers-python.png" alt="Python Pseudo-Random Number Generator" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-numpy.png"><img src="../images/2019/11/1000-random-numbers-numpy.png" alt="Numpy Pseudo-Random Number Generator" width="300" height="300"/></a></td>
    </tr>
    <tr>
        <td>Do you see the stripes? This means neighboring seeds lead to similar sequences. Kudos to my colleague <a href="http://jblewitt.com/blog/">James Blewitt</a> who made me aware of this problem.</td>
        <td colspan="2">This is how it should look like - no pattern to be seen.</td>
    </tr>
    <tr>
        <th>MT19937</th>
        <th>Philox</th>
        <th>Xoroshiro128</th>
    </tr>
    <tr>
        <td><a href="../images/2019/11/1000-random-numbers-MT19937.png"><img src="../images/2019/11/1000-random-numbers-MT19937.png" alt="MT19937 PRNG" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-Philox.png"><img src="../images/2019/11/1000-random-numbers-Philox.png" alt="Philox PRNG" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-Xoroshiro128.png"><img src="../images/2019/11/1000-random-numbers-Xoroshiro128.png" alt="Xoroshiro128 PRNG" width="300" height="300"/></a></td>
    </tr>
    <tr>
        <th>SFC64</th>
        <th>Xorshift1024</th>
        <th>ThreeFry</th>
    </tr>
    <tr>
        <td><a href="../images/2019/11/1000-random-numbers-SFC64.png"><img src="../images/2019/11/1000-random-numbers-SFC64.png" alt="SFC64 PRNG" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-Xorshift1024.png"><img src="../images/2019/11/1000-random-numbers-Xorshift1024.png" alt="Xorshift1024 PRNG" width="300" height="300"/></a></td>
        <td><a href="../images/2019/11/1000-random-numbers-ThreeFry.png"><img src="../images/2019/11/1000-random-numbers-ThreeFry.png" alt="ThreeFry PRNG" width="300" height="300"/></a></td>
    </tr>
</table>


Security in the sense of predictability of the sequence is also an important
property in many contexts. In the context of A/B-Testing, however, it does not
matter. State size is also interesting.

PHP and Golang do either not at all or at least not clearly state what the
default random number generator is.


## TL;DR

Bucketing is easy as long as you have one system (OS and Programming language /
library) where you execute the bucketing. Once you have more, you need to take
care of how <code>random.random()</code> actually works


## See also

[^1]: [Random Number Generator Overview](http://www.pcg-random.org/)
[^2]: Melissa E. O'Neill: [PCG: A Family of Simple Fast Space-Efficient Statistically Good Algorithms for Random Number Generation](https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf), 2014.
[^3]: Babu, Thomas: [Freestyle, a randomized version of ChaCha for resisting offline brute-force and dictionary attacks](https://arxiv.org/abs/1802.03201), 2018.
[^4]: Optimizely: [How bucketing works](https://docs.developers.optimizely.com/full-stack/docs/how-bucketing-works)
[^5]: Dario Gieselaar: [The Engineering Problem of A/B Testing](https://levelup.gitconnected.com/the-engineering-problem-of-a-b-testing-ac1adfd492a8), 2019. - Just a nice post about A/B Testing in general.
[^6]: [Bit Generators](https://docs.scipy.org/doc/numpy/reference/random/bit_generators/)
[^7]: PyPI: [randomgen](https://pypi.org/project/randomgen/)
[^8]: Wikipedia: [List of random number generators](https://en.wikipedia.org/wiki/List_of_random_number_generators)
