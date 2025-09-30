---
layout: post
lang: en
title: Funny Machine Learning
slug: funny-ml
author: Martin Thoma
date: 2019-12-31 20:00
category: My bits and bytes
tags: Machine Learning, Funny
featured_image: logos/data-science.png
---
Machine Learning brings awesome results, but sometimes it fails. And sometimes
it fails in a funny way 😁

<div class="info">This is an article I had for quite a while as a draft. As part of my yearly cleanup, I've published it without finishing it. It might not be finished or have other problems.</div>

## Item To Item Recommendations

<table class="table">
    <thead>
        <tr>
            <th>Source</th>
            <th>Recommendation</th>
            <th>Reason</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Hitler:_The_Rise_of_Evil">Hitler: The Rise Of Evil</a></td>
            <td><a href="https://en.wikipedia.org/wiki/Being_Elmo:_A_Puppeteer%27s_Journey">Being Elmo: A Puppeteer's Journey</a></td>
            <td>Both are documentaries</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Fuck_(film)">F**k</a></td>
            <td><a href="https://en.wikipedia.org/wiki/In_the_Womb">In the Womb</a></td>
            <td>Both are documentaries</td>
        </tr>
        <tr>
            <td><a href="https://de.wikipedia.org/wiki/Death_Wish_3">Death Wish 3</a></td>
            <td><a href="https://en.wikipedia.org/wiki/Bible_Collection">The Bible Collection</a> Vol.03 Moses </td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/The_Exorcist_(film)">The Exorcist</a></td>
            <td><a href="https://en.wikipedia.org/wiki/The_Last_Temptation_of_Christ">The Last Temptation of Christ</a></td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Child%27s_Play_3">Child's Play 3</a></td>
            <td>Michael Jackson: The Life of a rockstar</td>
            <td>Probably using the free-text for creating the recommendation[^1]</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Children_of_Men">Children of Men</a></td>
            <td><a href="https://en.wikipedia.org/wiki/WALL-E">WALL-E</a></td>
            <td></td>
        </tr>
        <tr>
            <td>Led Zepplin + Enron + <a href="https://en.wikipedia.org/wiki/Downfall_(2004_film)">Downfall</a></td>
            <td><a href="https://en.wikipedia.org/wiki/The_Nazis:_A_Warning_from_History">The Nazis</a></td>
            <td></td>
        </tr>
        <tr>
            <td>Maximum Overdrive</td>
            <td>Holy Bible: King James Version</td>
            <td></td>
        </tr>
        <tr>
            <td>Dracula</td>
            <td>A Charlie Brown Christmas</td>
            <td></td>
        </tr>
        <tr>
            <td>The Killers</td>
            <td>The Looney Tunes Golden Collection: Vol. 5</td>
            <td></td>
        </tr>
        <tr>
            <td>The Exorcist</td>
            <td>Where The Red Fern Grows</td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Butter_(1998_film)">Butter</a></td>
            <td><a href="https://en.wikipedia.org/wiki/Toast_(film)">Toast</a></td>
            <td>[^2]</td>
        </tr>
        <tr>
            <td>Sesame Street</td>
            <td>Breaking Bad</td>
            <td>[^2]</td>
        </tr>
        <tr>
            <td>My 600LB Life</td>
            <td>Discover Planet Ocean</td>
            <td>[^2]</td>
        </tr>
        <tr>
            <td>My 600LB Life</td>
            <td>The Whale</td>
            <td>[^2]</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/9_(2009_animated_film)">9</a></td>
            <td><a href="https://en.wikipedia.org/wiki/8%C2%BD">8 1/2</a></td>
            <td>Titles are somewhat similar[^3]</td>
        </tr>
        <tr>
            <td>Sophia the First</td>
            <td>The Human Centipede: First Sequence</td>
            <td>[^3]</td>
        </tr>
        <tr>
            <td>Happy Feet</td>
            <td>Tappy Toes</td>
            <td>[^3]</td>
        </tr>
    </tbody>
</table>


## Clustering

<table>
    <thead>
        <tr>
            <th>Cluster</th>
            <th>Element</th>
            <th>Why</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Movies about Parenthood</td>
            <td><a href="https://en.wikipedia.org/wiki/Poltergeist_(1982_film)">Poltergeist</a></td>
            <td>Life is pleasant for the close-knit Freeling family until a host of otherworldly forces invades their peaceful suburban home.[^2]</td>
        </tr>
        <tr>
            <td>African-American Fight the System Movies</td>
            <td><a href="https://de.wikipedia.org/wiki/Dr._Dolittle_2">Dr. Dolittle 2</a></td>
            <td>The actor is African-American[^1]</td>
        </tr>
        <tr>
            <td>Violent Movies</td>
            <td>March of the Penguins</td>
            <td></td>
        </tr>
        <tr>
            <td>Strong Female Lead</td>
            <td>Justin Bieber: Never Say Never</td>
            <td>[^2]</td>
        </tr>
        <tr>
            <td>Feel-good Movies</td>
            <td>The Cabin in the Woods</td>
            <td>[^3]</td>
        </tr>
    </tbody>
</table>


## Autocorrect

<table>
    <tr>
        <td>Dumb and Dumber</td>
        <td>Faith and Spirituality</td>
        <td>[^2]</td>
    </tr>
</table>


## Sentence Completion

<a href="https://talktotransformer.com/">talktotransformer.com</a> gives so many possibilties to have fun xD

```text
<b>If you compare Nazis to Unicorns </b> you will notice the big difference. Nazis are literally evil men who are trying to kill people, Unicorns are magical fairies who want to rescue the world from death. <mark>In many ways, Unicorns are evil too.</mark> Unicorns (as humans call them) often fall in love and become involved in "love games" where the pair has to outsmart, out-shout, out-kill, out-kill, out-fight, out-kill, etc. until one of them "loses" and falls apart in the process. This is not unlike the "war between light and darkness" where one side tries to take over and stop a whole group of creatures from doing their job.
This does not make the Unicorns evil or the Nazis evil or anything. It is merely how different our human cultures view this aspect of love.
The concept that a man could love more than another man is one of the oldest things we have for ourselves. We have this idea that "love is more important than everything else" and we put so much effort into putting
```

and

```text
<b>Trump thinks about Unicorns </b> as if they're actual people, just like us.  He's aware, of course.  So he understands the psychological toll they must take on their owners, his superiors, his followers.  Because he is an intellectual.  And when you are an intellectual, as he is, your view of the world is limited to the intellectual world.  So he's a big-hairy, hairy-minded unicorn.  His view is limited to the unicorn world: the big, big one, where a unicorn goes through his adventures in full costume.
But we Unicorns think of our lives as real things.  We are real, tangible, flesh and blood things that happen to us, like people you meet on a cross street. What about those who are non-human creatures by human standards?  We like them.  We want them.  We need them.  They're in our lives, too.  We want to be around them.  We want to feel like we,
```


## Footnotes

[^1]: https://worldwideinterweb.com/funniest-netflix-suggestions-ever-25-photos/
[^2]: https://www.ranker.com/list/weird-netflix-photos/nathandavidson
[^3]: https://www.funnyordie.com/2013/7/8/17702770/6-ridiculous-netflix-suggestions
