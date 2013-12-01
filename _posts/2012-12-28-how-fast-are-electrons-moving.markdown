---
layout: post
status: publish
published: true
title: How fast are electrons moving?
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 51981
wordpress_url: http://martin-thoma.com/?p=51981
date: 2012-12-28 07:04:47.000000000 +01:00
categories:
- Cyberculture
tags: []
comments:
- id: 754021
  author: Keba
  author_email: mariofuest@aol.com
  author_url: ''
  date: !binary |-
    MjAxMi0xMi0yOCAyMjo1Mzo0NSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0xMi0yOCAyMTo1Mzo0NSArMDEwMA==
  content: ! "> Hmm &hellip; seems to be very slow. Is my calculation correct?\r\n\r\nI
    don&lsquo;t know the \"v = &hellip;\" formula (but it makes sense, if my \"classical
    Physic approach below is usable here), but the calculation seems correct to me.
    You realise that less free electrons *increase* the speed of the electrons (if
    we keep I the same, i. e. \"put some more Volt in\")? So in copper each electron
    moves (accordiung to you) very slow, but as there are so many electrons the effects
    (-> move next electron) are faster.\r\n\r\nThat&lsquo;s not how you do Physics,
    but assume a pile with lots of balls. You put some energy to the first ball and
    \"instantly\" the last ball pops out of the pile. The speed of each ball is rather
    slow.\r\n\r\nNow put only 10% of the balls in another, similar pile. To keep the
    \"output rate of balls per time, ie. I) intact, use more power to push the first
    ball. It hits the second ball, which hits the third&hellip; As the angular momentum
    keeps the same all the time (no friction&hellip;), all balls have the same &ndash;
    higher &ndash; speed.\r\n\r\nSo do the same calculation with air &ndash; and you
    get greater speeds. ;)\r\n\r\nIf we keep A the same all the time, maybe the speed
    is always the same then? Ie. are I and Q proportional?\r\n\r\nRegards, *not* a
    Physic student, Keba."
featured_image: 2012/12/atom-electron-bohr1.png
---
I've recently learned something about electric circuits. The ideal model of circuits does ignore that electrons actually need time to pass the components of the circuit. So we introduced the "dead time model". So we added a model component for each real component that does only delay the incoming signal. But I've wondered if dead time of a cable wasn't important, too. So I thought the question would be <em>How fast are electrons moving in a cable?</em>, but I just realized that the question is <em>How fast does a signal move in a wire?</em>.

<h2>How fast are electrons moving through a wire?</h2>
If you have electric current $I$ (measured in Ampere), the wire is a cylindric conductore with a cross-sectional area of $A$, $e = -1.6021766 \cdot 10^{-19} C$  (coulombs) is the charge of an electron an $Q$ is $\frac{\text{mobile electrons}}{\text{volume}}$.
$v = \frac {I}{QeA}$

According to this source, $Q = 8.5 \cdot 10^{22} \frac{1}{cm^3}$ for copper. If $I=1 A$ and if your wire has a radius of 0.5mm, you get:
$v= \frac{1 A}{ 8.5 \cdot 10^{22} \frac{1}{cm^3} \cdot e \cdot ((0.5mm)^2 \cdot pi)} = 9.349 \cdot 10^{-5} \frac{m}{s} = $ (see <a href="http://www.wolframalpha.com/input/?i=%281+A%29%2F%288.5+*+10%5E%2822%29%2F%28cm%5E3%29+*+%28charge+of+an+electron%29+*+%28%280.5mm%29%5E2+*+pi%29%29">Wolfram|Alpha</a>).

Hmm ... seems to be very slow. Is my calculation correct?

<h2>How fast are electrical signals moving through a wire?</h2>
See <a href="http://physics.stackexchange.com/a/47635/7197">physics.stackexchange.com</a>


$v = \frac{c}{\sqrt{\mu_r \varepsilon_r}}$

where $\varepsilon_r$ is <a href="http://en.wikipedia.org/wiki/Relative_permittivity">relative permittivity</a> and $\mu_r$ is <a href="http://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Relative_permeability">relative magnetic susceptibility</a>.

