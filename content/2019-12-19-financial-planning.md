---
layout: post
lang: en
title: Financial Planning
slug: financial-planning
author: Martin Thoma
date: 2019-12-18 20:00
category: My bits and bytes
tags: Money
featured_image: logos/money.png
---
Recently I started to think way more seriously about my finances. I think I
should have done that more than 5 years ago and I guess this is the case for
many people.

I think about it in goals similar to [Maslow's hierarchy of needs](https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs):

1. *Basic Needs*: Rent, Food, Insurances, Communication
2. *Extended Needs*: Hobbies
3. *Retirement*: House, Monthly cost

No matter what I do, I don't want to risk my appartment. I don't want to risk
having enough food and I don't want to risk that I can't afford my insurances.

## Needs

### Basic Needs

<table class="table">
    <thead>
        <tr>
            <th>Item</th>
            <th>EUR / Month</th>
            <th>EUR / Year</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Rent</th>
            <td>510</td>
            <td>6120</td>
            <td>This includes everything: Heating, electricity, waste (<a href="https://de.wikipedia.org/wiki/Nebenkosten">Nebenkosten</a>)</td>
        </tr>
        <tr>
            <th>Food & Hygene</th>
            <td>150</td>
            <td>1800</td>
            <td>This might be hard to estimate. If you have a seperate bank account or pay in cash, you can just check what is currently the case.</td>
        </tr>
        <tr>
            <td>Transportation</td>
            <td>86</td>
            <td>1032</td>
            <td><a href="https://www.mvg.de/tickets-tarife/vielfahrer/isarcard.html">IsarCard M</a> and 30 EUR for visiting people outside of Munich</td>
        </tr>
        <tr>
            <td>Communication</td>
            <td>0</td>
            <td>0</td>
            <td>In my case Internet is included in the rent and I can use the work phone for the few calls I need make</td>
        </tr>
        <tr>
            <td>Clothes</td>
            <td>50</td>
            <td>600</td>
            <td>This is super hard to estimate. I basically have no idea how to do this well</td>
        </tr>
        <tr>
            <td><a href="https://en.wikipedia.org/wiki/Liability_insurance">Liability insurance</a></td>
            <td>3.34</td>
            <td>40.08</td>
            <td></td>
        </tr>
        <tfoot>
            <tr>
                <th>Sum</th>
                <th>800</th>
                <th>9592</th>
                <th></th>
            </tr>
        </tfoot>
    </tbody>
</table>

According to [numbeo](https://www.numbeo.com/cost-of-living/city-estimator/in/Munich)
I should consider a monthly cost of 1293&thinsp;EUR. They think I should rather
calculate with 200 EUR / month for food and only 32 EUR / month for clothes.


### Extended Needs

This is highly personal. To give you some ideas:

* Bouldering: 600 EUR / year = 50 EUR / month
* Vacation: 600 EUR / year = 50 EUR / month
* Books: 40 EUR / month
* Dating: 25 EUR / month
* Going in a restaurant once a month: 25 EUR / month
* Going to the cinema once a month: 10 EUR / month

That would be 200 EUR / month.


### Retirement

Now this is an interesting one. How much money do I need to live the rest of my
live? You could say that it is simply "Basic Needs" + "Extended Needs". Keep in
mind that both points will sharply increase when you have children. Also, as an
eldery person you might have different needs compared to your current
situation. On the one hand, you might be able to live in a location which is
way cheaper as you don't need to be close to your job. On the other hand, you
might need to be close to doctors or you might need to live in the ground
floor.

Considering those is hard on its own. Let's say you want 1500 EUR / month.


## Planning

The amount of money in "Basic Needs" can be used in two ways:

* **Security**: I want to have at least 3 months on my bank account at all
  times. This is money which should only be touched when the shit hits the fan.
  Not for Christmas spendings. I have a hard time even saying what that could
  be ... maybe when my employer would suddenly stop paying me?
* **Minimum Income**: This much money I need to make every month, no matter
  what.

The money you can invest is Income - Basic Needs - Extended Needs. Now we get
to the interesting point.


### When is it enough?

When could you happily retire and live from your fortune?

Assume you were 30 years old and expect to become 90 years old. This means
there are still 60 years to cover. With the 1500 EUR / month from the
retirement section, this would mean you need 1&thinsp;080&thinsp;000 EUR. But
it does not consider interest.

Let's assume that you would get 3% interest (excluding inflation). Assuming you
have a fortune of $F$ you would need:

\begin{align}
    0.03 \cdot F &= 1500 \text{EUR / month} \cdot 12 \text{months}\\
    F &= 600000 \text{EUR}
\end{align}

Once you reach one of the two points, you don't need to work anymore.


### Investments

#### Transactional account

A [transaction account](https://en.wikipedia.org/wiki/Transaction_account) (aka
current account or checking account) is not for investment. It is for daily
business. You can make some money when you use reward programs for changing
banking accounts, but that's it. In many cases they also cost money. And this
does not even consider inflation.


#### Certificate of deposit

A [Certificate of deposit](https://en.wikipedia.org/wiki/Certificate_of_deposit)
is one of the simplest and savest financial products you can get. You are
guaranteed to get the money back. However, the interest is pretty low. At the
moment, if you invest for 5 years you get about 0.6%. Inflation is at 1.5%,
meaning you lose money.


#### Crowdfunding

You can invest in many different things via crowdfunding:

* [Exporo](https://en.wikipedia.org/wiki/Exporo): Real estate
* [Kickstarter](https://en.wikipedia.org/wiki/Kickstarter): Business ideas

I don't like them too much as I miss transparency.


#### Exchange Traded Funds

I like [ETFs](https://en.wikipedia.org/wiki/Exchange-traded_fund). The most
important difference between ETFs is the index they track. Besides that:

* Replication: Physical or Synthetical
* TER
* Currency
* Type of distribution: Accumulating vs Distributing
* Rebalancing-Intervall: Quarterly

If you want to build up a fortune, you should invest in accumulating ETFs. If
you want to live from your money right now, you should invest in distributing
ETFs.

If you invested in [DE000ETF9504](https://www.finanzen.net/etf/comstage_1_euro_stoxx_50r_ucits_etf)
a year ago, you would have gotten +23.9%, but please notice that it dropped in
value after the first year!
