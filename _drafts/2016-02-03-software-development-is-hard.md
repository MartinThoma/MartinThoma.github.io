---
layout: post
title: Why Software Development is Hard
author: Martin Thoma
date: 2014-11-22 17:19
category: Cyberculture
tags:
- Development
featured_image: logos/star.png
---
Programming is like writing a recepie for a really, relly stupid but very
accurate person.<sup>[<a href="#target-audience" name="target-audience-ref">a</a>]</sup>
From this fact come jokes like:

> A programmer is told by his wife:
> "Buy a gallon of milk, and if there are eggs, buy a dozen."
> So the programmer goes, buys everything, and drives back to his house.
> Upon arrival, his wife angrily asks him, "Why did you get 13 gallons of milk?"
> The programmer says: "There were eggs!"


Software development is not only writing the recepie, but also structuring it
in a way that parts can get used for other recepies, that it is easy to find
where you can make adjustments, keeping in mind that some ingredients might
not always be available, that one might want to translate it with minimum
effort, ...

You might think, well, ok, I get it. You have to think a lot ahead. But I even
if you have worked for little projects, I guess the following might be new for
you.

This is about "Falsehoods Programmers Believes"


## Gender

When you write a web project, you sometimes want to save the gender of a
person. It might be something simple like figuring out which way to call the
user / write to the user is correct. Is it "Mr. Smith" or "Mrs. Smith"?
Or you might want to get some demographic information, dating functionality,
matching functions for social stuff, surveys.

But it is not as simple as "male", "female", "I don't want to answer".

The following list is from [cscyphers.com](http://www.cscyphers.com/blog/2012/06/28/falsehoods-programmers-believe-about-gender/) and gives you an impression of how difficult
it can get once you think about it (I've copied it here, because it seems to be
down - I've also added some examples):

1. There are two and only two genders.<br/>
   &rightarrow; [Third gender](https://en.wikipedia.org/wiki/Third_gender), [Transsexual](https://en.wikipedia.org/wiki/Transsexual)
2. Okay, then there are two and only two biological genders.
3. Okay, it's mostly determined by biology, right?
4. Please tell me it's determined by DNA.
5. Gender can be reliably determined through visual means. After all, no man would ever wear a burka.
6. Once gender is set, it never changes.
7. Even if the gender can change, it will only change from the one value to the other value.
8. Only one gender can be “active” at the same time.
9. We're tracking gender now, so we’ve always tracked it.
10. I only need to be concerned with human gender.
11. People have a gender.<br/>
    &rightarrow; [Agender](https://en.wikipedia.org/wiki/Genderqueer#Definitions_and_identity)
12. Gender can only change once.
13. A birth certificate or other legal document will tell you a person's gender.

See also: [medium.com/gender-2-0](https://medium.com/gender-2-0/falsehoods-programmers-believe-about-gender-f9a3512b4c9c#.rwr32ewdo)


## Names

See [kalzumeus.com](http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)


## Geography

See [wiesmann.codiferes.net](http://wiesmann.codiferes.net/wordpress/?p=15187&lang=en)


### Addresses

See [mjt.me.uk](https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/)


## Time
See [infiniteundo.com](http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time) and [part 2](http://infiniteundo.com/post/25509354022/more-falsehoods-programmers-believe-about-time), [part 3](http://puzzling.org/technology/computer-programming/2012/06/more-falsehoods-programmers-believe-about-time/)


## Online Shopping

See [http://wiesmann.codiferes.net](http://wiesmann.codiferes.net/wordpress/?p=22201)


## Computers

### Version numbers

The following list is from [Caleb Cushing](https://github.com/xenoterracide/falsehoods/blob/master/versions.md):

1. versions always increase
1. versions are numbers
1. versions are strings
1. versions are semantic
1. versions are decimals
1. a major number of 1 or above means stable api
1. versions with the same major number will have the same api
1. versions have numbers, periods, and maybe a preceding v
1. semantic is always the best way to go
1. versions are consistent within a project
1. semantic versions will never see double digits or triple digits within dots
1. at least if you're using a semantic version people can compare it correctly
1. versions will be consistent amongst projects in a given language or
   community
1. semantic versioning cannot be represented as number or decimal
1. as long as the versions increase the length of the version doesn't matter
1. if versions have the same number they are equivalent
1. in a given archive all code will have the same version
1. semantic versions can only have 3 positions
1. dates are bad for versions


### Other

* [Falsehoods programmers believe about networks](http://blog.erratasec.com/2012/06/falsehoods-programmers-believe-about.html#.VrHTsrIrLVN)
* [Falsehoods programmers believe about build systems](http://pozorvlak.livejournal.com/174763.html)
* [Fallacies of distributed computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)


## Footnotes

* [<a href="#target-audience-ref" name="target-audience">a</a>] This article
  is mainly aimed at non-developers. It should give people who only know how to
  use a computer by GUI help to get a glimpse of what we (sometimes) have to
  deal with.
