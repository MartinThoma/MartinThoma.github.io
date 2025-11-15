---
layout: post
title: Dämmstoffe
slug: daemstoffe
lang: de
author: Martin Thoma
date: 2023-12-23 23:00
category: German posts
tags: House
featured_image: logos/house.png
---
Dämmstoffe haben neben ihrer Dämmwirkung noch weitere relevante Eigenschaften:

* Preis
* Schimmelanfälligkeit
* Wasserdurchlässigkeit
* Wasserdampfdiffusionswiderstand: Gibt an, um welchen Faktor der Stoff
  diffusionsdichter ist als gleichdicke Luft. Der Wert kann nicht unter 1 liegen,
  geht aber beliebig hoch. Glas hat z.B. einen Wert von unendlich.
* Kapillaraktivität: Kann Feuchtigkeit wegtransportieren.
* Wasseraufnahme
* Brandklasse


## Anwendung

Anwendungsgebiete sind:

* Wände (innen)
* Wände (außen; auch: Fassade)
* Decken
* Dach (innen): Zwischensparren, Untersparren
* Dach (außen): Aufsparren

Je nach Anwendungsgebiet gibt es unterschiedliche Anforderungen an den Umgang mit
Feuchtigkeit und mechanischen Belastungen.

## Wärmeleitfähigkeit

* **λ-Wert** = W/(m·K): Je kleiner der Lambda-Wert, umso weniger Wärme lässt das Material bei
  gleicher Dicke passieren.
* **R-Wert** = d / λ = (m²·K) / W: Je höher der Wärmedurchlasswiderstand eines Bauteils, umso
  weniger lässt es Wärme entweichen.
* **U-Wert** = 1 / R = W/(m²·K): Je kleiner der U-Wert, umso besser ist der Wärmeschutz.

Den Lambda-Wert gibt man für Baustoffe an, den U-Wert für Bauteile.

Die Verlustleistung $Q$ (in Watt) berechnet sich aus:

* $U$: Dem U-Wert in W/(m²·K)
* $A$: Der Fläche des Bauteils in m²
* $\Delta T$: Der Temperaturdifferenz zwischen innen und außen in Kelvin

Die Normaußentemperatur beträgt in vielen Gegenden -13°C (oder wärmer). Wir wollen
+23°C erreichen, haben also $\Delta T = 36$.


## Beispiele

<style>
.good {
    background-color: #00ff00;
}
.bad {
    background-color: #ff2222;
}
</style>

<table>
    <tr>
        <th>Baustoff</th>
        <th>Preis</th>
        <th>Brandschutzklasse</th>
        <th>Resistent gegen Insekten und Nagetiere</th>
        <th>Lambda (WLG)</th>
        <th>U-Wert (1cm)</th>
        <th>U-Wert (10cm)</th>
        <th>Dichte</th>
        <th>Energieverlust pro m&sup2; bei 10cm</th>
        <th>Wasser&shy;dampf&shy;diffusions&shy;widerstand µ</th>
        <th>Kapillar&shy;aktivität</th>
        <th>Weiteres</th>
    </tr>
    <tr>
        <td>Mineral&shy;wolle (Glaswolle als Rolle)</td>
        <td>9.50&nbsp;€/m² für 10cm</td>
        <td class="good">A1</td>
        <td class="good">✔</td>
        <td class="good">0.035&nbsp;W/mK</td>
        <td>3.5</td>
        <td>0.35</td>
        <td>...</td>
        <td>15.3 W/m&sup2;</td>
        <td>1</td>
        <td>0</td>
        <td>Saugt sich bei Nässe voll und trocknet nur langsam wieder. Dadurch kann sich Schimmel bilden<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup> - gut wenn es trocken ist, also nicht als Zwischensparrendämmung im Dach!<sup id="fnref:3"><a class="footnote-ref" href="#fn:3">3</a></sup></td>
    </tr>
    <tr>
        <td>Mineral&shy;faserplatten (Steinwolle als Platte)</td>
        <td><a href="https://www.bausep.de/isover-topdec-easyloft-dachbodendaemmung.html?361=675938">24&nbsp;€/m²</a></td>
        <td class="good">A1</td>
        <td class="good">✔</td>
        <td class="good">0.039&nbsp;W/mK</td>
        <td>3.9</td>
        <td>0.39</td>
        <td>150 kg/m&sup3;</td>
        <td>14 W/m&sup2;</td>
        <td>1</td>
        <td></td>
        <td class="good">verrottungsfest und unangreifbar von Fäulnis und Schimmel</td>
    </tr>
    <tr>
        <td>Mineral&shy;dämmplatten</td>
        <td><a href="https://www.bausep.de/multipor-tipwall-m4-mineraldaemmplatte.html?361=675938">40&nbsp;€/m² bei 10cm</a></td>
        <td class="good">A1</td>
        <td class="good">✔</td>
        <td class="good">0.042 - 0.045&nbsp;W/mK</td>
        <td>4.5</td>
        <td>0.45</td>
        <td>90 - 115 kg/m³</td>
        <td>16.2 W/m&sup2;</td>
        <td>2-5</td>
        <td>++</td>
        <td class="good">schimmelresistent; unverrottbar</td>
    </tr>
    <tr>
        <td>Kalziumsilikatplatte ("CaSi Klimaplatte")</td>
        <td>TODO €/m²</td>
        <td class="good">A1</td>
        <td class="good">✔</td>
        <td>0.070&nbsp;W/mK</td>
        <td>7</td>
        <td>0.7</td>
        <td>230 - 265kg/m&sup3;</td>
        <td>25.2 W/m&sup2</td>
        <td>5-20</td>
        <td>+++</td>
        <td class="good">stark gegen Schimmel</td>
    </tr>
    <tr>
        <td>Poroton <abbr title="Poroton mit Perlite gefüll">T7</abbr></td>
        <td><a href="https://www.baustoffshop.de/poroton-planziegel-t7-36-5-p-perlite.html">23&nbsp;€/m² bei 24.8cm Dicke</a></td>
        <td class="good">F 90-A </td>
        <td class="good">✔</td>
        <td>0.070&nbsp;W/(mK)</td>
        <td>7</td>
        <td>0.7</td>
        <td>550 kg/m&sup3;</td>
        <td>25.2 W/m&sup2;</td>
        <td>4-5</td>
        <td>✔</td>
        <td></td>
    </tr>
    <tr>
        <td>Polyurethan Hartschaum (PUR)</td>
        <td>19&nbsp;€/m² bei 10cm</td>
        <td>B2</td>
        <td class="bad">✘<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></td>
        <td class="good">0.023&nbsp;W/mK</td>
        <td>2 - 4</td>
        <td>0.2 - 0.4</td>
        <td>...</td>
        <td>10.8 W / m&sup2;</td>
        <td>60</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Expandiertes Polystyrol (EPS), Extrudiertes Polystyrol (XPS), Polystyrol ("Styropor")</td>
        <td>17&nbsp;€/m² für 12cm; </td>
        <td>B1 - B2</td>
        <td class="bad">✘<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></td>
        <td class="good">0.032 - 0.040 W/mK</td>
        <td>3.2 - 4</td>
        <td>0.32 - 0.4</td>
        <td>31 - 39 kg/m&sup3;</td>
        <td>13.0 W/m&sup2;</td>
        <td>60 - 150</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Holzfaserdämmplatten</td>
        <td>23&nbsp;€/m² für 10cm Dicke</td>
        <td class="bad">E</td>
        <td class="good">✔<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></td>
        <td class="good">0.040&nbsp;W/mK</td>
        <td>4.0</td>
        <td>0.40</td>
        <td>250 kg/m³</td>
        <td>14.4 W/m&sup2;</td>
        <td>5-10</td>
        <td></td>
        <td class="good">resistent gegen Verrottung/Pilzbefall<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></td>
    </tr>
    <tr>
        <td>Beton</td>
        <td>TODO €/m²</td>
        <td class="good">A1</td>
        <td class="good">✔</td>
        <td class="bad">1.4&nbsp;W/mK</td>
        <td>140</td>
        <td>14</td>
        <td>...</td>
        <td>504 W/m&sup2;</td>
        <td>70 – 150</td>
        <td></td>
        <td></td>
    </tr>
