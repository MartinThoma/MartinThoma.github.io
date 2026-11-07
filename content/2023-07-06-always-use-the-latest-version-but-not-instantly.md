---
layout: post
title: Always use the latest version, but not instantly
slug: always-use-the-latest-version-but-not-instantly
lang: en
author: Martin Thoma
date: 2023-07-06 19:49
category: Code
tags: Software Engineering, Security, Software Versioning
featured_image: logos/development.png
summary: People don’t make security advisories. They might not even explicitly state that there was/is a security issue.
medium_url: https://medium.com/@martinthoma/always-use-the-latest-version-but-not-instantly-7ecf707cc31b
---
This is a warning to my fellow software developers. I’m writing this article as the current maintainer of pypdf and PyPDF2, probably the most widely used PDF packages in the Python ecosystem. At the same time, I’m working as a lead developer at a FinTech company and was working as a software engineer consultant for several years.

My experience is mainly from the Python ecosystem, but the same ideas are true for any programming language with anonymously developed and shared packages. That especially includes JavaScript, Java, PHP, Ruby, and Rust.

## “Always the latest” or “don’t touch running systems”?

Almost all software developers use third-party libraries to create their software systems. It’s necessary. At the same time, I think it’s completely impossible for anybody to review all the code properly. It’s already hard to just check the changelog thoroughly to make sure the updates don’t break anything in your own software.

In that environment, you might be tempted to stick with **the “don’t touch running systems” philosophy**. You only make an update when it’s absolutely necessary. That means when you need new functionality, when the package you use does not work with other new packages, or when there is a bug or security issue that affects you.

In contrast, **the “always use the latest version” philosophy** is to always try to update. Try to use the latest version… but not right away. In this article I’ll explain why I strongly suggest going with this.

## № 1: Small updates are less painful than big ones

Software evolves over time. When you make the small updates, you might not even recognize the tiny adjustments you make to your software.

Professional projects like Django have extensive CHANGELOGs and [a deprecation process](https://docs.djangoproject.com/en/dev/internals/release-process/#deprecation-policy). pypdf has [one as well](https://pypdf.readthedocs.io/en/latest/dev/deprecations.html). If you look at the warnings, you will be able to make the change before it breaks stuff. That doesn’t work if you upgrade several major versions at once.

## № 2: Security implications are not always clear

Parsing PDF files is pretty hard as the standard is so big. PDF viewers are not strict about the standard, just like browsers are not strict about the HTML standard either. That raises the expectation of users that PDF libraries also handle broken PDFs gracefully, if possible.

In that context, pypdf had infinite loops a couple of times. If you use them in a script that you execute, it’s not too bad. You just interrupt the script and you’re fine. But if you’re using it on a web server and people can trigger this, it can use your CPU. That raises the risk of a Denial of Service attack and thus breaking Availability.

When I became the maintainer of pypdf, it was not immediately clear to me that an infinite loop would have this implication. Also, what should I do with that knowledge?

Now I know that I need to [create a Security Advisory](https://docs.github.com/en/code-security/security-advisories/repository-security-advisories/about-repository-security-advisories) ([example](https://github.com/py-pdf/pypdf/security/advisories/GHSA-4vvm-4w3v-6mr8)): This will let your users know that there is a potentially severe issue. Attackers will also know, but they might also have that knowledge already. The security advisory will also make Dependabot and similar tools trigger an update alert for your users.

## № 3: Mixed updates

There are tons of projects out there which have only one, maybe two regularly contributing open source developers. They don’t have the resources to manage multiple major versions. If there is a known issue, it’s fixed in the latest version. Previous versions might also be affected, but don’t receive an update.

Big projects like Django and Ubuntu have the resources to support multiple versions. Small ones don’t. And even for the big ones I would be a bit suspicious if that always works.

## Why I don’t instantly use the latest version

Testing is hard and the test coverage of projects is mixed. For huge projects like Python and Django I typically wait until the first patch-update is out. So I wouldn’t use `django==5.0.0`, but wait for `django==5.0.1`.

That way others have stumbled over the issues and the community fixed them before I need to do it. At least on my production systems, I don’t want those surprises. On testing systems or private projects I prefer to take the latest and greatest 😄
