---
layout: post
title: What Is a Secure Password?
slug: what-is-a-secure-password
lang: en
author: Martin Thoma
date: 2021-02-10 18:02
category: Security
tags: Security, Password
featured_image: logos/cybersecurity.png
summary: Cybersecurity for non-developers
medium_url: https://medium.com/@martinthoma/what-is-a-secure-password-97263aeedea9
---
Passwords are the keys to the locks that secure our accounts: Your email, bank and investment account, social media, company portals, and many more use password-based authentication. They all ask you to create a secure password and sometimes give you rules like this:

* Minimum of 8 characters
* At least one digit, lower case letter, upper case letter, special character
* No consecutive 3 digits

However, I have seen some non-developers struggle to find a good password. **After reading this article, you should be able to come up with secure strong passwords that you can memorize**.

## The Attacker’s Perspective

> Feel free to ignore this (more technical) section and jump directly to the Secure Password recipe. This section is not required to understand how to create secure passwords.

You want to protect yourself against two scenarios:

1. The attacker wants to get access to your account. They can’t break the web service, so they try to see if you used a bad password.
1. The attacker broke a part of the web service. The password was stored as a hash (similar to encryption, but [not the same](../encryption-vs-encoding-vs-hashing/)). They want to get your password from that hash.

In both scenarios, the attacker might use the information they have from you or run a more general, non-personalized attack.

### Personalized Attack

Think about which information is easy to get from you:

* First and last name
* Name of children, partner, close friends, family, pets (e.g. via Facebook)
* Birthday of you/your partner
* Places you have lived at or which are important to you.

All of those are for sure not secure. Not even when you combine that, e.g. a city you have lived in + your birth year.

People and companies might get this information easily with social engineering. For example, think of those nice innocent online quizzes:

* “Which Superhero Are You?” can ask for your name, your birthday, pets.
* “Are you and your partner compatible?” and any other couple quiz can easily ask for birthdays, names, hobbies, important places, family structure, friends, …

By providing half-interesting information which gets advertised on Twitter / Facebook, you can get first information about interesting employees:

* “Download our e-book about SCRUM!” — but fill in your name, employer, your role, and how long you’re in that position first.
* “5 actions to improve your remote office”

There are many other ways to gather a lot of information about people. I’ll write a blog post about social engineering, I promise.

### Non-Personalized Attack

There are some words that people like to make use of in their passwords:

* Common English words: password, sex, admin
* Common English sentences: iloveyou
* Letter sequences: abc, asdf (also longer ones like abcd 🙄)
* Digit sequences: 1234

Attackers use lists of leaked passwords. Troy Hunt collected [21 million leaked passwords](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/) — all of them are insecure now.

Additionally, there are dictionary attacks. Just as the term indicates, a dictionary is used to hack the password. These dictionaries are not simply used directly, but instead, simple combination rules are applied:

* Replace single characters with digits / special characters. Leetspeak is popular, e.g. replacing `a -> @`, `o -> 0`, `i -> 1/!`, `t -> 7`.
* Combining two words

The point of those is that some rules are way more complex than others. For example, getting all 2-word combinations out of a 100k dictionary gives (100k)² = 10,000,000,000 possibilities. Replacing digits by the four rules above, assuming that every word has on average two of those gives about 4x the dictionary size. Hence only 400k possibilities. You want the attacker to go through many, hence taking two words is way more complex than replacing single characters.

### Give me ze Toolz!

You take some of your passwords and get the MD5 hash of them:

```
$ python -c "import hashlib as h; print(h.md5(b'love').hexdigest())"
b5c0b187fe309af0f4d35982fd961d7e
```

Add them to a text file `hashes.txt`:

```
b5c0b187fe309af0f4d35982fd961d7e
4d1f35512954cb227b25bbd92e15bc7b
b339b1d1144a5f210e86e9833aca18ff
d171e07e33050531aa70ad66f09ac142
```

Then install [hashcat](https://hashcat.net/hashcat/):

```
$ brew install hashcat  # on Mac using Homebrew
$ apt-get install hashcat  # on Ubuntu
```

And run it with [this English wordlist](https://github.com/dwyl/english-words/blob/master/words.txt):

```
$ hashcat -m 0 -a 0 hashes.txt words.txt -r /usr/share/hashcat/rules/dive.rule -o cracked.txt -O

# -m 0: It's an MD5 hash
# -a 0: Use the "straight" attack mode
# -r /usr/share/hashcat/rules/dive.rule: Use those rules
#             to derive passwords from given words
# -O Limit password length
```

On my 5-year-old laptop, it takes less than 1 second to crack the first 3 and about 16 seconds to crack the last one:

```
b5c0b187fe309af0f4d35982fd961d7e:love
b339b1d1144a5f210e86e9833aca18ff:Cracking
4d1f35512954cb227b25bbd92e15bc7b:cracking
d171e07e33050531aa70ad66f09ac142:Cr@ck1ng
```

## A recipe for Secure Passwords: Wikipedia

Now you might wonder how you actually come up with secure passwords. One simple method is to use a list of many words (30k or more) and pick 4 words at random. That gives (30k)⁴ = 810 · 10¹⁵.

In comparison, most people do this: Pick one word out of maybe 30k words in your active vocabulary that have at least 6 characters, add one digit, and replace up to three characters, then there are about 30k · 10 · 2 · 2 · 2 = 2.4 · 10⁶ possibilities. That is WAY less than 810 · 10¹⁵.

Now assume it would take 1/10 second to crack 2.4 · 10⁶. Then it would take 1070 years to crack the 4 random words. And it becomes way more extreme if you either pick more words or have a longer wordlist. Additionally, you can take a word list from your mother tongue. For example, if the Wikipedia in your language is big enough, you can use article names as the word list. As a random process to pick articles, you can click on “random article”.

To summarize:

1. Pick a Wikipedia which is in a language you know and has at least 50k articles ([comparison](https://meta.wikimedia.org/wiki/List_of_Wikipedias))
1. Click on “random article”. Write down the full name of the article.
1. Repeat step (2) for 4 times in total.

Now you have your password. For example, I would just have gotten `MojstranaFrederick WoltmannSoraruStorm Eleanor`. 46 characters — quite a beast. That is the biggest disadvantage of the Wikipedia Recipe for secure passwords.

## Diceware

[Diceware](https://en.wikipedia.org/wiki/Diceware) uses exactly the same principle but uses a word list. The list contains 6⁵ = 7776 common English words. The process for generating a password is:

1. You throw 5 dice and then you can look up one word
1. Repeat that at least 6 times

Here are some wordlists I can recommend:

* [English (5 dice)](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) by [EFF](https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation)
* [German (5 dice)](https://theworld.com/~reinhold/diceware_german.txt) by Arnold Reinhold
* [Spanish (5 dice)](https://theworld.com/~reinhold/DW-Espanol-1P.pdf) by Manuel Palao
* and [many more](https://theworld.com/~reinhold/diceware.html)

I got `basics-crawfish-undaunted-persuader-diagnosis-swimwear`. So 54 characters. You also don’t want to type that often. But think about how hard this is to remember and how hard it is to remember many of the “random” passwords you come up with.

## Related Topics

* **Password Managers**: You should definitely use a password manager! The main purpose of the password manager is to prevent password re-use. Every single service should have its own password. **NEVER re-use a password**. By using a password manager, you can automatically let it create super-strong passwords. And you only have to remember the password of the password manager.
* [**Multi-Factor Authentication (MFA) / Two-Factor Authentication (2FA)**](../multi-factor-authentication/): Some services allow you to use another factor to authenticate, e.g. an app or an SMS. This increases your security a lot. Use it.