For copper:
$\mu_r = 0.999994$
$\varepsilon_r = 3$, as you can't measure permeability of metallic conductors (see "Elektromagnetische Felder und Wellen". Paul Lorrain, Dale R. Corson, Fran&ccedil;ois Lorrain, page 75)
$v = \frac{c}{\sqrt{0.999994 \cdot 3}} = 0.577352 \cdot c$

<h2>How fast are electrons moving around an atom?</h2>
Well, first of all I have to mention, that electrons seem not to move around a nucleus as this image suggests:

[caption id="attachment_52041" align="aligncenter" width="300"]<a href="http://martin-thoma.com/how-fast-are-electrons-moving/atom-electron-bohr/" rel="attachment wp-att-52041"><img src="http://martin-thoma.com/wp-content/uploads/2012/12/atom-electron-bohr-300x300.png" alt="Atom according to Bohrs model" width="300" height="300" class="size-medium wp-image-52041" /></a> Atom according to Bohrs model[/caption]

A model with <a href="http://en.wikipedia.org/wiki/Atomic_orbital">atomic orbitals</a> seems to be more accurate. However, you can calulate the speed $v$ an electron would have in Bohrs model.

The centripedal force is
$F_Z = \frac{m \cdot v^2}{r}$
This force pushes the electron away from the nucleus.

The coulomb-force is
$F_C = \frac{e^2}{4 \pi \varepsilon_0 r^2}$
where $\varepsilon_0 \approx 8.8541 \cdot 10^{-12} \frac{F}{m}$ is <a href="http://en.wikipedia.org/wiki/Permittivity">permittivity</a>.

Now you calculate:
$\begin{align}F_\mathrm{C} = F_\mathrm{Z} \quad 
  &\Leftrightarrow \quad \frac{e^2}{4 \pi \varepsilon_0 r^2} = \frac{m_{e}v^2}{r}\\
  &\Leftrightarrow \quad v^2 = \frac{e^2}{4 \pi \varepsilon_0 r m_e} = \frac{e^2}{4 \pi \varepsilon_0 m_e} \cdot \frac{1}{r}
\end{align}$

Ok, we're almost there. But how do we get $r$? Well, you have to know this equation:
$ m_{e} v r = n \hbar$
where $n$ is the <a href="http://en.wikipedia.org/wiki/Principal_quantum_number">principal quantum number</a> and $\hbar$ is the <a href="http://en.wikipedia.org/wiki/Planck_constant">reduced Planck constant</a>.
So you get:
$\Leftrightarrow r = \frac{n \hbar}{v m_e}$

Now insert this in the equation above:
$\begin{align}
v^2 &=  \frac{e^2}{4 \pi \varepsilon_0 m_e} \cdot \frac{1}{\frac{n \hbar}{v m_e}}\\
\Rightarrow v &= \frac{e^2}{4 \pi \varepsilon_0 n \hbar}
\end{align}$

Lets take a hydrogen nucleus ($n=1$): 
We get $2.19 \cdot 10^6 \frac{m}{s} \approx 7.88 \cdot 10^6 \frac{km}{h}$ (see <a href="http://www.wolframalpha.com/input/?i=%28charge+of+electron%29%5E2%2F%284+pi+epsilon_0+h+bar%29">Wolfram|Alpha</a>).
This is much less than 1% of the speed of light (which is $1.079 \cdot 10^9 \frac{km}{h}$)

<h2>Sources</h2>
Very good:
<ul>
  <li><a href="http://physics.stackexchange.com/q/20187/7197">How fast do electrons travel in an atomic orbital?</a></li>
  <li><a href="http://physics.stackexchange.com/q/6177/7197">How fast do electrons move through a conductor?</a> &rarr; <a href="http://amasci.com/miscon/speed.html">SPEED OF "ELECTRICITY"</a></li>
  <li><a href="http://physics.stackexchange.com/q/15704/7197">Explanation for speed of an electrical impulse</a></li>
</ul>

Not so good:
<ul>
  <li><a href="http://en.wikipedia.org/wiki/Drift_velocity">Drift velocity</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Speed_of_electricity">Speed of electricity</a></li>
  <li><a href="http://en.wikipedia.org/wiki/Wave_propagation_speed">Wave propagation speed</a></li>
</ul>
