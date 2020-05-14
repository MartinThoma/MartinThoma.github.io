---
layout: post
title: Naming Styles
slug: naming-styles
author: Martin Thoma
date: 2020-05-14 20:00
category: Code
tags: Code, Style Guide
featured_image: logos/python.png
---
Naming styles are one of the trivial things in a style guide. Here are some of
then names you might hear.

## The Styles

* `snake_case`
* `camelCase`: Also lowerCamelCase
* `PascalCase`: Also UpperCamelCase
* `CONSTANT_CASE`: This is used in many languages for constants
* `cebab-case`: I have only seen this within strings. This is likely as the `-`
  is usually used for substraction. It's also used for file names. It's mentioned [here](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) and on [robinwieruch.de](https://www.robinwieruch.de/javascript-naming-conventions).


## Application

<table class="table">
    <thead>
        <tr>
            <th></th>
            <th>Variables</th>
            <th>Functions / Methods</th>
            <th>Classes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Python</td>
            <td>snake_case</td>
            <td>snake_case</td>
            <td>PascalCase</td>
        </tr>
        <tr>
            <td>JavaScript</td>
            <td>camelCase</td>
            <td>camelCase</td>
            <td>PascalCase</td>
        </tr>
        <tr>
            <td>C++</td>
            <td>snake_case</td>
            <td>PascalCase</td>
            <td>PascalCase</td>
        </tr>
        <tr>
            <td>Java</td>
            <td>camelCase</td>
            <td>camelCase</td>
            <td>PascalCase</td>
        </tr>
    </tbody>
</table>

## See also

Wikipedia:

* [Snake case](https://en.wikipedia.org/wiki/Snake_case)
* [Camel case](https://en.wikipedia.org/wiki/Camel_case)

Style Guide:

* [C++](https://google.github.io/styleguide/cppguide.html)
* [Java](https://google.github.io/styleguide/javaguide.html)
* [JavaScript](https://google.github.io/styleguide/jsguide.html)
* [Python](https://www.python.org/dev/peps/pep-0008/)
