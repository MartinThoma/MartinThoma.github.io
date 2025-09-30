---
layout: post
lang: en
title: Insecure Deserialization 😈🐝
slug: insecure-deserialization
URL: https://medium.com/bugbountywriteup/insecure-deserialization-5c64e9943f0e
author: Martin Thoma
date: 2021-01-28 20:00
category: Security
tags: AppSec, Cybersecurity
featured_image: logos/cybersecurity.png
---
Serialization is the act of transforming objects from an internal
representation to a stream of characters or bytes. The representation of the
serialized object should be platform- and language-independent. Data is
serialized and deserialized in applications to **store** or **transport** it.
In web applications, **JSON** or **XML** is often used for data exchange by
many APIs and protocols. File formats like PNG/GIF/JPEG/MPEG use XML to store
metadata. YAML became extremely popular for configuration files, e.g. in
[Cloudformation
templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html)
or [GitlabCI configuration files](https://docs.gitlab.com/ee/ci/yaml/).

Some file formats allow you to do more than just (de)serializing basic data
types. For example, imagine that you want to set up a CI pipeline. You might
have one step for executing unit tests, one step for checking the types, one
for linting. All of those steps might require installing the same set of
dependencies. Instead of repeating yourself, you want to use **references**.
You define a dictionary once and copy it in many places. References allow a
human to read, write, and modify the file quickly while the machine simply has
the same value(s) in multiple places.

Another powerful feature is to include **external entities**. In the simplest
case, this means that you want to include another file. For example, you could
have a logging configuration that you want to use in multiple places. In more
extreme cases, the external entities could be not in local files but only
available over the internet. To be honest, I don’t know why you would want
that. Please leave a commend if you know!

Most serialization formats are not powerful enough to represent arbitrary
objects you can have. There are differences in how powerful those formats are.
Some want to go very far in terms of compatibility with many languages. As a
potential side effect, they could allow **arbitrary code execution**.

## Why you should care

* Insecure deserialization was number 8 in the **OWASP Top 10**
  ([source](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)) 🐝
* 2013: The YAML node package
  ([CVE-2013–4660](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-4660))
  allowed remote code execution. Remote code execution is as bad as it gets:
  People can take your data, install a backdoor, shut down your service,
  delete or encrypt your data, use your service for crypto-mining, potentially
  harm your hardware.
* 2014: Android < 5.0 an insecure deserialization can result in arbitrary code
  execution ([CVE-2014–7911](https://nvd.nist.gov/vuln/detail/CVE-2014-7911))
* 2015: Android < 5.1.1 allows arbitrary code execution
  ([CVE-2015–3837](https://nvd.nist.gov/vuln/detail/CVE-2015-3837))
* 2015: ArcGIS allowed arbitrary code execution
  ([CVE-2015–2002](https://nvd.nist.gov/vuln/detail/CVE-2015-2002))

* 2015: [One Class to Rule Them All: 0-Day Deserialization Vulnerabilities in Android](https://www.usenix.org/system/files/conference/woot15/woot15-paper-peles.pdf) by Or Peles, Roee Hay, referencing [CVE-2015–3837](https://nvd.nist.gov/vuln/detail/CVE-2015-3837)

* 2019: Kubernetes was vulnerable to a billion laughs DOS attack ([CVE-2019–11253](https://nvd.nist.gov/vuln/detail/CVE-2019-11253))

* 2020: TYPO3 ([CVE-2020–11067](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11067)), IBM QRadar ([CVE-2020–4280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-4280) ) allowed remote code execution.

* 2020: Apache Tomcat allows remote code execution ([CVE-2020–9484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9484))

## How do Deserialization attacks work?

There is actually a multitude of deserialization attacks. One way to group them is by file format, e.g. YAML, XML, Python pickle files, and many others. Another way is by the objective the attacker wants to reach, e.g. Arbitrary Code execution or Denial of Service (DOS).

The issue is that those file formats are too powerful. They either directly allow code execution or they allow to create references to the file system or references to elements within the document.

### Attacking a YAML deserializer

Take this example.yaml file:

```yaml
!!python/object/apply:os.system

args: ['cat /etc/passwd']
```

And execute this Python code:

```python
import yaml  # pip install pyyaml is required

with open("example.yaml") as fp:
    data = fp.read()
yaml.unsafe_load(data)
```

This will print the contents of `/etc/passwd`. You could also delete any (or
all) files on the system, send a web request (e.g. with the contents of that
password file), download and execute software (e.g. a rootkit/backdoor). This
is probably as bad as it can get.

If you want to know more about YAML features, read this:
[**6 YAML Features most programmers don’t know**
*Level-up your YAML knowledge to write cleaner YAML files*levelup.gitconnected.com](https://levelup.gitconnected.com/6-yaml-features-most-programmers-dont-know-164762343af3)

### Attacking XML Deserialization

XML allows referencing external entities such as files (e.g. /etc/passwd ) or
websites. If you want to learn more about why this is an issue, read my
article about XXE attacks [**XXE attacks 😈** *PDF, Excel, SVG, ebooks — all
use XML. They can be
vulnerable.*medium.com](https://medium.com/faun/xxe-attacks-750e91448e8f)

Another possible attack vector is to use the reference feature of XML in a
billion laughs attack: [**DOS via a billion laughs 😈** *Consume arbitrary much
RAM by repeated
referencing*medium.com](https://medium.com/bugbountywriteup/dos-via-a-billion-laughs-9a79be96e139)

### Attacking Pickle Deserialization

Marco Slaviero has shown that deserialization of pickle files allows arbitrary code execution in his paper “[Sour Pickles](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf)”. It was summarized nicely by [Charles Menguy](https://stackoverflow.com/a/10302328/562769) in an example similar to this:

```python
import pickle

pickle.loads(b"cos\nsystem\n(S'cat /etc/passwd'\ntR.")
```

## How can I defend against deserialization attacks?

Two measures you can almost always do:

* **Principle of least privilege**: Run your code with as few privileges as
  possible. You do for sure not need root privileges. Depending on your level
  of paranoia, you could create a specialized user which only does the
  deserialization. You could remove the right to use the network from that
  user.
* **Defense in Depth**: Make sure every component takes possible security
  measures.

For some formats, you can tell the deserializer to ignore some of its features:

* **PyYAML**: Use the yaml.safe_load function. At some point, they changed the
  interface so that yaml.load points to yaml.safe_load . You can still use
  yaml.unsafe_load . I love that they included “unsafe” in the function call.
  This makes it obvious that something might be dangerous.
* **XML**: For Python, there is
  [defusedxml](https://pypi.org/project/defusedxml) which sets various XML
  parsers of Python to safe defaults, preventing
  [XEE](https://medium.com/faun/xxe-attacks-750e91448e8f), the billion laughs
  attack, and quadratic blowup.

For other formats like pickle, you just have to be sure that your input does not cause harm.

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
