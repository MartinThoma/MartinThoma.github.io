---
layout: post
title: Earth to Moon
slug: earth-to-moon
lang: en
author: Martin Thoma
date: 2023-09-15 20:00
category: My bits and bytes
tags: Physics, Science
featured_image: logos/earth.png
---
I've just watched an animated movie where a girl goes from Earth to the Moon with
a little toy rocket. That made me think: How much fuel do you minimally need
to get from Earth to the moon and how fast can it be?


## The Distance

The distance between Earth and moon changes. When they are closest it is called
[perigee](https://en.wikipedia.org/wiki/Apsis). That is approximately 360,000
kilometers. At apogee, the point at which the moon is farthest from Earth, the
distance is approximately 405,000 kilometers.
([source](https://www.nasa.gov/sites/default/files/files/Distance_to_the_Moon.pdf)).


Let's take 360,000 km for the remaining article.

## Maximum acceleration humans can endure

Let's completely ignore what is currently technically possible. We just assume
we have that distance on Earth.

Let's say we take 3G of acceleration. That is what astronauts need to endure
during take-off ([source](https://www.sciencefocus.com/science/whats-the-maximum-speed-a-human-can-withstand)).

1G is $9.8 \frac{m}{s^2}$, that means 3G is $29.4 \frac{m}{s^2}$.

With that acceleration, you get from 0 to $100 \frac{km}{h}$

$$v = a \cdot t \Leftrightarrow t = \frac{v}{a}$$

where v is the velocity (speed), a is the acceleration, and t is the time.

That means:

$$t = \frac{100 \frac{km}{h}}{29.4 \frac{m}{s^2}} = \frac{27.8 \frac{m}{s}}{29.4 \frac{m}{s^2}} = 0.95s$$

You get from 0 to 100km/h (62 miles per hour) in less than a second. That is
way faster than any production car ([source](https://en.wikipedia.org/wiki/List_of_fastest_production_cars_by_acceleration#By_acceleration_to_60_mph_(97_km/h)_(less_than_3_seconds))). The Tesla Model S Plaid is at 2 seconds, Ferrari/Porsche/Lamborghini are over 2s.

A 3G acceleration is really freaking fast and super uncomfortable. I guess over
a longer time it is also pretty dangerous for your health.


## Travel time

Assuming a 3G acceleration, starting with 0km/h and ending with 0km/h - we don't
want to crash into the moon. That means we accelerate half the distance and then
need to decelerate.

So we check how long it takes us to travel half the distance with 3G acceleration.
Then we double that time.

$$
\begin{align}
                   d &= v \cdot t + 0.5 \cdot a \cdot t^2\\
\Rightarrow 180 \cdot 10^6 \text{m} &= 0.5 \cdot 29.4 \frac{m}{s^2} \cdot t^2\\
\Leftrightarrow t &= \sqrt{12.2 \cdot 10^6} s\\
\Leftrightarrow t &\approx 3499s
\end{align}
$$

Doubling that time, it would still take about 7000s, which is almost **117 minutes**.
That is the absolute fastest time possible.
If you're having less luck with the distance and go at "only" 1G (0 to 100km/h in 2.8 seconds)
it would take about 3.4 hours.

Apollo 11 needed 76 hours ([source](https://de.wikipedia.org/wiki/Apollo_11)).

## Energy: A hard minimum

For an object of mass $m$ the energy required to escape Earth's gravitational field is $GMm / r$:


* r is radius of the Earth, nominally 6,371 kilometres (3,959 mi),
* G is the gravitational constant,
* M is the mass of the Earth, $M = 5.9736 \cdot 10^{24}$ kg

That means every kg (kilogram) needs over $62 \cdot 10^6$ Joule. Or 17.35 kWh.

Astonishingly little, but it adds up as you need to get a lot of weight up.

The [Space Shuttle Columbia](https://en.wikipedia.org/wiki/Space_Shuttle_Columbia) weighs
about 80,000 kg ([source](https://en.wikipedia.org/wiki/Space_Shuttle_Columbia)).
That means one needs about 1,390 MWh to lift it. At least 42 tons of
liquid hydrogen. Or as much as 700 German households need in energy per year.

Just to leave Earth. You need also quite a bit to land on the moon.


## Energy: Real numbers

> SpaceX fuels their crafts not with liquid hydrogen, but with kerosene, which
> has a lot more energy per gallon. Thanks to this and other advances, Falcon
> 9’s first stage uses 39,000 gallons of liquid oxygen and almost 25,000 gallons
> of kerosene, while the second stage uses 7,300 gallons of liquid oxygen and
> 4,600 gallons of kerosene. Combined, it makes lean mean 75,900 gallons of
> fuel.

([source](https://www.huffpost.com/entry/how-much-fuel-does-it-take-to-get-to-the-moon_b_598a35b5e4b030f0e267c83d))

* First stage, 39,000 gallons of liquid oxygen = 147,631 L. With 1.141 kg/L that makes 168 metric tons.
* First stage, 25,000 gallons of kerosene = 94,635 L. With 0.8 kg/L that makes about 76 metric tons.
* Second stage, 7,300 gallons of liquid oxygen = 27,633 L. With 1.141 kg/L that makes about 32 metric tons.
* Second stage, 4,600 gallons of kerosene = 17,412 L. With 0.8 kg/L that makes about 14 metric tons.

So in total about 290 tons of fuel.
