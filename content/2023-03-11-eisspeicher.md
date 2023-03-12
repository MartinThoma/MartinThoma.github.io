---
layout: post
title: Eisspeicher
slug: eisspeicher
author: Martin Thoma
date: 2023-03-11 20:00
category: German posts
tags: house, money, energy, heating
featured_image: logos/house.png
---
Im Jahr 2023 stehen in Deutschland verschiedene Heizsysteme zur Verfügung,
darunter Öl-, Gas-, Holzpellet- und Wärmepumpenheizungen. Innerhalb der
Kategorie der Wärmepumpen gibt es verschiedene Varianten wie Luft-Luft- und
Luft-Wasser-Wärmepumpen sowie Erdwärmepumpen mit unterschiedlichen Ausführungen.

Wärmepumpenheizungen arbeiten nach dem gleichen Prinzip wie ein Kühlschrank,
jedoch mit dem umgekehrten Ziel. Während der Kühlschrank die unerwünschte Wärme
aus dem Inneren nach außen transportiert, transportieren Wärmepumpenheizungen
Wärme von außen nach innen, um das Haus zu heizen. Hierbei wird die Energie
nicht direkt zum Heizen verwendet, sondern um ein Kältemittel zu komprimieren
und somit die Wärme zu "pumpen".

Wärmepumpenheizungen erfreuen sich einer hohen Beliebtheit aufgrund ihres hohen
Wirkungsgrades, der durch den COP-Wert (Coefficient of Performance) beschrieben
wird. Dieser Wert gibt an, wie viel Wärme die Wärmepumpe pro verbrauchter
Kilowattstunde Strom produziert. Inzwischen erreichen Wärmepumpenheizungen einen
COP-Wert von 4 oder höher, was bedeutet, dass sie für jede verbrauchte
Kilowattstunde Strom mindestens 4 Kilowattstunden an Wärme in der Wohnung
bereitstellen. Dies ist jedoch ein Durchschnittswert, der im Laufe des Jahres
variieren kann.

Ein entscheidender Faktor für die Effizienz von Wärmepumpenheizungen ist die
Temperaturdifferenz. Je höher die Temperaturdifferenz ist, desto schlechter ist
der Wirkungsgrad der Wärmepumpe. Aus diesem Grund ist es wünschenswert, extrem
kalte Temperaturen zu vermeiden. Erdwärmepumpen nutzen daher die Wärme des
Erdbodens. Allerdings sind Bohrungen für eine
Erdsonde nicht immer möglich und können kostspielig sein.

Als Alternative kann ein Eisspeicher installiert werden. Dies ist ein
Betonzylinder mit einem Fassungsvermögen von ca. 10m³ Wasser. Im
Sommer wird dem Wasser Wärme zugeführt, so dass der Eisspeicher zum Kühlen
verwendet werden kann. Im Winter kann die im Eisspeicher gespeicherte Wärme dann
wieder zum Heizen abgezogen werden.

## Energiegehalt

### Wassermenge

Von wie viel Wasser reden wird?

* 10m³ = 10.000 L
* Eis hat eine Dichte von 0.918 kg/L.

Also sind 10.000L bei 9180kg.

### Wärme Grundlagen

* spezifische Wärmekapazität von Wasser: 4190 J / (kg * K).
* Schmelzwärme von Wasser: 344 kJ / kg
* 1 kWh = 3600 kJ

Man benötigt also 4190 Joule um 1 kg Wasser um 1 Kelvin zu erwärmen.
Man benötigt jeodhc 344 kJ um 1 kg Eis zu schmelzen. Also genauso viel Energie
wie um 1 kg Wasser von 0°C auf 82°C zu erhitzen!

### Konkrete Wärmespeicher

Angenommen wir sind bei ca +9°C Wassertemperatur und haben keine Wärmeverluste.

Dann können wir durch das Abkühlen des Wasser von 9°C auf 0°C (flüssig) folgende
Energiemenge extrahieren:

\begin{align}
        & 4190\frac{\text{J}}{\text{kg} \cdot \text{K}} \cdot 9180\text{kg} \cdot 9\text{K}\\
       =& 346177800\text{J}\\
       =& 346177.8\text{kJ}\\
 \approx& 96\text{kWh}
\end{align}

Durch den Phasenübergang (Schmelzwärme) können wir 344 kJ/kg ⋅ 9180kg = 3157920 kJ = 877 kWh
extrahieren.

Insgesamt könnte der Wärmespeicher also 877 kWh + 96 kWh = 973 kWh vom Sommer
in den Winter bringen.

### Energiebedarf

Ein Haus mit 155m² Wohnfläche und einem Bedarf von 96 kWh / (m² ⋅ a) benötigt
im Jahr 14880 kWh zum heizen.

Der Wärmespeicher würde also 6.5% des Jahresbedarfs decken.

## Kritik

Folgendes habe ich hier nicht berücksichtigt:

* Auch im Winter wird der Erdboden vermutlich Wärme an den Wärmespeicher abgeben.
  Man kann also vermutlich mehr als die 973 kWh extrahieren.
* Der Wärmespeicher ist nicht perfekt isoliert - daher habe ich auch "nur" mit
  9°C gerechnet. Im Sommer dürfte die [Bodentemperatur](https://de.wikipedia.org/wiki/Bodentemperatur)
  in den 4m tiefe wohl eher höher sein.
* Der Heizbedarf ist nicht nur im Winter. Auch im Frühling oder in kühlen
  Sommernächten muss man heizen. Auch das spricht für eine höhere Abdeckung.


## Wirtschaftlichkeit

Der Eisspeicher kostet ca. 7000€ - 12000€ ([Quelle](https://www.heizung.de/waermepumpe/eisspeicher.html)).
Gehen wir mal von 10.000 EUR aus - und das ist vermutlich wesentlich zu niedrig.

Angegeben wird von Viessmann ein COP-Wert von bis zu 5 ([Quelle](https://www.baulinks.de/webplugin/2022/0265.php4)). Eine Luftwärmepumpe ist eher be 4.

Angenommen das würde für die benötigten 14880 kWh gelten (was es nicht tut, es
wird weniger/schlechter sein), dann würde man 2976 kWh Strom anstelle von
3720 kWh Strom pro Jahr für die Heizung bezahlen. Man spart sich also 744 kWh
Strom.

Bei einem Strompreis von 0.34 EUR/kWh sind das ca. 250€/Jahr.

Die Amortisationszeit wäre also bei 10.000 EUR/ (250 EUR/Jahr) = 40 Jahren - und
das obwohl ich Wartungskosten nicht berücksichtigt habe.

Investiert man in den S&P 500, so bekommt man im Schnitt pro Jahr relativ
sicher 5% Wertsteigerung. Das muss jede andere Investition schlagen. Das
bedeutet eine Verdoppelung nach 14 Jahren.

Der Eisspeicher lohnt sich also leider sehr deutlich nicht.

## Fazit

Der Eisspeicher ist ein tolles Konzept, aber zumindest für ein Einfamilienhaus
im Altbestand lohnt er sich einfach nicht.
