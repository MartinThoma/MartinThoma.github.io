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

```
def get_variation(user_id: int) -> str:
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
2. Use a hash (e.g. MD5) and convert the hexstring to a number (base 16 conversion)


## Seeding Solution

The above solution is nice, because it is absolutely clear how it works. It is
not so nice that you need to access a database.

Instead, you can play around with the seed of the random number generator. This
makes the database call redundant. By seeding we can guarantee the output of
the random number generator while still having (pseudo) random numbers.

```
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
            <td>✓</td>
            <td>Very different results</td>
            <td><a href="https://docs.python.org/3/library/random.html">Python 3.8</a>, <a href="https://stat.ethz.ch/R-manual/R-devel/library/base/html/Random.html">R</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Linear_congruential_generator">Linear congruential generator</a></td>
            <td>✓</td>
            <td>Similar results</td>
            <td><a href="https://docs.oracle.com/javase/8/docs/api/java/util/Random.html">Java 8</a>, <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/n4713.pdf">C++</a>, <a href="https://www.php.net/manual/en/function.rand.php">PHP?</a>, <a href="https://www.nu42.com/2014/05/perl-5200-brings-better-prng-to-windows.html">Perl</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Permuted_congruential_generator">Permuted Congruential Generator</a> <sup id="fnref-2"><a class="footnote-ref" href="#fn-2">2</a></sup></td>
            <td>✓</td>
            <td>?</td>
            <td><a href="https://docs.scipy.org/doc/numpy/reference/random/bit_generators/pcg64.html">Numpy</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Salsa20#ChaCha20_adoption">ChaCha20</a></td>
            <td>?</td>
            <td>?</td>
            <td><a href="https://rust-random.github.io/rand/rand/rngs/struct.StdRng.html">Rust</a></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Xorshift">xorshift128+</a></td>
            <td>?</td>
            <td>?</td>
            <td><a href="https://v8.dev/blog/math-random">JavaScript (V8)</a></td>
        </tr>
    </tbody>
</table>

I cannot judge the statistical quality of those, but I recommend reading [^1]
and [^2]. Security in the sense of predictability of the sequence is also an
important property in many contexts. In the context of A/B-Testing, however, it
does not matter. State size is also interesting.

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
