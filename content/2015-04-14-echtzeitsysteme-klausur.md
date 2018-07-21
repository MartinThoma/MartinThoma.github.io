---
layout: post
title: Echtzeitsysteme - Klausur
author: Martin Thoma
date: 2015-04-14 20:43
category: German posts
tags: Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Echtzeitsysteme&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://rob.ipr.kit.edu/mitarbeiter_96.php">Herrn Prof. Dr. Wörn</a> im Sommersemester 2015 gehört.</div>

## Behandelter Stoff

### Vorlesung

Der Dozent verwendete einige Abkürzungen, die mir nicht geläufig waren. Diese
habe ich unter anderem in der folgenden Tabelle aufgeführt.

<table>
<tr>
    <th>Datum</th>
    <th style="width:60px;">Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>14.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-1 - ES1-24)</td>
    <td><a href="https://de.wikipedia.org/wiki/Speicherprogrammierbare_Steuerung"><abbr title="Speicherprogrammierbare Steuerung">SPS</abbr></a>; NC; RC; <a href="https://de.wikipedia.org/wiki/Daisy_Chain">Daisy chain</a>; Mikroprozessor vs. Mikrorechner vs. Mikrorechnersystem; Aufbau eines Mikroprozessors; Speicherhierachie (L1-, L2- und L3-Cache, Hauptspeicher, Festplatte); superskalare Pipeline; Fixed-
priority-preemptive Unterbrechungsbehandlung</td>
</tr>
<tr>
    <td>15.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-25 - ES1-60)</td>
    <td>Watchdogs, <a href="http://de.wikipedia.org/wiki/Jitter">Jitter</a>, <a href="http://de.wikipedia.org/wiki/Speicherdirektzugriff">DMA</a>, <a href="http://de.wikipedia.org/wiki/Digitaler_Signalprozessor">Signalprozessor</a>, <abbr title="Very long instruction word">VLIW</abbr>; verschiedene Bus-Arten (z.B. PCI-Bus), Bus-Arbitation kümmert sich bei mehreren Bus-Mastern um die Zugriffskontrolle. Das kann zentral oder dezentral (z.B. über eine Daisy-Chain oder einen Identifikationsbus) geschehen; </td>
</tr>
<tr>
    <td>21.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-62 - ES1-83)</td>
    <td>Arbitrierung; Transaktionen</td>
</tr>
<tr>
    <td>22.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=423230&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Kapitel 2</a> (ES2-1 - ES2-?)</td>
    <td><a href="https://de.wikipedia.org/wiki/Ohmsches_Gesetz#Beschreibung">Ohmsches Gesetz</a>; Parallel- und Reihenschaltung von Widerständen; Spannungsteiler; <a href="https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln#Der_Knotenpunktsatz_.28Knotenregel.29_.E2.80.93_1._Kirchhoffsches_Gesetz">Knotenregel</a>; <a href="https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln#Der_Maschensatz_.28Maschenregel.29_.E2.80.93_2._Kirchhoffsches_Gesetz">Maschenregel</a>; Transistoren; Addierer; Differenzierer; Invertierter Addierer; Integrierer; AD/DA-Wandler</td>
</tr>
<tr>
    <td>28.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=423230&amp;cmd=sendfile&amp;cmdClass=ilrepositorygui&amp;cmdNode=ed&amp;baseClass=ilRepositoryGUI">Kapitel 2</a> (?)</td>
    <td>?</td>
</tr>
<tr>
    <td>12.05.2015</td>
    <td>?</td>
    <td>Hurwitz-Kriterium; Ortskurve; P-, Pi- und PID-Regler (I: Rück-Knala, D: Änderung); Vorsteuerung, Car Cruise Control</td>
</tr>
<tr>
    <td>19.05.2015</td>
    <td>2. Übung</td>
    <td>Operationsverstärker, AD-Wandler</td>
</tr>
<tr>
    <td>20.05.2015</td>
    <td>?</td>
    <td>?</td>
</tr>
<tr>
    <td>26.05.2015</td>
    <td>3. Übung</td>
    <td>Mit Jessica Hutzl</td>
</tr>
<tr>
    <td>27.05.2015</td>
    <td>Kapitel 4 (- ES 4-43)</td>
    <td>ISO/OSI-Modell, Profibus, CAN-Bus, INTERBUS</td>
