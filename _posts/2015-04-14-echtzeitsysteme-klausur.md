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
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
    <td>14.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&cmd=sendfile&cmdClass=ilrepositorygui&cmdNode=ed&baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-1 - ES1-24)</td>
    <td><a href="https://de.wikipedia.org/wiki/Speicherprogrammierbare_Steuerung"><abbr title="Speicherprogrammierbare Steuerung">SPS</abbr></a>; NC; RC; <a href="https://de.wikipedia.org/wiki/Daisy_Chain">Daisy chain</a>; Mikroprozessor vs. Mikrorechner vs. Mikrorechnersystem; Aufbau eines Mikroprozessors; Speicherhierachie (L1-, L2- und L3-Cache, Hauptspeicher, Festplatte); superskalare Pipeline; Fixed-
priority-preemptive Unterbrechungsbehandlung</td>
</tr>
<tr>
    <td>15.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&cmd=sendfile&cmdClass=ilrepositorygui&cmdNode=ed&baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-25 - ES1-60)</td>
    <td>Watchdogs, <a href="http://de.wikipedia.org/wiki/Jitter">Jitter</a>, <a href="http://de.wikipedia.org/wiki/Speicherdirektzugriff">DMA</a>, <a href="http://de.wikipedia.org/wiki/Digitaler_Signalprozessor">Signalprozessor</a>, <abbr title="Very long instruction word">VLIW</abbr>; verschiedene Bus-Arten (z.B. PCI-Bus), Bus-Arbitation kümmert sich bei mehreren Bus-Mastern um die Zugriffskontrolle. Das kann zentral oder dezentral (z.B. über eine Daisy-Chain oder einen Identifikationsbus) geschehen; </td>
</tr>
<tr>
    <td>21.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=422667&cmd=sendfile&cmdClass=ilrepositorygui&cmdNode=ed&baseClass=ilRepositoryGUI">Kapitel 1</a> (ES1-62 - ES1-83)</td>
    <td>Arbitrierung; Transaktionen</td>
</tr>
<tr>
    <td>22.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=423230&cmd=sendfile&cmdClass=ilrepositorygui&cmdNode=ed&baseClass=ilRepositoryGUI">Kapitel 2</a> (ES2-1 - ES2-?)</td>
    <td><a href="https://de.wikipedia.org/wiki/Ohmsches_Gesetz#Beschreibung">Ohmsches Gesetz</a>; Parallel- und Reihenschaltung von Widerständen; Spannungsteiler; <a href="https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln#Der_Knotenpunktsatz_.28Knotenregel.29_.E2.80.93_1._Kirchhoffsches_Gesetz">Knotenregel</a>; <a href="https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln#Der_Maschensatz_.28Maschenregel.29_.E2.80.93_2._Kirchhoffsches_Gesetz">Maschenregel</a>; Transistoren; Addierer; Differenzierer; Invertierter Addierer; Integrierer; AD/DA-Wandler</td>
</tr>
<tr>
    <td>28.04.2015</td>
    <td><a href="https://ilias.studium.kit.edu/ilias.php?ref_id=423230&cmd=sendfile&cmdClass=ilrepositorygui&cmdNode=ed&baseClass=ilRepositoryGUI">Kapitel 2</a> (?)</td>
    <td>?</td>
</tr>
</table>

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

## Material und Links

* [Vorlesungswebsite](http://www.math.kit.edu/stoch/lehre/wt2015s/de)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_409322.html)
* [Klausur-Musterlösungen](https://github.com/MartinThoma/KIT-Musterloesungen/tree/master/Echtzeitsysteme)

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
