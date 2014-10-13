---
layout: post
title: Trust in a Modern World
author: Martin Thoma
date: 2014-03-20 21:09
categories:
- Cyberculture
tags:
- Science
- Trust
featured_image: logos/web.png
---

Cutting edge science is difficult to understand. Unless it is your field of
study you might not even be able to understand well-established and accepted
facts that are hundrets of years old (thinking of the
[Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)).
But we don't have to understand everything. We trust some people and their
decisions who to trust. So we build a social web of trust. However, there is
not only one web. You might believe almost everything what a professor at
university tells you about his field of excellence. This trust might also spread
to fields that are connected, but at some point you will say that this is no
longer a topic where you rely on his expertise.

So we have connections between people and connections between topics.
How strong topics are connected depends on the people.

## Old World Trust

In the world before the Internet, trust is build by social indicator. You talk
to people, you compare your knowledge and you figure out what the strengths of
the other one is.

Institutions, exams and degrees are also indicators that lead to trust. MIT has
a high reputation and people value degrees from MIT.

In the scientific community we also have publications. The so called
"peer-reviewed journals", conference papers and probably books are an important
factor to get a high reputation in a given field.

## Problems of Old World Trust

Trust like it was described above is hard to measure. That means if you are
new to a field you probably cannot even find a single person who you could
trust.

Another problem is that in todays world you might more often get exposed to
different fields where you would like to check the current state of knowledge.
Eventually you also want to get a feeling for certainty of a fact and competing
theories.

Think of the hilarious debats you can find in the Internet about creationism vs.
evolution. Both are competing theories, both have supporters. For example,
[this paper](http://link.springer.com/article/10.1007%2Fs13752-011-0007-1) might
make you think that Darwins evolution theory is wrong. However, as you are not
an expert in the are and you don't want to become one, it would be nice if you
could easily find what is currently "consent".

## Current automatic measures

Currently, there are a few measures that can be automatically calculated. They
could give an indicator whom to trust. However, there are so many of them.
There is no complete system where you have many fields and can simply query
people, journals or institutions. I could not find a single measure where you
can adjust the measure by personal experience. Or where you can compare
competing theories.

### For People

The so called [h-index](https://en.wikipedia.org/wiki/H-index) is calculated
like this:

> A scientist has index $h$ if $h$ of his/her $N_p$ papers have at least $h$
> citations each, and the other $(N_p − h)$ papers have no more than $h$
> citations each.

The $h$ index values publications and citations. However, it does not
distinguish where it was published. Of course, one could simply say in advance
that one does only count publications and citations in a given set of journals.
But then you have the problem that you have to choose the journals. So you
move the problem: Which journals do you trust?
The next problem is that some authors might not want to publish in those
journals for other reasons (see [Open Access and the Boycott of Elsevier! Let uns not stop here and take the digital revolution one step further!](http://www.rene-pickhardt.de/open-access-and-the-boycott-of-elsevier-let-uns-not-stop-here-and-take-the-digital-revolution-one-step-further/)).

### For Publications

The [Eigenfactor](https://en.wikipedia.org/wiki/Eigenfactor) measures the
importance of a journal. Another one is the
[impact factor](https://en.wikipedia.org/wiki/Impact_factor)

### For Institutions

There are multiple rankings for universities. The Wikipedia article
[College and university rankings](https://en.wikipedia.org/wiki/College_and_university_rankings)
gives an overview of those.

## A new approach

I was thinking about this problem for quite a while. I did not come up with a
solution that is very good. However, one piece to a solution might be the following:

People could set up XML documents where statements are made and where a theory
is explained. Exaples could be

```xml
<theory>
    <name>Evolution</name>
    <definition>
        <name>Natural selection</name>
        <statement>Natural selection is the gradual process by which biological
                   traits become either more or less common in a population as a
                   function of the effect of inherited traits on the
                   differential reproductive success of organisms interacting
                   with their environment.</statement>
    </definition>
    <statement>Over thousands of years many variations of animals developed by
               random mutations. Together with natural selection this lead
               to live on earth as we know it.</statement>
</theory>
```

and

```xml
<theory>
    <name>Creationism</name>
    <definition>
        <name>God</name>
        <statement>An immortal, omnipresent, omnipotent being.</statement>
    </definition>
    <statement>God made it. Species do not change, but were created.</statement>
</theory>
```

Then people could state in a structured way what they think is true. Then people
could query a database for that. This would not have to be a centralised system,
but could be simple web pages with links. A variation of the page rank algorithm
could be used to propagate trust and see competing theories.