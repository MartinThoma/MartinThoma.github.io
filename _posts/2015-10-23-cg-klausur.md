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
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Computergrafik&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://cg.ivd.kit.edu/dachsbacher/">Herrn Prof. Dr. Ing. Carsten Dachsbacher</a> im Wintersemester 2015/2016 gehört.</div>

## Behandelter Stoff

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
    <td>Rotes / Rosa Rauschen, Lattice Value Noise, Perlin-Rauschen</td>
</tr>
</table>

## Folien

### Bilder, Farbe, Perzeption

Slide: `01_ Bilder, Farbe, Perzeption - Teil1.pdf`

<dl>
    <dt><dfn>Frame Buffer</dfn></dt>
    <dd>Speichert Bilder zur direkten wiedergabe auf dem Bildschirm.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Dithering_(Bildbearbeitung)"><dfn>Ditherhing</dfn> (<dfn>Fehlerdiffusion</dfn>)</a></dt>
    <dd>Ditherhing ist eine Methode zur Illusion einer größeren Farbtiefe.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Gammakorrektur"><dfn>Gamma-Korrektur</dfn></a></dt>
    <dd>\[I_{\text{out}} = I_{\text{in}}^\gamma\]</dd>
    <dt><dfn>Transferfunktion</dfn></dt>
    <dd>Eine Abbildung \(f\) von Farbwerten auf Helligeit:
        \[f: [0, N] \rightarrow [I_{\text{min}}, I_{\text{max}}]\]
        Diese Abbildung ist abhängig vom Display.</dd>
    <dt><dfn>Dynamikumfang</dfn></dt>
    <dd>Der Dynamikumfang beschreibt den erreichbaren Kontrast eines Wiedergabegrätes (Bildschirm, Beamer):
        \[R_d = \frac{I_{\text{max}} + k}{I_{\text{min}} + k}\]

        \(k\) ist dabei das Umgebungslicht, \(I_{max} / I_{min}\) sind
        Konstanten des Displays und geben die maximale bzw. minimale Helligkeit
        an.</dd>
    <dt><dfn>Gammut</dfn> (<dfn>Farbgammut</dfn>)</dt>
    <dd>Der Gamut eines Monitors entspricht dem Spektrum der darauf
        darstellbaren Farben.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Farbtemperatur"><dfn>Farbtemperatur</dfn></a></dt>
    <dd>Die Farbtemperatur ist ein Maß, um einen jeweiligen Farbeindruck einer
        Lichtquelle zu bestimmen.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Schwarzer_K%C3%B6rper"><dfn>Schwarzkörper</dfn></a>, <dfn>Schwarzkörperstrahlung</dfn></dt>
    <dd>Ein Schwarzkörper ist eine idealisierte thermische Strahlungsquelle.
        Die idealisierung besteht darin, dass der Körper die komplette
        auftretende Strahlung vollständig absorbiert. Gleichzeitig sendet er
        Wärmestrahlung (Schwarzkörperstrahlung) aus, welche nur von seiner
        Temperatur abhängig ist.</dd>
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
    <dt><a href="https://de.wikipedia.org/wiki/Weber-Fechner-Gesetz"><dfn>Weber-Fechner-Gesetz</dfn></a></dt>
    <dd>Das Weber-Fechner-Gesetz macht eine Aussage über die subjektiv
        empfundene Stärke von Sinneseindrücken im Abhängigkeit von der
        Intensität des Helligkeitsunterschiedes:

        \[E = c \cdot \frac{R}{R_0}\]

        wobei \(E\) die empfundene Reizstärke, \(c\) eine Konstante, \(R\) die
        tatsächliche Reizstärke und \(R_0\) eine Referenzreizstärke ist.</dd>
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


### Raytracing

Side: `02_ Raytracing (enthalt Abtastung aus Kapitel 1).pdf`

