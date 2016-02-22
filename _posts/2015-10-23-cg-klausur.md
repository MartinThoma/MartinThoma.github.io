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

#### Bilder, Farbe, Perzeption

Slide: `01_ Bilder, Farbe, Perzeption - Teil1.pdf`

<dl>
    <dt><dfn>Frame Buffer</dfn></dt>
    <dd>Speichert Bilder zur direkten wiedergabe auf dem Bildschirm.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Dithering_(Bildbearbeitung)"><dfn>Ditherhing</dfn> (<dfn>Fehlerdiffusion</dfn>)</a></dt>
    <dd>Ditherhing ist eine Methode zur Illusion einer größeren Farbtiefe.</dd>
    <dt><dfn>Dynamikumfang</dfn></dt>
    <dd>Der Dynamikumfang beschreibt den erreichbaren Kontrast eines Wiedergabegrätes (Bildschirm, Beamer):
        \[R_d = \frac{I_{\text{max} + k}}{I_{\text{min}} + k}\]

        TODO: Was ist \(k\)? Was ist \(I_{max} / I_{min}\)?</dd>
    <dt><dfn>Gamma-Korrektur</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Transferfunktion</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Gammut</dfn> (<dfn>Farbgammut</dfn>)</dt>
    <dd>TODO</dd>
</dl>

Slide: `01_ Bilder, Farbe, Perzeption - Teil2.pdf`

<dl>
    <dt><dfn>Additive Farmbischung</dfn></dt>
    <dd>Grundfarben: Rot, Grün, Blau<br/>
        Anwendung: Bildschirm</dd>
    <dt><dfn>Subtraktive Farbmischung</dfn></dt>
    <dd>Grundfarben: Cyan, Magenta, Gelb<br/>
        Anwendung: Drucker</dd>
    <dt><dfn>Graßmansche Gesetze</dfn></dt>
    <dd>Jeder Farbeindruck kann mit 3 Grundgrößen beschrieben werden.</dd>
    <dt><dfn>Weber-Fechner-Gesetz</dfn></dt>
    <dd>Das Weber-Fechner-Gesetz macht eine Aussage über die subjektiv
        empfundene Stärke von Sinneseindrücken im Abhängigkeit von der
        Intensität des Helligkeitsunterschiedes:

        TODO</dd>
</dl>

* RGB-Farbraum: Addition der Spektren, wird bei CRT/LCD-Farbmonitoren verwendet.
* CMY, CMYK: Subtraktive Farbmischung, wird bei Druckern verwendet. K (schwarz) nur aus praktischen Gründen.
* HSV-Farbraum: Weder Additiv noch subtraktiv, wird bei Benutzerschnittstellen verwendet
* CIE Color Matching Functions
* XYZ Color Space: Farbraum für Konversion zwischen Farbräumen
* Chromatizität
* xyY Farbraum
* Machsche Streifen / Bandeffekte
* Hermann-Gitter / Laterale Hemmung
* Windows clear type / Subpixel


#### Raytracing

Side: `02_ Raytracing (enthalt Abtastung aus Kapitel 1).pdf`

* Nyquist-Shannon-Abtasttheorem
* Vektoren, Ortsvektoren, Skalarprodukt
* Parametrisierte Geraden- und Ebenendarstellung
* Baryzentrische Koordinaten
* Strahl-Kugel-Schnitt
* Spekulare Reflektion
* Diffuse (Lambertsche) Reflektion
* BRDF - Bidirectional Reflectance Distribution Function
* Phong Beleuchtungsmodell
* Snellsches Brechungsgesetz
* Fresnel-Effekt
* Anti-Aliasing Strategien: Uniformes Supersampling, Adaptives Supersampling,
  Stochastisches Supersampling
* Schattenstrahlen
* Bewegungs- und Tiefenunschärfe
* Imperfekte Spiegelung und Transmission


#### Transformationen und homogene Koordinaten

Slide: `03_ Transformationen und homogene Koordinaten.pdf`

