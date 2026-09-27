---
layout: post
title: How I use AI on this blog
slug: how-i-use-ai
lang: en
author: Martin Thoma
date: 2026-09-27 20:00
category: My bits and bytes
tags: Blog, AI
featured_image: logos/ai.png
---
In September 2026, I reworked my complete blog:

* **Design**: This blog has a new theme. It has a dark mode, works better on
  phones, has a better search page, and images open in a lightbox where you can
  page through galleries.
* **Old articles**: I imported my articles from Medium. Then I went through
  all of the roughly 900 articles: I fixed typos, grammar, broken formulas and
  markup, added alt texts to images, removed tracking parameters from links and
  cleaned up the tags.

I could not have done this in a few weeks without AI. I mainly used Claude.
That's why I want to be transparent about what AI does on this blog and what it
doesn't.


## Images: "AI generated" and "AI modified"

Images that an AI tool made have a small badge in the top right corner:

* **AI generated**: The whole image comes from an AI tool. So far, I've used
  Claude, ChatGPT and Gemini. I want the caption to name the tool as well. I'm
  still adding that to older images.
* **AI modified**: A real photo that an AI tool changed. Cropping a photo or
  adjusting its brightness in a normal image editor doesn't count.

Images that **don't** get a badge:

* **My own photos and screenshots**, unless an AI tool changed them.
* **Diagrams**: charts, flow charts, network diagrams, pyramids and maps with
  data. They don't pretend to be a photo, so nobody takes them for real. If an
  AI tool made the diagram, the caption still says so.
* **Charts from data**: When Claude writes the Python code for a chart, the
  numbers come from the cited data, not from the AI. The caption says "created
  with Claude AI in Python/matplotlib" and names the data source.

The EU AI Act only requires a label for deep fakes: images that look like real
people, places or events and would falsely appear authentic[^1]. I label more
than that, because I think you should know when a picture wasn't taken by a
camera.


## Copy editing

AI proofreads my articles. It's a bit more than a spell checker, more like
copy editing:

* **Fixed directly**: typos, grammar, broken formulas and markup, obvious
  calculation errors and dead links.
* **Only flagged**: outdated facts, missing sources, unclear structure, a weird
  tone. AI adds those to a list, and I decide what to do with them.
* **Research**: AI looks up missing numbers and checks facts, but only with a
  source that I can follow.

I wrote down the rules for this blog in a file that the AI reads before it
changes anything: how to format sources, which tags to use, when an image gets
a badge.


## I check everything

Nothing goes online that I haven't checked. Every change is a diff in Git, so
I can see exactly what the AI changed before I publish it. If an article is
wrong, it's my mistake, not the AI's.


## No AI slop

I will **not** generate AI slop. I don't see a point in doing so: there is
enough generic text on the internet, and I write because I want to share what I
think and what I found out.

But I might use AI to rephrase a clumsy sentence, fix issues or find a better
formulation. The ideas, opinions and experiences are mine.


## Spell checker, search engine, talented intern

I use AI like three tools I already knew:

* **A spell checker**: It finds typos and grammar mistakes, and it suggests
  better formulations.
* **A search engine**: It finds sources and data much faster than I could. But
  just like with a search engine, I read the source before I trust it.
* **A very talented intern**: It is fast, knows a lot and does tedious work
  without complaining. But it also makes mistakes with full confidence. So I
  give it clear instructions, and I review its work.


## Footnotes

[^1]: [Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems](https://artificialintelligenceact.eu/article/50/) via artificialintelligenceact.eu, accessed 27.09.2026. The definition of a deep fake is in Article 3(60).
