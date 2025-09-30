---
layout: post
lang: de
title: Steckersolar-Batterien 2025
slug: steckersolar-batterien-2025
author: Martin Thoma
date: 2025-05-30 20:00
category: My bits and bytes
tags: reviews, energy, photovoltaics
featured_image: logos/earth.png
---
Ich habe eine Steckersolaranlage, welche ab ca. April regelmäßig mittags mehr
Strom produziert als ich verbrauche. Daher überlege ich mir eine Batterie
anzuschaffen um den Strom flexibler nutzen zu können.

## Modelle

<style>
    .red {
        background-color: red;
    }
</style>

<table>
  <thead>
    <tr>
      <th>Modell</th>
      <th>Preis</th>
      <th>Kapazität</th>
      <th>Maximale Erweiterbarkeit</th>
      <th>Maximale Leistung (Ausgang)</th>
      <th>Technologie</th>
      <th>Outdoor</th>
      <th>Maße</th>
      <th>PV-Eingänge</th>
      <th>Weiteres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://www.ecoflow.com/us/delta-3-series-portable-power-station">EcoFlow STREAM AC Pro</a></td>
      <td><a href="https://www.elektroland24.de/neue-energien/stromspeicher/ecoflow-efdelta3-eu-delta-3-portable-powerstation-1024-wh.html">750€</a></td>
      <td>1.9 kWh</td>
      <td>11.4kWh (6 Geräte)</td>
      <td>1200 W (kombiniert 2300 W)</td>
      <td class="red">LFP (4000 Zyklen)</td>
      <td>IP65</td>
      <td>255 &times; 254 &times; 458 mm (21.5 kg)</td>
      <td class="red">1&times; 500 W max., 11 - 60 V (130 Min)</td>
      <td>Hat USB-A und USB-C Ausgänge, kann auch übers Auto geladen werden... macht eher den Eindrcuk einer Campign-Lösung</td>
    </tr>
    <tr>
      <td><a href="https://eu.marstekenergy.com/de-de/products/marstek-b2500-balkonkraftwerk-mit-speicher">Marstek Solarbank B2500-D</a></td>
      <td><a href="https://solarfantasie.com/product/speicher/marstek-solarbank-b2500-solarspeicher-2240wh-lifepo4-akku-fur-balkonkraftwerk/">380€</a></td>
      <td>2.2 kWh</td>
      <td>6.7 kWh (3&nbsp;Geräte)</td>
      <td>800W</td>
      <td>LiFePO4 (6000 Zyklen)</td>
      <td>IP65</td>
      <td>T295 &times; B175 &times; H350mm (20kg)</td>
      <td>2&times; 12V~59V, 13.5 A, 800W MAX</td>
      <td>?</td>
    </tr>
    <tr>
      <td><a href="https://de.growattpower.com/products/growatt-noah-2000">Growatt Noah 2000</a></td>
      <td>1000€ (ausverkauft)</td>
      <td>2.0 kWh</td>
      <td>? (stapelbar)</td>
      <td>800W</td>
      <td>LFP (6000 Zyklen)</td>
      <td>IP66</td>
      <td>T235 &times; B406 &times; H270mm (23kg)</td>
      <td>2&times; 16 - 60 V⎓ ,26 A, 900 W MAX</td>
      <td>?</td>
    </tr>
  </tbody>
</table>

## Rentabilität berechnen

Im Grunde ist das ganz einfach. Es muss gelten:


Gewinn in der Lebenszeit = 0.9 &middot; Zyklen in der Lebenszeit &middot; Kapazität in kWh &middot; Preis pro kWh - Anschaffungspreis


Bei dem Marstek Solarbank B2500-D

0.9 &middot; 6000 &middot; 2.2 kWh &middot; 0.25 €/kWh - 380€ = 2590 €

Umso größer das Ergebnis, desto besser.

$$
\begin{align*}
\text{Amortisationszeit in Jahren} & = \frac{\text{Anschaffungspreis}}{\text{Ersparnis pro Jahr}} \\
& = \frac{\text{Anschaffungspreis}}{\text{Jährlicher Überschuss in kWh} \cdot \text{Preis pro kWh}}
\end{align*}
$$

In meinem Fall habe ich eine Ersparnis von 208kWh/Jahr &middot; 0.25€/kWh = 52€/Jahr.
Der Akku sollte also definitiv nicht mehr als 624€ kosten, damit er sich innerhalb
von 12 Jahren amortisieren kann.


Oder auch:

$$
\begin{align*}
\text{Lebenszeit in Jahren} & = \frac{\text{Zyklen} \cdot \text{Kapazität [kWh]}}{\text{Überschuss [kWh/Jahr]}} \\
& = \frac{6000 \cdot 2.2 \text{ kWh}}{208 \text{ kWh/Jahr}} \\
& = 63 \text{ Jahre}
\end{align*}
$$
