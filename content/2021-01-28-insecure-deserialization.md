---
layout: post
title: Insecure Deserialization 😈🐝
slug: insecure-deserialization
lang: en
author: Martin Thoma
date: 2021-01-28 20:00
category: Security
tags: AppSec, Security
featured_image: logos/cybersecurity.png
medium_url: https://medium.com/bugbountywriteup/insecure-deserialization-5c64e9943f0e
---
Serialization is the act of transforming objects from an internal
representation to a stream of characters or bytes. The representation of the
serialized object should be platform- and language-independent. Data is
serialized and deserialized in applications to **store** or **transport** it.
In web applications, **JSON** or **XML** is often used for data exchange by
many APIs and protocols. File formats like PNG/GIF/JPEG/MPEG can use XML to store
metadata ([XMP](https://en.wikipedia.org/wiki/Extensible_Metadata_Platform)). YAML became extremely popular for configuration files, e.g. in
[CloudFormation
templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html)
or [GitLab CI configuration files](https://docs.gitlab.com/ee/ci/yaml/).

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
that. Please leave a comment if you know!

Most serialization formats are not powerful enough to represent arbitrary
objects you can have. There are differences in how powerful those formats are.
Some want to go very far in terms of compatibility with many languages. As a
potential side effect, they could allow **arbitrary code execution**.

## Why you should care

* Insecure deserialization was number 8 in the **OWASP Top 10** of 2017
  ([source](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)) 🐝.
  In the 2021 edition, it is part of A08 "Software and Data Integrity Failures"
  ([source](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/))
* 2013: The YAML node package
  ([CVE-2013-4660](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-4660))
  allowed remote code execution. Remote code execution is as bad as it gets:
  People can take your data, install a backdoor, shut down your service,
  delete or encrypt your data, use your service for crypto-mining, potentially
  harm your hardware.
* 2014: In Android < 5.0, an insecure deserialization can result in arbitrary code
  execution ([CVE-2014-7911](https://nvd.nist.gov/vuln/detail/CVE-2014-7911))
* 2015: Android < 5.1.1 allows arbitrary code execution
  ([CVE-2015-3837](https://nvd.nist.gov/vuln/detail/CVE-2015-3837))
* 2015: ArcGIS allowed arbitrary code execution
  ([CVE-2015-2002](https://nvd.nist.gov/vuln/detail/CVE-2015-2002))

* 2015: [One Class to Rule Them All: 0-Day Deserialization Vulnerabilities in Android](https://www.usenix.org/system/files/conference/woot15/woot15-paper-peles.pdf) by Or Peles, Roee Hay, referencing [CVE-2015-3837](https://nvd.nist.gov/vuln/detail/CVE-2015-3837)

* 2019: Kubernetes was vulnerable to a billion laughs DoS attack ([CVE-2019-11253](https://nvd.nist.gov/vuln/detail/CVE-2019-11253))

* 2020: TYPO3 ([CVE-2020-11067](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11067)), IBM QRadar ([CVE-2020-4280](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-4280) ) allowed remote code execution.

* 2020: Apache Tomcat allows remote code execution ([CVE-2020-9484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9484))

## How do Deserialization attacks work?

There is actually a multitude of deserialization attacks. One way to group them is by file format, e.g. YAML, XML, Python pickle files, and many others. Another way is by the objective the attacker wants to reach, e.g. arbitrary code execution or Denial of Service (DoS).

The issue is that those file formats are too powerful. They either directly allow code execution or they allow creating references to the file system or references to elements within the document.

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
*Level-up your YAML knowledge to write cleaner YAML files*](../yaml-features/)

### Attacking XML Deserialization

XML allows referencing external entities such as files (e.g. `/etc/passwd`) or
websites. If you want to learn more about why this is an issue, read my
article about XXE attacks [**XXE attacks 😈** *PDF, Excel, SVG, ebooks — all
use XML. They can be
vulnerable.*](../xxe-attacks/)

Another possible attack vector is to use the reference feature of XML in a
billion laughs attack: [**DoS via a billion laughs 😈** *Consume arbitrary much
RAM by repeated
referencing*](../billion-laughs-dos/)

### Attacking Pickle Deserialization

Marco Slaviero has shown that deserialization of pickle files allows arbitrary code execution in his paper “[Sour Pickles](https://media.blackhat.com/bh-us-11/Slaviero/BH_US_11_Slaviero_Sour_Pickles_WP.pdf)”. It was summarized nicely by [Charles Menguy](https://stackoverflow.com/a/10302328/562769) in an example similar to this:

```python
import pickle

pickle.loads(b"cos\nsystem\n(S'cat /etc/passwd'\ntR.")
```

## How can I defend against deserialization attacks?

Two measures you can almost always do:

* **Principle of least privilege**: Run your code with as few privileges as
  possible. You certainly do not need root privileges. Depending on your level
  of paranoia, you could create a specialized user which only does the
  deserialization. You could remove the right to use the network from that
  user.
* **Defense in Depth**: Make sure every component takes possible security
  measures.

For some formats, you can tell the deserializer to ignore some of its features:

* **PyYAML**: Use the `yaml.safe_load` function. PyYAML 5.1 deprecated calling
  `yaml.load` without an explicit `Loader`, and since PyYAML 6.0 the `Loader` argument
  is mandatory ([changelog](https://github.com/yaml/pyyaml/blob/master/CHANGES)). You can still use
  `yaml.unsafe_load`. I love that they included “unsafe” in the function call.
  This makes it obvious that something might be dangerous.
* **XML**: For Python, there is
  [defusedxml](https://pypi.org/project/defusedxml) which sets various XML
  parsers of Python to safe defaults, preventing
  [XXE](../xxe-attacks/), the billion laughs
  attack, and quadratic blowup.

For other formats like pickle, you just have to be sure that your input does not cause harm.

## More in this series

In this series about application security (AppSec), we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: [SQL Injections](../sql-injections/) 😈🐝
* Part 2: [Don’t leak Secrets](../leaking-secrets/) 😇
* Part 3: [Cross-Site Scripting (XSS)](../xss/) 😈🐝
* Part 4: [Password Hashing](../password-hashing/) 😇
* Part 5: [ZIP Bombs](../zip-bombs/) 😈
* Part 6: [CAPTCHA](../captcha/) 😇
* Part 7: [Email Spoofing](../email-spoofing/) 😈
* Part 8: [Software Composition Analysis](../sca/) (SCA) 😇
* Part 9: [XXE attacks](../xxe-attacks/) 😈🐝
* Part 10: [Effective Access Control](../effective-access-control/) 😇
* Part 11: [DoS via a Billion Laughs](../billion-laughs-dos/) 😈
* Part 12: [Full Disk Encryption](../full-disk-encryption/) 😇
* Part 13: **Insecure Deserialization** 😈🐝
* Part 14: [Docker Security](../docker-security/) 😇
* Part 15: [Credential Stuffing](../credential-stuffing/) 😈🐝
* Part 16: [Multi-Factor Authentication](../multi-factor-authentication/) (MFA/2FA) 😇
* Part 17: [ReDoS](../redos/) 😈

The following articles are about to come:

* Part 18: Secure Messaging 😇
* Part 19: Cryptojacking 😈
* Part 20: Backups 😇
* Part 21: Cryptotrojans 😈
* Part 22: Single-Sign-On 😇
* Part 23: Clipboard Hijacking 😈
* Part 24: Certificates 😇
* Part 25: Race Condition Attacks in Blockchains 😈
* Part 26: Mobile Device Management (MDM) 😇
* Part 27: Server-Side Request Forgery (SSRF) 😈
* Part 28: Network Separation 😇
* Part 29: Social Engineering (including Phishing) 😈
* Part 30: Virtual Private Networks (VPNs) 😇
* Part 31: CSRF 😈

Let me know if you are interested in more articles around AppSec / InfoSec!
