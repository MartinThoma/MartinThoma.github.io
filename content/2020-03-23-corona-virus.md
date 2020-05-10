---
layout: post
title: Coronavirus disease 2019
slug: covid-19
author: Martin Thoma
date: 2020-03-23 20:00
category: My bits and bytes
tags: Medicine, Pandemic, Coronavirus, data science
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
* Germany has 28,000 intensive care beds in hospitals ([source](https://www.mdr.de/wissen/kliniken-krankenhaeuser-deutschland-kapazitaet-corona-100.html)). However, there are still other diseases. So we can't use all of them just for COVID-19 cases.

This means once we have more than 28000/0.05 = 560k new infections per day, we
have a problem.

The infections seem to follow an exponential growth pattern, but that doesn't
make much sense within limited populations. Assuming a [logistic growth
pattern](https://en.wikipedia.org/wiki/Logistic_growth) makes more sense:

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

I was pretty confused when I was trying to calculate those numbers. It seemed as
every scenario which stayed under the capacity of the healthcare system would
take massive measures to reach (isolation) and then also make the pandemic take
at least a year, rather two years. This was confirmed in [^7]. Obviously, it
is not possible to keep those measures up that long.

Now, the interesting part: **Due to economic reasons, we cannot keep
half-isolation measures that we get herd immunity. But we could keep isolation
for a couple of weeks even more extreme so that we can start contract tracing
again.** Mai Thi also gives an example how long it would take with "Wuhan-Style" lockdown
to contain the disease again: 56 days (see [Epidemic Calculator](https://gabgoh.github.io/COVID/index.html)).


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

## Course of disease

A lot of the following is from [Wikipedia](https://en.wikipedia.org/wiki/Coronavirus_disease_2019).

Everything starts with the **infection**. The virus is spread via respiratory
droplets produced when people cough or sneeze[^1]. The virus stays alive outside
of the human body on different materials for an astonishing long time[^2]:

<table class="table">
    <tr>
        <th>Material</th>
        <th>No virus found after</th>
        <th>Estimated livetime</th>
    </tr>
    <tr>
        <td>Copper</td>
        <td>4h</td>
        <td>18h</td>
    </tr>
    <tr>
        <td>Cardboard</td>
        <td>24h</td>
        <td>55h</td>
    </tr>
    <tr>
        <td>Stainless steel</td>
        <td>72h</td>
        <td>90h</td>
    </tr>
    <tr>
        <td>Plastic</td>
        <td>72h</td>
        <td>100h</td>
    </tr>
</table>

After the infection, the following symptoms may appear[^3]. The time between
infection and symptoms is called *incubation period* and is typically five to
six days for COVID-19 but may range from two to 14 days[^4].

There are also [asymptomatic](https://en.wikipedia.org/wiki/Asymptomatic)
cases. That means people have the infection and are infecting others, but don't
show any symptoms. There might be 50% of infected people being asymptomatic[^6].
Please note that I The Guardian gave a source for that number, but within that
source I can't find it.

<table class="table">
    <tr>
        <th>Symptom</th>
        <th>Corona %</th>
        <th>Influenca</th>
    </tr>
    <tr>
        <td>Fever</td>
        <td>87.9</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Dry cough</td>
        <td>67.7</td>
        <td>✔️ (not sure if dry)</td>
    </tr>
    <tr>
        <td>Fatigue</td>
        <td>38.1</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Sputum production</td>
        <td>33.4</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Loss of smell and taste</td>
        <td>30 to 66</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Shortness of breath</td>
        <td>18.6</td>
        <td>✔️ (emergency warning sign)</td>
    </tr>
    <tr>
        <td>Muscle or joint pain</td>
        <td>14.8</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Sore throat</td>
        <td>13.9</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Headache</td>
        <td>13.6</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Chills</td>
        <td>11.4</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Nausea or vomiting</td>
        <td>5.0</td>
        <td>✔️ (rather in children; emergency warning sign)</td>
    </tr>
    <tr>
        <td>Nasal congestion</td>
        <td>4.8</td>
        <td>✔️</td>
    </tr>
    <tr>
        <td>Diarrhoea</td>
        <td>3.7 to 31</td>
        <td>✔️ (rather in children)</td>
    </tr>
    <tr>
        <td>Haemoptysis</td>
        <td>0.9</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Conjunctival congestion</td>
        <td>0.8</td>
        <td>?</td>
    </tr>
</table>

Mild symptoms in an otherwise healthy individual may resolve over just a few
days. Similar to influenza, for an individual with other ongoing health issues,
such as a respiratory condition, recovery may take weeks and in severe cases
could be potentially fatal.[^5]


## Herd immunity

[Herd immunity](https://en.wikipedia.org/wiki/Herd_immunity) is the effect
that, if enough people are immune to a disease, it doesn't spread. This "it
doesn't spread" is hard for me to define more precisely, because it can be that
other people get infected. Just not in an amount which is relevant for the
complete herd.

I tried to find numbers when heard immunity kicks in. According to [^7], it would be 60% - 70%.


## Myth: COVID-19 affects only the elderly

[A Medical Worker Describes Terrifying Lung Failure From COVID-19 — Even in His Young Patients.](https://www.propublica.org/article/a-medical-worker-describes--terrifying-lung-failure-from-covid19-even-in-his-young-patients)

If you want a video of a young person being affected:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iFLSG-7K3Tc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Myth: COVID-19 is less severe than the flu

There is a good [German source](https://www.tagesschau.de/faktenfinder/corona-grippevergleich-101.html):

* Approximately 25,000 people died in Germany in 2017/2018 due to Influenza.
  That year was an outlier. in 2013/2014
  We currently have 1,107 dead people due to COVID-19, but we are just at the
  start. Italy already has 14,000 dead people due to COVID-19.
* We have vaccination against the flu, but not against COVID-19.

A comparison of deaths says more than a thousand words:

<blockquote class="imgur-embed-pub" lang="en" data-id="a/Si6BEgf"><a href="//imgur.com/a/Si6BEgf">It&#39;s just the flu</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>


## Name

The [Coronavirus](https://en.wikipedia.org/wiki/Coronavirus) causes the [Coronavirus disease 2019](https://en.wikipedia.org/wiki/Coronavirus_disease_2019), in short: COVID-19.

It is sometimes also called Wuhan virus ([nature.com, 2020-01-21](https://www.nature.com/articles/d41586-020-00146-w)), Fox News calls it ["chinese" coronavirus (2020-03-12)](https://www.youtube.com/watch?v=QI-9v-TdshU), [Trump, 2020-03-18](https://www.youtube.com/watch?v=7zatCqqRY_I). Especially in the US I have heard the term "foreign virus" pretty often. **Those names should not be used.** It should not be called like this, because it doesn't add anything to the discussion. "Coronavirus" is short, everybody knows what is meant. Adding "Wuhan", "Chinese" or "foreign" only strengthens racism and [Xenophobia](https://en.wikipedia.org/wiki/Xenophobia). There are several other examples of viruses in the past where we didn't use this naming:

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


## Predictions for Germany

Fitting a [generalized logistic function](https://en.wikipedia.org/wiki/Generalised_logistic_function)

$$f(x) = \frac{1}{1 + e^{-b \cdot x + c}}$$

to the data from 2020-02-24 to 2020-03-23 in order to get the total number of
infected people gave the following results.


### Issues

I assumend that at most 64 million people can (and will) become infected.

Please keep in mind that the data is not fixed. If a person gets the results of
the test later, the numbers for a given day might be corrected. And the
corrections are huge.

For 2020-03-20:

* 12,890: What I got from en-wiki at 2020-03-23
* 13,957: What I see on en-wiki at 2020-03-25 (08:25)
* 18,361: [statista.com](https://de.statista.com/statistik/daten/studie/1102667/umfrage/erkrankungs-und-todesfaelle-aufgrund-des-coronavirus-in-deutschland/) (2020-03-25 08:25)
* 19,850: [Berliner Morgenpost](https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/) (2020-03-25 08:25)

So the range is 6960 cases. The highest number is 54% higher than the lowest
one. With such extrem corrections of the current numbers, the predictions must
be pretty bad.

Naturally, the model also does not know about any changes like quarantine or
self-isolation. One could analogize to other countries, but I was too lazy
to implement that.

### Predictions

On the training data:

```text
LogitRegressor(beta=0.198, c=13.460, max_population=64000000.0)
Day 2020-02-24: 91 (+91) predicted vs 16 in reality
Day 2020-02-25: 111 (+20) predicted vs 18 in reality
Day 2020-02-26: 136 (+24) predicted vs 21 in reality
Day 2020-02-27: 165 (+30) predicted vs 26 in reality
Day 2020-02-28: 202 (+36) predicted vs 53 in reality
Day 2020-02-29: 246 (+44) predicted vs 66 in reality
Day 2020-03-01: 300 (+54) predicted vs 117 in reality
Day 2020-03-02: 365 (+66) predicted vs 150 in reality
Day 2020-03-03: 445 (+80) predicted vs 188 in reality
Day 2020-03-04: 543 (+97) predicted vs 240 in reality
Day 2020-03-05: 661 (+119) predicted vs 349 in reality
Day 2020-03-06: 806 (+145) predicted vs 534 in reality
Day 2020-03-07: 983 (+177) predicted vs 684 in reality
Day 2020-03-08: 1,198 (+215) predicted vs 847 in reality
Day 2020-03-09: 1,460 (+262) predicted vs 1,112 in reality
Day 2020-03-10: 1,780 (+320) predicted vs 1,460 in reality
Day 2020-03-11: 2,170 (+390) predicted vs 1,884 in reality
Day 2020-03-12: 2,645 (+475) predicted vs 2,369 in reality
Day 2020-03-13: 3,224 (+579) predicted vs 3,062 in reality
Day 2020-03-14: 3,930 (+706) predicted vs 3,795 in reality
Day 2020-03-15: 4,790 (+860) predicted vs 4,838 in reality
Day 2020-03-16: 5,839 (+1,049) predicted vs 6,012 in reality
Day 2020-03-17: 7,117 (+1,278) predicted vs 7,156 in reality
Day 2020-03-18: 8,675 (+1,558) predicted vs 8,198 in reality
Day 2020-03-19: 10,575 (+1,899) predicted vs 10,999 in reality
Day 2020-03-20: 12,890 (+2,315) predicted vs 13,957 in reality
Day 2020-03-21: 15,711 (+2,822) predicted vs 16,662 in reality
Day 2020-03-22: 19,151 (+3,439) predicted vs 18,610 in reality
Day 2020-03-23: 23,342 (+4,192) predicted vs 22,672 in reality
```

Let's see when the predictions start to fall apart. They will, because the
training data does not contain the isolation and also there isn't a lot of
training data for Germany.

Here are the [predictions from 2020-03-23](https://gist.github.com/MartinThoma/e35d7ee2cdf288be090ffc822bb53f1b):

```text
Date: Total infections at the end of the day (new infections on that day)
2020-03-24: 28,451 (+5,109) -- was 29,542
2020-03-25: 34,678 (+6,226)
2020-03-26: 42,266 (+7,588)
2020-03-27: 51,513 (+9,247)  -- somewhat accurate until here
2020-03-28: 62,781 (+11,268)
2020-03-29: 76,512 (+13,730)  -- pretty bad from here
```

Now, 2020-03-31, the following regression fits way better. This means the
growth rate was reduced from 19.8% to 15.1%. I'm more positive than the
estimator. I guess we don't have enough data for the quarantine. It would make
most sense to me to analogize with Italy.

Anyway, here you are with the bad estimators estimates:

```text
LogitRegressor(beta=0.151, c=12.220, max_population=64000000.0)
Day 2020-02-24: 316 (+316) predicted vs 16 in reality
Day 2020-02-25: 367 (+51) predicted vs 18 in reality
Day 2020-02-26: 427 (+60) predicted vs 21 in reality
Day 2020-02-27: 496 (+70) predicted vs 26 in reality
Day 2020-02-28: 577 (+81) predicted vs 53 in reality
Day 2020-02-29: 671 (+94) predicted vs 66 in reality
Day 2020-03-01: 781 (+109) predicted vs 117 in reality
Day 2020-03-02: 908 (+127) predicted vs 150 in reality
Day 2020-03-03: 1,056 (+148) predicted vs 188 in reality
Day 2020-03-04: 1,228 (+172) predicted vs 240 in reality
Day 2020-03-05: 1,428 (+200) predicted vs 349 in reality
Day 2020-03-06: 1,661 (+233) predicted vs 534 in reality
Day 2020-03-07: 1,932 (+271) predicted vs 684 in reality
Day 2020-03-08: 2,247 (+315) predicted vs 847 in reality
Day 2020-03-09: 2,613 (+366) predicted vs 1,112 in reality
Day 2020-03-10: 3,039 (+426) predicted vs 1,460 in reality
Day 2020-03-11: 3,535 (+495) predicted vs 1,884 in reality
Day 2020-03-12: 4,111 (+576) predicted vs 2,369 in reality
Day 2020-03-13: 4,781 (+670) predicted vs 3,062 in reality
Day 2020-03-14: 5,560 (+779) predicted vs 3,795 in reality
Day 2020-03-15: 6,466 (+906) predicted vs 4,838 in reality
Day 2020-03-16: 7,520 (+1,054) predicted vs 6,012 in reality
Day 2020-03-17: 8,745 (+1,226) predicted vs 7,156 in reality
Day 2020-03-18: 10,170 (+1,425) predicted vs 8,198 in reality
Day 2020-03-19: 11,828 (+1,657) predicted vs 10,999 in reality
Day 2020-03-20: 13,755 (+1,927) predicted vs 13,957 in reality
Day 2020-03-21: 15,997 (+2,242) predicted vs 16,662 in reality
Day 2020-03-22: 18,603 (+2,607) predicted vs 18,610 in reality
Day 2020-03-23: 21,635 (+3,031) predicted vs 22,672 in reality
Day 2020-03-24: 25,160 (+3,525) predicted vs 27,436 in reality
Day 2020-03-25: 29,259 (+4,099) predicted vs 31,554 in reality
Day 2020-03-26: 34,025 (+4,767) predicted vs 36,508 in reality
Day 2020-03-27: 39,568 (+5,543) predicted vs 42,288 in reality
Day 2020-03-28: 46,013 (+6,445) predicted vs 48,582 in reality
Day 2020-03-29: 53,506 (+7,494) predicted vs 52,547 in reality
Day 2020-03-30: 62,219 (+8,713) predicted vs 57,298 in reality
---
date, predicted accummulated sick, new sick
2020-03-31: 72,349 (+10,130)
2020-04-01: 84,127 (+11,777)
2020-04-02: 97,818 (+13,691)
2020-04-03: 113,734 (+15,916)
2020-04-04: 132,234 (+18,500)
2020-04-05: 153,735 (+21,502)
2020-04-06: 178,724 (+24,988)
2020-04-07: 207,761 (+29,037)
2020-04-08: 241,497 (+33,737)
2020-04-09: 280,688 (+39,191)
2020-04-10: 326,206 (+45,518)
2020-04-11: 379,061 (+52,856)
2020-04-12: 440,422 (+61,361)
2020-04-13: 511,635 (+71,213)
2020-04-14: 594,256 (+82,620)
2020-04-15: 690,073 (+95,817)
2020-04-16: 801,145 (+111,072)
2020-04-17: 929,831 (+128,687)
2020-04-18: 1,078,836 (+149,005)
2020-04-19: 1,251,245 (+172,409)
2020-04-20: 1,450,571 (+199,326)
2020-04-21: 1,680,799 (+230,229)
2020-04-22: 1,946,432 (+265,633)
2020-04-23: 2,252,528 (+306,096)
2020-04-24: 2,604,739 (+352,212)
2020-04-25: 3,009,340 (+404,600)
2020-04-26: 3,473,232 (+463,893)
2020-04-27: 4,003,940 (+530,708)
2020-04-28: 4,609,564 (+605,624)
2020-04-29: 5,298,702 (+689,138)
2020-04-30: 6,080,319 (+781,618)
```

Looking at the US is also interesting:

```text
LogitRegressor(beta=0.206, c=14.536, max_population=262400000.0)
Day 2020-02-24: 128 (+128) predicted vs 14 in reality
Day 2020-02-25: 157 (+29) predicted vs 14 in reality
Day 2020-02-26: 193 (+36) predicted vs 15 in reality
Day 2020-02-27: 237 (+44) predicted vs 15 in reality
Day 2020-02-28: 291 (+54) predicted vs 19 in reality
Day 2020-02-29: 358 (+67) predicted vs 24 in reality
Day 2020-03-01: 439 (+82) predicted vs 42 in reality
Day 2020-03-02: 540 (+101) predicted vs 57 in reality
Day 2020-03-03: 663 (+124) predicted vs 85 in reality
Day 2020-03-04: 815 (+152) predicted vs 111 in reality
Day 2020-03-05: 1,002 (+186) predicted vs 175 in reality
Day 2020-03-06: 1,231 (+229) predicted vs 252 in reality
Day 2020-03-07: 1,512 (+282) predicted vs 353 in reality
Day 2020-03-08: 1,858 (+346) predicted vs 497 in reality
Day 2020-03-09: 2,283 (+425) predicted vs 645 in reality
Day 2020-03-10: 2,806 (+522) predicted vs 936 in reality
Day 2020-03-11: 3,447 (+642) predicted vs 1,205 in reality
Day 2020-03-12: 4,236 (+789) predicted vs 1,598 in reality
Day 2020-03-13: 5,205 (+969) predicted vs 2,163 in reality
Day 2020-03-14: 6,396 (+1,191) predicted vs 2,825 in reality
Day 2020-03-15: 7,858 (+1,463) predicted vs 3,501 in reality
Day 2020-03-16: 9,656 (+1,798) predicted vs 4,373 in reality
Day 2020-03-17: 11,865 (+2,209) predicted vs 5,664 in reality
Day 2020-03-18: 14,579 (+2,714) predicted vs 8,074 in reality
Day 2020-03-19: 17,914 (+3,335) predicted vs 12,022 in reality
Day 2020-03-20: 22,011 (+4,097) predicted vs 17,439 in reality
Day 2020-03-21: 27,046 (+5,035) predicted vs 23,710 in reality
Day 2020-03-22: 33,232 (+6,186) predicted vs 32,341 in reality
Day 2020-03-23: 40,832 (+7,601) predicted vs 42,751 in reality
Day 2020-03-24: 50,171 (+9,339) predicted vs 52,690 in reality
Day 2020-03-25: 61,645 (+11,474) predicted vs 64,916 in reality
Day 2020-03-26: 75,742 (+14,097) predicted vs 81,966 in reality
Day 2020-03-27: 93,062 (+17,320) predicted vs 100,997 in reality
Day 2020-03-28: 114,341 (+21,279) predicted vs 121,105 in reality
Day 2020-03-29: 140,483 (+26,142) predicted vs 141,288 in reality
Day 2020-03-30: 172,598 (+32,115) predicted vs 162,126 in reality
---
2020-03-30: 172,598 (+32,115)
2020-03-31: 212,049 (+39,451)
2020-04-01: 260,508 (+48,459)
2020-04-02: 320,027 (+59,519)
2020-04-03: 393,124 (+73,097)
2020-04-04: 482,887 (+89,763)
2020-04-05: 593,100 (+110,212)  <------- Hit 0.5 million
2020-04-06: 728,397 (+135,297)
2020-04-07: 894,452 (+166,055)
2020-04-08: 1,098,204 (+203,752) <------- Hit one million
2020-04-09: 1,348,131 (+249,927)
2020-04-10: 1,654,576 (+306,445)
2020-04-11: 2,030,137 (+375,561)
2020-04-12: 2,490,130 (+459,993) <------- Trump wants it to be over
2020-04-13: 3,053,127 (+562,997)
2020-04-14: 3,741,581 (+688,454)
2020-04-15: 4,582,533 (+840,951)
```

## How bad is it?

* Hospitals have difficulties getting rid of the dead ([New York](https://www.youtube.com/watch?v=bE68xVXf8Kw))
* Hospitals don't have enough equipment:
    * [Italy: We no longer help those over 60](https://www.jpost.com/International/Israeli-doctor-in-Italy-We-no-longer-help-those-over-60-621856)
    * Twitter: [NHS gets medical equipment from @MedFet_UK (Medical Fetish Organization)](https://twitter.com/MedFet_UK/status/1243590308878848002)
* Supply Chains break
    * [Ethanol](https://www.faz.net/aktuell/wirtschaft/unternehmen/corona-herstellern-von-desinfektionsmitteln-geht-ethanol-aus-16689993.html)
    * [Mexican cartels and leads to shortages of meth and fentanyl](https://www.the-sun.com/news/567928/coronavirus-hits-mexican-cartels-and-leads-to-shortages-of-meth-and-fentanyl-as-chemicals-cant-be-sourced-from-china/)
* Supply of single goods breaks
    * Toilet paper everywhere
    * Personally, I've been searching for rice, flour and oil for a week. Also
      pasta got rare. It's still available once in a while, but not well-stocked.
    * [Condoms](https://www.theguardian.com/world/2020/mar/27/global-condom-shortage-coronavirus-shuts-down-production)
* Many local stores close ([Elbschlosskeller](https://twitter.com/UUlrichson1/status/1239991614099148801?s=20))
* Organized Crime starts to help
    * [Randsomeware Ethics](https://www.bleepingcomputer.com/news/security/ransomware-gangs-to-stop-attacking-health-orgs-during-pandemic/)
    * [Gangs in Rio de Janeiro](https://twitter.com/AndrewCesare/status/1242174265547468803)
* Events get cancelled:
    * 2020-03-12: [Leipziger Buchmesse](https://www.tagesschau.de/inland/corona-deutschland-103.html) - 100,000 visitors expected
    * [Wimbledon](https://us.cnn.com/2020/03/30/tennis/wimbledon-tennis-coronavirus-spt-int/index.html)
    * [Bayreuther Festspiele](https://www.bayreuther-tagblatt.de/bayreuther-festspiele-wegen-coronavirus-abgesagt/)
* Various websites scale down, to reduce network traffic:
    * Sony: [Playstation](https://www.heise.de/newsticker/meldung/Playstation-Network-Sony-verringert-Download-Geschwindigkeit-4689896.html)
    * [Akamai](https://blogs.akamai.com/2020/03/working-together-to-manage-global-internet-traffic-increases.html)


## Side-Effects

* **Online Services**: Companies are highly incentivized to check their remote
  working capabilities, schools and universities have to think about which
  materials they offer online, libraries increase their e-book offer. Even
  churches start to stream the church service. I hope that this permanently
  increases the online material. There are always people who can't leave their
  house. People who might be too old or people who need to stay at hospital.
  There are always people who have time for this at that specific moment.
  People who work multiple jobs or are simply working at other shifts. Adding
  material online makes our society more inclusive.
* **Social Contact**: Yes, we cannot see each other. But at least I started to
  contact more friends and talk more often with family. I'm not the only one
  who does that ([German
  source](https://www.heise.de/newsticker/meldung/In-Deutschland-wird-mehr-und-laenger-telefoniert-4688664.html))
* **Weather Forcasting**: Aparently planes have sensors and contribute their
  data to global weather forecasting. Now that less planes fly, forecasting
  becomes harder. [ADM-Aeolus](https://en.wikipedia.org/wiki/ADM-Aeolus) might help.
* **No school shootings**: [See Twitter](https://twitter.com/RobertKlemko/status/1249716012599083010) -
  I'm not sure if that is related.


## See also

* Statistics:
    * Johns Hopkins University: [Dashboard](https://coronavirus.jhu.edu/map.html)
    * [worldometers.info/coronavirus](https://www.worldometers.info/coronavirus/) - I'm NOT sure how trustworthy they are! The numbers currently roughly match the ones of Johns Hopkins University and they are trustworthy
    * 🇩🇪 Robert-Koch-Institue: [COVID-19: Fallzahlen in Deutschland und weltweit](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) (German)
    * 🇩🇪 Berliner Morgenpost: [Coronavirus-Monitor](https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/) (Map / Dashboard)
    * 🇩🇪 statista.com: [Entwicklung der täglich neu gemeldeten Fallzahl des Coronavirus (COVID-19) in Deutschland seit Januar 2020](https://de.statista.com/statistik/daten/studie/1100739/umfrage/entwicklung-der-taeglichen-fallzahl-des-coronavirus-in-deutschland/)
* Social Distancing
    * [Vox](https://www.youtube.com/watch?v=h9d86ocFlxE)
    * [The math behind why we need social distancing, starting right now](https://www.vox.com/2020/3/15/21180342/coronavirus-covid-19-us-social-distancing)
    * [Australian Government Department of Health](https://www.youtube.com/watch?v=2WCtGFNENYU)
    * 🇩🇪 Harald Lesch: [Coronavirus – unnötiger Alarm bei COVID-19?](https://www.youtube.com/watch?v=Fx11Y4xjDwA) (German)
    * 3Blue1Brown: [Exponential Growth and Epidemia](https://www.youtube.com/watch?v=Kas0tIxDvrg), 2020-03-08 on YouTube.
* [Stack Exchange](https://medicalsciences.stackexchange.com/questions/tagged/covid-19?tab=Votes): I'm not sure how good this is
* [How To Tell If We're Beating COVID-19](https://youtu.be/54XLXg4fYsc)
* Crowdsourcing
    * [COVID-19 Kaggle community contributions](https://www.kaggle.com/covid-19-contributions)
    * [Trajectory of COVID-19 Confirmed Cases](https://aatishb.com/covidtrends/): Explanation at [minutephysics](https://www.youtube.com/watch?v=54XLXg4fYsc)
        * [Countries with more than 100m inhabitants](https://aatishb.com/covidtrends/?country=Brazil&country=China&country=Egypt&country=India&country=Indonesia&country=Japan&country=Mexico&country=Nigeria&country=Pakistan&country=Philippines&country=Russia&country=US)
        * [European Union](https://aatishb.com/covidtrends/?country=Austria&country=Belgium&country=Bulgaria&country=Croatia&country=Cyprus&country=Czechia&country=Estonia&country=Finland&country=France&country=Germany&country=Hungary&country=Ireland&country=Italy&country=Latvia&country=Lithuania&country=Luxembourg&country=Malta&country=Netherlands&country=Poland&country=Portugal&country=Romania&country=Slovakia&country=Slovenia&country=Spain&country=Sweden&country=Switzerland)
    * [Epidemic Calculator](https://gabgoh.github.io/COVID/index.html)
* COVID-19 testing
    * 🇩🇪 [So oft wird auf COVID-19 getestet](https://de.statista.com/infografik/21211/anzahl-der-durchgefuehrten-coronavirus-tests-je-1-mio-einwohner-in-laendern-weltweit/) on statista.com

## Footnotes

[^1]: Centers for Disease Control and Prevention: [How Coronavirus Spreads](https://www.cdc.gov/coronavirus/2019-ncov/prepare/transmission.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fabout%2Ftransmission.html), March 2020.
[^2]: an Doremalen N, Bushmaker T, Morris DH, Holbrook MG, Gamble A, Williamson BN, et al. (March 2020). "[Aerosol and Surface Stability of SARS-CoV-2 as Compared with SARS-CoV-1](https://www.nejm.org/doi/10.1056/NEJMc2004973)". The New England Journal of Medicine. Massachusetts Medical Society.
[^3]: [Report of the WHO-China Joint Mission on Coronavirus Disease 2019 (COVID-19)](https://www.who.int/docs/default-source/coronaviruse/who-china-joint-mission-on-covid-19-final-report.pdf). World Health Organization (WHO). February 2020.
[^4]: [Q&A on coronaviruses (COVID-19)](https://www.who.int/news-room/q-a-detail/q-a-coronaviruses), World Health Organization (WHO). March 2020.
[^5]: [New South Wales](https://en.wikipedia.org/wiki/New_South_Wales) Government: [COVID-19 - Frequently asked questions](https://www.health.nsw.gov.au/Infectious/alerts/Pages/coronavirus-faqs.aspx), March 2020.
[^6]: Danielle Renwick: [Have I already had coronavirus? How would I know and what should I do?](https://www.theguardian.com/us-news/2020/mar/23/have-i-already-had-covid19-coronavirus). 2020-03-24.
[^7]: 🇩🇪 Mai Thi Nguyen-Kim: [Corona geht gerade erst los](https://www.youtube.com/watch?v=3z0gnXgK8Do), 2020-04-01. On YouTube.
[^8]: 🇩🇪 Deutsche Gesellschaft für Epidemiologie: [Stellungnahme der Deutschen Gesellschaft für Epidemiologie (DGEpi) zur Verbreitung des neuen
Coronavirus (SARS-CoV-2)](https://www.dgepi.de/assets/Stellungnahmen/Stellungnahme2020Corona_DGEpi-21032020-v2.pdf), 2020-03-21.
