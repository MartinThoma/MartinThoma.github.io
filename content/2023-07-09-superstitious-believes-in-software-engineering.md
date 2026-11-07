---
layout: post
title: Superstitious beliefs in Software Engineering
slug: superstitious-beliefs-in-software-engineering
lang: en
author: Martin Thoma
date: 2023-07-09 21:59
category: Code
tags: Software Engineering
featured_image: logos/code.png
summary: The Monkey-Ladder Experiment and what it teaches about “we have always done it like that”
medium_url: https://medium.com/@martinthoma/superstitious-believes-in-software-engineering-1067a7f5ec33
---
The Monkey-Ladder Experiment is a parable from “Competing for the Future” by Gary Hamel and C. K. Prahalad (1994) and goes like this:

> 4 monkeys in a room. In the center of the room is a tall pole with a bunch of bananas suspended from the top. One of the four monkeys scampers up the pole and grabs the bananas. Just as he does, he is hit with a torrent of **cold water** from an overhead shower. He runs like hell back down the pole without the bananas. Eventually, the other three try it with the same outcome. Finally, they just sit and don’t even try again. To hell with the damn bananas. But then, they remove one of the four monkeys and replace him with a new one. The new monkey enters the room, spots the bananas and decides to go for it. Just as he is about to scamper up the pole, the other three reach out and drag him back down. After a while, he gets the message. **There is something wrong, bad or evil that happens if you go after those bananas.** So, they kept replacing an existing monkey with a new one and each time, none of the new monkeys ever made it to the top. They each got the same message. Don’t climb that pole. None of them knew exactly why they shouldn’t climb the pole, they just knew not to. They all respected the well established precedent. EVEN AFTER THE SHOWER WAS REMOVED! ([Source](http://www.altfeldinc.com/pdfs/Competing%20for%20the%20Future.pdf))

It’s [well-illustrated on Stack Exchange](https://skeptics.stackexchange.com/q/6828/1201).

The interesting part of this thought experiment is that the monkeys never learn the rules by which the cold water is triggered.

Without knowledge or understanding of the mechanism, we just repeat what others did. **We need to challenge the status quo.**

You might hear sentences like this at work (and I might even say it!):

* “Don’t touch this” [because it’s working / too complex]
* “We have always done it like that” [but I don’t know why] ⚠️
* “I don’t know why, but we should do it like this”

The important part is to learn something so that you don’t have to repeat the same mistake multiple times. You can do that in three steps:

1. **Documentation**: Document what you’re doing in tickets / issues (e.g. Jira) or in Wiki systems (e.g. Confluence) or public chat channels (e.g. Slack).
1. **Add Context**: Give enough context so that it can be repeated.
1. **Add hints for future-you**: Give hints when it can be tried again, e.g. a link to an issue ticket (e.g. you might find a ticket to a third-party software bug that needs to be fixed first).

Those were my 2 cents for better software development. Cheers!
