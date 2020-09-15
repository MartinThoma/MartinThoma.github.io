---
layout: post
title: Logging Basics in Python
slug: logging-basics-in-python
URL: https://towardsdatascience.com/logging-basics-in-python-d0db13e538f9
author: Martin Thoma
date: 2020-09-15 20:00
category: Code
tags: Python, Logging
featured_image: logos/python.png
---
![The [dmesg](https://en.wikipedia.org/wiki/Dmesg) output. Screenshot taken by Martin Thoma.](https://cdn-images-1.medium.com/max/3760/1*7bpeZdDGtnxRIFE0iYp7OQ.png)*The [dmesg](https://en.wikipedia.org/wiki/Dmesg) output. Screenshot taken by Martin Thoma.*

Logging is the act of recording information about the current state of execution. It’s typically done for two purposes:

1. **Debugging**: To enable the developer to narrow down the cause of a system failure
2. **Monitoring**: To enable people on operations to know what is currently happening

## Hello, Sweet logging World!

The simplest way to log is like this:

```python
import logging
import sys

logging.basicConfig(
    format="{asctime} {levelname:<8} {message}",
    style="{",
    level=logging.DEBUG,
    stream=sys.stdout,
)

logging.info("Hello World!")
```

It gives output like this:

```text
2020-09-07 22:40:32,101 INFO     Hello World!
```

**BasicConfig should probably not be used**. Please continue reading “the 4 logging classes” to learn why 😁

![Image by Oliver Widder from [geek-and-poke.com](http://geek-and-poke.com/geekandpoke/2015/10/18/why-logging-is-so-important)](https://cdn-images-1.medium.com/max/4960/1*g34WT6mRV4_UKC06OnUNeg.jpeg)*Image by Oliver Widder from [geek-and-poke.com](http://geek-and-poke.com/geekandpoke/2015/10/18/why-logging-is-so-important)*

## The 4 Logging Classes

Python has a logger hierarchy in a tree structure. This means you can apply a log configuration for a single logger and make all child loggers behave the same way. This is useful if you want to configure a package. logging.basicConfig acts on the root logger. For this reason, it should only be used within application code, but not in library or framework code.

Python distinguishes 4 main components that you can adjust to your needs: Loggers, handlers, filters, and formatters. They act on log records that are created when you pass your log message to the logger.

### Loggers

A logger is an object you use to emit log records:

```python
import logging

logger = logging.getLogger(__name__)
```

You can emit 5 levels of log messages :

* **Debug**: extremely detailed, you can use this if you have no clue at a certain part of the code what is happening. Remember to remove it again.
* **Info**: nothing to worry about, but helpful to understand the system
* **Warning**: something that could become a problem that happened. Maybe an event that might indicate an error if it happens too often. Maybe the remaining storage becomes low. Maybe the internet connection was broken. Maybe a file was not writable.
* **Error**: an important event could not be executed, e.g. because of missing privileges or a file that should be read did not exist.
* **Critical**: a problem that requires the app to restart happened. For example, a kill signal was received.

You use it like this :

```python
logger.info("My first log message")
logger.warning("The specified file could not be opened.")
```

### Log Handlers

File handlers store stuff to files, stream handlers write logs to a stream:

```python
sh = logging.StreamHandler()
fh = logging.FileHandler("spam.log")
logger.addHandler(sh)
```

If you’re using a file handler, consider using a [RotatingFileHandler](https://docs.python.org/3/howto/logging-cookbook.html#using-file-rotation). It will create a new file once the log file becomes too big. You can specify how many files there might be. When the maximum is reached, the oldest file is deleted.

The [HTTPHandler](https://docs.python.org/3/library/logging.handlers.html#httphandler) is also noteworthy because it allows you to integrate into other systems such as Slack.

Commonly, you also want to set the log level to either the logger or the log handler:

```python
sh.setLevel(logging.INFO)
```

![Image by Oliver Widder from g[eek-and-poke.com](https://geekandpoke.typepad.com/geekandpoke/2010/01/geeks.html)](https://cdn-images-1.medium.com/max/2000/1*QR-5wpqk0J2X3O1vlYSrqQ.jpeg)*Image by Oliver Widder from g[eek-and-poke.com](https://geekandpoke.typepad.com/geekandpoke/2010/01/geeks.html)*

### Log Formatters

The log formatter changes the log message string. A formatter is attached to a log handler:

```python
formatter = logging.Formatter("{asctime} {levelname:<8} {message}", style="{")
sh.setFormatter(formatter)
```

The style attribute is interesting. The default is % which means the format string then needs to be (asctime)s (levelname)-8s (message)s . I never really learned how the percentage style formatting works. I like to stick to the curly braces.

There are way more [log record attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes) which you can use.

### Log Filters

[Log filters](https://docs.python.org/3/library/logging.html#filter-objects) provide the possibility to define which log records get shown:

```python
import datetime
import logging
import sys

logger = logging.getLogger(__name__)


class OnWeekendOnlyErrorsFilter(logging.Filter):
    def filter(self, record):
        is_weekday = datetime.datetime.today().weekday() < 5
        return is_weekday or record.levelno >= logging.ERROR


stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.WARNING)
stdout_handler.addFilter(OnWeekendOnlyErrorsFilter())
logger.addHandler(stdout_handler)
```

![Photo by [Nigel Tadyanehondo](https://unsplash.com/@nxvision?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/7872/0*LdnHX9sPcoVbJMbF)*Photo by [Nigel Tadyanehondo](https://unsplash.com/@nxvision?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

## Logging vs print vs exception

I’ve been very confused about when I should simply print out information and when I should log out or when I should throw an exception.

> You throw an exception in a library function so that the user of that function can catch the exception and show the end-user a meaningful error message. The end-user should never see a traceback.

**Logging is meant for other systems or developers** who try to understand what happened to a system, whereas **print is for the user**. The confusing part is that print messages go by default to the standard error. You can easily do the same with print. I’ve used it in the past to give the user feedback of what is currently happening, simply because logging had an easy way to include time stamps.

![Photo by [Esteban Lopez](https://unsplash.com/@exxteban?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/7744/0*nCSTE1Mg5o-lyMj1)*Photo by [Esteban Lopez](https://unsplash.com/@exxteban?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

## Warnings.warn vs logging.warning

According to [the official docs](https://docs.python.org/3/howto/logging.html#when-to-use-logging), you have two options when you want to issue a warning regarding a particular runtime event:

* [warnings.warn()](https://docs.python.org/3/library/warnings.html#warnings.warn) in library code, if the issue is avoidable and the client application should be modified to eliminate the warning
* [logging.warning()](https://docs.python.org/3/library/logging.html#logging.warning) if there is nothing the client application can do about the situation, but the event should still be noted

A typical use-case for warnings is [DeprecationWarning](https://docs.python.org/3/library/exceptions.html#DeprecationWarning) with which a library can tell its users to remove a certain type of usage. Or Scipy warning you that no BLAS library was found.

![Too few log messages are bad, but too many can be problematic as well. Photo by [Christa Dodoo](https://unsplash.com/@krystagrusseck?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/8064/0*OmKMed1DyMeALh3k)*Too few log messages are bad, but too many can be problematic as well. Photo by [Christa Dodoo](https://unsplash.com/@krystagrusseck?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

## What should I log?

I typically log code that takes long to execute pretty well, whereas I don’t add much logging to functions which are called super often and are fast. Most of the time there are initialization functions which load configuration. I always log the complete configuration but strip away credentials.

I also log errors and rare exceptions.

It’s hard to find the right balance. Too many log messages make it hard to find relevant information. To few messages might mean that you didn’t log the important information at all.

## Best practices

It’s a common practice for applications to create a log.py or a logger.py file in which the logger is initiated, log handler, and formatters are added. [OpenShot](https://github.com/OpenShot/openshot-qt) is doing it.

![Photo by [Kristina Flour](https://unsplash.com/@tinaflour?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/9640/0*-2fIUT_dAjXX0-2q)*Photo by [Kristina Flour](https://unsplash.com/@tinaflour?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

## Silencing loggers

A common cause of frustration is log messages from 3rd party software which spam your application. If they behave well, it is easy to silence them: Get the logger and set the level to something high:

```python
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
```

If you don’t even want critical log records, you can set

```python
logging.getLogger("urllib3").setLevel(logging.CRITICAL + 1)
```

To disable the child loggers as well:

```python
# Disable all child loggers of urllib3, e.g. urllib3.connectionpool
logging.getLogger("urllib3").propagate = False
```

You can also remove all handlers / add the [NullHandler](https://docs.python.org/3/library/logging.handlers.html#nullhandler).

## Should I always use Pythons’ logging library?

For sure not! Some scripts are so short that logging isn’t reasonable. Others, [like ArchiveBox](https://github.com/pirate/ArchiveBox/issues/468#issuecomment-688489159), implement their own specialized logging. And there are other logging libraries like [structlog](https://pypi.org/project/structlog).

## More information

Similar information is available in an amazing PyCon talk by [Curtis Maloney](undefined):

You can directly read the [documentation](https://docs.python.org/3/library/logging.html) or the official [logging howto](https://docs.python.org/3/howto/logging.html). To me, [reading StackOverflow](https://stackoverflow.com/questions/tagged/logging+python) is also often helpful.

With those resources, I hope nobody has to struggle with Python logging again. If you still have questions, let me know (info@martin-thoma.de).
