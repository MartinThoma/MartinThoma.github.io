---
layout: post
lang: de
title: Heizlastberechnung
slug: heizlastberechnung
author: Martin Thoma
date: 2023-08-12 20:00
category: German posts
tags: house, money
featured_image: logos/house.png
---
Ich will einige Energetische Sanierungsmaßnahmen an meinem Haus durchführen,
falls es denn wirtschaftlich sinnvoll ist. Dafür muss ich wissen wie groß die
Wärmepumpe dimensioniert sein muss. Ich muss das ggf. pro Raum wissen um beurteilen
zu können, ob ich neue Heizkörper benötige.

Die Heizlast ist die Wärmemenge, welche zur Aufrechterhaltung der Raumtemperatur
nötig ist. Da ich wissen will wie viel Leistung die Wärmepumpe(n) bringen sollen,
muss ich mir vor allem die Extremwerte ansehen.

## Normaußentemperatur

> Die Normaußentemperatur ist die tiefste Temperatur einer Kälteperiode, welche
> sich 10 Mal innerhalb von 20 Jahren über einen Zeitraum von mindestens zwei
> aufeinanderfolgenden Tagen gehalten haben muss.

Quelle: [haustechnikverstehen.de](https://www.haustechnikverstehen.de/glossary/normaussentemperatur/)

Es ist also insbesondere nicht die kälteste gemessene Temperatur. Es ist jedoch
eine sinnvolle annahme für die Dimensionierung des Heizsystems.

Beispiel: In Müchen (PLZ 80939) ist die Norm-Außentemperatur bei -12.9°C, aber
die kälteste gemessene Temperatur bei -19.20°C ([Quelle](https://www.waermepumpe.de/normen-technik/klimakarte/)).
Das Histogram zeigt, dass es in München zwischen 2005 und 2023 im Schnitt in einem
Jahr nur 5.8 Stunden unter -13°C hatte.

Legt man seine Heiztechnik nun für -12.9°C aus, dann ist es in diesen 5.8
Stunden im Jahr unterdimensioniert. In der Zeit verliert das Haus also Wärme,
wenn man nicht gegensteuert. Das kann man z.B. einfach mit einem mobilen
Heizlüfter für 20€. Allerdings sind diese 5 Stunden vermutlich eh in der Nacht.
Und das Haus wird ja nicht sofort klirrend kalt, sonder kühlt allmählich ab.

Wenn man hingegen die Heiztechnik nicht auf -12.9°C sondern auf -19.20°C auslegt,
dann kann man mit einigen tausend Euro an Mehrkosten rechnen.


## Hüllflächenverfahren

Das Hüllflächenverfahren habe ich von [schlau
energiesparen](https://www.youtube.com/watch?v=iwjGjYLrSOM) ([Alex
Boerger](https://www.linkedin.com/in/boerger/)) gelernt. Das Video und den Kanal
kann ich sehr empfehlen.

Das Hüllflächenverfahren ist eine einfache Methode zur berechnung der Heizlast
pro Raum.

Die Wärmeverluste lassen sich in zwei Kategorien aufteilen:

* **Lüftungswärmeverluste**: Wärmeverluste duch Luftaustausch
* **Transmissionswärmeverluste**: Wärmeverluste duch Abstrahlung

Die Berechnung von beiden werde ich im folgenden erklären. Um ein intutives
Verständnis von diesen zu bekommen:

Eine geschlossene Plastik-Tüte hat keinen Luftaustausch. Es gibt also keine
Lüftungswärme-Verluste. Dennoch wird es in der Tüte kalt. Das sieht man z.B.
wenn man Wassereis in den Gefrierschrank legt. Das sind reine
Transmissunswärmeverluste.

Umgekehrt verhindern diese Glasfaser-Dämmplatten nicht, dass es durch zieht.
Wenn man also zu viel Luftaustausch hat, dann kann der Lüftungswärmeverlust
auch hoch sein.


### Lüftungswärmeverluste

Man muss die Raumluft etwa alle zwei Stunden wechseln um Schimmel zu vermeiden.
Teilweise sehe ich auch 4x pro Tag ([Quelle](https://www.ndr.de/ratgeber/verbraucher/Wohnung-richtig-lueften-So-laesst-sich-Schimmel-vermeiden,richtiglueften100.html)), aber hier rechne ich mal lieber vorsichtig. Da die Gebäudehülle auch nicht
ganz dicht ist, nehme ich hier lieber einen höheren Wert an.

Ich muss also jede Stunde die Hälfte des Raumvolumens austauschen. Das heißt,
dass ich die Luft mit der Außentemperatur auf die Innentemperatur anheben muss.

Ich brauche also:

* **Raumvolumen $V$**: Typischerweise B×L×H. Bei einer Dachschräge oder nicht-Quaderförmigen
  Räumen wirds komplizierter, aber das ist immer noch alles einfache Geometrie.
* **Energie für 1m³ Luft**: 0.34 Wh / K
* **Pro Stunde die Hälfte des Raumvolumens**
* **Temperaturdifferenz $\Delta_T$**: Die gewünschte Innentemperatur minus die Norm-Außentemperatur

Daher ist die Leistung für den Ausgleich der Lüftungswärmeverluste:

$P_{\text{Lüftung}} = 0.34 \frac{Wh}{K} \cdot \frac{V}{2} \cdot \Delta_T$

Beispiel: Angenommen ich habe einen Raum mit 3m Länge, 4m Breite, und einer Raumhöhe von 2.45m. Dann habe ich ein Volumen von $V = 3\text{m} \cdot 4\text{m} \cdot 2.45\text{m} = 29.4\text{m}^3$.
Angenommen ich habe eine Norm-Außentemperatur von -13°C und eine Wunschtemperatur von 22°C.
Dann habe ich $\Delta_T = 22 - (-13) = 35 K$.

Um die Lüftungsverluste dieses Raumes auszugleichen muss ich also Wärme in Höhe
von $= 0.34 \frac{Wh}{K} \cdot \frac{29.4\text{m}^3}{2} \cdot 35 K \approx 175W$
hinzuführen.


### Transmissionswärmeverluste

Hier kommt es auf die Außenfläche an und der Wärmedurchgangskoeffzient (U-Wert)
kommt ins spiel. Der U-Wert gibt an wie viel Energie verloren geht, wenn
draußen die Temperatur ein Grad kälter ist. Er wird in $\frac{W}{m^2 \cdot K}$ angegeben.

Hier muss man jetzt sehr viele Flächen berechnen und die U-Werte der Bauteile
kennen. Das Bundesministeriumfür Wirtschaft und Energie sowie das Bundesministeriumdes Innern, für Bau und Heimat
haben für Altbauten Tabellen in einer [Bekanntmachung der Regeln zur Datenaufnahme und Datenverwendungim Wohngebäudebestand](https://www.bundesanzeiger.de/pub/publication/qzQUGd8A3unSCCbVMcf?0) aufgelistet.

Die wichtigsten Punkte:

* **Fenster**: z.B. die Baualtersklasse 1984 bis 1994 hat bei Holzfenstern mit zwei Scheiben einen U-Wert von $2.7 \frac{W}{m^2 \cdot K}$.
* **Rolläden**: z.B. $3.6 \frac{W}{m^2 \cdot K}$
* **Außenwände / Decke**: z.B. $0.6 \frac{W}{m^2 \cdot K}$

Angenommen der Raum hat ein Fenster mit den Maßen 1.10m × 1.20m. Dabei messe ich
die Niesche, nicht nur das Glas. Der U-Wert gilt für das Bauteil insgesamt.
Manchmal sieht man auch $U_W$ (w für window, also Fenster) und $U_G$ (g für glass, also das Fensterglaß).
Der $U_W$ Wert bezieht sich auf das ganze Bauteil.

Dann habe ich nur für das Fenster einen Wärmeverlust von $2.7\frac{\text{W}}{\text{m}^2 \cdot K} \cdot (1.1\text{m} \cdot 1.2\text{m}) \cdot (22 - (-13))K \approx 125 \text{W}$.

Die Rolladenfläche kann man einfach mit 10% der Fensterfläche annehmen. Dafür gibts dann
$3.6 \cdot 0.132 \cdot 35 \text{W} \approx 17\text{W}$.

Angenommen zwei Wände sind Außenwände. Interessant ist die Fläche von außen und
nicht von Innen. Wir können aber die Innenfläche berechnen und +25% addieren, also:

$0.6 \cdot (2.45 \cdot (4 + 3)) \cdot 1.25 \cdot 35 \text{W} \approx 450 \text{W}$.

Jetzt nehmen wir auch mal an, das sowohl das Geschoss darunter als auch das
Geschoss darüber beheizt sind. Dann sind wir hier fertig.

Wir kommen also auf Transimissionsverluste von $125 + 17 + 450 \text{W} = 592 \text{W}$.



## Die Leistung von Heizkörpern

[DIN EN 442 (Radiatoren und Konvektoren)](https://www.beuth.de/de/norm/din-en-442-2/207503152) gibt an welche
Leistung verschiedene Heizkörper haben. Ich habe die Norm nicht gelesen, habe aber
Auszüge davon gesehen.

Als erstes muss man die Maße (Breite × Höhe) des Heizkörpers bestimmen. Dann
braucht man den Heizkörper-Typ. Dieser besteht aus zwei Ziffern:

* Erste Ziffer: Anzahl der Platten, durch die Wasser fließt. Entweder 1, 2 oder 3.
* Zweite Ziffer: Anzahl der Lamellen. Entweder 0, 1, 2, oder 3.

Das kann man einfach sehen, wenn man den Heizkörper von oben anschaut.

Nun gibts Tabellen für die einzelnen Typen:

* [Typ 11](https://www.as-heizkoerper.de/contents/de/d57_din_en_442_bei_55_45_raum_20.html)
* [Typ 21](https://www.as-heizkoerper.de/contents/de/d59_DIN_EN_442_bei_75_60C_Raum_20C.html)
* [Typ 22](https://www.as-heizkoerper.de/contents/de/d83_Waermeleistung-Heizkoerper-Typ-22.html)
* [Typ 33](https://www.as-heizkoerper.de/contents/de/d84_Waermeleistung-Heizkoerper-Typ-33.html)

Die Angaben sind nun in der Form (exemplarisch für Typ 22, B80×H60):

* Vorlauf-Temperatur / Rücklauf-Temperatur / Raumtemperatur: Leistung
* 55 °C / 45°C / 20°C: 707 Watt
* 70 °C / 55°C / 20°C: 1128 Watt
* 75 °C / 65°C / 20°C: 1403 Watt

Wenn man also für einen Raum einen Wärmebedarf von 1200 Watt ermittelt hat und
man hat nur einen Heizkörper Typ 22 (B80×H60) darin, dann benötigt man eine
Vorlauftemperatur von 75°C.

Man kann die Vorlauftemperatur nur für das Gesamtgebäude festlegen. Daher
dominiert hier das schwächste Glied.

## Weiteres

* https://www.ubakus.de/u-wert-rechner/
* https://www.sbz-monteur.de/gut-zu-wissen/norm-waermeleistung-oder-reale-bedingungen