</table>

Wenn man jetzt ein 11m × 11m Haus hat, sich überlegt ein Geschoss (2.5m) mit ca.
20% Fenstern zu dämmen und man aktuell einen U-Wert von 1.7 W/(m²·K) hat,
dann wäre der Verlust aktuell bei

$$(11\text{m} + 11\text{m}) \cdot 2.5\text{m} \cdot 0.8 \cdot 1.7\frac{W}{\text{m}^2 \cdot K} \cdot 36 K = 2.7 kW$$

Das könnte mit einer 10cm XPS-Platte, die auf die Mauer aufgebracht wird, reduziert werden. Der neue
U-Wert kann über die R-Werte berechnet werden:

$$U_{neu} =\frac{1}{R_1 + R_2} = \frac{1}{\frac{1}{U_1} + \frac{1}{U_2}}$$

also:

$$\frac{1}{\frac{1}{1.7} + \frac{1}{0.35}} = 0.3$$

Würde man 20cm Aufbringen:

$$\frac{1}{\frac{1}{1.7} + \frac{1}{0.175}} = 0.16$$

Bei den 44m² Fläche und 36K Temperaturdifferenz ist die Wärmeverlustleistung:

* U-Wert 1.7: 2.7 kW
* U-Wert 0.3: 0.5 kW
* U-Wert 0.16: 0.3 kW

Bei angenommenen 10 Tagen mit dieser Kälte und weiteren 20 Tagen, um für die vielen
weniger kalten Tage zu rechnen, die dennoch Wärmeverlust haben, also 720h:

* U-Wert 1.7: $2.7 kW \cdot 720h = 1944 kWh$
* U-Wert 0.3: $0.5 kW \cdot 720h =  342 kWh$
* U-Wert 0.16: $0.3 kW \cdot 720h = 183 kWh$

Heizöl kostet aktuell ca. 1.13€/L und bringt 9.8 kWh/L, d.h. 0.12€/kWh:

* U-Wert 1.7: $2.7 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh}= 233€$
* U-Wert 0.3: $0.5 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh} =  41€$
* U-Wert 0.16: $0.3 kW \cdot 720h \cdot 0.12 \frac{EUR}{kWh}=  22€$


## Einzelnachweise

[^1]: n-tv.de: [Welcher Dämmstoff ist wofür geeignet?](https://www.n-tv.de/ratgeber/Welcher-Daemmstoff-ist-wofuer-geeignet-article21401269.html), 2019.
[^2]: architekt-riebler.at: [Holzfaser-Dämmplatten](http://www.architekt-riebler.at/energieeffizienz/waermedaemmungen/holzfaserdaemmung)
[^3]: Der Fachwerker: [Finger weg von diesen 3 Dämmstoffen!](https://www.youtube.com/watch?v=4iHTrwrfsIs)