</tr>
<tr>
    <td>02.06.2015</td>
    <td>Kapitel 4, 5 (ES 4-44 - 5-16)</td>
    <td>Rechtzeitigkeit</td>
</tr>
<tr>
    <td>03.06.2015</td>
    <td>?</td>
    <td>?</td>
</tr>
<tr>
    <td>09.06.2015</td>
    <td>Übung</td>
    <td>Regelung</td>
</tr>
<tr>
    <td>10.06.2015</td>
    <td>Übung</td>
    <td>-</td>
</tr>
</table>

### Abkürzungen

* LLF: Least-Laxity-First-Scheduling
* EDF: Earliest-Deadline-First-Scheduling
* GPS: Guaranteed Percentage Scheduling

### Wichtiges

* Ist eine Übertragungsfunktion in Pol-und-Nullstellenform $G(s)$ stabil?
  → Ja, falls der Realanteil aller Pole negativ ist.
* Ist eine Funktion $G(s)$ stabile?
  → Ja, falls die Nullstellen der Gleichung $G(s)+1=0$ links der $i$-Achse liegen.
* Ist $G(i \omega)$ stabil?
  → Ja, falls die Kurve (-1, 0i) NICHT umfährt (siehe [Nyquistkriterium](https://de.wikipedia.org/wiki/Stabilit%C3%A4tskriterium_von_Nyquist#Spezielles_Nyquistkriterium_.2F_.E2.80.9ELinke-Hand-Regel.E2.80.9C))

#### Hurwitz-Kriterium

Ein System $a_n x^{(n)} + a_{n-1} x^{(n-1)} + \dots + a_1 \dot{x} + a_0 x = 0$ ist dann stabil,
wenn

1. alle Koeffizienten $a_i > 0$ UND
2. alle [Hauptabschnittsdeterminanten](https://de.wikipedia.org/wiki/Minor_(Lineare_Algebra)#Hauptminoren) (auch Hauptminoren genannt) positiv sind.

Insbesondere gilt für $a_2 \cdot \ddot{x} + a_1 \dot{x} + a_0 x = 0$, dass die
Hauptabschnittsdeterminanten von

$$\begin{pmatrix}a_1 & 0\\0 & a_0\end{pmatrix}$$
zu überprüfen sind. Das ist jedoch schon durch das erste Kriterium erfüllt.

Bei $a_3 \cdot x^{(3)} + a_2 \cdot \ddot{x} + a_1 \dot{x} + a_0 x = 0$ ist

$$\begin{pmatrix}a_2 & a_0 & 0\\1 & a_1 & 0\\ 0 & a_2 & 1\end{pmatrix}$$

zu überprüfen, also:

* $a_2 > 0$?
* $a_2 \cdot a_1 - a_0 > 0$? (the determinant of size 2 and 3 is the same)


#### Schaltungen

* Subtrahierer: $U_A = \frac{R_0 (R_1 + R_3)}{R_1 (R_0 + R_2)} \cdot U_2 - \frac{R_3}{R_1} \cdot U_1$
* Invertierender Addierer: $U_A = - \left (\sum_{i=1}^{N-1} \frac{U_i}{R_i} \right ) \cdot R_N$
* Integrierer: $- \frac{1}{RC} \int U_E \mathrm{d}t$
* Differenzierer: $U_A = - R_N \cdot I_E$
* Invertierender OP: $y = - \frac{R_N}{R_1}$
* Nicht-Invertierender OP: $y = \frac{R_N+R_1}{R_1}$
* Parallelverfahren (vgl. ES 2 - 37)


## Typische Klausur

Die Klausuren sind alle sehr ähnlich zu einander:

* Regelung
    * Zeitkonstante Regelung: 7 Punkte
        * Definition Regelung / Steuerung: 1 Punkt
        * Laplace-Bereich / Übergangsfunktion: 1 Punkt
        * Transformationstabelle / Differentialgleichung: 1 Punkt
        * Ist ein gegebenes System stabil? (mit Übergangsfunktion): 1 Punkt
        * PID-Regler / stabilität / Fehler: 2 Punkte
        * Gütegrad von Regelungssystem: 1.5 Punkte
        * Bode-Diagramm: 1.5 Punkte
    * Zeitdiskrete Regelung: 8 Punkte
        * Aliasing / Abtasttheorem: 1 Punkt
        * Z-Transformierte Übertragungsfunktion G(z): 2 Punkte
        * Z-Transformierte / PD-Regelalgorithmus: 1 Punkt
        * Z-Transformierte / Regelkreis: 1 Punkt
        * Differenzialgleichungen → Differenzengleichung: 2 Punkte
        * Digital vs. Kontinuierlich (Diskretisierung): 1 Punkte
        * Stabilität eines Systems: 1 Punkt
* Rechnerarchitekturen / Busse / Operationsverstärker
    * Rechnerarchitekturen und Busse: 10 Punkte
        * Watchdog: 1 Punkt
        * Echtzeitausgabeeinheit (Konzept, Definition, Eigenschaften): 1 Punkt
        * Befehlsskalarer Prozessor / Sprungbedingungen: 1 Punkt
        * Bus-Eigenschaften: 2 Punkte
            * Echtzeitfähig oder nicht
            * Synchron ↔ asynchron
            * Getrennter Adress- und Datenbus ↔ multiplex
            * Burst-Datentransfer erlaubt oder auch nicht
    * Operationsverstärker in Analog- und Digitaltechnik: 8 Punkte
        * Schaltsymbol Operationsverstärker (mit Versorgungsspannung), Anschlüsse
          beschriften: 1 Punkt
        * Eingangsströme (real/ideal): 1 Punkt
        * Operationsverstärker: 4 Punkte
        * Prinzip Operationswandler: 1 Punkt
        * Asymmetrische / differenzielle Datenübertragung: 1 Punkt
        * A/D-Wandler: 2 Punkte
* Echtzeitkommunikation / Programmierung: 7 Punkte
    * ISO / OSI-Schichtenmodell: 1.5 Punkte
    * Manchester-Codierung: 1.5 Punkte
    * Übertragungsfehler: 1.5 Punkte
    * CAN-Dataframes: 2.5 Punkte
    * Zusätzliche Forderungen an Echtzeitsysteme: 1 Punkt
    * FPP-Scheduling: 2 Punkte
    * Periodenabweichung: 2 Punkte
    * Optimales Scheduling: 1 Punkt
    * Schwankungen: 1 Punkt
* Echtzeit-OS / SPS
    * Echtzeit-OS: 7 Punkte
        * Zusätzliche Anforderungen: 1 Punkt
        * Zusätzliche Anforderungen Middleware: 1 Punkt
        * Beispiele: 1 Punkt
        * Sperrsynchronisation: 2 Punkte
        * Seitenadressierung: 2 Punkte
    * SPS: 8 Punkte
        * <abbr title="Funktionspointer">FUP</abbr> → <abbr title="Anweisungsliste">AWL</abbr>: 2.5 Punkte
        * FUP → Structured Text: 2.5 Punkte
        * 3 Verarbeitungsschirtte von SPS im zyklischen Programmbetrieb: 1 Punkt
        * Konventionelle SPS ↔ Soft: 1 Punkt
        * Graphische ↔ textuelle Programmiersprache: 1 Punkt

## Material und Links

* [Vorlesungswebsite](http://www.math.kit.edu/stoch/lehre/wt2015s/de)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_409322.html)
* [Klausur-Musterlösungen](https://github.com/MartinThoma/KIT-Musterloesungen/tree/master/Echtzeitsysteme)
* Meine [Anki-Karten](../anki/Echtzeitsysteme - KIT Wörn 2015.apkg) (bestehend aus Teilen von [Echtzeitsysteme - KIT Wörn](https://ankiweb.net/shared/info/2095784594) und [Echtzeitsysteme KIT Wörn Wissensfragen Klausur](https://ankiweb.net/shared/info/2071108701) sowie weiteren Karten)

StackOverflow:

* [What is the difference between DMA and memory-mapped IO?](http://stackoverflow.com/q/3851677/562769)

## Übungsbetrieb

* Wo sind die Übungsblätter: ? (Ilias?)
* Abgabeform: Keine Abgabe
* Abgabe (wochentag): Keine Abgabe
* Rücknahme: -
* Turnus: ?
* Übungsschein verpflichtend: Es gibt keinen Übungsschein.
* Bonus durch Übungsschein: Es gibt keinen Übungsschein.

## Termine und Klausurablauf

**Datum**: Donnerstag, der 24.09.2015 von 14:00 Uhr-15:00 Uhr ([Quelle](http://www.informatik.kit.edu/klausuren.php?kid=522.35))<br/>
**Ort**: Gehrtsen HS ([Geb. 30.21](https://www.kithub.de/map/2144))<br/>
**Punkte**: 60<br/>
**Punkteverteilung**: 4 Aufgaben à 15 Punkte:

* Regelung
* Rechnerarchitekturen, Busse, Operationsverstärker, Analog-/Digitaltechnik
* Echtzeitkommunikation und Echtzeitprogrammierung
* Echtzeitbetriebssysteme und SPS

**Bestehensgrenze**: ?<br/>
**Übungsschein**: Gibt es nicht.<br/>
**Bonuspunkte**: Gibt es nicht.<br/>
**Ergebnisse**: Die Noten der Klausur werden am Schwarzen Brett im IAR-IPR (Geb. 40.28, Foyer, links) ausgehängt. Noch ist nichts da (Stand: 24.09.2015)<br/>
**Einsicht**: wird über [Ilias](https://ilias.studium.kit.edu/goto_produktiv_fold_450985.html) bekannt gegeben<br/>
**Erlaubte Hilfsmittel**: Keine


## Fazit

Dieses Modul kann man sich getrost schenken. Wenn man vorher nichts von
Regelungstechnik weiß, ist man hinterher auch nicht schlauer. Es scheint so zu
sein, dass die klausurrelevanten Teile alle in den Übungen besprochen werden.

Die bereitgestellten **Materialien** hätten besser sein können. Es gibt zwar
ein Skript welches sogar eine ISBN-Nummer hat, aber insbesondere bei dem
Regelungstechnik-Teil ist es nicht sonderlich hilfreich. Ich hatte das Gefühl,
dass mir da einfach Grundlagen fehlen. Diese werden auch nicht erklärt. Zu den
PDF-Folien muss man sagen, dass diese zwar schnell im Ilias hochgeladen wurden,
aber teilweise zu viele Informationen hatten. Es war nicht klar, was wichtig
ist. Außerdem hat teilweise, wenn man nur die Folien angesehen hat, der
Kontext gefehlt.

Ein **Highlight** waren Videos, in denen Roboter Kugeln auf einem Tablett
sehr schnell transportieren. Dazu müssen die Roboter das Tablett im
richtigen Winkel neigen. Das war ein Highlight der Vorlesung. Schade, dass
nie erklärt wurde wie so etwas berechnet wird.

**Vorwissen** in der Regelungstechnik und bei Differentialgleichungen ist
sicher hilfreich.

Die **Klausurvorbereitung** besteht hauptsächlich aus Auswendiglernen.
Verständnis ist wohl nicht nötig (mal schauen... ich konnte keinen
Notenschlüssel finden.), da die Klausuren immer nahezu identisch aufgebaut
sind.

Meine **Empfehlung** an Studenten ist, in die Übung zu gehen. Da kommen die
klausurrelevanten Sachen. Teilweise 1-zu-1 die gleichen Fragen.

**Verbesserungsvorschläge** für die Dozenten hätte ich auch ein paar:

1. Es sollte Tutorien geben.
2. Es sollte einen verpflichtenden Übungsschein geben. Mit 50% der Punkte hat
   man den Übungsschein, ab 75% gibts Bonuspunkte für die Klausur. Diese
   Übungsblätter werden von den Tutoren korrigiert und besprochen. Wenn die
   Studenten es reihenweise nicht schaffen merkt man schon, wo man die
   Vorlesung verbessern muss.
3. Veröffentlichung der Musterlösungen zu den Klausuren.
4. Anpassung des Skripts, z.B. wurde der VME-Bus durch den PCIe-Bus ersetzt.
5. Anpassung des Modulhandbuchs. Man sollte den Leuten *empfehlen*, zuvor
   die Vorlesung "Betriebssysteme" gehört zu haben.
6. Ein [Wikibook](https://de.wikibooks.org/wiki/Hauptseite) beginnen. Wenn man
   das für jedes Modul machen würde, könnte man auch Abhängigkeiten besser
   sehen und Studenten könnten fehlendes Wissen leichter nachholen. Außerdem
   würde man das Wissen frei verfügbar machen und man könnte die Exzellenz der
   Lehre zeigen, falls man wirklich der Meinung ist die Lehre am KIT sei
   exzellent. Über die Diskussionsseiten könnten Studenten und andere
   weitgehend anonym ihre Fragen stellen und Verbesserungsvorschläge machen.
   Über das Wiki-System könnten freiwillige Helfer insbesondere bei
   zeitaufwendigen Grafiken helfen.