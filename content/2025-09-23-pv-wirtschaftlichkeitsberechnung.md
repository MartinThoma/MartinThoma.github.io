---
layout: post
title: Wirtschaftlichkeitsberechnung einer Photovoltaikanlage
slug: wirtschaftlichkeitsberechnung-pv-anlage
lang: de
author: Martin Thoma
date: 2025-09-23 20:00
category: My bits and bytes
tags: house,photovoltaics
featured_image: logos/house.png
---
Ich besitze seit rund zwei Jahren ein eigenes Haus und habe im Mai 2025 eine
Wärmepumpe installieren lassen. Besonders spannend wird diese in Kombination mit
einer Photovoltaikanlage (PV-Anlage): Sie reduziert die Abhängigkeit von
steigenden Strompreisen, schont die Umwelt und kann im Idealfall sogar eine
gewisse Absicherung gegen kurzfristige Stromausfälle bieten.

In diesem Artikel gehe ich der Frage nach, ab welchem Preis sich eine PV-Anlage
für mich wirtschaftlich lohnt. Dabei analysiere ich meine aktuellen Stromkosten,
die verfügbare Dachfläche, den zu erwartenden Ertrag sowie verschiedene Betriebsszenarien.


## Aktuelle Strompreise und Tarife

Ich habe aktuell zwei Stromzähler und zwei Tarife:

<table>
  <thead>
    <tr>
      <th>Tarif</th>
      <th>Arbeitspreis</th>
      <th>Grundgebühr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wärmepumpen-Tarif (HT/NT)</td>
      <td style="text-align: right;">0.2050&nbsp;€/kWh</td>
      <td style="text-align: right;">93.88&nbsp;€/Jahr</td>
    </tr>
    <tr>
      <td>Hausstrom</td>
      <td style="text-align: right;">0.2505&nbsp;€/kWh</td>
      <td style="text-align: right;">126.43&nbsp;€/Jahr</td>
    </tr>
  </tbody>
</table>

Ich gehe von ca. 2% jährlichen Preissteigerungen aus.


## Verfügbare Dachfläche und Ausrichtung

Für die Dimensionierung einer PV-Anlage sind die verfügbare Dachfläche und deren Ausrichtung entscheidend.

<figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2025/09/efh-with-solar.jpg"><img src="../images/2025/09/efh-with-solar.jpg" alt="ChatGPT-Rendering eines Einfamilienhauses mit Solaranlage. Die Dachneigung könnte bei 45° sein." style="max-height: 512px"/></a>
    <figcaption class="text-center">ChatGPT-Rendering eines Einfamilienhauses mit Solaranlage. Die Dachneigung könnte bei 45° sein.</figcaption>
</figure>


Ich habe ein Satteldach mit Betondachsteinen (Braas Taunus Pfanne):

