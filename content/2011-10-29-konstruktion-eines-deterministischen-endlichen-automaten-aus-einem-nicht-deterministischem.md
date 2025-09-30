---
layout: post
lang: de
title: Konstruktion eines deterministischen endlichen Automaten aus einem nicht-deterministischem
slug: konstruktion-eines-deterministischen-endlichen-automaten-aus-einem-nicht-deterministischem
author: Martin Thoma
date: 2011-10-29 10:21:43.000000000 +02:00
category: German posts
tags: Computer science, Abstract machine, Theoretical computer science
featured_image: 2011/10/deterministic-finite-state-machine-thumb.png
alias: /potenzmengenkonstruktion/index.html
---
Der nicht-deterministische endliche Automat zu dem regul&auml;rem Ausdruck $(a \cup (ab(b)^\text{*}ba))^\text{*}$ ist folgender:
$Q = \{S, q_1, q_2\}$
$\Sigma = \{a, b\}$
$\delta = \text{siehe Grafik}$
$F = \{S\}$
$NEA = \left( Q, \Sigma, \delta, S, F \right)$

<figure class="aligncenter">
            <a href="../images/2011/10/myFiniteStateMachine1.png"><img src="../images/2011/10/myFiniteStateMachine1.png" alt="Nondeterministic finite-state machine" style="max-width:365px;max-height:119px;" class="size-full wp-image-8141 "/></a>
            <figcaption class="text-center">Nondeterministic finite-state machine</figcaption>
        </figure>

Will man daraus nun den endlichen Automaten konstruieren, l&auml;uft das im Prinzip &uuml;ber eine Potenzmengenkonstruktion.

Zuerst defnieren wir:
$\tilde{S} = E(S) = \{S\}$

Dann erstellen wir folgende Tabelle:
<table style="border:1px solid #000;">
  <tr>
    <th style="border:1px solid #000;">$\tilde{S}$</th>
    <th style="border:1px solid #000;">{S}</th>
  </tr>
  <tr>
    <th style="border:1px solid #000;">a</th>
    <td style="border:1px solid #000;">&nbsp;</td>
  </tr>
  <tr>
    <th style="border:1px solid #000;">b</th>
    <td style="border:1px solid #000;">&nbsp;</td>
  </tr>
</table>

Dann &uuml;berpr&uuml;ft man, welche Zust&auml;nde erreicht werden k&ouml;nnen, wenn man vom jedem Zustand in der Startmenge (hier also nur S) a einliest. Das ist in diesem Fall q1 oder S. Also haben wir eine weitere Zustandsmenge {q1, S}. Diese wird als neue Spalte in unsere Tabelle geschrieben:
<table style="border:1px solid #000;">
  <tr>
    <th style="border:1px solid #000;">$\tilde{S}$</th>
    <th style="border:1px solid #000;">{S}</th>
    <th style="border:1px solid #000;">{q1, S}</th>
  </tr>
  <tr>
    <th style="border:1px solid #000;">a</td>
    <td style="border:1px solid #000;">{q1, S}</td>
    <td style="border:1px solid #000;">&nbsp;</td>
  </tr>
  <tr>
    <th style="border:1px solid #000;">b</th>
    <td style="border:1px solid #000;">&nbsp;</td>
    <td style="border:1px solid #000;">&nbsp;</td>
  </tr>
</table>

Nun geht man also jede Spalte, von links nach rechts durch. F&uuml;r jede Spalte wird jede Zeile, von oben nach unten, &uuml;berpr&uuml;ft. Mit jeder &Uuml;berpr&uuml;fung kann eine neue Zustandsmenge als Spalte hinzukommen.
Die Anzahl der Zeilen ist eine Kopfzeile + die Anzahl der Zeichen im Eingabealphabet.

Am Ende schaut die Tablle wie folgt aus:
<table style="border:1px solid #000;">
  <tr>
    <th style="border:1px solid #000;">$\tilde{S}$</th>
    <th style="border:1px solid #000;">{S}</th>
    <th style="border:1px solid #000;">{q1, S}</th>
    <th style="border:1px solid #000;">$\emptyset$</th>
    <th style="border:1px solid #000;">{q2}</th>
    <th style="border:1px solid #000;">{q1, q2}</th>
  </tr>
  <tr>
    <th style="border:1px solid #000;">a</td>
    <td style="border:1px solid #000;">{q1, S}</td>
    <td style="border:1px solid #000;">{q1, S}</td>
    <td style="border:1px solid #000;">$\emptyset$</td>
    <td style="border:1px solid #000;">$\emptyset$</td>
    <td style="border:1px solid #000;">{S}</td>
  </tr>
  <tr>
    <th style="border:1px solid #000;">b</th>
    <td style="border:1px solid #000;">$\emptyset$</td>
    <td style="border:1px solid #000;">{q2}</td>
    <td style="border:1px solid #000;">$\emptyset$</td>
    <td style="border:1px solid #000;">{q1, q2}</td>
    <td style="border:1px solid #000;">{q1, q2}</td>
  </tr>
</table>

$\tilde{Q} = \{\{S\}, \{q_1, S\}, \{q_2\}, \{q_1, q_2\}\}$
$\tilde{F} = \{\{S\}, \{q_1, S\}\}$

Die &Uuml;bergangsfunktion wurde mit dieser Tabelle schon hinreichend dargestellt. Nun folgt eine Darstellung der deterministischen Variante des nichtdeterministischen Automaten:

<figure class="aligncenter">
            <a href="../images/2011/10/deterministic-fsm.png"><img src="../images/2011/10/deterministic-fsm.png" alt="Deterministic Finite State machine (create from a non-deterministic version)" style="max-width:512px;max-height:196px" class="size-full wp-image-8421"/></a>
            <figcaption class="text-center">Deterministic Finite State machine (create from a non-deterministic version)</figcaption>
        </figure>

<h2>Material</h2>
Die .gv sieht so aus:
```text
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle, label="{S}"] S;
    node [shape = doublecircle, label="{q1, S}"] q1S;

    node [shape = circle, label="{q2}"] q2;
    node [shape = circle, label="{q1, q2}"] q1q2;
    node [shape = circle, label="{}"] T;

    node [shape = point ]; qi
    qi -> S;

    S   -> q1S   [ label = "a" ];
    S   -> T     [ label = "b" ];

    q1S -> q1S   [ label = "a"];
    q1S -> q2    [ label = "b"];

    q2  -> T     [ label = "a"];
    q2  -> q1q2  [ label = "b"];

    q1q2 -> S    [ label = "a"];
    q1q2 -> q1q2 [ label = "b"];

    T -> T       [label = "a, b"];
}
```

Unter Linux kann man mit <a href="http://wiki.ubuntuusers.de/Graphviz">GraphViz</a> mit folgendem Befehl die Datei erstellen:
```bash
dot -Tpng graph.gv -o deterministic-fsm.png
```