<dl>
    <dt><dfn>Ray-Tracing</dfn></dt>
    <dd>Ray-Tracing ist ein Verfahren zum Erzeugen Fotorealistischer Bilder.
        Dabei geht man prinzipiell wie folgt vor:

        <ol>
            <li><b>Strahlerzeugung</b>: Für jeden Pixel werden Sichtstrahlen erzeugt</li>
            <li><b>Schnittberechnung</b>: Finde das primitiv (z.B. Dreieck) welches der Strahl schneidet und welches am nächsten zur Kamera ist und vor der Kamera liegt.</li>
            <li><b>Schattierung</b>: Beleuchtungsberechnung (shading)</li>
        </ol></dd>
    <dt><dfn>Phong-Beleuchtungsmodell</dfn></dt>
    <dd>Das Phong-Beleuchtungsmodell besteht aus 3&nbsp;Komponenten:
        <ul>
            <li>Ambiente Beleuchtung: Materialkoeffizient \(k_a\). Ambiente Beleuchtung ist indirekte Beleuchtung, also Licht von anderen Oberflächen</li>
            <li>Diffuse Beleuchtung: Materialkoeffizient \(k_d\). Diffuse Beleuchtung ist die Streuung des Lichts nahe beim "Streupunkt" (nach dem Lambertschen Gesetz).</li>
            <li>Spekulare Beleuchtung: Materialkoeffizient \(k_s\) sowie Phong-Exponent \(n\). Unter spekularer Beleuchtung versteht man direkte Spiegelung der Lichtquelle (imperfekte Spiegelung)</li>
        </ul>

        Das Ergibt folgende Formel für die Intensität \(I\):

       \[I = \overbrace{k_a \cdot I_L}^{\text{ambient}} + \overbrace{k_d \cdot I_L \cdot (N \cdot L)}^{\text{diffus}} + \overbrace{k_s \cdot I_L \cdot (R_L \cdot V)^n}^{\text{spekular}}\]

       hierbei ist \(I_L\) die Lichtintensität, die Richtung die das Licht nimmt \(L\) sowie die Oberflächennormale \(N\) und der Lichtreflektionsvektor \(R_L\). Der Vektor \(R_L\) liegt in der selben Ebene wie \(N\) und \(L\). Es gilt \(R_L = 2N \cdot (N \cdot L) - L\).</dd>
    <dt><dfn>Z-Fighting</dfn></dt>
    <dd>Polygone, welche in der selben Ebene liegen führen zu einem Flackern
        welches der beiden Polygone nun angezeigt wird. Dies kann verhindert
        werden, indem eines der Polygone minimal verschoben wird.</dd>
    <dt><dfn>Tessellation</dfn></dt>
    <dd>Parkettierung, also das Füllen einer Fläche mit Primitiven.</dd>
    <dt><dfn>Distributed Ray Tracing</dfn></dt>
    <dd>Bilder welche mit dem Whitted-Style Ray Tracing Verfahren gerendert
        wurden sehen zu perfekt aus. Die perfekte Spiegelung und Trasmission,
        die harten Schattenkanten und die unendliche Schärfentiefe kennen wir
        von realen Kameras so nicht.

        Distributed Ray Tracing ist eine alternative zu Whitted-Style Ray
        Tracing, welche diese Probleme zu lösen versucht. Dabei wird bei jeder
        Spiegelung nicht ein Schattenstrahl verschickt, sondern viele welche
        sich um den "Perfekten" Strahl konzentrieren.</dd>
</dl>

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


Übungsfolien: `01_ Rasterisierung.pdf`

* Rasterisierung von Linien
    * Brute-Force
    * Inkrementelle Berechnung
    * Bresenham Algorithmus
* Rasterisierung von Polygonen
* Sichtbarkeitsproblem
    * Maler-Algorithmus (Painters algorithm)
        * Vorgehen: Sortiere Dreiecke von hinten nach vorne und zeichne sie so.
        * Probleme: Abstandsmaß / Zyklen


Übungsfolien: `07_ Distributed Raytracing.pdf`

Hier sind eigentlich nur schöne Bilder. Ohne Kontext bringt der Foliensatz nichts :-/

* Distributed Raytracing kann Tiefenunschärfe, weiche Schatten und indirekte
  Beleuchtung.
* Monte Carlo Integration
* Pathtracing
* Many-Lights Method
* Voxel Cone Tracing
* Radiance Caches
* Finite Elemente / Radiosity


### Transformationen und homogene Koordinaten

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

