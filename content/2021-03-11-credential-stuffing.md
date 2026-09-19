---
layout: post
title: Credential Stuffing 😈🐝
slug: credential-stuffing
lang: en
author: Martin Thoma
date: 2021-03-11 20:00
category: Security
tags: Software Development, Programming, Cybersecurity, OWASP, Security
featured_image: logos/cybersecurity.png
medium_url: https://levelup.gitconnected.com/credential-stuffing-ff58ee8c3320
---
![Photo by [Max van den Oetelaar](https://unsplash.com/@maxvdo?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](../images/2021/03/credential-stuffing-1.jpg)*Photo by [Max van den Oetelaar](https://unsplash.com/@maxvdo?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Credential stuffing is a brute-force attack on a services’ user accounts. Not one specific account, but many. Typically by using credentials that were found in other hacks. As a user, you can see via [haveibeenpawned.com](https://haveibeenpwned.com/) if one of your accounts was compromised. Most likely, it was. Let’s learn what you can do!

## Why you should care

* Credential Stuffing is part of “Broken Authentication” and thus #2 in the **OWASP Top 10** ([source](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication))
* 2020: $3.5 million in fraudulent check withdrawals with credential stuffing ([more details](https://www.zdnet.com/article/fbi-says-credential-stuffing-attacks-are-behind-some-recent-bank-hacks/))
* 2020: About 500,000 Zoom users credentials were found with credential stuffing ([source](https://www.forbes.com/sites/daveywinder/2020/04/28/zoom-gets-stuffed-heres-how-hackers-got-hold-of-500000-passwords/))
* 2020: “Retail, travel, and hospitality industries attracted a startling 63% of credential stuffing attacks” [according to Akamai.](https://www.akamai.com/us/en/resources/our-thinking/state-of-the-internet-report/global-state-of-the-internet-security-ddos-attack-reports.jsp)
* 2021: AVM (FritzBox) registers a lot of credential stuffing attacks ([source](https://t3n.de/news/avm-angriffe-router-fritzbox-1363050/))

## How does a credential stuffing attack work?

1. The attacker gets a **list of valid credentials**, e.g. (username, password) for millions of people. [There are many leaks](https://haveibeenpwned.com/).
2. The attacker **tries them** on big services (Gmail, Facebook, Twitter, Banks, Reddit, …)

That’s it. It’s really trivial. Credential stuffing does not target you personally, but a lot of people at the same time. But that doesn’t help you when your bank account is empty at the end of the day, does it?

## How can I defend against a credential stuffing attack?

As a user, there are two perfect defense measures:

1. **Strong Passwords**: Good passwords might look different than you think. But [it’s easy to generate memorizable strong passwords](https://medium.com/geekculture/what-is-a-secure-password-97263aeedea9).
2. **Unique Passwords**: Don’t share passwords among services. Never.

To fulfill both in a convenient way, you should use a password manager. A third point that helps is to use multi-factor authentication (MFA). Having at least a second factor (2FA) goes a long way. However, the attacker most likely learns which passwords are correct and can work on breaking the second factor, e.g. by SIM swapping.

As a service provider, the defenses are not perfect and more complicated:

* **Rate Limiting**: If a single IP makes too many invalid password attempts, slow that IP down. For example, ask them to [solve a CAPTCHA](../captcha/) first. Or tell them that they are not allowed to log in for the next 30 seconds. Just be aware that this could also block valid users, e.g. at schools or other bigger open networks.
* **Web Application Firewalls (WAF)**: Full disclaimer here: I don’t have practical experience here. I’ve heard about “Proactive Bot Defense” which might be interesting for other attack scenarios as well. However, it certainly also has the issues to detect all attacks (False-Negatives) and to block only attacks (False-Positives).
* **Two-factor authentication (2FA)**: Forcing the user to use a second factor makes it a lot less likely that credential stuffing works, even if the user shared passwords with a vulnerable service and even when the password is weak.
* **Single-Sign-On (SSO)**: Letting another service handle the authentication side-steps all of those hassles. One variant which is well-known is “social login”. That is simply SSO by big social websites like Facebook, Twitter, Github, or LinkedIn.
* **Check users' passwords for breaches**: [haveibeenpawned](https://haveibeenpwned.com/Passwords) allows you to check if credential combinations are in a breach.

There are also some specific points to make the life of bot-developers harder, e.g. requiring JavaScript, blocking headless browsers, or blocking traffic from AWS. [Jarrod Overson](https://medium.com/u/a19804ea02f3) has written a very nice article about this:

[**10 Tips To Stop Credential Stuffing Attacks**
*10 steps you should take before buying an anti-automation service (+ 1 bonus tip).*jsoverson.medium.com](https://jsoverson.medium.com/10-tips-to-stop-credential-stuffing-attacks-db249cac6428)

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
* Part 11: [DOS via a Billion Laughs](../billion-laughs-dos/) 😈
* Part 12: [Full Disk Encryption](../full-disk-encryption/) 😇
* Part 13: [Insecure Deserialization](../insecure-deserialization/) 😈🐝
* Part 14: [Docker Security](../docker-security/) 😇
* Part 15: **Credential Stuffing** 😈🐝
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
