---
layout: post
title: Python Terminology: Distribution vs Package vs Module
slug: python-terminology-distribution-vs-package-vs-module
lang: en
author: Martin Thoma
date: 2023-01-28 13:57
category: Code
tags: Python, Packaging, Terminology
featured_image: logos/python.png
summary: What distributions, packages, and modules are in Python
medium_url: https://medium.com/@martinthoma/python-terminology-distribution-vs-package-vs-module-52feb40b4b97
status: draft
---
<figure>
    <a href="../images/2023/01/python-terminology-distribution-vs-package-vs-module-1.jpg"><img src="../images/2023/01/python-terminology-distribution-vs-package-vs-module-1.jpg" alt="Scrabble tiles on a wooden table forming the crossing words PACKAGE, PYTHON, DISTRIBUTION and MODULE" width="800" height="406"></a>
</figure>

A Python **distribution** is an archive file that contains one or more Python packages. The distribution file is what the end-user will download and install. Typically, it contains just one package.

There are two common types of distributions: Source distributions and the wheel binary format.

A Python **package** is an importable directory.

A Python **module** is a Python source code file. You can import a module. Most modules are in packages.

## Sources

* [PEP 561](https://peps.python.org/pep-0561/#definition-of-terms): Distributing and Packaging Type Information
* [PEP 427](https://peps.python.org/pep-0427/): The Wheel Binary Package Format 1.0
