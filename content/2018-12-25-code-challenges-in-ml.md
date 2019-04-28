---
layout: post
title: Code Challenges in ML
slug: code-challenges-in-ml
author: Martin Thoma
date: 2018-12-25 20:00
category: Machine Learning
tags: Machine Learning
featured_image: logos/ml.png
---
Having machines that can write software is the wet dreem of probably every
company. Instead of having years of development you just tell the machine what
to do and it automatically creates the software.

As you might have guessed, we are not there yet. Not even close. But a friend
of mine made me think about this problem. Being a software engineer, I tried to
split up the problem into smaller chunks that might be in reach.

Before we dive into those sub-problems, let me roughly describe how developing
big software works.


## Software Engineering 101

You have an idea. Let's take one of the [projects I never realized](https://martin-thoma.com/projects-i-never-realized/): A book portal.

We have a name for it, that's good. Book portal. But now we need to get some
details. One tool for that are user stories:

> As a science fiction book enthusiast, I would like to find more books I love.
> I am willing to note a couple of other books I loved, give some general
> restrictions like the language, minimum and maximum length and price range.
> Then I expect some recommendations.

Awesome, now we get a rough idea! So it actually is not a store, but a
recommendation engine!

But non-functional requirements often play a crucial role. Realizing this
project means you have to make sure you know what you want:

* How many books should be recommendable?
* How fast should the user be able to add new books?
* How much time does the recommender have between adding ratings for books and
  spitting out a recommendation?
* What is the minimum quality the recommendation engin needs to be useful?
* How many users are expected at peak times within 15 minutes?
* Is privacy a concern? What are we legaly obliged to do?

Once those questions are answered (especially the load-based ones), you can
draw an architecture. This means you try to find components that can be
developed largely independently. You have to define interfaces; so how those
components are supposed to communicate.

After the architecture, you develop the defined components.

Congratulations, you have an alpha version! Now you can go through the [other stages of Software Development](https://martin-thoma.com/software-development-stages/).


## Code Challenges

Many of the code-challenges are hard because it's not clear how to evaluate the
solutions. There are many possible (acceptable) solutions, but there is no way
to enumerate all of them.


### Architecture Generatation Problem

> Given a document describing the idea, user stories and non-functional
> requirements, generate an architecutre diagram.

I'm not sure how hard this is. It certainly is super hard to evaluate how well
the solution is.


### Equivalence Problem

Given two functions with the same signatures, are they equivalent?

* Why it's hard: Equivalence cannot be proven; hard to construct non-trivial cases
* What's good about it: Non-euqivalence can be proven with one counter-example
* Usefullness: 2/5


### Auto-Doc Problem

Given a function, write the documentation of it.

* Why it's hard: Many equivalent solutions
* What's good about it: Getting training data might be easy
* Usefullness: 5/5


### Code-Generation Problem

Given formal specification, generate code.

* Why it's hard: I'm not sure about the formal specification - how exactly would they look like?
* Usefullness: 3/5

The reason why I think this is not so useful is the specification. At the end,
the most exact specification is a program. Hence, if you need a very formal,
exact specification there is actually no code to generate. When the
specification is imprecise (like natural language), then there is (too much)
room for error.


### Code-Translation Problem

Given code in language A, translate it to equivalent code in language B.

* Why it's hard: Some things might not be possible at all. This would likely be
  the case when you translate C to Python.
* Usefullness: 5/5

The reason why this is super usefull are apps. Imagine if you only had to develop
an App for Android and could automatically translate it to iOS. (By the way: Is that possible with <a href="https://en.wikipedia.org/wiki/React_(JavaScript_library)#React_Native">React Native</a>?)

The key challenge here is to make the translated code maintainable. In some
sense You could say that the *Auto-doc problem* is part of this challenge.

#### Code-Style translation Problem

Code-Style translation Problem is a subtask of the more general
Code-Translation Problem. Imagine a Java-developer writing (correct) Python code.
Things you might see:

* OverlyLongVariableNamesLikeGermanWords
* Too many classes / subclasses where you could simply use `collections.namedtuple` / functions.
* Missing use of syntactic sugar such as `enumerate`, `zip`, list comprehensions

### Refactoring-problem

Given code, generate code with the same functionality which is (a) easier to
maintain (b) faster / more memory efficient (c) applicable to more cases.
