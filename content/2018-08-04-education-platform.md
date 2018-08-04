---
layout: post
title: Education platform
slug: education-platform
author: Martin Thoma
date: 2018-08-04 20:00
category: My bits and bytes
tags: Education
featured_image: logos/education.png
---
Learning is a core part of human development. Children want to understand the
world, adults want to improve their lifes and as a society we want advancement.
Education still faces serios inequality problems (<a href="https://m.metrotimes.com/news-hits/archives/2018/07/02/us-court-detroit-students-have-no-right-to-access-to-literacy">example</a>). In some cases because
educational material is too expensive, in many cases because having a good
teacher is still a bit related to luck. And in many cases this has not to be
the case. We have the technical infrastructure in many countries to deliver
awesome educational resouces to most people. But we lack the software.

This post is work in progress. I would like to build and deploy an improved
platform for teaching and learning. I've been thinking about this for quite a
while and very often I'm blocked by the complexity of the task. Although the
[current draft](https://martin-thoma.com/pdf/education-portal.pdf) is far
from being finished, I think it's important to start sharing ideas. A talk with
my flat mate gave me many more ideas. Thank you, Thomas!


## Existing Education Platforms

I usally try to see if the problem I want to solve already has a solution that
I can work with or improve upon. Here is the summary of it.

The "width" column indicates how many different areas of knowledge the platform
offers. The depth knowledge gives you a clue how sophisticated it can get.
The "students" and "creators" columns tell you how easy it is to access and how
the user experience (UX) for them are. The column "atomic" column tells you if
the platform supports creating a lesson for only one single small topic, e.g.
only a single page.

<table class="table">
    <thead>
    <tr>
        <th rowspan="2"></th>
        <th rowspan="2">Width</th>
        <th rowspan="2">Depth</th>
        <th colspan="2">Students</th>
        <th colspan="2">Creators</th>
        <th rowspan="2">Atomic</th>
        <th rowspan="2">Requirements</th>
    </tr>
    <tr>
        <th>UX</th>
        <th>Openness</th>
        <th>UX</th>
        <th>Openness</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th>Wikipedia</th>
        <td>5/5</td>
        <td>&nbsp;2/5 to 5/5</td>
        <td>2/5</td>
        <td>5/5</td>
        <td>1/5</td>
        <td>3/5</td>
        <td><span color="green">✓</span></td>
        <td><span color="red">✘</span></td>
    </tr>
    <tr>
        <th>Coursera</th>
        <td>2/5</td>
        <td>4/5 to 5/5</td>
        <td>4/5</td>
        <td></td>
        <td>?</td>
        <td>?</td>
        <td><span color="red">✘</span></td>
        <td><span color="red">✘</span></td>
    </tr>
    <tr>
        <th>YouTube</th>
        <td>5/5</td>
        <td>2/5</td>
        <td>2/5</td>
        <td>5/5*</td>
        <td>2/5</td>
        <td>4/5</td>
        <td><span color="green">✓</span></td>
        <td><span color="red">✘</span></td>
    </tr>
    <tr>
        <th>Duolingo</th>
        <td>1/5</td>
        <td>3/5</td>
        <td>5/5</td>
        <td>5/5</td>
        <td><span color="red">✘</span></td>
        <td>0/5</td>
        <td><span color="red">✘</span></td>
        <td><span color="red">✘</span></td>
    </tr>
    <tr>
        <td>edX</td>
        <td>3/5</td>
        <td>5/5</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td><span color="red">✘</span></td>
        <td><span color="red">✘</span></td>
    </tr>
    </tbody>
</table>


All of the projects I found have at least one of the following problems:

* **Width**: Their scope is too narrow, e.g. Duolingo is only for learning
  languages.
* **Depth**: YouTube videos are great for introducing a topic, but for diving
  deep you need to get active and complete some excercises.
* **User Experience**: The design is not good for supporting learning.
* **Openness**: Courses expensive or only partially available.


### Wikipedia

Wikipedia is an encyclopedia. It is supposed to be a reference work. It should
summarize all branches of knowledge and give references to the single
fact-pieces.

There is also <a href="https://en.wikipedia.org/wiki/MediaWiki">MediaWiki</a>,
the software behind Wikipedia. This software was used to build
<a href="https://en.wikipedia.org/wiki/Wikiversity">Wikiversity</a>. On Wikiversity,
you can find courses:

* [Assistant teacher course](https://en.wikiversity.org/wiki/Assistant_teacher_course)
* [Spanish 1](https://en.wikiversity.org/wiki/Spanish_1)
* [Electric Circuit Analysis](https://en.wikiversity.org/wiki/Electric_Circuit_Analysis)
* ...

So Wikiversity is a platform for [open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources) (OER).

People can use [images](https://commons.wikimedia.org/wiki/Category:Quality_images_by_Martin_Thoma), [videos](https://commons.wikimedia.org/wiki/File:Movement_of_organelles_in_Tradescantia_stamen_hair_cells.webm), [audio files](https://en.wikipedia.org/wiki/File:Becerra_string_quartet_4_-_1allegro.ogg) and even [PDF files](https://commons.wikimedia.org/w/index.php?title=File%3A05_Wikipedia_Qualitaet_Upload.pdf&page=12) to teach. I'm not sure of
JavaScript.

What I think can be improved:

* **Learners' UX**:
    * Finding courses that fit to your knowledge is hard
    * The general design is ... well, I'm not sure how to describe it. It could
      be posished more. Removing the clutter.
* **Teachers' UX**:
    * MediaWiki does not support Markdown
    * I don't think you can write HTML


### Coursera

Coursera is one of the best MOOC websites I know: It has 1 - 15 minute videos
which usually don't cover more than one topic, questions which keep you
engaged, the possibility to discuss the topic with fellow students. It's design
is beautiful and clean.


The main problem with it is the lack of openness. I have no idea how I could
add content to Coursera. Additionally, as a student, I think 41 EUR per month
is quite expensive.

And there are similar, but worse ones:

* Udemy: [Why Udemy is Bad](https://www.youtube.com/watch?v=X7jf70dNrUo)


### YouTube

YouTube is a website owned by Google which allows users to upload pretty much
any video. I think there are some constraints on the video length and once in a
while users run into - wrong - content filter problems due to digital rights
management.

On YouTube, you can find courses for:

* [Civil Engineering](https://www.youtube.com/watch?v=0olpSN6_TCc&list=PLTZM4MrZKfW8Saqr34bzDBN3FBYSoek5A&index=1)
* [Statistics](https://www.youtube.com/watch?v=zouPoc49xbk&list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr&index=1)
* [Physics](https://www.youtube.com/watch?v=BqKeiiezqzc&index=100&list=PL908547EAA7E4AE74)

The main problem with YouTube as a learning platform is the format. Video is
heard to index / search by website crawlers, it is hard for the user to find
a very specific part and it is super hard to create good videos. There is a
reason why you don't have many awesome video lectures.


### Single Websites
Once in a while, single people or small groups of people take the effort to
create content for others to learn from. Examples are:

* Fendt, Walter: [Physik Applets](http://www.walter-fendt.de/html5/phde/) (de)
* [Leifi Physik](https://www.leifiphysik.de) (de)
* Thoma, Martin: [Chemie](http://www.martin-thoma.de/chemie/) (de)

The problem of single websites is their limited scope. Most often, they are
driven by individuals. Once the individuals stop, the project will likely become
outdated or might simply not be available any longer. Also, you have to find those
sites and


## Relevant Elements

Things I want to have for an education platform:

* Discussion pages: It's important that you can talk about the stuff you learn.
  And the material might have errors.
* Flexible content: Allow all reasonable forms - pure text, images, PDFs,
  animations, videos, podcasts. People want to teach in different forms and
  they want to learn in many forms. Let them do it.
* Search: Make a clever tagging system which allows people to find the courses
  that suit best to them.


## Drafts


