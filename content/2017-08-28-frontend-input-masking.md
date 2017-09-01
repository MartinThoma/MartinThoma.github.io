---
layout: post
title: Frontend Input Masking
slug: frontend-input-masking
author: Martin Thoma
status: draft
date: 2017-08-28 20:00
category: Code
tags: Frontend
featured_image: logos/frontend.png
---

Input Masks are neat, because they guide the user when he has to type in common
information such as credit card numbers and phone numbers. Sure, you should
use the [HTML5 input type](https://developer.mozilla.org/en/docs/Web/HTML/Element/Input) such as `type='tel'`,
`type='tel-country-code'`
and `type='cc-number'`. They will, however, only validate the format on user side,
but not help him with the input (see [fiddle](https://jsfiddle.net/MartinThoma/rj5wkhtL/)).

Providing a `placeholder` is a first step to improve the situation, but it's
still not optimal.

One better way to do it is to insert the grouping characters (most of the time
it will be spaces, sometimes braces and for phone numbers also dashes or a plus sign)
and remove other characters. This, however, will allow the user to select the
characters which might not be desirable. See [jQuery Mask Plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/)
for an example.

To get the desired behaviour, I think one of the best solutions might be to
have multiple input fields (one per group) and make them look as if it is one.

It's astonishing to me that grouping is not applied by default for some
well-known formats such as `type='tel-country-code'`, `type='date'` and
`type='cc-number'`.

## See also

* [css-tricks.com](https://css-tricks.com/input-masking/)
* Stackoverflow:
    * [How to implement an input with a mask](https://stackoverflow.com/questions/12578507/how-to-implement-an-input-with-a-mask)
    * [Friendly format for phone numbers](https://ux.stackexchange.com/q/5675/3906)
* [Labelmask](http://bradfrost.com/blog/post/labelmask/)
* [Programmers imagine the most ridiculous ways to enter a phone number into a form](https://qz.com/679782/programmers-imagine-the-most-ridiculous-ways-to-input-a-phone-number/)
