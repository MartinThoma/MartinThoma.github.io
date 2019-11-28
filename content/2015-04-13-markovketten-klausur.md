---
layout: post
title: Markovsche Ketten - Klausur
author: Martin Thoma
date: 2015-04-13 13:42
category: German posts
tags: Klausur, mathematics, lecture-notes
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Markovsche Ketten&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei Herrn <a href="http://www.math.kit.edu/stoch/~klar/de">Dr. Bernhard Klar</a> im Sommersemester 2015 gehört. Aufgrund des sehr guten Skripts wurde dieser Artikel nie richtig begonnen.</div>

## Behandelter Stoff

Es wäre toll, wenn ich von jeder Vorlesung einen Mitschrieb hochladen könnte.
Gibt es Leute, die mir ihren Mitschrieb schicken würden? Einfach an info@martin-thoma.de schicken.

<dl>
    <dt><dfn>Stochastische Matrix</dfn></dt>
    <dd>Sei $S$ eine Menge und $P = (p_{ij})_{i,j \in S}$ eine Matrix. $P$ heißt <i>stochastische Matrix</i>, falls $\forall i,j \in S: p_{i,j} \geq 0$ gilt und $\forall i \in S: \sum_{j \in S} p_{ij} = 1$ gilt.</dd>
    <dt><dfn>Markov-Kette</dfn></dt>
    <dd>Seit $P$ eine stochastische Matrix. Eine Folge $X_0, X_1, X_2, \dots$ von $S$-wertigen Zufallsvariablen heißt homogene Markov-Kette mit <dfn>Übergangsmatrix</dfn> $P$, falls für alle $n \in \mathbb{N}$ und alle Zustände $i_k \in S$ mit $\mathbb{P}(X_0 = i_0, \dots, X_n = i_n) > 0$ gilt
    $$\mathbb{P}(X_{n+1} = i_{n+1} | X_0 = i_0, \dots, X_n = i_n) = \mathbb{P}(X_{n+1} = i_{n+1} | X_n = i_n) = p_{i_n, i_{n+1}}$$
    Die $p_{ij}$ heißen <dfn>Übergangswahrscheinlichkeiten</dfn> und die <dfn>Startverteilung</dfn> $\nu$ der Kette ist definiert durch $\nu(i) = \mathbb{P}(X_0 = i)$ mit $i \in S$.</dd>
    <dt><dfn>Irreduzible Markov-Kette</dfn></dt>
    <dd>Eine Markov-Kette $(X_n)$ beziehungsweise die Übergangsmatrix $P$ heißen irreduziebel, falls $S$ nur aus einer Klasse besteht.</dd>
    <dt><dfn>Recurrenter Zustand</dfn></dt>
    <dd>Ein Zustand $i \in S$ heißt rekurrent, falls $f_{ii}^* = 1$.</dd>
    <dt><dfn>Transienter Zustand</dfn></dt>
    <dd>Ein Zustand $i \in S$ heißt rekurrent, falls $f_{ii}^* \neq 1$.</dd>
</dl>


### Vorlesung

Zur Vorlesung gibt es das Skript "Markov-Ketten" von Frau Prof. Dr. Bäuerle.
(Ich habe eine Version von 2012).

<table>
<tr>
    <th>Datum</th>
    <th>Kapitel</th>
    <th>Inhalt</th>
</tr>
<tr>
<td>13.04.2015</td>
<td>0. Beispiele (<a href="//martin-thoma.com/pdf/markovketten-2015-04-13.pdf">Mitschrieb</a>)</td>
<td>Einführung in Markovketten mit vielen Beispielen (Weg des Betrunkenen, Ehrenfest-Modell, Irrfahrt, Vererbung); absorbierende Zustände; stochastische Matrix</td>
</tr>
<tr>
  <td>16.04.2015</td>
  <td>1. </td>
  <td>Konstruktion von Markov-Ketten</td>
</tr>
<tr>
  <td>20.04.2015</td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>21.04.2015</td>
  <td>3.10 - 4.6 (<a href="//martin-thoma.com/pdf/markovketten-2015-05-21.pdf">Mitschrieb</a>)</td>
  <td>Total-Variationsabstand, $d(\mu, \nu) = \frac{1}{2} \sum_{i \in S} |\mu(i)- \nu(i)|$, Periode, aperiodisch, ein Konvergenzsatz, Kopplungsargument</td>
</tr>
</table>

## Material und Links

### KIT

* [Vorlesungswebsite](http://www.math.kit.edu/stoch/lehre/mk2015s/de)
* [Ilias](https://ilias.studium.kit.edu/goto_produktiv_crs_411041.html)

### Sonstiges

* [Markov Chains](http://setosa.io/blog/2014/07/26/markov-chains/): A very short introduction to markov chains with beautiful visualizations
* [Wahrscheinlichkeitstheorie - Klausur (Info)](https://martin-thoma.com/wt-klausur/)
* [Statistik - Klausur](https://martin-thoma.com/statistik-vorlesung/)
* [Einführung in die Stochastik](https://martin-thoma.com/einfuhrung-in-die-stochastik/)

### Wichtigster Stoff

Wie immer Definitionen (Markovkette, transient, rekurrent, Klasse, irreduzibel)

Wenn man die Matrix so umsortiert, dass rechts unten die rekurrenten Zustände
sind (das ist nicht immer eine Einheitsmatrix!), Dann heißt die Matrix links
oben $Q$ und rechts oben $R$. Dann gilt:

* $(E-Q)^{-1} \cdot R$: Absorptionszeit
* $$(E-Q)^{-1} \cdot \begin{pmatrix}1\\\vdots\\1\end{pmatrix}$$: Schritte bis zur Absorption.
* Invariantes Maß finden: $\pi P = \pi$ bzw. $\pi Q = 0$ im zeitkontinuierlichen Fall

## Übungsbetrieb

Es gibt Dienstags und Mittwochs Tutorien.

* Wo sind die Übungsblätter: [Ilias](https://ilias.studium.kit.edu/goto_produktiv_fold_411044.html)
* Abgabeform: Handgeschrieben (?)
* Abgabe: ?
* Rücknahme: ?
* Turnus: Wöchentlich
* Übungsschein verpflichtend: Nein
* Bonus durch Übungsschein: Nein

## Termine und Klausurablauf

**Datum**: Montag, der 03.08.2015 von 11:00 bis 13:00 Uhr ([Quelle](http://www.math.kit.edu/stoch/lehre/mk2015s/event/mk-klausur/))<br/>
**Ort**: [Daimler-Hörsaal](http://www.kithub.de/map/2086) (Geb. 10.11, [Quelle](http://www.math.kit.edu/stoch/lehre/mk2015s/event/mk-klausur/))<br/>
**Punkte**: 60<br/>
**Punkteverteilung**: 6 Aufgaben mit 9-13 Punkten<br/>
**Bestehensgrenze**: ?<br/>
**Übungsschein**: ?<br/>
**Bonuspunkte**: ?<br/>
**Ergebnisse**: ?<br/>
**Einsicht**: Montag, 19.10.2015, 13:00 Uhr - 13:30 Uhr, Im Raum 2.071, [Mathematikgebäude](https://www.kithub.de/map/2133)<br/>
**Erlaubte Hilfsmittel**: ?
