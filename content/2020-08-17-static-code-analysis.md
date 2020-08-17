---
layout: post
title: Static Code Analysis for Python
slug: static-code-analysis
author: Martin Thoma
date: 2020-08-17 20:00
category: Code
tags: Unit Testing, Flake8, mypy
featured_image: logos/static-code-analysis.png
---
Static code analysis looks at the code without executing it. It is usually extremely fast to execute, requires little effort to add to your workflow, and can uncover common mistakes. The only downside is that it is not tailored towards your code.

In this article, you will learn how to perform various types of static code analysis in Python. While the article focuses on Python, the types of analysis can be done in any programming language.


## Code Complexity

![Photo by [John Barkiple](https://unsplash.com/@barkiple?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10368/0*hpBpO29k15vDdmHJ)*Photo by [John Barkiple](https://unsplash.com/@barkiple?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

One way to measure code complexity is the [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity), also called McCabe complexity as defined in [A Complexity Measure](https://books.google.de/books?id=vtNWAAAAMAAJ&pg=PA3&redir_esc=y):

$$CC = E - N + 2 \cdot P$$

where N is the number of nodes in the control flow graph, E is the number of edges and P is the number of condition-nodes (if-statements, while/for loops).

You can calculate it in Python with [radon](https://pypi.org/project/radon/):

```shell
$ pip install radon
$ radon cc mpu/aws.py -s
mpu/aws.py
    F 85:0 s3_download - B (6)
    F 16:0 list_files - A (3)
    F 165:0 _s3_path_split - A (2)
    F 46:0 s3_read - A (1)
    F 141:0 s3_upload - A (1)
    C 77:0 ExistsStrategy - A (1)
```

The first letter shows the **type of block** (F for function, C for class). Then radon gives the **line number**, the **name** of the class/function, a **grade** (A, B, C, D, E, or F), and the actual **complexity as a number**. Typically, a complexity below 10 is ok. [The most complex part of scipy](https://github.com/scipy/scipy/blob/master/scipy/sparse/linalg/eigen/lobpcg/lobpcg.py#L127) has a complexity of 61.

Besides radon, there are various other packages and Flake8 plugins:

* [flake8-annotations-complexity](https://pypi.org/project/flake8-annotations-complexity/): Nudge you to name complex types
* [flake8-cognitive-complexity](https://pypi.org/project/flake8-cognitive-complexity/): Validates cognitive functions complexity
* [flake8-expression-complexity](https://pypi.org/project/flake8-expression-complexity/): Make sure that single expressions are not too complicated; similar to cyclomatic complexity for functions / classes.
* [flake8-functions](https://pypi.org/project/flake8-functions/): Report too long functions and functions with too many arguments
* [mccabe](https://pypi.org/project/mccabe/): This is used by a couple of other tools and projects
* [wily](https://pypi.org/project/wily/): A command-line application for tracking, reporting on the complexity of Python tests and applications.
* [xenon](https://pypi.org/project/xenon/): Relies on radon

## Style Guides

![Make your code look professional. Photo by [Hunters Race](https://unsplash.com/@huntersrace?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10132/0*gC2HdhBSJwqGfFAF)*Make your code look professional. Photo by [Hunters Race](https://unsplash.com/@huntersrace?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

You might have heard the words “pythonic code”. It means to not only write correct Python code but use the languages features how they are intended to be used ([source](https://stackoverflow.com/a/25011492/562769)). It is for sure an opinionated term, but there are a lot of plugins that show you what a large part of the community considers to be pythonic.

Writing code in a similar style to other Python projects is valuable as people will have an easier time reading the code. This is important as we read software more often than we write it ([source](https://www.goodreads.com/quotes/835238-indeed-the-ratio-of-time-spent-reading-versus-writing-is)).

So, what is pythonic code?

Let’s start with [PEP-8](https://www.python.org/dev/peps/pep-0008/): It’s a style guide written and accepted by the Python community in 2001. So it’s been around for a while and most people want to follow most of it. The main part which I’ve seen most people not to agree with is the [maximum line length of 79](https://www.python.org/dev/peps/pep-0008/#maximum-line-length). I’m always recommending to follow this advice in 95% of your codebase. I gave [reasons](https://martin-thoma.com/python-style-guide/#maximum-line-length) for that.

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2020/08/black-logo.png"><img src="../images/2020/08/black-logo.png" alt="Logo of the black project" style="width: 512px;"/></a>
    <figcaption class="text-center">Logo of the black project. Image source: <a href="https://github.com/psf/black/blob/master/docs/_static/logo2.png">Black Contributors</a></figcaption>
</figure>

For pure code formatting, you should use an auto formatter. I grew into liking [black](https://pypi.org/project/black/) because it does NOT allow customization. Code formatted by black always looks the same. As you cannot customize it, you don’t need to discuss it. It just solves the issue of conflicting styles and arguments around it. Black is maintained by the Python Software Foundation and likely the most commonly adopted auto formatter for Python.

[yapf](https://github.com/google/yapf) by Google is another auto formatter.

## Docstrings

![Reading the manual can be fun if it’s written well. [Lasagne](https://lasagne.readthedocs.io/en/latest/modules/nonlinearities.html#lasagne.nonlinearities.sigmoid) and [Scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.prewitt.html#scipy.ndimage.prewitt) have pretty good documentation. Photo by [Laura Dewilde](https://unsplash.com/@lauradewilde97?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/8000/0*Ln2UNS74PuVuhOVM)*Reading the manual can be fun if it’s written well. [Lasagne](https://lasagne.readthedocs.io/en/latest/modules/nonlinearities.html#lasagne.nonlinearities.sigmoid) and [Scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.prewitt.html#scipy.ndimage.prewitt) have pretty good documentation. Photo by [Laura Dewilde](https://unsplash.com/@lauradewilde97?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

For docstrings, there is [PEP-257](https://www.python.org/dev/peps/pep-0257/). All of those rules are widely accepted in the community, but they still allow a wide variety of docstrings. There are three commonly used styles:

* [NumpyDoc-style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings: Used by Numpy and Scipy. It’s markdown with some specified sections such as `Parameters` and `Returns` in a fixed order.
* [Google-style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) docstrings: A super-slim format which has `Args:`and `Returns:`.
* [Sphinx-style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) docstrings: A very flexible format that uses restructured text.

I love the NumpyDoc format as it is super easy to read even when you just have it inside a text editor. Numpydoc is also well-supported by editors.

Here you can see the three in comparison:

```python
def get_meta_numpydoc(filepath, a_number, a_dict):
    """
    Get meta-information of an image.

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aenean commodo
    ligula eget dolor. Aenean massa. Cum sociis natoque penatibus
    et magnis dis
    parturient montes, nascetur ridiculus mus.

    Parameters
    ----------
    filepath : str
        Get metadata from this file
    a_number : int
        Some more details
    a_dict : dict
        Configuration

    Returns
    -------
    meta : dict
        Extracted meta information

    Raises
    ------
    IOError
        File could not be read
    """


def get_meta_google_doc(filepath, a_number, a_dict):
    """Get meta-information of an image.

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aenean commodo
    ligula eget dolor. Aenean massa. Cum sociis natoque penatibus
    et magnis dis
    parturient montes, nascetur ridiculus mus.

    Args:
        filepath: Get metadata from this file.
        a_number: Some more details.
        a_dict: Configuration.

    Returns:
        Extracted meta information:

    Raises:
        IOError: File could not be read.
    """


def get_meta_sphinx_doc(filepath, a_number, a_dict):
    """
    Get meta-information of an image.

    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aenean commodo
    ligula eget dolor. Aenean massa. Cum sociis natoque penatibus
    et magnis dis
    parturient montes, nascetur ridiculus mus.

    :param filepath: Get metadata from this file
    :type filepath: str
    :param a_number: Some more details
    :type a_number: int
    :param a_dict: Configuration
    :type a_dict: dict

    :returns: dict -- Extracted meta information

    :raises: IOError
    """
```

## Flake8

[You should always use a linter](https://medium.com/dailyjs/why-you-should-always-use-a-linter-and-or-pretty-formatter-bb5471115a76), as [Alberto Gimeno](undefined) pointed out. They can check your style, but more importantly, show potential errors.

[Flake8](https://pypi.org/project/flake8/) is a wrapper around PyFlakes, pycodestyle, and a McCabe script. It is the most commonly used tool for linting in Python. Flake8 is awesome because there are so many plugins for it. I found 223 packages with the string “flake8” within the name and looked at many of them. I’ve also looked at packages with the trove classifier Framework :: Flake8 and found 143 packages of which 122 started with flake8- . Only 21 packages had the Flake8 Framework trove classifier but didn’t start with flake8- and only two of them looked interesting.
> **Side note**: Typo squatting is an issue every open package repository has to fight with (Bachelor’s Thesis: [Typosquatting in Programming Language Package Managers](https://incolumitas.com/data/thesis.pdf) which has a [blog post](https://incolumitas.com/2016/06/08/typosquatting-package-managers/) and an [interesting follow-up](https://arxiv.org/pdf/2003.03471.pdf), Bachelor’s Thesis: [Attacks on Package Managers](https://is.muni.cz/th/y41ft/thesis_final_electronic.pdf)). There are examples in Python for it causing harm ([2017](https://mail.python.org/pipermail/security-announce/2017-September/000000.html), [2017](https://www.bleepingcomputer.com/news/security/ten-malicious-libraries-found-on-pypi-python-package-index/), [2017](https://nakedsecurity.sophos.com/2017/09/19/pypi-python-repository-hit-by-typosquatting-sneak-attack/), [2019](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/typosquatting-in-python-repositories/), [2019](https://snyk.io/blog/malicious-packages-found-to-be-typo-squatting-in-pypi/), [2019](https://sysdig.com/blog/malicious-python-libraries-jeilyfish-dateutil/)). There is [pypi-scan](https://github.com/jspeed-meyers/pypi-scan) for finding examples and [pypi-parker](https://pypi.org/project/pypi-parker/) to prevent common typos to be used. [William Bengtsson](undefined) also did something similar to harden the Python community against this thread. See his article below for more information about his project. Package parkinginflates the number of packages on PyPI and I filtered them by looking for the summary “A package to prevent exploit”.
[**Python Typosquatting for Fun not Profit**
*by William Bengtson | @__muscles*medium.com](https://medium.com/@williambengtson/python-typosquatting-for-fun-not-profit-99869579c35d)

Here are some of the interesting flake8 plugins:

* [cohesion](https://github.com/mschwager/cohesion): Check if class cohesion is below a threshold. This indicates that functionality should be split out of a class.

* [flake8-assert-msg](https://pypi.org/project/flake8-assert-msg/): Make sure assert statements have messages
* [flake8-blind-except](https://pypi.org/project/flake8-blind-except/): Prevent Pokemon exception catching
* [flake8-builtins](https://pypi.org/project/flake8-builtins/): Check for python builtins being used as variables or parameters.
* [flake8-docstrings](https://pypi.org/project/flake8-docstrings/): Adds pydocstyle support
* [flake8-isort](https://pypi.org/project/flake8-isort/): Use [isort](https://pypi.python.org/pypi/isort) to check if the imports on your python files are sorted the way you expect
* [flake8-logging-format](https://github.com/globality-corp/flake8-logging-format): Validate (lack of) logging format strings
* [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/): Checking common style issues or inconsistencies with pytest-based tests
* [flake8-requirements](https://pypi.org/project/flake8-requirements/): Checks/validates package import requirements. It reports missing and/or not used project direct dependencies
* [flake8-graphql](https://pypi.org/project/flake8-graphql/): Lint GraphQL query strings
* [flake8_implicit_str_concat](https://pypi.org/project/flake8_implicit_str_concat/): Goes well with black 🎉
* [flake8-mock](https://pypi.org/project/flake8-mock/): Check for mistakes using mocks
* [flake8-nb](https://pypi.org/project/flake8-nb/): Check jupyter notebooks
* [flake8-pyi](https://pypi.org/project/flake8-pyi/): Lint stub files
* [flake8-variables-names](https://pypi.org/project/flake8-variables-names/): Find common “meaningless” variable names
* [pep8-naming](https://pypi.org/project/pep8-naming/): Check your code against PEP 8 naming conventions
* [pandas-vet](https://pypi.org/project/pandas-vet/): Opinionated linting for Pandas code
* [wemake-python-styleguide](https://pypi.org/project/wemake-python-styleguide/): An opinionated style guide/checker which seems to be pretty popular. I haven’t seen that one before, though.

An alternative to parts of Flake8 [prospector](https://pypi.org/project/prospector/). It couples tools, but it is way less commonly used and thus not as flexible as Flake8.

## Flake8: Security and Bugs

![Be safe by looking at warning signs. Photo by [Troy Bridges](https://unsplash.com/@esptroy?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/8064/0*F1jS0N6EjU66u4nu)*Be safe by looking at warning signs. Photo by [Troy Bridges](https://unsplash.com/@esptroy?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

* [flake8-bandit](https://pypi.org/project/flake8-bandit/): Security Testing
* [flake8-bugbear](https://pypi.org/project/flake8-bugbear/): finding likely bugs and design problems in your program — usually it’s silent, but when it’s not you should have a look 🐻
* [flake8-requests](https://pypi.org/project/flake8-requests/): checks usage of the request framework

## Flake8: Remove Debugging Artifacts

It happened quite a couple of times to me: I’ve added some code while developing a new feature or debugging an old one and forgot to remove it afterward. It was most often caught by the reviewer, but it is not necessary to distract the reviewer with this.

[flake8-breakpoint](https://pypi.org/project/flake8-breakpoint/) checks for forgotten breakpoints and [flake8-print](https://pypi.org/project/flake8-print/) will complain about every print statement. [flake8-debugger](https://pypi.org/project/flake8-debugger/), [flake8-fixme](https://pypi.org/project/flake8-fixme/), [flake8-todo](https://pypi.org/project/flake8-todo/) go in the same direction.

## Let Dead Code Die

![Photo by [Kenny Orr](https://unsplash.com/@greyharpoon?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/11520/0*HolQng-8Fkoy-A63)*Photo by [Kenny Orr](https://unsplash.com/@greyharpoon?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Who hasn’t done it: You removed a functionality, but the code could be handy. So you comment it out. Or you add a if False block around it. Sometimes more sophisticated by adding a configuration option you don’t need.

The clean solution is to have a single, clear commit that removes that feature. Maybe add a git tag so that you can find it later if you want to add it again.

And then there is code which is dead, but you forgot about it. Luckily, you can automatically detect it:

* [flake8-eradicate](https://pypi.org/project/flake8-eradicate/): Find commented out (or so-called “dead”) code.
* [vulture](https://pypi.org/project/vulture/): Finds unused code in Python programs

## Flake8: Nudging Yourself to use Good Style

![Having an experienced developer review your code is awesome. In the best case, you will learn something new that you can apply in all further projects. And some plugins act like that. Photo by [Brooke Cagle](https://unsplash.com/@brookecagle?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/9446/0*lXvALfnWfaU_cFB_)*Having an experienced developer review your code is awesome. In the best case, you will learn something new that you can apply in all further projects. And some plugins act like that. Photo by [Brooke Cagle](https://unsplash.com/@brookecagle?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

Some plugins helped me to learn something about Python. For example, the following helped me to get rid of small little bugs and inconsistencies:

* [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/): Helps you write better list/set/dict comprehensions — I love this one 😍
* [flake8-executable](https://pypi.org/project/flake8-executable/): Check executable permissions and [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix)). Files should either executable and have a shebang, or not be executable and not have a shebang.
* [flake8-raise](https://pypi.org/project/flake8-raise/): Finds improvements for raise statements
* [flake8-pytest](https://pypi.org/project/flake8-pytest/): Use assert instead of assertEqual

The following new style nudging plugins aim to push you to use modern style Python:

* [flake8-pathlib](https://pypi.org/project/flake8-pathlib/): [Pathlib](https://docs.python.org/3.4/library/pathlib.html) was added in Python 3.4 and I’m still not quite used to it. This plugin might nudge me to use it when it’s appropriate.
* [flake8-string-format](https://pypi.org/project/flake8-string-format/), [flake8-printf-formatting](https://pypi.org/project/flake8-printf-formatting/), [flake8-sts](https://pypi.org/project/flake8-sfs/): String formatting.

This is one of the most valuable categories for me. If you know more plugins which help to use new styles, let me know 😃

## Flake8 Meta Plugins

![Image created by Martin Thoma via imgflip.com](https://cdn-images-1.medium.com/max/2400/1*E4HyDr73N_j4p3mn5X64pA.jpeg)*Image created by Martin Thoma via imgflip.com*

Flake8 has some plugins which don’t add more linting functionality, but improve flake8 in another way:

* [flake8–colors](https://pypi.org/project/flake8-colors/): ANSI colors highlight for Flake8
* [flake8-csv](https://pypi.org/project/flake8-csv/): Generate error reports in CSV format
* [flake8-json](https://pypi.org/project/flake8-json/): Generate error reports in JSON format
* [flake8-dashboard](https://pypi.org/project/flake8-dashboard/) and [flake8-html](https://pypi.org/project/flake8-html/): Generate an HTML report ([dashboard demo](https://aperezhortal.github.io/flake8-dashboard/example_dashboard/index.html))
* [flake8-immediate](https://pypi.org/project/flake8-immediate/): Prints the errors directly without any delay
* [flake8-strftime](https://pypi.org/project/flake8-strftime/): Checks for use of platform-specific strftime codes
* [flake8-SQL](https://pypi.org/project/flake8-SQL/) and [py-find-injection](http://py-find-injection): Looks for SQL queries and checks them against an opinionated style
* [flake8-tuple](https://pypi.org/project/flake8-tuple/): Checks for (probably) unintended one element tuples

And some plugins people might need for legal reasons like flake8-author, flake8-copyright, and flake8-license.
> To Flake8 plugin authors: Please make sure that you list the error codes your plugin introduces and that you give at least some examples of what your plugin considers bad / good.

## Type Annotations and Type Checking

![The mypy plugin for VS Code showing an issue with the types. Screenshot by Martin Thoma.](https://cdn-images-1.medium.com/max/3442/1*jXmhQQBv0xgpPQPUN08Z_A.png)*The mypy plugin for VS Code showing an issue with the types. Screenshot by Martin Thoma.*

It’s possible in Python, but you need to do it. It’s not done automatically. I’ve written a longer article about how [type annotations work in Python](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d). There are multiple tools you can use, but I recommend mypy. You can run it via pytest by using pytest-mypy or via flake8 by using flake8-mypy , but I prefer to run it separately. The main reason for it is that the output given by [CI pipelines](https://levelup.gitconnected.com/ci-pipelines-for-python-projects-9ac2830d2e38) is cleaner.

You can integrate type checking (e.g. via mypy) into your editor, but the type annotations alone already go a long way as they document what is expected.

## Package Structure

![Check that your package looks fine before shipping it. Photo by [Toby Stodart](https://unsplash.com/@tobystodart?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/10080/0*y67weckARV-M_yOh)*Check that your package looks fine before shipping it. Photo by [Toby Stodart](https://unsplash.com/@tobystodart?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

[pyroma](https://github.com/regebro/pyroma) rates how well a Python project complies with the best practices of the Python packaging ecosystem.

Here are some examples of my projects:

```shell
$ pyroma mpu
------------------------------
Checking mpu
Found mpu
------------------------------
Final rating: 10/10
Your cheese is so fresh most pe

$ pyroma nox
------------------------------
Checking nox
Found nox
------------------------------
Your long_description is not valid ReST:
<string>:2: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.
<string>:3: (WARNING/2) Field list ends without a blank line; unexpected unindent.
<string>:4: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.
------------------------------
Final rating: 9/10
Cottage Cheese
------------------------------
```

## Want to Know More About Unit Testing?

In this series, we already had:

* Part 1: [The basics of Unit Testing in Python](https://medium.com/swlh/unit-testing-in-python-basics-21a9a57418a0)
* Part 2: [Patching, Mocks, and Dependency Injection](https://levelup.gitconnected.com/unit-testing-in-python-mocking-patching-and-dependency-injection-301280db2fed)
* Part 3: [How to test Flask applications](https://medium.com/analytics-vidhya/how-to-test-flask-applications-aef12ae5181c) with Databases, Templates and Protected Pages
* Part 4: [tox and nox](https://medium.com/python-in-plain-english/unit-testing-in-python-tox-and-nox-833e4bbce729)
* Part 5: [Structuring Unit Tests](https://towardsdatascience.com/unit-testing-in-python-structure-57acd51da923)
* Part 6: [CI-Pipelines](https://towardsdatascience.com/ci-pipelines-for-python-projects-9ac2830d2e38)
* Part 7: [Property-based Testing](https://towardsdatascience.com/unit-testing-in-python-property-based-testing-892a741fc119)
* Part 8: [Mutation Testing](https://medium.com/analytics-vidhya/unit-testing-in-python-mutation-testing-7a70143180d8)
* Part 9: Static Code Analysis: Linters, Type Checking, and Code Complexity

Let me know if you’re interested in other topics around testing with Python or professional software development with Python: info@martin-thoma.de
