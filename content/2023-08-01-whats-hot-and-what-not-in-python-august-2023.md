---
layout: post
title: What’s hot and what’s not in Python, August 2023
slug: whats-hot-and-what-not-in-python-august-2023
lang: en
author: Martin Thoma
date: 2023-08-01 22:32
category: Code
tags: Python, PyPI
featured_image: logos/python.png
summary: An analysis of PyPI download statistics
medium_url: https://medium.com/@martinthoma/whats-hot-and-what-not-in-python-august-2023-2c3e5172109
---
The Python Package Index (PyPI) tracks the downloaded packages. I’ve checked the monthly statistics for the two time frames:

* 1st of June to 30th of June and
* 1st of July to 31st of July

and compared them.

It’s important to realize that download statistics do not tell you anything about the code quality and only give a small indication of popularity. The download statistics get pushed if people regularly download packages through their Continuous Integration (CI) systems for testing their own software. Being a dependency of a popular package certainly helps. And just being an indirect dependency by many packages is typically also not exciting. There is a reason why requests and boto3 are typically in the TOP-10.

## Top Newcomers

In the following, I tried to group packages if multiple newcomers are just the cause of another change.

1. № 134, downloaded 30232921x: [jsonschema-specifications](https://pypi.org/project/jsonschema-specifications/). That pulled [rpds-py](https://pypi.org/project/rpds-py/) and [referencing](https://pypi.org/project/referencing) up as well. And the reason it came up that quickly is because the [jsonschema](https://pypi.org/project/jsonschema/) package was popular before. Those [became a dependency in February](https://github.com/python-jsonschema/jsonschema/commit/bf94d57b2b6d77cc8057be295f077435f4d4020d), but only in July were the releases. Yes, multiple releases.
1. № 307, downloaded 12068823x: [**annotated-types**](https://pypi.org/project/annotated-types/) — [PEP-593](https://peps.python.org/pep-0593/) added `typing.Annotated`. Python is improved by “Python Enhancement Proposals” — short: PEPs. This package makes a PEP that was introduced in Python 3.9 usable for normal users. That is exciting 😍
1. № 1253, downloaded 1392567x: [google-re2](https://pypi.org/project/google-re2/), a drop-in replacement for the re module. It’s been on version 1.0 in 2020 already. I don’t know why it suddenly got such a boost in downloads. Likely because something from the Google Cloud packages now depends on it.
1. № 1539, downloaded 912974x: [wexpect](https://pypi.org/project/wexpect/), a Windows variant of [pexpect](https://pexpect.readthedocs.io/en/stable/). A module for spawning child applications. This one is even more confusing. It’s hardly a newcomer. I’m also not aware of any big packages now depending on it.
1. № 1921, downloaded 582748x: [LangSmith](https://pypi.org/project/langsmith/), a Python client for interacting with the [LangSmith platform](https://smith.langchain.com/). [LangChain](https://github.com/langchain-ai/langchain) is a tool for LLMs. You know, the ChatGPT hype.
1. № 2147, downloaded 467417x: [itables](https://pypi.org/project/itables/), Turn your Python DataFrames into Interactive Tables
1. № 2212, downloaded 443474x: [uproot3](https://pypi.org/project/uproot3/), is a reader and a writer of the [ROOT file format](https://root.cern/).
1. № 2220, downloaded 440534x: [awkward0](https://pypi.org/project/awkward0/) a pure Python+Numpy library for manipulating complex data structures as you would Numpy arrays
1. № 2240, downloaded 432486x: [coffea](https://pypi.org/project/coffea) is a package for the typical needs of a high-energy collider physics (HEP) experiment analysis
1. № 2247, downloaded 429644x: [boost-histogram](https://pypi.org/project/boost-histogram/) — Python bindings for Boost::Histogram.

## Top Trending

1. +4082, current rank is 282: [pydantic-core](https://pypi.org/project/pydantic-core/) — the data validation library [pydantic](https://pypi.org/project/pydantic/) released a 2.0 version which had heavy refactoring and tons of news / podcasts around it. pydantic is used by FastAPI and many other projects. If you don’t know it, it’s somewhat similar to attrs.
1. +2508, current rank is 2089: [awkward](https://pypi.org/project/awkward/) is a library for nested, variable-sized data. It’s in the [scikit-hep project](https://github.com/scikit-hep).
1. +2216, current rank is 637: [imdbpy](https://pypi.org/project/imdbpy/) and [cinemagoer](https://pypi.org/project/cinemagoer/). A Python package useful to retrieve and manage the data of the IMDb movie database about movies, people, characters and companies.
1. +2095, current rank is 1220: [logutils](https://pypi.org/project/logutils/) — handlers for the Python standard library’s logging package.
1. +2045, current rank is 2819: [types-pyserial](https://pypi.org/project/types-pyserial/), the type stubs for pyserial, a Python Serial Port Extension.
1. +1737, current rank is 3092: [pyobjc-framework-\*](https://pypi.org/project/pyobjc-framework-naturallanguage/) there are tons of libraries around macOS stuff.
1. +1714, current rank is 3237: [yapsy](https://pypi.org/project/yapsy/) is a library implementing the core mechanisms needed to build a plugin system into a wider application
1. +1664, current rank is 2168: [aiofile](https://pypi.org/project/aiofile/) — Real asynchronous file operations with asyncio support.
1. +1614, current rank is 452: [jupyter-lsp](https://pypi.org/project/jupyter-lsp/) — Multi-Language Server WebSocket proxy for your Jupyter
1. +1603, current rank is 2494: [rainbow-logging-handler](https://pypi.org/project/rainbow-logging-handler/)

I feel like the next time I do this, I need to (1) remove all packages from well-known organizations (2) remove packages on which other popular packages started to depend (3) remove packages which are dependencies of trending newcomers.

## Falling Fast

Packages in this category might need support. If you want to become a maintainer, here might be your chance :-)

1. -3338, current rank is 4255: [python-whois](https://pypi.org/project/python-whois/) — produce parsed WHOIS data for a given domain
1. -2547, current rank is 4963: [haralyzer](https://pypi.org/project/haralyzer/) — Using HAR Files To Analyze Web Pages.
1. -2489, current rank is 4907: [eyes-selenium](https://pypi.org/project/eyes-selenium/)
1. -2135, current rank is 4492: [browsermob-proxy](https://pypi.org/project/browsermob-proxy/)
1. -1881, current rank is 4704: [ssh-python](https://pypi.org/project/ssh-python/) — Bindings for libssh C library
1. -1687, current rank is 4227: [transparentpath](https://pypi.org/project/transparentpath/) use a GCS file system path as if it was local. GCS is Google Cloud Storage.
1. -1680, current rank is 3938: [robotframework-debuglibrary](https://pypi.org/project/robotframework-debuglibrary/)
1. -1660, current rank is 4759: [mozrunner](https://pypi.org/project/mozrunner/) (also [mozlog](https://pypi.org/project/mozlog/)), a supplemental standard library for Mozilla
1. -1461, current rank is 3612: [robotremoteserver](https://pypi.org/project/robotremoteserver/)
1. -1426, current rank is 4841: [openpyxl-stubs](https://pypi.org/project/openpyxl-stubs/) is actually [one of my libraries](https://github.com/MartinThoma/openpyxl-stubs) 😅 I haven’t taken care of it as I lost interest. I hope the library adds type annotations on their own.

## Bonus: A small PDF update

I care about the PDF ecosystem, so here is how the packages developed:

pypdf family:

* **pypdf**: +163, rank now is 1481 🎉 Maybe we make this pass PyPDF2 this year 🤞
* **pypdf2**: -31, rank now is 771. The decline is expected in favor of pypdf.
* **pypdf3**: +168, rank now is 4291. I don’t get why people continue to use that.

Text extraction / manipulation:

* **pdfminer-six**: -49, rank now is 970
* **pdfminer**: -133, rank now is 3508
* **pdfplumber**: -14, rank now is 2525
* **pymupdf**: +154, rank now is 1658. Well-deserved, it’s an excellent library.
* **pikepdf**: -154, rank now is 1970. Also a pretty good library
* **pdfrw**: -297, rank now is 3689

Generators:

* **reportlab**: -33, rank now is 886
* **fpdf**: -121, rank now is 1527
* **fpdf2**: -308, rank now is 3294 — oh no 😨 People should go to fpdf2. I wonder what they are using now
* **weasyprint**: -123, rank now is 1595
* **xhtml2pdf**: -68, rank now is 2170

Others:

* pdf2image: +19, rank now is 1697
* pdfkit: -54, rank now is 1705
* pyhanko: +117, rank now is 2396. Signing of PDFs.
* tabula-py: -95, rank now is 3303
* camelot-py: -49, rank now is 4078
* img2pdf: -716, rank now is 3457
* sphinxcontrib-svg2pdfconverter: -397, rank now is 4146
* pypdftk: -1332, rank now is 4621

You can get more insights in

[**The Python PDF Ecosystem in 2023** *Which libraries should you use for which use case?*](../the-python-pdf-ecosystem-in-2023/)
