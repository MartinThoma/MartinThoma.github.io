---
layout: post
title: Brute Force Attacks 😈
slug: brute-force-attacks
lang: en
author: Martin Thoma
date: 2024-08-23 10:47
category: Security
tags: Security, AppSec, Brute-Force, Password
featured_image: logos/cybersecurity.png
summary: Just try all options with an exhaustive brute-force search
medium_url: https://medium.com/@martinthoma/brute-force-attacks-c212429d2243
status: draft
---
Brute Force attacks are about accessing a system with authentication by trying all possible combinations.

Think about a combination lock. You can start at 0–0–0–0 and go up to 9–9–9–9. It might take a while, but you will get there.

Similarly, an attacker can get your smartphone PIN or bank account data.

## Why it Matters

It is the simplest approach for attackers to get an account. **Getting the plain-text password** when password files are leaked is also commonly done. The idea is that people typically re-use passwords (which you shouldn’t do for exactly this reason). You can see that this matters:

* 2024: 20 million MD5-hashed and salted passwords leaked by cutout.pro ([source](https://www.techradar.com/pro/security/top-ai-service-hit-by-massive-data-breach-20-million-cutoutpro-users-have-personal-info-leaked-so-change-passwords-now))
* 2023: 36 million hashed passwords leaked by Comcast ([source](https://techcrunch.com/2023/12/19/comcast-xfinity-hackers-36-million-customers/))
* 2023: 9 million SHA256 hashed passwords leaked by Zacks ([source](https://www.scmagazine.com/news/zacks-confirms-iaccount-data-hacked))
* 2022: 44 million hashed passwords leaked by START ([source](https://therecord.media/leading-russian-streaming-platform-suffers-data-leak-allegedly-impacting-44-million-users))
* 2020: 8.3 million MD5 hashed and salted passwords leaked by Freepik ([source](https://cisomag.com/freepik-suffered-data-breach/))
* 2016: 117 million SHA-1 hashed passwords leaked by LinkedIn ([source](https://www.vice.com/en/article/another-day-another-hack-117-million-linkedin-emails-and-password/))
* 2016: 43 million MD5 hashed passwords leaked by Last.fm ([source](https://techcrunch.com/2016/09/01/43-million-passwords-hacked-in-last-fm-breach/))
* 2012: 6.5 million SHA-1 hashed passwords leaked by LinkedIn ([source](https://techcrunch.com/2012/06/06/6-5-million-linkedin-passwords-reportedly-leaked-linkedin-is-looking-into-it/))

Any computer/laptop/tablet/smartphone to which you have physical access can be broken using brute force. It’s just a matter of time.

The other type of brute force attack is when you have a **live system**. That could be a bike lock, key-code opened digital lock, or any web service. If you know somebody's Google Mail address, you can just try to log in as that person by going to mail.google.com and trying passwords.

## How are Brute Force attacks executed?

Let’s assume you have an MD5-hashed password locally. That means the password was “scrambled” in a deterministic way. Authentication then works like this:

```python
def authenticate(user, provided_password):
    return user.hashed_stored_password == md5(provided_password)
```

[MD5](https://en.wikipedia.org/wiki/MD5) should never be used for password hashing as it is fast to compute. The problem is that an attacker can do this:

```python
import itertools
from hashlib import md5
import time


def brute_force_password(hashed_password):
    hashed_password_bytes = bytes.fromhex(hashed_password)

    t0 = time.time()
    for i, candidate in enumerate(generate_candidate(), start=1):
        if md5(candidate).digest() == hashed_password_bytes:
            t1 = time.time()
            speed = i / (t1 - t0)
            print(f"Password found in {t1 - t0:.1f}s after {i:,} iterations")
            print(f"Speed: {speed:.1f} hashes per second")
            return candidate.decode("utf-8")


def generate_candidate(length=1):
    ascii_bytes = bytes(range(32, 127))
    while True:
        for combination in itertools.product(ascii_bytes, repeat=length):
            yield bytes(combination)
        length += 1


print(brute_force_password("d0871a2b53c62de5e046fede42f3f7ab"))
```

This is a super simple example to illustrate the concept. Even on my old machine, using this trivial approach, using Python, using just one core, I can try 1.3 million passwords per second.

### Combinatorics — Why password length matters

If you use the standard 95 ASCII characters for your password:

```text
 !"#$%&'()*+,-./
0123456789
:;<=>?@
ABCDEFGHIJKLMNOPQRSTUVWXYZ
[\]^_`
abcdefghijklmnopqrstuvwxyz
{|}~
```

and pick your passwords completely at random, then a longer password leads to more possible passwords the attacker has to try. On my 7-year-old laptop, I can check about 1.3 Million MD5 hashes per second. With [John the Ripper](https://github.com/openwall/john), I get 61.2 Million MD5 hashes per second:

```bash
$ OMP_NUM_THREADS=2 ./john --format=raw-md5 --test

Benchmarking: Raw-MD5 [MD5 256/256 AVX2 8x3]... DONE
Raw: 61272K c/s real, 61272K c/s virtual
```

Note that this is the dumbest way to brute-force a password. Just trying everything. It’s also on just 2 cores of an old laptop. No GPU. And I didn’t try alternatives like [Hashcat](https://hashcat.net/hashcat/).

An Nvidia 3060 TI can do 32061.8 MH/s ([source](https://hashcat.net/forum/thread-9694.html), December 2020). That is 32,061,800,000 hashes per second!

This means the maximum time it takes passwords of a given length is:

* 1 character: 95 combinations (instant)
* 2 characters: 95² = 9025 combinations (instant)
* 3 characters: 95³ = 857,375 combinations (instant)
* 4 characters: 95⁴ = 81,450,625 combinations (instant)
* 5 characters: 95⁵ &gt; 7 billion (instant)
* 6 characters: 95⁶ &gt; 735 billion (23 seconds)
* 7 characters: 95⁷ &gt; 69 Trillion (37 minutes)
* 8 characters: 95⁸ (58 hours)
* 9 characters: 95⁹ (227 days)
* 10 characters: 95¹⁰ (60 years)

Note that the Nvidia RTX 3060 Ti is already several years old. I expect the speed to be even higher with a modern GPU.

## Techniques of Attackers

Improving brute force has two aspects: (1) First try the most likely passwords and (2) make sure you’re extremely fast with every try.

### Password lists

RockYou2024 is a list of 8.4 billion used passwords ([source](https://hackernoon.com/rockyou2024-billions-of-passwords-leaked-and-why-you-shouldnt-be-overly-worried)). This is a reasonable first guess when you have a password you want to crack. It takes less than a second to try all of them.

### Rainbow tables

Rainbow tables are pre-computed hashes. That is interesting if you don’t want to crack one password only, but many thousands.

### Dedicated Hardware

There are certain levels of hardware improvement:

* Using more than one CPU core
* Using thousands of GPU cores (6,144 CUDA cores in Nvidia 3070 Ti)
* Using specialized chips: Especially for Cryptocurrencies like Bitcoin people made specialized hardware that can compute certain relevant hash functions on a hardware chip.

## How can it be prevented?

The best way is to have a long randomly generated password that is used only in one service. Password managers are awesome.

But as a software developer, you have little control over your users' passwords. I would only apply one restriction: The password has to have at least 8 characters.

### Salt your Hashes

Instead of storing just the hashed password, you generate a random sequence for every user and hash it together with the password. That random sequence is called the salt:

```python
def authenticate(user, provided_password):
    return user.hashed_stored_password == md5(provided_password + user.salt)
```

The salt needs to be different for every single user. This way, the attacker can no longer use rainbow tables.

Typically you would use a key-derivation function like PBKDF2 or a hashing function like bcrypt that stores the salt alongside the hash.

### Use slow password hash functions

MD5 and SHA1 are fast to calculate. While we typically want this, it is also a desirable property for an attacker. If we want to make the cracking process hard, the hash function should be relatively slow. If possible, it should also be hard to develop ASICs (specialized hardware) for it.

General-purpose cryptographic hash functions like SHA-512 are secure, but they are fast as well. For passwords, use a dedicated password hashing function: Argon2, scrypt, bcrypt, or PBKDF2 with many iterations.

Additionally, you want to apply the hash function multiple times on the key. The only purpose of that is to make the computation slower.

Django uses [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) with SHA256 by default and stores passwords in the following format ([source](https://docs.djangoproject.com/en/5.1/topics/auth/passwords/#how-django-stores-passwords)):

```text
<algorithm>$<iterations>$<salt>$<hash>
```

### Live System Defenses: Time delays and maximum tries

If you have a live system to which people need to log in, you can slow down brute force by adding time delays between login attempts from the same IP address. So instead of trying hundreds of combinations per second, you could slow them down to one try every two seconds.

After a certain amount of failed login attempts, you can add a captcha. Or you could completely block the account — just be aware that this can also be an interesting attack vector. You could also block the attacking IP address.

<!-- series: appsec -->
