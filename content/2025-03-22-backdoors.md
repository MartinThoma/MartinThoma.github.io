---
layout: post
title: Backdoors 😈
slug: backdoors
lang: en
author: Martin Thoma
date: 2025-03-22 16:09
category: Security
tags: Security, AppSec
featured_image: logos/cybersecurity.png
summary: Hidden ways around authentication: hardcoded passwords, weakened cryptography, and compromised dependencies
medium_url: https://medium.com/@martinthoma/backdoors-10fa7a6aad27
---
<figure class="ai-generated">
    <a href="../images/2025/03/backdoors-1.jpg"><img src="../images/2025/03/backdoors-1.jpg" alt="Illustration of a glowing door in a wall made of green code" width="800" height="800"></a>
</figure>

A **backdoor** is a hidden method of bypassing a system’s authentication mechanism. It allows unauthorized access, often without the knowledge of the system owner. Backdoors can be introduced intentionally (e.g., for remote administration) or by attackers.

## Why it matters

In 2006, the US National Institute of Standards and Technology (NIST) published the standard NIST SP 800–90A, an algorithm for random number generation. The standard includes [Dual\_EC\_DRBG](https://en.wikipedia.org/wiki/Dual_EC_DRBG#Timeline_of_Dual_EC_DRBG), an algorithm with an **algorithmic** **weakness** that very likely allowed the NSA to break encryptions which made use of this random number generation algorithm. It’s a **cryptographic backdoor**.

In 2015, it was discovered that Juniper Networks’ Netscreen firewalls had **hardcoded passwords** ([source](https://www.theregister.com/2015/12/21/security_code_to_backdoor_juniper_firewalls_revealed_in_firmware/)).

In 2024, the [XZ Utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) was discovered by a professional software developer who wondered why a program used an [unexpected amount of processing power](https://theintercept.com/2024/04/03/linux-hack-xz-utils-backdoor/). We were lucky. This backdoor introduced a **vulnerability** to the code which would have allowed attackers to bypass the sshd authentication. That would have been a big deal as it’s so widespread across the internet.

## What can I do?

Leaking secrets is a common issue, especially for open source projects. It’s just easy to have a hardcoded password in the beginning of a project that is never removed. I’ve already written an article about how to deal with that:

[**Leaking Secrets** *How it happens and how you prevent it*](../leaking-secrets/)

The same tools allow you to search for secrets within your code.

When you want to find rootkits on your base-system, [rkhunter](https://en.wikipedia.org/wiki/Rkhunter) might be useful.

For containers, you might want to make them read-only:

[**Running Containers Read-Only - LinuxServer.io** *Welcome to the home of the LinuxServer.io documentation!*](https://docs.linuxserver.io/misc/read-only/)

The only action that helps to make sure your code doesn’t have backdoors is to do code reviews and audits.

<!-- series: appsec -->
