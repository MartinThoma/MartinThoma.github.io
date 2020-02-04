---
layout: post
title: HTML Quantities
slug: html-quantities
author: Martin Thoma
date: 2019-12-28 20:00
category: The Web
tags: HTML, Semantic Web
featured_image: logos/html.png
---

The web is constantly evolving, and so it the language of it: HTML. Many
changes users notice are around JavaScript, but we also got [semantic tags](https://www.w3schools.com/html/html5_semantic_elements.asp) such
as `<article>`, `<section>`, `<header>`, `<footer>`. With rich markup one can
allow unknown third parties to parse and extract relevant information, such
as the author or the time when an article was published. Or that it is an
article at all.

It's pretty cool that we now have those semantic HTML elements and that we have
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata">Microdata</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/microformats">Microformats</a> and <a href="https://en.wikipedia.org/wiki/RDFa">RDFa</a>
which gives us neat <a href="https://developers.google.com/search/docs/guides/intro-structured-data">Google Search Result previews</a>.

But [I miss a standard to annotate quantities](https://stackoverflow.com/q/53097575/562769).

<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>

## The problem

We use different quantities. The biggest clash are the two systems: The [metric system](https://en.wikipedia.org/wiki/Metric_system) vs [imperial units](https://en.wikipedia.org/wiki/Imperial_units). Just look at the following and try to answer basic questions:

* It was -5°F in winter in Augsburg. Was it cold?
* It was 35°C in summer in North Dakota. Was it hot?
* The truck has a horsepower of 500 and the car has 400 kW. Which one is more powerful?
* I could pay 1200 USD or 1100 EUR for my guide - which deal is better?

The last one is a bit unfair as exchange rates change, but the first 3 would be
easy if they were in a single unit / in the unit you know. I would like
browsers to be able to automatically convert units. But that is only possible
if units can be identified easily.


## Intermediate solution

```
<span class="quantity temperature"><span class="value">-5</span><span class="unit">°F</span></span>
<span class="quantity power"><span class="value">400</span><span class="unit">kW</span></span>
```


## Good solution

The intermediate solution is a bit verbose. I would prefer a syntax like:

```
<quantity type="temperature"><num>-5</num><unit>°F</unit></quantity>
<quantity type="power"><num>400</num><unit>kW</unit></quantity>
```

Where the `<num>` tag should be the number without any spaces / other tags, but
it should also have easy ways to customize the numbers (preferably via CSS):

* Thousands seperator: `,` or `.` or `'` or ` `
* Decimal seperator: `,` or `.`

You can do this number formatting with JavaScript [`toLocaleString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString):

```
num = 1234567
num.toLocaleString('en', {useGrouping:true})
```

gives `1,234,567.89`


## See also

* [How should I markup units of measurement in HTML5?](https://stackoverflow.com/q/15566636/562769)
