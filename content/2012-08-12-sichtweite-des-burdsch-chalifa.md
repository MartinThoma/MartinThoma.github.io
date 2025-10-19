---
layout: post
title: Sichtweite des Burdsch Chalifa
slug: sichtweite-des-burdsch-chalifa
lang: de
author: Martin Thoma
date: 2012-08-12 13:37:17.000000000 +02:00
category: German posts
tags: mathematics, Physics, Geometry
featured_image: 2012/08/skizze-math-thumb.png
---
<h2>Aufgabenstellung</h2>
Der Burdsch Chalifa war 2010 das höchste Gebäude der Erde. Bis zur Spitze sind es 830 m.

Angenommen, die Erde wäre eine perfekte Kugel mit einem Radius von 6370 km und die Sicht wäre nicht durch Nebel, Wolken oder sonstige Hindernisse eingeschränkt. Aus welcher Entfernung, die man über die Erde direkt zum Burdsch Chalifa zurücklegt, könnte man den Burdsch Chalifa maximal sehen?

<h3>Situationsskizze</h3>
<a href="../images/2012/08/earth-skizze.png"><img src="../images/2012/08/earth-skizze.png" alt="" title="Situationsskizze für die Berechnung" width="500" height="553" class="aligncenter size-full wp-image-39311" /></a>
Gesucht ist die Länge des neongrün hervorgehobenen Kreisbogens x.

<h3>Rechenweg</h3>
\begin{align}
        x &= \text{Umfang} \cdot \frac{\varphi}{360^\circ} \\
          &= 2 \cdot r \cdot \pi \cdot \frac{\cos^{-1}(\frac{r}{r+h})}{360^\circ} \\
          &= 2 \cdot 6370 \text{km} \cdot \pi \cdot \frac{\cos^{-1}(\frac{6370}{6370,83})}{360^\circ} \\
          &= 102,8 \text{km}
    \end{align}

<h3>Antwort</h3>
Bei optimalen, also unrealistischen, Bedingungen könnte man die Spitze des Burdsch Chalifa noch in 102,8 km entfernung sehen. Dies entspricht übrigens auch dem Punkt auf der Erdoberfläche, der vom Burdsch Chalifa am weitesten entfernt und zu sehen ist.
Auch wenn nur die Luftlinie gemessen wird, sind es 102,8 km, da der Erdradius bedeutend größer als der Burdsch Chalifa ist.

Laut <a href="http://www.bild.de/lifestyle/bams/burj-chalifa/burj-chalifa-bei-dieser-story-wurde-uns-schwindelig-828-meter-11056462.bild.html">Bildzeitung</a> kann man die Spitze des Burdsch Chalifa noch in 95 km sehen.

<h2>Erweiterung der Aufgabenstellung</h2>
Das Dorf Mileiha liegt direkt östlich vom Burdsch Chalifa (25&deg; 11' 50'' N, 55&deg; 16' 27'' O).

Wie weit östlich darf das Dorf maximal liegen, damit man die Spitze des Burdsch Chalifa bei optimalen Bedingungen noch sehen kann?

Hinweis: Es gelten noch immer die gleichen Voraussetzungen wie im ersten Teil der Aufgabe.

<h3>Situationsskizze</h3>
<a href="../images/2012/08/earth-skizze-21.png"><img src="../images/2012/08/earth-skizze-21.png" alt="" title="Skizze der Erde" width="500" height="299" class="aligncenter size-full wp-image-39411" /></a>

Gesucht ist die grün eingezeichnete Kurve, die sich über die Erdoberfläche krümmt. Ihre Länge sei x.
Um diese zu berechnen, müssen wir wissen welchen Radius die Kreisfläche hat, die entsteht, wenn man die Erde am 25. Breitengrad schneidet. Der Radius dieser Kreisfläche sei $r_{25}$.

<h3>Berechnung</h3>

\begin{align}
    \text{Breitengrad} &= 25 + \frac{11}{60} + \frac{50}{60 \cdot 60} \\
    \text{Breitengrad} &= \frac{9071}{360} \approx 25,1972 \\
    \cos(\frac{9071}{360}) &= \frac{r_{25,1972}}{6370\text{km}} \\
    r_{25,1972} &= \cos(\frac{9071}{360}) \cdot 6370\text{km} \\
    r_{25,1972} &\approx 5764\text{km}
\end{align}

Der soeben errechnete Radius kann einfach in die im ersten Abschnitt erarbeitete Formel eingesetzt werden:

\begin{align}
x &= 2 \cdot r \cdot \pi \cdot \frac{\cos^{-1}(\frac{r}{r+h})}{360^\circ} \\
  &= 2 \cdot 5764 \text{km} \cdot \pi \cdot \frac{\cos^{-1}(\frac{5764}{5764,83})}{360^\circ} \\
  &\approx 97,8 \text{km}
\end{align}

Nun sollte man noch berücksichtigen, dass die Beobachter wohl nicht auf der Erde kriechen, sondern ihre Augen in einer Höhe von ca. 1,6m sind:

\begin{align}
    x &= 2 \cdot 5764 \text{km} \cdot \frac{\pi}{360^\circ} \cdot ( \cos^{-1}(\frac{5764}{5764,83}) + \cos^{-1}(\frac{5764}{5764,0016}) \\
      &\approx 102 \text{km}
\end{align}

<h3>Antwort</h3>
Der am weitesten entfernte Punkt, der direkt östlich vom Burdsch Chalifa steht und von dem aus die Spitze des Burdsch Chalifa unter optimalen Bedinungen noch erkannt werden kann, liegt ca. 102 km entfernt.

Anmerkung: Mileiha liegt ca. 60 km vom Burdsch Chalifa entfernt. Er müsste also von Mileiha zu sehen sein.