<ul>
    <li>Transformationen werden grundsätzlich so dargestellt: \[x' \gets M \cdot x\]

        Es wird also der zu transformierende Vektor von rechts mit der
        Transformationsmatrix \(M\) multipliziert.</li>
    <li>Spiegelung an der \(y\)-Achse ist eine Multiplikation der \(x\)-Koordinaten mit (-1)</li>
    <li>Hierarchisches Modellieren, Szenengraph</li>
</ul>

Übungsfolien: `02_ Bildoperationen.pdf`

<dl>
    <dt><dfn>Filter</dfn> (<dfn>Bildfilter</dfn>)</dt>
    <dd>Ein Bildfilter ist ein Algorithmus, welcher als Input ein Bild bekommt
        und als Output ein Bild liefert.

        Typischerweise werden lineare Filter verwendet.

        Beispiele:

        <ul>
            <li>Helligkeitsänderung</li>
            <li>Kontraständerung (z.B. unschärfe (blur), schärfen (sharpen))</li>
            <li>Desaturierung</li>
            <li>Kantendetektion</li>
        </ul></dd>
    <dt><dfn>Linearer Filter</dfn></dt>
    <dd>Gewichtete Summe benachbarter Pixel-Werte.

        Siehe <b><a href="https://martin-thoma.com/graphic-filters/">Interaktives Beispiel</a></b></dd>
    <dt><dfn>Morphologische Filter</dfn></dt>
    <dd>Strukturverändernde Operation (z.B. Dilatation, Erosion, Öffnung, Schließung)</dd>
</dl>


### Texturen

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

    Eine Textur ist im Einheitsquadrat.

    Eine Textur kann folgendermaßen auf ein Objekt gemappt werden, indem das
    Objekt in einen Hilfskörper (z.B. Kugel, Würfel, Zylinder) gesteckt wird,
    auf welchen die Textur bereits gemappt wurde. Dann kann die Textur
    folgendermaßen auf das Objekt übertragen werden:

    <ul>
        <li>Normale des Hilfskörpers auf das Objekt</li>
        <li>Normale des Objekts auf den Hilfskörper</li>
        <li>Linie durch den Mittelpunkt des Objekts auf den Hilfskörper</li>
    </ul>
    </dd>
    <dt><dfn>Environment Map</dfn></dt>
    <dd>Eine Environment-Map ist eine Textur zur Darstellung der Umgebung.

        Bei Einvironment-Maps nimmt man an, dass der Betrachter weit genug von
        der Umgebung entfernt ist, sodass die Position keine Rolle spielt und
        ausschließlich die Blickrichtung wichtig ist.

        Übliche Parametrisierungen von Environment-Maps sind:
        <ul>
            <li>Cube Maps
            <ul>
                <li>+ ist bei korrekter Filterung nahtlos</li>
                <li>+ keine Singularität am Rand</li>
            </ul>
            </li>
            <li>Sphere Maps
            <ul>
                <li>- Singularität am Rand</li>
                <li>+ mit Kamera, Chromkugel und Photoshop kann sie recht
                 einfach aufgenommen / erstellt werden</li>
            </ul>
            </li>
            <li>LatLong-Map
            <ul>
                <li>- die Pole werden ungleichmäßig abgetastet</li>
            </ul>
            </li>
        </ul>

        Eine Anwendung war der "flüssige" Terminator im Hubschrauber (Terminator 2).
    </dd>
    <dt><dfn>Cube Map</dfn></dt>
    <dd>Um den Hintergrund darzustellen, kann man die Szene in einen von
        innen texturierten Cubus stecken. Ein Reflektionsrichtung \(\mathbf{r} = (r_x, r_y, r_z)\)
        bestimmt den Punkt auf dem Mantel des Würfels.

        Die betragsmäßig größte Komponente von \(\mathbf{r}\) bestimmt, welche
        Würfelfläche (links, rechts, vorne, hinten, oben, unten) genommen wird.

        Abhängig von der orientierung des koordinatensystems in bezug auf die
        Cube map kann sich dann also folgende Regel ergeben:
        <ul>
            <li>Wenn \(|r_x|\) am größten ist, ist es rechts (&lt; 0) oder links (&gt; 0),</li>
            <li>wenn \(|r_y|\) am größten ist, ist es vorne (&lt; 0) oder hinten (&gt; 0)</li>
            <li>wenn \(|r_z|\) am größten ist, ist es oben (&lt; 0) oder unten (&gt; 0)</li>
        </ul>

        Die Texturkoordinaten \((s, t)\) werden z.B. für (right) wie folgt erechnet:

        \[s = \frac{r_y}{2 \cdot  r_x}, \;\;\; t = \frac{r_z}{2 \cdot  r_x}\]
        </dd>
    <dt><dfn>Mip-Map</dfn> (<dfn>Mip map</dfn>, <dfn>Mipmap</dfn>, <dfn>Auflösungspyramide</dfn>)</dt>
    <dd>Mip steht für lat. <i>multum in parvo</i> (viel in wenig). Eine
        Mip-Map ist eine Vorfilterung von Texturen. Mip-Mapping hilft, wenn man
        in einem sehr flachem Winkel auf eine Ebene blickt.


        In einer Mip-Map wird die Original-Textur gespeichert, dann in der
        ersten Stufe eine Textur welche in beiden Dimensionen auf die hälfte
        verkleinert wurde (also 1/4 der ursprünglichen Größe).

        Es wird diejenige Mip-Map Stufe \(n\) gewählt, sodass gilt

        \[\text{Texelgröße}(n) \leq \text{Größe Pixelfootprint auf Textur} < Texelgröße(n+1)\]

        Dann wird eine Trilineare Interpolation der 8 nächsten Texel durchgeführt:
        <ul>
            <li>Bilinear auf Stufe \(n\), bilinear auf Stufe \(n+1\)</li>
            <li>linear zwischen diesen beiden Farben</li>
        </ul>

        Mip-Maps benötigen zusätzlich 1/3 der ursprünglichen Texturgröße.
        </dd>
    <dt><dfn>Isotrope Texturfilterung</dfn></dt>
    <dd>Eine Texturfilterung heißt isotrop, wenn sie in alle Richtungen
        gleich ist.

        Anisotrope Texturfilterungen sind gewünscht, weil sie in die Tiefe
        schärfe erhalten können, wohingegen isotrope Texturfilterung in die
        ferne unscharf wirken können. RIPmaps sind anisotrope
        Texturfilterungen.</dd>
</dl>

Übungsfolien: `04_ Texturen und Transformationen.pdf`

<dl>
    <dt><dfn>Limitationen von Whitted-Style Raytracing</dfn></dt>
    <dd><ul>
        <li>Keine Kaustiken oder korrekte Dispersion</li>
        <li>Keine indirekte Beleuchtung</li>
        <li>Keine Flächenlichtquellen</li>
        <li>Kein Motion-Blur oder Tiefenunschärfe</li>
    </ul>

    Mögliche Lösung: Distributed Raytracing</dd>
    <dt><dfn>Stratified Supersampling</dfn></dt>
    <dd>Strahlen werden durch zufällige Superpixelpositionen geschossen,
        aber möglichst gleichmäßig um Klumpen zu vermeiden.</dd>
</dl>

* Transformationen
* Texturen
    * Repeating / Clamping
    * Bilineare Filterung
    * Aliasing bei Verkleinerung
        * Lösung: Überabtastung oder Vorfilterung (z.B. Mip-Maps)
    * Mip-Maps
        * Auswahl der richtigen Texturgröße


### Räumliche Datenstrukturen

Slide: `05_ Raumliche Datenstrukturen.pdf` (10.12.2015)

<dl>
    <dt><dfn>Räumliche Datenstrukturen</dfn></dt>
    <dd>

    <ul>
        <li>Hüllkörper
        <ul>
            <li>Axis-Aligned Bounding Boxes (AABB)</li>
            <li>Bounding Volume Hierachies (BVH)</li>
        </ul>
        </li>
        <li>Reguläre Gitter</li>
        <li>Oktalbaum (Octree)</li>
        <li>kD-Baum</li>
    </ul>

    </dd>
    <dt><dfn>AABB</dfn> (<dfn>Axis-Aligned Bounding Box</dfn>)</dt>
    <dd>Axis-Aligned Bounding Boxes sind Rechtecke (Quader in 3D), deren Seiten
        parallel zu den Achsen des Koordinatensystems stehen. Sie werden als
        Hüllkörper verwendet.

        Alles wichtige zu AABBs kann man in Folie 18 - 29 nachlesen.</dd>
    <dt><dfn>BSP-Baum</dfn> (<dfn>Binary Space Partition Baum</dfn>)</dt>
    <dd>Teile den Raum mithilfe von Ebenen in zwei Teile. Die Ebenen dürfen
        beliebig im Raum liegen.

        Somit wird eine Baumstruktur aufgebaut, welche den Raum in immer
        kleinere Teile teilt.</dd>
    <dt><a href="https://en.wikipedia.org/wiki/K-d_tree" name="kd-tree"><dfn>kD-Baum</dfn></a></dt>
    <dd>Ein BSP-Baum, welcher nur achsenparallele Ebenen erlaubt.
        Der Raum wird also mit achsenparallelen Hyperebenen geteilt; es
        entsteht ein Binärbaum welcher den Raum partitioniert.</dd>
    <dt><dfn>Surface Area Heuristic</dfn> (<dfn>SAH</dfn>)</dt>
    <dd>Wähle die Split-Ebene so, dass die Kosten der Traversierung minimiert
        werden.</dd>
    <dt><dfn>Bounding-Volume-Hierachies</dfn> (<dfn>BVH</dfn>)</dt>
    <dd>BVHs sind eine Datenstruktur, welche den Raum in Hüllkörper unterteilt.
        Man hat also komplexe Objekte. Für diese Objekte muss man Schnittests
        machen. Das bedeutet im einfachsten Fall, dass man für \(n\) Dreiecke
        und einen Strahl genau \(n\) Schnittests machen muss.

        Interessanterweise dürfen sich Hüllkörper überlappen.

        Nun könnte man aber - je nach den Objekten - diese in jeweils zwei
        Quader unterteilen. Wenn der Strahl nur einen Quader schneidet, dann muss
        man auch nur für die Objekte in diesem Quader Schnittests durchführen.
        Innerhalb des Quaders kann man natürlich noch weiter die Objekte in
        Hüllkörper (üblicherweise Quader) unterteilen.

        Typische Hüllkörper sind:

        <ul>
            <li>AABB: Axis-Aligned Bounding Boxes</li>
            <li>Bounding Spheres</li>
            <li>OBB: Oriented Bounding Boxes</li>
            <li>Slabs: Schnitt von Paaren paralleler Halbebenen</li>
        </ul></dd>
    <dd>Die SAH ist ein Kriterium zum aufbau von BVHs / kD-Bäumen.

        Im Mittel sollen zufällige Strahlen, die den betrachteten Knoten
        schneiden, den gleichen Aufwand verursachen, egal welcher Kindknoten
        traversiert wird</dd>
    <dt><dfn>Oktalbäume</dfn> (<a href="https://en.wikipedia.org/wiki/Octree"><dfn>Octree</dfn></a>)</dt>
    <dt><dfn>Gitter</dfn></dt>
    <dd>Schnitttests können beschleunigt werden, indem über den Raum ein
        Gitter gelegt wird. Der Raum wird also in kleinere Teile zerlegt.

        </dd>
    <dd>Ein Octree unterteilt einen Quader in 8 kleiner Quader. Diese können
        wiederum in 8 kleinere Quader unterteilt werden.</dd>
    <dt><dfn>Mailboxing</dfn></dt>
    <dd>Speichern des Ergebnisses eines Schnitttests mit einem Objekt, um
        erneute Schnitttests zu verhindern.</dd>
</dl>


Übungsfolien: `05_ BVH.pdf`

* Median-Split: Die Entscheidung wird anhand der Mittelpunkte der AABBs getroffen.


### Rasterisierung, Clipping und Projektionstransformationen

Side: `06_ Rasterisierung, Clipping und Projektionstransformationen.pdf`

<dl>
    <dt><dfn>Tiefenpuffer</dfn> (<dfn>Z-Buffer</dfn>)</dt>
    <dd>Es wird ein Bild gespeichert, welches für jeden Pixel die Tiefe
        des vordersten Objekts angibt.</dd>
    <dt><dfn>Tiefentest</dfn></dt>
    <dd>Finden des Bildteiles, der für einen gegebenen Pixel am nächsten vor
        der Kamera ist.</dd>
    <dt><dfn>Clipping</dfn></dt>
    <dd>Abschneiden von Linien und Poligonen, die außerhalb des sichtbaren
        Bereichs liegen. Dies ist wichtig für die behandlung problematischer
        Fälle bei Projektionen.</dd>
    <dt><dfn>Algorithmus von Sutherland-Hodgeman</dfn></dt>
    <dd>Dient dem Clipping von Polygonen.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Frustum"><dfn>Frustum</dfn></a></dt>
    <dd>Ein Frustum ist ein Kegelstumpf, wobei in der Computergrafik eher ein
        Pyramidenstumpf gemeint ist. Das <i>View Frustum</i> ist der Bereich
        der Szene, der sichtbar ist.</dd>
    <dt><dfn>Outcodes</dfn></dt>
    <dd>Outcodes sind ein 4-Bit binärcode für die Bereiche um die Zeichenebene:
        \[(x < x_{\text{min}}, x > x_{\text{max}}, y < y_{\text{min}}, y > y_{\text{max}})\]
    </dd>
</dl>

Übungsfolien: `09_ Clipping.pdf`

<dl>
    <dt>Clipping von Linien</dt>
    <dd>Ein Rechteck \((x_{\text{min}}, x_{\text{max}}, y_{\text{min}}, y_{\text{max}})\)
        und eine Linie \(P_1 = (x_1, y_1), P_2 = (x_2, y_2)\) ist gegeben.

        Es gibt den "trivial reject" Fall, bei dem die komplette Linie
        außerhalb liegt und den "trivial accept" Fall, bei dem die komplette
        Linie innerhalb des Rechtecks liegt.</dd>
    <dt><dfn>Cohen-Sutherland Algorithmus</dfn></dt>
    <dd>Der Cohen-Sutherland Algorithmus dient dem Clipping von Linien mit
        einem Rechteck.

        Man unterteilt die Ebene, in der das Rechteck liegt in 9 Bereiche:
        (links oben, links mitte, links unten, mitte oben, mitte mitte,...).
        Die Punkte bekommen nun jeweils einen "Outcode" der ihre Position
        bzgl. dieser Bereiche bestimmt:

        \[\text{Outcode} = (x < x_{\text{min}}, x > x_{\text{max}}, y < y_{\text{min}}, y > y_{\text{max}})\]

        Mit den Outcodes gilt nun:

        <ul>
            <li>Trivial Accept: Outcode(\(P_1\)) \(\lor\) Outcode(\(P_2\)) = 0</li>
            <li>Trivial Reject: Outcode(\(P_1\)) \(\land\) Outcode(\(P_2\)) \(\neq\) 0</li>
        </ul>

        Interessant ist, dass in den nicht-trivialen Fällen zwar immer ein Teil
        der Strecke außerhalb des Rechtecks liegt, aber nicht unbedingt auch
        ein Teil innerhalb des Rechtecks liegen muss.</dd>
    <dt><dfn>\(\alpha\)-Clipping</dfn></dt>
    <dd>Führe Window Edge Coordinates (WEC) ein. Diese sind ein
        vorzeichenbehafteter Abstand zu den Clipping-Kanten. Wenn eine
        Koordinate negativ ist, dann liegt der Punkt außerhalb des
        Rechtecks.

        Ich habe den Algorithmus in <a href="https://github.com/MartinThoma/algorithms/blob/master/alpha-clipping/main.py#L146">Python-Pseudocode</a> geschrieben.</dd>
    <dt><dfn>Sutherland-Hodgeman Polygon Clipping</dfn></dt>
    <dd>Clipping wird Kante für Kante durchgeführt.</dd>
</dl>


### OpenGL

Slides: `07_ OpenGL (freiwilliges Bonusmaterial).pdf`, `07_ OpenGL (Teil 1).pdf`, `07_ OpenGL (Teil 2 und 3).pdf`

<dl>
    <dt><dfn>GL</dfn></dt>
    <dd>Short for "Graphics Library"</dd>
    <dt><a href="https://en.wikipedia.org/wiki/OpenGL_Utility_Toolkit"><dfn>GLUT</dfn></a></dt>
    <dd>OpenGL Utility Toolkit: Window manipulation, mouse and keyboard interactions.</dd>
    <dt><dfn>Shading</dfn></dt>
    <dd>
        <ul>
            <li>Flat shading:
                \[\begin{align}
        n &= \langle x_1-x_2, x_3-x_2\rangle\\
        f &= \langle n , L \rangle^+ \cdot (\lambda_1 c_1 + \lambda_2 c_2 + \lambda_3 c_3)
        \end{align}\]</li>
            <li>Gouraud-Shading
                \[\begin{align}
        c'_i &= c_i \langle n_i, L \rangle^+\\
        f &= \lambda_1 c'_1 + \lambda_2 c'_2 + \lambda_3 c'_3
        \end{align}\]</li>
            <li>Phong-Shading
                \[\begin{align}
        n &= \lambda_1 n_1 + \lambda_2 n_2 + \lambda_3 n_3\\
        f &=\langle n , L \rangle^+ \cdot (\lambda_1 c_1 + \lambda_2 c_2 + \lambda_3 c_3)
        \end{align}\]</li>
        </ul>


    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Gouraud_Shading"><dfn>Gouraud Shading</dfn></a></dt>
    <dd>Berechne Parameter wie z.B. Farbe an den Eckpunkten; interpoliere
        innerhalb des Polygons.</dd>
    <dt><dfn><a href="https://de.wikipedia.org/wiki/Phong_Shading">Phong Shading</a></dfn></dt>
    <dd>Beleuchtungsberechnung mit interpolierter Normalen.

        <span style="color: red; font-weight: bold;">Phong-Shading hat mit dem Phong-Beleuchtungsmodell inhaltlich nichts
        zu tun.</span></dd>
    <dt><dfn>Backface Culling</dfn></dt>
    <dd>Dreiecke, auf deren Rückseite man blickt werden üblicherweise nicht
        gezeichnet. (<code>glEnable(GL_CULL_FACE); glCullFace(GL_BACK);</code>)</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Stencilbuffer"><dfn>Stencil-Puffer</dfn></a></dt>
    <dd>Ein Stencil-Puffer ist eine Stanzmaske, welche für jeden Pixel im
        Framebuffer einen 8-bit Wert speichert. Im einfachsten Fall begrenzt
        der Stencil-Puffer das Renderinggebiet.</dd>
</dl>

In order to use GLUT, you need to include:

```c
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
```


OpenGL-Funktionen:

<ul>
    <li><code>gluLookAt</code></li>
    <li><code>glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT )</code></li>
