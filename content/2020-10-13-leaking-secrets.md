---
layout: post
title: Leaking Secrets 😇
slug: leaking-secrets
URL: https://levelup.gitconnected.com/leaking-secrets-240a3484cb80
author: Martin Thoma
date: 2020-10-13 20:00
category: My bits and bytes
tags: InfoSec, AppSec, Security, Cybersecurity
featured_image: logos/cybersecurity.png
---
One of the worst mistakes one can make in application security is to publicly post secrets. That can be API keys, database credentials, service tokens, or private keys for asymmetric cryptography such as RSA as used for GPG.

It’s best to prevent leaking credentials completely, but if it’s done you need to change them directly. You cannot hope that nobody has noticed it. People are scanning the public repositories for committed secrets.

## Why it Matters

Leaking secrets and credentials happens more often than one would think. I’m a bit astonished that we don’t see this more often in news articles, but there are certainly some hacks that could be traced back to leaked secrets:

* **2017**: Uber paid $100,000 to hackers who got personal data of 57 million customers.
* **2019**: Researchers find over 200,000 unique secrets on GitHub. They describe their methodology and findings in “[How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04B-3_Meli_paper.pdf)”
* **2020**: Daimlers' internal Gitlab was open to the public ([source](https://www.zdnet.com/article/mercedes-benz-onboard-logic-unit-olu-source-code-leaks-online/)). If there were any credentials in any of the repositories, they are now public as well. This is why [Defence in Depth](https://en.wikipedia.org/wiki/Defence_in_depth) makes sense. Don’t store your secrets in a repository, even if the repository is private.

## How leaking of secrets happens

It’s a mixture of missing knowledge, laziness, and human error. If people don’t know how to store the secrets properly, they just store them in a way that they know of. Even if people know how to do it well, it’s just so much simpler to directly copy the secret in the repository. And, of course, adding stuff that was not intended to be added also happens.

**Adding secrets to a public repository** is the most obvious mistake one can do. **Adding secrets to log messages** is more indirect and should not cause an immediate issue. However, it can allow a multi-step attack. For this reason “defense in depth” makes sense and thus secrets should not be part of log messages. It’s not even necessary that an attacker gets direct access to the log files. Maybe a developer shares a part of the logs publicly to investigate an issue. The problem is that people don’t tend to think of logs as a security-critical part of the software landscape.

## How can I prevent leaking secrets?

First, you need to make sure that people don’t see a need to use secrets in an unsafe way any longer. Then you can make it harder to commit secrets via **pre-commit** hooks. Finally, you **check on the server-side** when secrets were added.

### Logging

