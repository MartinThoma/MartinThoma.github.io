---
layout: post
lang: de
title: Zeitdilatation
slug: zeitdilatation
author: Martin Thoma
date: 2024-12-22 20:00
category: My bits and bytes
tags: mathematics, space
featured_image: logos/space.png
---
Der Weltraum ist wahnsinnig groß. Wir benötigen schon sehr lange um innerhalb
unseres Sonnensystems zu reisen. Die New Horizons Raumsonde hat 9.5 Jahre
gebraucht, um den Pluto zu erreichen. Und das, obwohl der Pluto nur etwa 4
Lichtstunden von der Erde entfernt ist. Ganz naiv gesagt hat die Sonde in etwa
eine Durchschnittsgeschwindigkeit von 0.42 Lichtstunden pro Jahr gehabt.
Das sind 0.005% der Lichtgeschwindigkeit.

Das nächste Sternensystem, Alpha Centauri, ist etwa 4.37 Lichtjahre entfernt.
Wenn wir das innerhalb von 30 Jahren erreichen wollten müssten wir sehr viel
schneller sein. Naiv gerechnet bräuchten wir eine Durchschnittsgeschwindigkeit
von 14.6% der Lichtgeschwindigkeit.


## Relativistische Effekte
Bei Geschwindigkeiten über 0.1% der Lichtgeschwindigkeit werden relativistische
Effekte relevant.

Die **Zeitdilatation** ist ein solcher Effekt. Sie besagt, dass die Zeit für einen
Beobachter, der sich relativ zu einem anderen Beobachter bewegt, langsamer
vergeht. Die Zeitdilatation ist ein Effekt der speziellen Relativitätstheorie.
Sie beträgt:

$$ t' = \frac{t}{\sqrt{1 - \frac{v^2}{c^2}}} $$


## Benötigte Beschleunigung
Nun wollen wir, dass für die Besatzung des Raumschiffs die erlebte Zeit
30 Jahre beträgt.

* Entfernung: 4.37 Lichtjahre
* Erlebte Zeit: 30 Jahre
* Gesucht: Geschwindigkeit

$$
\begin{align}
v &= \frac{s}{t} \\
  &= \frac{s}{\frac{t}{\sqrt{1 - \frac{v^2}{c^2}}}}\\
  &= \frac{s \sqrt{1 - \frac{v^2}{c^2}}}{t}\\
\Leftrightarrow v \cdot t &= s \sqrt{1 - \frac{v^2}{c^2}}\\
\Leftrightarrow v^2 \cdot t^2 &= s^2 \left(1 - \frac{v^2}{c^2}\right)\\
\Leftrightarrow v^2 \cdot t^2 \cdot c^2 &= s^2 \cdot c^2 - s^2 \cdot v^2\\
\Leftrightarrow v^2 (t^2 \cdot c^2 + s^2) &= s^2 \cdot c^2\\
\Leftrightarrow v^2 &= \frac{s^2 \cdot c^2}{t^2 \cdot c^2 + s^2}\\
\Leftrightarrow v &= \sqrt{\frac{s^2 \cdot c^2}{t^2 \cdot c^2 + s^2}}\\
&= \sqrt{\frac{s^2}{t^2 + \left ( \frac{s}{c} \right)^2}}\\
&= \frac{s}{\sqrt{t^2 + \left ( \frac{s}{c} \right)^2}}\\
&= \frac{4.37 \text{ Lichtjahre}}{\sqrt{(30\text{Jahre})^2 + \left (4.37\text{Jahre} \right)^2}}\\
&= 0.144c
\end{align}
$$

Man müsste also "nur" 14.4% der Lichtgeschwindigkeit als
Durchschnittsgeschwindigkeit haben um in 30 Jahren Alpha Centauri zu erreichen.

Nun muss man jedoch beschleunigen und abbremsen. Nehmen wir an, dass wir mit
konstanter Beschleunigung $a$ beschleunigen und abbremsen. Dann müssen wir nach
2.185 Lichtjahren abbremsen. Wir müssen also 2.185 Lichtjahre nach 15 Jahren
zurückgelegt haben.

Weil wir gleichmäßig beschleunigen und bei Stillstand beginnen, ist die Durchschnittsgeschwindigkeit die hälte der Maximalgeschwindigkeit. Ohne
Zeitdieletation müssen wir also bis auf etwa 30% der Lichtgeschwindigkeit
Beschleunigen.

$$
\begin{align}
a &= \frac{\Delta v}{\Delta t}\\
  &= \frac{0.3c}{15\text{15 Jahre}}\\
  &= \frac{0.3 \cdot 300 000 000 m/s}{15 \cdot 365.25 \cdot 24 \cdot 3600 s}\\
  &= 0.19 \frac{m}{s^2}
\end{align}
$$

Das ist ziemlich wenig:

* Ein Auto beschleunigt in etwa 3 Sekunden von 0 auf 100 km/h. Das sind etwa
  9.3 m/s².
* Beim freien Fall beschleunigt man mit etwa 9.81 m/s².

## Benötigte Energie

Nehmen wir mal an, dass ein Raumschiff für eine Reise von 30 Jahren das Ziel hat
eine permanente Besiedlung von Alpha Centauri zu ermöglichen. Gehen wir weiter
davon aus, das mindestens 500 Personen nötig sind um genug genetische Vielfalt
zu haben. Im Durschnitt wiegen sie 75kg. Jeder bekommt 25kg an persönlichen
Gegenständen. Für jeden werden 100L Wasser und 10kg Nahrungsmittel an Bord
gebraucht. Jede der 500 Personen bekommt einen Standardcontainers an Platz -
und das Leergewicht eines ISO-Container liegt bei 2300kg. Das wären jetzt schon

$$
\begin{align}
m &=500 \cdot (75\text{kg} + 25\text{kg} + 100\text{kg} + 10\text{kg} + 2300\text{kg})\\
&= 1255000\text{kg}
\end{align}
$$

Rechnen wir mal mit 1500 Tonnen. Die ISS wiegt etwa 430 Tonnen, hat aber
maximal 11 Personen an Bord.

Um eine Masse von 1.500.000kg auf 0.3c zu beschleunigen benötigt man:

$$
\begin{align}
E_k &= \left (\frac{1}{\sqrt{1- \frac{v^2}{c^2}}} - 1 \right ) \cdot m \cdot c^2
&= 0.048 \cdot 1500000 \text{kg} \cdot (300000000 \text{m/s})^2\\
&= 6.5 \cdot 10^{21} \text{J}
\end{align}
$$

Eine Wattstunde (1 Wh) sind $3600$ Joule. Wir renden also von $1.8 \cdot
10^{12}$ MWh. Das sind $1.8 \cdot 10^{9}$ TWh. Die Weltenergieverbrauch lag 2019
bei etwa 170.000 TWh. Also würde so ein Raumschiff etwa 10.000 Jahre den
Weltenergieverbrauch benötigen.

Mit Solarzellen werden wir also nicht weit kommen.
Wenn wir Interstellar reisen wollen, müssen wir uns also etwas anderes einfallen
lassen.

## Deuterium-Fusion

Aus einem Kilogram Deuterium ($^2H$) würde sich etwa $8.5 \cdot 10^{14}$ Joule,
also ca. 230 TWh, erzeugen. Man bräuchte also 740kg Deuterium und müsste
sämmtliche Energie nutzbar einsetzen können.

## Siehe auch

* Arthur Ruh: [Interstellare Reisen](https://www.twintech.ch/aruh/papers6/Sternreisen.pdf), 2021.