</ul>


Keyword in Shadern:

<ul>
    <li><code>in</code>: Input-Variable</li>
    <li><code>out</code>: Output-Variable</li>
    <li><code>uniform</code>: Bei jedem Shader-Aufruf gleich (also insbesondere für jeden Vertex gleich); read-only; z.B. Transformationsmatrix</li>
    <li><code>attribute</code>: Attribut eines Vertex; nur für Vertex-Shader; z.B. Farbe oder Normale</li>
    <li><code>varying</code>: weitergegebene/interpolierte Werte (schreiben in einem Shader, lesen im darauffolgenden Shader)</li>
</ul>

In Vertex-Shadern:

```cpp
gl_Position = P * V * M * vec4(position, 1.0);
```

Siehe auch:

<ul>
    <li><a href="http://www.glprogramming.com/red/">GLProgramming.com</a></li>
    <li><a href="http://www.opengl.org/registry/doc/glspec45.core.pdf">GL Specs</a></li>
    <li><a href="http://www.opengl.org/registry/doc/GLSLangSpec.4.50.pdf">GLSL Specs</a></li>
</ul>


Übungsfolien: `08_ Shaders.pdf`

<dl>
    <dt><dfn>Rasterisierungspipeline</dfn></dt>
    <dd><ol>
        <li>Geometrie-Verarbeitung</li>
        <li>Rasterisierung</li>
        <li>Pro-Fragment Operationen</li>
    </ol></dd>
    <dt><dfn>Koordinatensystem-Pipeline</dfn></dt>
    <dd><ul>
        <li>Objekt-Koordinaten</li>
        <li>Welt-Koordinaten</li>
        <li>Kamera-Koordinaten</li>
        <li>Clip Space Koordianten</li>
        <li>Normalisierte Geräte-Koordinaten</li>
        <li>Bildschirm-Koordinaten</li>
    </ul></dd>
    <dt><dfn>Vertex-Shader</dfn></dt>
    <dd>Eingabe:
        <ul>
            <li>Position</li>
            <li>Normale</li>
            <li>Farbe oder Texturkoordinate</li>
        </ul>

        Ausgabe:
        <ul>
            <li>Weitergeleitete Vertex-Attribute</li>
            <li>Position nach MVP-Transformation</li>
        </ul>
    </dd>
    <dt><dfn>Fragment-Shader</dfn></dt>
    <dd>Eingabe:
        <ul>
            <li>Interpolierte Vertex-Attribute</li>
            <li>Beleuchtungsinformationen</li>
        </ul>

        Ausgabe:
        <ul>
            <li>Farbe des Fragmentes</li>
        </ul>
    </dd>
    <dt><dfn>Shading</dfn></dt>
    <dd>
        <ul>
            <li>Flat Shading: Beleuchtungsberechnung pro Vertex (oder pro
                Fragment) mit Facetten-Normale</li>
            <li>Gouraud-Shading: Beleuchtungsberechnung pro Vertex mit
                gemittelter Normale der anliegenden Facetten</li>
            <li>Phong-Shading: Shading bzw. Beleuchtungsberechnung pro Fragment
                mit interpolierter Normale</li>
        </ul>
    </dd>
