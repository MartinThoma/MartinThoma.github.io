---
layout: post
title: Heizungsvergleich
slug: heizungsvergleich
lang: de
author: Martin Thoma
date: 2024-01-07 20:00
category: German posts
tags: house
featured_image: logos/house.png
---
Ich überlege mir gerade welches Heizsystem ich nutzen will und wie ich den
Übergang mache.

<style>
.good {
    background-color: green;
}

.bad {
    background-color: red;
}
</style>

## Brennstoffe

<table>
    <thead>
    <tr>
        <th>Brennstoff</th>
        <th>Einkaufspreis</th>
        <th>Brennwert</th>
        <th>Heizkosten</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Strom-Direkt</td>
        <td>0.30 €/kWh</td>
        <td>-</td>
        <td class="bad">0.30 €/kWh</td>
    </tr>
    <tr>
        <td>Wärmepumpe (SCOP=3)</td>
        <td>0.30 €/kWh</td>
        <td>-</td>
        <td>0.10 €/kWh</td>
    </tr>
    <tr>
        <td>Wärmepumpe (SCOP=5)</td>
        <td>0.30 €/kWh</td>
        <td>-</td>
        <td class="good">0.06 €/kWh</td>
    </tr>
    <tr>
        <td>Kaminholz (Fichte, 25cm)</td>
        <td>69 €/Schüttraummeter und </td>
        <td>1500 kWh/Schüttraummeter</td>
        <td class="good">0.05 €/kWh</td>
    </tr>
    <tr>
        <td><a href="https://www.heizpellets24.de/">Pallets</a></td>
        <td>0.293 €/kg</td>
        <td>4.9 kWh/kg</td>
        <td class="good">0.06 €/kWh</td>
    </tr>
    <tr>
        <td><a href="https://holzhof24.de/hackschnitzel/">Hackschnitzel</a> (20% Restfeuchte)</td>
        <td>0.68 €/kg</td>
        <td>3.4 kWh/kg</td>
        <td>0.20 €/kWh</td>
    </tr>
    <tr>
        <td>Gas</td>
        <td>0.10 €/kWh</td>
        <td>-</td>
        <td>0.10 €/kWh</td>
    </tr>
    <tr>
        <td>Braunkohlebriketts</td>
        <td>0.55€/kg</td>
        <td>5.6 kWh/kg</td>
        <td>0.10 €/kWh</td>
    </tr>
    <tr>
        <td><a href="https://www.heizoel24.de/heizoelpreise">Heizöl</a></td>
        <td>1.05 €/L</td>
        <td>9.8 kWh/L</td>
        <td>0.11 €/kWh</td>
    </tr>
    <tr>
        <td>Steinkohle</td>
        <td>1.34€/kg</td>
        <td>8.0 kWh/kg</td>
        <td class="bad">0.17 €/kWh</td>
    </tr>
    <tr>
        <td>Ethanol</td>
        <td>5.43€/kg / 4.59€/L</td>
        <td>7.9 kWh/kg / 5.9 kWh/L</td>
        <td class="bad">0.69 €/kWh</td>
    </tr>
    </tbody>
</table>

## Grundannahmen

* Strom: 0.32 €/kWh
* Heizöl:
    * 1.20 €/L mit 9.8 kWh/L Brennwert
    * 180 kWh/a für den Brenner
* 150 kWh/a für die Zirkulationspumpe bei einer Zentralheizung
* 20 Jahre Betrieb bei allen Systemen
* Heizbedarf von 10.000 kWh/a
* 1600 kWh/a: 800 kWh Wärme für Warmwasser pro Person pro Jahr

## Ölheizung

Hier rechne ich mal mit dem Einbau einer neuen Ölheizung.

Die Heizung kostet 20.000€ und die Tanks 10.000 €, also 30.000€ für die
**Installation**.

Sagen wir 200€/Jahr für die **Wartung**.

Der **Betrieb** ist bei $11.600\frac{\text{kWh}}{\text{a}} / 9.8\frac{\text{kWh}}{\text{L}} = 1183\frac{L}{\text{a}}$ Heizöl + $330\frac{\text{kWh}}{\text{a}}$ Strom,
also

$$1.20\frac{€}{L} \cdot 1183\frac{L}{a} \cdot 20a + 0.32\frac{€}{\text{kWh}} \cdot 330 \frac{\text{kWh}}{a} \cdot 20a = 30504€$$

In Summe: $$30000€ + 200 €/a \cdot 20 a + 30504 € = 64504 €$$

## Klimaanlagen + BWWP

Die **Installation** (Gerät + Montage) kostet ca. 3200€ pro 3.5 kW Heizleistung.
Sagen wir mal 12.000€ insgesamt. Für die Brauchwasser-Wärmepumpe (BWWP) rechne
ich nochmals mit 5.000€, also 17.000€ für das Gesamtsystem

Ich gehe davon aus, dass die **Wartung** im Schnitt 100€ pro Jahr kosten wird.
Das halbjährliche Reinigen der Innengeräte kann man selbst machen:

<iframe width="560" height="315" src="https://www.youtube.com/embed/XoAPgEnjUJg?si=ofDOuEYGoMmKVaKc&amp;start=1464" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Nur das Kältemittel müsste von einem Fachmann nachgefüllt werden ... falls das
denn jemals nötig wird.

Für den **Betrieb** nehme ich einen SCOP von 5 an. Ich habe Werte von 5.2 - 6.4
gesehen.

In Summe:

$$17000€ + 100 €/a \cdot 20a + 0.32\frac{\text{€}}{\text{kWh}} \cdot 10000\frac{\text{kWh}}{\text{a}} \cdot 20\text{a} / 5 + 0.32\frac{\text{€}}{\text{kWh}} \cdot 1600\frac{\text{kWh}}{\text{a}} \cdot 20a / 3= 35213.33€$$
