---
layout: post
title: Echtzeitsysteme - Klausur
author: Martin Thoma
date: 2015-04-14 20:43
categories:
- German posts
tags:
- Klausur
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Echtzeitsysteme&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://rob.ipr.kit.edu/mitarbeiter_96.php">Herrn Prof. Dr. Wörn</a> im Sommersemester 2015 gehört. Der Artikel wird bis zur Klausur laufend erweitert.</div>

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
</table>

### Abkürzungen

* LLF: Least-Laxity-First-Scheduling
* EDF: Earliest-Deadline-First-Scheduling


### Meine Fragen

* ES1-14: Was bedeutet das "x4" im "Unterbrechungswerk in der Steuereinheit"?
* ES1-23: Was bedeuten die Schalen?
* ES1-37: Was bedeutet TxD, RxD, AO0, AO1? AO könnte für "Analog Output" stehen.
* ES1-41: Was ist "naives PCI" und warum ist PCI Express 2.0 kein naives PCI?
* ES1-48: Was bedeutet "TW"? Warum sind bei WAIT=1 um "warten" herum die beiden
  Punkte markiert?
* ES1-49: Wofür steht "AS" und "DTACK"?
* ES1-52: Sind "Buszuteilung" und "Bus-Arbitration" synonyme oder verschiedene Verfahren?
* ES1-57
    * Warum kann durch Blocktransfers <a href="http://de.wikipedia.org/wiki/Priorit%C3%A4tsinversion">Prioritätsinversion</a> passieren?
    * Was ist ein Busmonitor?
* ES1-58: Was bedeutet "Kommandoorientiert (Klassifizierung der Bus-Transfers über Kommandos, nicht
Einzel-Signale)"? Wo genau ist der Unterschied?

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
* Meine [Anki-Karten](https://ankiweb.net/shared/info/1877369263) (bestehend aus Teilen von [Echtzeitsysteme - KIT Wörn](https://ankiweb.net/shared/info/2095784594) und [Echtzeitsysteme KIT Wörn Wissensfragen Klausur](https://ankiweb.net/shared/info/2071108701) sowie weiteren Karten)

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
**Ort**: einige Hörsäle<br/>
**Punkte**: 60<br/>
**Punkteverteilung**: 4 Aufgaben à 15 Punkte:

* Regelung
* Rechnerarchitekturen, Busse, Operationsverstärker, Analog-/Digitaltechnik
* Echtzeitkommunikation und Echtzeitprogrammierung
* Echtzeitbetriebssysteme und SPS

**Bestehensgrenze**: ?<br/>
**Übungsschein**: ?<br/>
**Bonuspunkte**: ?<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: ?<br/>
**Erlaubte Hilfsmittel**: ?
