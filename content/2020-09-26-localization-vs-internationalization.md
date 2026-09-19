---
layout: post
title: Localization vs Internationalization
slug: localization-vs-internationalization
lang: en
author: Martin Thoma
date: 2020-09-27 20:00
category: My bits and bytes
tags: Terminology, English
featured_image: logos/star.png
medium_url: https://medium.com/plain-and-simple/localization-vs-internationalization-fd2561dfdbcb
---
Internationalization is the process of making your software easy to adapt to different languages or regions.

Internationalization is often abbreviated as i18n. In a website, i18n can mean using Babel projects (e.g. [flask-babel](https://pypi.org/project/Flask-Babel/) in Python, [gettext](https://www.php.net/manual/en/intro.gettext.php) in PHP, [FormatJS](https://formatjs.io/) in JavaScript, …).

Localization is the process of adapting your software to a different language or region.

Localization is often abbreviated as l10n. l10n includes translation, adjusting currencies ($, €, £, ¥, …), systems of measurement (metric vs imperial), and time zones. The language change might make a lot of other changes necessary. For example, it can very well be that the layout does not work any longer. It might mean that you need to get more data about the user because there are other ways to address the user.

### Localization is not defined by the language

You might be tempted to use the language as an identifier for the locale. That doesn’t work:

* English: The UK has calendars that start on Monday, but the USA has calendars starting on Sunday. The UK has pounds, the US has dollars.
* German: Switzerland has the Swiss franc, Germany has the Euro.

### Localization is not defined by the country

This one is far closer, but there are many more detailed rules about time zones. For example, the [US has four time zones](https://en.wikipedia.org/wiki/Time_in_the_United_States) and [Russia has 11 time zones](https://en.wikipedia.org/wiki/Time_in_Russia).

Also, the language is not defined by the country. French is the official language of Quebec, but the rest of Canada speaks English.

## See also

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/0j74jcxSunY" frameborder="0" allowfullscreen></iframe></center>

* W3C: [Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n.en)
* Wikipedia: [Internationalization and localization](https://en.wikipedia.org/wiki/Internationalization_and_localization)
* Ben Hamill: [Falsehoods Programmers Believe About Language](http://garbled.benhamill.com/2017/04/18/falsehoods-programmers-believe-about-language)
* Skylar MacDonald: [Falsehoods Programmers Believe About Me](https://skylarmacdonald.com/falsehoods/)
