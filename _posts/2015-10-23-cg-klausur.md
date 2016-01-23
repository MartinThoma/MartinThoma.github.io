---
layout: post
title: Computergrafik - Klausur
author: Martin Thoma
date: 2015-10-23 11:30
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Computergrafik&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://ies.anthropomatik.kit.edu/mitarbeiter.php?person=beyerer">Herrn Prof. Dr. Ing. Carsten Dachsbacher</a> im Wintersemester 2015/2016 gehört. Der Artikel ist noch am Entstehen.</div>

## Behandelter Stoff

### Vorlesung

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>20.10.2015</td>
    <td>Einleitung</td>
    <td>Viele nette Bilder und Beispiele, wenig Inhalt</td>
</tr>
<tr>
    <td>22.10.2015</td>
    <td>Farbe, Darstellung &amp; Perzeption</td>
    <td><a href="https://de.wikipedia.org/wiki/Weber-Fechner-Gesetz">Weber-Fechner-Gesetz</a>, <a href="https://de.wikipedia.org/wiki/Nyquist-Shannon-Abtasttheorem">Abtasttheorem</a>, <a href="https://de.wikipedia.org/wiki/Dynamikumfang">Dynamikumfang</a>, Farbwahrnehmung im menschlichen Auge; <a href="https://de.wikipedia.org/wiki/Gammakorrektur">Gammakorrektur</a></td>
</tr>
<tr>
    <td>26.10.2015</td>
    <td>Übung</td>
    <td>gdb (bt - backtrace; p - print)</td>
</tr>
<tr>
    <td>26.10.2015</td>
    <td>&nbsp;</td>
    <td>Metamerismus: Unterschiedliche Spektren können gleichen Farbeindruck erwecken<br/>
        Addiere/subtrahiere Farbmischung<br/>
        <abbr title="Cyan, Magenta, Yellow">CMY</abbr> / <a href="https://de.wikipedia.org/wiki/CMYK-Farbmodell"><abbr title="Cyan, Magenta, Yellow, Key">CMYK</abbr></a> / <a href="https://de.wikipedia.org/wiki/RGB-Farbraum"><abbr title="Red Green Blue">RGB</abbr></a> / <abbr title="Hue Saturation Value">HSV</abbr> / <a href="https://de.wikipedia.org/wiki/CIE-Normvalenzsystem">XYZ</a><br/>
        <a href="https://de.wikipedia.org/wiki/Weber-Fechner-Gesetz">Weber-Fechner-Gesetz</a>: 2% heller
        </td>
</tr>
<tr>
    <td>29.10.2015</td>
    <td>Ray-Tracing: Kapitel 2</td>
    <td>Menschen nehmen Kontrastintensität und Luminenz besser als Chrominanz war.
        Das ermöglicht Kompression.<br/>
        clear-type / subpixel Darstellung<br/>
        Jaggies: Unerwünschter Treppenstufen-Effekt bei Rasterisierung von Strecken<br/>
        Kamera: Position (x,y,z), Blickrichtung (zu einem Punkt mit Koordinaten (x,y,z)) und up-Vektor<br/>
        Skalarprodukt, Kreuzprodukt<br/>
        <a href="https://de.wikipedia.org/wiki/Baryzentrische_Koordinaten">Baryzentrische Koordinaten</a>,
        </td>
</tr>
<tr>
    <td>02.11.2015</td>
    <td>Übung</td>
    <td>Rasterisierung von Linien (Implizite Darstellung)<br/>
        zbuffer: Tiefe des "nächsten" Polygons pro Pixel wird gespeichert<br/>
        Konsistenzregeln, z.B. wenn man zwei benachbarte farbige Dreiecke mit Diagonale hat
        und man die Farbe des Pixels berechnen muss, durch den beide Dreiecke
        teilweise gehen (37 Fälle; Katalog von Microsoft; macht die Hardware)</td>
</tr>
<tr>
    <td>26.11.2015</td>
    <td>?</td>
    <td><a href="https://en.wikipedia.org/wiki/Sphere_mapping">Sphere Mapping</a>; Vorfilterung von Environment Maps</td>
</tr>
<tr>
    <td>10.12.2015</td>
    <td>Räumliche Datenstrukturen</td>
    <td>BSP-Baum, kD-Baum</td>
</tr>
<tr>
    <td>14.01.2016</td>
    <td>OpenGL</td>
    <td>&nbsp;</td>
