---
layout: post
status: publish
published: true
title: Sichtweite des Burdsch Chalifa
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 39301
wordpress_url: http://martin-thoma.com/?p=39301
date: 2012-08-12 13:37:17.000000000 +02:00
categories:
- German posts
tags:
- mathematics
- Physics
- Geometry
comments: []
featured_image: 2012/08/skizze-math-thumb.png
---
<h2>Aufgabenstellung</h2>
Der Burdsch Chalifa war 2010 das h&ouml;chste Geb&auml;ude der Erde. Bis zur Spitze sind es 830 m.

Angenommen, die Erde w&auml;re eine perfekte Kugel mit einem Radius von 6370 km und die Sicht w&auml;re nicht durch Nebel, Wolken oder sonstige Hindernisse eingeschr&auml;nkt. Aus welcher Entfernung, die man &uuml;ber die Erde direkt zum Burdsch Chalifa zur&uuml;cklegt, k&ouml;nnte man den Burdsch Chalifa maximal sehen?

<h3>Situationsskizze</h3>
<a href="http://martin-thoma.com/wp-content/uploads/2012/08/earth-skizze.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/08/earth-skizze.png" alt="" title="Situationsskizze f&uuml;r die Berechnung" width="500" height="553" class="aligncenter size-full wp-image-39311" /></a>
Gesucht ist die L&auml;nge des neongr&uuml;n hervorgehobenen Kreisbogens x.

<h3>Rechenweg</h3>
$\begin{align}
        x &= \text{Umfang} \cdot \frac{\varphi}{360^\circ} \\
          &= 2 \cdot r \cdot \pi \cdot \frac{\cos^{-1}(\frac{r}{r+h})}{360^\circ} \\
          &= 2 \cdot 6370 \text{km} \cdot \pi \cdot \frac{\cos^{-1}(\frac{6370}{6370,83})}{360^\circ} \\
          &= 102,8 \text{km}
    \end{align}$

<h3>Antwort</h3>
Bei optimalen, also unrealistischen, Bedingungen k&ouml;nnte man die Spitze des Burdsch Chalifa noch in 102,8 km entfernung sehen. Dies entspricht &uuml;brigens auch dem Punkt auf der Erdoberfl&auml;che, der vom Burdsch Chalifa am weitesten entfernt und zu sehen ist.
Auch wenn nur die Luftlinie gemessen wird, sind es 102,8 km, da der Erdradius bedeutend gr&ouml;&szlig;er als der Burdsch Chalifa ist.

Laut <a href="http://www.bild.de/lifestyle/bams/burj-chalifa/burj-chalifa-bei-dieser-story-wurde-uns-schwindelig-828-meter-11056462.bild.html">Bildzeitung</a> kann man die Spitze des Burdsch Chalifa noch in 95 km sehen.

<h2>Erweiterung der Aufgabenstellung</h2>
Das Dorf Mileiha liegt direkt &ouml;stlich vom Burdsch Chalifa (25&deg; 11' 50'' N, 55&deg; 16' 27'' O).

Wie weit &ouml;stlich darf das Dorf maximal liegen, damit man die Spitze des Burdsch Chalifa bei optimalen Bedingungen noch sehen kann?

Hinweis: Es gelten noch immer die gleichen Voraussetzungen wie im ersten Teil der Aufgabe.

<h3>Situationsskizze</h3>
<a href="http://martin-thoma.com/wp-content/uploads/2012/08/earth-skizze-21.png"><img src="http://martin-thoma.com/wp-content/uploads/2012/08/earth-skizze-21.png" alt="" title="Skizze der Erde" width="500" height="299" class="aligncenter size-full wp-image-39411" /></a>

Gesucht ist die gr&uuml;n eingezeichnete Kurve, die sich &uuml;ber die Erdoberfl&auml;che kr&uuml;mmt. Ihre L&auml;nge sei x.
Um diese zu berechnen, m&uuml;ssen wir wissen welchen Radius die Kreisfl&auml;che hat, die entsteht, wenn man die Erde am 25. Breitengrad schneidet. Der Radius dieser Kreisfl&auml;che sei $r_{25}$.

<h3>Berechnung</h3>
$
        \begin{align}
            \text{Breitengrad} &= 25 + \frac{11}{60} + \frac{50}{60 \cdot 60} \\
            \text{Breitengrad} &= \frac{9071}{360} \approx 25,1972 \\
            \cos(\frac{9071}{360}) &= \frac{r_{25,1972}}{6370\text{km}} \\
            r_{25,1972} &= \cos(\frac{9071}{360}) \cdot 6370\text{km} \\
            r_{25,1972} &\approx 5764\text{km}
        \end{align}
$

Der soeben errechnete Radius kann einfach in die im ersten Abschnitt erarbeitete Formel eingesetzt werden:
$
    \begin{align}
        x &= 2 \cdot r \cdot \pi \cdot \frac{\cos^{-1}(\frac{r}{r+h})}{360^\circ} \\
          &= 2 \cdot 5764 \text{km} \cdot \pi \cdot \frac{\cos^{-1}(\frac{5764}{5764,83})}{360^\circ} \\
          &\approx 97,8 \text{km}
    \end{align}
$

Nun sollte man noch ber&uuml;cksichtigen, dass die Beobachter wohl nicht auf der Erde kriechen, sondern ihre Augen in einer H&ouml;he von ca. 1,6m sind:

$
    \begin{align}
        x &= 2 \cdot 5764 \text{km} \cdot \frac{\pi}{360^\circ} \cdot ( \cos^{-1}(\frac{5764}{5764,83}) + \cos^{-1}(\frac{5764}{5764,0016}) \\
          &\approx 102 \text{km}
    \end{align}
$

<h3>Antwort</h3>
Der am weitesten entfernte Punkt, der direkt &ouml;stlich vom Burdsch Chalifa steht und von dem aus die Spitze des Burdsch Chalifa unter optimalen Bedinungen noch erkannt werden kann, liegt ca. 102 km entfernt.

Anmerkung: Mileiha liegt ca. 60 km vom Burdsch Chalifa entfernt. Er m&uuml;sste also von Mileiha zu sehen sein.
