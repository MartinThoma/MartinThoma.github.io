---
layout: post
title: Password Hashing  😇
slug: password-hashing
URL: https://levelup.gitconnected.com/password-hashing-eb3b97684636
author: Martin Thoma
date: 2020-10-19 20:00
category: Security
tags: InfoSec, AppSec, Security, Cybersecurity, Password
featured_image: logos/cybersecurity.png
---
Software gets hacked, data breaches happen, data is leaked. It’s not a rare exception but happens all the time. We need to acknowledge that software is not perfect. This is where the concept of defense in depth comes into play.
> # Defense in depth means we don’t rely on a single security mechanism, but have multiple layers of security instead.

Password hashing is a prime example of defense in depth. If our database is secure, we don’t need password hashing. We hope it is the case and defend the database as well as possible, but we prepare for the worst case. We prepare for an attacker getting access to our users’ login credentials.

A key idea of privacy comes into play: You don’t have to worry about data you don’t have. In the case of passwords, we don’t store the passwords. Not even an encrypted version. We store a hashed version.

This way the effect is hopefully limited to our service. We need to tell the users that their accounts and data might have been exposed, but at least nobody will use the same username/password combination to log into their bank/Amazon/Social accounts.

## What is Hashing?

Hashing is like cooking. Given the recipe (the hashing algorithm) and the ingredients (the password), you can always get the same result. Just given the result (the hash), it is virtually impossible to reverse the process (figure out the password).

There are non-cryptographic hashing functions and cryptographic ones. The cryptographic ones are designed to be hard to compute. Meaning they take a lot of CPU power/time to apply. This is on purpose. If you need a few milliseconds to apply it on your (weak) server, the attacker hopefully also needs quite a while to apply it billions of times on huge dictionaries to crack the encrypted accounts with brute force.

