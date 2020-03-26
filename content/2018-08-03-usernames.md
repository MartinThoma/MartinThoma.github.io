---
layout: post
title: Usernames
slug: usernames
author: Martin Thoma
date: 2018-08-03 20:00
category: The Web
tags: Web Services
featured_image: logos/web.png
---
Usernames are used for identification in two places in web services: To let
people log in and to allow people recognizing each other. In this article I
want to share some ideas on usernames.


## Username vs Display name

When I look into my Stackoverflow profile, they have something called
"display name":

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/08/stackoverflow-profile.png"><img src="../images/2018/08/stackoverflow-profile.png" alt="Stackoverflow Profile edit page" style="width: 512px;"/></a>
    <figcaption class="text-center">Stackoverflow Profile edit page</figcaption>
</figure>

I like this a lot. I communicates clearly that it is something seen by others.

The next question that popped to my mind was if we need usernames at all.
Wouldn't it be simpler to just login with your password?

Two big problems with that idea:

* People might choose the same passwords
* Systems could allow multiple accounts and you might want to have autocompletion

This means we definitely need a username for logging in.


## Display name restrictions

Is it a good idea to let people completely freely choose their username from
any sequence of Unicode characters?

The problems I see with that:

* *Design*: People might choose names that break something. It's hard to have
  a nice design with a component that could grow arbitrarily.
* A minimum length might be desirable to make sure one can click on the name
  (at least one non-whitespace character)
* *Identity theft*: Think of the following usernames
    * `Obama` vs `0bama` vs `Obamа`: [Char 1072](http://www.fileformat.info/info/unicode/char/0430/index.htm)
    * Messing around with whitespace in the beginning / end of a name
    * Messing around with control characters
    * See [Unicode Confusables](http://unicode.org/reports/tr36/confusables.txt)
* *Script injection*: By allowing `<` and `>` an attacker could choose a
  username which loads HTML.
* *Interactions*: User interact. For example, in discussions they might
  naturally write `@martin` to mention the user `martin`. This means an `@`
  character should be excluded.
* *Markdown*: Other caracters like `#[]=*~` are also be a bad choice as they are
  part of Markdown.
* *Math*: `$` is a bad choice as it triggers MathJax / LaTeX.
* *Natural seperators*: Some characters are natural seperators in English,
  German and French: Whitespace, Comma `,`, Semi-colon `;`, dot `.`, double point
* *Offensive Language*: Actually, the main problem I see here is when developers
  try to be smart and have a false positive - seeing something as offensive
  which is just the name of a person.

Where you might want freedom:

* Multiple charactersets for multi-country support (Kyrillic, Arabic, Chinese, ...)


## What others do

<table class="table">
    <tr>
        <th>Service</th>
        <th>Min</th>
        <th>Max</th>
        <th>Charset</th>
        <th>Strip</th>
        <th>Other</th>
    </tr>
    <tr>
        <td>Twitter (Display Name)</td>
        <td>1</td>
        <td>50</td>
        <td>Unicode</td>
        <td>yes</td>
        <td></td>
    </tr>
    <tr>
        <td>Stack Overflow (Display Name)</td>
        <td>3</td>
        <td>30</td>
        <td>letters, digits, spaces, apostrophes, hyphens</td>
        <td>yes</td>
        <td>must start with a letter or digit</td>
    </tr>
</table>