<dl>
    <dt><dfn>Orthogonale Matrix</dfn></dt>
    <dd>Eine quadratische Matrix \(M \in \mathbb{R}^{n \times n}\) heißt
        genau dann orthogonal, wenn
        \[M^T \cdot M = M \cdot M^T = I_{n \times n}\]

        Für orthogonale Matrizen gilt also \(M^{-1} = M^T\)</dd>
    <dt><dfn>Homogene Koordinaten</dfn></dt>
    <dd>Der euklidische bzw. affine Raum wird um sog. <i>Fernpunkte</i>
        ergänzt.</dd>
    <dt><dfn>Rotation</dfn></dt>
    <dd>Die Rotation um (0, 0) in homogenen Koordinaten geht wie folgt:
        \[\begin{pmatrix}\cos \alpha & -\sin \alpha & 0\\ \sin \alpha & \cos \alpha & 0 \\ 0 '& 0 & 1\end{pmatrix}\]
    </dd>
    <dt><dfn>Skalierung</dfn></dt>
    <dd>Eine Skalierung in homogenen Koordinaten geht wie folgt:
        \[\begin{pmatrix}s_x & 0 & 0 & 0\\ 0 & s_y & 0 & 0\\ 0 & 0 & s_x & 0\\ 0 & 0 & 0 & 1\end{pmatrix}\]
    </dd>
    <dt><dfn>Scherung</dfn></dt>
    <dd>Eine Scherung in homogenen Koordinaten geht wie folgt:
        \[\begin{pmatrix}1 & 0 & d_x & 0\\ 0 & 1 & d_y & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix}\]
    </dd>
    <dt><dfn>Koordinatensysteme</dfn></dt>
    <dd>
        <ul>
            <li>Objektkoordinaten: Sie werden durch die <i>Modelltransformation</i> zu</li>
            <li>Weltkoordinaten: Sie werden durch die <i>Kameratransformation</i> zu</li>
            <li>Kamerakoordinaten</li>
        </ul>

        Der Ursprung des Welt-Koordiantensystems wird mit 0 bezeichnet.
        Die Basisvektoren mit \(x, y\).

        Das Modellkoordinatensystem hat den Ursprung \(e\) und die Basisvektoren
        \(u, v\)
    </dd>
</dl>

* Transformationen werden grundsätzlich so dargestellt: <div>\[x' \gets M \cdot x\]</div>
  Es wird also der zu transformierende Vektor von rechts mit der Transformationsmatrix M
  multipliziert.
* Spiegelung an der y-Achse ist eine Multiplikation der x-Koordinaten mit (-1)
* Hierarchisches Modellieren, Szenengraph


#### Texturen

Slide: `04_ Texturen.pdf`

<dl>
    <dt><dfn>Texturen</dfn></dt>
    <dd>Texturen können vielfältig eingesetzt werden:

    <ul>
        <li>Klassische Feinstrukturierung</li>
        <li>Reflektionseigenschaften</li>
        <li>Farbe</li>
        <li>Normalenvektoren (Bump- oder Normal mapping)</li>
        <li>Beleuchtung
        <ul>
            <li>Environment Mapping, Reflection Mapping</li>
            <li>Shadow Mapping, Light Mapping</li>
        </ul>
        </li>
        <li>Geometrie (Displacement Mapping)</li>
    </ul>

    Texturkoordinaten werden üblicherweise mit \((s, t)\) bezeichnet. Manchmal
    auch mit \((u, v)\).
    </dd>
</dl>


#### Räumliche Datenstrukturen

Slide: `05_ Raumliche Datenstrukturen.pdf` (10.12.2015)

* Hüllkörper
  * Axis-Aligned Bounding Boxes (AABB)
  * Bounding Volume Hierachies (BVH)
* Reguläre Gitter
* Oktalbaum (Octree)
* kD-Baum

<dl>
  <dt><dfn>BSP-Baum</dfn></dt>
  <dd>TODO</dd>
  <dt><dfn>Surface Area Heuristics</dfn> (<dfn>SAH</dfn>)</dt>
  <dd>Schätzfunktion für die Oberfläche eines Objekts (TODO?).</dd>
</dl>


#### Rasterisierung, Clipping und Projektionstransformationen

Side: `06_ Rasterisierung, Clipping und Projektionstransformationen.pdf`

* Tiefenpuffer, Z-Buffer
* Clipping
* Sutherland-Hodgeman Polygon Clipping


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


#### Blatt 6

* [glm::gtx::transform](http://glm.g-truc.net/0.9.0/api/a00192.html)


## Material und Links

* [Vorlesungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/index.php)
* [&Uuml;bungswebsite](http://cg.ivd.kit.edu/lehre/ws2015/cg/uebung.php)
* [E-Mail Verteiler](https://lists.ira.uni-karlsruhe.de/mailman/listinfo/cg.cg)

Siehe auch

* [World, View and Projection Transformation Matrices](http://www.codinglabs.net/article_world_view_projection_matrix.aspx)
* [How to calculate transformation matrix](http://stackoverflow.com/questions/18019968/how-to-calculate-transformation-matrix)
* OpenGL [Tutorial 3 : Matrices](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/)


## Literatur

* P. Shirley, S. Marschner: Fundamentals of Computer Graphics, 3rd Edition<br/>
  → Kapitel 3-9, Kapitel 11-12 (Data Structures for Graphics)


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
