---
layout: post
title: Getting a Feeling for Energy
author: Martin Thoma
date: 2015-05-19 19:17
categories:
- Cyberculture
tags:
- Energy
- Politics
- Poverty
featured_image: logos/energy.png
---
Have you heard of [GravityLight](https://www.indiegogo.com/projects/gravitylight-made-in-africa/x/7191655#/story)?

It is a gravity-powered lamp designed as an alternative for off-grid families
who would otherwise use kersene lamps. It is basically only a 12kg weight,
lifted and put on the gravity light. When the weight goes down again it pulls a
cord. This cord makes an electric motor which generates electricity for LEDs.

I wondered how much weight I would need to lift (assuming 100% efficiency) to
power my computer for 8 hours.

According to the power supply unit, my laptop can consume up to 65 Watt. That
is astonishingly low. I think my big one is at about 600-800 Watt.

\begin{align}
65 W \cdot 8 h &= \frac{65 kg \cdot m^2 \cdot 8h \cdot 60 \frac{min}{h} \cdot 60 \frac{s}{min}}{s^3}\\
&= 1872 \cdot 10^3 \frac{kg \cdot m^2}{s^2}
\end{align}

You might also remember from your physics courses that [potential energy](https://en.wikipedia.org/wiki/Potential_energy) is $E_{pot} = m \cdot g \cdot h$ where $m$ is the mass
(in kg), $g = 9.80 \frac{m}{s^2}$ is the gravitational acceleration and $h$ is
the height in meters.

\begin{align}
m \cdot h &= \frac{E_{pot}}{g}\\
&= \frac{1.872 \cdot 10^6 \frac{kg \cdot m^2}{s^2}}{9.80 \frac{m}{s^2}}\\
&= 191.0 \cdot 10^3 kg \cdot m
\end{align}

This means I would have to lift 191&ensp;000 packages one liter of milk to a height
of 1 meter. Every day. Just to let my small laptop run.

Or lets view it from another angle. I think lifting about 5 packages of milk
to a height of about 1.8m each hour would not be too exhausting. This would
generate about $E_{pot} = 5kg \cdot 1.80m \cdot 9.80 \frac{m}{s^2} / (1h \cdot 60 \frac{min}{h} \cdot 60 \frac{s}{min}) = 0.0245 \frac{kg \cdot m^2}{s^3} = 0.0245 W$.
Lets think what you can power with 0.0245 Watt...

It is amazing about how much energy we have today.