</tr>
<tr>
    <td>18.01.2016</td>
    <td>Übung</td>
    <td>Koordinatensystem-Pipeline, Shader</td>
</tr>
<tr>
    <td>19.01.2016</td>
    <td>Erzeugung von Landschaften</td>
    <td>Rotes / Rosa Rauschane, Lattice Value Noise, Perlin-Noise</td>
</tr>
</table>

### Folien

#### 10.12.2015

<dl>
  <dt><dfn>BSP-Baum</dfn></dt>
  <dd>TODO</dd>
  <dt><dfn>Surface Area Heuristics</dfn> (<dfn>SAH</dfn>)</dt>
  <dd>Schätzfunktion für die Oberfläche eines Objekts (TODO?).</dd>
</dl>

#### 19.01.2016

<dl>
    <dt><dfn>Perlin-Noise</dfn></dt>
    <dd>Zufallszahlen-Pool + Hash + Permutation</dd>
    <dt><dfn>Oktave</dfn></dt>
    <dd>Sammlung von Noise-Funktionen</dd>
</dl>


### Prüfungsfragen

Kommt noch... spätestens wenn die Klausur naht.

### Übungen

#### Blatt 1

Das Framework bekommt man ohne VM unter Ubuntu 15.04 nach der Installtion
folgender Pakete (vielleicht) zum laufen:

```bash
$ sudo apt-get install cmake xorg-dev libglu1-mesa-dev freeglut3 freeglut3-dev libglew1.5 libglew1.5-dev libglu1-mesa libglu1-mesa-dev libgl1-mesa-glx libgl1-mesa-dev libglfw3
```

Wenn ihr den Fehler

> error adding symbols: DSO missing from command line ubuntu

bekommt, dann solltet ihr einfach die obigen Pakete installieren, den
`build`-Ordner löschen und es neu versuchen.

{% gallery columns="3" size="medium" %}
    ../images/2015/11/color-cube.png     "Color cube"
    ../images/2015/11/gravity-field.png  "Gravity field"
    ../images/2015/11/temperature.png    "Temperature of a black body"
{% endgallery %}

Außerdem:

```bash
$ pacman -Syy
```

ausführen. Dann bekommt man auch nicht mehr 404er wenn man mit

```
$ pacman -S vim
```

vim installieren will.

In der VM sollte unter Settings → System → Acceleration die Option "Enable
VT-x/AMD-V" aktiviert sein. Zusätzlich sollte im BIOS des Host-Systems (also
von eurem Rechner) die "Intel Virtualization Technology" aktiviert sein.
(Man Laptop hat das nicht - bei mir funktionieren die Beispiele in der VM
aber auch nicht :-/)


## Material und Links

* [Vorlesungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/index.php)
* [&Uuml;bungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/uebung.php)
* [E-Mail Verteiler](https://lists.ira.uni-karlsruhe.de/mailman/listinfo/cg.cg)

## Übungsbetrieb

Es gibt Übungsblätter und Übungen, aber keine Tutorien und keine Bonuspunkte.

Um das Modul zu bestehen wird der Übungsschein benötigt. Für den Übungsschein
benötigt man 60% der Punkte der Übungsblätter. Die Übungsblätter werden über
[submit.ivd.kit.edu](https://submit.ivd.kit.edu/main/index.php) eingereicht.
Die Übungsblätter erscheinen alle 2&nbsp;Wochen. Es gibt also min.
6&nbsp;Übungsblätter und min. 120&nbsp;Punkte. Die Deadline ist Montag, 11:00.


## Termine und Klausurablauf

**Datum**: Mittwoch, der 09.03.2015 von 14:00 Uhr (Quelle: [informatik.kit.edu](http://www.informatik.kit.edu/klausuren.php?kid=546.35))<br/>

* 08.02.2016: Die Klausur-Anmeldung wird freigeschalten
* 04.03.2016: Anmeldeschluss
* 06.03.2016: Abmeldeschluss


**Ort**: <a href="https://www.kithub.de/map/2086">10.21 (Daimler und Benz)</a><br/>
**Punkte**: ?<br/>
**Zeit**: ? min<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: ?<br/>
**Bonuspunkte**: ?<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: Noch nicht bekannt (Stand: 23.10.2015)<br/>
**Erlaubte Hilfsmittel**: keine
