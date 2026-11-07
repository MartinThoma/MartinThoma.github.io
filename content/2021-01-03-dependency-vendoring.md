---
layout: post
title: Dependency Vendoring
slug: dependency-vendoring
lang: en
author: Martin Thoma
date: 2021-01-03 23:49
category: Code
tags: Software Engineering, Packaging
featured_image: logos/development.png
summary: What it is and why it’s done
medium_url: https://medium.com/@martinthoma/dependency-vendoring-dd765be75655
---
Vendoring in Software Engineering is the act of including 3rd party software directly in your product. The alternative is to let a dependency management tool install it.

One reason for vendoring is to avoid version conflicts when the dependencies are installed. For example, your `amazing` software could require the dependency `A` in version `3.2.1`, but the user needs `A==3.4.0`. Hence the version `amazing` needs conflicts with the version the user needs for something else. This is especially a problem if your software is a library. Maybe the user needs the library `A==3.4.0` in their project AND `amazing` as well. This issue is solved when `amazing` also contains `A` and thus does not trigger the dependency management tool.

However, there is a huge downside to vendoring: You have to make sure you add all security updates and bugfixes of `A` to your software. If `A` has a vulnerability, your software has as well. You need to release your software every time `A` releases a security update or a bugfix.

In the Python ecosystem, vendoring is rare, but some important packages do it: `pip` vendors its dependencies in `pip._vendor`, `setuptools` in `setuptools._vendor`, and I just stumbled over it in `dynaconf`.