* **Dachneigung**: 30° (0° = flach, mehr als 60° ist ungewöhnlich, [Tool](https://solar.red/photovoltaik-neigungswinkel/))
* **Ausrichtung**: Süd-West (ca. 50°, also etwas westlicher als Süd, [Tool](https://www.rechnerphotovoltaik.de/rechner/dachausrichtung))
* **Dachfläche: ca. 6m x 12m** (72m² pro Seite)
    * 10m x 10m Korpus, d.h. 10m x 5m für das rechtwinklige Dreieck
    * Dachüberstand von ca. 1m
    * Hypothenuse = 6m / cos(30°) = 6.93m


## Ertragsprognose

Basierend auf den Dachparametern lässt sich der zu erwartende Stromertrag berechnen.
Mit [solarserver.de](https://www.solarserver.de/pv-anlage-online-berechnen/)
kann man berechnen, wie viel Strom eine PV-Anlage an einem bestimmten Ort,
mit einer bestimmten Ausrichtung und Neigung erzeugt. Der
[Zusammenhang zwischen Neigung, Ausrichtung und Ertrag](https://www.rechnerphotovoltaik.de/photovoltaik/voraussetzungen/dachneigung)
zeigt, dass eine Neigung von 30° gar nicht so schlecht ist.

<table>
    <thead>
        <tr>
            <th>Monat</th>
            <th>kWh/kWp</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Januar</td>
            <td style="text-align: right;">40 kWh/kWp</td>
        </tr>
        <tr>
            <td>Februar</td>
            <td style="text-align: right;">60 kWh/kWp</td>
        </tr>
        <tr>
            <td>März</td>
            <td style="text-align: right;">100 kWh/kWp</td>
        </tr>
        <tr>
            <td>April</td>
            <td style="text-align: right;">125 kWh/kWp</td>
        </tr>
        <tr>
            <td>Mai</td>
            <td style="text-align: right;">130 kWh/kWp</td>
        </tr>
        <tr>
            <td>Juni</td>
            <td style="text-align: right;">135 kWh/kWp</td>
        </tr>
        <tr>
            <td>Juli</td>
            <td style="text-align: right;">138 kWh/kWp</td>
        </tr>
        <tr>
            <td>August</td>
            <td style="text-align: right;">124 kWh/kWp</td>
        </tr>
        <tr>
            <td>September</td>
            <td style="text-align: right;">98 kWh/kWp</td>
        </tr>
        <tr>
            <td>Oktober</td>
            <td style="text-align: right;">70 kWh/kWp</td>
        </tr>
        <tr>
            <td>November</td>
            <td style="text-align: right;">45 kWh/kWp</td>
        </tr>
        <tr>
            <td>Dezember</td>
            <td style="text-align: right;">30 kWh/kWp</td>
        </tr>
        <tr>
            <td><strong>Summe</strong></td>
            <td style="text-align: right;"><strong>1.080 kWh/kWp</strong></td>
        </tr>
    </tbody>
</table>

Die Gesamtleistung pro Jahr beträgt somit **1.080 kWh/kWp**.


## Analyse des Stromverbrauchs

Für den Stromverbrauch im Haushalt spielen folgende Faktoren eine zentrale Rolle:

1. **Heizung**: Der größte Anteil am Energiebedarf entfällt auf das Heizen –
   insbesondere in älteren Gebäuden. Relevant für den Stromverbrauch ist dies
   jedoch nur bei elektrischen Heizsystemen wie Wärmepumpen, Infrarotheizungen oder Nachtspeicheröfen. Weitere typische Großverbraucher sind:
    * Herd und Backofen
    * Waschmaschine und Trockner
    * Heizlüfter
2. **Warmwasser**: Auch die Warmwasserbereitung kann einen erheblichen
   Strombedarf verursachen.
3. **Haushalt**: Wieder Wärme (Kühl- und Gefrierschrank, heißes Wasser für
   Spülmaschine und Waschmaschine, Herd und Ofen). Die Beleuchtung spielt nur
   dann eine Rolle, wenn man noch alte
   Glühbirnen/Halogenlampen/Energiesparlampen hat. Oder wenn man viele LEDs hat,
   die man lange brennen lässt. Laptops und Smartphones spielen keine Rolle.
4. **Anzahl der Personen** im Haushalt: Je mehr Personen, desto höher der Verbrauch –
   hauptsächlich aufgrund von Warmwasser und häufigerem Waschen/Spülen/Trocknen.

Es gibt Tabellen mit typischen Verbrauchswerten. Einen Teil meiner Daten habe
ich selbst gemessen, die in Klammern angegebenen Werte sind dagegen Schätzungen.
Die Angaben beziehen sich auf ein Haus mit rund 200&nbsp;m² beheizter Fläche,
2&nbsp;Personen (plus gelegentlich 2&nbsp;Gäste) sowie 2&nbsp;Katzen.

### Monatlicher Stromverbrauch im Detail


<style>
.border-right {
    border-right: 1px solid black;
}
</style>

<table>
    <thead>
        <tr>
            <th class="border-right">Monat</th>
            <th>Haushalt</th>
            <th>Warmwasser</th>
            <th class="border-right">Heizung</th>
            <th>Kosten Haushalt<br/>im Monat</th>
            <th>Kosten Warmwasser<br/>im Monat</th>
            <th class="border-right">Kosten Heizung<br/>im Monat</th>
            <th>Nächtlicher Haushalt&shy;strom&shy;verbrauch</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="border-right">Januar</td>
            <td style="text-align: right;">8.7 kWh/Tag</td>
            <td style="text-align: right;">(2.4&nbsp;kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(38 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">67.56 €</td>
            <td style="text-align: right;">15.25 €</td>
            <td style="text-align: right; background-color: #ff0000;" class="border-right">241.49 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">Februar</td>
            <td style="text-align: right;">8.5 kWh/Tag</td>
            <td style="text-align: right;">(2.0 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(30 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">59.62 €</td>
            <td style="text-align: right;">11.48 €</td>
            <td style="text-align: right; background-color: #ff0000;" class="border-right">172.20 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">März</td>
            <td style="text-align: right;">10.3&nbsp;kWh/Tag</td>
            <td style="text-align: right;">(1.8 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(11 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">79.98 €</td>
            <td style="text-align: right;">11.44 €</td>
            <td style="text-align: right; background-color: #ffdd22;" class="border-right">69.91 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">April</td>
            <td style="text-align: right;">8.5 kWh/Tag</td>
            <td style="text-align: right;">(1.5 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(4 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">63.88 €</td>
            <td style="text-align: right;">9.23 €</td>
            <td style="text-align: right;" class="border-right">24.60 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">Mai</td>
            <td style="text-align: right;">8.5 kWh/Tag</td>
            <td style="text-align: right;">1.2 kWh/Tag</td>
            <td style="text-align: right;" class="border-right">(3 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">66.00 €</td>
            <td style="text-align: right;">7.63 €</td>
            <td style="text-align: right;" class="border-right">19.07 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">Juni</td>
            <td style="text-align: right;">6.1 kWh/Tag</td>
            <td style="text-align: right;">1.2 kWh/Tag</td>
            <td style="text-align: right;" class="border-right">1.0 kWh/Tag</td>
            <td style="text-align: right;">45.84 €</td>
            <td style="text-align: right;">7.38 €</td>
            <td style="text-align: right;" class="border-right">6.15 €</td>
            <td style="text-align: right;">0.7 kWh - 1.7 kWh<br/>median=0.8 kWh</td>
        </tr>
        <tr>
            <td class="border-right">Juli</td>
            <td style="text-align: right;">5.9 kWh/Tag</td>
            <td style="text-align: right;">1.1 kWh/Tag</td>
            <td style="text-align: right;" class="border-right">0.3 kWh/Tag</td>
            <td style="text-align: right;">47.37 €</td>
            <td style="text-align: right;">6.99 €</td>
            <td style="text-align: right;" class="border-right">1.91 €</td>
            <td style="text-align: right;">0.6 kWh - 1.7 kWh<br/>median=0.8 kWh</td>
        </tr>
        <tr>
            <td class="border-right">August</td>
            <td style="text-align: right;">6.8 kWh/Tag</td>
            <td style="text-align: right;">1.2 kWh/Tag</td>
            <td style="text-align: right;" class="border-right">0.3 kWh/Tag</td>
            <td style="text-align: right; background-color: #ffdd22;">52.80 €</td>
            <td style="text-align: right;">7.63 €</td>
            <td style="text-align: right;" class="border-right">1.91 €</td>
            <td style="text-align: right;">0.8 kWh - 1.3 kWh<br/>median=1.0 kWh</td>
        </tr>
        <tr>
            <td class="border-right">September</td>
            <td style="text-align: right;">7.7 kWh/Tag</td>
            <td style="text-align: right;">(1.2 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(2.7 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">57.87 €</td>
            <td style="text-align: right;">7.38 €</td>
            <td style="text-align: right;" class="border-right">16.61 €</td>
            <td style="text-align: right;">0.7 kWh - 2.8 kWh<br/>median=1.2 kWh</td>
        </tr>
        <tr>
            <td class="border-right">Oktober</td>
            <td style="text-align: right;">7.5 kWh/Tag</td>
            <td style="text-align: right;">(1.8 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(9 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">58.24 €</td>
            <td style="text-align: right;">11.44 €</td>
            <td style="text-align: right; background-color: #ffdd22;" class="border-right">57.20 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">November</td>
            <td style="text-align: right;">10.3 kWh/Tag</td>
            <td style="text-align: right;">(2.0 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(25 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">77.40 €</td>
            <td style="text-align: right;">12.30 €</td>
            <td style="text-align: right; background-color: #ff0000;" class="border-right">153.75 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td class="border-right">Dezember</td>
            <td style="text-align: right;">10.0 kWh/Tag</td>
            <td style="text-align: right;">(2.4 kWh/Tag)</td>
            <td style="text-align: right;" class="border-right">(40 kWh/Tag)</td>
            <td style="text-align: right; background-color: #ffdd22;">77.66 €</td>
            <td style="text-align: right;">15.25 €</td>
            <td style="text-align: right; background-color: #ff0000;" class="border-right">254.20 €</td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td><strong>Summe</strong></td>
            <td style="text-align: right;"><strong>3005 kWh</strong></td>
            <td style="text-align: right;"><strong>ca. 602 kWh</strong></td>
            <td style="text-align: right;" class="border-right"><strong>ca. 4971 kWh</strong></td>
            <td style="text-align: right;"><strong>754.22 €</strong></td>
            <td style="text-align: right;"><strong>123.40 €</strong></td>
            <td style="text-align: right;" class="border-right"><strong>1019.00 €</strong></td>
            <td style="text-align: right;">TODO</td>
        </tr>
        <tr>
            <td><strong>Durchschnitt</strong></td>
            <td style="text-align: right;"><strong>8.2 kWh/Tag</strong></td>
            <td style="text-align: right;"><strong>1.6 kWh/Tag</strong></td>
            <td style="text-align: right;"><strong>13.6 kWh/Tag</strong></td>
            <td style="text-align: right;"><strong>2.06€/Tag</strong></td>
            <td style="text-align: right;"><strong>0.34€/Tag</strong></td>
            <td style="text-align: right;" class="border-right"><strong>2.79€/Tag</strong></td>
            <td style="text-align: right;">TODO</td>
        </tr>
    </tbody>
</table>

### Gesamtkosten im Überblick

Basierend auf den oben genannten Verbrauchswerten bezahle ich ohne
Photovoltaik-Anlage voraussichtlich:

<table>
    <tbody>
        <tr>
          <td>Haushaltsstrom</td>
          <td style="text-align: right;">879.18 €/Jahr</td>
        </tr>
        <tr>
          <td>Wärmepumpenstrom</td>
          <td style="text-align: right;">1236.34 €/Jahr</td>
        </tr>
        <tr>
          <td>Erster Stromzähler (Bezug/Einspeisung)</td>
          <td style="text-align: right;">30 €/Jahr</td>
        </tr>
        <tr>
          <td>Zweiter Stromzähler (HT/NT)</td>
          <td style="text-align: right;">30 €/Jahr</td>
        </tr>
        <tr>
            <th>Gesamt</th>
            <th style="text-align: right;">2175.52 €/Jahr</th>
        </tr>
    </tbody>
</table>


## Einspeisevergütung nach dem EEG

Die Höhe der Einspeisevergütung ist ein wichtiger Faktor für die Wirtschaftlichkeitsberechnung.

[Laut Bundesnetzagentur](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/EEG_Foerderung/start.html) gibt es im September 2025 für
Teileinspeisung:

<table>
    <thead>
        <tr>
            <th>Leistung</th>
            <th>Vergütung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: right;">bis 10 kWp</td>
            <td style="text-align: right;">0.078&nbsp;€/kWh</td>
        </tr>
        <tr>
            <td style="text-align: right;">10 kWp - 40 kWp</td>
            <td style="text-align: right;">0.068&nbsp;€/kWh</td>
        </tr>
        <tr>
            <td style="text-align: right;">40 kWp - 750 kWp</td>
            <td style="text-align: right;">0.0556&nbsp;€/kWh</td>
        </tr>
    </tbody>
</table>

Dabei wird eine Mischkalkulation angewendet, d.h. wenn ich eine 12 kWp Anlage
habe, erhalte ich für die ersten 10 kWp 0.078 €/kWh und für die restlichen 2 kWp
0.068 €/kWh. Pro eingespeister kWh erhalte ich somit (10 * 0.078 + 2 * 0.068) / 12 = 0.0753 €/kWh.

Der Vergütungsanspruch nach dem EEG besteht für die Dauer von 20 Jahren. Die
20-Jahre-Frist beginnt ab der Inbetriebnahme zu laufen.


## Wirtschaftlichkeits&shy;berechnung

Um die Rentabilität einer PV-Anlage zu bewerten, betrachte ich zwei Szenarien:
das ungünstigste (Volleinspeisung) und das günstigste (maximaler Eigenverbrauch).

Ich gehe pessimistisch von einer Lebensdauer der PV-Anlage von 20 Jahren aus.

### Null-Szenario: Keine PV-Anlage

* Jährliche Kosten ohne PV-Anlage: 2175.52 €
* Jährliche Kostensteigerung: 2%
* Kummulative Kosten in 20 Jahren: $\sum_{i=0}^{n=19} 2175.52 \cdot (1 + 0.02)^i = 52859$ EUR

Wenn man von 20.000 EUR Investitionskosten für die PV-Anlage ausgeht und diese
als Alternative zur PV-Anlage mit 3% Wertsteigerung anlegt und am Ende mit
26.375% versteuert, dann hat man:

$$\begin{align*}
\text{Investment} &= 20000 + 20000 \cdot (1.03^{20}-1) \cdot (1 - 0.26375)\\
&= 20000 + 20000 \cdot 0.8061 \cdot 0.73625\\
&= 20000 + 11879.5\\
&= 31879.5 \text{ EUR}
\end{align*}$$

Das heißt nach 20 Jahren bin ich **-20979.5 EUR** ärmer als heute, wenn ich
keine PV-Anlage installiere.

### Worst-Case-Szenario: Volleinspeisung

* Vergütung: 0.078 €/kWh
* Ertrag: 1.080 kWh/kWp/Jahr

⇒ 84.24 €/kWp pro Jahr an Einnahmen. Bei Zählerzusammenlegung entstehen sogar
höhere Ausgaben, da ich dann auf den bezogenen Strom den höheren Verbrauchspreis
zahlen muss.

Nach 20 Jahren habe ich also 52859 EUR an Stromkosten bezahlt und  1684.80 EUR
an Einnahmen durch die Einspeisevergütung erhalten.

Ich bin also **-51174.20 EUR** ärmer als heute, wenn ich eine PV-Anlage installiere
und den gesamten Strom einspeise, aber nur die Vergütung für Teileinspeisung
erhalte.


### Best-Case-Szenario: Maximaler Eigenverbrauch mit Einspeisevergütung

Ich gehe hier von einer Zählerzusammenlegung aus, d.h. der Strom kostet dann
0.2505 €/kWh + 126.43 €/Jahr.

Für die Berechnung nehme ich eine 10 kWp Anlage als Beispiel:

<table>
    <thead>
        <tr>
            <th class="border-right">Monat</th>
            <th>Strombedarf</th>
            <th class="border-right">PV-Ertrag</th>
            <th>Einspeisung</th>
            <th class="border-right">Netzbezug</th>
            <th>Vergütung</th>
            <th>Kosten Strom</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="border-right">Januar</td>
            <td style="text-align: right;">1522 kWh</td>
            <td style="text-align: right;" class="border-right;">400 kWh</td>
            <td style="text-align: right;">0 kWh</td>
            <td style="text-align: right;" class="border-right;">1122 kWh</td>
            <td style="text-align: right;">0 €</td>
            <td style="text-align: right; background-color: #ff0000;">281.06 €</td>
        </tr>
        <tr>
            <td class="border-right">Februar</td>
            <td style="text-align: right;">1134 kWh</td>
            <td style="text-align: right;" class="border-right;">600 kWh</td>
            <td style="text-align: right;">0 kWh</td>
            <td style="text-align: right;" class="border-right;">534 kWh</td>
            <td style="text-align: right;">0 €</td>
            <td style="text-align: right; background-color: #ff0000;">133.77 €</td>
        </tr>
        <tr>
            <td class="border-right">März</td>
            <td style="text-align: right;">716 kWh</td>
            <td style="text-align: right;" class="border-right;">1000 kWh</td>
            <td style="text-align: right;">284 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">22.15 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">April</td>
            <td style="text-align: right;">420 kWh</td>
            <td style="text-align: right;" class="border-right;">1250 kWh</td>
            <td style="text-align: right;">830 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">64.74 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">Mai</td>
            <td style="text-align: right;">394 kWh</td>
            <td style="text-align: right;" class="border-right;">1300 kWh</td>
            <td style="text-align: right;">906 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">70.67 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">Juni</td>
            <td style="text-align: right;">249 kWh</td>
            <td style="text-align: right;" class="border-right;">1350 kWh</td>
            <td style="text-align: right;">1101 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">74.87 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">Juli</td>
            <td style="text-align: right;">226 kWh</td>
            <td style="text-align: right;" class="border-right;">1380 kWh</td>
            <td style="text-align: right;">1154 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">85.88 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">August</td>
            <td style="text-align: right;">257 kWh</td>
            <td style="text-align: right;" class="border-right;">1240 kWh</td>
            <td style="text-align: right;">983 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">76.67 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">September</td>
            <td style="text-align: right;">348 kWh</td>
            <td style="text-align: right;" class="border-right;">980 kWh</td>
            <td style="text-align: right;">632 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">49.30 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">Oktober</td>
            <td style="text-align: right;">568 kWh</td>
            <td style="text-align: right;" class="border-right;">700 kWh</td>
            <td style="text-align: right;">132 kWh</td>
            <td style="text-align: right;" class="border-right;">0 kWh</td>
            <td style="text-align: right;">9.98 €</td>
            <td style="text-align: right;">0 €</td>
        </tr>
        <tr>
            <td class="border-right">November</td>
            <td style="text-align: right;">1119 kWh</td>
            <td style="text-align: right;" class="border-right;">450 kWh</td>
            <td style="text-align: right;">0 kWh</td>
            <td style="text-align: right;" class="border-right;">669 kWh</td>
            <td style="text-align: right;">0 €</td>
            <td style="text-align: right; background-color: #ff0000;">167.59 €</td>
        </tr>
        <tr>
            <td class="border-right">Dezember</td>
            <td style="text-align: right;">1625 kWh</td>
            <td style="text-align: right;" class="border-right;">300 kWh</td>
            <td style="text-align: right;">0 kWh</td>
            <td style="text-align: right;" class="border-right;">1325 kWh</td>
            <td style="text-align: right;">0 €</td>
            <td style="text-align: right; background-color: #ff0000;">331.92 €</td>
        </tr>
        <tr>
            <td><strong>Summe</strong></td>
            <td style="text-align: right;"><strong>8578 kWh</strong></td>
            <td style="text-align: right;" class="border-right;"><strong>10800 kWh</strong></td>
            <td style="text-align: right;"><strong>6022 kWh</strong></td>
            <td style="text-align: right;" class="border-right;"><strong>3650 kWh</strong></td>
            <td style="text-align: right;"><strong>454.26 €</strong></td>
            <td style="text-align: right;"><strong>914.34 €</strong></td>
        </tr>
    </tbody>
</table>


Die Kosten mit einer 10 kWp PV-Anlage wären also:

<table>
    <thead>
        <tr>
            <th>Kostenart</th>
            <th style="text-align: right;">Betrag</th>
            <th style="text-align: right;">Kummuliert über 20 Jahre<br/>(incl. 2% Steigerung p.a.)</th>
        </tr>
    <tbody>
        <tr>
          <td>Strombezug</td>
          <td style="text-align: right;">-914.34 €/Jahr - 126.43€/Jahr</td>
          <td style="text-align: right;">-25287.97 €</td>
        </tr>
        <tr>
          <td>Vergütung</td>
          <td style="text-align: right;">454.26 €/Jahr</td>
          <td style="text-align: right;">9085.20 €</td>
        </tr>
        <tr>
          <td>Zählerkosten</td>
          <td style="text-align: right;">-30 €/Jahr</td>
            <td style="text-align: right;">-600 €</td>
        </tr>
        <tr>
            <th>Gesamt</th>
            <th style="text-align: right;">490.08 €/Jahr</th>
            <th style="text-align: right;">-16802.77 €</th>
        </tr>
    </tbody>
</table>

Ich wäre nach 20 Jahren also **-16802.77 EUR** ärmer als heute, wenn ich
eine 10 kWp PV-Anlage installiere und den Eigenverbrauch maximiere.

**Faktoren, die die Wirtschaftlichkeit reduzieren:**

* Auch im Sommer wird es Tage geben, an denen Strom zugekauft werden muss. Ein
  Batteriespeicher kann dies abmildern.
* Die Module können durch Alterung oder Verschmutzung an Leistung verlieren.
* Teile der Anlage können kaputtgehen oder Wartung benötigen.
* Mehrkosten für die Gebäudeversicherung.

**Faktoren, die die Wirtschaftlichkeit erhöhen:**

* Die Strompreise werden voraussichtlich weiter steigen.
* Die Anlage hält möglicherweise länger als 20 Jahre.
* Durch geschickte Steuerung der Verbraucher (z.B. Wärmepumpe, Waschmaschine) lässt sich der Eigenverbrauchsanteil erhöhen.
* Ein Energie-Management-System (EMS) kann mit einem dynamischem Stromtarif
  zu günstigen Zeiten Strom kaufen.


## Technische Aspekte und weitere Überlegungen

Neben der Anzahl der kWp der Module und der Kapazität eines eventuellen Speichers spielen weitere
Faktoren eine wichtige Rolle:

### Lebensdauer und Garantien

Die Garantien auf die verschiedenen Komponenten variieren stark:

* **Solarmodule**: 25 Jahre Leistungsgarantie (meist 80% der Nennleistung), 10-12 Jahre Produktgarantie
* **Wechselrichter**: 5 bis 12 Jahre Garantie, oft erweiterbar
* **Batteriespeicher**: 10 Jahre Leistungsgarantie, 2 bis 10 Jahre Produktgarantie

### Wechselrichter-Eigenschaften

Der Wechselrichter ist das Herzstück der Anlage und wandelt den von den Solarmodulen
erzeugten Gleichstrom in Wechselstrom um, der im Haushalt genutzt werden kann.

Wichtige Eigenschaften:

* **Effizienz**: Moderne Wechselrichter erreichen Wirkungsgrade von über 95%
* **Notstromfähigkeit**: Kann der Wechselrichter auch bei Stromausfall Strom
    liefern? Hier ist zwischen Notstrombetrieb (nur wenige Steckdosen),
    Ersatzstrombetrieb (gesamter Haushalt) und Inselbetrieb (getrenntes Netz) zu
    unterscheiden. Die Schwarzstartfähigkeit ist eine notwendige, aber keine hinreichende Bedingung für den Ersatzstrombetrieb und Inselbetrieb.
    Für den Notstrombetrieb ist sie nicht notwendig.
* **API**: Ich will eine offene lokale Schnittstelle, um programmatisch Daten
    auszulesen und den Wechselrichter zu steuern. Damit kann ich sicherstellen,
    dass ich den Wechselrichter noch voll nutzen kann, auch wenn der Hersteller
    den Support einstellt.

### Schnittstellen und Kommunikation

Ich will die Anlage in mein bestehendes Smart Home (Home Assistant) integrieren.

Eventuell will ich auch ein unabhängiges Energie-Management-System (EMS)
einsetzen, z.B. [Optimapower](https://optimapower.ai/).

Das EMS sollte mit dem Wechselrichter / dem Batteriespeicher kommunizieren können,
ohne dass ich dafür Internet benötige.


## Fazit

Die Wirtschaftlichkeitsberechnung zeigt deutlich, dass eine Photovoltaikanlage
unter den gegebenen Bedingungen eine sehr rentable Investition darstellt. Da ich
einige konservative Annahmen getroffen habe, ist die tatsächliche Rentabilität
hoffentlich höher. Bei einer Investition von 20.000 EUR in eine 10 kWp Anlage mit
einem Batteriespeicher von 10 kWh könnte ich nach 20 Jahren etwa 4176 EUR
Gewinn über dem Vergleichsszenario ohne PV-Anlage erzielen.

Besonders vorteilhaft wirken sich aus:
- Der hohe Eigenverbrauchsanteil durch die Wärmepumpe
- Die günstige Süd-West-Ausrichtung des Dachs
- Die zu erwartenden weiteren Strompreissteigerungen

## Offene Fragen

1. Muss ich die Einspeisevergütung versteuern?
2. Kann ich die PV-Anlage von der Steuer absetzen?
3. Wie war das mit der 60% Regelung des Solarspitzengesetz?
    * Es wird keine Einspeisevergütung mehr gezahlt, wenn der Strompreis an der
      Börse ins Negative fällt.
    * Es besteht für den Messstellenbetreiber die Pflicht zum Einbau eines
      intelligenten Messsystems (Smart Meter) und einer Steuerbox, wenn die
      Anlage mindestens 7 kW Leistung hat.
    * Bis diese Technik eingebaut und getestet wird, darf die Einspeiseleistung
      nur 60 % der installierten Leistung betragen. Für Anlagen zwischen 25 und
      100 kW ist bis zum Einbau der Technik zusätzlich eine Fernsteuerbarkeit
      (z.B. über Rundsteuerempfänger) verpflichtend.