</dl>

* Cube-Maps
* Diffuse Vorfilterung
* Texturzugriffe in GLSL


### Prozedurale Modellierung, Content Creation

Slides: `08_ Prozedurale Modellierung, Content Creation.pdf` am 19.01.2016

<dl>
    <dt><dfn>Rauschfunktion</dfn> (<dfn>Noise-Funktion</dfn>)</dt>
    <dd>Eine Funktion
        \[n: \mathbb{R}^n \rightarrow [a, b] \subsetneq \mathbb{R}\]
        heißt Rauschfunktion, wenn gilt:

        <ul>
            <li><b>Periodenfrei</b>: Eine Rauschfunktion darf keine sichtbare
                Periodizität aufweisen.</li>
            <li><b>Räumliche Korrelation</b>:
                \(n(\mathbf{x}) \approx n(\mathbf{x} + \varepsilon)\)</li>
            <li>definierte Frequenzverteilung, bandlimitiert (Aliasing reduzieren)</li>
        </ul>
     </dd>
    <dt><dfn>Perlin-Rauschen</dfn> (<dfn>Perlin-Noise</dfn>)</dt>
    <dd>Zufallszahlen-Pool + Hash + Permutation</dd>
    <dt><dfn>Oktave</dfn></dt>
    <dd>Sammlung von Rauschfunktionen</dd>
    <dt><dfn>Turbulenzfunktion</dfn></dt>
    <dd>Eine <i>Turbulenzfunktion</i> summiert \(k\) Ergebnisse (Oktave) mehrerer
        Rauschfunktionen auf:

        \[\text{turbulence}(x) = \sum_k \left (\frac{1}{2} \right )^k \cdot n (2^k \cdot x)\]

        Einsatzgebiete:

        <ul>
            <li>Natürliche Oberflächen</li>
            <li>Feuer</li>
        </ul>

        </dd>
    <dt><dfn>Pixelbasierte Textursynthese</dfn></dt>
    <dd>Man hat ein kleines Beispiel (Exemplar) und erzeugt daraus - Pixel für
        Pixel - eine komplette Textur.

        Dieses Verfahren ist langsam.</dd>
    <dt><dfn>Patchbasierte Textursynthese</dfn></dt>
    <dd>Verwende bei der Texturgenerierung nicht nur einzelne Pixel aus dem
        Beispiel, sondern größere Patches.</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Lindenmayer-System"><dfn>Lindenmayer-System</dfn></a> (<dfn>L-System</dfn>)</dt>
    <dd>Ein Lindenmayer-System ist eine Grammatik \(G = (V, \Sigma, \omega, P)\),
        wobei

        <ul>
            <li>\(V \neq \emptyset\) das Alphabet ist,</li>
            <li>\(\Sigma \subseteq V\) die Menge der Konstanten ist,</li>
            <li>\(\omega \in V^*\) das Startwort ist,</li>
            <li>\(P \subseteq (V^* \setminus \Sigma^*) \times V^*\) die Menge der Ersetzungsregeln ist</li>
        </ul>
        </dd>