Either don’t log environment variables at all or make REALLY sure that there are no secrets inside. You can also blacklist patterns as [Joe Crobak](undefined) showed in his post “[Seven Best Practices for Keeping Sensitive Data Out of Logs](https://medium.com/@joecrobak/seven-best-practices-for-keeping-sensitive-data-out-of-logs-3d7bbd12904)”.

### Storing Secrets Locally: Direnv

[direnv](https://direnv.net/) is a shell extension that makes your shell execute an .envrc file if you are in the folder or a subfolder. Such a file can look like this:

```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-west-2
```

Make sure the .envrc file is kept private by adding it to the .gitignore file.

Wherever people would have used their secrets in the code, they now can use the environment variable instead.

Storing secrets in environment variables is far from being optimal as every single process can easily access them. However, it is better than storing them in a file that is accessible even to other systems. In the worst case even to the public internet.

### Pre-commit hooks

[pre-commit](https://pre-commit.com/) is an application that helps you to apply git hooks. Those are executed before code is added to the git repository.

You can make sure that no AWS credentials or private keys are added to the repository by creating the following .pre-commit-config.yaml file:

```yaml
repos:
-   repo: [https://github.com/pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    rev: v3.2.0
    hooks:
    -   id: detect-aws-credentials
    -   id: detect-private-key
-   repo: git@github.com:Yelp/detect-secrets
    rev: v0.14.3
    hooks:
    -   id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: .*/tests/.*
```

Then execute pre-commit install and you’re done 🙂

Yelps [**detect-secrets**](https://github.com/Yelp/detect-secrets) tries to find secrets in source code by finding high-entropy strings and the others look for common file formats/strings.

There are [many other cool things](https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e) you can do with pre-commit.

### Storing Secrets Server-Side: Environment Variables

There are many secrets vault solutions, including the ones of the source code hosting providers:

* [AWS SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
* [Azure Key Vault](https://azure.microsoft.com/de-de/services/key-vault/)
* [GitlabCI Environment Variables](https://docs.gitlab.com/ee/ci/variables/) and [Hashi Corp Vault Server for Secrets](https://docs.gitlab.com/ee/ci/secrets/)
* [GitHub](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets): Encrypted Secrets
* [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/): Secured Variables

### Storing Secrets Server-Side: Vaults

Supplying the secrets via environment variables has two major drawbacks: (1) Every process can access them (2) Developers might want to log environment variables and thus leak secrets into the logs.

Having a dedicated store for secrets and only getting the secrets once it’s necessary is one solution to this problem.

AWS SSM is a very common solution. Here is how you use it with Python:

```python
import boto3


def get_ssm_param(name: str) -> str:
    client = boto3.client("ssm")
    param = client.get_parameter(Name=name, WithDecryption=True)
    return param["Parameter"]["Value"]
```

### Source Hosting Secrets Detection

Most source hosting services offer a possibility to check for leaked secrets. [GitLab](https://docs.gitlab.com/ee/user/application_security/secret_detection/) calls it “secret detection”, [GitHub](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning) calls it “secret scanning” and [GitGuardian](https://www.gitguardian.com/) offers secret detection & remediation.

One can integrate Yelps [secret-detection](https://github.com/Yelp/detect-secrets) into the CI pipeline. For Python, the SAST tool bandit can also be integrated into the CI pipeline. It offers [basic secret detection](https://bandit.readthedocs.io/en/latest/plugins/b105_hardcoded_password_string.html). Just remember: If the CI pipeline fails because of a found secret, you have to change that secret.

## Testing the Past

Making sure that new commits are safe is good, but you also need to know if there was an incident in the past, before the security improvements were introduced. There are two tools to help you:

[**GitLeaks**](https://github.com/zricethezav/gitleaks) scans your whole repository for leaked secrets. This includes credentials that were committed and removed but are still in the commit history.

Here is how you install it on Linux:

```bash
# You can also go to
# [https://github.com/zricethezav/gitleaks/releases](https://github.com/zricethezav/gitleaks/releases)
# and download the version you need in the browser
$ wget [https://github.com/zricethezav/gitleaks/releases/download/v6.1.2/gitleaks-linux-amd64](https://github.com/zricethezav/gitleaks/releases/download/v6.1.2/gitleaks-linux-amd64)

$ mv gitleaks-linux-amd64 gitleaks
$ chmod +x gitleaks
$ sudo mv gitleaks /usr/local/bin/

$ cd your-repo
$ gitleaks --repo=. -v
INFO[2020-10-13T17:38:49+02:00] cloning... .
Enumerating objects: 115, done.
Counting objects: 100% (115/115), done.
Compressing objects: 100% (42/42), done.
Total 115 (delta 68), reused 115 (delta 68)
INFO[2020-10-13T17:38:49+02:00] No leaks detected. 29 commits scanned in 111 milliseconds 984 microseconds
```

[**Keyhacks**](https://github.com/streaak/keyhacks#AWS-Access-Key-ID-and-Secret) is a project which shows you if leaked keys are still valid and what an attacker could do with them.

[**HaveIbeenPwned**](https://haveibeenpwned.com/) is interesting for your private accounts. You can register and will receive an email if your email appears in a data leak. It happens so often 😱 For this reason: **Don’t re-use passwords! A re-used password is a leaked password!**


## A note about environment Variables

Environment variables are by far not bullet-proof. Several malicious 3rd-party
packages simply send the hostname with environment variables to a server ([source](https://github.com/rsc-dev/pypi_malware#malware-packages)).


## What’s next?

In this series about application security (AppSec) we already explained some of the techniques of the attackers 😈 and also techniques of the defenders 😇:

* Part 1: [SQL Injections](https://medium.com/faun/sql-injections-e8bc9a14c95) 😈
* Part 2: [Don’t leak Secrets](https://levelup.gitconnected.com/leaking-secrets-240a3484cb80) 😇
* Part 3: [Cross-Site Scripting (XSS)](https://levelup.gitconnected.com/cross-site-scripting-xss-fd374ce71b2f) 😈
* Part 4: [Password Hashing](https://levelup.gitconnected.com/password-hashing-eb3b97684636) 😇
* Part 5: [ZIP Bombs](https://medium.com/bugbountywriteup/zip-bombs-30337a1b0112) 😈
* Part 6: [CAPTCHA](https://medium.com/plain-and-simple/captcha-500991bd90a3) 😇
* Part 7: [Email Spoofing](https://medium.com/bugbountywriteup/email-spoofing-9da8d33406bf)

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
