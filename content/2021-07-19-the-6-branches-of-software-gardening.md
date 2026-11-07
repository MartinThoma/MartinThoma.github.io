---
layout: post
title: The 7 Branches of Software Gardening
slug: the-6-branches-of-software-gardening
lang: en
author: Martin Thoma
date: 2021-07-19 20:15
category: Code
tags: Software Engineering, Software Quality
featured_image: logos/code.png
summary: Small tasks that keep software maintainable: dependencies, documentation, TODOs, deprecations, training, community, and tooling
medium_url: https://medium.com/@martinthoma/the-6-branches-of-software-gardening-a90b3c0d6220
status: draft
---
Software is evolving all the time. Bugs get fixed, the documentation is improved, it is compiled for new operating systems, ported to other devices, new features are added. New developers get trained and old developers leave the team.

People who think software is once written and then finished got it wrong. Software is like a garden: You have to put effort into it to keep the current quality.

To me, software gardening tasks are small- to medium-sized tasks that you can almost always do. If done regularly, they don’t require a lot of effort. Software gardening makes sure that complex changes in the software can be done more easily. It’s about keeping technical debt low by maintaining the existing software.

After reading this article, you will know 7 different aspects of software gardening.

## 1. Update your Dependencies

Most software heavily relies on other software. Even if you decide that your software is feature-complete, the other software still evolves. Most importantly, **bugs** are found and exploits are developed. That means you need to update your dependency to make sure your software is not vulnerable.

There are other updates of your dependencies that you want. **Features get deprecated** and responsible developers give hints on how to deal with the deprecation. If you don’t update your dependency in this case, you might end up being at a state where your version does not get security updates any longer. And then you need to either patch the software yourself or deal with many deprecations at once. Believe me, that is not fun. Especially when the developers who originally wrote the code are gone.

The last type of update you definitely want to include is security updates. The National Vulnerability Database (NVD) by NIST can be used to figure out what you need to update. For Python software, you can use [safety](https://pypi.org/project/safety/) to get notified. For JavaScript, you can use `yarn audit` or `npm audit`.

Make sure you update all the components of your software system. Those are the direct dependencies, indirect dependencies (transitive dependencies), software installed within the Docker container, your CI/CD pipeline, the operating systems.

## 2. Documentation: Concepts, Processes, Components, Algorithms

Documentation comes in form of naming stuff, comments, tutorials, user guides, algorithms. Let’s go through them one by one.

### Naming Stuff

Finding good names for concepts is hard, but important. Using a common language helps the team to communicate efficiently. You can find more ideas in this direction when you read about behavior-driven development (BDD).

For example, at [Cashlink](https://cashlink.de/) we deal with the tokenization of securities. Think of a solar park where you have 100 people owning 1% of the park each. The share they own is represented by a digital token. That token is first bought when the investors do the initial investment. Creating the token is called *minting*. Sending the token for the first time to the investor is called *issuing*. An investor holds the token in a digital wallet. When the investor *transfers* the token from one wallet they own to another wallet, we say the investor *moves* a token. When the investor transfers the token to another person, we call it *handover*. So we have several words for slightly different types of transfers: Minting, issuing, moving, handover.

Once you have the terminology defined and use it in the same way throughout the company, you can make sure that you name your variables, classes, functions, and methods using that terminology.

### Comments

Very often it is possible to avoid comments by using expressive names and defining functions. For example:

```python
# Bad example
def foo(...):
    # do a
    ...

    # do b
    ...

# Good example
def foo(...):
    do_a(...)
    do_b(...)

def do_a(...):
    ...

def do_b(...):
    ...
```

You can see this in the clean code movement:

[**Stop Writing Code Comments** *“Clean code should read like well-written prose.” — Robert C. Martin*](https://blog.usejournal.com/stop-writing-code-comments-28fef5272752)

However, there are some cases where you do need code comments. For example when you write code because you need to deal with a bug in third-party software. Or when some part of the code is necessary, but you don’t quite understand why.

### How-To’s, Tutorials, and User Guides

Some software is only used by people which are close to you, e.g. friends, family, direct team members, students. If that is the case, they can probably reach out to you if something doesn’t work.

In other cases, you should have some form of how-to / tutorial. The simplest one is a good readme (see point 3 in [my handover article](../9-steps-to-software-project-handovers/)).

A user guide is holistic. It deals with installation instructions, a minimal example of how to use the software, and has links to tutorials/how-tos for more specific topics.

### Architectural overview and Algorithms

Document complex workflows and algorithms as well as the general architecture. Understanding every detail does not mean you understand the whole. The human brain is a perfect example of that. We do understand how neurons work pretty well, but the high-level question of how humans can develop such complex ideas is still not well-understood.

## 3. Fix TODOs: A small refactoring a day keeps the sprint planning away 😜

When I develop software, I sometimes realize that there is a sub-optimal part in the code. However, at that moment I don’t have the time to deal with it. I add some `TODO` comments or a `NOTE` to find this place later and fix it properly.

Try to do those small refactorings when you have the time. Big changes in the codebase need to be planned and aligned with the team. Small ones can be done when you find the time.

I also love the boy scout rule:

> **Always leave the code better than you found it**.

If you want to clean something small up, look for `TODO`, `NOTE`. In Python, you can also look for `type: ignore` and `# noqa`.

## 4. Deprecate Features

Deprecating features is an acquired taste seasoned engineers develop 😄 If a feature gets deprecated and finally removed, you don’t need to test it any longer. You don’t need to maintain it.

Deprecate features whenever it’s reasonable.

And do it in a structured way if your software is used by others:

* Discuss it to figure out what your community thinks about it
* Create a deprecation plan which states in which version a deprecation warning will be added and when it will be finally removed. Document alternatives that can be used.
* Add the deprecation warning according to plan and listen to your users' feedback
* Remove the feature 🎉

A tool that can help you to find dead code in Python projects is [vulture](https://pypi.org/project/vulture/). It doesn’t help to deprecate features, but to find smaller parts that are simply not used anymore.

## 5. Train developers

Software needs developers to maintain it and continue development. Without developers, the software is dead.

I’ve already summarized 9 steps to a good handover. You can also use those ideas for training new developers:

[**9 Steps to Software Project Handovers** *Passing on the baton isn’t a cakewalk. Here’s how to do it*](../9-steps-to-software-project-handovers/)

You should also be aware that developers might find their sweet spots and not know much about other parts of the system. Make sure that they keep learning about the software they are developing.

## 6. Community Building

Software is not built in isolation. We heavily rely on other software to write, build, test, deploy, and run the software. Developers use an ecosystem of existing software.

If you see an issue in that ecosystem, create a ticket. Maybe you can suggest a solution? Can you even create a pull request (PR) that solves the issue?

From a non-technical perspective, you could help others use the same software that you use. You can write documentation, tutorials, and how-tos. You can answer questions on StackOverflow regarding the ecosystem. You can do software gardening in the ecosystem you rely on.

## 7. Tooling Improvements

Some tools require tweaking the code or help to suggest parts where you can simplify the code. Almost all of them do static code analysis:

[**Static Code Analysis for Python** *Type and style checking, potential bugs, and code complexity*](../static-code-analysis/)

You can add those tools to your CI/CD pipeline and thus make it easier to keep the code in good shape, even when new developers join.

## Summary

Updating dependencies, documentation, fixing TODOs, deprecating unused features, training developers, community building, and tooling improvements are 7 branches of software gardening. You can do this for almost every software project at almost any point in time. Doing it regularly keeps your software in shape.