</dl>

Slides: `08_ Prozedurale Modellierung (freiwilliges Bonus Material).pdf`

<dl>
    <dt><dfn>Turbulenz-Texturen</dfn></dt>
    <dd>z.B. Diamon Square / Midpoint Displacement Algorithmus</dd>
</dl>

* Prozedurale Shader
* Raymarching
* Fraktale / Mandelbrot-Menge
* L-Systeme / D0L-Systeme


### Kurven und Flächen

Slides: `09_ Kurven und Flachen.pdf`


<dl>
    <dt><dfn>Kubische Bézierkurven</dfn></dt>
    <dd>Kubische Bézierkurven sind von der Form
        \[f(u) = (1-u)^3 b_0 + 3u (1-u)^2 b_1 + 3u^2 (1-u) b_2 + u^3 b_3\]
        wobei \(b_0, b_1, b_2 \in \mathbb{R}^n\) und \(u \in [0, 1]\) gilt.

        Diese Faktoren (also \((1-u)^3, 3u (1-u)^2, 3u^2 (1-u), u^3\))
        werden auch Bernstein-Polynome genannt. Genau wie die Monome sind sie
        eine Basis für Polynome.</dd>
    <dt><dfn>Bernstein-Polynome</dfn></dt>
    <dd>\[B_i^n(u) = \binom{n}{i} u^i (1-u)^{n-i}\]</dd>
    <dt><dfn>Béziersplines</dfn></dt>
    <dd>Ein Bézierspline ist eine Liste von Bézierkurven.</dd>
    <dt><dfn>\(C^k\)-stetige Splines</dfn></dt>
    <dd>Es seien
    <div>\[\begin{align}F(u) &= \sum_{i=0}^n B_i^n(u) \mathbf{f}_i\\
                        G(u) &= \sum_{i=0}^n B_i^n(u) \mathbf{g}_i\end{align}\]

    Der Spline aus \(F, G\) heißt

    <ul>
        <li>\(C^0\) stetig \(:\Leftrightarrow F(1) = G(0) \Leftrightarrow \mathbf{f}_n = \mathbf{g}_0\)</li>
        <li>\(C^1\) stetig \(:\Leftrightarrow F'(1) = G'(0) \land C^0 \Leftrightarrow \mathbf{f}_n - f_{n-1} = \mathbf{g}_1 - \mathbf{g}_0 \land C^0\)</li>
        <li>\(C^2\) stetig \(:\Leftrightarrow F''(1) = G''(0) \land C^1 \Leftrightarrow \mathbf{f}_{n-1} + (\mathbf{f}_{n-1} - \mathbf{f}_{n-2}) = \mathbf{g}_{1} + (\mathbf{g}_{1} - \mathbf{g}_{2}) \land C^1\)</li>
    </ul>
    </div>
    </dd>
    <dt><dfn>B-Splines</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Algorithmus von De Casteljau</dfn></dt>
    <dd>Siehe <a href="https://github.com/MartinThoma/algorithms/tree/master/de-casteljau-algorithm">Code</a>.</dd>
