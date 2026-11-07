---
layout: post
title: 9 Steps to Software Project Handovers
slug: 9-steps-to-software-project-handovers
lang: en
author: Martin Thoma
date: 2021-06-04 17:01
category: Code
tags: Software Engineering, Project Management
featured_image: logos/code.png
summary: Passing on the baton isn’t a cakewalk. Here’s how to do it
medium_url: https://medium.com/@martinthoma/9-steps-to-software-project-handovers-9325fbb72cfc
---
Software projects need to be handed over all the time. New people join, others leave the company. When I did my first handover, I was pretty bad at it. I improved over time and just got an excellent introduction by [Niklas Baumstark](https://twitter.com/_niklasb).

Let me share some ideas on how I think you can structure amazing handovers in nine steps. Let’s get started!

## 1. Plan Ahead

Handovers take time. You will forget to mention important things and the receiver will forget to ask important questions. The sooner you begin, the better. This leaves room to let the knowledge sink in — and come back to you if something is unclear.

## 2. Clean Up!

Before you hand it over, make sure the software is clean. Search for `TODO` notes. Either remove them or clarify them.

Remove dead code — *you aren’t gonna need it* ([YAGNI principle](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)).

In general, you should only install the software you actually use. Over time, you may have installed stuff that was needed once but isn’t needed any longer. Remove unused dependencies. It’s really hard for people who don’t know why they’re installed to remove them.

Also, update the dependencies you have. Preferably to a long-term support version (LTS version).

Make sure that the unit tests work and that you cover the important parts — or point out which parts are not covered and need to be treated with caution! Letting those tests run in a CI pipeline helps to make sure they are actually executed.

Docker helps to make sure that people can run the software.

And finally, commit everything to version control and push!

## 3. Create an Awesome README

The README file is the first impression your software makes. It should clearly state what the project is about in Tweet length, give instructions on how to install it, and show how to use it.

There are a couple of other things you might want to mention. For example, how to run the tests or core design principles, guarantees the software gives, or the types of users the project has.

There are many things you can document, but try to keep it short. A README should not be overwhelming. You can add links to more detailed documentation.

If you are wondering how to structure it, have a look at readme.so:

[**readme.so - Easiest Way to Create A README** *Use readme.so's markdown editor and ready made templates to easily create a simple README for your repositories*readme.so](https://readme.so/en)

## 4. Talk About Design Principles

Written documentation is good, but it’s very different to hear it from a core developer. The way you emphasize things and the points you repeat give way more nuance than just the written text. It also gives the chance to ask questions. And at the very least, you know that the person who got the project has heard about the core ideas before.

Professional novelists have their personal styles, and they are all “valid.” It’s similar to software. It starts with simple stylistic choices (e.g. if you mark strings with `'single quotes'` or with `"double quotes"`). In which order do you typically write function arguments?

Those are tiny choices that are nice to keep consistent but not crucial.

Frameworks are crucial. They force you to use a certain style of development.

The guarantees you give to users are crucial. Do the users of your library expect an independent security audit before each release? Can your users expect your API to respond in 25ms? Are your endpoints safe to [retry](../10-robustness-resiliency-design-patterns/)?

Assumptions are crucial. Which services do you expect to respond in which time? Where are your security boundaries?

## 5. Actually Give Access to Everything

It’s obvious that software developers need access to the code they should maintain. But you might also want to think about all of the other documents (e.g. in Confluence, Google Drive, Schematic images on Mural/Draw.IO/Lucidchart). Make sure you link to them from the README of your software project.

They might need access to different environments besides local (e.g. a staging environment) or several of them.

They might need access to accounts (e.g. for AWS). Where do your logs live? Where are errors collected? Where are bugs, issues, stories, and tasks collected?

Oh, and please don’t only give them access. Make sure they know how to use the resources.

## 6. Give Pointers on Where To Start

What are the core classes/objects/functions of the software?

Where does the execution start? What is used most often? Which parts of the code base are rather stable and which need frequent adjustments?

## 7. Point Out Work in Progress

Software is never finished. It evolves all the time. There is always work to do.

What are the next tasks for your project? Where is work that was started but never finished?

## 8. Talk About Processes

How do you handle new releases? How do deployments work? Who are the people who need to be informed in case of critical bugs? What do you consider an incident and how do you handle it? How do you handle backups? Does every change need to have a pull request and a review?

## 9. Review and Be Reviewed

Make a non-trivial change and let the other person review it. Maybe even go through the code when they review it. Point out what they need to check and explain why you implemented the change how you did.

If that worked, reverse it. Let the other person make a change and review it. Make sure you point out details (e.g. when the order of arguments breaks with the typical choice throughout the library or when the naming scheme of a REST endpoint is a bit different from the rest). You know those points, but the other person might not even be aware that one can be consistent in those aspects.
