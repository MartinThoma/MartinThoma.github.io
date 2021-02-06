---
layout: post
title: DOS via a billion laughs 😈
subtitle: Consume arbitrary much RAM by repeated referencing
slug: billion-laughs-dos
URL: https://medium.com/bugbountywriteup/dos-via-a-billion-laughs-9a79be96e139
author: Martin Thoma
date: 2020-12-23 20:00
category: Security
tags: InfoSec, AppSec, Security, Cybersecurity
featured_image: logos/cybersecurity.png
---
![Image by the author](https://cdn-images-1.medium.com/max/3708/1*Mlli4bOg_zK6Jbllje6bFQ.png)*Image by the author*

The billion laughs attack is known since 2003 ([source](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1564)). The attack uses the references in XML files to make a small source file be huge in memory if all references are expanded. It’s also known as a LOL bomb, XML bomb, or in a variation as a YAML bomb and git bomb. It is a type of denial of service (DOS) attack as it can bring a service down.

## Why you should care

This is a bit too specific to be visible in many news articles. However, there are several big projects which were vulnerable over the years:

* 2003: libxml2 was vulnerable ([CVE-2003–1564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1564))
* 2015: MediaWiki was vulnerable ([CVE-2015–2942](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2942))
* 2016: [libxml2](https://en.wikipedia.org/wiki/Libxml2) was vulnerable … again ([CVE-2016–3705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-3705))
* 2016: HTTP/2 header compression was used to build an HPACK bomb ([CVE-2016–6581](https://nvd.nist.gov/vuln/detail/CVE-2016-6581))
* 2019: Kubernetes was vulnerable ([source](https://github.com/kubernetes/kubernetes/issues/83253), [CVE-2019–11253](https://nvd.nist.gov/vuln/detail/CVE-2019-11253))
* 2019: [c3p0](https://www.mchange.com/projects/c3p0/) (JDBC database drivers) was vulnerable ([CVE-2019–5427](https://nvd.nist.gov/vuln/detail/CVE-2019-5427))

## How it works

The following XML defines an entity laugh , then an entity ha2 which contains laugh twice. This pattern is repeated. This means ha5 contains laugh indirectly 16 times. You can see the exponential growth, can’t you?

```xml
<?xml version="1.0"?>

<!DOCTYPE root [
<!ENTITY laugh "😆">
<!ENTITY ha2 "&ha; &ha;">
<!ENTITY ha3 "&ha2; &ha2;">
<!ENTITY ha4 "&ha3; &ha3;">
<!ENTITY ha5 "&ha4; &ha4;">
]>

<root>&ha5;</root>
```

With ha31, we would have 2³⁰ times 😆 . That is a billion laughs. Please note how asymmetric this is: With a document that is less than 1kB big the attacker can make the parser consume about Gigabytes of memory. This can easily consume all memory of a machine and thus render it unusable until the parser is killed or the machine is restarted.

A slight variation of the **billion laughs attack** is called **quadratic blowup**.

Please notice that similar attacks are possible in other file formats such as YAML. The key point here is that those formats have references.

## How can I defend against a billion laughs?

Assuming that you cannot control the input directly and prevent XMLs with attacks from reaching you at all, I can think of 4 measures:

* **Lazy evaluation of references**: Instead of evaluating the whole document at once, the references are only resolved when necessary. It might solve some issues.
* **No evaluation of references**: Throwing the dangerous feature out of the window for sure means that you’re not vulnerable to the attack anymore. You need to make sure it doesn’t affect your users, though. Communicating this might be hard.
* **Reference recursion depth limit**: The parser itself could be aware of this issue and have a threshold when it stops evaluating references. However, this might also lead to false-positives — documents that get not parsed, because the parser thinks it’s an attack.
* **RAM restriction**: You can run the code that might execute the billion laughs attack under resource restrictions. This means the execution thread/process receives a (catchable) exception and can continue execution normally. It might especially mean that even if the exception is not thrown, the rest of your system might be fine. Only that thread/process might be killed.

So, how do you do this with Python?

The resource restriction is easiest:

```python
import resource
import contextlib


@contextlib.contextmanager
def limit(resource_type, limit):
    """Temporarily limit a resource."""
    soft_limit, hard_limit = resource.getrlimit(resource_type)
    resource.setrlimit(resource_type, (limit, hard_limit))  # set soft limit
    try:
        yield
    finally:
        resource.setrlimit(resource_type, (soft_limit, hard_limit))  # restore


def dangerous_call():
    [i ** 2 for i in range(10 ** 5)]


try:
    with limit(resource.RLIMIT_AS, 2 ** 24):
        dangerous_call()
except MemoryError:
    print("Your call consumed too much memory!")
```

Restricting the parser is sometimes possible, sometimes not. It depends on your
parser. Some have parameters like resolve_entities
([lxml](https://lxml.de/api/lxml.etree.XMLParser-class.html)).

Limiting the maximum decompression size was done against the HTTP/2 “HPACK”
bomb
([source](https://python-hyper.org/projects/hpack/en/latest/security/CVE-2016-6581.html#the-solution)).

## See also

Kate Murphey wrote an awesome article about git bombs, check it out!
[**Exploding Git Repositories**
*If you are an adventurous sort (and can handle a potential reboot) I invite you to clone this tiny repo: $ git clone…*kate.io](https://kate.io/blog/git-bomb/)

## What’s next?

In this series about application security (AppSec) we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: [SQL Injections](https://medium.com/faun/sql-injections-e8bc9a14c95) 😈
* Part 2: [Don’t leak Secrets](https://levelup.gitconnected.com/leaking-secrets-240a3484cb80) 😇
* Part 3: [Cross-Site Scripting (XSS)](https://levelup.gitconnected.com/cross-site-scripting-xss-fd374ce71b2f) 😈
* Part 4: [Password Hashing](https://levelup.gitconnected.com/password-hashing-eb3b97684636) 😇
* Part 5: [ZIP Bombs](https://medium.com/bugbountywriteup/zip-bombs-30337a1b0112) 😈
* Part 6: [CAPTCHA](https://medium.com/plain-and-simple/captcha-500991bd90a3) 😇
* Part 7: [Email Spoofing](https://medium.com/bugbountywriteup/email-spoofing-9da8d33406bf) 😈
* Part 8: [Software Composition Analysis](https://medium.com/python-in-plain-english/software-composition-analysis-sca-7e573214a98e) (SCA) 😇
* Part 9: [XXE attacks](https://medium.com/faun/xxe-attacks-750e91448e8f) 😈
* Part 10: [Effective Access Control](https://levelup.gitconnected.com/effective-access-control-331f883cb0ff) 😇
* Part 11: [DOS via a Billion Laughs](https://medium.com/bugbountywriteup/dos-via-a-billion-laughs-9a79be96e139) 😈
* Part 12: [Full Disk Encryption](https://medium.com/faun/full-disk-encryption-2090489f9760) 😇
* Part 13: [Insecure Deserialization](https://medium.com/bugbountywriteup/insecure-deserialization-5c64e9943f0e) 😈
* Part 14: [Docker Security](https://levelup.gitconnected.com/docker-security-5f4df118948c) 😇

And this is about to come:

* CSRF 😈
* DOS 😈
* ReDoS 😈
* Credential Stuffing 😈
* Cryptojacking 😈
* Single-Sign-On 😇
* Two-Factor Authentication 😇
* Backups 😇

Let me know if you are interested in more articles around AppSec / InfoSec!