</dl>


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
* [Inoffizielle Musterlösungen](https://github.com/MartinThoma/KIT-Musterloesungen) für die Altklausuren

Siehe auch

* [World, View and Projection Transformation Matrices](http://www.codinglabs.net/article_world_view_projection_matrix.aspx)
* [How to calculate transformation matrix](http://stackoverflow.com/questions/18019968/how-to-calculate-transformation-matrix)
* Martin Thoma: [**Interactive Graphic Filters example**](https://martin-thoma.com/html5/graphic-filters/graphic-filters.htm)
* [Interactive Blending example (OpenGL)](http://www.andersriggelsen.dk/glblendfunc.php)
* Martin Thoma: [Minimal OpenGL example](https://github.com/MartinThoma/algorithms/tree/master/OpenGL/color-cube)
* Martin Thoma: [**alpha-cliping pythonic pseudocode**](https://github.com/MartinThoma/algorithms/blob/master/alpha-clipping/main.py#L149)
* [Minimal GLSL example](https://open.gl/drawing)
* [A Primer on Bézier Curves](http://pomax.github.io/bezierinfo/)
* StackExchange:
    * [What is the worst case time complexity for intersection tests with BVHs?](http://cs.stackexchange.com/q/53986/2914)
    * [Ray Tracing vs Rasterization](http://stackoverflow.com/q/15078820/562769)
* Íñigo Quílez: [Raymarching Distance Fields](http://iquilezles.org/www/articles/raymarchingdf/raymarchingdf.htm)

Software

* OpenGL
    * OpenGL [Tutorial 3 : Matrices](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/)
    * [OpenGL Cheat Sheet](http://www.khronos.org/files/opengl45-quick-reference-card.pdf)
    * [glBegin](https://wiki.delphigl.com/index.php/glBegin) / [2](https://www.opengl.org/sdk/docs/man2/xhtml/glBegin.xml)
* [Terragen](http://planetside.co.uk/products/terragen3): Erzeugung von Landschaften
* [xfrog](http://xfrog.com/): Erzeugung von Pflanzen


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


**Ort**:<br/>

<ul>
    <li>A... - Kon...: <a href="https://www.kithub.de/map/2086">Benz-Hörsaal Geb. 10.21</a></li>
    <li>Kop... - Stumpf...: <a href="https://www.kithub.de/map/2086">Daimler-Hörsaal Geb. 10.21</a></li>
    <li>Stumpp... - Z...: <a href="https://www.kithub.de/map/2310">Redtenbacher Hörsaal Geb. 10.91, Raum 050</a></li>
</ul>

**Punkte**: 120<br/>
**Zeit**: 60 min<br/>
**Punkteverteilung**: ?<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: Gibt es. Dieser wird für das Modul, aber nicht für die Klausur benötigt. Mit mindestens 72&nbsp;Punkten (60% von 120 Punkten) hat man den Übungsschein.<br/>
**Bonuspunkte**: Gibt es nicht.<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: Noch nicht bekannt (Stand: 29.03.2016)<br/>
**Erlaubte Hilfsmittel**:

<ul>
    <li>Stift</li>
    <li>Geodreieck</li>
    <li>Zirkel</li>
</ul>
