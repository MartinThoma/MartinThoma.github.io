---
layout: post
status: publish
published: true
title: Konstruktion eines deterministischen endlichen Automaten aus einem nicht-deterministischem
author: Martin Thoma
author_login: moose
author_email: info@martin-thoma.de
author_url: http://www.martin-thoma.com
wordpress_id: 8231
wordpress_url: http://martin-thoma.com/?p=8231
date: 2011-10-29 10:21:43.000000000 +02:00
categories:
- German posts
tags:
- Computer science
- Abstract machine
- Theoretical computer science
comments:
- id: 49421
  author: philipp
  author_email: phlyer89@yahoo.de
  author_url: ''
  date: !binary |-
    MjAxMi0wMi0xOSAxNTozMTozOSArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xOSAxMzozMTozOSArMDEwMA==
  content: ! "Hey,\r\nbin gerade zuf&auml;llig auf Deine Seite gesto&szlig;en. Tolle
    Arbeit.\r\n\r\nEine Frage zu obiger Thematik habe ich: Muss ich bei einem DEA
    nicht noch den sog. \"Junk-Zustand\", der hier durch die leere Menge entsteht,
    einbauen, dass ich f&uuml;r jede m&ouml;gliche Eingabe eine Zuordnung habe? \r\n\r\nFalls
    ich das nicht muss, falsch es trotzdem zu machen ist es deshalb nicht oder?"
- id: 49601
  author: Martin Thoma
  author_email: info@martin-thoma.de
  author_url: http://www.martin-thoma.com
  date: !binary |-
    MjAxMi0wMi0xOSAyMDoyNDozMyArMDEwMA==
  date_gmt: !binary |-
    MjAxMi0wMi0xOSAxODoyNDozMyArMDEwMA==
  content: ! "Hallo Philipp,\r\n\r\nden Junk-Zustand (oder auch Trash-Zustand genannt)
    sollte man hinzuf&uuml;gen. In meinem Beispiel ist das die leere Menge. \r\n\r\nDa
    man von dem Trash-Zustand nur wieder in den Trash-Zustand kommt, hatte ich ihn
    weggelassen. Er wurde also implizit benutzt. Laut GBI soll man bei Endlichen Automaten
    ja jede M&ouml;glichkeit explizit angeben. Im Zustand {q2} k&ouml;nnte noch a
    gelesen werden. Von dort aus w&uuml;rde man im Trash-Zustand landen.\r\n\r\nIn
    der Klausur sollte das unbedingt explizit stehen! Das w&auml;ren verschenkte Punkte!
    \r\n\r\nAlso nochmals:\r\n1. In der Tabelle fehlt ganz rechts eine Spalte, in
    der in jeder Zeile die leere Menge steht\r\n2. In dem Graphen fehlt ein Zustand,
    der mit der leeren Menge bezeichnet wird und aus dem man nicht mehr heraus kommt.\r\n\r\nDanke
    f&uuml;r den Hinweis!\r\n\r\nedit: Ich habe den Artikel nun verbessert, sodass
    es nach der Definition aus GBI korrekt ist."
---
Der nicht-deterministische endliche Automat zu dem regul&auml;rem Ausdruck $(a \cup (ab(b)^\text{*}ba))^\text{*}$ ist folgender:
$Q = \{S, q_1, q_2\}$
$\Sigma = \{a, b\}$
$\delta = \text{siehe Grafik}$
$F = \{S\}$
$NEA = \left( Q, \Sigma, \delta, S, F \right)$

[caption id="attachment_8141" align="aligncenter" width="365" caption="Nondeterministic finite-state machine"]<a href="http://martin-thoma.com/wp-content/uploads/2011/10/myFiniteStateMachine1.png"><img class="size-full wp-image-8141 " title="Nondeterministic finite-state machine" src="http://martin-thoma.com/wp-content/uploads/2011/10/myFiniteStateMachine1.png" alt="Nondeterministic finite-state machine" width="365" height="119" /></a>[/caption]

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

[caption id="attachment_8421" align="aligncenter" width="512" caption="Deterministic Finite State machine (create from a non-deterministic version)"]<a href="http://martin-thoma.com/wp-content/uploads/2011/10/deterministic-fsm.png"><img src="http://martin-thoma.com/wp-content/uploads/2011/10/deterministic-fsm.png" alt="Deterministic Finite State machine (create from a non-deterministic version)" title="Deterministic Finite State machine (create from a non-deterministic version)" width="512" height="196" class="size-full wp-image-8421" /></a>[/caption]

<h2>Material</h2>
Die .gv sieht so aus:
[text]digraph finite_state_machine {
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
}[/text]

Unter Linux kann man mit <a href="http://wiki.ubuntuusers.de/Graphviz">GraphViz</a> mit folgendem Befehl die Datei erstellen:
[bash]dot -Tpng graph.gv -o deterministic-fsm.png[/bash]
