---
layout: post
title: Python is interpreted
slug: python-is-interpreted
author: Martin Thoma
date: 2020-05-20 20:00
category: Code
tags: Python
featured_image: logos/python.png
---
Python is interpreted. Python is a scripting language. I hear those two
statements pretty often when people want to say that Python is slow or that
Python is not suited for large systems. In this article I want to dispel those myths.

## Interpreted Language

What does it mean to say Python "is" an interpreted language? If you mean that Python is usually interpreted, that statement is correct. If you mean that Python is always interpreted, you are wrong[^6].

Usually, this comes with the connotation that Python is slow.

## Scripting Language

Next, what does it mean to say Python "is" a scripting language. According to Wikipedia:
> A scripting or script language is a programming language for a special run-time environment that automates the execution of tasks

That sound a lot like "interpreted language" to me. However, later in the article you can read

> with the term "script" often used for small programs (up to a few thousand lines of code)

Which leads to the myth that you can't build complex systems with Python.


## Myth: Python is Slow

What people usually mean with that statement is that raw execution speed is low.

### Speed is not Everything

However, they tend to forget other important properties like development speed,
ease to find developers, flexibility of the built systems to adjust for future
changes.

A case in point is this claim about the speed of YouTube developers ([ycombinator referencing "Python Interviews" by Mike Driscoll](https://news.ycombinator.com/item?id=16674628)). The fact that Python is well-suited for rapid prototyping is also appreciated at CERN[4^]. Same for Quora[5^].

### Raw Number-Crunching

Python has a lot of awesome libraries. Three of them help you with raw number crunching:

* **Numpy and Scipy**: Two battle-proven libaries which build on [BLAS libraries](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms). So the computationally heavy stuff is executed in highly optimized libraries which are written in Fortran.
* **Tensorflow / PyTorch**: Both libraries heavily rely on [CUDA](https://en.wikipedia.org/wiki/CUDA) and CuDNN, meaning the code which does the number cruniching is executed on the GPU. No Python involved.

## Myth: Python can use multiple cores

... because of the [GIL](https://en.wikipedia.org/wiki/Global_interpreter_lock).
That is just plain wrong. Have a look at my [asyncio article](https://martin-thoma.com/asyncio/)
to get an overview over concurrency in Python.

## Myth: Python cannot be used in big systems

Large systems might not need single heavy number crunching like BLAS libraries do. They might (a) have just "organizational complexity", meaning a lot of business logic or (b) a lot of single small requests comming into a web service.

There are a lot of [pages](https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites) which say "Python is used at website XY". However,
it's pretty hard to tell where and how exactly Python is used. It is a pretty
awesome language for writing "glue code", meaning code which helps to keep
things together. It's also nice for ad-hoc stuff which could mean that it is
only used for that. But, and that is the point of this paragraph, you can also
build big systems with Python. Here are some examples:

* **Instagram** uses Django (sources: [2011](https://instagram-engineering.com/what-powers-instagram-hundreds-of-instances-dozens-of-technologies-adf2e22da2ad), [2016](https://instagram-engineering.com/web-service-efficiency-at-instagram-with-python-4976d078e366), [2017](https://instagram-engineering.com/copy-on-write-friendly-python-garbage-collection-ad6ed5233ddf)): Instagram is at place 29 of the gloally most popular websites ([Alexa, April 2020](https://web.archive.org/web/20200416015659/https://www.alexa.com/topsites)). The fact that Instagram uses Django for their website shows two things: You can build complex systems using Python and you can build systems that scale.
* **Pinterest** uses Flask and Django ([Quora 2015](https://www.quora.com/What-challenges-has-Pinterest-encountered-with-Flask/answer/Steve-Cohen?srid=hXZd&share=1) by [Steve Cohen](https://www.linkedin.com/in/icecreamcohen/)): Pinterest is also one of the 500 most-visited websites on earth.
* **Facebook** ([2016](https://engineering.fb.com/production-engineering/python-in-production-engineering/)): A lot of places, but all seem not super huge. Facebook has released the [Tornado Webserver](https://en.wikipedia.org/wiki/Tornado_(web_server)) which they seemed to have used for their real-time updates[2^].
* **Dropbox** makes heavy use of Python. They had Guido van Rossum working for them for quite a while and in 2019 they put a lot of effort in 2019 to update their code: [Our journey to type checking 4 million lines of Python](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)
* **Netflix** also uses Python in [many places](https://netflixtechblog.com/python-at-netflix-bba45dae649e).

Other big players where I have seen claims, but no reliable source:

* Yahoo Maps, Yahoo Groups [1^]
* Google[1^] [3^]: I see this menioned all the time and you can find job postings for this, but no details what Google uses Python for.
* YouTube: [1^], [3^]

## How to make Python Fast

I will likely write way more about this, but here are some core ideas:

1. **Analyze**: Where do you spend most of your execution time. Is it mainly waiting for I/O? Then look at my [asyncio article](https://martin-thoma.com/asyncio/).
2. **Use libraries**: Python has a lot of awesome libraries which are well-maintaned. It takes a while to figure out which ones exist, but Numpy, Scipy, Tensorflow, PyTorch, Flask, Django, nltk, [scikit-learn](https://scikit-learn.org/stable/), [spacy](https://spacy.io/). And learn how to use them correctly. I had a 96x speedup just for using numpy for matrix multiplication. I had a 46x speedup by using numpy and a vectorized solution. Still pure Python in both cases.
3. **Interpreters**: You don't need to use the standard interpreter. [PyPy](https://www.pypy.org/) might be way faster due to JIT compilation.
4. **C-Bindings**: If Python is to slow for a specific task, you don't need to abandon Python. Cython, ctypes, cffi, c extension and pybind11 are some of the options you have.


## How to build big Systems with Python

A lot of the answer is not Python specific and would require way more than just this small part of the article. Some tiny hints which help:

* Coding Standards: [pre-commit](https://pre-commit.com/), [black](https://github.com/psf/black), [flake8](https://flake8.pycqa.org/en/latest/)
* [Type hints](https://docs.python.org/3/library/typing.html) and [mypy](http://mypy-lang.org/) for type checking
* Testing: [pytest](https://docs.pytest.org/en/latest/)

## Footnotes

[1^]: Python.org wiki: [Organizations using Python](https://wiki.python.org/moin/OrganizationsUsingPython)
[2^]: David Recordon: [Tornado: Facebook's Real-Time Web Framework for Python](https://developers.facebook.com/blog/post/301), 2018.
[3^]: [Python Quotes](https://www.python.org/about/quotes/)
[4^]: [Python : The Holy Grail of Programming](http://cdsweb.cern.ch/journal/CERNBulletin/2006/31/News%20Articles/974627?ln=en), 2006.
[5^]: [Adam D'Angelo](https://en.wikipedia.org/wiki/Adam_D%27Angelo): [Why did Quora choose Python for its development?](https://www.quora.com/Why-did-Quora-choose-Python-for-its-development-What-technological-challenges-did-the-founders-face-before-they-decided-to-go-with-Python-rather-than-PHP), 2014.
[6^]: Ramchandra Apte: [Is it feasible to compile Python to machine code?](https://stackoverflow.com/a/11415005/562769), 2012.
