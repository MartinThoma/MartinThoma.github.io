---
layout: post
title: Dämmstoffe
slug: daemstoffe
author: Martin Thoma
date: 2023-12-23 23:00
category: German posts
tags: House
featured_image: logos/star.png
---
Dämmstoffe haben neben ihrer Dämmwirkung noch ein paar relevenate Eigenschaften:

* Preis
* Schimmelanfälligkeit
* Wasserdurchlässigkeit
* Wasseraufnahme
* Brandklasse

## Wärmeleitfähigkeit

* λ-Wert = W/(m K): Je kleiner der Lambda-Wert, umso weniger Wärme lässt das Material bei
  gleicher Dicke passieren.
* R-Wert = d / λ = (m² K) / W: Je höher der Wärmedurchlasswiderstand eines Bauteils, umso
  weniger lässt es Wärme entweichen.
* U-Wert = 1 / R = W/(m² K),: Je kleiner der U-Wert, umso besser ist der Wärmeschutz.

Den Lambda-Wert gibt man für Baustoffe an. Den U-Wert für Bauteile.

Die Verlustleistung $Q$ (in Watt) berechnet sich aus:

* $U$: Dem U-Wert in W/(m² K)
* $A$: Der Fläche des Bauteils in m²
* $\Delta T$: Der Temperaturdifferenz innen und Außen in Kelvin.

Die Normaußentemperatur beträgt in vielen Gegenden -13°C (oder wärmer). Wir wollen
+23°C erreichen, haben also $\Delta T = 36$.


## Beispiele

<table>
    <tr>
        <th>Baustoff</th>
        <th>Brandschutzklasse</th>
        <th>Lambda</th>
        <th>U-Wert (1cm)</th>
        <th>U-Wert (10cm)</th>
        <th>Energieverlust pro m&sup2; bei 10cm</th>
    </tr>
    <tr>
        <td>Polyurethan Hartschaum (PUR)</td>
        <td>B2</td>
        <td>0.020 - 0.040&nbsp;W/mK</td>
        <td>2 - 4</td>
        <td>0.2 - 0.4</td>
        <td>10.8 W / m&sup2;</td>
    </tr>
    <tr>
        <td>Expandiertes Polystyrol (EPS), Extrudiertes Polystyrol (XPS), Polystyrol ("Styropor")</td>
        <td>B1 - B2</td>
        <td>0,032 - 0,040 W/mK</td>
        <td>3.2 - 4</td>
        <td>0.32 - 0.4</td>
        <td>13.0 W/m&sup2;</td>
    </tr>
    <tr>
        <td>Mineral&shy;faserplatten</td>
        <td>A1</td>
        <td>0.039&nbsp;W/mK</td>
        <td>3.9</td>
        <td>0.39</td>
        <td>14 W/m&sup2;</td>
    </tr>
    <tr>
        <td>Mineral&shy;fasermatten</td>
        <td>A1</td>
        <td>0.042&nbsp;W/mK</td>
        <td>4.2</td>
        <td>0.42</td>
        <td>15.1 W/m&sup2;</td>
    </tr>
    <tr>
        <td>Mineral&shy;wolle / Glaswolle</td>
        <td>A1</td>
        <td>0.035 - 0.050&nbsp;W/mK</td>
        <td>3.5 - 5</td>
        <td>0.35 - 0.5</td>
        <td>15.3 W/m&sup2;</td>
    </tr>
    <tr>
        <td>Beton</td>
        <td>A1</td>
        <td>1.4&nbsp;W/mK</td>
        <td>140</td>
        <td>14</td>
        <td>504 W/m&sup2;</td>
    </tr>
</table>

Wenn man jetzt ein 11m x 11m Haus hat, sich überlegt ein Geschoss (2.5m) mit ca
20% Fenstern zu dämmen und man aktuell ca. einen U-Wert von 1.7 W/(m²K) hat,
dann wäre der Verlust aktuell bei

$$(11m + 11m) \cdot 2.5m \cdot 0.8 \cdot 1.7 W/(m² K) \cdot 36 K = 2.7 kW$$

Das könnte mit einer 10cm XPS-Platte auf die Mauer aufbringt, beträgt der neue
U-Wert über die R-Werte berechnet werden:

$$U_{neu} =\frac{1}{R_1 + R_2} = \frac{1}{\frac{1}{U_1} + \frac{1}{U_2}}$$

also:

$$\frac{1}{\frac{1}{1.7} + \frac{1}{0.35}} = 0.3$$

Würde man 20cm Aufbringen:

$$\frac{1}{\frac{1}{1.7} + \frac{1}{0.175}} = 0.16$$

Bei den 44m² Fläche und 36K Temperaturdifferenz ist die Wärmeverlustleistung:

* U-Wert 1.7: 2.7 kW
* U-Wert 0.3: 0.5 kW
* U-Wert 0.16: 0.3 kW

Bei angenommenen 10 Tagen mit dieser Kälte und weitern 20 um für die vielen
weniger kalten Tage welche dennoch Wärmeverlust haben zu rechnen, also 720h:

* U-Wert 1.7: $2.7 kW \cdot 720h = 1944 kWh$
* U-Wert 0.3: $0.5 kW \cdot 720h =  342 kWh$
* U-Wert 0.16: $0.3 kW \cdot 720h = 183 kWh$

Heizöl kostet aktuell ca. 1.13€/L und bringt 9.8 kWh/L, d.h. 0.12€/kWh:

* U-Wert 1.7: $2.7 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh}= 233 kWh$
* U-Wert 0.3: $0.5 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh} =  41 kWh$
* U-Wert 0.16: $0.3 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh}=  22 kWh$
