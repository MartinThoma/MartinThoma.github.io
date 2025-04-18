---
layout: post
title: Betriebskosten: Wärmepumpe vs Ölheizung
slug: betriebskosten-waermepumpe-vs-oelheizung
author: Martin Thoma
date: 2023-08-13 20:00
category: German posts
tags: money, house
featured_image: logos/house.png
---
Wir müssen weg von Fossilen Energieträgern, wenn wir unsere Klimaziele einhalten
wollen. Es ist auch interessant um uns unabhängiger von einzelnen Ländern zu
machen. Aber wie sieht es wirtschaftlich aus?

Strom kostet aktuell mindestens 0,34 €/kWh und Öl / Gas / Holz ist nicht gerade
günstiger.


## Heizbedarf

Angenommen wir haben Haus der Energieeffizienzklasse C mit
$90\frac{\text{kWh}}{m^2 \cdot a}$ und $150\text{m}^2$ Wohnfläche. Dann benötigt
es also im Jahr 13.500kWh an Energie.

## Warmwasser

Angenommen jede Person duscht ca. 15 Minuten pro Tag. Mein Duschkopf lässt ca.
4L/min durch. Das ist sehr wenig. Anscheinend ist unter 8L/min schon wenig; ab
12L/min ist es viel.

Damit sind wir pro person bei 60L/Tag und Person. Bei zwei Personen wären wir
bei 120L/Tag fürs Duschen.

Nehmen wir nun an, dass das kalte Wasser bei 15°C liegt und wir bei 40°C duschen.
Also haben wir eine Temperaturdifferenz von 25°C. Wasser hat eine [spezifische
Wärmekapazität](https://de.wikipedia.org/wiki/Spezifische_W%C3%A4rmekapazit%C3%A4t)
von 4.18 kJ/kg K. Das bedeutet:

120L/Tag * 1 kg/L * 25 K * 4.18 kJ/kg K / Tag =12.540 kJ/Tag = 3.48 kWh/Tag

Das sind dann 1270.2 kWh/Jahr. Bei Heizöl sind das 130L/Jahr.


## Betriebskosten Ölheizung

Heizöl liefert ca. 9.8 kWh/L. Nehmen wir mal eine optimale [Öl-Brennwertheizung](https://de.wikipedia.org/wiki/Brennwertkessel)
mit 100% Effizienz an ([ein paar Zahlen](https://www.energie-fachberater.de/expertenrat/expertenrat-wirkungsgrad-oelheizung-1414418105.php)).

Preis pro kWh Wärme = Preis Heizöl / 9.8

Wir lassen hier komplett außen vor, dass die Ölheizung auch Strom benötigt. Die
Zahlen sind also sehr zugunsten der Ölheizung.


## Betriebskosten Wärmepumpe

Nehmen wir auch an, dass wir eine Wärmepumpe mit einen <abbr title="Seasonal
Coefficient of Performance">SCOP</abbr> von 4 haben. Das bedeutet, für jede kWh
an Strom die wir in die Heizung stecken, können wir im Jahresschnitt 4&nbsp;kWh
an Energie aus der Umgebung ziehen. Lambda-Wärmepumpen haben einen SCOP von 5.7 ([Quelle](https://lambda-wp.at/luft/)).

Das bedeutet, die Betriebskosten sind:

Preis pro kWh Wärme = Strompreis pro kWh / 4

## Vergleich

Der Break-Even ist erreicht, wenn

Preis Heizöl / 9.8 = Preis Strom / 4

oder

Preis Heizöl = $2.45 \cdot $ Preis Strom

Aktuell:

* Heizöl: 1.12 €/L ([Quelle](https://www.heizoel24.de/))
* Strom: 0.2423 €/kWh

Heizen mit Heizöl ist aktuell also ca. 89% teuerer als mit einer typischen
Wärmepumpe. Hat man eine effiziente Wärmepumpe wie die oben genannte ist es noch
extremer.

Bei einem halbwegs modernen Haus mit dem obigem Heizbedarf würde man mit Öl
ca. 1378 L pro Jahr benötigen und mit der Wärmepumpe ca. 3375 kWh an Strom.
Für das Öl würde man 1543€ bezahlen und für den Strom ca. 818€.


## Fazit

Wärmepumpen lohnen sich bei den Betriebskosten so richtig. Insbesondere wenn durch
eine eigene Photovoltaik-Anlage der Strom noch günstiger ist.

Mit den Anschaffungskosten ist es etwas schwerer. Aber dafür gibts ja Förderungen.