![Photo by [American Heritage Chocolate](https://unsplash.com/@americanheritagechocolate?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/11800/0*JY7QzN4RasPmA7Nf)*Photo by [American Heritage Chocolate](https://unsplash.com/@americanheritagechocolate?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

## Why it Matters

There are [so many leaks](https://en.wikipedia.org/wiki/List_of_data_breaches), it is hard to keep track of the leaks.

* **2012**: LinkedIn leaked 6.5 million passwords. Passwords have been hashed with SHA-1 and were not salted ([source](https://arstechnica.com/information-technology/2012/06/8-million-leaked-passwords-connected-to-linkedin/)).
* **2013**: Adobe leaked 130 million passwords ([source](https://www.theguardian.com/technology/2013/nov/07/adobe-password-leak-can-check)). The passwords were encrypted, not hashed.
* **2016**: LinkedIn got hacked and used a weak hashing algorithm ([source](https://www.zdnet.com/article/these-are-the-worst-passwords-from-the-linkedin-hack))
* **2019**: 1.2 million passwords got leaked via the porn site Luscious([source](https://www.forbes.com/sites/daveywinder/2019/08/20/popular-porn-site-breach-exposed-12-million-anonymous-user-profiles/#3c0cbe067039))
* **2019**: Facebook had hundreds of millions of passwords stored in plain text ([source 1](https://about.fb.com/news/2019/03/keeping-passwords-secure/), [source 2](https://www.nytimes.com/2019/03/21/technology/personaltech/facebook-passwords.html))
* **2019**: Zynga leaked 170 million passwords ([source](https://www.theguardian.com/games/2019/dec/19/170m-passwords-stolen-in-zynga-words-with-friends-hack-monitor-says)). Zynga used hashing and salting.

You can see if you might have been affected by [haveibeenpwned.com](https://haveibeenpwned.com/).

## Salt — because hashing is not enough

When credentials are leaked, it essentially is a big table with usernames and
the (hopefully) hashed passwords. If you applied the same algorithm to all
passwords, you can see which users have the same passwords. Extra information
such as the user names, the usage of the platform, or other attacks such as
phishing might lead to information about those passwords.

To counter such password cracking attacks, a string is added to the password.
This string is randomly generated for each user. The string is stored
side-by-side to the password. The only reason to have that string is to make
the same plain-text password have different hash values.

## How can I hash passwords?

Computing a key from a password which then can be stored now got quite a bit
more complex: We need the password, a hashing function, a random salt per user,
and sometimes even a number of rounds to hash. There is a lot of possibilities
to get it wrong. Also, what do you do to migrate from one hashing function to
another? What do you do to increase the number of rounds as hardware becomes
better?

You for sure don’t want to always force users to enter a new password. You want
to be able to let users migrate over time.

A key derivation function as implemented in Pythons
[werkzeug](https://pypi.org/project/Werkzeug/) package with adjustable
computational difficulty like [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) is
your friend. It’s a function that takes the password, the hashing function, the
salt, the number of rounds. It returns the key. In most programming languages
you two functions:

```python
def generate_key(password, hash_function, salt_length) -> key:
    ...


def check_key(password, key) -> bool:
    ...
```

As an example:

```python-repl
>>> **from** werkzeug.security **import** generate_password_hash as gen_key
>>> key = **gen_key**("foobar", "pbkdf2:sha512:1000", salt_length=8)

>>> key
'pbkdf2:sha512:1000**$**qc8Q9uqK**$**4f28daacb10dea6667e00c866607073b7a740817e8c4a267c1cedd05cf36cbdf609b14cf446d73d76819f37a3e0475160d444a4fab39526e72aca611960e4c77'

>>> **from** werkzeug.security **import** check_password_hash as check_key
>>> **check_key**(key, "foobar")
True
```

You can see that the first part of the method contains all the parameters necessary for the method. This means it is easy to extend. The second part (delimited by the Dollar symbol) is the 8 characters of the salt. Then comes the password which is hashed with the given method and salt.

There are other key derivate functions. Most notably [scrypt](https://en.wikipedia.org/wiki/Scrypt), which was not only designed to be demanding to the CPU but also requires much memory. For Python, there is passlib which offers a lot of hashing functions and key derivation functions. However, it seems not too wide-spread ([source](https://github.com/pallets/werkzeug/issues/1917#issuecomment-710762497)). Instead, you can create something similar on your own by using core Python functions such as [hashlib.scrypt](https://docs.python.org/3/library/hashlib.html#hashlib.scrypt) . A noteworthy key derivation function is [Argon2](https://en.wikipedia.org/wiki/Argon2).

## Common Mistakes

Let’s make a checklist. If you are a developer, I hope you can checkmark those:

☑ I don’t store passwords in plain text.
☑ I don’t use encryption for passwords.
☑ I don’t use a non-cryptographic hashing function (e.g. CRC-32, )
☑ I don’t use a weak cryptographic hashing function (e.g. MD5, SHA-1)
☑ I use a different, randomly calculated salt for each user for calculating the hashes.

As a user, I hope you can checkmark the following points:

☑ I don’t re-use passwords. Ever.
☑ I don’t share my passwords.
☑ I don’t use weak passwords.
☑ I make sure I don’t [leak my secrets](https://levelup.gitconnected.com/leaking-secrets-240a3484cb80).
☑ I am aware of phishing. (If you are not — a blog post will follow😀)

As a developer, you can prevent some mistakes from the user by a password policy. For example, making it mandatory to have at least 8 characters and maybe run the password through a simple dictionary attack before you allow it. I wouldn’t put password rules up, though. [XKCD 936](https://xkcd.com/936/) explains why.

![Image by Oliver Widder ([Geek and Poke](https://geekandpoke.typepad.com/geekandpoke/2009/08/post20-security.html))](https://cdn-images-1.medium.com/max/2992/1*BYKHbPTILDYTxW2Xug8xPA.jpeg)*Image by Oliver Widder ([Geek and Poke](https://geekandpoke.typepad.com/geekandpoke/2009/08/post20-security.html))*

## What can I do as a user?

As a user, you should **use different passwords for different services**. The passwords should not be super weak as well (e.g. guessable). This combination makes it impossible for me to just memorize. I have only a handful of strong passwords I memorize. For the rest, I need to **use a password manager**. The password manager can then suggest strong passwords as well.

A strong password has high entropy. This means:

* At least 8 characters. Let’s rather be safe and have at least 10 characters.
* A rich character set (e.g. upper- and lower-case letters, digits, special characters)
* Is not a combination of only two or three words in a dictionary

You can also **change your passwords regularly**. This will make sure that people who had access for a while without being noticed will be blocked out again.

## See also

It feels like [Tom Scott](https://en.wikipedia.org/wiki/Tom_Scott_(entertainer)) / [Computerphile](https://www.youtube.com/user/Computerphile) made a video about all the security topics I want to write about 😄

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/8ZtInClXe1Q" frameborder="0" allowfullscreen></iframe></center>

## What’s next?

In this series about application security (AppSec) we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: [SQL Injections](https://medium.com/faun/sql-injections-e8bc9a14c95) 😈
* Part 2: [Don’t leak Secrets](https://levelup.gitconnected.com/leaking-secrets-240a3484cb80) 😇
* Part 3: [Cross-Site Scripting (XSS)](https://levelup.gitconnected.com/cross-site-scripting-xss-fd374ce71b2f) 😈
* Part 4: [Password Hashing](https://levelup.gitconnected.com/password-hashing-eb3b97684636) 😇
* Part 5: [ZIP Bombs](https://medium.com/bugbountywriteup/zip-bombs-30337a1b0112) 😈
* Part 6: [CAPTCHA](https://medium.com/plain-and-simple/captcha-500991bd90a3) 😇
* Part 7: [Email Spoofing](https://medium.com/bugbountywriteup/email-spoofing-9da8d33406bf)
* Part 8: [Software Composition Analysis](https://medium.com/python-in-plain-english/software-composition-analysis-sca-7e573214a98e) (SCA) 😇
* Part 9: [XXE attacks](https://medium.com/faun/xxe-attacks-750e91448e8f) 😈

And this is about to come:

* CSRF 😈
* DOS 😈
* Credential Stuffing 😈
* Cryptojacking 😈
* Single-Sign-On 😇
* Two-Factor Authentication 😇
* Backups 😇
* Disk Encryption 😇

Let me know if you are interested in more articles around AppSec / InfoSec!
