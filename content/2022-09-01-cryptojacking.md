---
layout: post
title: Cryptojacking 😈
slug: cryptojacking
lang: en
author: Martin Thoma
date: 2022-09-01 09:19
category: Security
tags: Security, AppSec, Cryptocurrency
featured_image: logos/cybersecurity.png
summary: What it is, why it matters, how it’s done, and how to prevent cryptojacking
medium_url: https://medium.com/@martinthoma/cryptojacking-55a73622fb6d
status: draft
---
Cryptojacking is the unexpected and unwanted use of computational resources to mine crypto-currencies. It’s hijacking resources to mine crypto-currencies.

Don’t confuse it with ransomware doing crypto-locking. Crypto-locking prevents you from accessing your data and uses blackmailing to get money. Cryptojacking uses your computational resources like a parasite, but they don’t touch your data and they might even try to not use too much in order to stay undetected for longer.

Crypto-currencies such as Bitcoin (BTC) and Ethereum (ETH) have gained a lot of popularity in 2021 / 2022. Before 2020, they only were used by few people and the total market capitalization was pretty low. For this reason there wasn’t a lot of money to make with them.

Let me give you a Tweet-length explanation how crypto-currencies allow you to convert computational resources into money: Every crypto-currency needs to ensure that there is a shared ground truth of who owns what over a large network of independent nodes (a consensus protocol). The clearest way how to do that in a secure manner is called “Proof of Work” (PoW): You make a computationally hard task and the first one who solves the task may change the state of the database. To incentivize people, you allow people to spend a bit more of the cryptocurrency than previously existed. The person who solves the computationally hard work is called the “miner” and the “mining reward” is how they get money.

Monero was pretty popular to mine crypto in cryptojacking attacks. One reason might be that most serious Bitcoin / Ethereum mining use so much computational power via GPUs and custom chips (ASICs) that cryptojacking would not be cost-effective enough.

More about that in my articles:

[**The Blockchain** *An Introduction to Blockchain, Bitcoin ₿, and related concepts*](../blockchain/)

[**Blockchain 101** *Transactions, Blocks, Consensus, Protocols, and Networks*](../blockchain-101/)

## Why Cryptojacking matters

* 2017: Starbucks cafe’s wi-fi made computers mine crypto-currency ([source](https://www.bbc.com/news/technology-42338754))
* 2018: Hackers Enlisted Tesla’s Public Cloud to Mine Cryptocurrency ([source](https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/))
* 2018: Unsecured AWS led to cryptojacking attack on LA Times ([source](https://nakedsecurity.sophos.com/2018/02/27/unsecured-aws-led-to-cryptojacking-attack-on-la-times/))
* 2020: AWS Cryptojacking Worm Spreads Through the Cloud ([source](https://threatpost.com/aws-cryptojacking-worm-cloud/158427/))
* 2021: \$45,000 AWS Crypto-Mining Hack Generates \$800 of Monero ([source](https://www.tomshardware.com/news/aws-45000-usd-bill-for-crypto-mining-hack))

## How are Cryptojacking attacks executed?

There are four simple and common ways:

* **JavaScript injection in Websites**: If an attacker can make your website include JavaScript, they can make all users of that website mine crypto-currencies for them. In-Browser cryptojacking is inefficient, but it’s possible. That’s what happened to Starbucks users in 2017. [Coinhive was famous for being used by cryptojackers](https://www.zdnet.com/article/coinhive-cryptojacking-service-to-shut-down-in-march-2019/).
* **Leaked Cloud Secrets**: People often accidentally put their AWS secrets into public Github repositories. They might delete the secrets eventually, but they forget that they are still in the git history. Attackers can scrape Github (or other source code hosting sites like Gitlab) and use them. Cryptojacking provides them with a simple way to convert those keys to money without blackmailing.
* **Misconfigured servers**: Some servers are configured in the wrong way or simply don’t require passwords where they should. This can allow attackers to execute arbitrary code. Maybe it doesn’t directly allow access to confidential data, e.g. when it’s a test system. But with cryptojacking the attacker does not have to steal data to make money. Tesla had the issue of a misconfigured server which was detected in 2018.
* **Supply-chain attacks**: Instead of going directly for your services, attackers might target commonly used software and include cryptominers in them. Malicious open source maintainers could even include them directly.

## What can I do to prevent Cryptojacking attacks?

There are two sides to defending against cryptojacking: **Server admins** and **website users**.

When admins are affected by cryptojacking, something else had to be severely broken beforehand. You should have **billing alerts**, but I would not do anything specifically against cryptojacking. In the end, losing money due to too many resources being used might be way cheaper and easier to detect than leaking your customers’ data or being blackmailed as somebody can shut down your servers.

If somebody was able to include a cryptominer into your website, you have an XSS vulnerability:

[**Cross-site Scripting (XSS) 😈** *What it is, why it matters, how they are executed, how to prevent XSS attacks — and how to create a cookie stealer!*](../xss/)

You should deal with that in the same way as you would with other XSS vulnerabilities. For a business, the cryptojacking attack is way less damaging and easier to detect than leaking customer / business secrets.

As a **user**, it’s very annoying if websites use too many resources. No matter for which reason. But it’s only annoying and doesn’t really do harm. You might run out of battery sooner and your screen might freeze. Ad-blockers might help with that, e.g. [this blocklist](https://firebog.net/) seems to have cryptominers on it. However, the location of the cryptominer can easily change and also fingerprints for those scripts can easily be adjusted. The only effective way to prevent cryptomining is to disable JavaScript, but that makes most of the internet unusable nowadays.

## How to identify Cryptojacking

You can identify cryptojacking by extreme CPU usage. The network traffic might also help ([source](https://www.sciencedirect.com/science/article/abs/pii/S1742287618303359), [source](https://jis-eurasipjournals.springeropen.com/articles/10.1186/s13635-021-00126-1)). Code-complexity was also successfully used to detect in-browser cryptojacking ([source](https://arxiv.org/pdf/1809.02152.pdf)).

<!-- series: appsec -->
