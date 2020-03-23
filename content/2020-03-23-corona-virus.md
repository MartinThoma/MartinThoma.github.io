---
layout: post
title: Coronavirus disease 2019
slug: covid-19
author: Martin Thoma
date: 2020-03-23 20:00
category: My bits and bytes
tags: Medicine, Pandemic, Coronavirus
featured_image: logos/star.png
---
The [Coronavirus](https://en.wikipedia.org/wiki/Coronavirus) runs around the
world and causes many changes in our everyday lives. Correct information is
important so that people behave well.


## What are good sources?

* [World Health Oranization](https://www.who.int/emergencies/diseases/novel-coronavirus-2019): Hands down the source I would trust most
* [Johns Hopkins University](https://coronavirus.jhu.edu/map.html)
* Video: [Kurzgesagt](https://www.youtube.com/watch?v=BtN-goy9VOY)
* German Sources
    * [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
    * Bundesregierung
        * [Informationen zum neuartigen Coronavirus / Covid-19](https://www.infektionsschutz.de/coronavirus/)
        * [Leitlinien gegen Ausbreitung des Coronavirus](https://www.bundesregierung.de/breg-de/themen/coronavirus/leitlinien-bund-laender-1731000)

## What can we do...

### ...now?

* **Hygene**: Wash your hands properly ([video](https://www.youtube.com/watch?v=IisgnbMfKvI))
* **Don't hoard**
* [**Social Distancing**](https://en.wikipedia.org/wiki/Social_distancing)
    * Stay at home
    * Don't meet other people in person
* **Support Others**

#### Social Distancing

The idea behind social distancing is to minimize risk of getting infected. The
less people you talk to, the less often you interact with other humans, the
less risk to spread the virus.

The main point of it is not that you don't get infected (although [you really don't want to get this](https://www.youtube.com/watch?v=iFLSG-7K3Tc)), but that the infection
over the country slows down. Roughly 5% of people who get infected need
intensive care at hospital. We only have a limited amount of beds in hospitals
for intensive care. If we run out of beds, people die. This is what "flatten
the curve" is about.

##### Flatten The Curve

The following summarizes what Harald Lesch discuessed ([video](https://www.youtube.com/watch?v=Fx11Y4xjDwA)).

* 5% of people who get COVID-19 need intensive care at hospital ([source](https://jamanetwork.com/journals/jama/fullarticle/2762130))
* A hospitalized case stays there for 11 days in average ([source](https://www.npr.org/sections/goatsandsoda/2020/03/20/815408287/how-the-novel-coronavirus-and-the-flu-are-alike-and-different))
* Germany has 28,000 intensive care beds in hospitals ([source](https://www.mdr.de/wissen/kliniken-krankenhaeuser-deutschland-kapazitaet-corona-100.html))

This means once we have more than 28000/0.05 = 560k new infections per day, we
have a problem.

The infections seem to follow an exponential growth, but that doesn't make
much sense within limited populations. It's [exponential
growth](https://en.wikipedia.org/wiki/Logistic_growth):

* It starts like exponential growth
* At some point it flattens out to linear growth
* At the end, getting the last few uninfected people, it decays exponentially

Taking this growth model (a [generalized logistic function](https://en.wikipedia.org/wiki/Generalised_logistic_function)) and the
thoughts from before. I also assume that once 20 million people (1/4th of
Germany) was infected, the virus will basically stop due to heard immunity. I
don't know if this is a reasonable assumption. The higher this number needs to
be, the more depressing the picture looks:

<figure class="aligncenter img-thumbnail">
    <a href="../images/2020/03/flatten-the-curve.png"><img src="../images/2020/03/flatten-the-curve.png" alt="The number of new infections by day. Note that the total number of infections in both cases is the same, but the number of people ofer the capacity of hospitals is lower. This means less people die because of missing medical equipment" style="width: 512px;"/></a>
    <figcaption class="text-center">The number of new infections by day. Note that the total number of infections in both cases is the same, but the flatter curve is within the carring capacity of the hospitals. This means no people die because of missing medical equipment.</figcaption>
</figure>

You can find the [code on GitHub](https://github.com/MartinThoma/algorithms/tree/master/Python/covid-19).

However, looking at [the statistics for China](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_in_mainland_China#Statistics), one
can see that the number of sick people decreases after roughly 33 days. So if
other countries have similar strict quarantines, I would expect a similar
behaviour. This would mean for Germany that the most severe time is already
behind us. I guess the truth is somewhere in between. I I would need to to
guess, I would say that the situation will become more severe until maybe 20th
of April and then becomes better.


#### Support Others

Eldery people are at most risk. They should isolate themselves as much as
possible. Maybe you can buy them food? Maybe you can call your (grand) parents
or teach them how to use video chat software like Skype, so that they don't
feel alone.

Medical staff and eldery care staff also needs your help basically the same way
([video, 49s](https://www.youtube.com/watch?v=jmSPOSGpAYs)): Help them to buy
groceries and give them emotional support. They have a pretty stressful time
right now, they are not super well paid, they are in contact with all the sick
people. Remember: You might need them as well.

### ...in future?

Personally, you can do a bit of prepping so that you don't panic when there is
an pandemic:

* Have enough food for 14 days at home, for example pasta, rice, wheat, and oil
* Have toiletries for at least 14 days at home
* Be well-connected with your family and friends
* Have a bike / car, so that you can go alone to the supermarket.
* [Zero Waste](https://en.wikipedia.org/wiki/Zero_waste): If you have re-usable
  stuff, you might need to buy less. For example, [Silicone baking mats](https://www.amazon.com/AmazonBasics-Silicone-Baking-Mat-Sheet/dp/B0725GYNG6) and [cotton handkerchiefs](https://www.amazon.com/Handkerchiefs-Cotton-White-Hankie-Pieces/dp/B01930CBF4) can help.

Companies can move to a remote-first strategy. [Working remotely](https://martin-thoma.com/working-remotely/) has a couple of advantages. It can be supported by:

* Make sure people have a laptop which they can take home
    * Make sure people have a video conference software installed (e.g. Skype)
    * Make sure people have access to everything from outside the company network
* Company-wide chat (e.g. Slack / [Mattermost](https://mattermost.com/))

Schools and the boards of education of countries can finally put the
educational material online, for free. It's about time.

Government agencies can do the same what companies can do, but additionally
make sure that the people don't need to come in person.
[E-government](https://en.wikipedia.org/wiki/E-government) rules.

Countries can make sure they have clear plans what to do. Especially hospitals
need to be equipped (material and people).


## Myth: It affects only the elderly

[A Medical Worker Describes Terrifying Lung Failure From COVID-19 — Even in His Young Patients.](https://www.propublica.org/article/a-medical-worker-describes--terrifying-lung-failure-from-covid19-even-in-his-young-patients)

If you want a video of a young person being affected:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iFLSG-7K3Tc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Name

The [Coronavirus](https://en.wikipedia.org/wiki/Coronavirus) causes the [Coronavirus disease 2019](https://en.wikipedia.org/wiki/Coronavirus_disease_2019), in short: COVID-19.

It is sometimes also called Wuhan virus ([nature.com, 2020-01-21](https://www.nature.com/articles/d41586-020-00146-w)), Fox News calls it ["chinese" coronavirus (2020-03-12)](https://www.youtube.com/watch?v=QI-9v-TdshU), [Trump, 2020-03-18](https://www.youtube.com/watch?v=7zatCqqRY_I). Especially in the US I have heard the term "foreign virus" pretty often. **Those names should not be used.** It should not be called like this, because it doesn't add anything to the discussion. "Coronavirus" is short, everybody knows what is meant. Adding "Wuhan", "Chinese" or "foreign" only strengthens racial biases. There are several other examples of viruses in the past where we didn't use this naming:

* [2009 flu pandemic](https://en.wikipedia.org/wiki/2009_flu_pandemic): Commonly known as swine flu. Nobody said "Mexican virus"
* [2015–16 Zika virus epidemic](https://en.wikipedia.org/wiki/2015%E2%80%9316_Zika_virus_epidemic): Nobody said "Brazilian virus"
* [2002–2004 SARS outbreak](https://en.wikipedia.org/wiki/2002%E2%80%932004_SARS_outbreak#Timeline): Nobody said "Chinese virus" - this also shows another problem. How do you start calling them if there are two different ones?


## Timeline of the Pandemic

* 2019-09-18: sciencemag claims this was the start ([source](https://science.sciencemag.org/content/367/6477/492))
* 2019-11-17: First case of COVID-19 in Wuhan, China.
* 2019-12-31:
    * The chinese pandemic team starts looking at cases in Wuhan after 44 [Pneumonias](https://en.wikipedia.org/wiki/Pneumonia) with unknown origin
    * Taiwan starts screening people
* 2020-01-13: Case in Thailand confirmed
* 2020-01-15: Case in Japan confirmed
* 2020-01-21: First confirmed case in the [United States](https://en.wikipedia.org/wiki/Timeline_of_the_2020_coronavirus_pandemic_in_the_United_States)
* 2020-01-26: 2744 confirmed cases in China, 80 dead. [RKI](https://en.wikipedia.org/wiki/Robert_Koch_Institute) declares Wuhan an risk area.
* 2020-01-28: First confirmed case in [Germany](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Germany) and [Italy](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Italy).
* 2020-01-30: First confirmed case in [India](https://en.wikipedia.org/wiki/Timeline_of_the_2020_coronavirus_pandemic_in_India)
* 2020-01-31:
    * More than 100 cases in Germany
    * First confirmed case in [Spain](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Spain)
* 2020-02-20: First death toll in [Iran](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Iran)
* 2020-02-22: Israel and Libanon confirm first cases
* 2020-02-23: More than 100 cases in Italy
* 2020-02-24: First confirmed cases in Kuwait, Bahrain, Afghanistan, Irak
* 2020-02-25: First confirmed case in [Switzerland](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Switzerland)
* 2020-02-29: More than 1000 cases in Italy
* 2020-03-02: More than 100 cases in Spain
* 2020-03-05:
    * More than 100 cases in the United States
    * More than 100 cases in Switzerland
* 2020-03-09:
    * More than 1000 cases in Spain
    * More than 1000 cases in Germany
    * First confirmed case in Brunei
* 2020-03-10: More than 10,000 cases in Italy
* 2020-03-11: More than 1000 cases in the United States
* 2020-03-12: First death in Indonesia
* 2020-03-13: More than 1000 cases in Switzerland
* 2020-03-17:
    * More than 10,000 cases in Spain
    * More than 100 cases in India
* 2020-03-19:
    * More than 10,000 cases in the United States
    * More than 10,000 cases in Germany

Another way to look at it is by Google searches:

<script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/2152_RC02/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"coronavirus","geo":"","time":"2020-01-01 2020-03-22"},{"keyword":"sex","geo":"","time":"2020-01-01 2020-03-22"},{"keyword":"/m/0cqt90","geo":"","time":"2020-01-01 2020-03-22"}],"category":0,"property":""}, {"exploreQuery":"date=2020-01-01%202020-03-22&q=coronavirus,sex,%2Fm%2F0cqt90","guestPath":"https://trends.google.de:443/trends/embed/"}); </script>

A small timeline:

* 2020-01-21: The Coronavirus became more interesting than Donald Trump
* 2020-01-31: It almost became as interesting as porn/sex
* 2020-02-20: People lost interest again
* 2020-02-24: The Coronavirus became as interesting as porn/sex
* 2020-03-09: The Coronavirus starts to get super interesting - maybe, because
  a couple of countries in Europe start realizing that this is getting out of
  hand.
* 2020-03-15: The Coronavirus hit a maximum.

## See also

* Statistics:
    * Johns Hopkins University: [Dashboard](https://coronavirus.jhu.edu/map.html)
    * [worldometers.info/coronavirus](https://www.worldometers.info/coronavirus/) - I'm NOT sure how trustworthy they are! The numbers currently roughly match the ones of Johns Hopkins University and they are trustworthy
    * Robert-Koch-Institue: [COVID-19: Fallzahlen in Deutschland und weltweit](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) (German)
* Social Distancing
    * [Vox](https://www.youtube.com/watch?v=h9d86ocFlxE)
    * [The math behind why we need social distancing, starting right now](https://www.vox.com/2020/3/15/21180342/coronavirus-covid-19-us-social-distancing)
    * [Australian Government Department of Health](https://www.youtube.com/watch?v=2WCtGFNENYU)
    * Harald Lesch: [Coronavirus – unnötiger Alarm bei COVID-19?](https://www.youtube.com/watch?v=Fx11Y4xjDwA) (German)
    * 3Blue1Brown: [Exponential Growth and Epidemia](https://www.youtube.com/watch?v=Kas0tIxDvrg), 2020-03-08 on YouTube.