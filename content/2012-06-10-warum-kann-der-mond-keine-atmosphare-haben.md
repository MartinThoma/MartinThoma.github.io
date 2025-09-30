---
layout: post
lang: de
title: Warum kann der Mond keine Atmosph&auml;re haben?
slug: warum-kann-der-mond-keine-atmosphare-haben
author: Martin Thoma
date: 2012-06-10 15:22:02.000000000 +02:00
category: German posts
tags: Physics
featured_image: 2012/06/moon.jpg
---
Ich lese gerade das Buch 2025 von Frank Sch&auml;tzing, in dem es um den Abbau des Isotops <a href="http://de.wikipedia.org/wiki/Helium-3#Kernfusion"><sup>3</sup>He</a> geht. Es wird auch kurz erw&auml;hnt, dass es auf dem Mond keine Atmosph&auml;re geben kann. Warum ist das so?

## Die kurze Antwort
Der Mond ist leicht. Er &uuml;bt deshalb eine weitaus geringere Anziehungskraft aus, als die Erde. Deshalb ist die Geschwindigkeit, die ben&ouml;tigt wird um den Mond zu verlassen auch um einiges niedriger als die Fluchtgeschwindigkeit der Erde. Gleichzeitig ist es auf dem Mond sehr hei&szlig;, die einzelnen Gas-Teilchen bewegen sich also sehr schnell. Das bedeutet, sie k&ouml;nnen den Mond verlassen.

## Die lange Antwort

### Definitionen und Gr&ouml;&szlig;en
Die <a href="http://de.wikipedia.org/wiki/Atmosph%C3%A4re_(Astronomie)">Atmosph&auml;re</a> bezeichnet die gasf&ouml;rmige H&uuml;lle um einen Himmelsk&ouml;rper.

Die <a href="http://de.wikipedia.org/wiki/Fluchtgeschwindigkeit#Zweite_kosmische_Geschwindigkeit_oder_Fluchtgeschwindigkeit">Fluchtgeschwindigkeit</a>

Der Mond hat Temperaturen von bis zu 130 &deg;C. Das sind 403,15 Kelvin.
Die Masse des <a href="http://de.wikipedia.org/wiki/Mond">Mondes</a> betr&auml;gt $7,349 \cdot 10^{22} kg$, der Radius betr&auml;gt 1738 km.
Die Atommasse von Sauerstoff betr&auml;gt $15,999 u$.

### Mittlere Geschwindigkeit eines Gases
Die mittlere Geschwindigkeit eines Gases berechnet sich wie folgt:
$E_{Kin} = \bar E_i$
$\Leftrightarrow \frac{1}{2} \cdot m \cdot v^2 = \frac{3}{2} \cdot k \cdot T$, wobei k die <a href="http://de.wikipedia.org/wiki/Boltzmann-Konstante">Boltzmann-Konstante</a> ist und T die thermodynamische Temperatur
$\Leftrightarrow v^2 = \frac{3 \cdot k \cdot T}{m}$
Da wir die mittlere Geschwindigkeit eines Gasteilchens wollen, m&uuml;ssen wir die <a href="http://de.wikipedia.org/wiki/Maxwell-Boltzmann-Verteilung">Maxwell-Geschwindigkeitsverteilung</a> beachten:
$\Rightarrow \bar v = \sqrt{\frac{8}{2 \cdot \pi}} \sqrt{\frac{3 \cdot k \cdot T}{m}}$
$\Leftrightarrow \sqrt{\frac{12 \cdot k \cdot T}{\pi \cdot M \cdot u}}$, mit M als <a href="http://de.wikipedia.org/wiki/Atommasse">Atommasse</a> und u als <a href="http://de.wikipedia.org/wiki/Atomare_Masseneinheit">atomare Masseneinheit</a>.

### Berechnung der Fluchtgeschwindigkeit
$v_{fl} = \sqrt{\frac{2 \cdot G \cdot m}{r}}$, wobei G die <a href="http://de.wikipedia.org/wiki/Gravitationskonstante">Gravitationskonstante</a>, m die Masse des Himmelsk&ouml;rpers und r dessen Radius. Siehe auch: <a href="http://de.wikipedia.org/wiki/Kosmische_Geschwindigkeiten">1. Kosmische Geschwindigkeit</a>.

### Berechnung
Nun ben&ouml;tigen wir noch folgende Faustregel:

<blockquote>Eine Faustregel besagt, dass sich in der Atmosph&auml;re eines Planeten nur solche Gase befinden, deren mittlere Geschwindigkeit kleiner als ein Sechstel der Fluchtgeschwindigkeit f&uuml;r diesen Planeten ist.</blockquote>
Quelle:  <a href="http://www.leifiphysik.de/web_ph12/musteraufgaben/08gastheorie/atmos/atmos.htm">Leifi-Physik</a>

$v_{fl}(\text{Mond}) \approx \sqrt{\frac{2 \cdot (6,67384 \cdot 10^{-11} \cdot \frac{m^3}{kg \cdot s^2}) \cdot (7,349 \cdot 10^{22} kg)}{1738000 m}} \approx 2375,70 \frac{m}{s}$
$\Rightarrow \frac{1}{6} v_{fl}(\text{Mond}) \approx 395,95$

Die mittlere Geschwindigkeit von Sauerstoff bei 130 &deg;C ist:<br/>
$\bar v (O_2, \text{Mond}) \approx \sqrt{\frac{12 \cdot (1,3806488 \cdot 10^{-23}) \cdot (130 + 273,15)}{\pi \cdot (2 \cdot 15,999) \cdot (1,660538921 \cdot 10^{-27})}} \cdot \frac{m}{s} \approx 632,56 \frac{m}{s}$<br/>
Achtung: Ein Sauerstoffmolek&uuml;l hat 2 Atome!

$\Rightarrow \frac{1}{6} v_{fl}(\text{Mond}) < \bar v (O_2, \text{Mond}) \Rightarrow$ Langfristig kann es keine sauerstoffhaltige Atmosph&auml;re auf dem Mond geben.
